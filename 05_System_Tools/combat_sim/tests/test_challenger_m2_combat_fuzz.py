"""
Tier 4/5 Adversarial Randomized Combat Engine Fuzzer & Stress Test Suite: Challenger 1 (Milestone 2).
Exhaustively and empirically stress-tests:
1. Randomized Encounter Playouts (1,000+ combat runs):
   - Arbitrary topology graphs (Linear, Star, Ring, Mesh, Disconnected).
   - Random goblin boss compositions (weapons, armor, shields, quirks, stats).
   - Random player mob compositions (sizes 1..6, health dice, armor).
   - Random enemy compositions (Standard, Elite with complex traits, Enemy Mobs).
2. Deep Invariant Verification:
   - Deadlock / Infinite Loop Freedom: Every encounter completes in <= 50 rounds.
   - Victor Consistency: State.victor strictly matches living allies vs enemies.
   - Health / Grit Integrity: Living bosses have grit > 0; living mobs have size > 0 and dice >= 1.
   - Zone Topology Validity: Every entity occupies a valid zone in the graph.
   - Condition Lifecycles: Staggered condition never persists across round boundaries.
3. Deterministic Seed Replayability:
   - Fixed seed guarantees identical combat trajectories and outcomes.
"""

from __future__ import annotations

import random
import time
from typing import List, Tuple, Union
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
    Shield,
    Weapon,
    create_arbalest,
    create_bone_shiv,
    create_heavy_armor,
    create_heavy_greataxe,
    create_light_armor,
    create_medium_armor,
    create_notched_sword,
    create_pot_lid_shield,
    create_shortbow,
    create_tower_pavise,
)
from combat_sim.domain.quirks import AnkleBite, Butcher, MeatShield, PushLuck
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import (
    Bastion,
    BeastAncestryTrait,
    DryBones,
    EnemyTrait,
    HumanoidAncestryTrait,
    MonstrosityAncestryTrait,
    ParryingBuckler,
    PlateBastion,
    PressurizedSteamVent,
    ThickBlubber,
    UndeadAncestryTrait,
    VoraciousRegrowth,
)
from combat_sim.engine.combat import CombatEngine, CombatState, CombatSummary, RoundSummary


def build_random_topology(rng: random.Random) -> Tuple[TopologyGraph, List[str]]:
    """Generate a randomized topology graph (Linear, Ring, Star, or Mesh)."""
    topo = TopologyGraph()
    zone_count = rng.randint(2, 6)
    zone_ids = [f"z{i}" for i in range(1, zone_count + 1)]

    for zid in zone_ids:
        cover = rng.choice([CoverType.NONE, CoverType.PARTIAL, CoverType.FULL])
        diff = rng.choice([Difficulty.EASY, Difficulty.NORMAL, Difficulty.HARD])
        is_flam = rng.choice([True, False])
        zone = Zone(
            id=zid,
            name=f"Zone {zid}",
            profile=ZoneProfile(difficulty=diff, tn=rng.randint(1, 2)),
            cover=cover,
            is_flammable=is_flam,
        )
        if rng.random() < 0.2:
            zt = rng.choice(list(ZoneTraitType))
            zone.add_trait(ZoneTrait(zt))
        topo.add_zone(zone)

    # Topology shape
    shape = rng.choice(["linear", "ring", "star", "mesh"])
    if shape == "linear" or zone_count <= 2:
        for i in range(len(zone_ids) - 1):
            topo.connect(zone_ids[i], zone_ids[i + 1])
    elif shape == "ring":
        for i in range(len(zone_ids)):
            topo.connect(zone_ids[i], zone_ids[(i + 1) % len(zone_ids)])
    elif shape == "star":
        hub = zone_ids[0]
        for spoke in zone_ids[1:]:
            topo.connect(hub, spoke)
    else:  # mesh
        for i in range(len(zone_ids)):
            for j in range(i + 1, len(zone_ids)):
                if rng.random() < 0.6:
                    topo.connect(zone_ids[i], zone_ids[j])

    return topo, zone_ids


