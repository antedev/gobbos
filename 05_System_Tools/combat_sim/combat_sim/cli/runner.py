"""Interactive CLI Runner and Scenario Execution Orchestrator.

Provides the step-by-step turn-by-turn interactive runner, scenario loaders,
and scripted output formatters for the Gobbos tactical combat simulation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import random
import sys
from typing import Any, Callable, Dict, List, Optional, TextIO, Union

from combat_sim.core.events import (
    AnsiColor,
    CombatEvent,
    CombatEventFormatter,
    EventDispatcher,
    EventType,
)
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
    create_heavy_greataxe,
    create_light_armor,
    create_medium_armor,
    create_notched_sword,
    create_pot_lid_shield,
    create_spiked_mace,
)
from combat_sim.domain.quirks import AnkleBite, MeatShield, PushLuck
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import (
    BeastAncestryTrait,
    DryBones,
    HumanoidAncestryTrait,
    ParryingBuckler,
    ThickBlubber,
    UndeadAncestryTrait,
)
from combat_sim.engine.combat import CombatEngine, CombatState, CombatSummary, RoundSummary


# =============================================================================
# Reference Scenario Builders
# =============================================================================

def build_street_skirmish() -> Dict[str, Any]:
    """Construct Scenario 1: Street Skirmish.

    Armored Boss (Shield + Sword + Ankle Bite) + Size 3 Mob vs
    Robber Gang & Footpads across 3 street zones with Partial Cover.
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

    return {
        "name": "Street Skirmish",
        "description": "Armored Boss (Shield + Sword + Ankle Bite) + Mob vs Robbers & Footpads in 3-zone street",
        "topology": topo,
        "allies": [boss, mob],
        "enemies": [robber_gang, footpad_a, footpad_b],
    }


def build_maulers_den() -> Dict[str, Any]:
    """Construct Scenario 2: The Mauler's Den.

    2 Heavy Weapon Bosses (Heavy Greataxes + Meat Shield) + 2 Mobs vs
    Forest Mauler (Elite Bear with Thick Blubber and Crushing Claws Cleave).
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

    return {
        "name": "The Mauler's Den",
        "description": "2 Bosses (Heavy 2H + Meat Shield) + 2 Mobs vs Forest Mauler in 2-zone cave",
        "topology": topo,
        "allies": [boss1, boss2, mob1, mob2],
        "enemies": [bear],
    }


def build_tomb_highwayman() -> Dict[str, Any]:
    """Construct Scenario 3: Tomb of the Highwayman.

    Boss (Spiked Mace / Medium Armor) + Mob vs Armored Highwayman (Parrying Buckler)
    & 2 Rattlebone Skeletons in crypt with Slippery and Shoring traits.
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
        zone_id="burial_vault",
        defence_tn=2,
        movement=1,
        morale_tn=1,
        ancestry=Ancestry.UNDEAD,
        traits=[DryBones(), UndeadAncestryTrait()],
        attacks=[ThreatAttack(name="Notched Scimitar", threat_stat="Tough", threat_tn=1, damage=1)],
    )

    return {
        "name": "Tomb of the Highwayman",
        "description": "Boss + Mob vs Armored Highwayman (Parrying Buckler) & Skeletons in crypt",
        "topology": topo,
        "allies": [boss, mob],
        "enemies": [highwayman, skel_a, skel_b],
    }


SCENARIO_REGISTRY: Dict[str, Dict[str, Any]] = {
    "street_skirmish": {
        "id": "street_skirmish",
        "name": "Street Skirmish",
        "aliases": ["street_skirmish", "street", "1", "skirmish"],
        "description": "Armored Boss (Shield + Sword + Ankle Bite) + Mob vs Robbers & Footpads in 3-zone street",
        "builder": build_street_skirmish,
    },
    "maulers_den": {
        "id": "maulers_den",
        "name": "The Mauler's Den",
        "aliases": ["maulers_den", "mauler", "2", "den"],
        "description": "2 Bosses (Heavy 2H + Meat Shield) + 2 Mobs vs Forest Mauler in 2-zone cave",
        "builder": build_maulers_den,
    },
    "tomb_highwayman": {
        "id": "tomb_highwayman",
        "name": "Tomb of the Highwayman",
        "aliases": ["tomb_highwayman", "tomb", "3", "highwayman"],
        "description": "Boss + Mob vs Armored Highwayman (Parrying Buckler) & Skeletons in crypt",
        "builder": build_tomb_highwayman,
    },
}


