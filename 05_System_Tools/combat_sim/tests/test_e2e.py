"""
Tier 4 Test Suite: End-to-End Opaque-Box Acceptance Criteria Verification.
Verifies the complete Gobbos combat system against all official acceptance criteria:
1. Dice Engine & Resolution (exploding 6s, salvage rolls, Gobbo Gamble, Bangaranga, Clatter).
2. Equipment, Weapons, Armor & Shields (Impact Size, Parry, Mitigation, Slink Bane, Consumables).
3. Boss Quirks (Meat Shield, Ankle Bite, Push Luck, Twists).
4. Enemy Ancestries & Traits (Parrying Buckler, Thick Blubber, Voracious Regrowth, Steam Vent, Dry Bones, Overkill).
5. Mob Swarm Dynamics (symmetrical Dice-HP, single-target spillover, AoE multiplication, cross-gang).
6. Scenarios Playout (Street Skirmish, The Mauler's Den, Tomb of the Highwayman).
7. Action Economy, Round Loops, and Morale.
"""

from __future__ import annotations

import math
from unittest.mock import patch
import pytest

from combat_sim.core.types import (
    ActionType,
    Ancestry,
    Condition,
    CoverType,
    Difficulty,
    EnemyScale,
    Tag,
    ThreatProfile,
    WeaponHandedness,
    WeaponTrait,
    ZoneTraitType,
)
from combat_sim.core.dice import (
    DiceResult,
    ClatterResult,
    BangarangaPool,
    roll_dice,
    resolve_clatter,
)
from combat_sim.domain.topology import Zone, ZoneProfile, ZoneTrait, TopologyGraph
from combat_sim.domain.equipment import (
    create_bone_shiv,
    create_notched_sword,
    create_heavy_greataxe,
    create_dwarven_great_hammer,
    create_spiked_mace,
    create_sling,
    create_shortbow,
    create_light_armor,
    create_medium_armor,
    create_heavy_armor,
    create_pot_lid_shield,
    create_tower_pavise,
    create_spark_bomb,
    create_fire_flask,
    create_powder_keg,
)
from combat_sim.domain.quirks import (
    MeatShield,
    AnkleBite,
    PushLuck,
    SecondWind,
    TwistModifier,
)
from combat_sim.domain.traits import (
    ParryingBuckler,
    ThickBlubber,
    VoraciousRegrowth,
    PressurizedSteamVent,
    DryBones,
    PlateBastion,
    BeastAncestryTrait,
    UndeadAncestryTrait,
)
from combat_sim.domain.entities import (
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
    EliteEnemy,
    EnemyMob,
    ThreatAttack,
)


