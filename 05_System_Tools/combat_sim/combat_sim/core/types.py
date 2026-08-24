"""Core enumeration and data types for the Gobbos tactical combat simulation."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, IntEnum
from typing import Set


class Difficulty(IntEnum):
    """Target face thresholds for Gobbos d6 dice tests."""
    EASY = 4     # Easy: Success on 4, 5, 6
    NORMAL = 5   # Normal: Success on 5, 6
    HARD = 6     # Hard: Success on 6 only

    def meets_threshold(self, face: int) -> bool:
        """Check if a die face meets or exceeds this difficulty threshold."""
        return face >= self.value

    @property
    def label(self) -> str:
        """Return the standard shorthand notation (e.g. 4+, 5+, 6)."""
        if self.value == 6:
            return "6"
        return f"{self.value}+"


class Condition(str, Enum):
    """Tactical status conditions affecting entities in combat."""
    WEAKENED = "Weakened"      # -1d on physical tests (Tough/Slink)
    RESTRAINED = "Restrained"  # Cannot move, -1d on Dodge/Parry
    DUMB = "Dumb"              # -1d on mental/Brains tests
    SILENCED = "Silenced"      # Cannot give verbal Orders
    BLINDED = "Blinded"        # -2d on visual/ranged tests, auto-fail Line of Sight
    TERRIFIED = "Terrified"    # Must move away from terror source, cannot attack
    STUNNED = "Stunned"        # Loses all actions for round, 0 active defence
    PRONE = "Prone"            # Must spend 1 Move action to stand, -1d Dodge/Parry, +1d incoming melee
    STAGGERED = "Staggered"    # -1 Defence TN on enemies, -1d Dodge/Parry on Bosses, -1 Armor Die on Mobs


class Ancestry(str, Enum):
    """Universal enemy ancestry categories."""
    BEAST = "Beast"              # Fire/Loud morale triggers, mindless immunity
    HUMANOID = "Humanoid"        # Tactical discipline, 50% casualty morale
    UNDEAD = "Undead"            # Morale immune, Holy weakness, Dry Bones traits
    MONSTROSITY = "Monstrosity"  # Mass resistance, Sweeping Cleave attacks
    FIEND = "Fiend"              # Fire immunity, Holy weakness, Chaos opportunism


class EnemyScale(str, Enum):
    """Scale classification for enemies."""
    STANDARD = "Standard"  # One-hit kill on hits meeting Defence TN
    ELITE = "Elite"        # Multi-wound track, Overkill wound conversion
    MOB = "Mob"            # Shared Dice-HP pool with casualty scaling


class CoverType(str, Enum):
    """Environmental cover classifications."""
    NONE = "None"        # Open terrain, no cover modifiers
    PARTIAL = "Partial"  # -1d Bane on incoming ranged attacks, +1d Boon on Dodge reactions
    FULL = "Full"        # Blocks direct Line of Sight / ranged targeting


class ActionType(str, Enum):
    """Action declarations in combat."""
    MOVE = "Move"
    MELEE_ATTACK = "Melee Attack"
    RANGED_ATTACK = "Ranged Attack"
    PLUNDER = "Plunder"
    MANIPULATE = "Manipulate"
    ORDER = "Order"
    DODGE = "Dodge"
    PARRY = "Parry"
    SCATTER = "Scatter"


class ZoneTraitType(str, Enum):
    """Environmental traits and hazards assigned to zones."""
    SLIPPERY = "Slippery"      # Slink test or fall Prone
    BURNING = "Burning"        # Slink test or take 2 Fire damage; spreads
    TOXIC = "Toxic"            # Tough test or become Weakened
    NARROW = "Narrow"          # Max Mob Size 2 without penalty, giants cannot enter
    PILLARS = "Pillars"        # Free Action to claim Full Cover from one direction
    RUBBLE = "Rubble"          # Double movement cost (2 moves to cross)
    SHORING = "Shoring"        # Interactive structural collapse opportunity


class WeaponHandedness(IntEnum):
    """Weapon grip requirements."""
    ONE_HAND = 1
    TWO_HAND = 2
    ONE_HANDED = 1
    TWO_HANDED = 2


class WeaponTrait(str, Enum):
    """Special mechanical traits on weapons."""
    BASHING = "Bashing"                # +1d Boon vs Dry Bones skeletons
    CLEAVE = "Cleave"                  # Excess successes hit extra units / full Mob pool
    PIERCING = "Piercing"              # -1d Bane vs Dry Bones, ignores non-piercing immunities
    CUTTING = "Cutting"                # -1d Bane vs Dry Bones
    REACH = "Reach"                    # Attack from behind allies or 1 zone away
    VERSATILE = "Versatile"            # +1d Boon when gripped with 2 hands
    ARMOR_PIERCING = "Armor Piercing"  # Bypasses 1 passive armor mitigation die
    HEAVY = "Heavy"                    # +1 Impact Size for Stagger calculation
    CRUSHING = "Crushing"              # +2 Impact Size for Stagger calculation
    CONCEALABLE = "Concealable"        # Draw as an incidental Free Action
    FAST_THROW = "Fast Throw"          # Usable without stowing off-hand gear
    RAPID_SHOT = "Rapid Shot"          # Fires across 2 zones without range penalty
    CLOCKWORK = "Clockwork"            # 2 distinct ranged attacks with 1 Standard Action


class Tag:
    """Master element and property tag constants."""
    FIRE = "[Fire]"
    EXPLOSIVE = "[Explosive]"
    ACIDIC = "[Acidic]"
    SHOCK = "[Shock]"
    TOXIC = "[Toxic]"
    LOUD = "[Loud]"
    TASTY = "[Tasty]"
    ANGELIC = "[Angelic]"
    LIGHT = "[Light]"
    PURIFIED = "[Purified]"
    BLEEDING = "[Bleeding]"
    GASEOUS = "[Gaseous]"
    SLICK = "[Slick]"
    DARK = "[Dark]"
    HARDENED = "[Hardened]"
    SPIKY = "[Spiky]"
    TERRIFYING = "[Terrifying]"
    REGENERATING = "[Regenerating]"


@dataclass(frozen=True)
class ThreatProfile:
    """Deterministic threat profile for enemy attacks and hazard detonations."""
    threat_stat: str = "Tough"
    difficulty: Difficulty = Difficulty.NORMAL
    threat_tn: int = 1
    damage: int = 1
    tags: Set[str] = field(default_factory=set)
    impact_size: int = 1
    is_aoe: bool = False
    cleave: bool = False
    range_zones: int = 0

    @property
    def shorthand(self) -> str:
        """Visual shorthand notation: e.g. Tough 5+/2 (2 Dmg)."""
        diff_str = self.difficulty.label
        aoe_str = " AoE" if self.is_aoe else ""
        return f"{self.threat_stat} {diff_str}/{self.threat_tn} ({self.damage} Dmg{aoe_str})"
