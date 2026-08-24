"""Combat resolution engines: AttackResolver, ClatterResolver, MobReactionResolver, HazardResolver, MoraleResolver."""

from __future__ import annotations

from dataclasses import dataclass, field
import math
import random
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import combat_sim.core.dice as dice
from combat_sim.core.dice import (
    ClatterResult,
    DiceResult,
    resolve_clatter,
    roll_d6,
    roll_dice,
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
    Armor,
    Consumable,
    Equipment,
    Shield,
    Weapon,
)
from combat_sim.domain.quirks import AnkleBite, MeatShield, PushLuck, Quirk
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import EnemyTrait


@dataclass
class AttackResult:
    """Detailed resolution breakdown of an attack action."""
    hit: bool = False
    successes: int = 0
    wounds_dealt: int = 0
    damage_dealt: int = 0
    staggered: bool = False
    killed: bool = False
    target_defeated: bool = False
    fumble: bool = False
    is_critical: bool = False
    faces: List[int] = field(default_factory=list)
    bonus_faces: List[int] = field(default_factory=list)
    pool_size: int = 0
    gambled: bool = False
    target_remaining: str = ""
    trait_reactions: List[Dict[str, Any]] = field(default_factory=list)
    counter_attack: Optional[Dict[str, Any]] = None
    log_messages: List[str] = field(default_factory=list)


