"""Combat simulation analytics and Monte Carlo batch engine."""

from combat_sim.analytics.metrics import (
    ABComparisonResult,
    DistributionStats,
    SimulationMetrics,
    SimulationRunResult,
    StatisticalAggregator,
)
from combat_sim.analytics.monte_carlo import (
    MonteCarloSimulator,
    PRESET_SCENARIOS,
    build_maulers_den,
    build_street_skirmish,
    build_tomb_highwayman,
)

__all__ = [
    "ABComparisonResult",
    "DistributionStats",
    "MonteCarloSimulator",
    "PRESET_SCENARIOS",
    "SimulationMetrics",
    "SimulationRunResult",
    "StatisticalAggregator",
    "build_maulers_den",
    "build_street_skirmish",
    "build_tomb_highwayman",
]