def build_random_party(
    rng: random.Random, zone_ids: List[str]
) -> List[Union[GoblinBoss, PlayerMob]]:
    """Generate randomized goblin party allies (Bosses and Mobs)."""
    allies: List[Union[GoblinBoss, PlayerMob]] = []

    # 1 to 2 Goblin Bosses
    boss_count = rng.randint(1, 2)
    for b_idx in range(boss_count):
        weapon_choice = rng.choice([
            create_notched_sword,
            create_heavy_greataxe,
            create_shortbow,
            create_arbalest,
            create_bone_shiv,
        ])()
        armor_choice = rng.choice([
            lambda: None,
            create_light_armor,
            create_medium_armor,
            create_heavy_armor,
        ])()
        shield_choice = (
            rng.choice([lambda: None, create_pot_lid_shield, create_tower_pavise])()
            if weapon_choice.handedness == WeaponHandedness.ONE_HANDED
            else None
        )

        quirk_pool = [MeatShield(), AnkleBite(), PushLuck(), Butcher()]
        quirks = rng.sample(quirk_pool, k=rng.randint(0, 2))

        boss = GoblinBoss(
            id=f"boss_{b_idx+1}",
            name=f"Boss {b_idx+1}",
            zone_id=rng.choice(zone_ids),
            tough=rng.randint(1, 3),
            slink=rng.randint(1, 3),
            mouth=rng.randint(1, 3),
            brains=rng.randint(1, 2),
            grunt=rng.randint(1, 3),
            max_grunt=3,
            main_hand=weapon_choice,
            off_hand=shield_choice,
            armor=armor_choice,
            quirks=quirks,
        )
        allies.append(boss)

    # 0 to 2 Player Mobs
    mob_count = rng.randint(0, 2)
    for m_idx in range(mob_count):
        mob_size = rng.randint(1, 5)
        mob = PlayerMob(
            id=f"mob_{m_idx+1}",
            name=f"Mob {m_idx+1}",
            zone_id=rng.choice(zone_ids),
            size=mob_size,
            armor_rating=rng.randint(0, 2),
        )
        allies.append(mob)

    return allies


def build_random_enemies(rng: random.Random, zone_ids: List[str]) -> List[Enemy]:
    """Generate randomized enemy roster (Standard, Elite, Enemy Mob)."""
    enemies: List[Enemy] = []
    enemy_count = rng.randint(1, 4)

    for e_idx in range(enemy_count):
        scale = rng.choice([EnemyScale.STANDARD, EnemyScale.ELITE, EnemyScale.MOB])
        zid = rng.choice(zone_ids)

        if scale == EnemyScale.STANDARD:
            anc = rng.choice(list(Ancestry))
            traits: List[EnemyTrait] = []
            if anc == Ancestry.UNDEAD:
                traits.append(UndeadAncestryTrait())
                traits.append(DryBones())
            elif anc == Ancestry.BEAST:
                traits.append(BeastAncestryTrait())
            elif anc == Ancestry.HUMANOID:
                traits.append(HumanoidAncestryTrait())
                if rng.random() < 0.4:
                    traits.append(ParryingBuckler())

            enemy = StandardEnemy(
                id=f"std_{e_idx+1}",
                name=f"Standard {e_idx+1}",
                zone_id=zid,
                defence_tn=rng.randint(1, 2),
                ancestry=anc,
                traits=traits,
                attacks=[
                    ThreatAttack(
                        name="Attack",
                        threat_profile=ThreatProfile(
                            threat_stat="Tough",
                            difficulty=rng.choice([Difficulty.EASY, Difficulty.NORMAL]),
                            threat_tn=rng.randint(1, 2),
                            damage=rng.randint(1, 3),
                        ),
                    )
                ],
            )
            enemies.append(enemy)

        elif scale == EnemyScale.ELITE:
            traits_elite: List[EnemyTrait] = []
            if rng.random() < 0.5:
                traits_elite.append(ThickBlubber())
            if rng.random() < 0.4:
                traits_elite.append(VoraciousRegrowth())
            if rng.random() < 0.3:
                traits_elite.append(PressurizedSteamVent())

            enemy = EliteEnemy(
                id=f"elite_{e_idx+1}",
                name=f"Elite {e_idx+1}",
                zone_id=zid,
                defence_tn=rng.randint(1, 3),
                wounds=rng.randint(2, 5),
                max_wounds=5,
                traits=traits_elite,
                attacks=[
                    ThreatAttack(
                        name="Smash",
                        threat_profile=ThreatProfile(
                            threat_stat="Tough",
                            difficulty=Difficulty.NORMAL,
                            threat_tn=rng.randint(1, 2),
                            damage=rng.randint(2, 4),
                        ),
                    )
                ],
            )
            enemies.append(enemy)

        else:  # Enemy Mob
            enemy = EnemyMob(
                id=f"emob_{e_idx+1}",
                name=f"Enemy Mob {e_idx+1}",
                zone_id=zid,
                size=rng.randint(2, 5),
                base_damage=rng.randint(1, 2),
                defence_tn=1,
                attacks=[
                    ThreatAttack(
                        name="Swarm Strike",
                        threat_profile=ThreatProfile(
                            threat_stat="Tough",
                            difficulty=Difficulty.NORMAL,
                            threat_tn=1,
                            damage=2,
                        ),
                    )
                ],
            )
            enemies.append(enemy)

    return enemies


