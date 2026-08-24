"""Monte Carlo batch simulation engine and throughput runner for tactical combat encounters.

Provides:
- MonteCarloSimulator: High-throughput batch simulation engine (1,000+ runs in < 10.0s).
- Pre-built scenario factories (Street Skirmish, The Mauler's Den, Tomb of the Highwayman).
- A/B balance testing and comparative analytics.
"""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
import inspect
import random
import time
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from combat_sim.core.types import (
    Ancestry,
    Condition,
    CoverType,
    Difficulty,
    EnemyScale,
    Tag,
    ThreatProfile,
    WeaponTrait,
    ZoneTraitType,
)
from combat_sim.domain.entities import (
    EliteEnemy,
    Enemy,
    EnemyMob,
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
    ThreatAttack,
)
from combat_sim.domain.equipment import (
    create_dwarven_great_hammer,
    create_heavy_armor,
    create_heavy_greataxe,
    create_light_armor,
    create_medium_armor,
    create_notched_sword,
    create_pot_lid_shield,
    create_shortbow,
    create_sling,
    create_spiked_mace,
)
from combat_sim.domain.quirks import AnkleBite, MeatShield, PushLuck, SecondWind
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import (
    BeastAncestryTrait,
    DryBones,
    HumanoidAncestryTrait,
    ParryingBuckler,
    ThickBlubber,
    UndeadAncestryTrait,
    VoraciousRegrowth,
)
from combat_sim.engine.combat import CombatEngine, CombatSummary
from combat_sim.analytics.metrics import (
    ABComparisonResult,
    DistributionStats,
    SimulationMetrics,
    SimulationRunResult,
    StatisticalAggregator,
)


ScenarioTuple = Tuple[TopologyGraph, List[Union[GoblinBoss, PlayerMob]], List[Enemy]]
ScenarioFactory = Callable[..., ScenarioTuple]


# =============================================================================
# Reference Scenario Factories
# =============================================================================

def build_street_skirmish() -> ScenarioTuple:
    """Scenario 1: Street Skirmish.

    Armored Boss (Shield + Sword + Medium Armor + Ankle Bite) + Size 3 Mob
    vs Robber Gang (Size 3) + Footpad Shiv + Footpad Slinger across 3 zones with Partial Cover.
    """
    topo = TopologyGraph()
    z_west = Zone(id="street_west", name="Street West", profile=ZoneProfile(Difficulty.NORMAL, 1))
    z_center = Zone(
        id="street_center",
        name="Street Center",
        profile=ZoneProfile(Difficulty.NORMAL, 1),
        cover=CoverType.PARTIAL,
    )
    z_east = Zone(
        id="alley_east",
        name="Alley East",
        profile=ZoneProfile(Difficulty.NORMAL, 1),
        traits=[ZoneTrait(ZoneTraitType.NARROW)],
    )
    topo.add_zone(z_west)
    topo.add_zone(z_center)
    topo.add_zone(z_east)
    topo.connect("street_west", "street_center")
    topo.connect("street_center", "alley_east")

    boss = GoblinBoss(
        id="garg",
        name="Boss Garg",
        zone_id="street_west",
        tough=2,
        slink=2,
        mouth=2,
        brains=1,
        grunt=2,
        main_hand=create_notched_sword(),
        off_hand=create_pot_lid_shield(),
        armor=create_medium_armor(),
        quirks=[AnkleBite()],
    )

    mob = PlayerMob(
        id="runts",
        name="Garg's Runts",
        zone_id="street_west",
        size=3,
        boss_id="garg",
    )

    robber_gang = EnemyMob(
        id="robbers",
        name="Robber Gang",
        zone_id="street_center",
        size=3,
        defence_tn=1,
        movement=2,
        morale_tn=2,
        base_damage=1,
        attacks=[
            ThreatAttack(
                name="Shiv Swarm",
                threat_stat="Slink",
                difficulty=Difficulty.NORMAL,
                threat_tn=1,
                damage=3,
            )
        ],
    )

    footpad_a = StandardEnemy(
        id="footpad_a",
        name="Footpad Shiv",
        zone_id="street_center",
        defence_tn=1,
        movement=2,
        morale_tn=1,
        attacks=[ThreatAttack(name="Rusty Shiv", threat_stat="Slink", threat_tn=1, damage=1)],
    )

    footpad_b = StandardEnemy(
        id="footpad_b",
        name="Footpad Slinger",
        zone_id="alley_east",
        defence_tn=1,
        movement=2,
        morale_tn=1,
        attacks=[
            ThreatAttack(
                name="Thrown Cobblestone",
                threat_stat="Slink",
                threat_tn=1,
                damage=1,
                range_zones=1,
            )
        ],
    )

    return topo, [boss, mob], [robber_gang, footpad_a, footpad_b]


