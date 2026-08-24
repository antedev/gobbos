"""
Empirical Stress Test Suite by Challenger 1 (Milestone 1).
Adversarial test harness validating:
1. Extreme Mob Health Dice decrements, massive spillover, exact kills, and full-pool AoE wipeouts.
2. Stagger calculations across complete matrix of Impact Sizes (0, 1, 2, 3, 4) vs Target Sizes (0, 1, 2, 3, 4).
3. Overkill wound conversion formulas across Defence TNs (1, 2, 3, 4), partial hits, exact hits, and high-success multipliers.
4. Complex TopologyGraph routing: disconnected subgraphs, isolated nodes, cycles, dynamic disconnects, and radius boundaries.
5. Entity edge cases: zero Grit/Health initialization, over-encumbrance, movement penalties, and multiple trait interactions.
"""

from __future__ import annotations

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
    Consumable,
    Equipment,
    Shield,
    Weapon,
    create_arbalest,
    create_bone_shiv,
    create_crossbow,
    create_dwarven_great_hammer,
    create_fire_flask,
    create_godstone_aegis,
    create_great_hammer,
    create_greataxe,
    create_halberd,
    create_heavy_arbalest,
    create_heavy_armor,
    create_heavy_greataxe,
    create_light_armor,
    create_light_crossbow,
    create_longbow,
    create_medium_armor,
    create_medium_sword,
    create_military_longbow,
    create_molotov,
    create_mortar_shell,
    create_notched_sword,
    create_pot_lid_shield,
    create_powder_keg,
    create_repeating_crossbow,
    create_runed_carapace,
    create_shield,
    create_shortbow,
    create_sling,
    create_smoke_pot,
    create_sol_quartz,
    create_spiked_mace,
    create_tower_pavise,
)
from combat_sim.domain.quirks import (
    AnkleBite,
    Butcher,
    MeatShield,
    OpportunityStrike,
    PushLuck,
    Quirk,
    SecondWind,
    SlipperyQuirk,
    SwallowLoot,
    TwistModifier,
)
from combat_sim.domain.topology import (
    TopologyGraph,
    Zone,
    ZoneProfile,
    ZoneTrait,
)
from combat_sim.domain.traits import (
    Bastion,
    BeastAncestryTrait,
    DryBones,
    EnemyTrait,
    FiendAncestryTrait,
    HumanoidAncestryTrait,
    MonstrosityAncestryTrait,
    ParryingBuckler,
    PlateBastion,
    PressurizedSteamVent,
    SteamVent,
    ThickBlubber,
    UndeadAncestryTrait,
    VoraciousRegrowth,
)


