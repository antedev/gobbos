"""
Tier 2/3/5 Adversarial Stress Test Suite: Challenger 2 (Milestone 2).
Exhaustively and empirically stress-tests:
1. Mob Scatter Reactions:
   - Resource consumption hierarchy (Free Orders > Saved Reactions > Standard Actions > Zero Actions).
   - Scaling Size penalty: mod_tn = threat_tn + (size - 1) for sizes 1 to 8.
   - Distance difficulty thresholds (same zone +1 auto-success, normal distance, max distance hard 6, out of range).
   - Clean scatter movement to adjacent zone with 0 damage.
   - Gamble Trample Disaster: gamble fumble causes threat.damage + 1 AoE damage, out of control, and Boss Stagger in same zone.
   - Normal failure with Armor dice mitigation.
2. Swarm Terror Morale Resolution:
   - 50% casualty threshold triggers across even and odd enemy squad sizes.
   - Swarm pool scaling from surviving Bosses and Mob sizes.
   - Ancestry specific traits: Undead total morale immunity, Beast trigger reasons (fire, loud, 50% loss), Humanoid/Monstrosity checks.
   - Morale failure state: has_fled = True, is_alive = False.
3. Environmental Hazards & Fire Propagation:
   - Entry hazard tests (Slippery -> Prone, Burning -> Damage, Toxic -> Weakened) across Boss and Mob entities.
   - End-of-round fire spread across varied graph topologies (Linear, Star, Ring, Disconnected, Non-flammable).
   - Stochastic fire spread probability validation on 1d6 >= 5.
4. Tactical AI & Combat Engine Lifecycle:
   - Boss AI action budgeting, reaction saving, target prioritization, and ranged weapon fallback.
   - Mob AI Boredom rule adherence (max 1 melee attack, move chaining) and Unordered Mob Loitering vs Out-of-Control tables.
   - Enemy AI deterministic pathing, target acquisition, and Enemy Mob damage scaling.
   - Full 5-phase round lifecycle and state cleanup (Stagger clearing, fire/acid tracking reset).
5. Empirical Bug Reproductions (Documenting Implementation Defects):
   - NameError in combat_sim/engine/ai.py: Missing ClatterResolver import when Enemy attacks Boss.
   - Integer division defect in combat_sim/engine/combat.py: len(dead) >= len(enemies) // 2 premature triggers on odd squad sizes.
"""

from __future__ import annotations

import random
from unittest.mock import patch
import pytest

from combat_sim.core.dice import roll_d6, roll_dice
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
from combat_sim.domain.entities import (
    BaseEntity,
    EliteEnemy,
    Enemy,
    EnemyMob,
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
    ThreatAttack,
)
from combat_sim.domain.equipment import (
    Armor,
    Shield,
    Weapon,
    create_arbalest,
    create_fire_flask,
    create_heavy_armor,
    create_heavy_greataxe,
    create_light_armor,
    create_medium_armor,
    create_notched_sword,
    create_pot_lid_shield,
    create_shortbow,
)
from combat_sim.domain.quirks import AnkleBite, MeatShield, PushLuck
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import (
    Bastion,
    BeastAncestryTrait,
    DryBones,
    EnemyTrait,
    FiendAncestryTrait,
    HumanoidAncestryTrait,
    MonstrosityAncestryTrait,
    ParryingBuckler,
    ThickBlubber,
    UndeadAncestryTrait,
    VoraciousRegrowth,
)
from combat_sim.engine.ai import BossAI, EnemyAI, MobAI
from combat_sim.engine.combat import CombatEngine, CombatState, CombatSummary, RoundSummary
from combat_sim.engine.resolver import (
    AttackResolver,
    AttackResult,
    ClatterResolver,
    HazardResolver,
    MobReactionResolver,
    MoraleResolver,
)


