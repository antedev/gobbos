"""Main CLI application entrypoint for the Gobbos Combat Simulator.

Provides full command-line interfaces for:
- `run`: Single-encounter interactive or scripted turn-by-turn simulation.
- `batch`: High-performance Monte Carlo statistical batch analysis.
- `list-scenarios`: Catalog of available pre-built scenarios and rules configurations.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from typing import Any, Dict, List, Optional

from combat_sim.cli.runner import (
    InteractiveRunner,
    SCENARIO_REGISTRY,
    create_engine_for_scenario,
    get_available_scenarios,
    load_scenario,
)
from combat_sim.core.events import AnsiColor, CombatEventFormatter
from combat_sim.domain.entities import GoblinBoss, PlayerMob


def run_batch_simulation(
    scenario_name: str,
    iterations: int = 1000,
    seed: int = 42,
    max_rounds: int = 50,
    colorize: bool = True,
) -> Dict[str, Any]:
    """Execute high-performance Monte Carlo batch simulation and return statistical metrics."""
    formatter = CombatEventFormatter(colorize=colorize)
    use_color = formatter.colorize

    print(formatter._style("=" * 70, AnsiColor.BOLD, AnsiColor.CYAN, force_color=use_color))
    print(formatter._style(f"  RUNNING MONTE CARLO BATCH SIMULATION: {scenario_name}".center(70), AnsiColor.BOLD, AnsiColor.BRIGHT_CYAN, force_color=use_color))
    print(formatter._style(f"  Iterations: {iterations:,} | Base Seed: {seed} | Max Rounds: {max_rounds}".center(70), AnsiColor.DIM, force_color=use_color))
    print(formatter._style("=" * 70, AnsiColor.BOLD, AnsiColor.CYAN, force_color=use_color))

    start_time = time.perf_counter()

    wins = 0
    losses = 0
    draws = 0
    round_counts: List[int] = []
    boss_grit_totals: Dict[str, List[int]] = {}
    mob_size_totals: Dict[str, List[int]] = {}
    total_enemies_killed = 0
    total_ally_casualties = 0

    for i in range(iterations):
        run_seed = seed + i
        engine = create_engine_for_scenario(scenario_name, seed=run_seed)
        summary = engine.run_to_completion(max_rounds=max_rounds)

        if summary.victor == "allies":
            wins += 1
        elif summary.victor == "enemies":
            losses += 1
        else:
            draws += 1

        round_counts.append(summary.total_rounds)
        total_enemies_killed += summary.enemies_killed
        total_ally_casualties += summary.total_casualties

        for bname, grit in summary.boss_grit_remaining.items():
            if bname not in boss_grit_totals:
                boss_grit_totals[bname] = []
            boss_grit_totals[bname].append(grit)

        for mname, size in summary.mob_sizes_remaining.items():
            if mname not in mob_size_totals:
                mob_size_totals[mname] = []
            mob_size_totals[mname].append(size)

    elapsed = time.perf_counter() - start_time
    runs_per_sec = iterations / max(0.0001, elapsed)

    # Calculate statistics
    win_pct = (wins / iterations) * 100.0
    loss_pct = (losses / iterations) * 100.0
    draw_pct = (draws / iterations) * 100.0
    avg_rounds = sum(round_counts) / max(1, len(round_counts))
    min_rounds = min(round_counts) if round_counts else 0
    max_rounds_obs = max(round_counts) if round_counts else 0

    divider = "-" * 70
    border = "=" * 70

    print(f"\n{formatter._style('>>> AGGREGATED BATCH RESULTS <<<'.center(70), AnsiColor.BOLD, force_color=use_color)}")
    print(formatter._style(divider, AnsiColor.DIM, force_color=use_color))

    # Outcomes
    win_str = formatter._style(f"{wins:,} ({win_pct:.1f}%)", AnsiColor.BOLD, AnsiColor.BRIGHT_GREEN, force_color=use_color)
    loss_str = formatter._style(f"{losses:,} ({loss_pct:.1f}%)", AnsiColor.BOLD, AnsiColor.BRIGHT_RED, force_color=use_color)
    draw_str = formatter._style(f"{draws:,} ({draw_pct:.1f}%)", AnsiColor.YELLOW, force_color=use_color)

    print(f"  • Goblin Party Victories (Wins): {win_str}")
    print(f"  • Enemy Victories / TPK (Losses): {loss_str}")
    print(f"  • Stalemate / Timeout (Draws):   {draw_str}")
    print(formatter._style(divider, AnsiColor.DIM, force_color=use_color))

    # Round statistics
    print(f"  • Encounter Duration: Avg {avg_rounds:.2f} rounds (Min: {min_rounds}, Max: {max_rounds_obs})")
    print(f"  • Avg Enemies Killed per Run: {total_enemies_killed / max(1, iterations):.2f}")
    print(f"  • Avg Ally Casualties per Run: {total_ally_casualties / max(1, iterations):.2f}")

    # Boss grit statistics
    if boss_grit_totals:
        print("\n  • Boss Survival & Grit Metrics:")
        for bname, grits in boss_grit_totals.items():
            avg_g = sum(grits) / max(1, len(grits))
            surv = sum(1 for g in grits if g > 0)
            surv_pct = (surv / iterations) * 100.0
            print(f"    - {bname}: Avg {avg_g:.2f} Grit remaining | Survival: {surv_pct:.1f}%")

    # Mob survival statistics
    if mob_size_totals:
        print("\n  • Mob Survival & Size Metrics:")
        for mname, sizes in mob_size_totals.items():
            avg_s = sum(sizes) / max(1, len(sizes))
            surv = sum(1 for s in sizes if s > 0)
            surv_pct = (surv / iterations) * 100.0
            print(f"    - {mname}: Avg Size {avg_s:.2f} remaining | Survival: {surv_pct:.1f}%")

    print(formatter._style(divider, AnsiColor.DIM, force_color=use_color))
    perf_str = formatter._style(f"{elapsed:.3f}s ({runs_per_sec:,.0f} runs/sec)", AnsiColor.BOLD, AnsiColor.CYAN, force_color=use_color)
    print(f"  • Performance: Completed {iterations:,} iterations in {perf_str}")
    print(formatter._style(border, AnsiColor.BOLD, AnsiColor.CYAN, force_color=use_color))

    return {
        "scenario": scenario_name,
        "iterations": iterations,
        "wins": wins,
        "losses": losses,
        "draws": draws,
        "win_rate": win_pct,
        "loss_rate": loss_pct,
        "draw_rate": draw_pct,
        "avg_rounds": avg_rounds,
        "elapsed_seconds": elapsed,
        "runs_per_second": runs_per_sec,
    }


def handle_list_scenarios(colorize: bool = True) -> None:
    """List all pre-built scenarios and registered blueprints."""
    formatter = CombatEventFormatter(colorize=colorize)
    use_color = formatter.colorize

    print(formatter._style("=" * 70, AnsiColor.BOLD, AnsiColor.YELLOW, force_color=use_color))
    print(formatter._style("  AVAILABLE GOBBOS COMBAT SCENARIOS".center(70), AnsiColor.BOLD, AnsiColor.BRIGHT_YELLOW, force_color=use_color))
    print(formatter._style("=" * 70, AnsiColor.BOLD, AnsiColor.YELLOW, force_color=use_color))

    scenarios = get_available_scenarios()
    for idx, (key, spec) in enumerate(scenarios.items(), 1):
        name_styled = formatter._style(spec["name"], AnsiColor.BOLD, AnsiColor.BRIGHT_CYAN, force_color=use_color)
        key_styled = formatter._style(f"[ID: {key}]", AnsiColor.DIM, force_color=use_color)
        aliases = ", ".join(f"'{a}'" for a in spec.get("aliases", []))
        print(f"\n  {idx}. {name_styled} {key_styled}")
        print(f"     Description: {spec['description']}")
        print(f"     Aliases: {aliases}")

    print(formatter._style("\n" + "=" * 70, AnsiColor.BOLD, AnsiColor.YELLOW, force_color=use_color))
    print("  Run a scenario with: python -m combat_sim.cli.main run --scenario <id>")
    print("  Batch analysis with: python -m combat_sim.cli.main batch --scenario <id> --iterations 1000")


def build_parser() -> argparse.ArgumentParser:
    """Construct the main CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="gobbos-sim",
        description="Gobbos TTRPG Tactical Combat Simulation & Balance Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # 1. 'run' subcommand
    run_parser = subparsers.add_parser("run", help="Run a single encounter (interactive or scripted)")
    run_parser.add_argument(
        "-s", "--scenario",
        required=True,
        help="Scenario identifier (e.g. street_skirmish, maulers_den, tomb_highwayman)",
    )
    run_parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        default=False,
        help="Enable step-by-step interactive mode with keyboard stepping prompts",
    )
    run_parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random number generator seed (default: non-deterministic)",
    )
    run_parser.add_argument(
        "-m", "--max-rounds",
        type=int,
        default=50,
        help="Maximum combat rounds before declaring a draw (default: 50)",
    )
    run_parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help="Disable ANSI color escape sequences",
    )

    # 2. 'batch' subcommand
    batch_parser = subparsers.add_parser("batch", help="Run Monte Carlo statistical batch analysis")
    batch_parser.add_argument(
        "-s", "--scenario",
        required=True,
        help="Scenario identifier (e.g. street_skirmish, maulers_den, tomb_highwayman)",
    )
    batch_parser.add_argument(
        "-n", "--iterations", "--runs",
        type=int,
        default=1000,
        help="Number of Monte Carlo iterations to simulate (default: 1000)",
    )
    batch_parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Base random number generator seed (default: 42)",
    )
    batch_parser.add_argument(
        "-m", "--max-rounds",
        type=int,
        default=50,
        help="Maximum combat rounds per iteration (default: 50)",
    )
    batch_parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help="Disable ANSI color escape sequences",
    )

    # 3. 'list-scenarios' subcommand
    list_parser = subparsers.add_parser("list-scenarios", help="List all available reference scenarios")
    list_parser.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help="Disable ANSI color escape sequences",
    )

    return parser


def main(args: Optional[List[str]] = None) -> int:
    """CLI application entrypoint."""
    parser = build_parser()
    parsed = parser.parse_args(args)

    if not parsed.command:
        parser.print_help()
        return 0

    colorize = not getattr(parsed, "no_color", False)

    if parsed.command == "list-scenarios":
        handle_list_scenarios(colorize=colorize)
        return 0

    elif parsed.command == "run":
        runner = InteractiveRunner(
            scenario_name=parsed.scenario,
            interactive=parsed.interactive,
            seed=parsed.seed,
            max_rounds=parsed.max_rounds,
            colorize=colorize,
        )
        runner.run()
        return 0

    elif parsed.command == "batch":
        run_batch_simulation(
            scenario_name=parsed.scenario,
            iterations=parsed.iterations,
            seed=parsed.seed,
            max_rounds=parsed.max_rounds,
            colorize=colorize,
        )
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
