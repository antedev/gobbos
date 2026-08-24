"""Core combat loop engine orchestrating the 5-phase tactical round cycle."""

from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Any, Callable, Dict, List, Optional, Union

from combat_sim.core.dice import BangarangaPool
from combat_sim.core.types import Condition
from combat_sim.domain.entities import (
    BaseEntity,
    EliteEnemy,
    Enemy,
    EnemyMob,
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
)
from combat_sim.domain.topology import TopologyGraph
from combat_sim.domain.traits import VoraciousRegrowth
from combat_sim.engine.ai import BossAI, EnemyAI, MobAI
from combat_sim.engine.resolver import HazardResolver, MoraleResolver


@dataclass
class RoundSummary:
    """Detailed summary of a single combat round."""
    round_number: int
    allies_alive: int
    enemies_alive: int
    actions_taken: List[Dict[str, Any]] = field(default_factory=list)
    casualties: List[str] = field(default_factory=list)
    morale_events: List[Dict[str, Any]] = field(default_factory=list)
    hazard_events: List[str] = field(default_factory=list)
    is_combat_over: bool = False
    victor: Optional[str] = None


@dataclass
class CombatSummary:
    """Complete summary report of an entire combat encounter."""
    scenario_name: str
    total_rounds: int
    victor: str  # "allies", "enemies", "draw"
    allies_survived: bool
    boss_grit_remaining: Dict[str, int] = field(default_factory=dict)
    mob_sizes_remaining: Dict[str, int] = field(default_factory=dict)
    enemies_killed: int = 0
    total_casualties: int = 0
    round_summaries: List[RoundSummary] = field(default_factory=list)


@dataclass
class CombatState:
    """State snapshot of an active tactical combat encounter."""
    scenario_name: str
    topology: TopologyGraph
    allies: List[Union[GoblinBoss, PlayerMob]]
    enemies: List[Enemy]
    current_round: int = 0
    bangaranga_pool: BangarangaPool = field(default_factory=lambda: BangarangaPool(initial_dice=5))
    is_combat_over: bool = False
    victor: Optional[str] = None
    round_history: List[RoundSummary] = field(default_factory=list)

    @property
    def living_allies(self) -> List[Union[GoblinBoss, PlayerMob]]:
        return [a for a in self.allies if a.is_alive]

    @property
    def living_enemies(self) -> List[Enemy]:
        return [e for e in self.enemies if e.is_alive and not e.has_fled]