class AttackResolver:
    """Resolves player/mob attacks against enemies and environment."""

    @staticmethod
    def resolve_melee_attack(
        attacker: Union[GoblinBoss, PlayerMob],
        target: Enemy,
        weapon: Optional[Weapon] = None,
        topology: Optional[TopologyGraph] = None,
        allow_gamble: bool = True,
        rng: Optional[random.Random] = None,
    ) -> AttackResult:
        """Execute a Melee Attack action against an enemy in the same Zone."""
        log_msgs: List[str] = []
        eff_defence = target.get_effective_defence_tn()

        # 1. Determine base dice pool
        if isinstance(attacker, GoblinBoss):
            base_pool = attacker.tough
            wielder_size = attacker.size
            # Check Versatile weapon 2H grip (+1d Boon)
            if weapon and weapon.has_trait(WeaponTrait.VERSATILE) and attacker.off_hand is None:
                base_pool += 1
            # Check Butcher quirk
            butcher = attacker.get_quirk("Butcher")
            if butcher and butcher.can_trigger(attacker, {"target": target}):
                res = butcher.apply(attacker, {"target": target})
                base_pool += res.get("boon_dice", 1)
        elif isinstance(attacker, PlayerMob):
            base_pool = attacker.get_attack_pool_size()
            wielder_size = attacker.size
        else:
            base_pool = 1
            wielder_size = 1

        # Check attacker conditions
        if attacker.has_condition(Condition.WEAKENED):
            base_pool = max(0, base_pool - 1)
        if attacker.has_condition(Condition.BLINDED):
            base_pool = max(0, base_pool - 2)

        # 2. Impact Size calculation
        if weapon:
            impact_size = weapon.get_effective_impact_size(wielder_size)
            tags = weapon.tags
            traits = weapon.traits
        else:
            impact_size = wielder_size
            tags = set()
            traits = set()

        # 3. Enemy trait pool & difficulty modifications
        diff = Difficulty.NORMAL
        for trait in target.traits:
            diff = trait.on_incoming_attack_modify_difficulty(target, attacker, weapon, diff)
            base_pool = trait.on_incoming_attack_modify_pool(target, attacker, weapon, base_pool)

        # 4. Roll attack dice pool
        dice_res = roll_dice(
            pool_size=base_pool,
            difficulty=diff,
            tn=eff_defence,
            allow_gamble=allow_gamble,
            rng=rng,
        )

        successes = dice_res.successes
        is_crit = dice_res.is_critical
        fumble = dice_res.fumble

        # 5. Cross-gang super-mob in-fighting penalty
        if isinstance(attacker, PlayerMob) and getattr(attacker, "is_cross_gang", False):
            ones_count = dice_res.faces.count(1)
            if ones_count > 0:
                attacker.take_single_target_damage(ones_count)
                log_msgs.append(f"Cross-gang in-fighting! {ones_count} self-damage to Mob.")

        # 6. Critical double-explosion bonus
        if is_crit and isinstance(attacker, GoblinBoss):
            attacker.gain_grunt(1)
            log_msgs.append(f"Critical Double Explosion! {attacker.name} gained +1 Grunt.")

        # 7. Evaluate hit outcome vs target scale
        wounds_dealt = 0
        damage_dealt = 0
        staggered = False
        killed = False
        target_defeated = False
        trait_reactions = []

        if successes >= eff_defence:
            hit = True
            if isinstance(target, StandardEnemy):
                hit_dict = target.take_hit(successes=successes, impact_size=impact_size)
                killed = hit_dict.get("killed", True)
                target_defeated = killed
                wounds_dealt = 1
                damage_dealt = 1
            elif isinstance(target, EliteEnemy):
                hit_dict = target.take_hit(successes=successes, impact_size=impact_size, tags=tags)
                wounds_dealt = hit_dict.get("wounds_dealt", 0)
                damage_dealt = wounds_dealt
                killed = hit_dict.get("killed", False)
                target_defeated = killed
                trait_reactions = hit_dict.get("trait_reactions", [])
            elif isinstance(target, EnemyMob):
                # Check Cleave trait
                has_cleave = WeaponTrait.CLEAVE in traits
                if has_cleave:
                    damage_dealt = target.take_aoe_damage(successes)
                else:
                    damage_dealt = target.take_single_target_damage(successes)
                killed = not target.is_alive
                target_defeated = killed
        elif successes >= 1:
            # Partial hit: check Stagger
            hit = False
            if impact_size >= target.size:
                target.add_condition(Condition.STAGGERED)
                staggered = True
                log_msgs.append(f"Partial hit ({successes}/{eff_defence} TN)! Impact Size {impact_size} >= Target Size {target.size} inflicts Staggered.")
            else:
                log_msgs.append(f"Partial hit ({successes}/{eff_defence} TN)! Target mass resistance ({target.size} > {impact_size}) negates Stagger.")
        else:
            hit = False
            log_msgs.append(f"Attack missed completely ({successes} successes).")

        if isinstance(target, StandardEnemy):
            target_remaining = "DEAD" if killed else "1 HP"
        elif isinstance(target, EliteEnemy):
            target_remaining = f"{target.wounds}/{target.max_wounds} Wounds"
        elif isinstance(target, EnemyMob):
            target_remaining = f"Size {target.size}, Dice {target.health_dice}" if target.is_alive else "WIPED OUT"
        else:
            target_remaining = "?"

        return AttackResult(
            hit=hit,
            successes=successes,
            wounds_dealt=wounds_dealt,
            damage_dealt=damage_dealt,
            staggered=staggered,
            killed=killed,
            target_defeated=target_defeated,
            fumble=fumble,
            is_critical=is_crit,
            faces=dice_res.faces,
            bonus_faces=dice_res.bonus_faces,
            pool_size=base_pool,
            gambled=dice_res.gambled,
            target_remaining=target_remaining,
            trait_reactions=trait_reactions,
            log_messages=log_msgs,
        )

    @staticmethod
    def resolve_ranged_attack(
        attacker: GoblinBoss,
        target: Enemy,
        weapon: Weapon,
        topology: TopologyGraph,
        allow_gamble: bool = True,
        rng: Optional[random.Random] = None,
    ) -> AttackResult:
        """Execute a Ranged Attack action across discrete zones."""
        log_msgs: List[str] = []
        eff_defence = target.get_effective_defence_tn()

        # Distance check
        dist = topology.get_distance(attacker.zone_id, target.zone_id)
        if dist < 0 or dist > weapon.range_zones:
            return AttackResult(
                hit=False,
                log_messages=[f"Target out of range (Distance {dist} > Range {weapon.range_zones})."],
            )

        # Line of Sight / Cover check
        target_zone = topology.get_zone(target.zone_id)
        cover = target_zone.get_cover_from(attacker.zone_id) if target_zone else CoverType.NONE
        if cover == CoverType.FULL:
            return AttackResult(
                hit=False,
                log_messages=["Target has Full Cover; direct ranged attack impossible."],
            )

        base_pool = attacker.slink - attacker.get_slink_bane()

        # Partial Cover penalty: -1d Bane
        if cover == CoverType.PARTIAL:
            base_pool -= 1

        # Attacker conditions
        if attacker.has_condition(Condition.BLINDED):
            base_pool -= 2
        if attacker.has_condition(Condition.WEAKENED):
            base_pool -= 1

        base_pool = max(0, base_pool)

        # Trait pool modifications
        diff = Difficulty.NORMAL
        for trait in target.traits:
            diff = trait.on_incoming_attack_modify_difficulty(target, attacker, weapon, diff)
            base_pool = trait.on_incoming_attack_modify_pool(target, attacker, weapon, base_pool)

        dice_res = roll_dice(
            pool_size=base_pool,
            difficulty=diff,
            tn=eff_defence,
            allow_gamble=allow_gamble,
            rng=rng,
        )

        successes = dice_res.successes
        is_crit = dice_res.is_critical
        fumble = dice_res.fumble

        impact_size = weapon.get_effective_impact_size(attacker.size)
        tags = weapon.tags

        wounds_dealt = 0
        damage_dealt = 0
        staggered = False
        killed = False
        target_defeated = False
        trait_reactions = []

        if successes >= eff_defence:
            hit = True
            if isinstance(target, StandardEnemy):
                hit_dict = target.take_hit(successes=successes, impact_size=impact_size)
                killed = hit_dict.get("killed", True)
                target_defeated = killed
                wounds_dealt = 1
                damage_dealt = 1
            elif isinstance(target, EliteEnemy):
                hit_dict = target.take_hit(successes=successes, impact_size=impact_size, tags=tags)
                wounds_dealt = hit_dict.get("wounds_dealt", 0)
                damage_dealt = wounds_dealt
                killed = hit_dict.get("killed", False)
                target_defeated = killed
                trait_reactions = hit_dict.get("trait_reactions", [])
            elif isinstance(target, EnemyMob):
                damage_dealt = target.take_single_target_damage(successes)
                killed = not target.is_alive
                target_defeated = killed
        elif successes >= 1:
            hit = False
            if impact_size >= target.size:
                target.add_condition(Condition.STAGGERED)
                staggered = True
        else:
            hit = False

        if isinstance(target, StandardEnemy):
            target_remaining = "DEAD" if killed else "1 HP"
        elif isinstance(target, EliteEnemy):
            target_remaining = f"{target.wounds}/{target.max_wounds} Wounds"
        elif isinstance(target, EnemyMob):
            target_remaining = f"Size {target.size}, Dice {target.health_dice}" if target.is_alive else "WIPED OUT"
        else:
            target_remaining = "?"

        return AttackResult(
            hit=hit,
            successes=successes,
            wounds_dealt=wounds_dealt,
            damage_dealt=damage_dealt,
            staggered=staggered,
            killed=killed,
            target_defeated=target_defeated,
            fumble=fumble,
            is_critical=is_crit,
            faces=dice_res.faces,
            bonus_faces=dice_res.bonus_faces,
            pool_size=base_pool,
            gambled=dice_res.gambled,
            target_remaining=target_remaining,
            trait_reactions=trait_reactions,
            log_messages=log_msgs,
        )