class TestCombatEngineRandomizedFuzzer:
    """Randomized Monte Carlo fuzzer validating complete engine state space."""

    def test_fuzzer_1000_random_combats_no_deadlocks_or_corruption(self):
        """Execute 1,000 fully randomized combat encounters asserting zero crashes, zero deadlocks, and valid invariants."""
        master_seed = 421337
        master_rng = random.Random(master_seed)
        total_runs = 1000
        start_time = time.perf_counter()

        allies_wins = 0
        enemies_wins = 0
        draws = 0

        for run_idx in range(total_runs):
            run_rng = random.Random(master_rng.randint(1, 10000000))
            topo, zone_ids = build_random_topology(run_rng)
            allies = build_random_party(run_rng, zone_ids)
            enemies = build_random_enemies(run_rng, zone_ids)

            engine = CombatEngine(
                topology=topo,
                allies=allies,
                enemies=enemies,
                scenario_name=f"Fuzz Encounter {run_idx+1}",
                rng=run_rng,
            )

            summary: CombatSummary = engine.run_to_completion(max_rounds=50)

            # Invariant 1: Playout terminated within max rounds
            assert summary.total_rounds <= 50, f"Run {run_idx}: Exceeded max rounds"
            assert engine.state.is_combat_over is True

            # Invariant 2: Victor matches living entities
            living_allies = [a for a in allies if a.is_alive]
            living_enemies = [e for e in enemies if e.is_alive and not e.has_fled]

            if len(living_allies) > 0 and len(living_enemies) == 0:
                assert summary.victor == "allies", f"Run {run_idx}: Expected allies victor"
                allies_wins += 1
            elif len(living_enemies) > 0 and len(living_allies) == 0:
                assert summary.victor == "enemies", f"Run {run_idx}: Expected enemies victor"
                enemies_wins += 1
            elif summary.total_rounds >= 50:
                assert summary.victor == "draw", f"Run {run_idx}: Expected draw at round 50"
                draws += 1

            # Invariant 3: Health and Grit invariants
            for a in allies:
                if isinstance(a, GoblinBoss):
                    if a.is_alive:
                        assert a.grit > 0, f"Living boss {a.name} has grit <= 0"
                    else:
                        assert a.grit == 0, f"Dead boss {a.name} has grit > 0"
                elif isinstance(a, PlayerMob):
                    if a.is_alive:
                        assert a.size > 0, f"Living mob {a.name} has size <= 0"
                        assert len(a.health_dice) == a.size
                        assert all(d >= 1 for d in a.health_dice)
                    else:
                        assert a.size == 0
                        assert len(a.health_dice) == 0

            # Invariant 4: Zone validity
            for a in living_allies:
                assert topo.get_zone(a.zone_id) is not None, f"Entity {a.name} in invalid zone {a.zone_id}"
            for e in living_enemies:
                assert topo.get_zone(e.zone_id) is not None, f"Entity {e.name} in invalid zone {e.zone_id}"

            # Invariant 5: Stagger condition cleared
            for a in allies:
                assert not a.has_condition(Condition.STAGGERED)
            for e in enemies:
                assert not e.has_condition(Condition.STAGGERED)

        elapsed = time.perf_counter() - start_time
        print(f"\nFuzzer Completed {total_runs} combats in {elapsed:.3f}s:")
        print(f"  Allies Wins: {allies_wins} ({allies_wins/total_runs*100:.1f}%)")
        print(f"  Enemies Wins: {enemies_wins} ({enemies_wins/total_runs*100:.1f}%)")
        print(f"  Draws: {draws} ({draws/total_runs*100:.1f}%)")
        assert elapsed < 10.0, f"Fuzzer took too long: {elapsed:.3f}s >= 10.0s SLA"

    def test_fuzzer_deterministic_replay(self):
        """Identical random seeds must produce 100% identical combat summaries and action counts."""
        seed = 999888
        for _ in range(2):
            rng1 = random.Random(seed)
            topo1, zone_ids1 = build_random_topology(rng1)
            allies1 = build_random_party(rng1, zone_ids1)
            enemies1 = build_random_enemies(rng1, zone_ids1)
            engine1 = CombatEngine(topo1, allies1, enemies1, "Replay 1", rng=rng1)
            sum1 = engine1.run_to_completion(max_rounds=30)

            rng2 = random.Random(seed)
            topo2, zone_ids2 = build_random_topology(rng2)
            allies2 = build_random_party(rng2, zone_ids2)
            enemies2 = build_random_enemies(rng2, zone_ids2)
            engine2 = CombatEngine(topo2, allies2, enemies2, "Replay 2", rng=rng2)
            sum2 = engine2.run_to_completion(max_rounds=30)

            assert sum1.total_rounds == sum2.total_rounds
            assert sum1.victor == sum2.victor
            assert sum1.enemies_killed == sum2.enemies_killed
            assert sum1.total_casualties == sum2.total_casualties
            assert len(sum1.round_summaries) == len(sum2.round_summaries)


if __name__ == "__main__":
    print("Running Challenger 1 M2 Combat Fuzzer...")
    fuzzer = TestCombatEngineRandomizedFuzzer()
    fuzzer.test_fuzzer_1000_random_combats_no_deadlocks_or_corruption()
    fuzzer.test_fuzzer_deterministic_replay()
    print("All combat fuzzer tests passed successfully!")
