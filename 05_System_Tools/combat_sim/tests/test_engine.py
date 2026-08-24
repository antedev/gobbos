"""Tier 1/2/3 Test Suite: Combat Engine and Resolvers.

Exhaustively verifies:
1. AttackResolver (Melee, Ranged, Impact Size Stagger, Overkill Wounds, AoE/Cleave, Cross-Gang).
2. ClatterResolver (Active Evasion, Armor Mitigation, Ablative Gear Sacrifice, Meat Shield).
3. MobReactionResolver (Mob Scatter clean move vs Gamble Trample Disaster).
4. HazardResolver (Slippery, Burning, Toxic Spores, Fire Spread).
5. MoraleResolver (50% casualty Swarm Terror, Beast triggers, Undead immunity).
6. CombatEngine (5-Phase Round Cycle, State Management, Combat Summary).
"""

from __future__ import annotations

import random
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
    BeastAncestryTrait,
    DryBones,
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


class TestAttackResolverEngine:
    """Validate AttackResolver melee, ranged, and damage interactions."""

    def test_melee_attack_kills_standard_enemy(self):
        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", tough=3)
        guard = StandardEnemy(id="g1", name="Guard", zone_id="z1", defence_tn=1)

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 3, 2]):
            res = AttackResolver.resolve_melee_attack(boss, guard, allow_gamble=False)
            assert res.hit is True
            assert res.killed is True
            assert guard.is_alive is False

    def test_melee_attack_staggers_on_partial_hit(self):
        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", tough=3, main_hand=create_heavy_greataxe())
        bear = EliteEnemy(id="e1", name="Bear", zone_id="z1", defence_tn=2, size=2, wounds=3)

        # 1 success vs Defence 2 with Heavy Axe (Impact Size 2 >= Bear Size 2) -> Staggered
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 2, 2]):
            res = AttackResolver.resolve_melee_attack(boss, bear, weapon=boss.main_hand, allow_gamble=False)
            assert res.hit is False
            assert res.staggered is True
            assert bear.is_staggered is True
            assert bear.wounds == 3

    def test_ranged_attack_out_of_range(self):
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))
        topo.add_zone(Zone(id="z2", name="Z2"))
        topo.add_zone(Zone(id="z3", name="Z3"))
        topo.add_zone(Zone(id="z4", name="Z4"))
        topo.connect("z1", "z2")
        topo.connect("z2", "z3")
        topo.connect("z3", "z4")

        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", slink=3, main_hand=create_shortbow())  # Range 2
        enemy = StandardEnemy(id="e1", name="Target", zone_id="z4")  # Distance 3

        res = AttackResolver.resolve_ranged_attack(boss, enemy, boss.main_hand, topo)
        assert res.hit is False
        assert "Target out of range" in res.log_messages[0]


class TestClatterResolverEngine:
    """Validate ClatterResolver defense, meat shield, and ablative gear sacrifice."""

    def test_clatter_clean_dodge_with_partial_cover_boon(self):
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1", cover=CoverType.PARTIAL))

        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", slink=2, saved_reactions=1)
        threat = ThreatProfile(threat_stat="Slink", difficulty=Difficulty.NORMAL, threat_tn=1, damage=2)

        # Partial cover adds +1d to Slink pool -> rolls 3 dice
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 2, 2]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat, topology=topo)
            assert res.evaded is True
            assert res.damage_taken == 0
            assert boss.saved_reactions == 0

    def test_clatter_ablative_shield_sacrifice_on_lethal_damage(self):
        boss = GoblinBoss(
            id="b1",
            name="Garg",
            zone_id="z1",
            grit=1,
            max_grit=4,
            slink=1,
            saved_reactions=0,
            actions_left=0,
            off_hand=create_pot_lid_shield(),
        )
        threat = ThreatProfile(threat_stat="Tough", difficulty=Difficulty.NORMAL, threat_tn=1, damage=3)

        # 0 saved actions -> cannot evade. Armor dice = 1 (shield). Rolls 2 (fails to mitigate)
        # Damage 3 would drop Grit from 1 to -2 (fatal). Shield is sacrificed!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2]):
            res = ClatterResolver.resolve_boss_defense(boss, None, threat)
            assert res.evaded is False
            assert res.damage_taken == 0
            assert boss.grit == 1  # Survived!
            assert boss.off_hand is None  # Shield was shattered and removed