def build_maulers_den() -> ScenarioTuple:
    """Scenario 2: The Mauler's Den.

    2 Heavy Weapon Bosses (Greataxes + Meat Shield) + 2 Mobs (Size 2 & 3)
    vs Forest Mauler (Elite Bear, Wounds 3, Thick Blubber, Cleave) in 2 cave zones.
    """
    topo = TopologyGraph()
    z_entrance = Zone(
        id="den_entrance",
        name="Den Entrance",
        profile=ZoneProfile(Difficulty.NORMAL, 2),
        traits=[ZoneTrait(ZoneTraitType.NARROW)],
    )
    z_main = Zone(
        id="main_den",
        name="Main Den",
        profile=ZoneProfile(Difficulty.NORMAL, 2),
        traits=[
            ZoneTrait(ZoneTraitType.RUBBLE),
            ZoneTrait(ZoneTraitType.PILLARS),
        ],
    )
    topo.add_zone(z_entrance)
    topo.add_zone(z_main)
    topo.connect("den_entrance", "main_den")

    boss1 = GoblinBoss(
        id="skag",
        name="Boss Skag",
        zone_id="den_entrance",
        tough=3,
        slink=1,
        mouth=2,
        brains=1,
        grunt=2,
        main_hand=create_heavy_greataxe(),
        armor=create_light_armor(),
        quirks=[MeatShield()],
    )

    boss2 = GoblinBoss(
        id="grub",
        name="Boss Grub",
        zone_id="den_entrance",
        tough=3,
        slink=2,
        mouth=1,
        brains=1,
        grunt=2,
        main_hand=create_heavy_greataxe(),
        armor=create_light_armor(),
        quirks=[MeatShield()],
    )

    mob1 = PlayerMob(id="mob_skag", name="Skag's Boyz", zone_id="den_entrance", size=2, boss_id="skag")
    mob2 = PlayerMob(id="mob_grub", name="Grub's Crew", zone_id="den_entrance", size=3, boss_id="grub")

    bear = EliteEnemy(
        id="forest_mauler",
        name="Forest Mauler",
        zone_id="main_den",
        size=2,
        wounds=3,
        max_wounds=3,
        defence_tn=2,
        movement=2,
        morale_tn=3,
        ancestry=Ancestry.BEAST,
        traits=[ThickBlubber(), BeastAncestryTrait()],
        attacks=[
            ThreatAttack(
                name="Crushing Claws",
                threat_stat="Tough",
                difficulty=Difficulty.NORMAL,
                threat_tn=2,
                damage=3,
                cleave=True,
            )
        ],
    )

    return topo, [boss1, boss2, mob1, mob2], [bear]


def build_tomb_highwayman() -> ScenarioTuple:
    """Scenario 3: Tomb of the Highwayman.

    Boss Wizgog (Spiked Mace + Push Luck) + Mob (Size 3, Armor 1)
    vs Armored Highwayman (Elite, Parrying Buckler) + 2 Skeletons (Dry Bones) in 2 crypt zones.
    """
    topo = TopologyGraph()
    z_ante = Zone(
        id="crypt_antechamber",
        name="Crypt Antechamber",
        profile=ZoneProfile(Difficulty.NORMAL, 1),
        traits=[ZoneTrait(ZoneTraitType.SLIPPERY)],
    )
    z_vault = Zone(
        id="burial_vault",
        name="Burial Vault",
        profile=ZoneProfile(Difficulty.NORMAL, 2),
        traits=[ZoneTrait(ZoneTraitType.SHORING)],
    )
    topo.add_zone(z_ante)
    topo.add_zone(z_vault)
    topo.connect("crypt_antechamber", "burial_vault")

    boss = GoblinBoss(
        id="wizgog",
        name="Boss Wizgog",
        zone_id="crypt_antechamber",
        tough=2,
        slink=3,
        mouth=2,
        brains=2,
        grunt=2,
        main_hand=create_spiked_mace(),
        armor=create_light_armor(),
        quirks=[PushLuck()],
    )

    mob = PlayerMob(
        id="tomb_diggers",
        name="Tomb Diggers",
        zone_id="crypt_antechamber",
        size=3,
        armor_rating=1,
        boss_id="wizgog",
    )

    highwayman = EliteEnemy(
        id="highwayman",
        name="Armored Highwayman",
        zone_id="burial_vault",
        size=1,
        wounds=2,
        max_wounds=2,
        defence_tn=2,
        movement=1,
        morale_tn=2,
        traits=[ParryingBuckler(), HumanoidAncestryTrait()],
        attacks=[
            ThreatAttack(name="Broadsword", threat_stat="Tough", threat_tn=2, damage=2)
        ],
    )

    skel_a = StandardEnemy(
        id="skel_a",
        name="Skeleton Sentry A",
        zone_id="burial_vault",
        defence_tn=2,
        movement=1,
        morale_tn=1,
        ancestry=Ancestry.UNDEAD,
        traits=[DryBones(), UndeadAncestryTrait()],
        attacks=[ThreatAttack(name="Notched Scimitar", threat_stat="Tough", threat_tn=1, damage=1)],
    )

    skel_b = StandardEnemy(
        id="skel_b",
        name="Skeleton Sentry B",
        zone_id="crypt_antechamber",
        defence_tn=2,
        movement=1,
        morale_tn=1,
        ancestry=Ancestry.UNDEAD,
        traits=[DryBones(), UndeadAncestryTrait()],
        attacks=[ThreatAttack(name="Notched Scimitar", threat_stat="Tough", threat_tn=1, damage=1)],
    )

    return topo, [boss, mob], [highwayman, skel_a, skel_b]


