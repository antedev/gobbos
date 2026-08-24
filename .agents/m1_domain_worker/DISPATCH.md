## 2026-08-23T21:27:25Z
You are the Implementation Worker for Milestone 1: Tactical Domain & Models.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m1_domain_worker\

You MUST read the authoritative specifications first:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_gear_0\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_rules_0\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\explorer_scenarios_0\handoff.md

Your mission:
Implement Milestone 1 in `05_System_Tools/combat_sim`:
1. `05_System_Tools/combat_sim/pyproject.toml` and package configuration.
2. `combat_sim/__init__.py`
3. `combat_sim/core/__init__.py` and `combat_sim/core/types.py`:
   - All Enums: `Difficulty` (EASY=4, NORMAL=5, HARD=6), `Condition` (WEAKENED, RESTRAINED, DUMB, SILENCED, BLINDED, TERRIFIED, STUNNED, PRONE, STAGGERED), `Ancestry` (BEAST, HUMANOID, UNDEAD, MONSTROSITY, FIEND), `EnemyScale` (STANDARD, ELITE, MOB), `CoverType` (NONE, PARTIAL, FULL), `ActionType` (MOVE, MELEE_ATTACK, RANGED_ATTACK, PLUNDER, MANIPULATE, ORDER, DODGE, PARRY, SCATTER), `ZoneTraitType` (SLIPPERY, BURNING, TOXIC, NARROW, PILLARS, RUBBLE, SHORING).
4. `combat_sim/domain/__init__.py`
5. `combat_sim/domain/entities.py`:
   - `BaseEntity`, `GoblinBoss` (Tough, Slink, Mouth, Brains, Grunt, Grit, Loadout, Actions budget), `PlayerMob` (Size, health_dice List[int], armor rating, ordered/out of control), `Enemy` (Base), `StandardEnemy`, `EliteEnemy` (Wounds, max_wounds, Defence TN), `EnemyMob` (Size, health_dice List[int], base damage).
6. `combat_sim/domain/equipment.py`:
   - `Weapon` (handedness, bulk, impact_size, traits like BASHING, CLEAVE, PIERCING, REACH, range_zones), `Armor` (bulk, armor_dice, slink_bane), `Shield` (bulk, armor_dice, enables_parry), `Consumable` / `Explosive` (area threat profiles, damage, impact_size, tags).
   - Standard Equipment Catalogue factory functions for all weapons, armor, shields, and explosives.
7. `combat_sim/domain/quirks.py`:
   - `Quirk` base class, `MeatShield`, `AnkleBite`, `PushLuck` / `SecondWind`, `Twist` modifiers.
8. `combat_sim/domain/traits.py`:
   - `EnemyTrait` base class, `ParryingBuckler`, `ThickBlubber`, `Bastion`, `SteamVent`, `VoraciousRegrowth`, `DryBones`, Ancestry trait handlers.
9. `combat_sim/domain/topology.py`:
   - `Zone`, `ZoneProfile`, `ZoneTrait`, `TopologyGraph` (graph traversal, BFS distance, adjacency, pathfinding).

Exclusive write ownership: You exclusively own files in `05_System_Tools/combat_sim/combat_sim/core/` and `05_System_Tools/combat_sim/combat_sim/domain/` and `05_System_Tools/combat_sim/pyproject.toml`.
