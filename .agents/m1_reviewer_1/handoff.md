# Milestone 1: Tactical Domain & Models - Reviewer 1 Handoff Report

**Reviewer**: Reviewer 1 (`m1_reviewer_1`)  
**Roles**: Reviewer, Adversarial Critic  
**Date**: 2026-08-23T21:34:30Z  
**Verdict**: **`APPROVE`**  
**Working Directory**: `c:\Users\ante\Documents\github\gobbos\.agents\m1_reviewer_1`

---

## 1. Observation

A comprehensive code audit, static structural analysis, and rulebook cross-examination of the Milestone 1 codebase in `05_System_Tools/combat_sim/` were conducted against `ORIGINAL_REQUEST.md`, `PROJECT.md`, `m1_domain_worker/handoff.md`, and official Gobbos rules in `02_PROD_Core_Rules/` and `01_STAGE_Drafts/`.

### Core Observations by Component:

1. **Core Enums & Types (`05_System_Tools/combat_sim/combat_sim/core/types.py`)**:
   - `Difficulty(IntEnum)` (lines 10–26): Implements `EASY = 4`, `NORMAL = 5`, `HARD = 6`, method `meets_threshold(face: int) -> bool` returning `face >= self.value`, and property `label` returning `"4+"`, `"5+"`, `"6"` (strictly adhering to the Gobbos rulebook standard of omitting `+` on 6).
   - `Condition(str, Enum)` (lines 28–39): Contains all 9 tactical conditions (`WEAKENED`, `RESTRAINED`, `DUMB`, `SILENCED`, `BLINDED`, `TERRIFIED`, `STUNNED`, `PRONE`, `STAGGERED`).
   - `Ancestry(str, Enum)` (lines 41–48): Contains `BEAST`, `HUMANOID`, `UNDEAD`, `MONSTROSITY`, `FIEND`.
   - `EnemyScale(str, Enum)` (lines 50–55): Contains `STANDARD`, `ELITE`, `MOB`.
   - `CoverType(str, Enum)` (lines 57–62): Contains `NONE`, `PARTIAL`, `FULL`.
   - `ActionType(str, Enum)` (lines 64–75): Contains `MOVE`, `MELEE_ATTACK`, `RANGED_ATTACK`, `PLUNDER`, `MANIPULATE`, `ORDER`, `DODGE`, `PARRY`, `SCATTER`.
   - `ZoneTraitType(str, Enum)` (lines 77–86): Contains `SLIPPERY`, `BURNING`, `TOXIC`, `NARROW`, `PILLARS`, `RUBBLE`, `SHORING`.
   - `WeaponHandedness(IntEnum)` (lines 88–91): Contains `ONE_HAND = 1`, `TWO_HAND = 2`.
   - `WeaponTrait(str, Enum)` (lines 94–109): Contains `BASHING`, `CLEAVE`, `PIERCING`, `CUTTING`, `REACH`, `VERSATILE`, `ARMOR_PIERCING`, `HEAVY`, `CRUSHING`, `CONCEALABLE`, `FAST_THROW`, `RAPID_SHOT`, `CLOCKWORK`.
   - `Tag` (lines 111–131): Contains all master tags (`[Fire]`, `[Explosive]`, `[Acidic]`, `[Shock]`, `[Toxic]`, `[Loud]`, `[Tasty]`, `[Angelic]`, `[Light]`, `[Purified]`, `[Bleeding]`, `[Gaseous]`, `[Slick]`, `[Dark]`, `[Hardened]`, `[Spiky]`, `[Terrifying]`, `[Regenerating]`).
   - `ThreatProfile` (lines 133–152): Encapsulates deterministic incoming threat parameters (`threat_stat`, `difficulty`, `threat_tn`, `damage`, `tags`, `impact_size`, `is_aoe`, `cleave`, `range_zones`) and formatted `shorthand`.

2. **Abstract Topologies & Graph Routing (`05_System_Tools/combat_sim/combat_sim/domain/topology.py`)**:
   - `ZoneProfile` (lines 12–23): Tracks `difficulty`, `tn`, `description`, and `shorthand` (e.g. `'5+/2'`).
   - `ZoneTrait` (lines 25–32): Tracks `trait_type`, `description`, `is_active`, and arbitrary `metadata`.
   - `Zone` (lines 34–86): Tracks `id`, `name`, `profile`, `cover`, `traits`, `loot_bulk`, `is_flammable`, `is_burning`, `is_blocked`, and `directional_cover` mapping. Methods `has_trait`, `get_trait`, `add_trait` (auto-syncing `is_burning`), `remove_trait`, `get_cover_from`, and `set_directional_cover`.
   - `TopologyGraph` (lines 87–190): Fully implemented graph structure with BFS algorithms:
     - `get_distance(z1, z2)` (lines 126–150): BFS shortest distance returning zone hops (0 for same zone, -1 for unreachable).
     - `find_path(z1, z2)` (lines 151–171): BFS shortest path returning ordered zone IDs list.
     - `get_zones_within_distance(zone_id, max_dist)` (lines 173–189): BFS radius exploration.
     - `connect` / `disconnect` (lines 99–113): Dynamic adjacency management for interactive terrain collapses (e.g., Shoring).

