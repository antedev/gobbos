"""Enemy Traits, Reactions, and Ancestry Handlers."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Set

from combat_sim.core.types import (
    Ancestry,
    Condition,
    Difficulty,
    Tag,
    WeaponTrait,
)


@dataclass
class EnemyTrait(ABC):
    """Abstract base class for active and passive enemy traits and reactions."""
    name: str
    description: str = ""

    def on_round_start(self, enemy: Any, state: Optional[Any] = None) -> None:
        """Triggered at the start of each combat round."""
        pass

    def on_round_end(self, enemy: Any, state: Optional[Any] = None) -> None:
        """Triggered during the Round Closure phase."""
        pass

    def on_incoming_attack_modify_difficulty(
        self, enemy: Any, attacker: Any, attack: Any, current_diff: Difficulty
    ) -> Difficulty:
        """Modify attack difficulty threshold (e.g. Parrying Buckler)."""
        return current_diff

    def on_incoming_attack_modify_pool(
        self, enemy: Any, attacker: Any, attack: Any, current_pool: int
    ) -> int:
        """Modify attacker dice pool size (e.g. Thick Blubber / Dry Bones)."""
        return current_pool

    def on_incoming_damage_modify(
        self,
        enemy: Any,
        attacker: Any,
        damage: int,
        tags: Optional[Set[str]] = None,
        traits: Optional[Set[WeaponTrait]] = None,
    ) -> int:
        """Modify damage taken (e.g. Plate Bastion)."""
        return damage

    def on_wound_taken(
        self, enemy: Any, wounds_taken: int, source: Any, state: Optional[Any] = None
    ) -> Optional[Dict[str, Any]]:
        """Triggered when the enemy suffers one or more Wounds (e.g. Steam Vent)."""
        return None

    def on_morale_check_trigger(self, enemy: Any, trigger_reason: str) -> bool:
        """Evaluate if trait prevents or forces an immediate Morale check."""
        return False


# =========================================================================
# Specific Unique Traits & Reactions
# =========================================================================

@dataclass
class ParryingBuckler(EnemyTrait):
    """The first melee attack each round is Hard (6); subsequent melee attacks are Normal (5+)."""
    name: str = "Parrying Buckler"
    description: str = "1st melee attack received each round is Hard 6; subsequent melee attacks are Normal 5+."
    buckler_active: bool = True

    def on_round_start(self, enemy: Any, state: Optional[Any] = None) -> None:
        self.buckler_active = True

    def on_incoming_attack_modify_difficulty(
        self, enemy: Any, attacker: Any, attack: Any, current_diff: Difficulty
    ) -> Difficulty:
        # Check if attack is melee (range_zones == 0)
        is_melee = getattr(attack, "is_melee", True) if attack else True
        if self.buckler_active and is_melee:
            self.buckler_active = False
            return Difficulty.HARD
        return current_diff


@dataclass
class ThickBlubber(EnemyTrait):
    """Dense blubber imposes Bane 1 (-1d) on incoming attacks unless carrying the [Fire] tag."""
    name: str = "Thick Blubber"
    description: str = "-1d Bane on incoming attacks unless attack has [Fire] tag."

    def on_incoming_attack_modify_pool(
        self, enemy: Any, attacker: Any, attack: Any, current_pool: int
    ) -> int:
        tags: Set[str] = getattr(attack, "tags", set()) if attack else set()
        if Tag.FIRE not in tags and "[Fire]" not in tags:
            return max(0, current_pool - 1)
        return current_pool


@dataclass
class PlateBastion(EnemyTrait):
    """Ignores first 1 point of damage unless attack has Piercing or elemental tags."""
    name: str = "Plate Armor Bastion"
    description: str = "Ignores first 1 damage per attack unless Piercing, [Fire], [Acidic], or [Shock]."

    def on_incoming_damage_modify(
        self,
        enemy: Any,
        attacker: Any,
        damage: int,
        tags: Optional[Set[str]] = None,
        traits: Optional[Set[WeaponTrait]] = None,
    ) -> int:
        t_set = tags or set()
        tr_set = traits or set()
        
        has_piercing = WeaponTrait.PIERCING in tr_set
        has_element = bool(t_set.intersection({Tag.FIRE, Tag.ACIDIC, Tag.SHOCK, "[Fire]", "[Acidic]", "[Shock]"}))
        
        if not has_piercing and not has_element:
            return max(0, damage - 1)
        return damage


@dataclass
class Bastion(PlateBastion):
    """Alias for PlateBastion."""
    name: str = "Bastion"


@dataclass
class PressurizedSteamVent(EnemyTrait):
    """Taking a Wound releases scalding steam (all goblins in zone test Slink 5+/2 or take 2 Fire damage)."""
    name: str = "Pressurized Steam Vent"
    description: str = "Taking a Wound erupts steam across zone; all goblins test Slink 5+/2 or take 2 Fire damage."

    def on_wound_taken(
        self, enemy: Any, wounds_taken: int, source: Any, state: Optional[Any] = None
    ) -> Optional[Dict[str, Any]]:
        if wounds_taken >= 1:
            return {
                "steam_vent_burst": True,
                "threat_difficulty": Difficulty.NORMAL,
                "threat_tn": 2,
                "damage": 2,
                "tags": {Tag.FIRE},
                "zone_id": getattr(enemy, "zone_id", None),
            }
        return None


@dataclass
class SteamVent(PressurizedSteamVent):
    """Alias for PressurizedSteamVent."""
    name: str = "Steam Vent"


@dataclass
class VoraciousRegrowth(EnemyTrait):
    """Recovers 1 lost Wound at Round Start unless damaged by [Fire] or [Acidic] in prior round."""
    name: str = "Voracious Regrowth"
    description: str = "Heals 1 lost Wound at Round Start unless damaged by [Fire] or [Acidic] in prior round."

    def on_round_start(self, enemy: Any, state: Optional[Any] = None) -> None:
        disabled = getattr(enemy, "last_round_fire_or_acid_damage", False)
        current_wounds = getattr(enemy, "wounds", 0)
        max_wounds = getattr(enemy, "max_wounds", 0)
        if not disabled and current_wounds < max_wounds:
            enemy.heal_wound(1)


@dataclass
class DryBones(EnemyTrait):
    """Skeletal anatomy: Piercing/Cutting/Bows suffer Bane 1 (-1d); Bashing/Crushing gain Boon 1 (+1d)."""
    name: str = "Dry Bones"
    description: str = "Piercing/Cutting suffer -1d Bane; Bashing/Crushing gain +1d Boon."

    def on_incoming_attack_modify_pool(
        self, enemy: Any, attacker: Any, attack: Any, current_pool: int
    ) -> int:
        traits: Set[WeaponTrait] = getattr(attack, "traits", set()) if attack else set()
        is_ranged = getattr(attack, "is_ranged", False) if attack else False

        pool = current_pool
        # Check Bashing / Crushing
        if WeaponTrait.BASHING in traits or WeaponTrait.CRUSHING in traits:
            pool += 1
        # Check Piercing / Cutting or ranged bow
        elif WeaponTrait.PIERCING in traits or WeaponTrait.CUTTING in traits or is_ranged:
            pool = max(0, pool - 1)
        return pool


# =========================================================================
# Ancestry Trait Handlers
# =========================================================================

@dataclass
class BeastAncestryTrait(EnemyTrait):
    """Beast ancestry: Fire/Loud morale triggers and mindless immunity."""
    name: str = "Beast Ancestry"
    description: str = "Triggers Morale on [Fire] / [Loud] / 50% loss; immune to Mouth persuasion."

    def on_morale_check_trigger(self, enemy: Any, trigger_reason: str) -> bool:
        if trigger_reason in ("fire", "loud", "50_percent_loss"):
            return True
        return False


@dataclass
class UndeadAncestryTrait(EnemyTrait):
    """Undead ancestry: Morale immune, Terrified immune, holy weakness."""
    name: str = "Undead Ancestry"
    description: str = "Immune to Morale and Terrified; Holy/Angelic attacks deal +1 Success."

    def on_morale_check_trigger(self, enemy: Any, trigger_reason: str) -> bool:
        return False  # Never triggers morale check


@dataclass
class MonstrosityAncestryTrait(EnemyTrait):
    """Monstrosity ancestry: Hulking mass resistance and natural Sweeping Cleave."""
    name: str = "Monstrosity Ancestry"
    description: str = "Immune to Prone/Stagger unless Impact Size >= Size; melee attacks naturally Cleave."


@dataclass
class FiendAncestryTrait(EnemyTrait):
    """Fiend ancestry: Fire immunity, holy weakness, chaos opportunism."""
    name: str = "Fiend Ancestry"
    description: str = "Immune to [Fire]; [Purified]/[Angelic] reduces Defence TN by 1."


@dataclass
class HumanoidAncestryTrait(EnemyTrait):
    """Humanoid ancestry: Tactical discipline and standard morale."""
    name: str = "Humanoid Ancestry"
    description: str = "Tactical discipline and standard 50% casualty morale checks."