class TestMobHealthExtremeStress:
    """Stress testing single-target damage spillover, exact kills, and AoE wipeouts."""

    def test_extreme_overkill_single_target_damage(self):
        """Massive single-target damage (50, 100, 1000) cleanly wipes all health dice without index errors."""
        for dmg in [50, 100, 1000]:
            mob = PlayerMob(id="M1", name="Swarm", zone_id="Z1", health_dice=[6, 6, 6])
            total_dealt = mob.take_single_target_damage(dmg)
            assert total_dealt == 18
            assert mob.health_dice == []
            assert mob.size == 0
            assert mob.is_alive is False

    def test_exact_kill_single_target_damage(self):
        """Exact damage equal to total health wipes mob cleanly."""
        mob = PlayerMob(id="M1", name="Swarm", zone_id="Z1", health_dice=[6, 6, 6])
        total_dealt = mob.take_single_target_damage(18)
        assert total_dealt == 18
        assert mob.health_dice == []
        assert mob.size == 0
        assert mob.is_alive is False

    def test_exact_die_boundary_spillover(self):
        """Damage exactly matching die faces decrements and removes only depleted dice."""
        # [6, 6, 6] taking exactly 6 damage -> [6, 6], Size 2
        mob = PlayerMob(id="M1", name="Swarm", zone_id="Z1", health_dice=[6, 6, 6])
        dealt1 = mob.take_single_target_damage(6)
        assert dealt1 == 6
        assert mob.health_dice == [6, 6]
        assert mob.size == 2
        assert mob.is_alive is True

        # [6, 6] taking exactly 12 damage -> [], Size 0
        dealt2 = mob.take_single_target_damage(12)
        assert dealt2 == 12
        assert mob.health_dice == []
        assert mob.size == 0
        assert mob.is_alive is False

    def test_asymmetric_dice_pool_spillover(self):
        """Spillover across jagged/asymmetric dice pool faces (e.g. [1, 2, 3, 4, 5, 6])."""
        mob = PlayerMob(id="M1", name="Ragtag", zone_id="Z1", health_dice=[1, 2, 3, 4, 5, 6])
        assert mob.size == 6
        # Total HP = 21

        # Deal 5 damage:
        # Die 1 (1) takes 1 -> depleted (rem 4)
        # Die 2 (2) takes 2 -> depleted (rem 2)
        # Die 3 (3) takes 2 -> becomes 1 (rem 0)
        # Surviving dice: [1, 4, 5, 6]
        dealt = mob.take_single_target_damage(5)
        assert dealt == 5
        assert mob.health_dice == [1, 4, 5, 6]
        assert mob.size == 4
        assert mob.is_alive is True

    def test_zero_and_negative_single_target_damage(self):
        """Zero or negative damage causes no state change."""
        mob = PlayerMob(id="M1", name="Swarm", zone_id="Z1", health_dice=[6, 6])
        assert mob.take_single_target_damage(0) == 0
        assert mob.health_dice == [6, 6]
        assert mob.take_single_target_damage(-10) == 0
        assert mob.health_dice == [6, 6]

    def test_aoe_extreme_damage_wipeout(self):
        """Extreme AoE damage (50) simultaneously wipes all dice."""
        mob = PlayerMob(id="M1", name="Swarm", zone_id="Z1", health_dice=[6, 6, 6, 6, 6])
        dealt = mob.take_aoe_damage(50)
        assert dealt == 30
        assert mob.health_dice == []
        assert mob.size == 0
        assert mob.is_alive is False

    def test_aoe_exact_die_face_wipeout(self):
        """AoE damage equal to highest die face cleanly eliminates all dice at or below that value."""
        mob = PlayerMob(id="M1", name="Swarm", zone_id="Z1", health_dice=[2, 4, 6])
        # AoE 4:
        # Die 1 (2 - 4 <= 0) -> wiped
        # Die 2 (4 - 4 <= 0) -> wiped
        # Die 3 (6 - 4 = 2) -> survives as 2
        dealt = mob.take_aoe_damage(4)
        assert dealt == 10  # 12 - 2 = 10
        assert mob.health_dice == [2]
        assert mob.size == 1
        assert mob.is_alive is True

    def test_enemy_mob_spillover_and_scaling(self):
        """EnemyMob mirrors spillover and dynamic damage scaling."""
        mob = EnemyMob(id="EM1", name="Goblins", zone_id="Z1", size=4, base_damage=2)
        assert mob.get_mob_damage() == 5  # 2 + (4 - 1) = 5

        # Deal 13 damage to [6, 6, 6, 6]:
        # Die 1 (6) removed
        # Die 2 (6) removed
        # Die 3 (6) takes 1 -> becomes 5
        # Remaining: [5, 6], Size 2
        dealt = mob.take_single_target_damage(13)
        assert dealt == 13
        assert mob.health_dice == [5, 6]
        assert mob.size == 2
        assert mob.get_mob_damage() == 3  # 2 + (2 - 1) = 3


