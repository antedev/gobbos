"""Scenario class model and scenario registry for Gobbos combat encounters."""

from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union

from combat_sim.domain.entities import Enemy, GoblinBoss, PlayerMob
from combat_sim.domain.topology import TopologyGraph

if TYPE_CHECKING:
    from combat_sim.engine.combat import CombatEngine, CombatState


@dataclass
class Scenario:
    """Tactical encounter scenario configuration with graph topology and combatant rosters."""

    name: str
    description: str
    topology: TopologyGraph
    allies: List[Union[GoblinBoss, PlayerMob]]
    enemies: List[Enemy]
    victory_condition: Optional[Callable[[Any], bool]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def create_engine(self, rng: Optional[random.Random] = None) -> CombatEngine:
        """Instantiate a ready-to-run CombatEngine for this scenario."""
        from combat_sim.engine.combat import CombatEngine

        return CombatEngine(
            topology=self.topology,
            allies=self.allies,
            enemies=self.enemies,
            scenario_name=self.name,
            rng=rng,
        )


class ScenarioRegistry:
    """Central registry for discovering and instantiating combat scenarios."""

    _registry: Dict[str, Callable[[], Scenario]] = {}
    _descriptions: Dict[str, str] = {}
    _aliases: Dict[str, str] = {}

    @classmethod
    def register(
        cls,
        name: str,
        factory: Callable[[], Scenario],
        description: str = "",
        aliases: Optional[List[str]] = None,
    ) -> None:
        """Register a scenario factory by canonical name with optional aliases."""
        key = cls._normalize_name(name)
        cls._registry[key] = factory
        cls._descriptions[key] = description or name
        cls._aliases[key] = key

        if aliases:
            for alias in aliases:
                norm_alias = cls._normalize_name(alias)
                cls._aliases[norm_alias] = key

    @classmethod
    def get_scenario(cls, name: str) -> Scenario:
        """Retrieve and construct a fresh Scenario instance by name or alias."""
        key = cls._normalize_name(name)
        canonical = cls._aliases.get(key)
        if not canonical or canonical not in cls._registry:
            available = ", ".join(sorted(cls._registry.keys()))
            raise KeyError(
                f"Unknown scenario '{name}'. Available registered scenarios: {available}"
            )
        factory = cls._registry[canonical]
        return factory()

    @classmethod
    def list_scenarios(cls) -> List[str]:
        """Return a sorted list of registered canonical scenario names."""
        return sorted(list(cls._registry.keys()))

    @classmethod
    def list_scenario_details(cls) -> List[Dict[str, Any]]:
        """Return detailed metadata for all registered scenarios."""
        details = []
        for key in cls.list_scenarios():
            details.append(
                {
                    "key": key,
                    "name": cls._descriptions.get(key, key),
                    "description": cls._descriptions.get(key, ""),
                }
            )
        return details

    @classmethod
    def is_registered(cls, name: str) -> bool:
        """Check if a scenario name or alias is registered."""
        key = cls._normalize_name(name)
        return key in cls._aliases

    @classmethod
    def clear(cls) -> None:
        """Clear all registered scenarios (useful for isolated testing)."""
        cls._registry.clear()
        cls._descriptions.clear()
        cls._aliases.clear()

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Normalize scenario name for case-insensitive, punctuation-tolerant lookup."""
        return (
            name.strip()
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
            .replace("'", "")
            .replace("’", "")
        )


def register_default_scenarios() -> None:
    """Register all reference scenarios in the global ScenarioRegistry."""
    from combat_sim.scenarios.maulers_den import build_maulers_den
    from combat_sim.scenarios.street_skirmish import build_street_skirmish
    from combat_sim.scenarios.tomb_highwayman import build_tomb_highwayman

    ScenarioRegistry.register(
        name="street_skirmish",
        factory=build_street_skirmish,
        description=(
            "Street Skirmish: Armored Boss Garg + Size 3 Mob vs Robber Gang and Footpads."
        ),
        aliases=["Street Skirmish", "street", "skirmish"],
    )
    ScenarioRegistry.register(
        name="maulers_den",
        factory=build_maulers_den,
        description=(
            "The Mauler's Den: 2 Heavy Weapon Bosses + 2 Mobs vs Elite Forest Mauler."
        ),
        aliases=[
            "The Mauler's Den",
            "The Maulers Den",
            "maulers_den",
            "mauler_den",
            "mauler",
        ],
    )
    ScenarioRegistry.register(
        name="tomb_highwayman",
        factory=build_tomb_highwayman,
        description=(
            "Tomb of the Highwayman: Boss Wizgog + Size 3 Mob vs Armored Highwayman & Skeletons."
        ),
        aliases=[
            "Tomb of the Highwayman",
            "Tomb of the Highway Man",
            "tomb_highwayman",
            "highwayman",
            "tomb",
        ],
    )


def get_scenario(name: str) -> Scenario:
    """Convenience function to get a Scenario from the default registry."""
    return ScenarioRegistry.get_scenario(name)


def list_scenarios() -> List[str]:
    """Convenience function to list all registered scenario keys."""
    return ScenarioRegistry.list_scenarios()
