"""Statistical metrics models and aggregators for combat simulations.

Provides:
- DistributionStats: Descriptive statistics (mean, median, stddev, min, max, q25, q75).
- SimulationRunResult: Data record for a single combat simulation iteration.
- SimulationMetrics: Aggregated results across batch Monte Carlo runs.
- ABComparisonResult: Comparative balance analytics between two configurations.
- StatisticalAggregator: Computation engine for metrics and formatted ASCII tables.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import math
import statistics
from typing import Any, Callable, Dict, List, Optional, Sequence, Union


@dataclass(frozen=True)
class DistributionStats:
    """Descriptive statistics for a numeric sample distribution."""
    count: int = 0
    mean: float = 0.0
    median: float = 0.0
    stddev: float = 0.0
    min: float = 0.0
    max: float = 0.0
    q25: float = 0.0
    q75: float = 0.0

    @classmethod
    def from_values(cls, values: Sequence[Union[int, float]]) -> DistributionStats:
        """Calculate distribution statistics from a sequence of numeric values."""
        if not values:
            return cls()

        float_vals = [float(v) for v in values]
        n = len(float_vals)
        sorted_vals = sorted(float_vals)

        mean_val = sum(float_vals) / n
        med_val = statistics.median(sorted_vals)
        std_val = statistics.stdev(float_vals) if n > 1 else 0.0
        min_val = sorted_vals[0]
        max_val = sorted_vals[-1]

        # Calculate 25th and 75th percentiles
        if n >= 4:
            try:
                quants = statistics.quantiles(sorted_vals, n=4)
                q25 = quants[0]
                q75 = quants[2]
            except Exception:
                q25 = sorted_vals[int(0.25 * (n - 1))]
                q75 = sorted_vals[int(0.75 * (n - 1))]
        elif n == 1:
            q25 = float_vals[0]
            q75 = float_vals[0]
        elif n == 2:
            q25 = sorted_vals[0]
            q75 = sorted_vals[1]
        else:  # n == 3
            q25 = sorted_vals[0]
            q75 = sorted_vals[2]

        return cls(
            count=n,
            mean=round(mean_val, 4),
            median=round(med_val, 4),
            stddev=round(std_val, 4),
            min=round(min_val, 4),
            max=round(max_val, 4),
            q25=round(q25, 4),
            q75=round(q75, 4),
        )

    def to_dict(self) -> Dict[str, float]:
        """Convert statistics to dictionary."""
        return {
            "count": float(self.count),
            "mean": self.mean,
            "median": self.median,
            "stddev": self.stddev,
            "min": self.min,
            "max": self.max,
            "q25": self.q25,
            "q75": self.q75,
        }

    def format_compact(self) -> str:
        """Compact string representation: mean ± stddev [min, med, max]."""
        if self.count == 0:
            return "N/A"
        return f"{self.mean:.2f} ± {self.stddev:.2f} [min={self.min:.1f}, med={self.median:.1f}, max={self.max:.1f}]"


@dataclass
class SimulationRunResult:
    """Detailed outcome record of a single combat encounter execution."""
    run_id: int
    scenario_name: str
    victor: str  # "allies", "enemies", "draw"
    total_rounds: int
    allies_survived: bool
    is_tpk: bool
    boss_grit_remaining: Dict[str, int] = field(default_factory=dict)
    boss_total_grit: int = 0
    mob_sizes_remaining: Dict[str, int] = field(default_factory=dict)
    mob_total_size: int = 0
    initial_mob_size: int = 0
    mob_casualties: int = 0
    enemies_killed: int = 0
    total_casualties: int = 0
    seed: Optional[int] = None

    @classmethod
    def from_combat_summary(
        cls,
        summary: Any,
        run_id: int = 0,
        initial_mob_size: int = 0,
        seed: Optional[int] = None,
    ) -> SimulationRunResult:
        """Construct a run record from a CombatSummary dataclass."""
        boss_grit = getattr(summary, "boss_grit_remaining", {})
        mob_sizes = getattr(summary, "mob_sizes_remaining", {})
        victor = getattr(summary, "victor", "draw")
        allies_survived = getattr(summary, "allies_survived", False)

        boss_total = sum(boss_grit.values())
        mob_total = sum(mob_sizes.values())
        is_tpk = (not allies_survived) or (boss_total == 0 and mob_total == 0)

        calc_mob_casualties = max(0, initial_mob_size - mob_total) if initial_mob_size > 0 else 0

        return cls(
            run_id=run_id,
            scenario_name=getattr(summary, "scenario_name", "Scenario"),
            victor=victor,
            total_rounds=getattr(summary, "total_rounds", 0),
            allies_survived=allies_survived,
            is_tpk=is_tpk,
            boss_grit_remaining=dict(boss_grit),
            boss_total_grit=boss_total,
            mob_sizes_remaining=dict(mob_sizes),
            mob_total_size=mob_total,
            initial_mob_size=initial_mob_size,
            mob_casualties=calc_mob_casualties,
            enemies_killed=getattr(summary, "enemies_killed", 0),
            total_casualties=getattr(summary, "total_casualties", 0),
            seed=seed,
        )


@dataclass
class SimulationMetrics:
    """Aggregated statistical performance metrics from a batch simulation."""
    scenario_name: str
    total_runs: int
    wins: int
    losses: int
    draws: int
    tpks: int
    win_rate: float
    loss_rate: float
    draw_rate: float
    tpk_rate: float
    rounds: DistributionStats
    boss_grit: DistributionStats
    boss_grit_by_name: Dict[str, DistributionStats] = field(default_factory=dict)
    mob_surviving_size: DistributionStats = field(default_factory=DistributionStats)
    mob_casualties: DistributionStats = field(default_factory=DistributionStats)
    mob_sizes_by_name: Dict[str, DistributionStats] = field(default_factory=dict)
    enemies_killed: DistributionStats = field(default_factory=DistributionStats)
    elapsed_time_seconds: float = 0.0
    runs_per_second: float = 0.0
    results: List[SimulationRunResult] = field(default_factory=list)

    def summary_line(self) -> str:
        """One-line summary of key metrics."""
        return (
            f"[{self.scenario_name}] {self.total_runs:,} runs in {self.elapsed_time_seconds:.3f}s "
            f"({self.runs_per_second:,.1f} runs/s) | "
            f"Win: {self.win_rate * 100:.1f}% | Loss: {self.loss_rate * 100:.1f}% | "
            f"TPK: {self.tpk_rate * 100:.1f}% | Rounds: {self.rounds.mean:.2f} ± {self.rounds.stddev:.2f} | "
            f"Boss Grit: {self.boss_grit.mean:.2f} | Mob Surv: {self.mob_surviving_size.mean:.2f}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert metrics to a nested dictionary representation."""
        return {
            "scenario_name": self.scenario_name,
            "total_runs": self.total_runs,
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "tpks": self.tpks,
            "win_rate": self.win_rate,
            "loss_rate": self.loss_rate,
            "draw_rate": self.draw_rate,
            "tpk_rate": self.tpk_rate,
            "rounds": self.rounds.to_dict(),
            "boss_grit": self.boss_grit.to_dict(),
            "boss_grit_by_name": {k: v.to_dict() for k, v in self.boss_grit_by_name.items()},
            "mob_surviving_size": self.mob_surviving_size.to_dict(),
            "mob_casualties": self.mob_casualties.to_dict(),
            "mob_sizes_by_name": {k: v.to_dict() for k, v in self.mob_sizes_by_name.items()},
            "enemies_killed": self.enemies_killed.to_dict(),
            "elapsed_time_seconds": self.elapsed_time_seconds,
            "runs_per_second": self.runs_per_second,
        }

    def format_ascii_table(self, title: Optional[str] = None) -> str:
        """Format metrics into a clean, human-readable ASCII summary table."""
        table_title = title or f"Monte Carlo Simulation: {self.scenario_name}"
        width = 72
        sep = "=" * width
        thin_sep = "-" * width

        lines = [
            sep,
            f" {table_title.center(width - 2)} ",
            sep,
            f" Total Iterations : {self.total_runs:>10,d}     Elapsed Time : {self.elapsed_time_seconds:>8.4f}s",
            f" Simulation Speed : {self.runs_per_second:>10,.1f} runs/s",
            thin_sep,
            " OUTCOME RATES".center(width),
            thin_sep,
            f"  Goblin Party Victories (Win)  : {self.wins:>6,d}  ({self.win_rate * 100:>6.2f}%)",
            f"  Enemy Victories (Loss)        : {self.losses:>6,d}  ({self.loss_rate * 100:>6.2f}%)",
            f"  Draw / Max Round Limit        : {self.draws:>6,d}  ({self.draw_rate * 100:>6.2f}%)",
            f"  Total Party Kill (TPK Rate)   : {self.tpks:>6,d}  ({self.tpk_rate * 100:>6.2f}%)",
            thin_sep,
            f" {'METRIC DISTRIBUTION':<26} | {'MEAN':>8} | {'MEDIAN':>6} | {'STDDEV':>6} | {'MIN':>4} | {'MAX':>4}",
            thin_sep,
            f" {'Encounter Duration (Rounds)':<26} | {self.rounds.mean:>8.2f} | {self.rounds.median:>6.1f} | {self.rounds.stddev:>6.2f} | {self.rounds.min:>4.0f} | {self.rounds.max:>4.0f}",
            f" {'Boss Grit Remaining':<26} | {self.boss_grit.mean:>8.2f} | {self.boss_grit.median:>6.1f} | {self.boss_grit.stddev:>6.2f} | {self.boss_grit.min:>4.0f} | {self.boss_grit.max:>4.0f}",
            f" {'Surviving Mob Size':<26} | {self.mob_surviving_size.mean:>8.2f} | {self.mob_surviving_size.median:>6.1f} | {self.mob_surviving_size.stddev:>6.2f} | {self.mob_surviving_size.min:>4.0f} | {self.mob_surviving_size.max:>4.0f}",
            f" {'Mob Casualties':<26} | {self.mob_casualties.mean:>8.2f} | {self.mob_casualties.median:>6.1f} | {self.mob_casualties.stddev:>6.2f} | {self.mob_casualties.min:>4.0f} | {self.mob_casualties.max:>4.0f}",
            f" {'Enemies Defeated':<26} | {self.enemies_killed.mean:>8.2f} | {self.enemies_killed.median:>6.1f} | {self.enemies_killed.stddev:>6.2f} | {self.enemies_killed.min:>4.0f} | {self.enemies_killed.max:>4.0f}",
        ]

        if self.boss_grit_by_name:
            lines.append(thin_sep)
            lines.append(" PER-BOSS GRIT BREAKDOWN".center(width))
            lines.append(thin_sep)
            for boss_name, dist in self.boss_grit_by_name.items():
                label = f"Boss: {boss_name}"
                lines.append(
                    f" {label:<26} | {dist.mean:>8.2f} | {dist.median:>6.1f} | {dist.stddev:>6.2f} | {dist.min:>4.0f} | {dist.max:>4.0f}"
                )

        if self.mob_sizes_by_name:
            lines.append(thin_sep)
            lines.append(" PER-MOB SURVIVAL BREAKDOWN".center(width))
            lines.append(thin_sep)
            for mob_name, dist in self.mob_sizes_by_name.items():
                label = f"Mob: {mob_name}"
                lines.append(
                    f" {label:<26} | {dist.mean:>8.2f} | {dist.median:>6.1f} | {dist.stddev:>6.2f} | {dist.min:>4.0f} | {dist.max:>4.0f}"
                )

        lines.append(sep)
        return "\n".join(lines)