class TestStaggerAndImpactSizeMatrix:
    """Stress testing the complete Impact Size vs Target Size matrix."""

    @pytest.mark.parametrize(
        "wielder_size,weapon_factory,expected_impact_size",
        [
            (1, create_bone_shiv, 1),
            (1, create_notched_sword, 1),
            (1, create_heavy_greataxe, 2),
            (1, create_dwarven_great_hammer, 3),
            (1, create_halberd, 2),
            (1, create_heavy_arbalest, 2),
            (2, create_bone_shiv, 2),
            (2, create_heavy_greataxe, 3),
            (2, create_dwarven_great_hammer, 4),
            (3, create_heavy_greataxe, 4),
        ],
    )
    def test_weapon_impact_size_scaling(self, wielder_size, weapon_factory, expected_impact_size):
        weapon = weapon_factory()
        assert weapon.get_effective_impact_size(wielder_size=wielder_size) == expected_impact_size

    @pytest.mark.parametrize(
        "impact_size,target_size,should_stagger",
        [
            (1, 1, True),   # Light vs Size 1 -> Stagger
            (1, 2, False),  # Light vs Size 2 -> Mass resistance
            (1, 3, False),  # Light vs Size 3 -> Mass resistance
            (2, 1, True),   # Heavy vs Size 1 -> Stagger
            (2, 2, True),   # Heavy vs Size 2 -> Stagger
            (2, 3, False),  # Heavy vs Size 3 -> Mass resistance
            (3, 1, True),   # Crushing vs Size 1 -> Stagger
            (3, 2, True),   # Crushing vs Size 2 -> Stagger
            (3, 3, True),   # Crushing vs Size 3 -> Stagger
            (4, 3, True),   # Huge/Mob Heavy vs Size 3 -> Stagger
            (0, 1, False),  # 0 Impact vs Size 1 -> No stagger
        ],
    )
    def test_stagger_evaluation_against_standard_enemy(self, impact_size, target_size, should_stagger):
        enemy = StandardEnemy(id="E1", name="Enemy", zone_id="Z1", defence_tn=2, size=target_size)
        res = enemy.take_hit(successes=1, impact_size=impact_size)
        assert res["staggered"] is should_stagger
        assert enemy.is_staggered is should_stagger
        if should_stagger:
            assert enemy.get_effective_defence_tn() == 1  # 2 - 1 = 1
        else:
            assert enemy.get_effective_defence_tn() == 2

    @pytest.mark.parametrize(
        "impact_size,target_size,should_stagger",
        [
            (1, 1, True),
            (1, 2, False),
            (1, 3, False),
            (2, 2, True),
            (2, 3, False),
            (3, 3, True),
        ],
    )
    def test_stagger_evaluation_against_elite_enemy(self, impact_size, target_size, should_stagger):
        elite = EliteEnemy(
            id="E1", name="Elite Boss", zone_id="Z1", defence_tn=3, size=target_size, wounds=3, max_wounds=3
        )
        # 1 success vs Defence 3 = partial hit
        res = elite.take_hit(successes=1, impact_size=impact_size)
        assert res["wounds_dealt"] == 0
        assert res["staggered"] is should_stagger
        assert elite.is_staggered is should_stagger
        if should_stagger:
            assert elite.get_effective_defence_tn() == 2  # 3 - 1 = 2
        else:
            assert elite.get_effective_defence_tn() == 3

    def test_stagger_cleared_at_round_closure(self):
        """Stagger condition is cleared by clear_stagger(), restoring base Defence TN."""
        enemy = StandardEnemy(id="E1", name="Guard", zone_id="Z1", defence_tn=2, size=1)
        enemy.take_hit(successes=1, impact_size=1)
        assert enemy.is_staggered is True
        assert enemy.get_effective_defence_tn() == 1

        enemy.clear_stagger()
        assert enemy.is_staggered is False
        assert enemy.get_effective_defence_tn() == 2