class ClatterResolver:
    """Resolves incoming deterministic enemy attacks against Goblin Bosses and Player Mobs."""

    @staticmethod
    def resolve_boss_defense(
        boss: GoblinBoss,
        attacker: Any,
        threat: ThreatProfile,
        allied_mob: Optional[PlayerMob] = None,
        topology: Optional[TopologyGraph] = None,
        allow_gear_sacrifice: bool = True,
        rng: Optional[random.Random] = None,
    ) -> ClatterResult:
        """Resolve incoming attack on Boss with Meat Shield, Slink/Tough evasion, and Armor mitigation."""
        # 1. Check Meat Shield Quirk
        meat_shield = boss.get_quirk("Meat Shield")
        if (
            meat_shield
            and allied_mob
            and meat_shield.can_trigger(boss, {"allied_mob": allied_mob})
        ):
            # Trigger Meat Shield redirection
            res = meat_shield.apply(boss, {"allied_mob": allied_mob, "use_grunt": True})
            if res.get("success"):
                # Mob takes the hit instead
                mob_armor = allied_mob.get_armor_dice()
                if mob_armor > 0:
                    armor_faces = [dice.roll_d6(rng) for _ in range(mob_armor)]
                    armor_succ = sum(1 for f in armor_faces if f >= 5)
                else:
                    armor_succ = 0

                unmitigated = max(0, threat.damage - armor_succ)
                if threat.is_aoe or threat.cleave:
                    allied_mob.take_aoe_damage(unmitigated)
                else:
                    allied_mob.take_single_target_damage(unmitigated)

                return ClatterResult(
                    evaded=True,  # Boss takes 0 damage
                    stat_successes=0,
                    armor_successes=armor_succ,
                    mitigated_damage=threat.damage,
                    damage_taken=0,
                    stat_faces=[],
                    armor_faces=[],
                )

        # 2. Determine Active Defense availability and pool
        can_react = boss.saved_reactions > 0 or boss.actions_left > 0
        stat_dice = 0
        diff = threat.difficulty

        if can_react:
            # Evaluate Dodge (Slink) vs Parry (Tough)
            slink_pool = max(0, boss.slink - boss.get_slink_bane())
            tough_pool = boss.tough if boss.can_parry() else 0

            # Condition penalties
            if boss.has_condition(Condition.WEAKENED):
                slink_pool = max(0, slink_pool - 1)
                tough_pool = max(0, tough_pool - 1)
            if boss.has_condition(Condition.RESTRAINED) or boss.has_condition(Condition.PRONE) or boss.has_condition(Condition.STAGGERED):
                slink_pool = max(0, slink_pool - 1)
                tough_pool = max(0, tough_pool - 1)

            # Zone Cover bonus to Dodge
            if topology:
                zone = topology.get_zone(boss.zone_id)
                if zone and zone.cover == CoverType.PARTIAL:
                    slink_pool += 1

            if slink_pool >= tough_pool and slink_pool > 0:
                stat_dice = slink_pool
                defense_type = "dodge"
            elif tough_pool > 0:
                stat_dice = tough_pool
                defense_type = "parry"
            else:
                stat_dice = 0
                defense_type = "none"

            # Consume 1 reaction/action
            if not boss.use_reaction():
                if boss.actions_left > 0:
                    boss.actions_left -= 1
        else:
            defense_type = "none"

        # 3. Passive Armor Dice
        armor_dice = boss.get_armor_dice()
        if "[Armor Piercing]" in threat.tags:
            armor_dice = max(0, armor_dice - 1)

        # 4. Resolve Clatter Roll
        clatter_res = resolve_clatter(
            threat_tn=threat.threat_tn,
            stat_dice=stat_dice,
            difficulty=diff,
            armor_dice=armor_dice,
            incoming_damage=threat.damage,
            can_dodge_or_parry=can_react,
            rng=rng,
        )

        # 5. Post-defense: Ankle Bite check on clean Dodge vs melee in same zone
        if (
            clatter_res.evaded
            and defense_type == "dodge"
            and attacker is not None
            and getattr(attacker, "zone_id", None) == boss.zone_id
        ):
            ankle_bite = boss.get_quirk("Ankle Bite")
            if ankle_bite and ankle_bite.can_trigger(
                boss, {"is_clean_dodge": True, "is_melee": True, "attacker": attacker}
            ):
                counter = ankle_bite.apply(
                    boss, {"is_clean_dodge": True, "is_melee": True, "attacker": attacker}
                )
                # Counter-attack can be executed by caller or engine

        # 6. Post-defense: Damage application & Ablative Gear Sacrifice
        if not clatter_res.evaded and clatter_res.damage_taken > 0:
            if allow_gear_sacrifice and clatter_res.damage_taken >= boss.grit:
                # Check Ablative Shield or Armor sacrifice
                if isinstance(boss.off_hand, Shield) and not getattr(boss.off_hand, "immune_to_piercing", False):
                    # Sacrifice shield!
                    boss.off_hand = None
                    clatter_res.mitigated_damage += clatter_res.damage_taken
                    clatter_res.damage_taken = 0
                elif boss.armor:
                    # Sacrifice armor!
                    boss.armor = None
                    clatter_res.mitigated_damage += clatter_res.damage_taken
                    clatter_res.damage_taken = 0
                else:
                    boss.take_damage(clatter_res.damage_taken)
            else:
                boss.take_damage(clatter_res.damage_taken)

        return clatter_res