@dataclass
class ABComparisonResult:
    """Comparative analysis results between two simulation configurations (A vs B)."""
    name_a: str
    name_b: str
    metrics_a: SimulationMetrics
    metrics_b: SimulationMetrics
    win_rate_delta: float
    loss_rate_delta: float
    tpk_rate_delta: float
    mean_rounds_delta: float
    mean_grit_delta: float
    mean_mob_size_delta: float
    mean_casualties_delta: float

    def to_dict(self) -> Dict[str, Any]:
        """Convert A/B comparison to dictionary."""
        return {
            "name_a": self.name_a,
            "name_b": self.name_b,
            "config_a": self.metrics_a.to_dict(),
            "config_b": self.metrics_b.to_dict(),
            "deltas": {
                "win_rate": self.win_rate_delta,
                "loss_rate": self.loss_rate_delta,
                "tpk_rate": self.tpk_rate_delta,
                "mean_rounds": self.mean_rounds_delta,
                "mean_boss_grit": self.mean_grit_delta,
                "mean_mob_size": self.mean_mob_size_delta,
                "mean_mob_casualties": self.mean_casualties_delta,
            },
        }

    def format_ascii_table(self, title: Optional[str] = None) -> str:
        """Format A/B balance comparison into a clean ASCII table."""
        table_title = title or f"A/B Balance Comparison: {self.name_a} vs {self.name_b}"
        width = 82
        sep = "=" * width
        thin_sep = "-" * width

        def fmt_delta(val: float, is_pct: bool = False) -> str:
            sign = "+" if val > 0 else ""
            if is_pct:
                return f"{sign}{val * 100:.2f}%"
            return f"{sign}{val:.2f}"

        lines = [
            sep,
            f" {table_title.center(width - 2)} ",
            sep,
            f" {'METRIC':<30} | {self.name_a[:16]:>16} | {self.name_b[:16]:>16} | {'DELTA (B - A)':>12}",
            thin_sep,
            f" {'Sample Size (Iterations)':<30} | {self.metrics_a.total_runs:>16,d} | {self.metrics_b.total_runs:>16,d} | {'--':>12}",
            f" {'Win Rate (%)':<30} | {self.metrics_a.win_rate * 100:>15.2f}% | {self.metrics_b.win_rate * 100:>15.2f}% | {fmt_delta(self.win_rate_delta, is_pct=True):>12}",
            f" {'Loss Rate (%)':<30} | {self.metrics_a.loss_rate * 100:>15.2f}% | {self.metrics_b.loss_rate * 100:>15.2f}% | {fmt_delta(self.loss_rate_delta, is_pct=True):>12}",
            f" {'TPK Rate (%)':<30} | {self.metrics_a.tpk_rate * 100:>15.2f}% | {self.metrics_b.tpk_rate * 100:>15.2f}% | {fmt_delta(self.tpk_rate_delta, is_pct=True):>12}",
            thin_sep,
            f" {'Mean Duration (Rounds)':<30} | {self.metrics_a.rounds.mean:>16.2f} | {self.metrics_b.rounds.mean:>16.2f} | {fmt_delta(self.mean_rounds_delta):>12}",
            f" {'Mean Boss Grit Remaining':<30} | {self.metrics_a.boss_grit.mean:>16.2f} | {self.metrics_b.boss_grit.mean:>16.2f} | {fmt_delta(self.mean_grit_delta):>12}",
            f" {'Mean Surviving Mob Size':<30} | {self.metrics_a.mob_surviving_size.mean:>16.2f} | {self.metrics_b.mob_surviving_size.mean:>16.2f} | {fmt_delta(self.mean_mob_size_delta):>12}",
            f" {'Mean Mob Casualties':<30} | {self.metrics_a.mob_casualties.mean:>16.2f} | {self.metrics_b.mob_casualties.mean:>16.2f} | {fmt_delta(self.mean_casualties_delta):>12}",
            f" {'Mean Enemies Defeated':<30} | {self.metrics_a.enemies_killed.mean:>16.2f} | {self.metrics_b.enemies_killed.mean:>16.2f} | {fmt_delta(self.metrics_b.enemies_killed.mean - self.metrics_a.enemies_killed.mean):>12}",
            sep,
        ]
        return "\n".join(lines)