3. **Equipment & Catalogue Factories (`05_System_Tools/combat_sim/combat_sim/domain/equipment.py`)**:
   - Class hierarchy: `Equipment(ABC)` -> `Weapon`, `Armor`, `Shield`, `Consumable`.
   - Fumble break threshold logic: `Equipment.roll_breaks(roll)` (lines 26–30) correctly checks `break_roll <= break_threshold` (T1: $\le 4$, T2: $\le 3$, T3: $\le 2$, T4: $\le 1$, T5: 0).
   - Impact Size calculation: `Weapon.get_effective_impact_size(wielder_size)` (lines 62–65) correctly computes `max(0, wielder_size + impact_size_modifier)` with `+1` for `Heavy` and `+2` for `Crushing`.
   - Armor & Shields:
     - Light Armor (`create_light_armor`, line 308): `+1d` Armor Die, `0` Slink Bane.
     - Medium Armor (`create_medium_armor`, line 321): `+2d` Armor Dice, `1` Slink Bane (`-1d`).
     - Heavy Armor (`create_heavy_armor`, line 334): `+3d` Armor Dice, `2` Slink Bane (`-2d`), `cannot_swim=True`.
     - Runed Carapace (`create_runed_carapace`, line 347): `+3d` Armor Dice, `1` Slink Bane.
     - Standard Shield (`create_pot_lid_shield`, line 360): `+1d` Armor Die, `enables_parry=True`.
     - Tower Pavise (`create_tower_pavise`, line 379): `+2d` Armor Dice, `enables_parry=True`, `halves_movement=True`.
     - Godstone Aegis (`create_godstone_aegis`, line 393): `+2d` Armor Dice, `immune_to_piercing=True`, `break_threshold=0`.
   - Consumables: Full implementation of Spark Bombs, Fire Flasks/Molotovs, Smoke Pots, Demolition Powder Kegs, Siege Mortar Shells, and Sol-Quartz Cores with Area Threat profiles.

4. **Boss Quirks & Modular Twists (`05_System_Tools/combat_sim/combat_sim/domain/quirks.py`)**:
   - `TwistModifier` (lines 10–52): Modular modifiers (`Spiteful`, `Loud`, `Efficient`, `Reflexive`).
   - `Quirk(ABC)` (lines 54–92): Encapsulates `grunt_cost`, `action_cost`, `is_passive`, `twists`, `get_effective_grunt_cost()` (reduces Grunt cost by 1 per Efficient twist, min 0), and `is_free_action()`.
   - Quirk implementations:
     - `MeatShield` (lines 94–146): Validates living allied Mob in same zone; spends Grunt or saved Reaction; redirects attack.
     - `AnkleBite` (lines 148–176): Passive trigger on clean Dodge vs melee attacker in same zone; grants immediate free melee counter-attack at `+1` Success.
     - `PushLuck` / `SecondWind` (lines 178–215): Spends 1 Grunt; rerolls all non-1 dice while keeping 1s locked.
     - `OpportunityStrike` / `SlipperyQuirk` (lines 217–239), `SwallowLoot` (lines 241–257), `Butcher` (lines 259–278).

5. **Enemy Traits & Ancestries (`05_System_Tools/combat_sim/combat_sim/domain/traits.py`)**:
   - `EnemyTrait(ABC)` (lines 18–64): Complete lifecycle hooks (`on_round_start`, `on_round_end`, `on_incoming_attack_modify_difficulty`, `on_incoming_attack_modify_pool`, `on_incoming_damage_modify`, `on_wound_taken`, `on_morale_check_trigger`).
   - `ParryingBuckler` (lines 70–89): Sets 1st melee attack received in each round to `Difficulty.HARD` (6); subsequent melee attacks resolve at `Difficulty.NORMAL` (5+); resets on `on_round_start`.
   - `ThickBlubber` (lines 91–104): Imposes `-1d` Bane on attacker dice pool unless attack carries `Tag.FIRE` (`"[Fire]"`).
   - `PlateBastion` / `Bastion` (lines 106–135): Subtracts 1 from incoming damage unless attack has `WeaponTrait.PIERCING` or elemental tags (`[Fire]`, `[Acidic]`, `[Shock]`).
   - `PressurizedSteamVent` / `SteamVent` (lines 137–162): On taking 1+ Wounds, returns steam vent burst hazard event with `Difficulty.NORMAL` (5+), TN 2, 2 Fire damage in zone.
   - `VoraciousRegrowth` (lines 164–177): At `on_round_start`, heals 1 lost Wound if `last_round_fire_or_acid_damage` is False.
   - `DryBones` (lines 179–198): Grants `+1d` Boon on Bashing/Crushing weapons; imposes `-1d` Bane on Piercing, Cutting, and ranged bow attacks.
   - Ancestry traits: `BeastAncestryTrait`, `UndeadAncestryTrait`, `MonstrosityAncestryTrait`, `FiendAncestryTrait`, `HumanoidAncestryTrait`.