class MobReactionResolver:
    """Resolves Mob reactions to incoming attacks (Scatter order vs Passive Armor)."""

    @staticmethod
    def resolve_mob_scatter(
        mob: PlayerMob,
        boss: GoblinBoss,
        threat: ThreatProfile,
        topology: Optional[TopologyGraph] = None,
        allow_gamble: bool = True,
        rng: Optional[random.Random] = None,
    ) -> Dict[str, Any]:
        """Resolve Mob Scatter reaction via Boss Mouth test vs modified Threat TN."""
        # Check resources
        has_reaction = boss.saved_reactions > 0 or boss.free_orders_left > 0 or boss.actions_left > 0
        if not has_reaction:
            return {"scattered": False, "reason": "no_actions_or_orders"}

        # Consume Boss resource (prefer free order, then saved reaction, then standard action)
        if boss.free_orders_left > 0:
            boss.free_orders_left -= 1
        elif boss.saved_reactions > 0:
            boss.saved_reactions -= 1
        elif boss.actions_left > 0:
            boss.actions_left -= 1

        # Modified TN: Threat TN + (Mob Size - 1)
        mod_tn = threat.threat_tn + max(0, mob.size - 1)

        # Same zone gives +1 automatic success
        same_zone = (boss.zone_id == mob.zone_id)
        auto_successes = 1 if same_zone else 0

        # Distance difficulty shift
        diff = Difficulty.NORMAL
        if topology and not same_zone:
            dist = topology.get_distance(boss.zone_id, mob.zone_id)
            if dist > boss.mouth + 1:
                return {"scattered": False, "reason": "out_of_range"}
            elif dist == boss.mouth + 1:
                diff = Difficulty.HARD

        dice_res = roll_dice(
            pool_size=boss.mouth,
            difficulty=diff,
            tn=max(1, mod_tn - auto_successes),
            allow_gamble=allow_gamble,
            rng=rng,
        )

        total_succ = dice_res.successes + auto_successes

        if total_succ >= mod_tn:
            # Clean Scatter: 0 damage, moves 1 zone into cover/adjacent
            if topology:
                adj = topology.get_adjacent(mob.zone_id)
                if adj:
                    mob.move_to(adj[0])
            return {
                "scattered": True,
                "damage_taken": 0,
                "gamble_fumble": False,
            }
        else:
            # Failed Scatter
            if dice_res.fumble:
                # TRAMPLE DISASTER: full damage + 1 AoE Trample damage to all dice + drops loot + Out of Control + Boss Staggered
                mob.take_aoe_damage(threat.damage + 1)
                mob.out_of_control = True
                if same_zone:
                    boss.add_condition(Condition.STAGGERED)
                return {
                    "scattered": False,
                    "damage_taken": threat.damage + 1,
                    "gamble_fumble": True,
                    "trample": True,
                }
            else:
                # Normal failure: takes attack damage mitigated by armor
                armor_dice = mob.get_armor_dice()
                armor_succ = sum(1 for f in [roll_d6(rng) for _ in range(armor_dice)] if f >= 5) if armor_dice > 0 else 0
                actual_dmg = max(0, threat.damage - armor_succ)
                if threat.is_aoe or threat.cleave:
                    mob.take_aoe_damage(actual_dmg)
                else:
                    mob.take_single_target_damage(actual_dmg)
                return {
                    "scattered": False,
                    "damage_taken": actual_dmg,
                    "gamble_fumble": False,
                }


