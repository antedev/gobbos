"""CLI module for Gobbos Combat Simulation & Balance Toolkit.

Exports the interactive runner, CLI entrypoint, and scenario loader utilities.
"""

from combat_sim.cli.runner import (
    InteractiveRunner,
    SCENARIO_REGISTRY,
    create_engine_for_scenario,
    get_available_scenarios,
    load_scenario,
)

__all__ = [
    "InteractiveRunner",
    "SCENARIO_REGISTRY",
    "create_engine_for_scenario",
    "get_available_scenarios",
    "load_scenario",
]
