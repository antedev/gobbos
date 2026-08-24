"""Pre-built reference scenarios and scenario registry for Gobbos combat simulator."""

from __future__ import annotations

from combat_sim.scenarios.maulers_den import (
    build_maulers_den,
    create_maulers_den,
)
from combat_sim.scenarios.registry import (
    Scenario,
    ScenarioRegistry,
    get_scenario,
    list_scenarios,
    register_default_scenarios,
)
from combat_sim.scenarios.street_skirmish import (
    build_street_skirmish,
    create_street_skirmish,
)
from combat_sim.scenarios.tomb_highwayman import (
    build_tomb_highwayman,
    create_tomb_highwayman,
)

# Auto-register all reference scenarios into the global ScenarioRegistry
register_default_scenarios()

__all__ = [
    "Scenario",
    "ScenarioRegistry",
    "get_scenario",
    "list_scenarios",
    "register_default_scenarios",
    "build_street_skirmish",
    "create_street_skirmish",
    "build_maulers_den",
    "create_maulers_den",
    "build_tomb_highwayman",
    "create_tomb_highwayman",
]