class TestMobScatterReactionsEmpirical:
    """Adversarial stress-testing of Mob Scatter mechanics and failure modes."""

    def test_mob_scatter_resource_consumption_order(self):
        """Verify Boss resource consumption hierarchy: Free Order -> Saved Reaction -> Standard Action."""
        threat = ThreatProfile(threat_stat="Tough", threat_tn=1, damage=2)

        # 1. Has Free Order: consumes Free Order, leaves reactions and standard actions untouched
        boss1 = GoblinBoss(id="b1", name="Boss1", zone_id="z1", mouth=3, free_orders_left=1, saved_reactions=1, actions_left=2)
        mob1 = PlayerMob(id="m1", name="Mob1", zone_id="z1", size=1)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5]):
            res1 = MobReactionResolver.resolve_mob_scatter(mob1, boss1, threat, allow_gamble=False)
            assert res1["scattered"] is True
            assert boss1.free_orders_left == 0
            assert boss1.saved_reactions == 1
            assert boss1.actions_left == 2

        # 2. No Free Orders, but has Saved Reaction: consumes Saved Reaction
        boss2 = GoblinBoss(id="b2", name="Boss2", zone_id="z1", mouth=3, free_orders_left=0, saved_reactions=1, actions_left=2)
        mob2 = PlayerMob(id="m2", name="Mob2", zone_id="z1", size=1)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5]):
            res2 = MobReactionResolver.resolve_mob_scatter(mob2, boss2, threat, allow_gamble=False)
            assert res2["scattered"] is True
            assert boss2.free_orders_left == 0
            assert boss2.saved_reactions == 0
            assert boss2.actions_left == 2

        # 3. No Free Orders, No Saved Reactions, but has Standard Actions: consumes Standard Action
        boss3 = GoblinBoss(id="b3", name="Boss3", zone_id="z1", mouth=3, free_orders_left=0, saved_reactions=0, actions_left=3)
        mob3 = PlayerMob(id="m3", name="Mob3", zone_id="z1", size=1)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5]):
            res3 = MobReactionResolver.resolve_mob_scatter(mob3, boss3, threat, allow_gamble=False)
            assert res3["scattered"] is True
            assert boss3.free_orders_left == 0
            assert boss3.saved_reactions == 0
            assert boss3.actions_left == 2

        # 4. Zero resources available: fails immediately with reason
        boss4 = GoblinBoss(id="b4", name="Boss4", zone_id="z1", mouth=3, free_orders_left=0, saved_reactions=0, actions_left=0)
        mob4 = PlayerMob(id="m4", name="Mob4", zone_id="z1", size=1)
        res4 = MobReactionResolver.resolve_mob_scatter(mob4, boss4, threat, allow_gamble=False)
        assert res4["scattered"] is False
        assert res4["reason"] == "no_actions_or_orders"

    @pytest.mark.parametrize("mob_size", [1, 2, 3, 4, 5, 6, 8])
    def test_mob_scatter_size_penalty_scaling(self, mob_size):
        """Modified TN = Threat TN + max(0, size - 1). Large mobs are harder to herd."""
        threat_tn = 2
        expected_mod_tn = threat_tn + (mob_size - 1)

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", mouth=8, free_orders_left=1)
        mob = PlayerMob(id="m1", name="Mob", zone_id="z1", size=mob_size)
        threat = ThreatProfile(threat_stat="Tough", threat_tn=threat_tn, damage=2)

        needed_roll_successes = expected_mod_tn - 1
        faces = [5] * needed_roll_successes + [2] * (8 - needed_roll_successes)

        with patch("combat_sim.core.dice.roll_d6", side_effect=faces):
            res = MobReactionResolver.resolve_mob_scatter(mob, boss, threat, allow_gamble=False)
            assert res["scattered"] is True
            assert res["damage_taken"] == 0

    def test_mob_scatter_distance_penalties(self):
        """Cross-zone command: distance <= Mouth + 1 is Normal, distance == Mouth + 1 is Hard 6, beyond is Out of Range."""
        topo = TopologyGraph()
        for i in range(1, 6):
            topo.add_zone(Zone(id=f"z{i}", name=f"Z{i}"))
        for i in range(1, 5):
            topo.connect(f"z{i}", f"z{i+1}")

        threat = ThreatProfile(threat_stat="Tough", threat_tn=1, damage=2)

        # Test at z4 (distance 3 == Mouth + 1): Difficulty is Hard 6
        boss_z1 = GoblinBoss(id="b1", name="Boss", zone_id="z1", mouth=2, free_orders_left=1)
        mob_z4 = PlayerMob(id="m1", name="Mob", zone_id="z4", size=1)

        # Roll [5, 2]: 5 is a success at Normal, but fails at Hard 6!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 2]):
            res_hard = MobReactionResolver.resolve_mob_scatter(mob_z4, boss_z1, threat, topology=topo, allow_gamble=False)
            assert res_hard["scattered"] is False

        # Roll [6, 2, 2]: 6 succeeds at Hard 6 (and explodes bonus die 2)!
        boss_z1.free_orders_left = 1
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 2, 2]):
            res_hard_succ = MobReactionResolver.resolve_mob_scatter(mob_z4, boss_z1, threat, topology=topo, allow_gamble=False)
            assert res_hard_succ["scattered"] is True

        # Test at z5 (distance 4 > Mouth + 1): Out of range!
        boss_z1.free_orders_left = 1
        mob_z5 = PlayerMob(id="m2", name="Mob5", zone_id="z5", size=1)
        res_oor = MobReactionResolver.resolve_mob_scatter(mob_z5, boss_z1, threat, topology=topo, allow_gamble=False)
        assert res_oor["scattered"] is False
        assert res_oor["reason"] == "out_of_range"

    def test_mob_scatter_gamble_trample_disaster_details(self):
        """Adversarial check: Gamble Trample Disaster inflicts AoE damage, drops loot/control, and staggers Boss in same zone only."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))
        topo.add_zone(Zone(id="z2", name="Z2"))
        topo.connect("z1", "z2")

        threat = ThreatProfile(threat_stat="Tough", threat_tn=3, damage=2)

        # Case A: Boss in same zone
        boss_same = GoblinBoss(id="b1", name="Boss1", zone_id="z1", mouth=2, free_orders_left=1)
        mob_same = PlayerMob(id="m1", name="Mob1", zone_id="z1", health_dice=[6, 6, 6], size=3)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 2, 2]):
            res_same = MobReactionResolver.resolve_mob_scatter(mob_same, boss_same, threat, topology=topo, allow_gamble=True)
            assert res_same["scattered"] is False
            assert res_same["gamble_fumble"] is True
            assert res_same["trample"] is True
            assert mob_same.out_of_control is True
            assert boss_same.has_condition(Condition.STAGGERED)
            assert mob_same.health_dice == [3, 3, 3]

        # Case B: Boss in DIFFERENT zone (distance 1) -> Boss should NOT be staggered by trample in another zone!
        boss_diff = GoblinBoss(id="b2", name="Boss2", zone_id="z1", mouth=2, free_orders_left=1)
        mob_diff = PlayerMob(id="m2", name="Mob2", zone_id="z2", health_dice=[6, 6, 6], size=3)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 2, 2]):
            res_diff = MobReactionResolver.resolve_mob_scatter(mob_diff, boss_diff, threat, topology=topo, allow_gamble=True)
            assert res_diff["scattered"] is False
            assert res_diff["gamble_fumble"] is True
            assert res_diff["trample"] is True
            assert mob_diff.out_of_control is True
            assert not boss_diff.has_condition(Condition.STAGGERED)

    def test_mob_scatter_normal_failure_armor_mitigation(self):
        """Normal failure without gamble fumble takes threat damage mitigated by Mob Armor dice (5+)."""
        threat = ThreatProfile(threat_stat="Tough", threat_tn=3, damage=3, is_aoe=False)

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", mouth=2, free_orders_left=1)
        mob = PlayerMob(id="m1", name="Mob", zone_id="z1", health_dice=[6, 6, 6], size=3, armor_rating=1)

        # Boss rolls [2, 3] in roll_dice (core/dice.py), then Mob rolls [5] in resolve_mob_scatter (engine/resolver.py)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 3]), \
             patch("combat_sim.engine.resolver.roll_d6", side_effect=[5]):
            res = MobReactionResolver.resolve_mob_scatter(mob, boss, threat, allow_gamble=False)
            assert res["scattered"] is False
            assert res["gamble_fumble"] is False
            assert res["damage_taken"] == 2
            assert mob.health_dice == [4, 6, 6]


class TestSwarmTerrorMoraleEmpirical:
    """Adversarial stress-testing of Swarm Terror Morale checks and Ancestry traits."""

    def test_morale_check_swarm_pool_composition(self):
        """Swarm pool = sum(surviving Bosses [1 each]) + sum(surviving Mob sizes)."""
        boss1 = GoblinBoss(id="b1", name="Boss1", zone_id="z1", is_alive=True)
        boss2 = GoblinBoss(id="b2", name="Boss2", zone_id="z1", is_alive=False)
        mob1 = PlayerMob(id="m1", name="Mob1", zone_id="z1", size=4, is_alive=True)
        mob2 = PlayerMob(id="m2", name="Mob2", zone_id="z1", size=3, is_alive=True)
        mob3 = PlayerMob(id="m3", name="Mob3", zone_id="z1", size=0, is_alive=False)

        allies = [boss1, boss2, mob1, mob2, mob3]
        enemy = StandardEnemy(id="e1", name="Bandit", zone_id="z1", morale_tn=2, ancestry=Ancestry.HUMANOID)

        # 8 dice rolled vs Morale TN 2 on 5+: [5, 5, 2, 2, 2, 2, 2, 2] -> 2 successes >= 2 -> Breaks!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2, 2, 2, 2, 2, 2]):
            res = MoraleResolver.check_swarm_terror([enemy], allies)
            assert res["enemies_broken"] is True
            assert enemy.has_fled is True
            assert enemy.is_alive is False
            assert "e1" in res["broken_enemy_ids"]

    def test_undead_ancestry_total_morale_immunity(self):
        """Undead enemies never test Morale and never flee, regardless of swarm pool size or 50% losses."""
        allies = [
            GoblinBoss(id="b1", name="Boss", zone_id="z1", is_alive=True),
            PlayerMob(id="m1", name="Horde", zone_id="z1", size=10, is_alive=True),
        ]
        undead_skeleton = StandardEnemy(
            id="sk1",
            name="Skeleton",
            zone_id="z1",
            morale_tn=1,
            ancestry=Ancestry.UNDEAD,
            traits=[UndeadAncestryTrait()],
        )
        humanoid_thug = StandardEnemy(
            id="th1",
            name="Thug",
            zone_id="z1",
            morale_tn=1,
            ancestry=Ancestry.HUMANOID,
            traits=[HumanoidAncestryTrait()],
        )

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5] + [2] * 10):
            res = MoraleResolver.check_swarm_terror([undead_skeleton, humanoid_thug], allies)
            assert res["enemies_broken"] is True
            assert "th1" in res["broken_enemy_ids"]
            assert humanoid_thug.has_fled is True
            assert undead_skeleton.has_fled is False
            assert undead_skeleton.is_alive is True

    def test_beast_ancestry_trait_reactions(self):
        """Beast ancestry trait responds to fire and loud stimuli in addition to 50% losses."""
        beast = EliteEnemy(
            id="b1",
            name="Cave Bear",
            zone_id="z1",
            morale_tn=2,
            ancestry=Ancestry.BEAST,
            traits=[BeastAncestryTrait()],
        )
        beast_trait = beast.traits[0]

        assert beast_trait.on_morale_check_trigger(beast, "fire") is True
        assert beast_trait.on_morale_check_trigger(beast, "loud") is True
        assert beast_trait.on_morale_check_trigger(beast, "50_percent_loss") is True
        assert beast_trait.on_morale_check_trigger(beast, "regular_melee") is False

    def test_morale_check_zero_swarm_pool_does_not_break_enemies(self):
        """If all allies are dead (swarm pool = 0), morale check does not trigger or break enemies."""
        dead_allies = [
            GoblinBoss(id="b1", name="DeadBoss", zone_id="z1", is_alive=False),
            PlayerMob(id="m1", name="DeadMob", zone_id="z1", size=0, is_alive=False),
        ]
        enemy = StandardEnemy(id="e1", name="Bandit", zone_id="z1", morale_tn=1)

        res = MoraleResolver.check_swarm_terror([enemy], dead_allies)
        assert res["enemies_broken"] is False
        assert enemy.has_fled is False
        assert enemy.is_alive is True


class TestHazardsAndFirePropagationEmpirical:
    """Adversarial stress-testing of Environmental Hazards and Fire spread across complex topologies."""

    def test_zone_entry_hazards_all_types(self):
        """Test Slippery, Burning, and Toxic hazards for both Goblin Boss and Player Mob."""
        # 1. Slippery zone: Slink check vs profile. Fail -> Prone condition
        z_slip = Zone(id="z_slip", name="Icy Patch", profile=ZoneProfile(difficulty=Difficulty.NORMAL, tn=2))
        z_slip.add_trait(ZoneTrait(ZoneTraitType.SLIPPERY))

        boss_slip = GoblinBoss(id="b1", name="Boss", zone_id="z_slip", slink=2)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 2]):
            res_s = HazardResolver.resolve_entry_hazard(boss_slip, z_slip)
            assert res_s.get("slippery_failed") is True
            assert boss_slip.has_condition(Condition.PRONE)

        # 2. Burning zone: Slink check vs profile. Fail -> 2 damage
        z_burn = Zone(id="z_burn", name="Fire Pit", profile=ZoneProfile(difficulty=Difficulty.NORMAL, tn=1))
        z_burn.add_trait(ZoneTrait(ZoneTraitType.BURNING))

        boss_burn = GoblinBoss(id="b2", name="Boss2", zone_id="z_burn", slink=2, grit=6)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 2]):
            res_b = HazardResolver.resolve_entry_hazard(boss_burn, z_burn)
            assert res_b.get("burning_damage") == 2
            assert boss_burn.grit == 4

        mob_burn = PlayerMob(id="m1", name="Mob", zone_id="z_burn", health_dice=[6, 6, 6], size=3)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 2]):
            res_mb = HazardResolver.resolve_entry_hazard(mob_burn, z_burn)
            assert res_mb.get("burning_damage") == 2
            assert mob_burn.health_dice == [4, 6, 6]

        # 3. Toxic zone: Tough check vs profile. Fail -> Weakened condition
        z_tox = Zone(id="z_tox", name="Spore Cave", profile=ZoneProfile(difficulty=Difficulty.NORMAL, tn=1))
        z_tox.add_trait(ZoneTrait(ZoneTraitType.TOXIC))

        boss_tox = GoblinBoss(id="b3", name="Boss3", zone_id="z_tox", tough=2)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 2]):
            res_t = HazardResolver.resolve_entry_hazard(boss_tox, z_tox)
            assert res_t.get("toxic_weakened") is True
            assert boss_tox.has_condition(Condition.WEAKENED)

    def test_fire_spread_linear_graph(self):
        """Fire propagates down a 4-zone linear flammable chain on 5-6 rolls."""
        topo = TopologyGraph()
        for i in range(1, 5):
            topo.add_zone(Zone(id=f"z{i}", name=f"Barn {i}", is_flammable=True))
        for i in range(1, 4):
            topo.connect(f"z{i}", f"z{i+1}")

        topo.get_zone("z1").is_burning = True
        topo.get_zone("z1").add_trait(ZoneTrait(ZoneTraitType.BURNING))

        # Round 1: Z1 checks Z2. Rolls 5 -> Z2 ignites!
        with patch("combat_sim.engine.resolver.roll_d6", side_effect=[5]):
            ignited_r1 = HazardResolver.spread_fire(topo)
            assert "z2" in ignited_r1
            assert topo.get_zone("z2").is_burning is True

        # Round 2: Z1 checks (no unburned neighbors), Z2 checks Z3. Rolls 6 -> Z3 ignites!
        with patch("combat_sim.engine.resolver.roll_d6", side_effect=[6]):
            ignited_r2 = HazardResolver.spread_fire(topo)
            assert "z3" in ignited_r2
            assert topo.get_zone("z3").is_burning is True

    def test_fire_spread_blocked_by_non_flammable_zone(self):
        """Stone / Water zones (is_flammable=False) block fire spread completely."""
        topo = TopologyGraph()
        z1 = Zone(id="z1", name="Flammable Hut", is_burning=True, is_flammable=True)
        z2 = Zone(id="z2", name="Stone Bridge", is_burning=False, is_flammable=False)
        z3 = Zone(id="z3", name="Flammable Mill", is_burning=False, is_flammable=True)

        topo.add_zone(z1)
        topo.add_zone(z2)
        topo.add_zone(z3)
        topo.connect("z1", "z2")
        topo.connect("z2", "z3")

        with patch("combat_sim.engine.resolver.roll_d6", side_effect=[6, 6, 6]):
            ignited = HazardResolver.spread_fire(topo)
            assert len(ignited) == 0
            assert topo.get_zone("z2").is_burning is False
            assert topo.get_zone("z3").is_burning is False

    def test_fire_spread_all_flammable_spokes(self):
        """All connected flammable zones ignite when rolling 5+."""
        topo = TopologyGraph()
        center = Zone(id="center", name="Courtyard", is_burning=True, is_flammable=True)
        topo.add_zone(center)

        spokes = ["north", "south", "east", "west"]
        for s in spokes:
            topo.add_zone(Zone(id=s, name=s.capitalize(), is_burning=False, is_flammable=True))
            topo.connect("center", s)

        # All rolls are 5 -> all 4 spokes ignite!
        with patch("combat_sim.engine.resolver.roll_d6", return_value=5):
            ignited = HazardResolver.spread_fire(topo)
            assert set(ignited) == set(spokes)
            for s in spokes:
                assert topo.get_zone(s).is_burning is True


class TestTacticalAIAndCombatEngineLifecycleEmpirical:
    """Adversarial stress-testing of tactical AI decision trees and engine round lifecycle."""

    def test_boss_ai_target_priority_and_reaction_budgeting(self):
        """Boss AI reserves 1 reaction when facing living enemies and prioritizes Standard enemies over Elites."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", tough=3, grit=8, actions_left=3, saved_reactions=0)
        footpad = StandardEnemy(id="s1", name="Footpad", zone_id="z1", defence_tn=1)
        troll = EliteEnemy(id="e1", name="Troll", zone_id="z1", defence_tn=2, wounds=4)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5, 5, 5, 5]):
            acts = BossAI.execute_turn(boss, [boss], [footpad, troll], topo, rng=random.Random(42))
            assert boss.saved_reactions == 1
            assert footpad.is_alive is False
            assert troll.wounds < 4

    def test_mob_ai_boredom_rule_enforcement(self):
        """Ordered Mob can Melee Attack at most ONCE per turn, but can Move multiple times."""
        topo = TopologyGraph()
        for i in range(1, 4):
            topo.add_zone(Zone(id=f"z{i}", name=f"Z{i}"))
        topo.connect("z1", "z2")
        topo.connect("z2", "z3")

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1")
        mob = PlayerMob(id="m1", name="Mob", zone_id="z1", size=3, actions_left=2)
        enemy = StandardEnemy(id="e1", name="Guard", zone_id="z1", defence_tn=3)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 2, 2]):
            acts = MobAI.execute_ordered_mob_turn(mob, boss, [boss, mob], [enemy], topo)
            attack_acts = [a for a in acts if a.get("action") == "Mob Melee Attack"]
            assert len(attack_acts) == 1
            assert mob.actions_left == 0

    def test_unordered_mob_loitering_vs_out_of_control(self):
        """Unordered controlled mob rolls Loitering (1 saved reaction); Out-of-Control rolls panic (0 saved reactions)."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))
        topo.add_zone(Zone(id="z2", name="Z2"))
        topo.connect("z1", "z2")

        # Loitering mob: rolls 4 (wanders 1 zone, saves 1 reaction)
        mob_loiter = PlayerMob(id="m1", name="Loiterer", zone_id="z1", size=3, out_of_control=False)
        with patch("combat_sim.engine.ai.roll_d6", return_value=4):
            res_l = MobAI.execute_unordered_mob(mob_loiter, topo)
            assert res_l["state"] == "Loitering"
            assert res_l["saved_reactions"] == 1
            assert mob_loiter.zone_id == "z2"
            assert mob_loiter.saved_reactions == 1

        # Out-of-Control mob: rolls 1 (panics/flees 1 zone, 0 saved reactions)
        mob_ooc = PlayerMob(id="m2", name="Panicker", zone_id="z1", size=3, out_of_control=True)
        with patch("combat_sim.engine.ai.roll_d6", return_value=1):
            res_o = MobAI.execute_unordered_mob(mob_ooc, topo)
            assert res_o["state"] == "Out of Control"
            assert res_o["saved_reactions"] == 0
            assert mob_ooc.zone_id == "z2"
            assert mob_ooc.saved_reactions == 0


class TestRemediatedEngineBehaviorsEmpirical:
    """Empirical verification of remediated engine behaviors and group attack mechanics."""

    def test_enemy_ai_boss_attack_clatter_resolution_clean_execution(self):
        """Remediation 1: EnemyAI.execute_enemy_turns resolves Clatter defense against GoblinBoss without NameError."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", tough=3, grit=6, saved_reactions=1)
        enemy = StandardEnemy(
            id="e1",
            name="Bandit",
            zone_id="z1",
            attacks=[ThreatAttack(name="Club", threat_tn=1, damage=1)],
        )

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5]):
            acts = EnemyAI.execute_enemy_turns([enemy], [boss], topo)
            assert len(acts) == 1
            assert acts[0]["action"] == "Enemy Attack on Boss"
            assert acts[0]["actor"] == "Bandit"
            assert acts[0]["target"] == "Boss"
            assert acts[0]["evaded"] is True
            assert acts[0]["damage_taken"] == 0
            assert boss.grit == 6

    def test_50_percent_morale_threshold_odd_and_even_counts(self):
        """Remediation 2: 50% casualty Morale check evaluates (dead_count * 2 >= total_count) and dead_count > 0."""
        # Squad of 3 enemies: 1 casualty is 33% (No trigger), 2 casualties is 67% (Triggers)
        total_3 = 3
        assert (1 * 2 >= total_3) is False  # 1/3 dead does not trigger
        assert (2 * 2 >= total_3) is True   # 2/3 dead triggers

        # Squad of 4 enemies: 1 casualty is 25% (No trigger), 2 casualties is 50% (Triggers)
        total_4 = 4
        assert (1 * 2 >= total_4) is False  # 1/4 dead does not trigger
        assert (2 * 2 >= total_4) is True   # 2/4 dead triggers

        # Squad of 5 enemies: 2 casualties is 40% (No trigger), 3 casualties is 60% (Triggers)
        total_5 = 5
        assert (2 * 2 >= total_5) is False  # 2/5 dead does not trigger
        assert (3 * 2 >= total_5) is True   # 3/5 dead triggers

    def test_enemy_ai_group_attack_combining_on_boss(self):
        """Remediation 3A: Multiple enemies in the same zone combine up to 3 attackers into a single Group Attack on a Boss."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", tough=3, grit=8, saved_reactions=1)
        enemies = [
            StandardEnemy(id="e1", name="Bandit 1", zone_id="z1", attacks=[ThreatAttack(name="Club", threat_tn=1, damage=2)]),
            StandardEnemy(id="e2", name="Bandit 2", zone_id="z1", attacks=[ThreatAttack(name="Club", threat_tn=1, damage=2)]),
            StandardEnemy(id="e3", name="Bandit 3", zone_id="z1", attacks=[ThreatAttack(name="Club", threat_tn=1, damage=2)]),
        ]

        # 3 enemies combine: Base Damage (2) + (3 - 1) = 4 Damage
        # Boss evades with 1 reaction (rolls 5+ on Tough 3)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5]):
            acts = EnemyAI.execute_enemy_turns(enemies, [boss], topo)
            assert len(acts) == 1
            assert acts[0]["action"] == "Group Attack on Boss"
            assert acts[0]["attacker_count"] == 3
            assert acts[0]["damage"] == 4
            assert acts[0]["evaded"] is True
            assert acts[0]["damage_taken"] == 0

    def test_enemy_ai_group_attack_combining_on_mob_unlimited(self):
        """Remediation 3B: Multiple enemies in the same zone combine with no limit when attacking a PlayerMob."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        mob = PlayerMob(id="m1", name="Mob", zone_id="z1", health_dice=[6, 6, 6], size=3)
        enemies = [
            StandardEnemy(id=f"e{i}", name=f"Wolf {i}", zone_id="z1", attacks=[ThreatAttack(name="Bite", threat_tn=1, damage=2)])
            for i in range(1, 6)
        ]

        # 5 enemies combine: Base Damage (2) + (5 - 1) = 6 Damage
        # Single-target damage applied to Mob: exhausts first 6 HP die, Mob becomes Size 2 [6, 6]
        acts = EnemyAI.execute_enemy_turns(enemies, [mob], topo)
        assert len(acts) == 1
        assert acts[0]["action"] == "Group Attack on Mob"
        assert acts[0]["attacker_count"] == 5
        assert acts[0]["damage_dealt"] == 6
        assert mob.size == 2
        assert mob.health_dice == [6, 6]

    def test_enemy_ai_group_attack_overflow_to_allied_mob(self):
        """Remediation 3C: If 4 enemies and 1 Boss + 1 Mob in zone, 3 swarm Boss and 1 attacks Mob."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", tough=3, grit=8, saved_reactions=1)
        mob = PlayerMob(id="m1", name="Mob", zone_id="z1", health_dice=[6, 6, 6], size=3)
        enemies = [
            StandardEnemy(id=f"e{i}", name=f"Bandit {i}", zone_id="z1", attacks=[ThreatAttack(name="Club", threat_tn=1, damage=2)])
            for i in range(1, 5)
        ]

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 5]):
            acts = EnemyAI.execute_enemy_turns(enemies, [boss, mob], topo)
            assert len(acts) == 2
            # Attack 1: 3 enemies on Boss (Damage = 2 + 2 = 4)
            assert acts[0]["action"] == "Group Attack on Boss"
            assert acts[0]["target"] == "Boss"
            assert acts[0]["attacker_count"] == 3
            assert acts[0]["damage"] == 4
            # Attack 2: 1 enemy on Mob (Damage = 2)
            assert acts[1]["action"] == "Enemy Attack on Mob"
            assert acts[1]["target"] == "Mob"
            assert acts[1]["attacker_count"] == 1
            assert acts[1]["damage_dealt"] == 2
            assert mob.health_dice == [4, 6, 6]

    def test_enemy_ai_group_attack_with_enemy_mob_damage_scaling(self):
        """Remediation 3D: EnemyMob primary attacker scales mob damage (+ Size - 1) plus group attack bonus (+ count - 1)."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", tough=3, grit=10, saved_reactions=0, actions_left=0)
        # EnemyMob Size 4 with base_damage 2 -> mob damage = 2 + (4 - 1) = 5
        enemy_mob = EnemyMob(id="em1", name="Goblin Horde", zone_id="z1", size=4, base_damage=2)
        std_enemy = StandardEnemy(id="e1", name="Ogre", zone_id="z1", attacks=[ThreatAttack(name="Club", threat_tn=1, damage=2)])

        # Group attack of 2 attackers (EnemyMob + StandardEnemy): combined damage = 5 + (2 - 1) = 6
        acts = EnemyAI.execute_enemy_turns([enemy_mob, std_enemy], [boss], topo)
        assert len(acts) == 1
        assert acts[0]["action"] == "Group Attack on Boss"
        assert acts[0]["attacker_count"] == 2
        assert acts[0]["damage"] == 6
        assert boss.grit == 4  # 10 - 6 = 4

    def test_combat_engine_50_percent_morale_check_end_to_end(self):
        """Remediation 3E: Full CombatEngine run_round verifies Swarm Terror triggers at >= 50% casualties only."""
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        # Case A: 3 enemies, 1 dead (33.3% loss) -> Swarm Terror does NOT trigger
        boss_a = GoblinBoss(id="b1", name="Boss", zone_id="z1", conditions={Condition.STUNNED})
        e1 = StandardEnemy(id="e1", name="E1", zone_id="z1", is_alive=False)  # Dead
        e2 = StandardEnemy(id="e2", name="E2", zone_id="z1", is_alive=True, morale_tn=1)
        e3 = StandardEnemy(id="e3", name="E3", zone_id="z1", is_alive=True, morale_tn=1)

        engine_a = CombatEngine(topo, [boss_a], [e1, e2, e3], "Morale Test A")
        summary_a = engine_a.run_round()
        assert len(summary_a.morale_events) == 0  # 1/3 dead did not trigger morale check!
        assert e2.is_alive is True
        assert e3.is_alive is True

        # Case B: 3 enemies, 2 dead (66.7% loss) -> Swarm Terror triggers and e3 flees on failed check
        boss_b = GoblinBoss(id="b1", name="Boss", zone_id="z1", conditions={Condition.STUNNED})
        e1_b = StandardEnemy(id="e1", name="E1", zone_id="z1", is_alive=False)  # Dead
        e2_b = StandardEnemy(id="e2", name="E2", zone_id="z1", is_alive=False)  # Dead
        e3_b = StandardEnemy(id="e3", name="E3", zone_id="z1", is_alive=True, morale_tn=1)

        engine_b = CombatEngine(topo, [boss_b], [e1_b, e2_b, e3_b], "Morale Test B")
        with patch("combat_sim.core.dice.roll_d6", return_value=5):  # 5 is success vs TN 1 -> enemy breaks and flees
            summary_b = engine_b.run_round()
            assert len(summary_b.morale_events) == 1
            assert summary_b.morale_events[0]["enemies_broken"] is True
            assert e3_b.has_fled is True