6. **Combat Entities (`05_System_Tools/combat_sim/combat_sim/domain/entities.py`)**:
   - `BaseEntity(ABC)` (lines 24–93): Tracks conditions set, alive state, zone location, and condition helpers (`is_staggered`, `is_prone`, `is_weakened`, etc.).
   - `GoblinBoss` (lines 94–263):
     - `__post_init__` (lines 119–129): Auto-calculates `max_grit = 4 + (2 * tough)`.
     - Action budget: 3 Standard Actions, 1 Free Order, saved reactions tracking.
     - Defence accessors: `get_armor_dice()` sums armor and shield dice; `get_slink_bane()` gets armor bane; `can_parry()` evaluates shield parry enablement.
     - Derived stats: `get_movement_speed()` (Slink $\le 1$: 2, $\le 3$: 3, $4$: 4, $5$: 5, halved by tower pavise, reduced if over-laden), `get_carry_capacity()` ($4 + 2 \times \text{Tough} + \text{Swallow Loot}$).
   - `PlayerMob` (lines 264–353):
     - Symmetrical Dice-HP array (`health_dice: List[int]`, initialized to `[6] * size`).
     - Single-target damage (`take_single_target_damage`, lines 290–314): decrements active die (`health_dice[0]`), pops exhausted dice ($<1$), and spills remainder into subsequent dice.
     - AoE damage (`take_aoe_damage`, lines 315–334): subtracts damage simultaneously from every die in the pool (`d - dmg`), filtering out dice $\le 0$.
     - Dynamic `size = len(health_dice)` synchronization.
   - `StandardEnemy` (lines 439–453):
     - `take_hit(successes, impact_size)`: One-hit kill on `successes >= eff_def`; inflicts `Condition.STAGGERED` if `successes >= 1 and impact_size >= size`.
   - `EliteEnemy` (lines 455–522):
     - `take_hit(successes, impact_size, tags)`: Overkill wound conversion via `wounds_dealt = successes // eff_def` (where `eff_def` is `max(1, defence_tn - 1)` if staggered); inflicts `Condition.STAGGERED` if `successes >= 1 and impact_size >= size`; checks fire/acid tags for Regrowth suppression; executes trait reactions (`on_wound_taken`).
   - `EnemyMob` (lines 523–582):
     - Deterministic damage scaling via `get_mob_damage()` returning `base_damage + max(0, size - 1)`.

7. **Test Suites Inspection (`05_System_Tools/combat_sim/tests/`)**:
   - `test_domain_m1.py` (673 lines): 19 exhaustive tests across all enums, BFS topology routing, equipment catalogue, quirks & twists, traits & ancestries, and entity state lifecycles.
   - `test_equipment_armor.py` (299 lines), `test_quirks.py` (220 lines), `test_enemy_traits.py` (285 lines), `test_mob_health.py` (149 lines), `test_scenarios.py` (418 lines), `test_dice.py` (280 lines), `test_e2e.py` (286 lines), `test_performance.py` (174 lines).

---

## 2. Logic Chain

1. **Interface Contract Verification (PROJECT.md & ORIGINAL_REQUEST.md -> types.py & domain/)**:
   - *Observation 1*: `PROJECT.md` lines 84–96 specify entity attributes, topology methods, equipment traits, and quirks.
   - *Logic*: All specified signatures (`GoblinBoss`, `PlayerMob`, `Enemy`, `TopologyGraph.get_distance`, `TopologyGraph.get_adjacent`, `Weapon`, `Armor`, `Shield`, `Consumable`) match the contracts exactly.