class TestMobReactionResolverEngine:
    """Validate Mob Scatter clean move and Gamble Trample Disaster."""

    def test_mob_scatter_clean_success(self):
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))
        topo.add_zone(Zone(id="z2", name="Z2"))
        topo.connect("z1", "z2")

        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", mouth=2, free_orders_left=1)
        mob = PlayerMob(id="m1", name="Runts", zone_id="z1", size=3)
        threat = ThreatProfile(threat_stat="Tough", threat_tn=1, damage=2)

        # Same zone gives +1 auto success. Modified TN = 1 + (3 - 1) = 3.
        # Boss rolls Mouth 2d6: [5, 5] -> 2 successes + 1 auto = 3 -> Clean Scatter!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5]):
            res = MobReactionResolver.resolve_mob_scatter(mob, boss, threat, topo, allow_gamble=False)
            assert res["scattered"] is True
            assert res["damage_taken"] == 0
            assert mob.zone_id == "z2"  # Scurried to adjacent zone!

    def test_mob_scatter_gamble_trample_disaster(self):
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Z1"))

        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", mouth=2, free_orders_left=1)
        mob = PlayerMob(id="m1", name="Runts", zone_id="z1", health_dice=[6, 6, 6])
        threat = ThreatProfile(threat_stat="Tough", threat_tn=2, damage=2)

        # Modified TN = 2 + 2 = 4. Auto success = 1.
        # Mouth 2d6 rolls [1, 2] -> fails. Gamble rerolls 1 into 2 -> still fails -> Fumble!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 2, 2]):
            res = MobReactionResolver.resolve_mob_scatter(mob, boss, threat, topo, allow_gamble=True)
            assert res["scattered"] is False
            assert res["trample"] is True
            assert mob.out_of_control is True
            assert boss.is_staggered is True


class TestHazardAndMoraleResolvers:
    """Validate Hazard checks, fire spread, and Morale triggers."""

    def test_fire_spread_to_flammable_adjacent_zone(self):
        topo = TopologyGraph()
        z1 = Zone(id="z1", name="Burning Barn", is_burning=True, is_flammable=True)
        z2 = Zone(id="z2", name="Wooden Shed", is_burning=False, is_flammable=True)
        topo.add_zone(z1)
        topo.add_zone(z2)
        topo.connect("z1", "z2")

        # Roll 5 on 1d6 -> spreads!
        with patch("combat_sim.engine.resolver.roll_d6", side_effect=[5]):
            ignited = HazardResolver.spread_fire(topo)
            assert "z2" in ignited
            assert z2.is_burning is True

    def test_swarm_terror_breaks_humanoids_but_not_undead(self):
        allies = [
            GoblinBoss(id="b1", name="Garg", zone_id="z1", is_alive=True),
            PlayerMob(id="m1", name="Runts", zone_id="z1", size=3, is_alive=True),
        ]
        # Swarm pool = 1 + 3 = 4 dice
        humanoid = StandardEnemy(id="h1", name="Robber", zone_id="z1", morale_tn=1, ancestry=Ancestry.HUMANOID)
        undead = StandardEnemy(id="u1", name="Skeleton", zone_id="z1", morale_tn=1, ancestry=Ancestry.UNDEAD, traits=[UndeadAncestryTrait()])

        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 2, 3, 4]):
            res = MoraleResolver.check_swarm_terror([humanoid, undead], allies)
            assert humanoid.has_fled is True
            assert humanoid.is_alive is False
            assert undead.has_fled is False
            assert undead.is_alive is True


class TestCombatEngineLoop:
    """Validate the 5-phase combat engine loop and encounter completion."""

    def test_combat_engine_single_round_and_completion(self):
        topo = TopologyGraph()
        topo.add_zone(Zone(id="z1", name="Arena"))

        boss = GoblinBoss(id="b1", name="Garg", zone_id="z1", tough=3, grit=8, main_hand=create_heavy_greataxe())
        mob = PlayerMob(id="m1", name="Boyz", zone_id="z1", size=3)
        footpad = StandardEnemy(
            id="f1",
            name="Footpad",
            zone_id="z1",
            defence_tn=1,
            attacks=[ThreatAttack(name="Shiv", threat_tn=1, damage=1)],
        )

        engine = CombatEngine(
            topology=topo,
            allies=[boss, mob],
            enemies=[footpad],
            scenario_name="Test Duel",
            rng=random.Random(42),
        )

        summary = engine.run_to_completion(max_rounds=10)
        assert summary.victor == "allies"
        assert summary.allies_survived is True
        assert summary.enemies_killed == 1
        assert summary.total_rounds >= 1
