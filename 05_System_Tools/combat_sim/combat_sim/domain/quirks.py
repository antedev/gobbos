"""Boss Quirks, Talents, and Modular Twist Modifiers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TwistModifier:
    """Modular Twist attached to a Quirk modifying its triggers, costs, or side-effects."""
    name: str
    tier: int = 1
    description: str = ""

    @staticmethod
    def spiteful() -> TwistModifier:
        """T1 Spiteful: Deals 1 Grit damage or +1 Success against nearest enemy on activation."""
        return TwistModifier(
            name="Spiteful",
            tier=1,
            description="Deals 1 Grit damage or grants +1 Success against nearest enemy on activation.",
        )

    @staticmethod
    def loud() -> TwistModifier:
        """T1 Loud: Rallies 1 Fleeing Mob, but imposes Bane 1 (-1d) on stealth Slink tests for the round."""
        return TwistModifier(
            name="Loud",
            tier=1,
            description="Rallies 1 Fleeing Mob in zone, but imposes Bane 1 (-1d) on stealth for the round.",
        )

    @staticmethod
    def efficient() -> TwistModifier:
        """T2 Efficient: Reduces the Grunt activation cost of the attached Quirk by 1 (min 0)."""
        return TwistModifier(
            name="Efficient",
            tier=2,
            description="Reduces Grunt activation cost by 1 (minimum 0).",
        )

    @staticmethod
    def reflexive() -> TwistModifier:
        """T3 Reflexive: Converts a 1 Action cost into a Free Action."""
        return TwistModifier(
            name="Reflexive",
            tier=3,
            description="Converts a 1 Action cost into a Free Action.",
        )


@dataclass
class Quirk(ABC):
    """Abstract base class for all Goblin Boss Quirks and Talents."""
    name: str
    description: str = ""
    tier: int = 1
    grunt_cost: int = 0
    action_cost: int = 0
    is_passive: bool = False
    twists: List[TwistModifier] = field(default_factory=list)

    def get_effective_grunt_cost(self) -> int:
        """Calculate Grunt cost after applying Efficient twists."""
        cost = self.grunt_cost
        for twist in self.twists:
            if twist.name.lower() == "efficient":
                cost = max(0, cost - 1)
        return cost

    def is_free_action(self) -> bool:
        """Check if action cost is 0 or converted via Reflexive twist."""
        if self.action_cost == 0:
            return True
        return any(t.name.lower() == "reflexive" for t in self.twists)

    def add_twist(self, twist: TwistModifier) -> None:
        """Attach a modular twist modifier to this quirk."""
        self.twists.append(twist)

    @abstractmethod
    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        """Evaluate whether this quirk's activation condition is met."""
        pass

    @abstractmethod
    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute the quirk mechanics and return outcome metadata."""
        pass


@dataclass
class MeatShield(Quirk):
    """Spend 1 Grunt / Reaction when taking damage to shove an allied Mob in the zone to take the hit."""
    name: str = "Meat Shield"
    description: str = "Spend 1 Grunt or Reaction when hit to redirect all damage to an allied Mob in your Zone."
    tier: int = 1
    grunt_cost: int = 1
    action_cost: int = 0
    is_passive: bool = False

    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        """Requires an allied mob in the same zone, and either sufficient Grunt or a saved reaction."""
        if not context:
            return False
        allied_mob = context.get("allied_mob")
        if not allied_mob or not getattr(allied_mob, "is_alive", False):
            return False
        # Check zone matching
        if getattr(allied_mob, "zone_id", None) != getattr(boss, "zone_id", None):
            return False
        # Check resource availability
        has_grunt = getattr(boss, "grunt", 0) >= self.get_effective_grunt_cost()
        has_reaction = getattr(boss, "saved_reactions", 0) > 0 or getattr(boss, "actions_left", 0) > 0
        return has_grunt or has_reaction

    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Deduct Grunt/Reaction and redirect incoming attack to the allied Mob."""
        ctx = context or {}
        allied_mob = ctx.get("allied_mob")
        prefer_grunt = ctx.get("use_grunt", True)
        
        effective_cost = self.get_effective_grunt_cost()
        if prefer_grunt and getattr(boss, "grunt", 0) >= effective_cost:
            boss.grunt -= effective_cost
            spent = "grunt"
        elif getattr(boss, "saved_reactions", 0) > 0:
            boss.saved_reactions -= 1
            spent = "saved_reaction"
        elif getattr(boss, "actions_left", 0) > 0:
            boss.actions_left -= 1
            spent = "action"
        elif getattr(boss, "grunt", 0) >= effective_cost:
            boss.grunt -= effective_cost
            spent = "grunt"
        else:
            spent = "none"

        return {
            "redirected_to": getattr(allied_mob, "name", "Allied Mob"),
            "resource_spent": spent,
            "success": True,
        }