2. **Core Mathematical Accuracy (Rulebook -> Domain Models)**:
   - *Observation 2*: `GoblinBoss.__post_init__` implements `calculated_grit = 4 + (2 * self.tough)`.
   - *Logic*: For Tough 1, Grit = 6; for Tough 2, Grit = 8; for Tough 3, Grit = 10. This matches the specified Grit formula.
   - *Observation 3*: `EliteEnemy.take_hit` implements `wounds_dealt = successes // eff_def if successes >= eff_def else 0`.
   - *Logic*: Against Defence TN 2, 0–1 successes deal 0 Wounds, 2–3 successes deal 1 Wound, 4–5 successes deal 2 Wounds (Overkill), 6+ successes deal 3 Wounds. This directly reflects the Gobbos Overkill rule ($\lfloor \text{Successes} / \text{Defence TN} \rfloor$).
   - *Observation 4*: `PlayerMob.take_single_target_damage` decrements the active die and pops it upon reaching 0, spilling remainder to the next die; `take_aoe_damage` subtracts damage simultaneously across all dice.
   - *Logic*: Single-target attacks degrade the mob sequentially die-by-die, while AoE/Cleave attacks simultaneously hollow out the entire swarm pool, matching `STAGE 13_Goblin_mob.md`.

3. **Adversarial Stress-Testing & Integrity Verification**:
   - *Observation 5*: Checked for hardcoded return values, dummy mocks, or facades in the domain modules (`combat_sim/domain/*.py` and `combat_sim/core/types.py`).
   - *Logic*: All classes and methods contain authentic, general-purpose logic. `TopologyGraph` implements standard BFS traversal with queue and visited sets. `GoblinBoss`, `PlayerMob`, and `EliteEnemy` maintain genuine state mutations. No integrity violations or self-certifying stubs were found.
   - *Observation 6*: Tested edge cases:
     - Zero/negative damage inputs in `take_damage`, `take_single_target_damage`, `take_aoe_damage` return 0 with zero state corruption.
     - Massive damage exceeding total mob health terminates cleanly when `health_dice` empties, setting `size = 0` and `is_alive = False`.
     - 0 successes against Standard/Elite enemies do not inflict Stagger (requires $\ge 1$ success).
     - Staggered Elite enemies reduce effective Defence TN by 1 (minimum 1), properly increasing overkill wound yields.
     - Disconnected zones in `TopologyGraph` return distance `-1` and empty path `[]`.

---

## 3. Caveats

- **Milestone 2 Combat Loop Orchestration**: The domain models provide all prerequisite state, accessors, hooks, and damage arithmetic; full combat turn loop orchestration (5-phase round flow, dice roller integration, Clatter roll resolution, AI decision heuristics) will be orchestrated in Milestone 2.
- **Scenario Definitions Assembly**: Pre-built scenarios (Street Skirmish, The Mauler's Den, Tomb of the Highwayman) are verified in tests and domain assemblies, and will be registered in `combat_sim.scenarios` during Milestone 5.

---

## 4. Conclusion

Milestone 1 (Tactical Domain & Models) is **fully implemented, rules-accurate, structurally robust, and completely free of integrity violations**. All enums, models, equipment factories, quirks, enemy traits, ancestries, and graph topology models meet or exceed the requirements of `ORIGINAL_REQUEST.md` and `PROJECT.md`.

**Explicit Verdict**: **`APPROVE`**

---

## 5. Verification Method

To independently verify Milestone 1 implementation:

1. **Python Package Import Inspection**:
   ```python
   import combat_sim.core as core
   import combat_sim.domain as domain
   print("Core Types:", [c.__name__ for c in [core.Difficulty, core.Condition, core.Ancestry, core.ThreatProfile]])
   print("Domain Factories:", len(domain.__all__))
   ```

2. **Execute M1 Verification Test Suite**:
   ```bash
   python 05_System_Tools/combat_sim/tests/test_domain_m1.py
   # or with pytest:
   python -m pytest 05_System_Tools/combat_sim/tests/test_domain_m1.py -v
   ```

3. **Key Files for Manual Code Audit**:
   - `05_System_Tools/combat_sim/combat_sim/core/types.py` (Enums, Tags, ThreatProfile)
   - `05_System_Tools/combat_sim/combat_sim/domain/topology.py` (Zone, ZoneTrait, TopologyGraph BFS)
   - `05_System_Tools/combat_sim/combat_sim/domain/equipment.py` (Weapons, Armor, Shields, Consumables)
   - `05_System_Tools/combat_sim/combat_sim/domain/quirks.py` (Quirks & Twists)
   - `05_System_Tools/combat_sim/combat_sim/domain/traits.py` (Enemy Traits & Ancestries)
   - `05_System_Tools/combat_sim/combat_sim/domain/entities.py` (GoblinBoss, PlayerMob, StandardEnemy, EliteEnemy, EnemyMob)
