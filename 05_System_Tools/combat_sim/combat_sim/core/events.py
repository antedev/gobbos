"""Event system for tactical combat simulation.

Provides structured combat events, an event listener dispatcher registry,
and a rich human-readable turn-by-turn event log formatter with ANSI colorization.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import os
import sys
import time
from typing import Any, Callable, Dict, List, Optional, Set, Union


class EventType(str, Enum):
    """Granular event categories emitted across the 5-phase combat lifecycle."""
    ROUND_START = "ROUND_START"
    ACTION_DECLARED = "ACTION_DECLARED"
    ROLL_RESOLVED = "ROLL_RESOLVED"
    CLATTER_RESOLVED = "CLATTER_RESOLVED"
    DAMAGE_APPLIED = "DAMAGE_APPLIED"
    MOB_SCATTER = "MOB_SCATTER"
    MOB_TRAMPLE = "MOB_TRAMPLE"
    QUIRK_TRIGGERED = "QUIRK_TRIGGERED"
    HAZARD_TICKED = "HAZARD_TICKED"
    MORALE_TRIGGERED = "MORALE_TRIGGERED"
    STAGGER_CLEARED = "STAGGER_CLEARED"
    COMBAT_END = "COMBAT_END"

    def __str__(self) -> str:
        return self.value


@dataclass
class CombatEvent:
    """Immutable record of an individual event or resolution during combat."""
    event_type: EventType
    description: str
    round: int = 0
    phase: str = ""
    entity_id: Optional[str] = None
    entity_name: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        """Convert event to a standard dictionary representation."""
        return {
            "event_type": self.event_type.value if isinstance(self.event_type, EventType) else str(self.event_type),
            "description": self.description,
            "round": self.round,
            "phase": self.phase,
            "entity_id": self.entity_id,
            "entity_name": self.entity_name,
            "details": dict(self.details),
            "timestamp": self.timestamp,
        }


EventCallback = Callable[[CombatEvent], None]


class EventDispatcher:
    """Listener registry and dispatcher for combat events."""

    def __init__(self, record_history: bool = True):
        self._listeners: Dict[str, List[EventCallback]] = {}
        self._global_listeners: List[EventCallback] = []
        self._history: List[CombatEvent] = []
        self.record_history: bool = record_history

    def register(
        self,
        event_type: Optional[Union[EventType, str]],
        callback: EventCallback,
    ) -> None:
        """Register a callback for a specific event type, or globally if event_type is None or '*'."""
        if event_type is None or event_type == "*":
            if callback not in self._global_listeners:
                self._global_listeners.append(callback)
            return

        key = event_type.value if isinstance(event_type, EventType) else str(event_type).upper()
        if key not in self._listeners:
            self._listeners[key] = []
        if callback not in self._listeners[key]:
            self._listeners[key].append(callback)

    def unregister(
        self,
        event_type: Optional[Union[EventType, str]],
        callback: EventCallback,
    ) -> bool:
        """Unregister a previously registered callback."""
        if event_type is None or event_type == "*":
            if callback in self._global_listeners:
                self._global_listeners.remove(callback)
                return True
            return False

        key = event_type.value if isinstance(event_type, EventType) else str(event_type).upper()
        if key in self._listeners and callback in self._listeners[key]:
            self._listeners[key].remove(callback)
            return True
        return False

    def dispatch(self, event: CombatEvent) -> None:
        """Dispatch an event to all matching registered listeners and global listeners."""
        if self.record_history:
            self._history.append(event)

        key = event.event_type.value if isinstance(event.event_type, EventType) else str(event.event_type).upper()
        listeners = list(self._listeners.get(key, []))
        for cb in listeners:
            cb(event)

        global_listeners = list(self._global_listeners)
        for cb in global_listeners:
            cb(event)

    def emit(
        self,
        event_type: EventType,
        description: str,
        round: int = 0,
        phase: str = "",
        entity_id: Optional[str] = None,
        entity_name: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> CombatEvent:
        """Convenience method to construct, dispatch, and return a CombatEvent."""
        event = CombatEvent(
            event_type=event_type,
            description=description,
            round=round,
            phase=phase,
            entity_id=entity_id,
            entity_name=entity_name,
            details=details or {},
        )
        self.dispatch(event)
        return event

    def clear(self) -> None:
        """Clear all listeners and recorded history."""
        self._listeners.clear()
        self._global_listeners.clear()
        self._history.clear()

    def clear_history(self) -> None:
        """Clear only the recorded event history."""
        self._history.clear()

    def get_history(self, event_type: Optional[Union[EventType, str]] = None) -> List[CombatEvent]:
        """Retrieve recorded history, optionally filtered by event type."""
        if event_type is None:
            return list(self._history)
        key = event_type.value if isinstance(event_type, EventType) else str(event_type).upper()
        return [
            e for e in self._history
            if (e.event_type.value if isinstance(e.event_type, EventType) else str(e.event_type).upper()) == key
        ]

    # Convenience helper registration methods
    def on_action(self, callback: EventCallback) -> None:
        self.register(EventType.ACTION_DECLARED, callback)

    def on_roll(self, callback: EventCallback) -> None:
        self.register(EventType.ROLL_RESOLVED, callback)

    def on_damage(self, callback: EventCallback) -> None:
        self.register(EventType.DAMAGE_APPLIED, callback)

    def on_clatter(self, callback: EventCallback) -> None:
        self.register(EventType.CLATTER_RESOLVED, callback)

    def on_quirk(self, callback: EventCallback) -> None:
        self.register(EventType.QUIRK_TRIGGERED, callback)

    def on_hazard(self, callback: EventCallback) -> None:
        self.register(EventType.HAZARD_TICKED, callback)

    def on_morale(self, callback: EventCallback) -> None:
        self.register(EventType.MORALE_TRIGGERED, callback)

    def on_condition(self, callback: EventCallback) -> None:
        self.register(EventType.STAGGER_CLEARED, callback)

    def on_round_end(self, callback: EventCallback) -> None:
        self.register(EventType.STAGGER_CLEARED, callback)

    def on_combat_end(self, callback: EventCallback) -> None:
        self.register(EventType.COMBAT_END, callback)


class AnsiColor:
    """ANSI color escape sequences for clean terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"

    # Standard colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