PRESET_SCENARIOS: Dict[str, Tuple[str, ScenarioFactory]] = {
    "street_skirmish": ("Street Skirmish", build_street_skirmish),
    "maulers_den": ("The Mauler's Den", build_maulers_den),
    "tomb_highwayman": ("Tomb of the Highwayman", build_tomb_highwayman),
}


# =============================================================================
# Monte Carlo Batch Simulator
# =============================================================================

class MonteCarloSimulator:
    """High-throughput Monte Carlo batch simulation engine for tactical combat scenarios."""

    def __init__(
        self,
        scenario_factory: Optional[Union[ScenarioFactory, str]] = None,
        scenario_name: Optional[str] = None,
        max_rounds: int = 50,
    ):
        """Initialize the simulator with a scenario factory or named preset.

        Args:
            scenario_factory: Callable returning (topology, allies, enemies) or preset name.
            scenario_name: Human-readable name for reporting (auto-resolved if preset).
            max_rounds: Maximum combat rounds allowed per encounter before declaring draw.
        """
        self.max_rounds = max_rounds

        if isinstance(scenario_factory, str):
            key = scenario_factory.lower().replace("-", "_").replace(" ", "_")
            if key in PRESET_SCENARIOS:
                default_name, factory = PRESET_SCENARIOS[key]
                self.scenario_factory = factory
                self.scenario_name = scenario_name or default_name
            else:
                available = ", ".join(PRESET_SCENARIOS.keys())
                raise ValueError(f"Unknown preset scenario '{scenario_factory}'. Available: {available}")
        elif scenario_factory is not None:
            self.scenario_factory = scenario_factory
            self.scenario_name = scenario_name or getattr(scenario_factory, "__name__", "Custom Scenario")
        else:
            # Default to street skirmish
            self.scenario_factory = build_street_skirmish
            self.scenario_name = scenario_name or "Street Skirmish"

    @classmethod
    def from_preset(cls, preset_name: str, max_rounds: int = 50) -> MonteCarloSimulator:
        """Create a simulator instance from a preset scenario name."""
        return cls(scenario_factory=preset_name, max_rounds=max_rounds)

    def run_single(
        self,
        seed: Optional[int] = None,
        run_id: int = 0,
    ) -> SimulationRunResult:
        """Execute a single complete tactical combat encounter."""
        rng = random.Random(seed) if seed is not None else random.Random()

        # Build fresh scenario instances
        sig = inspect.signature(self.scenario_factory)
        if len(sig.parameters) > 0:
            topo, allies, enemies = self.scenario_factory(rng=rng)
        else:
            topo, allies, enemies = self.scenario_factory()

        # Calculate initial mob size
        initial_mob_size = sum(a.size for a in allies if isinstance(a, PlayerMob))

        # Instantiate engine
        engine = CombatEngine(
            topology=topo,
            allies=allies,
            enemies=enemies,
            scenario_name=self.scenario_name,
            rng=rng,
        )

        summary = engine.run_to_completion(max_rounds=self.max_rounds)
        return SimulationRunResult.from_combat_summary(
            summary=summary,
            run_id=run_id,
            initial_mob_size=initial_mob_size,
            seed=seed,
        )

    def run(
        self,
        iterations: int = 1000,
        base_seed: Optional[int] = 42,
        progress_callback: Optional[Callable[[int, int], None]] = None,
        progress_interval: int = 100,
    ) -> SimulationMetrics:
        """Execute a high-throughput batch simulation over N iterations.

        Args:
            iterations: Number of combat encounters to simulate (e.g. 100 to 10,000+).
            base_seed: Base integer seed for deterministic, reproducible simulation runs.
            progress_callback: Optional callback receiving (current_run, total_runs).
            progress_interval: Step frequency for invoking progress_callback.

        Returns:
            SimulationMetrics containing all statistical aggregations and distributions.
        """
        if iterations <= 0:
            return StatisticalAggregator.aggregate(self.scenario_name, [], 0.0)

        results: List[SimulationRunResult] = []
        start_time = time.perf_counter()

        for i in range(iterations):
            run_seed = (base_seed + i) if base_seed is not None else None
            res = self.run_single(seed=run_seed, run_id=i)
            results.append(res)

            if progress_callback and (i + 1 == iterations or (i + 1) % progress_interval == 0):
                progress_callback(i + 1, iterations)

        elapsed = time.perf_counter() - start_time
        return StatisticalAggregator.aggregate(
            scenario_name=self.scenario_name,
            results=results,
            elapsed_seconds=elapsed,
        )

    @staticmethod
    def run_ab_comparison(
        factory_a: Union[ScenarioFactory, str],
        factory_b: Union[ScenarioFactory, str],
        iterations: int = 1000,
        name_a: str = "Configuration A",
        name_b: str = "Configuration B",
        base_seed: Optional[int] = 42,
        max_rounds: int = 50,
    ) -> ABComparisonResult:
        """Run an A/B balance comparison across two loadouts, quirks, or enemy variants."""
        sim_a = MonteCarloSimulator(scenario_factory=factory_a, scenario_name=name_a, max_rounds=max_rounds)
        sim_b = MonteCarloSimulator(scenario_factory=factory_b, scenario_name=name_b, max_rounds=max_rounds)

        metrics_a = sim_a.run(iterations=iterations, base_seed=base_seed)
        metrics_b = sim_b.run(iterations=iterations, base_seed=base_seed)

        return StatisticalAggregator.compare_ab(
            metrics_a=metrics_a,
            metrics_b=metrics_b,
            name_a=name_a,
            name_b=name_b,
        )


