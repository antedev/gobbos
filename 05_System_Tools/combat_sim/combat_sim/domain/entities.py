"""Core combat entity domain models: Goblin Bosses, Mobs, and Deterministic Enemies."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Type, Union

from combat_sim.core.types import (
    ActionType,
    Ancestry,
    Condition,
    Difficulty,
    EnemyScale,
    Tag,
    ThreatProfile,
    WeaponTrait,
)
from combat_sim.domain.equipment import Armor, Equipment, Shield, Weapon
from combat_sim.domain.quirks import Quirk
from combat_sim.domain.traits import EnemyTrait


@dataclass
class BaseEntity(ABC):
    """Abstract base entity representing all combatants in a tactical encounter."""
    id: str
    name: str
    zone_id: str
    size: int = 1
    is_alive: bool = True
    conditions: Set[Condition] = field(default_factory=set)

    def has_condition(self, condition: Condition) -> bool:
        """Check if entity is currently affected by a condition."""
        return condition in self.conditions

    def add_condition(self, condition: Condition) -> None:
        """Apply a status condition to the entity."""
        self.conditions.add(condition)

    def remove_condition(self, condition: Condition) -> bool:
        """Remove a status condition. Returns True if was present."""
        if condition in self.conditions:
            self.conditions.remove(condition)
            return True
        return False

    def clear_stagger(self) -> None:
        """Clear the Staggered condition (automatically executed during Round Closure)."""
        self.remove_condition(Condition.STAGGERED)

    def move_to(self, new_zone_id: str) -> None:
        """Update entity's current zone location."""
        self.zone_id = new_zone_id

    @property
    def is_staggered(self) -> bool:
        return Condition.STAGGERED in self.conditions

    @property
    def is_prone(self) -> bool:
        return Condition.PRONE in self.conditions

    @property
    def is_weakened(self) -> bool:
        return Condition.WEAKENED in self.conditions

    @property
    def is_restrained(self) -> bool:
        return Condition.RESTRAINED in self.conditions

    @property
    def is_blinded(self) -> bool:
        return Condition.BLINDED in self.conditions

    @property
    def is_silenced(self) -> bool:
        return Condition.SILENCED in self.conditions

    @property
    def is_terrified(self) -> bool:
        return Condition.TERRIFIED in self.conditions

    @property
    def is_stunned(self) -> bool:
        return Condition.STUNNED in self.conditions

    @property
    def is_dumb(self) -> bool:
        return Condition.DUMB in self.conditions