def get_available_scenarios() -> Dict[str, Dict[str, Any]]:
    """Return all registered scenario blueprints."""
    return dict(SCENARIO_REGISTRY)


def load_scenario(name: str) -> Dict[str, Any]:
    """Find and instantiate a fresh scenario instance by name or alias."""
    lookup = name.strip().lower().replace(" ", "_").replace("-", "_").replace("'", "")
    for key, spec in SCENARIO_REGISTRY.items():
        if lookup == key or lookup == spec["name"].lower().replace(" ", "_").replace("'", ""):
            return spec["builder"]()
        if lookup in spec.get("aliases", []):
            return spec["builder"]()

    # If not found, check if a custom module can load it
    try:
        from combat_sim.scenarios.registry import get_scenario  # type: ignore
        custom_scen = get_scenario(name)
        return {
            "name": getattr(custom_scen, "name", name),
            "description": getattr(custom_scen, "description", ""),
            "topology": getattr(custom_scen, "topology", TopologyGraph()),
            "allies": getattr(custom_scen, "allies", []),
            "enemies": getattr(custom_scen, "enemies", []),
        }
    except Exception:
        pass

    available = ", ".join(f"'{k}'" for k in SCENARIO_REGISTRY.keys())
    raise KeyError(f"Unknown scenario '{name}'. Available scenarios: {available}")


def create_engine_for_scenario(scenario_name: str, seed: Optional[int] = None) -> CombatEngine:
    """Instantiate a CombatEngine loaded with the requested scenario and seed."""
    scen_data = load_scenario(scenario_name)
    rng = random.Random(seed) if seed is not None else random.Random()
    return CombatEngine(
        topology=scen_data["topology"],
        allies=scen_data["allies"],
        enemies=scen_data["enemies"],
        scenario_name=scen_data.get("name", scenario_name),
        rng=rng,
    )


# =============================================================================
# Interactive Runner
# =============================================================================

