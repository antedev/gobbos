"""Tactical Combat AI heuristics for Goblin Bosses, Player Mobs, and Deterministic Enemies."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Any, Dict, List, Optional, Tuple, Union

from combat_sim.core.dice import roll_d6
from combat_sim.core.types import ActionType, Condition, CoverType, ThreatProfile
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
from combat_sim.domain.equipment import Weapon
from combat_sim.domain.topology import TopologyGraph
from combat_sim.engine.resolver import AttackResolver, AttackResult, ClatterResolver


class BossAI:
    """Tactical AI heuristic for player-controlled Goblin Bosses."""

    @staticmethod
    def execute_turn(
        boss: GoblinBoss,
        allies: List[Union[GoblinBoss, PlayerMob]],
        enemies: List[Enemy],
        topology: TopologyGraph,
        rng: Optional[random.Random] = None,
    ) -> List[Dict[str, Any]]:
        """Execute a full tactical turn for a Goblin Boss within their action budget."""
        actions_log: List[Dict[str, Any]] = []

        if not boss.is_alive or boss.has_condition(Condition.STUNNED):
            return actions_log

        # 1. Action Budgeting: Reserve 1 Reaction for defensive Clatter/Scatter if threatened
        enemies_alive = [e for e in enemies if e.is_alive and not e.has_fled]
        enemies_in_zone = [e for e in enemies_alive if e.zone_id == boss.zone_id]

        if (enemies_in_zone or len(enemies_alive) > 0) and boss.actions_left > 1 and boss.saved_reactions == 0:
            boss.save_reaction()
            actions_log.append({"action": "Save Reaction", "actor": boss.name, "saved_reactions": boss.saved_reactions})

        # 2. Free Order phase: Command an allied Mob if present
        if boss.free_orders_left > 0:
            allied_mobs = [
                m for m in allies
                if isinstance(m, PlayerMob) and m.is_alive and not m.is_ordered and not m.out_of_control
            ]
            if allied_mobs:
                target_mob = allied_mobs[0]
                boss.free_orders_left -= 1
                target_mob.is_ordered = True
                actions_log.append({
                    "action": "Free Order",
                    "actor": boss.name,
                    "target_mob": target_mob.name,
                })
                # Execute Mob turn
                mob_acts = MobAI.execute_ordered_mob_turn(target_mob, boss, allies, enemies, topology, rng=rng)
                actions_log.extend(mob_acts)

        # 3. Spend remaining Standard Actions
        while boss.actions_left > 0:
            enemies_alive = [e for e in enemies if e.is_alive and not e.has_fled]
            if not enemies_alive:
                break

            enemies_in_zone = [e for e in enemies_alive if e.zone_id == boss.zone_id]

            if enemies_in_zone:
                # Target priority: Standard (easy 1-hit kill), then lowest Wounds Elite
                target = min(
                    enemies_in_zone,
                    key=lambda e: (0 if isinstance(e, StandardEnemy) else 1, getattr(e, "wounds", 10)),
                )
                boss.actions_left -= 1
                res = AttackResolver.resolve_melee_attack(
                    attacker=boss,
                    target=target,
                    weapon=boss.main_hand,
                    topology=topology,
                    rng=rng,
                )
                actions_log.append({
                    "action": "Melee Attack",
                    "actor": boss.name,
                    "target": target.name,
                    "hit": res.hit,
                    "successes": res.successes,
                    "wounds_dealt": res.wounds_dealt,
                    "staggered": res.staggered,
                    "killed": res.killed,
                    "faces": res.faces,
                    "bonus_faces": res.bonus_faces,
                    "pool_size": res.pool_size,
                    "is_critical": res.is_critical,
                    "fumble": res.fumble,
                    "gambled": res.gambled,
                    "remaining": res.target_remaining,
                })
            else:
                # Check ranged weapon capability
                has_ranged = boss.main_hand and boss.main_hand.is_ranged
                if has_ranged:
                    # Find nearest enemy in range
                    ranged_targets = [
                        e for e in enemies_alive
                        if 0 < topology.get_distance(boss.zone_id, e.zone_id) <= boss.main_hand.range_zones
                    ]
                    if ranged_targets:
                        target = ranged_targets[0]
                        boss.actions_left -= 1
                        res = AttackResolver.resolve_ranged_attack(
                            attacker=boss,
                            target=target,
                            weapon=boss.main_hand,
                            topology=topology,
                            rng=rng,
                        )
                        actions_log.append({
                            "action": "Ranged Attack",
                            "actor": boss.name,
                            "target": target.name,
                            "hit": res.hit,
                            "successes": res.successes,
                            "wounds_dealt": res.wounds_dealt,
                            "killed": res.killed,
                            "faces": res.faces,
                            "bonus_faces": res.bonus_faces,
                            "pool_size": res.pool_size,
                            "is_critical": res.is_critical,
                            "fumble": res.fumble,
                            "gambled": res.gambled,
                            "remaining": res.target_remaining,
                        })
                        continue

                # Move toward nearest enemy zone
                nearest_enemy = min(enemies_alive, key=lambda e: topology.get_distance(boss.zone_id, e.zone_id))
                path = topology.find_path(boss.zone_id, nearest_enemy.zone_id)
                if len(path) > 1:
                    next_zone = path[1]
                    boss.actions_left -= 1
                    boss.move_to(next_zone)
                    actions_log.append({
                        "action": "Move",
                        "actor": boss.name,
                        "from_zone": path[0],
                        "to_zone": next_zone,
                    })
                else:
                    boss.actions_left -= 1

        return actions_log


class MobAI:
    """Tactical AI heuristic for Player Mobs and un-ordered behavior."""

    @staticmethod
    def execute_ordered_mob_turn(
        mob: PlayerMob,
        boss: GoblinBoss,
        allies: List[Union[GoblinBoss, PlayerMob]],
        enemies: List[Enemy],
        topology: TopologyGraph,
        rng: Optional[random.Random] = None,
    ) -> List[Dict[str, Any]]:
        """Execute up to 2 ordered actions obeying the Mob Boredom rule."""
        actions_log: List[Dict[str, Any]] = []
        if not mob.is_alive or mob.size <= 0:
            return actions_log

        mob.is_ordered = True
        actions_taken_types: List[ActionType] = []

        while mob.actions_left > 0:
            enemies_alive = [e for e in enemies if e.is_alive and not e.has_fled]
            if not enemies_alive:
                break

            enemies_in_zone = [e for e in enemies_alive if e.zone_id == mob.zone_id]

            if enemies_in_zone and ActionType.MELEE_ATTACK not in actions_taken_types:
                # Melee attack target in zone
                target = enemies_in_zone[0]
                mob.actions_left -= 1
                actions_taken_types.append(ActionType.MELEE_ATTACK)

                res = AttackResolver.resolve_melee_attack(
                    attacker=mob,
                    target=target,
                    weapon=None,
                    topology=topology,
                    rng=rng,
                )
                actions_log.append({
                    "action": "Mob Melee Attack",
                    "actor": mob.name,
                    "target": target.name,
                    "hit": res.hit,
                    "successes": res.successes,
                    "damage_dealt": res.damage_dealt,
                    "killed": res.killed,
                    "faces": res.faces,
                    "bonus_faces": res.bonus_faces,
                    "pool_size": res.pool_size,
                    "is_critical": res.is_critical,
                    "fumble": res.fumble,
                    "gambled": res.gambled,
                    "remaining": res.target_remaining,
                })
            else:
                # Move toward nearest enemy (Boredom rule explicitly allows Move twice)
                nearest_enemy = min(enemies_alive, key=lambda e: topology.get_distance(mob.zone_id, e.zone_id))
                path = topology.find_path(mob.zone_id, nearest_enemy.zone_id)
                if len(path) > 1:
                    next_zone = path[1]
                    mob.actions_left -= 1
                    actions_taken_types.append(ActionType.MOVE)
                    mob.move_to(next_zone)
                    actions_log.append({
                        "action": "Mob Move",
                        "actor": mob.name,
                        "to_zone": next_zone,
                    })
                else:
                    mob.actions_left -= 1

        return actions_log

    @staticmethod
    def execute_unordered_mob(
        mob: PlayerMob,
        topology: TopologyGraph,
        rng: Optional[random.Random] = None,
    ) -> Dict[str, Any]:
        """Resolve un-ordered mob behavior (Loitering 1 action/1 saved vs Out of Control 2 actions/0 saved)."""
        if not mob.is_alive or mob.size <= 0:
            return {"action": "dead"}

        if not mob.out_of_control:
            # Loitering Table (d6)
            roll = roll_d6(rng)
            mob.actions_left = 0
            mob.saved_reactions = 1  # Saves 1 action for defense

            if roll == 1:
                desc = "Bickering and arguing over shiny rocks."
            elif roll == 2:
                desc = "Inspecting gear and picking noses."
            elif roll == 3:
                desc = "Snatching loose scrap and junk."
            elif roll == 4:
                # Wander 1 zone
                adj = topology.get_adjacent(mob.zone_id)
                if adj:
                    mob.move_to(adj[0])
                desc = f"Wandered into adjacent zone {mob.zone_id}."
            elif roll == 5:
                desc = "Snooping around for hidden secrets."
            else:
                desc = "Taunting and yelling insults across the battlefield."

            return {
                "state": "Loitering",
                "roll": roll,
                "description": desc,
                "saved_reactions": 1,
            }
        else:
            # Out of Control Table (d6)
            roll = roll_d6(rng)
            mob.actions_left = 0
            mob.saved_reactions = 0  # 0 saved actions

            if roll in (1, 2):
                # Panic / Flee
                adj = topology.get_adjacent(mob.zone_id)
                if adj:
                    mob.move_to(adj[0])
                desc = "Panicking and fleeing wildly!"
            elif roll in (3, 4):
                # Loot / Trash
                desc = "Trashing current zone looking for snacks."
            else:
                # Frenzy attack nearest entity
                desc = "Frenzy swarm attack against nearest entity!"

            return {
                "state": "Out of Control",
                "roll": roll,
                "description": desc,
                "saved_reactions": 0,
            }


class EnemyAI:
    """Tactical AI heuristic for deterministic enemies with Swarm combining."""

    @staticmethod
    def execute_enemy_turns(
        enemies: List[Enemy],
        allies: List[Union[GoblinBoss, PlayerMob]],
        topology: TopologyGraph,
        rng: Optional[random.Random] = None,
    ) -> List[Dict[str, Any]]:
        """Execute all active enemy turns with swarm combining on Bosses and Mobs."""
        actions_log: List[Dict[str, Any]] = []

        living_allies = [a for a in allies if a.is_alive]
        if not living_allies:
            return actions_log

        # 1. Movement phase: Each enemy not in a zone with living allies moves 1 step toward nearest ally
        for enemy in enemies:
            if not enemy.is_alive or enemy.has_fled:
                continue

            allies_in_zone = [a for a in living_allies if a.zone_id == enemy.zone_id and a.is_alive]
            if not allies_in_zone:
                nearest_ally = min(living_allies, key=lambda a: topology.get_distance(enemy.zone_id, a.zone_id))
                path = topology.find_path(enemy.zone_id, nearest_ally.zone_id)
                if len(path) > 1:
                    next_zone = path[1]
                    enemy.move_to(next_zone)
                    actions_log.append({
                        "action": "Enemy Move",
                        "actor": enemy.name,
                        "to_zone": next_zone,
                    })

        # 2. Group Attack combining phase by Zone
        # Identify all distinct zones with active enemies
        active_zones = {e.zone_id for e in enemies if e.is_alive and not e.has_fled}

        for zone_id in sorted(active_zones):
            # Living enemies in this zone
            zone_enemies = [e for e in enemies if e.is_alive and not e.has_fled and e.zone_id == zone_id]
            if not zone_enemies:
                continue

            # Living allies in this zone
            zone_allies = [a for a in allies if a.is_alive and a.zone_id == zone_id]
            if not zone_allies:
                continue

            zone_bosses = [a for a in zone_allies if isinstance(a, GoblinBoss) and a.is_alive]
            zone_mobs = [a for a in zone_allies if isinstance(a, PlayerMob) and a.is_alive]

            available_enemies = list(zone_enemies)

            # Attack Goblin Bosses first (up to 3 attackers per Boss combined into a single Group Attack)
            for boss in zone_bosses:
                if not boss.is_alive or not available_enemies:
                    break

                # Combine up to 3 attackers on this Boss
                swarm_count = min(3, len(available_enemies))
                attackers = available_enemies[:swarm_count]
                available_enemies = available_enemies[swarm_count:]

                primary_enemy = attackers[0]
                attack = primary_enemy.attacks[0] if primary_enemy.attacks else ThreatAttack(name="Strike", damage=1)
                base_threat = attack.threat_profile

                # Handle EnemyMob base damage
                base_dmg = primary_enemy.get_mob_damage() if isinstance(primary_enemy, EnemyMob) else base_threat.damage
                combined_dmg = base_dmg + (len(attackers) - 1)

                threat = ThreatProfile(
                    threat_stat=base_threat.threat_stat,
                    difficulty=base_threat.difficulty,
                    threat_tn=base_threat.threat_tn,
                    damage=combined_dmg,
                    tags=base_threat.tags,
                    impact_size=base_threat.impact_size,
                    is_aoe=base_threat.is_aoe,
                    cleave=base_threat.cleave,
                    range_zones=base_threat.range_zones,
                )

                allied_mob_in_zone = next((m for m in zone_mobs if m.is_alive), None)

                clatter = ClatterResolver.resolve_boss_defense(
                    boss=boss,
                    attacker=primary_enemy,
                    threat=threat,
                    allied_mob=allied_mob_in_zone,
                    topology=topology,
                    rng=rng,
                )

                actor_name = primary_enemy.name if len(attackers) == 1 else f"Group Attack ({', '.join(e.name for e in attackers)})"
                actions_log.append({
                    "action": "Group Attack on Boss" if len(attackers) > 1 else "Enemy Attack on Boss",
                    "actor": actor_name,
                    "target": boss.name,
                    "attacker_count": len(attackers),
                    "damage": combined_dmg,
                    "evaded": clatter.evaded,
                    "damage_taken": clatter.damage_taken,
                    "boss_grit": boss.grit,
                })

            # Attack Player Mobs next (all remaining available enemies combine into a Group Attack, no limit)
            for mob in zone_mobs:
                if not mob.is_alive or not available_enemies:
                    break

                attackers = list(available_enemies)
                available_enemies.clear()

                primary_enemy = attackers[0]
                attack = primary_enemy.attacks[0] if primary_enemy.attacks else ThreatAttack(name="Strike", damage=1)
                base_threat = attack.threat_profile

                base_dmg = primary_enemy.get_mob_damage() if isinstance(primary_enemy, EnemyMob) else base_threat.damage
                combined_dmg = base_dmg + (len(attackers) - 1)

                threat = ThreatProfile(
                    threat_stat=base_threat.threat_stat,
                    difficulty=base_threat.difficulty,
                    threat_tn=base_threat.threat_tn,
                    damage=combined_dmg,
                    tags=base_threat.tags,
                    impact_size=base_threat.impact_size,
                    is_aoe=base_threat.is_aoe,
                    cleave=base_threat.cleave,
                    range_zones=base_threat.range_zones,
                )

                if threat.is_aoe or threat.cleave:
                    dealt = mob.take_aoe_damage(combined_dmg)
                else:
                    dealt = mob.take_single_target_damage(combined_dmg)

                actor_name = primary_enemy.name if len(attackers) == 1 else f"Group Attack ({', '.join(e.name for e in attackers)})"
                actions_log.append({
                    "action": "Group Attack on Mob" if len(attackers) > 1 else "Enemy Attack on Mob",
                    "actor": actor_name,
                    "target": mob.name,
                    "attacker_count": len(attackers),
                    "damage_dealt": dealt,
                    "mob_size": mob.size,
                })

        return actions_log