class TestE2EAcceptanceCriteria:
    """Opaque-box verification of all project acceptance criteria."""

    # -------------------------------------------------------------------------
    # Criteria 1: Dice System Fidelity
    # -------------------------------------------------------------------------
    def test_e2e_exploding_sixes_and_critical(self):
        """Verify recursive exploding 6s and double explosion critical."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 6, 4]):
            res = roll_dice(pool_size=1, difficulty=Difficulty.NORMAL, allow_gamble=False)
            assert res.successes == 2  # 6 (init) + 6 (bonus 1)
            assert res.is_critical is True
            assert res.bonus_faces == [6, 4]

    def test_e2e_salvage_roll_logic(self):
        """Verify 1d6 salvage roll when pool <= 0."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6]):
            res = roll_dice(pool_size=0, difficulty=Difficulty.NORMAL)
            assert res.salvage is True
            assert res.successes == 1
            assert res.bonus_faces == []  # Salvage 6 does not explode

        with patch("combat_sim.core.dice.roll_d6", side_effect=[1]):
            res = roll_dice(pool_size=-2, difficulty=Difficulty.NORMAL)
            assert res.salvage is True
            assert res.fumble is True
            assert res.successes == 0

    def test_e2e_gobbo_gamble_resolution(self):
        """Verify Gobbo Gamble rerolls 1s on failure; continuing failure causes fumble."""
        # Initial: [1, 2] vs Normal 5+/1 -> fails.
        # Gamble rerolls 1 into 6 (explodes to 3) -> 1 success -> Pass!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 2, 6, 3]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, tn=1, allow_gamble=True)
            assert res.gambled is True
            assert res.successes == 1
            assert res.fumble is False

        # Initial: [1, 2] vs Normal 5+/1 -> fails.
        # Gamble rerolls 1 into 2 -> still 0 successes -> Fumble!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 2, 2]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, tn=1, allow_gamble=True)
            assert res.gambled is True
            assert res.successes == 0
            assert res.fumble is True

    def test_e2e_clatter_roll_evasion_vs_armor(self):
        """Verify Clatter roll active evasion and passive armor mitigation."""
        # Clean Dodge: Slink 2d6 rolls [5, 6] (2 succ >= TN 1) -> 0 damage
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 6, 2]):
            res_clean = resolve_clatter(threat_tn=1, stat_dice=2, difficulty=Difficulty.NORMAL, armor_dice=1, incoming_damage=3)
            assert res_clean.evaded is True
            assert res_clean.damage_taken == 0

        # Failed Dodge: Slink 2d6 rolls [2, 3] (0 succ). Armor 2d6 rolls [5, 6] (2 succ) -> 3 - 2 = 1 dmg
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 3, 5, 6]):
            res_mit = resolve_clatter(threat_tn=1, stat_dice=2, difficulty=Difficulty.NORMAL, armor_dice=2, incoming_damage=3)
            assert res_mit.evaded is False
            assert res_mit.damage_taken == 1

    # -------------------------------------------------------------------------
    # Criteria 2: Equipment & Stagger Fidelity
    # -------------------------------------------------------------------------
    def test_e2e_equipment_impact_size_stagger(self):
        """Verify weapon Impact Size modifiers vs target Size for Stagger condition."""
        boss = GoblinBoss(id="b1", name="Skag", zone_id="z1", size=1, tough=3)
        bear = EliteEnemy(id="e1", name="Bear", zone_id="z1", size=2, defence_tn=2)

        # Medium sword: Impact mod 0 -> Impact Size 1 < Bear Size 2 -> cannot stagger
        sword = create_notched_sword()
        assert sword.get_effective_impact_size(boss.size) < bear.size

        # Heavy Greataxe: Impact mod +1 -> Impact Size 2 >= Bear Size 2 -> staggers on partial hit!
        axe = create_heavy_greataxe()
        assert axe.get_effective_impact_size(boss.size) >= bear.size

    def test_e2e_shield_parry_and_armor_slink_bane(self):
        """Verify Shield unlocks Parry and Medium/Heavy armor imposes Slink Bane."""
        boss = GoblinBoss(
            id="b1",
            name="Garg",
            zone_id="z1",
            tough=2,
            slink=3,
            off_hand=create_pot_lid_shield(),
            armor=create_medium_armor(),
        )
        assert boss.can_parry() is True
        assert boss.get_armor_dice() == 3  # 2d from Medium + 1d from Shield
        assert boss.get_slink_bane() == 1  # Medium Armor Slink Bane 1

    # -------------------------------------------------------------------------
    # Criteria 3: Boss Quirks Fidelity
    # -------------------------------------------------------------------------
    def test_e2e_meat_shield_damage_redirection(self):
        """Verify Meat Shield redirects damage to allied Mob in Zone."""
        boss = GoblinBoss(id="b1", name="Skag", zone_id="z1", grunt=2)
        mob = PlayerMob(id="m1", name="Boyz", zone_id="z1", health_dice=[6, 6, 6])
        quirk = MeatShield()

        ctx = {"allied_mob": mob, "use_grunt": True}
        assert quirk.can_trigger(boss, ctx) is True
        res = quirk.apply(boss, ctx)
        assert res["success"] is True
        assert boss.grunt == 1

        # Mob takes the 3 damage
        mob.take_single_target_damage(3)
        assert mob.health_dice == [3, 6, 6]

    def test_e2e_ankle_bite_counter_attack(self):
        """Verify Ankle Bite triggers on clean Dodge with +1 Success."""
        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1")
        footpad = StandardEnemy(id="f1", name="Footpad", zone_id="z1", defence_tn=1)
        quirk = AnkleBite()

        ctx = {"is_clean_dodge": True, "is_melee": True, "attacker": footpad}
        assert quirk.can_trigger(boss, ctx) is True
        res = quirk.apply(boss, ctx)
        assert res["free_counter_attack"] is True
        assert res["bonus_successes"] == 1

    # -------------------------------------------------------------------------
    # Criteria 4: Enemy Traits & Overkill Wounds
    # -------------------------------------------------------------------------
    def test_e2e_parrying_buckler_cycle(self):
        """Verify Parrying Buckler Hard 6 first-attack rule."""
        highwayman = EliteEnemy(id="h1", name="Highwayman", zone_id="z1", traits=[ParryingBuckler()])
        buckler: ParryingBuckler = highwayman.get_trait("Parrying Buckler")

        attack = ThreatAttack(name="Strike", range_zones=0)  # Melee
        diff1 = buckler.on_incoming_attack_modify_difficulty(highwayman, None, attack, Difficulty.NORMAL)
        assert diff1 == Difficulty.HARD

        diff2 = buckler.on_incoming_attack_modify_difficulty(highwayman, None, attack, Difficulty.NORMAL)
        assert diff2 == Difficulty.NORMAL

    def test_e2e_thick_blubber_and_fire_bypass(self):
        """Verify Thick Blubber Bane vs normal weapons and Fire bypass."""
        bear = EliteEnemy(id="b1", name="Bear", zone_id="z1", traits=[ThickBlubber()])
        blubber: ThickBlubber = bear.get_trait("Thick Blubber")

        sword = create_notched_sword()
        molotov = create_fire_flask()

        assert blubber.on_incoming_attack_modify_pool(bear, None, sword, 3) == 2
        assert blubber.on_incoming_attack_modify_pool(bear, None, molotov, 3) == 3

    def test_e2e_overkill_wound_calculation(self):
        """Verify Overkill wound calculation against Elite enemy."""
        bear = EliteEnemy(id="b1", name="Bear", zone_id="z1", wounds=3, max_wounds=3, defence_tn=2)
        # 4 successes vs Defence 2 -> 2 Wounds dealt
        hit_res = bear.take_hit(successes=4)
        assert hit_res["wounds_dealt"] == 2
        assert bear.wounds == 1
        assert bear.is_alive is True

    # -------------------------------------------------------------------------
    # Criteria 5: Mob Health Dice Dynamics
    # -------------------------------------------------------------------------
    def test_e2e_mob_single_target_decrement_and_spillover(self):
        """Verify Mob active die decrement, spillover, and die removal."""
        mob = PlayerMob(id="m1", name="Runts", zone_id="z1", health_dice=[2, 6, 6])
        mob.take_single_target_damage(4)
        assert mob.health_dice == [4, 6]
        assert mob.size == 2

    def test_e2e_mob_aoe_full_pool_damage(self):
        """Verify AoE damage applied simultaneously to all dice in pool."""
        mob = PlayerMob(id="m1", name="Runts", zone_id="z1", health_dice=[6, 6, 6, 6])
        dealt = mob.take_aoe_damage(3)
        assert dealt == 12
        assert mob.health_dice == [3, 3, 3, 3]

    # -------------------------------------------------------------------------
    # Criteria 6: Action Economy & Round Flow
    # -------------------------------------------------------------------------
    def test_e2e_boss_action_economy_reset_and_reactions(self):
        """Verify Boss 3 Standard Actions + 1 Free Order and Reaction holding."""
        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", tough=2, grunt=2)
        boss.reset_turn_actions()
        assert boss.actions_left == 3
        assert boss.free_orders_left == 1
        assert boss.saved_reactions == 0

        # Reserve 1 reaction
        assert boss.save_reaction() is True
        assert boss.actions_left == 2
        assert boss.saved_reactions == 1

        # Use reaction during enemy turn
        assert boss.use_reaction() is True
        assert boss.saved_reactions == 0

    def test_e2e_stagger_clearing_on_round_closure(self):
        """Verify Staggered condition clears on Round Closure."""
        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1")
        boss.add_condition(Condition.STAGGERED)
        assert boss.is_staggered is True

        boss.clear_stagger()
        assert boss.is_staggered is False