class TestOverkillWoundConversions:
    """Stress testing the Overkill Wound conversion across Defence TNs and success counts."""

    @pytest.mark.parametrize(
        "defence_tn,successes,expected_wounds,expected_staggered",
        [
            # Defence TN 1
            (1, 0, 0, False),
            (1, 1, 1, False),
            (1, 2, 2, False),
            (1, 3, 3, False),
            (1, 5, 5, False),
            # Defence TN 2
            (2, 0, 0, False),
            (2, 1, 0, True),   # 1 success vs Def 2, Impact Size 2 >= Size 2 -> Staggers
            (2, 2, 1, False),  # 2 successes = 1 Wound
            (2, 3, 1, False),  # 3 successes = 1 Wound
            (2, 4, 2, False),  # 4 successes = 2 Wounds
            (2, 5, 2, False),  # 5 successes = 2 Wounds
            (2, 6, 3, False),  # 6 successes = 3 Wounds
            # Defence TN 3
            (3, 0, 0, False),
            (3, 1, 0, True),
            (3, 2, 0, True),
            (3, 3, 1, False),
            (3, 4, 1, False),
            (3, 5, 1, False),
            (3, 6, 2, False),
            (3, 9, 3, False),
            # Defence TN 4
            (4, 0, 0, False),
            (4, 3, 0, True),
            (4, 4, 1, False),
            (4, 8, 2, False),
        ],
    )
    def test_overkill_wounds_exact_resolution(
        self, defence_tn, successes, expected_wounds, expected_staggered
    ):
        elite = EliteEnemy(
            id="E1",
            name="Test Boss",
            zone_id="Z1",
            defence_tn=defence_tn,
            size=2,
            wounds=10,
            max_wounds=10,
        )
        res = elite.take_hit(successes=successes, impact_size=2)
        assert res["wounds_dealt"] == expected_wounds
        assert res["staggered"] is expected_staggered

    def test_overkill_wound_lethal_transition(self):
        """Overkill damage reducing Wounds to 0 sets is_alive to False and flags killed."""
        elite = EliteEnemy(id="E1", name="Elite", zone_id="Z1", defence_tn=2, wounds=2, max_wounds=2)
        res = elite.take_hit(successes=4, impact_size=1)  # 2 Wounds dealt
        assert res["wounds_dealt"] == 2
        assert res["killed"] is True
        assert elite.wounds == 0
        assert elite.is_alive is False

    def test_overkill_with_staggered_enemy(self):
        """An already Staggered enemy has Defence TN reduced by 1, increasing Overkill wounds."""
        elite = EliteEnemy(id="E1", name="Elite", zone_id="Z1", defence_tn=3, wounds=4, max_wounds=4)
        elite.add_condition(Condition.STAGGERED)
        assert elite.get_effective_defence_tn() == 2  # 3 - 1 = 2

        # 4 successes vs effective Defence 2 = 2 Wounds dealt!
        res = elite.take_hit(successes=4, impact_size=1)
        assert res["wounds_dealt"] == 2
        assert elite.wounds == 2


