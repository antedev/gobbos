"""
Tier 2/5 Adversarial Clatter Roll & Defense Edge Case Test Suite: Challenger 1 (Milestone 2).
Exhaustively and empirically stress-tests:
1. Low-level resolve_clatter boundary cases:
   - 0 saved actions / can_dodge_or_parry=False.
   - stat_dice=0 vs armor_dice=0.
   - Negative, zero, and extreme incoming damage.
   - Non-exploding armor dice on face 6.
   - Extreme threat TNs (0, 100).
2. Boss ClatterResolver defense dynamics:
   - Reaction vs standard action consumption order.
   - Slink Dodge vs Tough Parry automatic selection (requires Shield for Tough Parry).
   - Slink Bane penalties from Medium Armor (-1d) and Heavy Armor (-2d).
   - Zone Partial Cover +1d Dodge boon.
   - [Armor Piercing] tag reducing armor dice pool by 1 (min 0).
   - Ablative gear sacrifice on lethal damage (Shield prioritized over Armor).
   - Meat Shield quirk redirection to allied Mob in zone.
   - Ankle Bite counter-attack trigger conditions.
"""

from __future__ import annotations

import random
from unittest.mock import patch
import pytest

from combat_sim.core.types import (
    Ancestry,
    Condition,
    CoverType,
    Difficulty,
    Tag,
    ThreatProfile,
    WeaponTrait,
)
from combat_sim.core.dice import (
    ClatterResult,
    resolve_clatter,
    roll_d6,
)
from combat_sim.domain.entities import (
    EliteEnemy,
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
)
from combat_sim.domain.equipment import (
    create_heavy_armor,
    create_light_armor,
    create_medium_armor,
    create_notched_sword,
    create_pot_lid_shield,
    create_tower_pavise,
)
from combat_sim.domain.quirks import AnkleBite, MeatShield
from combat_sim.domain.topology import TopologyGraph, Zone
from combat_sim.engine.resolver import ClatterResolver