@dataclass
class AnkleBite(Quirk):
    """Passive: On a clean Dodge reaction against a melee enemy in the same Zone, trigger immediate counter-attack with +1 Success."""
    name: str = "Ankle Bite"
    description: str = "On clean Dodge vs melee attacker in same zone, make immediate free Melee Counter-Attack at +1 Success."
    tier: int = 1
    grunt_cost: int = 0
    action_cost: int = 0
    is_passive: bool = True

    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        """Triggers if the Boss achieved a clean Dodge against an attacker in the same Zone."""
        if not context:
            return False
        is_clean_dodge = context.get("is_clean_dodge", False)
        is_melee = context.get("is_melee", True)
        attacker = context.get("attacker")
        if not is_clean_dodge or not is_melee or not attacker:
            return False
        return getattr(attacker, "zone_id", None) == getattr(boss, "zone_id", None)

    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Provides a bonus free attack declaration with +1 automatic Success."""
        return {
            "free_counter_attack": True,
            "bonus_successes": 1,
            "target": context.get("attacker") if context else None,
        }


@dataclass
class PushLuck(Quirk):
    """Spend 1 Grunt after rolling a test to reroll all non-1 dice (keeping 1s locked for Gobbo Gamble)."""
    name: str = "Push Luck"
    description: str = "Spend 1 Grunt after rolling to reroll all non-1 dice on any test."
    tier: int = 1
    grunt_cost: int = 1
    action_cost: int = 0
    is_passive: bool = False

    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        """Requires at least 1 Grunt (or 0 if Efficient) and non-empty roll faces."""
        if not context:
            return False
        effective_cost = self.get_effective_grunt_cost()
        if getattr(boss, "grunt", 0) < effective_cost:
            return False
        faces = context.get("faces", [])
        return any(f != 1 for f in faces)

    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Deduct Grunt and return instruction to reroll non-1 dice."""
        effective_cost = self.get_effective_grunt_cost()
        boss.grunt = max(0, getattr(boss, "grunt", 0) - effective_cost)
        faces = context.get("faces", []) if context else []
        reroll_indices = [i for i, f in enumerate(faces) if f != 1]
        return {
            "reroll_indices": reroll_indices,
            "locked_indices": [i for i, f in enumerate(faces) if f == 1],
            "grunt_spent": effective_cost,
        }


@dataclass
class SecondWind(PushLuck):
    """Alias for Push Luck quirk."""
    name: str = "Second Wind"


@dataclass
class OpportunityStrike(Quirk):
    """Passive: Moving out of an enemy zone does not provoke Opportunity Attacks."""
    name: str = "Slippery / Opportunity Strike"
    description: str = "Moving out of an enemy Zone does not trigger enemy Opportunity Attacks."
    tier: int = 1
    grunt_cost: int = 0
    action_cost: int = 0
    is_passive: bool = True

    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        return True

    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {"ignores_opportunity_attacks": True}


@dataclass
class SlipperyQuirk(OpportunityStrike):
    """Alias for Opportunity Strike / Slippery."""
    name: str = "Slippery"


@dataclass
class SwallowLoot(Quirk):
    """Passive: Swallow up to 2 Bulk of items without occupying Carry Capacity."""
    name: str = "Swallow Loot"
    description: str = "Swallow up to 2 Bulk of items to carry them without occupying carry capacity."
    tier: int = 1
    grunt_cost: int = 0
    action_cost: int = 0
    is_passive: bool = True
    internal_bulk_capacity: int = 2

    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        return True

    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {"bonus_unencumbered_bulk": self.internal_bulk_capacity}


@dataclass
class Butcher(Quirk):
    """Passive: Gain Boon 1 (+1d) when attacking a target whose Size is strictly smaller than yours."""
    name: str = "Butcher"
    description: str = "Gain Boon 1 (+1d) when attacking an enemy whose Size is strictly smaller than yours."
    tier: int = 1
    grunt_cost: int = 0
    action_cost: int = 0
    is_passive: bool = True

    def can_trigger(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> bool:
        if not context:
            return False
        target = context.get("target")
        if not target:
            return False
        return getattr(boss, "size", 1) > getattr(target, "size", 1)

    def apply(self, boss: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {"boon_dice": 1}