class CombatEngine:
    """Orchestrates full 5-phase tactical combat encounters."""

    def __init__(
        self,
        topology: TopologyGraph,
        allies: List[Union[GoblinBoss, PlayerMob]],
        enemies: List[Enemy],
        scenario_name: str = "Tactical Encounter",
        rng: Optional[random.Random] = None,
    ):
        self.topology = topology
        self.allies = allies
        self.enemies = enemies
        self.scenario_name = scenario_name
        self.rng = rng or random.Random()
        self.state = CombatState(
            scenario_name=scenario_name,
            topology=topology,
            allies=allies,
            enemies=enemies,
        )

    def run_round(self) -> RoundSummary:
        """Execute one complete 5-phase combat round."""
        if self.state.is_combat_over:
            return RoundSummary(
                round_number=self.state.current_round,
                allies_alive=len(self.state.living_allies),
                enemies_alive=len(self.state.living_enemies),
                is_combat_over=True,
                victor=self.state.victor,
            )

        self.state.current_round += 1
        current_round = self.state.current_round
        round_actions: List[Dict[str, Any]] = []
        casualties: List[str] = []

        # =====================================================================
        # Phase 1: Round Start & Trait Resets
        # =====================================================================
        for ally in self.state.allies:
            if ally.is_alive:
                ally.reset_turn_actions()

        for enemy in self.state.enemies:
            if enemy.is_alive:
                enemy.reset_turn_actions()
                for trait in enemy.traits:
                    trait.on_round_start(enemy, self.state)

        # =====================================================================
        # Phase 2: Player Active Turn (Boss & Mob Actions)
        # =====================================================================
        for boss in self.state.allies:
            if isinstance(boss, GoblinBoss) and boss.is_alive:
                boss_acts = BossAI.execute_turn(
                    boss=boss,
                    allies=self.state.allies,
                    enemies=self.state.enemies,
                    topology=self.topology,
                    rng=self.rng,
                )
                round_actions.extend(boss_acts)

        # Resolve any un-ordered controlled Mobs (Loitering) or uncontrolled Mobs
        for mob in self.state.allies:
            if isinstance(mob, PlayerMob) and mob.is_alive and not mob.is_ordered:
                mob_res = MobAI.execute_unordered_mob(mob, self.topology, rng=self.rng)
                round_actions.append({"actor": mob.name, "unordered_action": mob_res})

        # Check combat end condition after player active turn
        if not self.state.living_enemies:
            for ally in self.state.allies:
                ally.clear_stagger()
            for enemy in self.state.enemies:
                enemy.clear_stagger()
            self.state.is_combat_over = True
            self.state.victor = "allies"
            summary = RoundSummary(
                round_number=current_round,
                allies_alive=len(self.state.living_allies),
                enemies_alive=0,
                actions_taken=round_actions,
                is_combat_over=True,
                victor="allies",
            )
            self.state.round_history.append(summary)
            return summary

        # =====================================================================
        # Phase 3: Enemy Active Turn (Deterministic Threats)
        # =====================================================================
        enemy_acts = EnemyAI.execute_enemy_turns(
            enemies=self.state.enemies,
            allies=self.state.allies,
            topology=self.topology,
            rng=self.rng,
        )
        round_actions.extend(enemy_acts)

        # Check combat end condition after enemy active turn
        if not self.state.living_allies:
            for ally in self.state.allies:
                ally.clear_stagger()
            for enemy in self.state.enemies:
                enemy.clear_stagger()
            self.state.is_combat_over = True
            self.state.victor = "enemies"
            summary = RoundSummary(
                round_number=current_round,
                allies_alive=0,
                enemies_alive=len(self.state.living_enemies),
                actions_taken=round_actions,
                is_combat_over=True,
                victor="enemies",
            )
            self.state.round_history.append(summary)
            return summary

        # =====================================================================
        # Phase 4: Round Closure (Stagger Clear, Morale, Hazards)
        # =====================================================================
        # 1. Automatically clear Staggered conditions on all units
        for ally in self.state.allies:
            ally.clear_stagger()
        for enemy in self.state.enemies:
            enemy.clear_stagger()
            for trait in enemy.traits:
                trait.on_round_end(enemy, self.state)
            # Cycle Voracious Regrowth fire tracking
            if isinstance(enemy, EliteEnemy):
                enemy.last_round_fire_or_acid_damage = enemy.current_round_fire_or_acid_damage
                enemy.current_round_fire_or_acid_damage = False

        # 2. Check 50% casualty Swarm Terror Morale checks
        morale_events: List[Dict[str, Any]] = []
        dead_enemies = [e for e in self.state.enemies if not e.is_alive or e.has_fled]
        if len(dead_enemies) > 0 and len(dead_enemies) * 2 >= len(self.state.enemies):
            morale_res = MoraleResolver.check_swarm_terror(
                enemies=self.state.enemies,
                allies=self.state.allies,
                trigger_reason="50_percent_loss",
                rng=self.rng,
            )
            if morale_res.get("enemies_broken"):
                morale_events.append(morale_res)

        # 3. Fire spread across connected flammable zones
        ignited_zones = HazardResolver.spread_fire(self.topology, rng=self.rng)

        # =====================================================================
        # Phase 5: Combat End Evaluation
        # =====================================================================
        victor = None
        if not self.state.living_enemies:
            self.state.is_combat_over = True
            self.state.victor = "allies"
            victor = "allies"
        elif not self.state.living_allies:
            self.state.is_combat_over = True
            self.state.victor = "enemies"
            victor = "enemies"

        summary = RoundSummary(
            round_number=current_round,
            allies_alive=len(self.state.living_allies),
            enemies_alive=len(self.state.living_enemies),
            actions_taken=round_actions,
            casualties=casualties,
            morale_events=morale_events,
            hazard_events=ignited_zones,
            is_combat_over=self.state.is_combat_over,
            victor=victor,
        )
        self.state.round_history.append(summary)
        return summary

    def run_to_completion(self, max_rounds: int = 50) -> CombatSummary:
        """Run combat rounds sequentially until victory, defeat, or max_rounds limit."""
        while not self.state.is_combat_over and self.state.current_round < max_rounds:
            self.run_round()

        if not self.state.is_combat_over:
            # Max rounds reached -> Draw
            self.state.is_combat_over = True
            self.state.victor = "draw"

        # Tally metrics
        boss_grit = {}
        for a in self.state.allies:
            if isinstance(a, GoblinBoss):
                boss_grit[a.name] = a.grit

        mob_sizes = {}
        for a in self.state.allies:
            if isinstance(a, PlayerMob):
                mob_sizes[a.name] = a.size

        enemies_killed = sum(1 for e in self.state.enemies if not e.is_alive)

        return CombatSummary(
            scenario_name=self.scenario_name,
            total_rounds=self.state.current_round,
            victor=self.state.victor or "draw",
            allies_survived=len(self.state.living_allies) > 0,
            boss_grit_remaining=boss_grit,
            mob_sizes_remaining=mob_sizes,
            enemies_killed=enemies_killed,
            total_casualties=len(self.state.allies) - len(self.state.living_allies),
            round_summaries=self.state.round_history,
        )