# =============================================================================
# CLI Entrypoint for Direct Execution
# =============================================================================

def main():
    """Command-line interface for running Monte Carlo simulations directly."""
    parser = argparse.ArgumentParser(description="Gobbos Tactical Combat Monte Carlo Batch Simulator")
    parser.add_argument(
        "--scenario",
        type=str,
        default="street_skirmish",
        choices=["street_skirmish", "maulers_den", "tomb_highwayman"],
        help="Preset scenario to simulate",
    )
    parser.add_argument(
        "-n", "--runs",
        type=int,
        default=1000,
        help="Number of iterations to execute (default: 1000)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Base random seed for reproducibility",
    )
    parser.add_argument(
        "--ab",
        action="store_true",
        help="Run an A/B comparison (e.g. Shield vs 2H Heavy weapon)",
    )

    args = parser.parse_args()

    if not args.ab:
        sim = MonteCarloSimulator.from_preset(args.scenario)
        print(f"Starting Monte Carlo simulation ({args.runs:,} iterations) for '{sim.scenario_name}'...")
        metrics = sim.run(iterations=args.runs, base_seed=args.seed)
        print(metrics.format_ascii_table())
    else:
        # Example A/B comparison: Street Skirmish with Shield vs Heavy Greataxe
        def factory_shield():
            return build_street_skirmish()

        def factory_greataxe():
            topo, allies, enemies = build_street_skirmish()
            boss = allies[0]
            boss.main_hand = create_heavy_greataxe()
            boss.off_hand = None
            boss.armor = create_light_armor()
            return topo, allies, enemies

        print(f"Running A/B Balance Comparison ({args.runs:,} runs each)...")
        comp = MonteCarloSimulator.run_ab_comparison(
            factory_a=factory_shield,
            factory_b=factory_greataxe,
            iterations=args.runs,
            name_a="Shield + Sword",
            name_b="2H Heavy Greataxe",
            base_seed=args.seed,
        )
        print(comp.format_ascii_table())


if __name__ == "__main__":
    main()