class StatisticalAggregator:
    """Aggregates combat iteration outcomes into statistical metrics and comparisons."""

    @staticmethod
    def aggregate(
        scenario_name: str,
        results: Sequence[Union[SimulationRunResult, Any]],
        elapsed_seconds: float = 0.0,
    ) -> SimulationMetrics:
        """Compute comprehensive summary metrics over a batch of run outcomes."""
        total_runs = len(results)
        if total_runs == 0:
            empty_dist = DistributionStats()
            return SimulationMetrics(
                scenario_name=scenario_name,
                total_runs=0,
                wins=0,
                losses=0,
                draws=0,
                tpks=0,
                win_rate=0.0,
                loss_rate=0.0,
                draw_rate=0.0,
                tpk_rate=0.0,
                rounds=empty_dist,
                boss_grit=empty_dist,
                mob_surviving_size=empty_dist,
                mob_casualties=empty_dist,
                enemies_killed=empty_dist,
                elapsed_time_seconds=elapsed_seconds,
                runs_per_second=0.0,
                results=[],
            )

        # Standardize items to SimulationRunResult
        standardized_results: List[SimulationRunResult] = []
        for i, r in enumerate(results):
            if isinstance(r, SimulationRunResult):
                standardized_results.append(r)
            elif isinstance(r, dict):
                # Lightweight dictionary outcome
                victor = "allies" if r.get("victory", 0.0) >= 1.0 else ("enemies" if r.get("boss_grit", 0.0) <= 0 and r.get("mob_size", 0.0) <= 0 else "draw")
                boss_grit = int(r.get("boss_grit", 0))
                mob_size = int(r.get("mob_size", 0))
                standardized_results.append(
                    SimulationRunResult(
                        run_id=i,
                        scenario_name=scenario_name,
                        victor=victor,
                        total_rounds=int(r.get("rounds", 0)),
                        allies_survived=(boss_grit > 0 or mob_size > 0),
                        is_tpk=(boss_grit <= 0 and mob_size <= 0),
                        boss_grit_remaining={"Boss": boss_grit},
                        boss_total_grit=boss_grit,
                        mob_sizes_remaining={"Mob": mob_size},
                        mob_total_size=mob_size,
                        initial_mob_size=int(r.get("initial_mob_size", mob_size)),
                        mob_casualties=int(r.get("mob_casualties", 0)),
                        enemies_killed=int(r.get("enemies_killed", 0)),
                    )
                )
            else:
                # CombatSummary or object
                standardized_results.append(
                    SimulationRunResult.from_combat_summary(r, run_id=i)
                )

        # Outcome tallies
        wins = sum(1 for r in standardized_results if r.victor == "allies")
        losses = sum(1 for r in standardized_results if r.victor == "enemies")
        draws = sum(1 for r in standardized_results if r.victor == "draw")
        tpks = sum(1 for r in standardized_results if r.is_tpk)

        win_rate = wins / total_runs
        loss_rate = losses / total_runs
        draw_rate = draws / total_runs
        tpk_rate = tpks / total_runs

        # Distributions
        rounds_dist = DistributionStats.from_values([r.total_rounds for r in standardized_results])
        boss_grit_dist = DistributionStats.from_values([r.boss_total_grit for r in standardized_results])
        mob_surv_dist = DistributionStats.from_values([r.mob_total_size for r in standardized_results])
        mob_cas_dist = DistributionStats.from_values([r.mob_casualties for r in standardized_results])
        enemies_dist = DistributionStats.from_values([r.enemies_killed for r in standardized_results])

        # Per-Boss grit distributions
        all_boss_names = set()
        for r in standardized_results:
            all_boss_names.update(r.boss_grit_remaining.keys())

        boss_grit_by_name = {}
        for b_name in sorted(all_boss_names):
            vals = [r.boss_grit_remaining.get(b_name, 0) for r in standardized_results]
            boss_grit_by_name[b_name] = DistributionStats.from_values(vals)

        # Per-Mob size distributions
        all_mob_names = set()
        for r in standardized_results:
            all_mob_names.update(r.mob_sizes_remaining.keys())

        mob_sizes_by_name = {}
        for m_name in sorted(all_mob_names):
            vals = [r.mob_sizes_remaining.get(m_name, 0) for r in standardized_results]
            mob_sizes_by_name[m_name] = DistributionStats.from_values(vals)

        runs_per_second = (total_runs / elapsed_seconds) if elapsed_seconds > 0 else 0.0

        return SimulationMetrics(
            scenario_name=scenario_name,
            total_runs=total_runs,
            wins=wins,
            losses=losses,
            draws=draws,
            tpks=tpks,
            win_rate=win_rate,
            loss_rate=loss_rate,
            draw_rate=draw_rate,
            tpk_rate=tpk_rate,
            rounds=rounds_dist,
            boss_grit=boss_grit_dist,
            boss_grit_by_name=boss_grit_by_name,
            mob_surviving_size=mob_surv_dist,
            mob_casualties=mob_cas_dist,
            mob_sizes_by_name=mob_sizes_by_name,
            enemies_killed=enemies_dist,
            elapsed_time_seconds=elapsed_seconds,
            runs_per_second=runs_per_second,
            results=standardized_results,
        )

    @staticmethod
    def compare_ab(
        metrics_a: SimulationMetrics,
        metrics_b: SimulationMetrics,
        name_a: Optional[str] = None,
        name_b: Optional[str] = None,
    ) -> ABComparisonResult:
        """Compare two simulation metric sets and compute balance deltas (B - A)."""
        label_a = name_a or metrics_a.scenario_name
        label_b = name_b or metrics_b.scenario_name

        return ABComparisonResult(
            name_a=label_a,
            name_b=label_b,
            metrics_a=metrics_a,
            metrics_b=metrics_b,
            win_rate_delta=metrics_b.win_rate - metrics_a.win_rate,
            loss_rate_delta=metrics_b.loss_rate - metrics_a.loss_rate,
            tpk_rate_delta=metrics_b.tpk_rate - metrics_a.tpk_rate,
            mean_rounds_delta=metrics_b.rounds.mean - metrics_a.rounds.mean,
            mean_grit_delta=metrics_b.boss_grit.mean - metrics_a.boss_grit.mean,
            mean_mob_size_delta=metrics_b.mob_surviving_size.mean - metrics_a.mob_surviving_size.mean,
            mean_casualties_delta=metrics_b.mob_casualties.mean - metrics_a.mob_casualties.mean,
        )
