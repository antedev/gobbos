# Forensic Audit Report: Milestone 1 (Tactical Domain & Models)

**Auditor Archetype**: Forensic Auditor  
**Date**: 2026-08-23T21:35:00Z  
**Target**: Milestone 1 (`05_System_Tools/combat_sim/combat_sim/`)  
**Verdict**: **`CLEAN`**

---

## 1. Observation

A full forensic static analysis and code audit was conducted across all files created for Milestone 1 in `c:\Users\ante\Documents\github\gobbos\05_System_Tools\combat_sim\`:

1. **`combat_sim/core/types.py` & `combat_sim/core/__init__.py`**:
   - `Difficulty(IntEnum)`: Accurately maps `EASY = 4`, `NORMAL = 5`, `HARD = 6`, with formatting `.label` (`4+`, `5+`, `6`) and threshold check `.meets_threshold(face)`.
   - `Condition(str, Enum)`: Accurately models all 9 tactical conditions (`WEAKENED`, `RESTRAINED`, `DUMB`, `SILENCED`, `BLINDED`, `TERRIFIED`, `STUNNED`, `PRONE`, `STAGGERED`).
   - `Ancestry(str, Enum)`: Models `BEAST`, `HUMANOID`, `UNDEAD`, `MONSTROSITY`, `FIEND`.
   - `EnemyScale(str, Enum)`: `STANDARD`, `ELITE`, `MOB`.
   - `CoverType(str, Enum)`: `NONE`, `PARTIAL`, `FULL`.
   - `ActionType(str, Enum)`: `MOVE`, `MELEE_ATTACK`, `RANGED_ATTACK`, `PLUNDER`, `MANIPULATE`, `ORDER`, `DODGE`, `PARRY`, `SCATTER`.
   - `ZoneTraitType(str, Enum)`: `SLIPPERY`, `BURNING`, `TOXIC`, `NARROW`, `PILLARS`, `RUBBLE`, `SHORING`.
   - `WeaponHandedness(IntEnum)`: `ONE_HAND = 1`, `TWO_HAND = 2`.
   - `WeaponTrait(str, Enum)`: All 13 official traits (`BASHING`, `CLEAVE`, `PIERCING`, `CUTTING`, `REACH`, `VERSATILE`, `ARMOR_PIERCING`, `HEAVY`, `CRUSHING`, `CONCEALABLE`, `FAST_THROW`, `RAPID_SHOT`, `CLOCKWORK`).
   - `Tag`: Constants for property tags (`[Fire]`, `[Explosive]`, `[Acidic]`, `[Shock]`, `[Toxic]`, `[Loud]`, `[Tasty]`, `[Angelic]`, `[Light]`, `[Purified]`, `[Bleeding]`, `[Gaseous]`, `[Slick]`, `[Dark]`, `[Hardened]`, `[Spiky]`, `[Terrifying]`, `[Regenerating]`).
   - `ThreatProfile`: Immutable dataclass modeling deterministic enemy threats with shorthand visualization (e.g., `Tough 5+/2 (2 Dmg)`).

2. **`combat_sim/domain/topology.py`**:
   - `ZoneProfile`: `difficulty`, `tn`, and shorthand code formatting (`5+/1`, `4+/2`).
   - `ZoneTrait`: Active status and metadata tracking.
   - `Zone`: Trait attachment/query/removal, flammability and burning state management, and directional cover mapping (`get_cover_from`, `set_directional_cover`).
   - `TopologyGraph`: Graph model with adjacency mapping, BFS shortest distance routing (`get_distance`), BFS path finding (`find_path`), adjacency checks, and zone radius queries (`get_zones_within_distance`).

3. **`combat_sim/domain/equipment.py`**:
   - `Equipment(ABC)`: Bulk, tier, and Fumble break threshold evaluation (`roll_breaks`).
   - `Weapon(Equipment)`: Handedness, impact size calculation (`get_effective_impact_size`), range in zones, weapon traits, property tags, and stat prerequisites.
   - `Armor(Equipment)`: Armor dice (+1d to +3d), Slink bane (0 to 2), and swimming restriction.
   - `Shield(Equipment)`: Armor dice (+1d to +2d), Parry enablement flag (`enables_parry`), movement speed reduction, and piercing immunity.
   - `Consumable(Equipment)`: Area threat profiles, blast ranges, impact sizes, and elemental tags.
   - 25 standard factory functions (`create_bone_shiv`, `create_notched_sword`, `create_spiked_mace`, `create_heavy_greataxe`, `create_great_hammer`, `create_halberd`, `create_sling`, `create_shortbow`, `create_light_crossbow`, `create_military_longbow`, `create_heavy_arbalest`, `create_repeating_crossbow`, `create_light_armor`, `create_medium_armor`, `create_heavy_armor`, `create_runed_carapace`, `create_pot_lid_shield`, `create_tower_pavise`, `create_godstone_aegis`, `create_spark_bomb`, `create_fire_flask`, `create_smoke_pot`, `create_powder_keg`, `create_mortar_shell`, `create_sol_quartz`).

4. **`combat_sim/domain/quirks.py`**:
   - `TwistModifier`: Modular twists (`Spiteful`, `Loud`, `Efficient` [-1 Grunt cost], `Reflexive` [converts action to Free Action]).
   - `MeatShield`: Validates allied Mob in the same zone, checks Grunt or Reaction availability, deducts resources, and redirects damage.
   - `AnkleBite`: Validates clean Dodge reaction vs melee attacker in the same zone, returning free counter-attack with +1 automatic Success.
   - `PushLuck` / `SecondWind`: Validates Grunt availability, locks 1s for Gobbo Gamble, and returns non-1 indices to reroll.
   - Additional quirks: `OpportunityStrike` / `SlipperyQuirk`, `SwallowLoot`, `Butcher`.

5. **`combat_sim/domain/traits.py`**:
   - `EnemyTrait(ABC)`: Standard lifecycle hooks (`on_round_start`, `on_round_end`, `on_incoming_attack_modify_difficulty`, `on_incoming_attack_modify_pool`, `on_incoming_damage_modify`, `on_wound_taken`, `on_morale_check_trigger`).
   - `ParryingBuckler`: Enforces Hard (6) on 1st melee attack received each round and Normal (5+) on subsequent; resets on round start.
   - `ThickBlubber`: Imposes -1d Bane unless attack carries the `[Fire]` tag.
   - `PlateBastion` / `Bastion`: Flat -1 damage reduction unless bypassed by Piercing or elemental tags (`[Fire]`, `[Acidic]`, `[Shock]`).
   - `PressurizedSteamVent` / `SteamVent`: Erupts Slink 5+/2 (2 Fire Dmg) hazard upon suffering a Wound.
   - `VoraciousRegrowth`: Recovers 1 Wound at round start unless suppressed by prior-round Fire or Acid damage.
   - `DryBones`: Imposes -1d Bane on Piercing/Cutting/Ranged and grants +1d Boon on Bashing/Crushing.
   - Ancestry Handlers: `BeastAncestryTrait`, `UndeadAncestryTrait`, `MonstrosityAncestryTrait`, `FiendAncestryTrait`, `HumanoidAncestryTrait`.

6. **`combat_sim/domain/entities.py`**:
   - `BaseEntity(ABC)`: ID, name, zone ID, size, condition set, Stagger clearing, and status flags.
   - `GoblinBoss`: Grit formula ($4 + 2 \times \text{Tough}$), action budget (3 Standard + 1 Free Order), saved reactions, inventory/loadout, unencumbered bulk capacity, Slink speed calculation with armor/encumbrance penalties, armor dice calculation, and Parry authorization.
   - `PlayerMob`: Symmetrical Dice-HP array (`health_dice`), single-target active die reduction with spillover to next dice, simultaneous AoE damage across all dice in pool, attack pool scaling by Size, and passive armor calculation.
   - `ThreatAttack`: Deterministic attack action generator with threat profiles.
   - `StandardEnemy`: One-hit kill on hits $\ge$ effective Defence TN; Stagger on partial hit when $\text{Impact Size} \ge \text{Target Size}$.
   - `EliteEnemy`: Multi-Wound track, Overkill wound conversion ($\lfloor \text{Successes} / \text{Defence TN} \rfloor$), Stagger on partial hit, Voracious Regrowth fire/acid damage tracking, and `on_wound_taken` reactions.
   - `EnemyMob`: Symmetrical Dice-HP array, deterministic attack damage scaling ($\text{Base} + \text{Size} - 1$), single-target & AoE damage.

7. **Unit Test Coverage (`tests/test_domain_m1.py`)**:
   - 19 comprehensive unit tests covering all enums, topology BFS, equipment catalogue, quirks & twists, enemy traits & ancestries, and entity state lifecycles.

---

## 2. Logic Chain

1. **Deterministic Design & Math Bloat Elimination**:
   - All enemy threats are modeled deterministically via `ThreatProfile` and `ThreatAttack`. The GM never rolls dice to hit, strictly conforming to Tenet 2 and R1/R2 requirements.
2. **Symmetrical Mob Health Mechanics**:
   - Both `PlayerMob` and `EnemyMob` implement genuine list-based dice tracking (`health_dice: List[int]`). Single-target attacks correctly decrement the head die and spill excess into subsequent dice. AoE attacks simultaneously subtract from all dice in the pool, maintaining genuine swarm physics.
3. **Overkill & Stagger Fidelity**:
   - `EliteEnemy.take_hit()` computes wounds using integer floor division $\lfloor \text{Successes} / \text{Effective Defence TN} \rfloor$. Stagger condition dynamically reduces Defence TN by 1 and is cleared during round closure.
4. **Prohibited Pattern Verification**:
   - *Hardcoded test results*: None. All calculations are dynamic and mathematical.
   - *Facade implementations*: None. All methods contain genuine state mutations and business logic.
   - *Fabricated outputs*: None. No pre-generated log files exist.
   - *Self-certifying tests*: Tests evaluate real domain algorithms (BFS, damage spillover, Overkill).
   - *Execution delegation*: Pure Python standard library implementation with zero prohibited third-party dependencies.

---

## 3. Caveats

- **Milestone Scope**: Milestone 1 is focused on the tactical domain models, entities, equipment, quirks, traits, and topologies. The combat execution loop (dice rolling with exploding 6s, Gobbo Gambles, Clatter Roll defense resolution, turn sequence, and AI heuristics) will be orchestrated in Milestone 2.
- **Scenario Assemblies**: Pre-built reference scenarios (Street Skirmish, The Mauler's Den, Tomb of the Highwayman) will be assembled in Milestone 5 using these M1 domain classes.

---

## 4. Conclusion

The Milestone 1 work product exhibits complete structural and mechanical fidelity to the official Gobbos rules and technical specifications. Zero integrity violations, dummy stubs, or bypassed calculations were found.

**Verdict**: **`CLEAN`**

---

## 5. Verification Method

To independently verify Milestone 1:

1. **Inspect Module Definitions**:
   ```bash
   python -c "import combat_sim.core as core; import combat_sim.domain as domain; print('M1 Package successfully imported!')"
   ```
2. **Execute Domain Test Suite**:
   ```bash
   python -m pytest 05_System_Tools/combat_sim/tests/test_domain_m1.py -v
   ```
3. **Execute Focused Trait & Equipment Suites**:
   ```bash
   python -m pytest 05_System_Tools/combat_sim/tests/test_equipment_armor.py 05_System_Tools/combat_sim/tests/test_quirks.py 05_System_Tools/combat_sim/tests/test_enemy_traits.py 05_System_Tools/combat_sim/tests/test_mob_health.py -v
   ```
