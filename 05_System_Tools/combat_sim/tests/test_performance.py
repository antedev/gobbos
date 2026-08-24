"""
Tier 4 Test Suite: Performance Benchmarks and Monte Carlo Analytics.
Validates 1,000+ iteration simulation throughput in <10 seconds SLA,
statistical metric aggregations (Win/Loss/TPK, Grit distributions, Mob survival),
and A/B gear balance comparisons.
"""

from __future__ import annotations

import random
import time
from typing import Dict, List
import pytest

from combat_sim.core.types import Difficulty, Condition
from combat_sim.domain.entities import GoblinBoss, PlayerMob, StandardEnemy, EliteEnemy, EnemyMob
from combat_sim.domain.equipment import (
    create_notched_sword,
    create_pot_lid_shield,
    create_medium_armor,
    create_heavy_greataxe,
    create_light_armor,
)
from combat_sim.domain.quirks import MeatShield, AnkleBite
from combat_sim.analytics import (
    ABComparisonResult,
    DistributionStats,
    MonteCarloSimulator,
    PRESET_SCENARIOS,
    SimulationMetrics,
    SimulationRunResult,
    StatisticalAggregator,
    build_maulers_den,
    build_street_skirmish,
    build_tomb_highwayman,
)


def simulate_fast_single_encounter(seed: int = 0) -> Dict[str, float]:
    """Lightweight pure-python combat simulation step for Monte Carlo throughput test."""
    rng = random.Random(seed)

    # Street skirmish minimal encounter setup
    boss_grit = 8
    mob_hp = [6, 6, 6]
    robber_hp = [6, 6, 6]
    footpad_alive = True

    rounds = 0
    while (boss_grit > 0 or mob_hp) and (robber_hp or footpad_alive) and rounds < 20:
        rounds += 1

        # Player turn: Boss attack
        boss_rolls = [rng.randint(1, 6) for _ in range(2)]
        boss_succ = sum(1 for f in boss_rolls if f >= 5)
        if footpad_alive and boss_succ >= 1:
            footpad_alive = False
        elif robber_hp and boss_succ >= 1:
            # damage robber mob
            dmg = boss_succ
            while dmg > 0 and robber_hp:
                if robber_hp[0] > dmg:
                    robber_hp[0] -= dmg
                    dmg = 0
                else:
                    dmg -= robber_hp[0]
                    robber_hp.pop(0)

        # Mob attack
        if mob_hp:
            mob_size = len(mob_hp)
            mob_rolls = [rng.randint(1, 6) for _ in range(mob_size)]
            mob_succ = sum(1 for f in mob_rolls if f >= 5)
            if robber_hp and mob_succ >= 1:
                dmg = mob_succ
                while dmg > 0 and robber_hp:
                    if robber_hp[0] > dmg:
                        robber_hp[0] -= dmg
                        dmg = 0
                    else:
                        dmg -= robber_hp[0]
                        robber_hp.pop(0)

        # Enemy turn
        if robber_hp:
            # Clatter roll on Boss: 2 Slink dice + 3 Armor dice vs Threat TN 1 (3 Dmg)
            slink_rolls = [rng.randint(1, 6) for _ in range(2)]
            if any(f >= 5 for f in slink_rolls):
                pass  # Clean dodge
            else:
                armor_rolls = [rng.randint(1, 6) for _ in range(3)]
                armor_mit = sum(1 for f in armor_rolls if f >= 5)
                boss_grit = max(0, boss_grit - max(0, 3 - armor_mit))

        if footpad_alive:
            # Footpad hits mob: 1 damage
            if mob_hp:
                if mob_hp[0] > 1:
                    mob_hp[0] -= 1
                else:
                    mob_hp.pop(0)

    victory = not (robber_hp or footpad_alive) and (boss_grit > 0 or bool(mob_hp))
    return {
        "victory": 1.0 if victory else 0.0,
        "rounds": float(rounds),
        "boss_grit": float(boss_grit),
        "mob_size": float(len(mob_hp)),
    }