class InteractiveRunner:
    """Step-by-step turn-by-turn interactive and scripted combat simulator."""

    def __init__(
        self,
        scenario_name: str = "street_skirmish",
        interactive: bool = False,
        seed: Optional[int] = None,
        max_rounds: int = 50,
        colorize: bool = True,
        output_stream: Optional[TextIO] = None,
        input_func: Optional[Callable[[str], str]] = None,
        dispatcher: Optional[EventDispatcher] = None,
        formatter: Optional[CombatEventFormatter] = None,
    ):
        self.scenario_name = scenario_name
        self.interactive = interactive
        self.seed = seed
        self.max_rounds = max_rounds
        self.output_stream = output_stream or sys.stdout
        self.input_func = input_func or input
        self.dispatcher = dispatcher or EventDispatcher(record_history=True)
        self.formatter = formatter or CombatEventFormatter(colorize=colorize)
        self._auto_mode = not interactive

    def _write(self, text: str) -> None:
        """Write formatted text to the configured output stream."""
        self.output_stream.write(text + "\n")
        self.output_stream.flush()

    def run(self) -> CombatSummary:
        """Execute the full combat simulation with stepping and logging."""
        engine = create_engine_for_scenario(self.scenario_name, self.seed)

        # Print Initial Encounter Header
        self._print_encounter_header(engine)

        round_num = 0
        while not engine.state.is_combat_over and round_num < self.max_rounds:
            round_num += 1

            # Format Round Start Banner
            round_header = self.formatter.format_round_header(round_num, phase="START")
            self._write(round_header)

            self.dispatcher.emit(
                EventType.ROUND_START,
                f"Starting Round {round_num}",
                round=round_num,
                phase="Round Start",
            )

            # Interactive Step Prompt before round execution
            if self.interactive and not self._auto_mode:
                user_cmd = self._prompt_user(f"\n[Round {round_num}] [Enter: step | r: round | a: auto | q: quit] > ")
                if user_cmd in ("q", "quit", "exit"):
                    self._write("\n[Simulation aborted by user]")
                    engine.state.is_combat_over = True
                    engine.state.victor = "aborted"
                    break
                elif user_cmd in ("a", "auto"):
                    self._auto_mode = True

            # Execute the 5-phase round
            summary: RoundSummary = engine.run_round()

            # Process and format all actions taken in this round
            self._process_round_actions(summary, round_num)

            # Print End of Round Status
            self._print_round_state(engine.state, round_num)

            # Interactive pause after round if still stepping
            if self.interactive and not self._auto_mode and not summary.is_combat_over:
                user_cmd = self._prompt_user(f"[Round {round_num} Complete] [Enter: continue | a: auto | q: quit] > ")
                if user_cmd in ("q", "quit", "exit"):
                    self._write("\n[Simulation aborted by user]")
                    break
                elif user_cmd in ("a", "auto"):
                    self._auto_mode = True

        # Final Combat End Resolution
        if not engine.state.is_combat_over:
            engine.state.is_combat_over = True
            engine.state.victor = "draw"

        combat_summary = engine.run_to_completion(max_rounds=self.max_rounds)

        self.dispatcher.emit(
            EventType.COMBAT_END,
            f"Encounter concluded in {combat_summary.total_rounds} rounds.",
            round=combat_summary.total_rounds,
            phase="Combat End",
            details={
                "victor": combat_summary.victor,
                "allies_survived": combat_summary.allies_survived,
                "enemies_killed": combat_summary.enemies_killed,
            },
        )

        # Print Final Summary Table
        summary_str = self.formatter.format_combat_summary(combat_summary)
        self._write(summary_str)

        return combat_summary

    def _prompt_step(self, prompt: str) -> str:
        """Prompt user for interactive step input."""
        try:
            val = self.input_func(prompt).strip().lower()
            return val
        except (EOFError, KeyboardInterrupt):
            return "auto"

    def _print_encounter_header(self, engine: CombatEngine) -> None:
        """Print initial setup roster and topology."""
        border = "=" * 70
        self._write(self.formatter._style(border, AnsiColor.BOLD, AnsiColor.YELLOW))
        self._write(self.formatter._style(f"  GOBBOS COMBAT SIMULATOR: {engine.scenario_name}".center(70), AnsiColor.BOLD, AnsiColor.BRIGHT_YELLOW))
        self._write(self.formatter._style(border, AnsiColor.BOLD, AnsiColor.YELLOW))

        # Allies roster
        self._write("\n  ALLIES ROSTER:")
        for ally in engine.state.allies:
            if isinstance(ally, GoblinBoss):
                gear_desc = []
                if ally.main_hand:
                    gear_desc.append(ally.main_hand.name)
                if ally.off_hand:
                    gear_desc.append(ally.off_hand.name)
                if ally.armor:
                    gear_desc.append(ally.armor.name)
                gear_str = f" [Gear: {', '.join(gear_desc)}]" if gear_desc else ""
                quirks_str = f" [Quirks: {', '.join(q.name for q in ally.quirks)}]" if ally.quirks else ""
                self._write(f"    - {ally.name} (Goblin Boss) -- Grit: {ally.grit}/{ally.max_grit}, Grunt: {ally.grunt}/{ally.max_grunt}, Zone: {ally.zone_id}{gear_str}{quirks_str}")
            elif isinstance(ally, PlayerMob):
                self._write(f"    - {ally.name} (Player Mob) -- Size: {ally.size}, Health Dice: {ally.health_dice}, Zone: {ally.zone_id}")

        # Enemies roster
        self._write("\n  ENEMIES ROSTER:")
        for enemy in engine.state.enemies:
            if isinstance(enemy, EliteEnemy):
                self._write(f"    - {enemy.name} (Elite) -- Wounds: {enemy.wounds}/{enemy.max_wounds}, Defence: {enemy.defence_tn}, Zone: {enemy.zone_id}")
            elif isinstance(enemy, EnemyMob):
                self._write(f"    - {enemy.name} (Enemy Mob) -- Size: {enemy.size}, Health Dice: {enemy.health_dice}, Zone: {enemy.zone_id}")
            else:
                self._write(f"    - {enemy.name} (Standard) -- Defence: {enemy.defence_tn}, Zone: {enemy.zone_id}")

        # Zones
        self._write("\n  ZONE TOPOLOGY:")
        for zid, zone in engine.topology.zones.items():
            adj = ", ".join(engine.topology.get_adjacent(zid)) or "None"
            traits = ", ".join(t.trait_type.value for t in zone.traits) if zone.traits else "None"
            cover = f" [Cover: {zone.cover.value}]" if zone.cover != CoverType.NONE else ""
            self._write(f"    - Zone [{zid}] '{zone.name}': Profile {zone.profile.shorthand}{cover} (Traits: {traits}) -> Adjacent: [{adj}]")
        self._write("")

    def _process_round_actions(self, summary: RoundSummary, round_num: int) -> None:
        """Emit structured events and format output for all actions in the round."""
        self._write("\n  --- Action Log ---")
        for act in summary.actions_taken:
            actor = act.get("actor", "Entity")
            action_name = act.get("action", "Action")

            # 1. Emit and log Action Declaration
            action_event = self.dispatcher.emit(
                EventType.ACTION_DECLARED,
                f"performs {action_name}" + (f" -> target: [{act.get('target')}]" if act.get("target") else ""),
                round=round_num,
                phase="Player Active" if "Boss" in actor or "Mob" in actor or "Runts" in actor or "Crew" in actor or "Boyz" in actor else "Enemy Active",
                entity_name=actor,
                details=act,
            )
            self._write(self.formatter.format_event(action_event))

            # 2. Process Attack Results if present
            if "hit" in act or "successes" in act:
                succ = act.get("successes", 0)
                hit = act.get("hit", False)
                roll_event = self.dispatcher.emit(
                    EventType.ROLL_RESOLVED,
                    f"Roll result: {succ} successes (Hit: {hit})",
                    round=round_num,
                    entity_name=actor,
                    details={
                        "pool_size": act.get("pool_size", 2),
                        "difficulty": "5+",
                        "faces": act.get("faces", []),
                        "bonus_faces": act.get("bonus_faces", []),
                        "successes": succ,
                        "is_critical": act.get("is_critical", False),
                        "fumble": act.get("fumble", False),
                        "gambled": act.get("gambled", False),
                    },
                )
                self._write(self.formatter.format_event(roll_event))

                if hit:
                    dmg = act.get("wounds_dealt", act.get("damage", 1))
                    target = act.get("target", "Target")
                    killed = act.get("killed", False)
                    dmg_event = self.dispatcher.emit(
                        EventType.DAMAGE_APPLIED,
                        f"Dealt {dmg} damage to {target}",
                        round=round_num,
                        entity_name=target,
                        details={
                            "amount": dmg,
                            "hp_type": "Wounds" if "wounds_dealt" in act else "Damage",
                            "killed": killed,
                            "remaining": act.get("remaining", ""),
                        },
                    )
                    self._write(self.formatter.format_event(dmg_event))

            # 3. Process Clatter Defense if present
            if "clatter" in act or "evaded" in act or "clean_dodge" in act:
                evaded = act.get("evaded", act.get("clean_dodge", False))
                clatter_event = self.dispatcher.emit(
                    EventType.CLATTER_RESOLVED,
                    f"Clatter resolution for {actor}",
                    round=round_num,
                    entity_name=actor,
                    details={
                        "evaded": evaded,
                        "stat_successes": act.get("stat_successes", 1 if evaded else 0),
                        "armor_successes": act.get("armor_successes", 0),
                        "damage_taken": act.get("damage_taken", 0),
                    },
                )
                self._write(self.formatter.format_event(clatter_event))

            # 4. Process Quirk Triggers if present
            if act.get("meat_shield"):
                q_event = self.dispatcher.emit(
                    EventType.QUIRK_TRIGGERED,
                    "Shoved allied Mob to intercept incoming attack!",
                    round=round_num,
                    entity_name=actor,
                    details={"quirk": "Meat Shield"},
                )
                self._write(self.formatter.format_event(q_event))

            if act.get("ankle_bite"):
                q_event = self.dispatcher.emit(
                    EventType.QUIRK_TRIGGERED,
                    "Clean dodge triggered immediate counter-attack with +1 Success!",
                    round=round_num,
                    entity_name=actor,
                    details={"quirk": "Ankle Bite"},
                )
                self._write(self.formatter.format_event(q_event))

            # 5. Process Unordered Mob results
            if "unordered_action" in act:
                uact = act["unordered_action"]
                desc = uact.get("description", "")
                state = uact.get("state", "Loitering")
                if "Scatter" in desc or "flee" in desc.lower():
                    m_event = self.dispatcher.emit(
                        EventType.MOB_SCATTER,
                        f"Unordered Mob {state}: {desc}",
                        round=round_num,
                        entity_name=actor,
                    )
                    self._write(self.formatter.format_event(m_event))
                elif "trample" in desc.lower():
                    m_event = self.dispatcher.emit(
                        EventType.MOB_TRAMPLE,
                        f"Unordered Mob {state}: {desc}",
                        round=round_num,
                        entity_name=actor,
                    )
                    self._write(self.formatter.format_event(m_event))

        # Morale and Hazard events
        for mor in summary.morale_events:
            mor_event = self.dispatcher.emit(
                EventType.MORALE_TRIGGERED,
                f"Morale Check: {mor.get('trigger_reason', 'Loss')} -> Enemies Broken: {mor.get('enemies_broken', [])}",
                round=round_num,
                details=mor,
            )
            self._write(self.formatter.format_event(mor_event))

        for haz in summary.hazard_events:
            haz_event = self.dispatcher.emit(
                EventType.HAZARD_TICKED,
                f"Zone hazard activated / fire spread: {haz}",
                round=round_num,
            )
            self._write(self.formatter.format_event(haz_event))

    def _print_round_state(self, state: CombatState, round_num: int) -> None:
        """Print concise battlefield snapshot at end of round."""
        self._write("\n  --- Round Status ---")
        ally_strs = []
        for a in state.allies:
            if isinstance(a, GoblinBoss):
                status = f"{a.name} ({a.grit}/{a.max_grit} Grit)" if a.is_alive else f"{a.name} (DEAD)"
                ally_strs.append(status)
            elif isinstance(a, PlayerMob):
                status = f"{a.name} (Size {a.size})" if a.is_alive else f"{a.name} (DISPERSED)"
                ally_strs.append(status)

        enemy_strs = []
        for e in state.enemies:
            if isinstance(e, EliteEnemy):
                status = f"{e.name} ({e.wounds}/{e.max_wounds} Wounds)" if e.is_alive else f"{e.name} (DEAD)"
                enemy_strs.append(status)
            elif isinstance(e, EnemyMob):
                status = f"{e.name} (Size {e.size})" if e.is_alive else f"{e.name} (DISPERSED)"
                enemy_strs.append(status)
            else:
                status = f"{e.name}" if e.is_alive else f"{e.name} (DEAD)"
                enemy_strs.append(status)

        self._write(f"  Allies: {', '.join(ally_strs)}")
        self._write(f"  Enemies: {', '.join(enemy_strs)}")