class HazardResolver:
    """Resolves environmental hazard triggers and end-of-round fire propagation."""

    @staticmethod
    def resolve_entry_hazard(
        entity: BaseEntity,
        zone: Zone,
        rng: Optional[random.Random] = None,
    ) -> Dict[str, Any]:
        """Trigger hazard checks when an entity enters or starts turn in a zone."""
        results = {}

        # Slippery hazard
        if zone.has_trait(ZoneTraitType.SLIPPERY):
            if isinstance(entity, GoblinBoss):
                slink_pool = max(0, entity.slink - entity.get_slink_bane())
                res = roll_dice(slink_pool, zone.profile.difficulty, zone.profile.tn, rng=rng)
                if not res.is_success:
                    entity.add_condition(Condition.PRONE)
                    results["slippery_failed"] = True
            elif isinstance(entity, PlayerMob):
                res = roll_dice(2, zone.profile.difficulty, zone.profile.tn, rng=rng)
                if not res.is_success:
                    entity.add_condition(Condition.PRONE)
                    results["slippery_failed"] = True

        # Burning hazard
        if zone.has_trait(ZoneTraitType.BURNING) or zone.is_burning:
            if isinstance(entity, GoblinBoss):
                slink_pool = max(0, entity.slink - entity.get_slink_bane())
                res = roll_dice(slink_pool, zone.profile.difficulty, zone.profile.tn, rng=rng)
                if not res.is_success:
                    entity.take_damage(2)
                    results["burning_damage"] = 2
            elif isinstance(entity, PlayerMob):
                res = roll_dice(2, zone.profile.difficulty, zone.profile.tn, rng=rng)
                if not res.is_success:
                    entity.take_single_target_damage(2)
                    results["burning_damage"] = 2

        # Toxic hazard
        if zone.has_trait(ZoneTraitType.TOXIC):
            if isinstance(entity, GoblinBoss):
                res = roll_dice(entity.tough, zone.profile.difficulty, zone.profile.tn, rng=rng)
                if not res.is_success:
                    entity.add_condition(Condition.WEAKENED)
                    results["toxic_weakened"] = True
            elif isinstance(entity, PlayerMob):
                res = roll_dice(entity.size, zone.profile.difficulty, zone.profile.tn, rng=rng)
                if not res.is_success:
                    entity.add_condition(Condition.WEAKENED)
                    results["toxic_weakened"] = True

        return results

    @staticmethod
    def spread_fire(topology: TopologyGraph, rng: Optional[random.Random] = None) -> List[str]:
        """At End of Round, roll 1d6 for each burning zone; on 5-6, ignites adjacent flammable zones."""
        newly_ignited = []
        burning_zones = [z for z in topology.zones.values() if z.is_burning or z.has_trait(ZoneTraitType.BURNING)]

        for bz in burning_zones:
            for adj_id in topology.get_adjacent(bz.id):
                adj_zone = topology.get_zone(adj_id)
                if adj_zone and adj_zone.is_flammable and not adj_zone.is_burning:
                    roll = roll_d6(rng)
                    if roll >= 5:
                        adj_zone.add_trait(ZoneTrait(ZoneTraitType.BURNING))
                        adj_zone.is_burning = True
                        newly_ignited.append(adj_id)

        return newly_ignited