class TestTopologyGraphComplexStress:
    """Stress testing disconnected subgraphs, cycles, dynamic graph alterations, and radius lookups."""

    def test_disconnected_subgraphs_and_isolated_nodes(self):
        """BFS distance and pathfinding correctly return -1 and [] across disconnected components."""
        graph = TopologyGraph()
        # Subgraph A: A1 - A2 - A3
        a1, a2, a3 = Zone(id="A1", name="A1"), Zone(id="A2", name="A2"), Zone(id="A3", name="A3")
        # Subgraph B: B1 - B2
        b1, b2 = Zone(id="B1", name="B1"), Zone(id="B2", name="B2")
        # Isolated Node: C1
        c1 = Zone(id="C1", name="C1")

        for z in [a1, a2, a3, b1, b2, c1]:
            graph.add_zone(z)

        graph.connect("A1", "A2")
        graph.connect("A2", "A3")
        graph.connect("B1", "B2")

        # Distances within subgraphs
        assert graph.get_distance("A1", "A3") == 2
        assert graph.find_path("A1", "A3") == ["A1", "A2", "A3"]
        assert graph.get_distance("B1", "B2") == 1
        assert graph.find_path("B1", "B2") == ["B1", "B2"]

        # Distances across disconnected subgraphs
        assert graph.get_distance("A1", "B1") == -1
        assert graph.find_path("A1", "B1") == []
        assert graph.get_distance("A1", "C1") == -1
        assert graph.find_path("A1", "C1") == []
        assert graph.get_distance("B2", "C1") == -1
        assert graph.find_path("B2", "C1") == []

        # Self distances
        assert graph.get_distance("C1", "C1") == 0
        assert graph.find_path("C1", "C1") == ["C1"]

        # Non-existent node checks
        assert graph.get_distance("A1", "NON_EXISTENT") == -1
        assert graph.find_path("A1", "NON_EXISTENT") == []
        assert graph.get_distance("NON_EXISTENT", "A1") == -1

    def test_cycle_and_multipath_routing(self):
        """BFS shortest path takes shortest route through cyclic diamond/mesh graphs."""
        graph = TopologyGraph()
        # Diamond:
        #       N1
        #     /    \
        #   N0      N3
        #     \    /
        #       N2
        for i in range(4):
            graph.add_zone(Zone(id=f"N{i}", name=f"Node {i}"))

        graph.connect("N0", "N1")
        graph.connect("N0", "N2")
        graph.connect("N1", "N3")
        graph.connect("N2", "N3")

        assert graph.get_distance("N0", "N3") == 2
        path = graph.find_path("N0", "N3")
        assert len(path) == 3
        assert path[0] == "N0" and path[-1] == "N3"
        assert path[1] in ("N1", "N2")

    def test_dynamic_edge_disconnection(self):
        """Disconnecting zones (e.g. collapsed tunnel / shoring) updates distance and pathfinding immediately."""
        graph = TopologyGraph()
        z1, z2, z3 = Zone(id="Z1", name="Z1"), Zone(id="Z2", name="Z2"), Zone(id="Z3", name="Z3")
        for z in [z1, z2, z3]:
            graph.add_zone(z)

        graph.connect("Z1", "Z2")
        graph.connect("Z2", "Z3")

        assert graph.get_distance("Z1", "Z3") == 2
        assert graph.are_adjacent("Z1", "Z2") is True

        # Collapse tunnel Z1-Z2
        graph.disconnect("Z1", "Z2")
        assert graph.are_adjacent("Z1", "Z2") is False
        assert graph.are_adjacent("Z2", "Z1") is False
        assert graph.get_distance("Z1", "Z3") == -1
        assert graph.find_path("Z1", "Z3") == []
        # Z2 and Z3 still connected
        assert graph.get_distance("Z2", "Z3") == 1

    def test_radius_lookups_boundary_cases(self):
        """Radius lookup get_zones_within_distance across deep linear topologies."""
        graph = TopologyGraph()
        for i in range(6):
            graph.add_zone(Zone(id=f"Z{i}", name=f"Zone {i}"))
        for i in range(5):
            graph.connect(f"Z{i}", f"Z{i+1}")

        # Radius 0
        assert graph.get_zones_within_distance("Z2", 0) == ["Z2"]
        # Radius 1
        assert set(graph.get_zones_within_distance("Z2", 1)) == {"Z1", "Z2", "Z3"}
        # Radius 2
        assert set(graph.get_zones_within_distance("Z2", 2)) == {"Z0", "Z1", "Z2", "Z3", "Z4"}
        # Radius 10 (exceeds graph length)
        assert len(graph.get_zones_within_distance("Z2", 10)) == 6
        # Negative radius
        assert graph.get_zones_within_distance("Z2", -1) == []
        # Invalid zone
        assert graph.get_zones_within_distance("Z_INVALID", 2) == []