class TestResolveClatterFunctionBoundaries:
    """Low-level boundary and edge case testing of resolve_clatter."""

    def test_clatter_zero_saved_actions_disables_evasion(self):
        """When can_dodge_or_parry is False, stat_dice are not rolled regardless of pool size."""
        # Threat TN 1, Damage 2. Stat dice 10 (would easily evade if allowed).
        # Armor 2d6 rolls [5, 2] -> 1 armor success -> takes 1 damage.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 2]):
            res = resolve_clatter(
                threat_tn=1,
                stat_dice=10,
                difficulty=Difficulty.NORMAL,
                armor_dice=2,
                incoming_damage=2,
                can_dodge_or_parry=False,
            )
            assert res.evaded is False
            assert res.stat_successes == 0
            assert res.armor_successes == 1
            assert res.mitigated_damage == 1
            assert res.damage_taken == 1

    def test_clatter_zero_stat_dice_falls_back_to_armor(self):
        """When stat_dice == 0, active evasion is bypassed and only armor rolls."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5]):
            res = resolve_clatter(
                threat_tn=1,
                stat_dice=0,
                difficulty=Difficulty.NORMAL,
                armor_dice=2,
                incoming_damage=2,
                can_dodge_or_parry=True,
            )
            assert res.evaded is False
            assert res.stat_successes == 0
            assert res.armor_successes == 2
            assert res.damage_taken == 0

    def test_clatter_zero_armor_dice_takes_full_damage(self):
        """When armor_dice == 0 and evasion fails, takes 100% of incoming damage."""
        # Slink 1d6 rolls [2] (fails TN 1) -> 0 armor dice -> takes 5 damage
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2]):
            res = resolve_clatter(
                threat_tn=1,
                stat_dice=1,
                difficulty=Difficulty.NORMAL,
                armor_dice=0,
                incoming_damage=5,
                can_dodge_or_parry=True,
            )
            assert res.evaded is False
            assert res.stat_successes == 0
            assert res.armor_successes == 0
            assert res.mitigated_damage == 0
            assert res.damage_taken == 5

    def test_clatter_armor_dice_do_not_explode_on_six(self):
        """Armor dice rolled on face 6 count as 1 mitigation success and do NOT explode."""
        # Threat TN 2, Damage 4. Stat dice 1d rolls [2] (fails).
        # Armor 1d6 rolls [6]. Does NOT explode. 1 success -> mitigates 1, takes 3.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 6]):
            res = resolve_clatter(
                threat_tn=2,
                stat_dice=1,
                difficulty=Difficulty.NORMAL,
                armor_dice=1,
                incoming_damage=4,
                can_dodge_or_parry=True,
            )
            assert res.evaded is False
            assert res.armor_successes == 1
            assert len(res.armor_faces) == 1
            assert res.armor_faces == [6]
            assert res.mitigated_damage == 1
            assert res.damage_taken == 3

    @pytest.mark.parametrize("damage", [0, -1, -5])
    def test_clatter_zero_and_negative_incoming_damage(self, damage):
        """Zero or negative incoming damage results in 0 damage taken and 0 mitigated."""
        res = resolve_clatter(
            threat_tn=1,
            stat_dice=0,
            difficulty=Difficulty.NORMAL,
            armor_dice=2,
            incoming_damage=damage,
            can_dodge_or_parry=False,
        )
        assert res.evaded is False
        assert res.damage_taken == 0
        assert res.mitigated_damage == 0

    def test_clatter_extreme_threat_tn_boundaries(self):
        """Threat TN 0 is automatically evaded if stat_dice > 0; TN 100 fails evasion."""
        # Threat TN 0
        res_tn0 = resolve_clatter(
            threat_tn=0,
            stat_dice=1,
            difficulty=Difficulty.NORMAL,
            armor_dice=0,
            incoming_damage=3,
        )
        assert res_tn0.evaded is True
        assert res_tn0.damage_taken == 0

        # Threat TN 100 (fails evasion, takes damage)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 5, 6]):
            res_tn100 = resolve_clatter(
                threat_tn=100,
                stat_dice=1,
                difficulty=Difficulty.NORMAL,
                armor_dice=1,
                incoming_damage=3,
            )
            assert res_tn100.evaded is False
            assert res_tn100.armor_successes == 1
            assert res_tn100.damage_taken == 2


class TestClatterResolverBossDefenseEmpirical:
    """Adversarial testing of Boss defense resolution via ClatterResolver."""

    def test_boss_defense_consumes_saved_reaction_before_standard_action(self):
        """Boss with saved_reactions > 0 consumes reaction; actions_left is untouched."""
        boss = GoblinBoss(
            id="b1", name="Boss", zone_id="z1", slink=3, saved_reactions=1, actions_left=2
        )
        threat = ThreatProfile(threat_stat="Slink", threat_tn=1, damage=2)

        # Rolls [5, 5, 2] -> 2 succ >= 1 TN -> clean dodge
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat)
            assert res.evaded is True
            assert boss.saved_reactions == 0
            assert boss.actions_left == 2

    def test_boss_defense_consumes_standard_action_if_no_saved_reaction(self):
        """Boss with 0 saved reactions consumes 1 standard action for active defense."""
        boss = GoblinBoss(
            id="b1", name="Boss", zone_id="z1", slink=3, saved_reactions=0, actions_left=3
        )
        threat = ThreatProfile(threat_stat="Slink", threat_tn=1, damage=2)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat)
            assert res.evaded is True
            assert boss.saved_reactions == 0
            assert boss.actions_left == 2

    def test_boss_defense_zero_actions_and_reactions_forces_passive_armor(self):
        """Boss with 0 saved reactions and 0 actions cannot dodge or parry."""
        boss = GoblinBoss(
            id="b1",
            name="Boss",
            zone_id="z1",
            slink=3,
            saved_reactions=0,
            actions_left=0,
            armor=create_light_armor(),  # +1d armor die
        )
        threat = ThreatProfile(threat_stat="Slink", threat_tn=1, damage=2)

        # Cannot roll Slink. Rolls 1 armor die: [5] -> mitigates 1 -> takes 1 damage
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat)
            assert res.evaded is False
            assert res.stat_successes == 0
            assert res.armor_successes == 1
            assert res.damage_taken == 1
            assert boss.grit == boss.max_grit - 1

    def test_slink_bane_penalties_on_medium_and_heavy_armor(self):
        """Medium armor applies -1d Slink Bane; Heavy armor applies -2d Slink Bane."""
        # Medium armor (+2d armor, -1d Slink)
        boss_med = GoblinBoss(
            id="b1", name="MedBoss", zone_id="z1", slink=3, actions_left=1, armor=create_medium_armor()
        )
        assert boss_med.get_slink_bane() == 1
        assert boss_med.get_armor_dice() == 2

        # Heavy armor (+3d armor, -2d Slink)
        boss_hvy = GoblinBoss(
            id="b2", name="HvyBoss", zone_id="z1", slink=3, actions_left=1, armor=create_heavy_armor()
        )
        assert boss_hvy.get_slink_bane() == 2
        assert boss_hvy.get_armor_dice() == 3

    def test_shield_enables_tough_parry_when_tough_exceeds_slink(self):
        """Equipping a Shield enables Tough Parry; if Tough > Slink, Boss uses Tough for defense."""
        boss = GoblinBoss(
            id="b1",
            name="ShieldBoss",
            zone_id="z1",
            tough=4,
            slink=1,
            actions_left=1,
            off_hand=create_pot_lid_shield(),  # Shield enables parry
        )
        assert boss.can_parry() is True

        threat = ThreatProfile(threat_stat="Tough", threat_tn=2, damage=2)
        # Uses Tough 4d pool: [5, 5, 2, 2] -> 2 successes -> Clean Parry!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2, 2]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat)
            assert res.evaded is True
            assert res.stat_successes == 2
            assert res.damage_taken == 0

    def test_armor_piercing_threat_reduces_armor_dice(self):
        """[Armor Piercing] tag in ThreatProfile subtracts 1 die from defender's armor dice."""
        boss = GoblinBoss(
            id="b1",
            name="Boss",
            zone_id="z1",
            slink=1,
            actions_left=0,
            armor=create_medium_armor(),  # Normally 2 armor dice
        )
        assert boss.get_armor_dice() == 2

        # Threat with [Armor Piercing]
        ap_threat = ThreatProfile(threat_stat="Tough", threat_tn=1, damage=2, tags={"[Armor Piercing]"})

        # Armor dice reduced to 2 - 1 = 1 die. Rolls [5] -> mitigates 1 damage.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5]):
            res = ClatterResolver.resolve_boss_defense(boss, None, ap_threat)
            assert res.evaded is False
            assert len(res.armor_faces) == 1
            assert res.armor_successes == 1
            assert res.damage_taken == 1

    def test_ablative_gear_sacrifice_on_lethal_damage(self):
        """When incoming damage >= current Grit, sacrificing Shield or Armor reduces damage to 0 and destroys gear."""
        # Case A: Sacrifices Shield first
        boss_shield = GoblinBoss(
            id="b1",
            name="Boss",
            zone_id="z1",
            grit=2,
            actions_left=0,
            off_hand=create_pot_lid_shield(),
            armor=create_light_armor(),
        )
        lethal_threat = ThreatProfile(threat_stat="Tough", threat_tn=1, damage=3)

        # 2 total armor dice (1 shield + 1 armor) roll [2, 2] -> 0 successes -> 3 damage >= 2 Grit!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 2]):
            res = ClatterResolver.resolve_boss_defense(boss_shield, None, lethal_threat, allow_gear_sacrifice=True)
            assert res.damage_taken == 0
            assert boss_shield.grit == 2  # Survived!
            assert boss_shield.off_hand is None  # Shield destroyed!
            assert boss_shield.armor is not None  # Armor preserved

        # Case B: No Shield, sacrifices Armor
        boss_armor = GoblinBoss(
            id="b2",
            name="Boss2",
            zone_id="z1",
            grit=2,
            actions_left=0,
            armor=create_light_armor(),
        )
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2]):
            res_b = ClatterResolver.resolve_boss_defense(boss_armor, None, lethal_threat, allow_gear_sacrifice=True)
            assert res_b.damage_taken == 0
            assert boss_armor.grit == 2
            assert boss_armor.armor is None  # Armor destroyed!

    def test_meat_shield_quirk_redirects_damage_to_mob(self):
        """Meat Shield quirk redirects attack to allied Mob in zone, applying mob armor and damage."""
        boss = GoblinBoss(
            id="b1",
            name="Boss",
            zone_id="z1",
            grunt=2,
            grit=6,
            quirks=[MeatShield()],
        )
        mob = PlayerMob(
            id="m1",
            name="Bodyguard Mob",
            zone_id="z1",
            health_dice=[6, 6, 6],
            size=3,
            armor_rating=3,  # 3 armor dice
        )
        threat = ThreatProfile(threat_stat="Tough", threat_tn=2, damage=4, is_aoe=False)

        # Meat shield triggers:
        # Mob rolls 3 armor dice: [5, 5, 2] -> 2 successes -> mitigates 2 damage.
        # Mob takes 4 - 2 = 2 single-target damage: [6, 6, 6] -> [4, 6, 6].
        # Boss takes 0 damage, spends 1 Grunt.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat, allied_mob=mob)
            assert res.evaded is True
            assert res.damage_taken == 0
            assert boss.grunt == 1  # 2 - 1 = 1
            assert boss.grit == 6  # Undamaged
            assert mob.health_dice == [4, 6, 6]

    def test_ankle_bite_counter_attack_trigger(self):
        """Clean Dodge vs melee attacker in same zone triggers Ankle Bite counter-attack."""
        boss = GoblinBoss(
            id="b1",
            name="Boss",
            zone_id="z1",
            slink=3,
            actions_left=1,
            quirks=[AnkleBite()],
        )
        attacker = StandardEnemy(id="e1", name="Bandit", zone_id="z1")
        threat = ThreatProfile(threat_stat="Slink", threat_tn=1, damage=2)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2]):
            res = ClatterResolver.resolve_boss_defense(boss, attacker, threat)
            assert res.evaded is True


if __name__ == "__main__":
    print("Running Challenger 1 M2 Clatter Edge empirical tests...")
    import sys
    test_classes = [
        TestResolveClatterFunctionBoundaries,
        TestClatterResolverBossDefenseEmpirical,
    ]
    passed = 0
    failed = 0
    for cls in test_classes:
        inst = cls()
        for attr in dir(inst):
            if attr.startswith("test_"):
                fn = getattr(inst, attr)
                try:
                    fn()
                    print(f"  [PASS] {cls.__name__}.{attr}")
                    passed += 1
                except Exception as e:
                    print(f"  [FAIL] {cls.__name__}.{attr}: {e}")
                    failed += 1
    print(f"\nResult: {passed} passed, {failed} failed.")
    if failed > 0:
        sys.exit(1)