class CombatEventFormatter:
    """Generates clean, colorized, human-readable turn-by-turn combat logs."""

    def __init__(self, colorize: bool = True):
        self.colorize = colorize and self._supports_color()

    @staticmethod
    def _supports_color() -> bool:
        """Check if terminal environment supports ANSI escape codes."""
        if "NO_COLOR" in os.environ:
            return False
        if not hasattr(sys.stdout, "isatty"):
            return False
        # Windows 10+ supports ANSI or if running in modern terminal
        return sys.stdout.isatty() or os.environ.get("TERM") is not None or "WT_SESSION" in os.environ

    def _style(self, text: str, *styles: str, force_color: Optional[bool] = None) -> str:
        """Apply ANSI styles if colorization is active."""
        active = self.colorize if force_color is None else force_color
        if not active or not styles:
            return text
        prefix = "".join(styles)
        return f"{prefix}{text}{AnsiColor.RESET}"

    def format_event(self, event: CombatEvent, colorize: Optional[bool] = None) -> str:
        """Format an individual combat event into a human-readable string."""
        active_color = self.colorize if colorize is None else colorize
        etype = event.event_type

        if etype == EventType.ROUND_START:
            round_str = f"=== [ROUND {event.round}] Phase: {event.phase or 'Round Start'} ==="
            return self._style(round_str, AnsiColor.BOLD, AnsiColor.BRIGHT_CYAN, force_color=active_color)

        elif etype == EventType.ACTION_DECLARED:
            actor = event.entity_name or event.entity_id or "Entity"
            desc = event.description
            actor_styled = self._style(f"[{actor}]", AnsiColor.BOLD, AnsiColor.YELLOW, force_color=active_color)
            return f"  -> {actor_styled} {desc}"

        elif etype == EventType.ROLL_RESOLVED:
            d = event.details
            pool_size = d.get("pool_size", "?")
            diff = d.get("difficulty", "5+")
            faces = d.get("faces", [])
            bonus_faces = d.get("bonus_faces", [])
            successes = d.get("successes", 0)
            is_crit = d.get("is_critical", False)
            fumble = d.get("fumble", False)
            gambled = d.get("gambled", False)

            faces_str = f"faces: {faces}"
            if bonus_faces:
                faces_str += f" + explosions: {bonus_faces}"

            succ_styled = self._style(
                f"{successes} Success{'es' if successes != 1 else ''}",
                AnsiColor.BOLD, AnsiColor.BRIGHT_GREEN if successes > 0 else AnsiColor.RED,
                force_color=active_color,
            )

            tags = []
            if is_crit:
                tags.append(self._style("[CRITICAL!]", AnsiColor.BOLD, AnsiColor.BRIGHT_MAGENTA, force_color=active_color))
            if fumble:
                tags.append(self._style("[FUMBLE!]", AnsiColor.BOLD, AnsiColor.BRIGHT_RED, force_color=active_color))
            if gambled:
                tags.append(self._style("[GAMBLED]", AnsiColor.CYAN, force_color=active_color))

            tag_str = f" ({', '.join(tags)})" if tags else ""
            return f"    * Dice Pool ({pool_size}d6 vs {diff}): [{faces_str}] -> {succ_styled}{tag_str}"

        elif etype == EventType.CLATTER_RESOLVED:
            d = event.details
            target = event.entity_name or event.entity_id or "Target"
            evaded = d.get("evaded", False)
            stat_succ = d.get("stat_successes", 0)
            armor_succ = d.get("armor_successes", 0)
            dmg_taken = d.get("damage_taken", 0)

            target_styled = self._style(f"[{target}]", AnsiColor.BOLD, AnsiColor.YELLOW, force_color=active_color)
            if evaded:
                result_styled = self._style("CLEAN EVASION (0 Damage Taken)", AnsiColor.BOLD, AnsiColor.BRIGHT_GREEN, force_color=active_color)
            else:
                result_styled = self._style(f"HIT -> Took {dmg_taken} Damage", AnsiColor.BOLD, AnsiColor.BRIGHT_RED, force_color=active_color)

            clatter_desc = f"[Clatter Defense] for {target_styled}: {stat_succ} Stat Succ, {armor_succ} Armor Mit => {result_styled}"
            return f"    {clatter_desc}"

        elif etype == EventType.DAMAGE_APPLIED:
            d = event.details
            target = event.entity_name or event.entity_id or "Target"
            amount = d.get("amount", d.get("damage", 0))
            hp_type = d.get("hp_type", "Damage")
            remaining = d.get("remaining", "")
            killed = d.get("killed", False)

            target_styled = self._style(f"[{target}]", AnsiColor.BOLD, force_color=active_color)
            if "wound" in hp_type.lower():
                dmg_label = f"{amount} Wound{'s' if amount != 1 else ''}"
            elif "grit" in hp_type.lower():
                dmg_label = f"{amount} Grit"
            else:
                dmg_label = f"{amount} Damage"
            dmg_styled = self._style(dmg_label, AnsiColor.BRIGHT_RED, force_color=active_color)

            rem_str = f" (Remaining: {remaining})" if remaining else ""
            line = f"    [Damage] {target_styled} takes {dmg_styled}{rem_str}"
            if killed:
                line += " " + self._style("[ELIMINATED / DEAD]", AnsiColor.BOLD, AnsiColor.RED, force_color=active_color)
            return line

        elif etype == EventType.MOB_SCATTER:
            actor = event.entity_name or event.entity_id or "Mob"
            actor_styled = self._style(f"[{actor}]", AnsiColor.BOLD, AnsiColor.CYAN, force_color=active_color)
            return f"    [Scatter] {actor_styled} SCATTER! {event.description}"

        elif etype == EventType.MOB_TRAMPLE:
            actor = event.entity_name or event.entity_id or "Mob"
            actor_styled = self._style(f"[{actor}]", AnsiColor.BOLD, AnsiColor.BRIGHT_RED, force_color=active_color)
            return f"    [Trample] {actor_styled} TRAMPLE DISASTER! {event.description}"

        elif etype == EventType.QUIRK_TRIGGERED:
            actor = event.entity_name or event.entity_id or "Entity"
            actor_styled = self._style(f"[{actor}]", AnsiColor.BOLD, AnsiColor.MAGENTA, force_color=active_color)
            quirk_name = event.details.get("quirk", "Quirk")
            quirk_styled = self._style(f"[{quirk_name}]", AnsiColor.BOLD, AnsiColor.BRIGHT_MAGENTA, force_color=active_color)
            return f"    [Quirk] Triggered: {quirk_styled} by {actor_styled} -> {event.description}"

        elif etype == EventType.HAZARD_TICKED:
            return f"    [Hazard] {self._style(event.description, AnsiColor.BRIGHT_YELLOW, force_color=active_color)}"

        elif etype == EventType.MORALE_TRIGGERED:
            return f"    [Morale] Trigger: {self._style(event.description, AnsiColor.BRIGHT_MAGENTA, force_color=active_color)}"

        elif etype == EventType.STAGGER_CLEARED:
            actor = event.entity_name or event.entity_id or "Entity"
            return f"    [Stagger] Cleared: [{actor}] recovered from Staggered."

        elif etype == EventType.COMBAT_END:
            victor = event.details.get("victor", "draw").upper()
            color = AnsiColor.BRIGHT_GREEN if victor == "ALLIES" else (AnsiColor.BRIGHT_RED if victor == "ENEMIES" else AnsiColor.YELLOW)
            banner = f"=== COMBAT CONCLUDED: {victor} VICTORY! ({event.description}) ==="
            return self._style(banner, AnsiColor.BOLD, color, force_color=active_color)

        return f"  - {event.description}"

    def format_round_header(self, round_number: int, phase: Optional[str] = None, colorize: Optional[bool] = None) -> str:
        """Generate a prominent round banner."""
        active = self.colorize if colorize is None else colorize
        phase_str = f" -- {phase}" if phase else ""
        border = "=" * 70
        title = f"  ROUND {round_number}{phase_str}  "
        padded = title.center(70, "=")
        return (
            f"\n{self._style(border, AnsiColor.CYAN, force_color=active)}\n"
            f"{self._style(padded, AnsiColor.BOLD, AnsiColor.BRIGHT_CYAN, force_color=active)}\n"
            f"{self._style(border, AnsiColor.CYAN, force_color=active)}"
        )

    def format_combat_summary(self, summary: Any, colorize: Optional[bool] = None) -> str:
        """Format a final CombatSummary report."""
        active = self.colorize if colorize is None else colorize
        victor = getattr(summary, "victor", "unknown").upper()

        if victor == "ALLIES":
            vic_color = AnsiColor.BRIGHT_GREEN
            vic_title = "VICTORY FOR THE GOBLINS!"
        elif victor == "ENEMIES":
            vic_color = AnsiColor.BRIGHT_RED
            vic_title = "TOTAL PARTY KNOCKOUT (TPK) / DEFEAT!"
        else:
            vic_color = AnsiColor.BRIGHT_YELLOW
            vic_title = "STALEMATE / DRAW"

        border = "=" * 70
        divider = "-" * 70

        lines = [
            "",
            self._style(border, AnsiColor.BOLD, force_color=active),
            self._style(f"  COMBAT ENCOUNTER SUMMARY: {getattr(summary, 'scenario_name', 'Encounter')}".center(70), AnsiColor.BOLD, force_color=active),
            self._style(f"  {vic_title}".center(70), AnsiColor.BOLD, vic_color, force_color=active),
            self._style(divider, AnsiColor.DIM, force_color=active),
            f"  - Victor: {self._style(victor, AnsiColor.BOLD, vic_color, force_color=active)}",
            f"  - Total Rounds Elapsed: {getattr(summary, 'total_rounds', 0)}",
            f"  - Allies Survived: {getattr(summary, 'allies_survived', False)}",
            f"  - Enemies Defeated: {getattr(summary, 'enemies_killed', 0)}",
            f"  - Total Ally Casualties: {getattr(summary, 'total_casualties', 0)}",
        ]

        boss_grit = getattr(summary, "boss_grit_remaining", {})
        if boss_grit:
            lines.append("  - Boss Remaining Grit:")
            for bname, grit in boss_grit.items():
                g_str = self._style(f"{grit} Grit", AnsiColor.BRIGHT_GREEN if grit > 0 else AnsiColor.RED, force_color=active)
                lines.append(f"    - {bname}: {g_str}")

        mob_sizes = getattr(summary, "mob_sizes_remaining", {})
        if mob_sizes:
            lines.append("  - Mob Remaining Size:")
            for mname, size in mob_sizes.items():
                s_str = self._style(f"Size {size}", AnsiColor.CYAN if size > 0 else AnsiColor.RED, force_color=active)
                lines.append(f"    - {mname}: {s_str}")

        lines.append(self._style(border, AnsiColor.BOLD, force_color=active))
        return "\n".join(lines)