@dataclass
class GoblinBoss(BaseEntity):
    """Player Character Goblin Boss with stats, Grit, action economy, and loadout."""
    tough: int = 1
    slink: int = 1
    mouth: int = 1
    brains: int = 1
    grunt: int = 1
    max_grunt: int = 1

    grit: int = 4
    max_grit: int = 4

    actions_left: int = 3
    max_actions: int = 3
    free_orders_left: int = 1
    max_free_orders: int = 1
    saved_reactions: int = 0

    main_hand: Optional[Weapon] = None
    off_hand: Optional[Equipment] = None
    armor: Optional[Armor] = None
    inventory: List[Equipment] = field(default_factory=list)
    quirks: List[Quirk] = field(default_factory=list)

    def __post_init__(self):
        # Auto-calculate max_grit if not explicitly set
        if self.max_grit == 4 and self.tough > 0:
            # Formula: 4 + 2 * tough (PROD 10_Stats.md)
            calculated_grit = 4 + (2 * self.tough)
            if self.grit == 4:
                self.grit = calculated_grit
            self.max_grit = calculated_grit
        if self.max_grunt == 1:
            self.max_grunt = max(1, self.grunt)

    def reset_turn_actions(self) -> None:
        """Reset action budget at the start of the round."""
        self.actions_left = self.max_actions
        self.free_orders_left = self.max_free_orders
        self.saved_reactions = 0

    def save_reaction(self) -> bool:
        """Reserve a Standard Action to be used as a Reaction during the Enemy Turn."""
        if self.actions_left > 0:
            self.actions_left -= 1
            self.saved_reactions += 1
            return True
        return False

    def use_reaction(self) -> bool:
        """Consume a reserved Reaction."""
        if self.saved_reactions > 0:
            self.saved_reactions -= 1
            return True
        return False

    def spend_grunt(self, amount: int = 1) -> bool:
        """Deduct Grunt points if available."""
        if self.grunt >= amount:
            self.grunt -= amount
            return True
        return False

    def gain_grunt(self, amount: int = 1) -> None:
        """Recover Grunt points up to max_grunt."""
        self.grunt = min(self.max_grunt, self.grunt + amount)

    def take_damage(self, dmg: int) -> int:
        """Apply unmitigated damage to Grit. Updates alive state."""
        if dmg <= 0:
            return 0
        actual_loss = min(self.grit, dmg)
        self.grit -= dmg
        if self.grit <= 0:
            self.grit = 0
            self.is_alive = False
        return actual_loss

    def heal_grit(self, amount: int) -> int:
        """Restore lost Grit points up to max_grit."""
        if amount <= 0:
            return 0
        old_grit = self.grit
        self.grit = min(self.max_grit, self.grit + amount)
        if self.grit > 0:
            self.is_alive = True
        return self.grit - old_grit

    def get_armor_dice(self) -> int:
        """Calculate total passive Armor Dice from equipped armor and shield."""
        total = 0
        if self.armor:
            total += self.armor.armor_dice
        if isinstance(self.off_hand, Shield):
            total += self.off_hand.armor_dice
        return total

    def get_slink_bane(self) -> int:
        """Determine Slink test penalty imposed by equipped armor."""
        if self.armor:
            return self.armor.slink_bane
        return 0

    def can_parry(self) -> bool:
        """Check if Boss has a Shield equipped that enables Tough Parry reactions."""
        return isinstance(self.off_hand, Shield) and self.off_hand.enables_parry

    def get_carry_capacity(self) -> int:
        """Calculate unburdened carry capacity in Bulk (4 + 2 * Tough + Quirk bonuses)."""
        base_cap = 4 + (2 * self.tough)
        for q in self.quirks:
            if q.name == "Swallow Loot":
                base_cap += getattr(q, "internal_bulk_capacity", 2)
        return base_cap

    def get_total_carried_bulk(self) -> int:
        """Sum total bulk of all equipped and carried items."""
        total = 0
        if self.main_hand:
            total += self.main_hand.bulk
        if self.off_hand:
            total += self.off_hand.bulk
        if self.armor:
            total += self.armor.bulk
        for item in self.inventory:
            total += item.bulk
        return total

    def get_movement_speed(self) -> int:
        """Determine movement in zones per Move action based on Slink and gear."""
        # Slink 1: 2, Slink 2-3: 3, Slink 4: 4, Slink 5: 5
        if self.slink <= 1:
            speed = 2
        elif self.slink <= 3:
            speed = 3
        elif self.slink == 4:
            speed = 4
        else:
            speed = 5

        # Check if off_hand shield halves movement (e.g. Tower Pavise)
        if isinstance(self.off_hand, Shield) and self.off_hand.halves_movement:
            speed = max(1, speed // 2)

        # Check if over-laden
        if self.get_total_carried_bulk() > self.get_carry_capacity():
            speed = max(1, speed - 1)

        return speed

    def has_quirk(self, quirk_cls_or_name: Union[str, Type[Quirk]]) -> bool:
        """Check if Boss has the specified Quirk equipped."""
        if isinstance(quirk_cls_or_name, str):
            return any(q.name.lower() == quirk_cls_or_name.lower() for q in self.quirks)
        return any(isinstance(q, quirk_cls_or_name) for q in self.quirks)

    def get_quirk(self, quirk_cls_or_name: Union[str, Type[Quirk]]) -> Optional[Quirk]:
        """Retrieve the Quirk instance if equipped."""
        if isinstance(quirk_cls_or_name, str):
            for q in self.quirks:
                if q.name.lower() == quirk_cls_or_name.lower():
                    return q
            return None
        for q in self.quirks:
            if isinstance(q, quirk_cls_or_name):
                return q
        return None


@dataclass
class PlayerMob(BaseEntity):
    """Player-controlled Mob of runts with symmetrical Dice-HP and casualty scaling."""
    size: int = 3
    health_dice: List[int] = field(default_factory=list)
    actions_left: int = 2
    max_actions: int = 2
    saved_reactions: int = 0
    is_ordered: bool = False
    out_of_control: bool = False
    armor_rating: int = 0  # 0 = None, 1 = Light (+1d), 2 = Medium (+2d)
    equipment: List[Equipment] = field(default_factory=list)
    boss_id: Optional[str] = None

    def __post_init__(self):
        if not self.health_dice and self.size > 0:
            self.health_dice = [6] * self.size
        elif self.health_dice:
            self.size = len(self.health_dice)

    def reset_turn_actions(self) -> None:
        """Reset action economy at round start."""
        self.actions_left = self.max_actions
        self.saved_reactions = 0
        self.is_ordered = False

    def take_single_target_damage(self, dmg: int) -> int:
        """Apply single-target damage to active die with spillover into subsequent dice."""
        if dmg <= 0 or not self.health_dice:
            return 0

        initial_hp = sum(self.health_dice)
        remaining_damage = dmg

        while remaining_damage > 0 and self.health_dice:
            active_die = self.health_dice[0]
            if active_die > remaining_damage:
                self.health_dice[0] -= remaining_damage
                remaining_damage = 0
            else:
                # Active die is exhausted and removed
                remaining_damage -= active_die
                self.health_dice.pop(0)

        self.size = len(self.health_dice)
        if self.size == 0:
            self.is_alive = False

        total_dealt = initial_hp - sum(self.health_dice)
        return total_dealt

    def take_aoe_damage(self, dmg: int) -> int:
        """Apply AoE/Cleave damage simultaneously to EVERY single die in the health pool."""
        if dmg <= 0 or not self.health_dice:
            return 0

        initial_hp = sum(self.health_dice)
        new_dice = []
        for d in self.health_dice:
            remaining = d - dmg
            if remaining > 0:
                new_dice.append(remaining)

        self.health_dice = new_dice
        self.size = len(self.health_dice)
        if self.size == 0:
            self.is_alive = False

        total_dealt = initial_hp - sum(self.health_dice)
        return total_dealt

    def get_attack_pool_size(self) -> int:
        """Calculate base melee attack dice pool size (= Current Size)."""
        pool = self.size
        if self.is_weakened:
            pool = max(0, pool - 1)
        return pool

    def get_carry_capacity(self) -> int:
        """Calculate Mob total carry capacity in Bulk (Size * 4)."""
        return self.size * 4

    def get_armor_dice(self) -> int:
        """Return passive armor dice granted by outfitting."""
        dice = self.armor_rating
        if self.is_staggered:
            dice = max(0, dice - 1)
        return dice


@dataclass
class ThreatAttack:
    """An incoming deterministic attack action from an enemy."""
    name: str
    threat_stat: str = "Tough"
    difficulty: Difficulty = Difficulty.NORMAL
    threat_tn: int = 1
    damage: int = 1
    tags: Set[str] = field(default_factory=set)
    impact_size: int = 1
    is_aoe: bool = False
    cleave: bool = False
    range_zones: int = 0
    threat_profile: Optional[ThreatProfile] = None

    def __post_init__(self):
        if self.threat_profile is not None:
            tp = self.threat_profile
            self.threat_stat = tp.threat_stat
            self.difficulty = tp.difficulty
            self.threat_tn = tp.threat_tn
            self.damage = tp.damage
            self.tags = tp.tags
            self.impact_size = tp.impact_size
            self.is_aoe = tp.is_aoe
            self.cleave = tp.cleave
            self.range_zones = tp.range_zones
        else:
            self.threat_profile = ThreatProfile(
                threat_stat=self.threat_stat,
                difficulty=self.difficulty,
                threat_tn=self.threat_tn,
                damage=self.damage,
                tags=self.tags,
                impact_size=self.impact_size,
                is_aoe=self.is_aoe,
                cleave=self.cleave,
                range_zones=self.range_zones,
            )

    @property
    def is_melee(self) -> bool:
        return self.range_zones == 0

    @property
    def is_ranged(self) -> bool:
        return self.range_zones > 0


@dataclass
class Enemy(BaseEntity):
    """Abstract base enemy class implementing deterministic threat models."""
    enemy_scale: EnemyScale = EnemyScale.STANDARD
    ancestry: Ancestry = Ancestry.HUMANOID
    defence_tn: int = 1
    movement: int = 2
    morale_tn: int = 1
    actions_left: int = 2
    max_actions: int = 2
    traits: List[EnemyTrait] = field(default_factory=list)
    attacks: List[ThreatAttack] = field(default_factory=list)
    has_fled: bool = False

    def reset_turn_actions(self) -> None:
        """Reset actions at the start of the round."""
        self.actions_left = self.max_actions

    def get_effective_defence_tn(self) -> int:
        """Calculate Defence TN after accounting for Staggered condition (-1 TN, min 1)."""
        if self.is_staggered:
            return max(1, self.defence_tn - 1)
        return self.defence_tn

    def has_trait(self, trait_cls_or_name: Union[str, Type[EnemyTrait]]) -> bool:
        """Check if enemy has an active trait."""
        if isinstance(trait_cls_or_name, str):
            return any(t.name.lower() == trait_cls_or_name.lower() for t in self.traits)
        return any(isinstance(t, trait_cls_or_name) for t in self.traits)

    def get_trait(self, trait_cls_or_name: Union[str, Type[EnemyTrait]]) -> Optional[EnemyTrait]:
        """Retrieve the active trait instance if present."""
        if isinstance(trait_cls_or_name, str):
            for t in self.traits:
                if t.name.lower() == trait_cls_or_name.lower():
                    return t
            return None
        for t in self.traits:
            if isinstance(t, trait_cls_or_name):
                return t
        return None

    def add_trait(self, trait: EnemyTrait) -> None:
        """Attach a trait to this enemy."""
        self.traits.append(trait)


@dataclass
class StandardEnemy(Enemy):
    """Standard minion enemy (One-Hit Kill on attacks meeting Defence TN)."""
    enemy_scale: EnemyScale = EnemyScale.STANDARD

    def take_hit(self, successes: int, impact_size: int = 1) -> Dict[str, Any]:
        """Resolve incoming hit against Standard Enemy."""
        eff_def = self.get_effective_defence_tn()
        if successes >= eff_def:
            self.is_alive = False
            return {"killed": True, "staggered": False, "wounds_dealt": 1}
        elif successes >= 1 and impact_size >= self.size:
            self.add_condition(Condition.STAGGERED)
            return {"killed": False, "staggered": True, "wounds_dealt": 0}
        return {"killed": False, "staggered": False, "wounds_dealt": 0}


@dataclass
class EliteEnemy(Enemy):
    """Elite / Boss enemy tracking multiple Wounds with Overkill wound conversion."""
    enemy_scale: EnemyScale = EnemyScale.ELITE
    wounds: int = 2
    max_wounds: int = 2
    last_round_fire_or_acid_damage: bool = False
    current_round_fire_or_acid_damage: bool = False

    def take_hit(
        self, successes: int, impact_size: int = 1, tags: Optional[Set[str]] = None
    ) -> Dict[str, Any]:
        """Resolve incoming attack with Overkill wound conversion (floor(successes / Defence TN))."""
        eff_def = self.get_effective_defence_tn()
        wounds_dealt = successes // eff_def if successes >= eff_def else 0

        if wounds_dealt > 0:
            self.wounds = max(0, self.wounds - wounds_dealt)
            if self.wounds == 0:
                self.is_alive = False
            
            # Check elemental tags for Voracious Regrowth suppression
            t_set = tags or set()
            if bool(t_set.intersection({Tag.FIRE, Tag.ACIDIC, "[Fire]", "[Acidic]" })):
                self.current_round_fire_or_acid_damage = True

            # Trigger on_wound_taken trait reactions (e.g. Steam Vent)
            trait_reactions = []
            for trait in self.traits:
                reaction = trait.on_wound_taken(self, wounds_dealt, source=None)
                if reaction:
                    trait_reactions.append(reaction)

            return {
                "wounds_dealt": wounds_dealt,
                "staggered": False,
                "killed": not self.is_alive,
                "wounds_remaining": self.wounds,
                "trait_reactions": trait_reactions,
            }
        elif successes >= 1 and impact_size >= self.size:
            self.add_condition(Condition.STAGGERED)
            return {
                "wounds_dealt": 0,
                "staggered": True,
                "killed": False,
                "wounds_remaining": self.wounds,
                "trait_reactions": [],
            }
        return {
            "wounds_dealt": 0,
            "staggered": False,
            "killed": False,
            "wounds_remaining": self.wounds,
            "trait_reactions": [],
        }

    def heal_wound(self, amount: int = 1) -> int:
        """Recover lost Wounds up to max_wounds."""
        if amount <= 0:
            return 0
        old_wounds = self.wounds
        self.wounds = min(self.max_wounds, self.wounds + amount)
        if self.wounds > 0:
            self.is_alive = True
        return self.wounds - old_wounds


@dataclass
class EnemyMob(Enemy):
    """Enemy mob entity sharing Dice-HP with deterministic casualty-scaled attacks."""
    enemy_scale: EnemyScale = EnemyScale.MOB
    size: int = 3
    health_dice: List[int] = field(default_factory=list)
    base_damage: int = 1

    def __post_init__(self):
        if not self.health_dice and self.size > 0:
            self.health_dice = [6] * self.size
        elif self.health_dice:
            self.size = len(self.health_dice)

    def get_mob_damage(self) -> int:
        """Calculate deterministic attack damage (= Base Damage + Current Size - 1)."""
        return self.base_damage + max(0, self.size - 1)

    def take_single_target_damage(self, dmg: int) -> int:
        """Apply single-target damage to active die with spillover."""
        if dmg <= 0 or not self.health_dice:
            return 0

        initial_hp = sum(self.health_dice)
        remaining_damage = dmg

        while remaining_damage > 0 and self.health_dice:
            active_die = self.health_dice[0]
            if active_die > remaining_damage:
                self.health_dice[0] -= remaining_damage
                remaining_damage = 0
            else:
                remaining_damage -= active_die
                self.health_dice.pop(0)

        self.size = len(self.health_dice)
        if self.size == 0:
            self.is_alive = False

        return initial_hp - sum(self.health_dice)

    def take_aoe_damage(self, dmg: int) -> int:
        """Apply AoE/Cleave damage simultaneously to all dice in pool."""
        if dmg <= 0 or not self.health_dice:
            return 0

        initial_hp = sum(self.health_dice)
        new_dice = []
        for d in self.health_dice:
            rem = d - dmg
            if rem > 0:
                new_dice.append(rem)

        self.health_dice = new_dice
        self.size = len(self.health_dice)
        if self.size == 0:
            self.is_alive = False

        return initial_hp - sum(self.health_dice)