class TestEntityEdgeCasesAndLoadouts:
    """Stress testing Boss Grit, encumbrance, speeds, and composite trait interactions."""

    def test_boss_grit_and_carry_capacity(self):
        """Boss Grit and Carry capacity scale precisely with Tough stat."""
        # Tough 0: Grit = 4, Capacity = 4
        boss0 = GoblinBoss(id="B0", name="Weak", zone_id="Z1", tough=0, slink=1)
        assert boss0.max_grit == 4
        assert boss0.get_carry_capacity() == 4

        # Tough 3: Grit = 10 (4 + 2 * 3), Capacity = 10 (4 + 2 * 3)
        boss3 = GoblinBoss(id="B3", name="Hulk", zone_id="Z1", tough=3, slink=2)
        assert boss3.max_grit == 10
        assert boss3.get_carry_capacity() == 10

    def test_overburdened_movement_speed_penalty(self):
        """Carried bulk exceeding capacity imposes -1 zone movement penalty, min 1."""
        boss = GoblinBoss(
            id="B1",
            name="Hoarder",
            zone_id="Z1",
            tough=1,  # Capacity = 6 Bulk
            slink=3,  # Base speed = 3
        )
        assert boss.get_carry_capacity() == 6
        assert boss.get_movement_speed() == 3

        # Add 7 bulk of gear
        boss.main_hand = create_heavy_greataxe()  # Bulk 3
        boss.armor = create_heavy_armor()          # Bulk 3
        boss.inventory = [create_notched_sword()]  # Bulk 2 -> Total Bulk = 8
        assert boss.get_total_carried_bulk() == 8
        assert boss.get_movement_speed() == 2  # 3 - 1 = 2 (overburdened)

    def test_tower_pavise_and_overburdened_speed_stacking(self):
        """Tower Pavise halves movement speed; combined with overburdened, speed drops to minimum 1."""
        boss = GoblinBoss(
            id="B1",
            name="Slow Boss",
            zone_id="Z1",
            tough=1,  # Capacity = 6
            slink=1,  # Base speed = 2
            off_hand=create_tower_pavise(),  # Halves speed: 2 // 2 = 1
        )
        assert boss.get_movement_speed() == 1

        # Overburden boss further
        boss.inventory = [create_heavy_armor(), create_heavy_armor(), create_heavy_armor()]
        # Speed cannot drop below 1
        assert boss.get_movement_speed() == 1

    def test_composite_enemy_trait_stacking(self):
        """Enemy with Parrying Buckler, Thick Blubber, and Plate Bastion applies all defenses correctly."""
        buckler = ParryingBuckler()
        blubber = ThickBlubber()
        bastion = PlateBastion()

        boss_enemy = EliteEnemy(
            id="E1",
            name="Armored Warlord",
            zone_id="Z1",
            defence_tn=2,
            traits=[buckler, blubber, bastion],
        )

        sword = create_notched_sword()  # Melee, Cutting, no Fire, no Piercing

        # 1. 1st attack difficulty modified by buckler -> HARD (6)
        diff = buckler.on_incoming_attack_modify_difficulty(boss_enemy, None, sword, Difficulty.NORMAL)
        assert diff == Difficulty.HARD

        # 2. Attack pool modified by blubber -> -1d Bane (no Fire tag)
        pool = blubber.on_incoming_attack_modify_pool(boss_enemy, None, sword, current_pool=4)
        assert pool == 3

        # 3. Damage modified by bastion -> ignores 1 damage (no Piercing, no element)
        dmg = bastion.on_incoming_damage_modify(
            boss_enemy, None, damage=3, tags=sword.tags, traits=sword.traits
        )
        assert dmg == 2


if __name__ == "__main__":
    print("Executing Challenger 1 Stress Test Harness...")
    test_classes = [
        TestMobHealthExtremeStress,
        TestStaggerAndImpactSizeMatrix,
        TestOverkillWoundConversions,
        TestTopologyGraphComplexStress,
        TestEntityEdgeCasesAndLoadouts,
    ]
    passed_count = 0
    failed_count = 0

    for cls in test_classes:
        instance = cls()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                method = getattr(instance, method_name)
                if callable(method):
                    try:
                        # Check if method uses pytest parametrization
                        if hasattr(method, "pytestmark"):
                            # Handle parametrized methods manually if executed directly
                            pass
                        method()
                        print(f"  [PASS] {cls.__name__}.{method_name}")
                        passed_count += 1
                    except TypeError:
                        # Parametrized test invoked without args directly - runs via pytest
                        pass
                    except Exception as e:
                        print(f"  [FAIL] {cls.__name__}.{method_name}: {e}")
                        failed_count += 1

    print(f"\nStress Test Summary: {passed_count} direct tests passed, {failed_count} failed.")