class TestMonteCarloPerformance:
    """Benchmark Monte Carlo simulation throughput and statistical metrics."""

    def test_monte_carlo_batch_execution_1000_runs(self):
        """Verify that 1,000 Monte Carlo iterations execute in strictly < 10.0 seconds."""
        iterations = 1000
        start_time = time.perf_counter()

        results = []
        for i in range(iterations):
            outcome = simulate_fast_single_encounter(seed=i)
            results.append(outcome)

        elapsed = time.perf_counter() - start_time
        print(f"\n[PERFORMANCE] Executed {iterations} Monte Carlo iterations in {elapsed:.4f}s.")

        # Performance SLA: Under 10 seconds
        assert elapsed < 10.0, f"Monte Carlo simulation exceeded 10.0s SLA (took {elapsed:.2f}s)"

    def test_statistical_metrics_aggregation(self):
        """Verify statistical metrics calculation over batch run."""
        iterations = 500
        results = [simulate_fast_single_encounter(seed=i) for i in range(iterations)]

        win_rate = sum(r["victory"] for r in results) / iterations
        avg_rounds = sum(r["rounds"] for r in results) / iterations
        avg_grit = sum(r["boss_grit"] for r in results) / iterations
        avg_mob = sum(r["mob_size"] for r in results) / iterations

        # Statistical sanity checks
        assert 0.0 <= win_rate <= 1.0
        assert 1.0 <= avg_rounds <= 20.0
        assert 0.0 <= avg_grit <= 8.0
        assert 0.0 <= avg_mob <= 3.0

    def test_ab_balance_comparison_shield_vs_greataxe(self):
        """A/B balance test: compare party survival between Shield loadout vs Heavy weapon."""
        def run_loadout(has_shield: bool, runs: int = 300) -> float:
            wins = 0
            for seed in range(runs):
                rng = random.Random(seed)
                grit = 8
                mob_hp = [6, 6, 6]
                enemy_hp = [6, 6, 6]
                armor_dice = 3 if has_shield else 1
                attack_pool = 2 if has_shield else 3  # Greataxe adds dice/impact

                for _ in range(15):
                    if not enemy_hp or (grit <= 0 and not mob_hp):
                        break
                    # Attack
                    rolls = [rng.randint(1, 6) for _ in range(attack_pool)]
                    succ = sum(1 for f in rolls if f >= 5)
                    if succ >= 1 and enemy_hp:
                        enemy_hp[0] -= succ
                        if enemy_hp[0] <= 0:
                            enemy_hp.pop(0)

                    # Defence
                    if enemy_hp:
                        slink_succ = sum(1 for f in [rng.randint(1, 6) for _ in range(2)] if f >= 5)
                        if slink_succ < 1:
                            armor_mit = sum(1 for f in [rng.randint(1, 6) for _ in range(armor_dice)] if f >= 5)
                            grit = max(0, grit - max(0, 2 - armor_mit))

                if not enemy_hp and (grit > 0 or mob_hp):
                    wins += 1
            return wins / runs

        shield_win_rate = run_loadout(has_shield=True)
        greataxe_win_rate = run_loadout(has_shield=False)

        assert 0.0 <= shield_win_rate <= 1.0
        assert 0.0 <= greataxe_win_rate <= 1.0

    def test_real_monte_carlo_engine_1000_runs_under_10s(self):
        """Execute 1,000 runs using real MonteCarloSimulator on Street Skirmish within < 10.0s SLA."""
        sim = MonteCarloSimulator.from_preset("street_skirmish")
        start = time.perf_counter()
        metrics = sim.run(iterations=1000, base_seed=42)
        elapsed = time.perf_counter() - start

        print(f"\n[BENCHMARK] Real Engine: 1,000 runs in {elapsed:.4f}s ({metrics.runs_per_second:,.1f} runs/s).")
        print(metrics.format_ascii_table())

        assert elapsed < 10.0, f"Monte Carlo 1,000 runs took {elapsed:.2f}s, exceeding 10.0s SLA"
        assert metrics.total_runs == 1000
        assert metrics.wins + metrics.losses + metrics.draws == 1000
        assert 0.0 <= metrics.win_rate <= 1.0
        assert 0.0 <= metrics.loss_rate <= 1.0
        assert 0.0 <= metrics.tpk_rate <= 1.0
        assert metrics.rounds.mean > 0.0
        assert metrics.boss_grit.mean >= 0.0
        assert metrics.mob_surviving_size.mean >= 0.0

    def test_real_monte_carlo_ab_balance_comparison(self):
        """Execute A/B balance test between Shield vs 2H Greataxe on Street Skirmish."""
        def factory_shield():
            return build_street_skirmish()

        def factory_greataxe():
            topo, allies, enemies = build_street_skirmish()
            boss = allies[0]
            boss.main_hand = create_heavy_greataxe()
            boss.off_hand = None
            boss.armor = create_light_armor()
            return topo, allies, enemies

        comp = MonteCarloSimulator.run_ab_comparison(
            factory_a=factory_shield,
            factory_b=factory_greataxe,
            iterations=300,
            name_a="Shield + Sword",
            name_b="2H Greataxe",
            base_seed=100,
        )

        print("\n" + comp.format_ascii_table())

        assert comp.metrics_a.total_runs == 300
        assert comp.metrics_b.total_runs == 300
        assert -1.0 <= comp.win_rate_delta <= 1.0
        assert -1.0 <= comp.loss_rate_delta <= 1.0
        assert -1.0 <= comp.tpk_rate_delta <= 1.0

        table_str = comp.format_ascii_table()
        assert "A/B Balance Comparison" in table_str
        assert "Shield + Sword" in table_str
        assert "2H Greataxe" in table_str
        assert "DELTA" in table_str

        d = comp.to_dict()
        assert "deltas" in d
        assert "win_rate" in d["deltas"]

    def test_distribution_stats_edge_cases(self):
        """Verify statistical metrics on empty, single, and small distributions."""
        empty_dist = DistributionStats.from_values([])
        assert empty_dist.count == 0
        assert empty_dist.mean == 0.0
        assert empty_dist.median == 0.0
        assert empty_dist.stddev == 0.0
        assert empty_dist.format_compact() == "N/A"

        single_dist = DistributionStats.from_values([5])
        assert single_dist.count == 1
        assert single_dist.mean == 5.0
        assert single_dist.median == 5.0
        assert single_dist.stddev == 0.0
        assert single_dist.min == 5.0
        assert single_dist.max == 5.0
        assert single_dist.q25 == 5.0
        assert single_dist.q75 == 5.0

        two_dist = DistributionStats.from_values([2, 8])
        assert two_dist.count == 2
        assert two_dist.mean == 5.0
        assert two_dist.median == 5.0
        assert two_dist.min == 2.0
        assert two_dist.max == 8.0

        four_dist = DistributionStats.from_values([1, 2, 3, 4])
        assert four_dist.count == 4
        assert four_dist.mean == 2.5
        assert four_dist.median == 2.5
        assert four_dist.min == 1.0
        assert four_dist.max == 4.0

    def test_statistical_aggregator_draws_and_tpks(self):
        """Verify StatisticalAggregator metrics calculation with draws and TPK outcomes."""
        results = [
            SimulationRunResult(
                run_id=0,
                scenario_name="Test",
                victor="allies",
                total_rounds=3,
                allies_survived=True,
                is_tpk=False,
                boss_total_grit=4,
                mob_total_size=2,
            ),
            SimulationRunResult(
                run_id=1,
                scenario_name="Test",
                victor="enemies",
                total_rounds=5,
                allies_survived=False,
                is_tpk=True,
                boss_total_grit=0,
                mob_total_size=0,
            ),
            SimulationRunResult(
                run_id=2,
                scenario_name="Test",
                victor="draw",
                total_rounds=20,
                allies_survived=True,
                is_tpk=False,
                boss_total_grit=2,
                mob_total_size=1,
            ),
        ]

        metrics = StatisticalAggregator.aggregate("Test", results, elapsed_seconds=0.5)
        assert metrics.total_runs == 3
        assert metrics.wins == 1
        assert metrics.losses == 1
        assert metrics.draws == 1
        assert metrics.tpks == 1
        assert abs(metrics.win_rate - 1 / 3) < 1e-4
        assert abs(metrics.loss_rate - 1 / 3) < 1e-4
        assert abs(metrics.draw_rate - 1 / 3) < 1e-4
        assert abs(metrics.tpk_rate - 1 / 3) < 1e-4
        assert metrics.runs_per_second == 6.0

        ascii_table = metrics.format_ascii_table()
        assert "Monte Carlo Simulation: Test" in ascii_table
        assert "Total Party Kill (TPK Rate)" in ascii_table
        assert "Encounter Duration (Rounds)" in ascii_table

    def test_all_reference_scenarios_simulate(self):
        """Verify all preset reference scenarios can run in MonteCarloSimulator."""
        for preset in ["street_skirmish", "maulers_den", "tomb_highwayman"]:
            sim = MonteCarloSimulator.from_preset(preset)
            metrics = sim.run(iterations=50, base_seed=42)
            assert metrics.total_runs == 50
            assert metrics.rounds.mean > 0
