"""Weapons, Armor, Shields, Consumables, and Equipment Catalogue."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from typing import Set

from combat_sim.core.types import (
    Difficulty,
    Tag,
    ThreatProfile,
    WeaponHandedness,
    WeaponTrait,
)


@dataclass
class Equipment(ABC):
    """Abstract base class for all inventory and tactical items."""
    name: str
    bulk: int = 1
    tier: int = 1
    break_threshold: int = 0  # Breaks on 1..break_threshold on Fumble Break roll

    def roll_breaks(self, break_roll: int) -> bool:
        """Evaluate if an item shatters on a Fumble break roll."""
        if self.break_threshold <= 0:
            return False
        return break_roll <= self.break_threshold


@dataclass
class Weapon(Equipment):
    """Melee and ranged weaponry with handedness, ranges, and tactical traits."""
    handedness: WeaponHandedness = WeaponHandedness.ONE_HAND
    impact_size_modifier: int = 0
    traits: Set[WeaponTrait] = field(default_factory=set)
    tags: Set[str] = field(default_factory=set)
    range_zones: int = 0  # 0 = Melee (same zone), 1 = Thrown/Sling, 2 = Bow/Crossbow, 3 = Longbow/Arbalest
    min_tough: int = 0
    min_brains: int = 0

    @property
    def is_melee(self) -> bool:
        """True if weapon is designed for melee combat within the same zone."""
        return self.range_zones == 0

    @property
    def is_ranged(self) -> bool:
        """True if weapon can target enemies across discrete zones."""
        return self.range_zones > 0

    def has_trait(self, trait: WeaponTrait) -> bool:
        """Check if weapon has the specified mechanical trait."""
        return trait in self.traits

    def has_tag(self, tag: str) -> bool:
        """Check if weapon carries the specified property tag."""
        return tag in self.tags

    def get_effective_impact_size(self, wielder_size: int = 1) -> int:
        """Calculate effective impact size for Stagger condition evaluations."""
        return max(0, wielder_size + self.impact_size_modifier)


@dataclass
class Armor(Equipment):
    """Protective suits granting passive Armor Dice during Clatter mitigation."""
    armor_dice: int = 1
    slink_bane: int = 0
    cannot_swim: bool = False


@dataclass
class Shield(Equipment):
    """Defensive shields providing passive armor and unlocking active Parry reactions."""
    armor_dice: int = 1
    enables_parry: bool = True
    halves_movement: bool = False
    immune_to_piercing: bool = False


@dataclass
class Consumable(Equipment):
    """Throwables, bombs, and tactical alchemy with area threat profiles."""
    threat: ThreatProfile = field(default_factory=ThreatProfile)
    blast_range: int = 0  # Target distance in zones (0 = same zone, 1 = adjacent zone, etc.)
    is_explosive: bool = False
    impact_size: int = 1
    damage: int = 1
    tags: Set[str] = field(default_factory=set)


# =========================================================================
# Standard Equipment Catalogue Factory Functions
# =========================================================================

# --- Melee Weapons ---

def create_bone_shiv() -> Weapon:
    """T1 Light Melee (1H, Bulk 1, Concealable)."""
    return Weapon(
        name="Sharpened Bone Shiv",
        bulk=1,
        tier=1,
        break_threshold=4,
        handedness=WeaponHandedness.ONE_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.CONCEALABLE, WeaponTrait.PIERCING},
        range_zones=0,
    )


def create_notched_sword() -> Weapon:
    """T2 Medium Melee (1H, Bulk 2, Cutting)."""
    return Weapon(
        name="Notched Scimitar / Sword",
        bulk=2,
        tier=2,
        break_threshold=3,
        handedness=WeaponHandedness.ONE_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.CUTTING},
        range_zones=0,
    )


def create_medium_sword() -> Weapon:
    """Alias for standard 1H medium sword."""
    return create_notched_sword()


def create_spiked_mace() -> Weapon:
    """T2 Medium Melee (1H, Bulk 2, Bashing)."""
    return Weapon(
        name="Spiked Mace",
        bulk=2,
        tier=2,
        break_threshold=3,
        handedness=WeaponHandedness.ONE_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.BASHING},
        range_zones=0,
    )


def create_heavy_greataxe() -> Weapon:
    """T2 Heavy Melee (2H, Bulk 3, +1 Impact Size, Cleave)."""
    return Weapon(
        name="Scrap Greataxe",
        bulk=3,
        tier=2,
        break_threshold=3,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=1,
        traits={WeaponTrait.HEAVY, WeaponTrait.CLEAVE, WeaponTrait.CUTTING},
        range_zones=0,
    )


def create_greataxe() -> Weapon:
    """Alias for heavy greataxe."""
    return create_heavy_greataxe()


def create_great_hammer() -> Weapon:
    """T3 Heavy Melee (2H, Bulk 3, +2 Impact Size, Crushing, Bashing)."""
    return Weapon(
        name="Dwarven Great-Hammer",
        bulk=3,
        tier=3,
        break_threshold=2,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=2,
        traits={WeaponTrait.CRUSHING, WeaponTrait.BASHING, WeaponTrait.HEAVY},
        range_zones=0,
    )


def create_dwarven_great_hammer() -> Weapon:
    """Alias for Dwarven Great-Hammer."""
    return create_great_hammer()


def create_halberd() -> Weapon:
    """T3 Heavy Melee (2H, Bulk 3, +1 Impact Size, Reach, Cleave)."""
    return Weapon(
        name="Guardsman Halberd",
        bulk=3,
        tier=3,
        break_threshold=2,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=1,
        traits={WeaponTrait.HEAVY, WeaponTrait.REACH, WeaponTrait.CLEAVE, WeaponTrait.CUTTING},
        range_zones=0,
    )


# --- Ranged Weapons ---

def create_sling() -> Weapon:
    """T1 Ranged (1H, Bulk 1, Range 1 Zone, Fast Throw)."""
    return Weapon(
        name="Leather Sling",
        bulk=1,
        tier=1,
        break_threshold=4,
        handedness=WeaponHandedness.ONE_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.FAST_THROW, WeaponTrait.BASHING},
        range_zones=1,
    )


def create_shortbow() -> Weapon:
    """T2 Ranged (2H, Bulk 2, Range 2 Zones, Rapid Shot)."""
    return Weapon(
        name="Shortbow",
        bulk=2,
        tier=2,
        break_threshold=3,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.RAPID_SHOT, WeaponTrait.PIERCING},
        range_zones=2,
    )


def create_light_crossbow() -> Weapon:
    """T2 Ranged (2H, Bulk 2, Range 2 Zones, min_brains=2, Armor Piercing)."""
    return Weapon(
        name="Light Crossbow",
        bulk=2,
        tier=2,
        break_threshold=3,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.ARMOR_PIERCING, WeaponTrait.PIERCING},
        range_zones=2,
        min_brains=2,
    )


def create_crossbow() -> Weapon:
    """Alias for light crossbow."""
    return create_light_crossbow()


def create_military_longbow() -> Weapon:
    """T3 Ranged (2H, Bulk 2, Range 3 Zones, min_tough=2, Piercing)."""
    return Weapon(
        name="Military Longbow",
        bulk=2,
        tier=3,
        break_threshold=2,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.PIERCING},
        range_zones=3,
        min_tough=2,
    )


def create_longbow() -> Weapon:
    """Alias for military longbow."""
    return create_military_longbow()


def create_heavy_arbalest() -> Weapon:
    """T3 Ranged (2H, Bulk 3, Range 3 Zones, min_tough=2, min_brains=2, Heavy [+1 Impact], Armor Piercing)."""
    return Weapon(
        name="Heavy Siege Arbalest",
        bulk=3,
        tier=3,
        break_threshold=2,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=1,
        traits={WeaponTrait.HEAVY, WeaponTrait.ARMOR_PIERCING, WeaponTrait.PIERCING},
        range_zones=3,
        min_tough=2,
        min_brains=2,
    )


def create_arbalest() -> Weapon:
    """Alias for heavy arbalest."""
    return create_heavy_arbalest()


def create_repeating_crossbow() -> Weapon:
    """T4 Ranged (2H, Bulk 3, Range 2 Zones, Clockwork Feed)."""
    return Weapon(
        name="Repeating Clockwork Crossbow",
        bulk=3,
        tier=4,
        break_threshold=1,
        handedness=WeaponHandedness.TWO_HAND,
        impact_size_modifier=0,
        traits={WeaponTrait.CLOCKWORK, WeaponTrait.PIERCING},
        range_zones=2,
        min_brains=2,
    )


# --- Armor & Shields ---

def create_light_armor() -> Armor:
    """T1 Light Armor (+1d Armor Die, 0 Slink Bane, Bulk 1)."""
    return Armor(
        name="Padded Leather Jerkin",
        bulk=1,
        tier=1,
        break_threshold=4,
        armor_dice=1,
        slink_bane=0,
        cannot_swim=False,
    )


def create_medium_armor() -> Armor:
    """T2 Medium Armor (+2d Armor Dice, Bane 1 on Slink, Bulk 2)."""
    return Armor(
        name="Riveted Mail Hauberk",
        bulk=2,
        tier=2,
        break_threshold=3,
        armor_dice=2,
        slink_bane=1,
        cannot_swim=False,
    )


def create_heavy_armor() -> Armor:
    """T3 Heavy Armor (+3d Armor Dice, Bane 2 on Slink, Bulk 3, Cannot Swim)."""
    return Armor(
        name="Ironclad Plate Harness",
        bulk=3,
        tier=3,
        break_threshold=2,
        armor_dice=3,
        slink_bane=2,
        cannot_swim=True,
    )


def create_runed_carapace() -> Armor:
    """T4 Masterwork Heavy Armor (+3d Armor Dice, Bane 1 on Slink, Bulk 3)."""
    return Armor(
        name="Dwarven Runed Carapace",
        bulk=3,
        tier=4,
        break_threshold=1,
        armor_dice=3,
        slink_bane=1,
        cannot_swim=True,
    )


def create_pot_lid_shield() -> Shield:
    """T2 Standard Shield (+1d Armor Die, enables Tough Parry, Bulk 1)."""
    return Shield(
        name="Spiked Pot-Lid Shield",
        bulk=1,
        tier=2,
        break_threshold=3,
        armor_dice=1,
        enables_parry=True,
        halves_movement=False,
        immune_to_piercing=False,
    )


def create_shield() -> Shield:
    """Alias for standard shield."""
    return create_pot_lid_shield()


def create_tower_pavise() -> Shield:
    """T3 Tower Shield (+2d Armor Dice, enables Tough Parry, Halves Movement, Bulk 2)."""
    return Shield(
        name="Tower Pavise",
        bulk=2,
        tier=3,
        break_threshold=2,
        armor_dice=2,
        enables_parry=True,
        halves_movement=True,
        immune_to_piercing=False,
    )


def create_godstone_aegis() -> Shield:
    """T5 Artifact Shield (+2d Armor Dice, enables Parry, immune to piercing, never breaks, Bulk 2)."""
    return Shield(
        name="Godstone Aegis",
        bulk=2,
        tier=5,
        break_threshold=0,
        armor_dice=2,
        enables_parry=True,
        halves_movement=False,
        immune_to_piercing=True,
    )


# --- Consumables & Explosives ---

def create_spark_bomb() -> Consumable:
    """T1 Spark Bomb (Threat 4+/1, 1 Dmg, Blast Range 0, [Explosive], Impact Size 1)."""
    threat = ThreatProfile(
        threat_stat="Slink",
        difficulty=Difficulty.EASY,
        threat_tn=1,
        damage=1,
        tags={Tag.EXPLOSIVE},
        impact_size=1,
        is_aoe=True,
        range_zones=0,
    )
    return Consumable(
        name="Spark Bomb",
        bulk=1,
        tier=1,
        break_threshold=4,
        threat=threat,
        blast_range=0,
        is_explosive=True,
        impact_size=1,
        damage=1,
        tags={Tag.EXPLOSIVE},
    )


def create_fire_flask() -> Consumable:
    """T2 Fire Flask / Molotov (Threat 5+/1, 2 Dmg, Blast Range 1, [Fire], Impact Size 2)."""
    threat = ThreatProfile(
        threat_stat="Slink",
        difficulty=Difficulty.NORMAL,
        threat_tn=1,
        damage=2,
        tags={Tag.FIRE},
        impact_size=2,
        is_aoe=True,
        range_zones=1,
    )
    return Consumable(
        name="Fire Flask (Molotov)",
        bulk=1,
        tier=2,
        break_threshold=3,
        threat=threat,
        blast_range=1,
        is_explosive=False,
        impact_size=2,
        damage=2,
        tags={Tag.FIRE},
    )


def create_molotov() -> Consumable:
    """Alias for Fire Flask."""
    return create_fire_flask()


def create_smoke_pot() -> Consumable:
    """T2 Choking Smoke Pot (Threat 4+/1, 0 Dmg, Blast Range 1, [Gaseous, Dark], Impact Size 0)."""
    threat = ThreatProfile(
        threat_stat="Slink",
        difficulty=Difficulty.EASY,
        threat_tn=1,
        damage=0,
        tags={Tag.GASEOUS, Tag.DARK},
        impact_size=0,
        is_aoe=True,
        range_zones=1,
    )
    return Consumable(
        name="Choking Smoke Pot",
        bulk=1,
        tier=2,
        break_threshold=3,
        threat=threat,
        blast_range=1,
        is_explosive=False,
        impact_size=0,
        damage=0,
        tags={Tag.GASEOUS, Tag.DARK},
    )


def create_powder_keg() -> Consumable:
    """T3 Demolition Powder Keg (Threat 5+/2, 3 Dmg, Blast Range 1, [Explosive], Impact Size 3)."""
    threat = ThreatProfile(
        threat_stat="Slink",
        difficulty=Difficulty.NORMAL,
        threat_tn=2,
        damage=3,
        tags={Tag.EXPLOSIVE},
        impact_size=3,
        is_aoe=True,
        range_zones=1,
    )
    return Consumable(
        name="Demolition Powder Keg",
        bulk=2,
        tier=3,
        break_threshold=2,
        threat=threat,
        blast_range=1,
        is_explosive=True,
        impact_size=3,
        damage=3,
        tags={Tag.EXPLOSIVE},
    )


def create_mortar_shell() -> Consumable:
    """T4 Siege Mortar Shell (Threat 5+/3, 4 Dmg, Blast Range 2, [Explosive], Impact Size 4)."""
    threat = ThreatProfile(
        threat_stat="Slink",
        difficulty=Difficulty.NORMAL,
        threat_tn=3,
        damage=4,
        tags={Tag.EXPLOSIVE},
        impact_size=4,
        is_aoe=True,
        range_zones=2,
    )
    return Consumable(
        name="Siege Mortar Shell",
        bulk=3,
        tier=4,
        break_threshold=1,
        threat=threat,
        blast_range=2,
        is_explosive=True,
        impact_size=4,
        damage=4,
        tags={Tag.EXPLOSIVE},
    )


def create_sol_quartz() -> Consumable:
    """T5 Sol-Quartz Core (Threat 6/3, 5 Dmg, Blast Range 3, [Explosive], Impact Size 5)."""
    threat = ThreatProfile(
        threat_stat="Slink",
        difficulty=Difficulty.HARD,
        threat_tn=3,
        damage=5,
        tags={Tag.EXPLOSIVE, Tag.LIGHT},
        impact_size=5,
        is_aoe=True,
        range_zones=3,
    )
    return Consumable(
        name="Sol-Quartz Core",
        bulk=4,
        tier=5,
        break_threshold=0,
        threat=threat,
        blast_range=3,
        is_explosive=True,
        impact_size=5,
        damage=5,
        tags={Tag.EXPLOSIVE, Tag.LIGHT},
    )