class MoraleResolver:
    """Resolves Swarm Terror checks and Beast morale triggers."""

    @staticmethod
    def check_swarm_terror(
        enemies: List[Enemy],
        allies: List[Union[GoblinBoss, PlayerMob]],
        trigger_reason: str = "50_percent_loss",
        rng: Optional[random.Random] = None,
    ) -> Dict[str, Any]:
        """Evaluate Swarm Terror Morale check for enemy group."""
        # Calculate Swarm Terror pool: surviving Mob Size + surviving PCs
        swarm_pool = 0
        for ally in allies:
            if ally.is_alive:
                if isinstance(ally, GoblinBoss):
                    swarm_pool += 1
                elif isinstance(ally, PlayerMob):
                    swarm_pool += ally.size

        if swarm_pool <= 0:
            return {"enemies_broken": False, "fled_count": 0}

        # Check each enemy group
        broken_enemies = []
        for enemy in enemies:
            if not enemy.is_alive or enemy.has_fled:
                continue

            # Check Ancestry traits
            morale_immune = False
            for trait in enemy.traits:
                if isinstance(trait, EnemyTrait) and trait.name == "Undead Ancestry":
                    morale_immune = True
                    break

            if morale_immune:
                continue

            # Roll Swarm Terror pool vs Enemy Morale TN on 5+
            res = roll_dice(
                pool_size=swarm_pool,
                difficulty=Difficulty.NORMAL,
                tn=enemy.morale_tn,
                allow_gamble=False,
                rng=rng,
            )

            if res.is_success:
                enemy.has_fled = True
                enemy.is_alive = False
                broken_enemies.append(enemy.id)

        return {
            "enemies_broken": len(broken_enemies) > 0,
            "broken_enemy_ids": broken_enemies,
            "fled_count": len(broken_enemies),
        }
