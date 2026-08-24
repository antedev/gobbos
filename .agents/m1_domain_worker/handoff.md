# Milestone 1: Tactical Domain & Models - Handoff Report

**Agent**: Implementation Worker (`m1_domain_worker`)  
**Date**: 2026-08-23T21:32:00Z  
**Milestone**: M1 - Tactical Domain & Models  
**Working Directory**: `c:\Users\ante\Documents\github\gobbos\05_System_Tools\combat_sim`  

---

## 1. Observation

Authoritative game rules and technical requirements from `PROJECT.md`, `ORIGINAL_REQUEST.md`, `spec_miner_gear_0/handoff.md`, `spec_miner_rules_0/handoff.md`, and `explorer_scenarios_0/handoff.md` were directly translated into genuine Python domain models in `05_System_Tools/combat_sim`:

1. **`05_System_Tools/combat_sim/pyproject.toml`**:
   - Standard setuptools configuration targeting Python $\ge 3.10$ with package entrypoint and pytest integration.
2. **`combat_sim/core/types.py` & `combat_sim/core/__init__.py`**:
   - `Difficulty(IntEnum)`: `EASY = 4`, `NORMAL = 5`, `HARD = 6`, with `.label` notation (`4+`, `5+`, `6`) and `.meets_threshold(face)`.
   - `Condition(Enum)`: `WEAKENED`, `RESTRAINED`, `DUMB`, `SILENCED`, `BLINDED`, `TERRIFIED`, `STUNNED`, `PRONE`, `STAGGERED`.
   - `Ancestry(Enum)`: `BEAST`, `HUMANOID`, `UNDEAD`, `MONSTROSITY`, `FIEND`.
   - `EnemyScale(Enum)`: `STANDARD`, `ELITE`, `MOB`.
   - `CoverType(Enum)`: `NONE`, `PARTIAL`, `FULL`.
   - `ActionType(Enum)`: `MOVE`, `MELEE_ATTACK`, `RANGED_ATTACK`, `PLUNDER`, `MANIPULATE`, `ORDER`, `DODGE`, `PARRY`, `SCATTER`.
   - `ZoneTraitType(Enum)`: `SLIPPERY`, `BURNING`, `TOXIC`, `NARROW`, `PILLARS`, `RUBBLE`, `SHORING`.
   - `WeaponHandedness(IntEnum)`: `ONE_HAND = 1`, `TWO_HAND = 2`.
   - `WeaponTrait(Enum)`: `BASHING`, `CLEAVE`, `PIERCING`, `CUTTING`, `REACH`, `VERSATILE`, `ARMOR_PIERCING`, `HEAVY`, `CRUSHING`, `CONCEALABLE`, `FAST_THROW`, `RAPID_SHOT`, `CLOCKWORK`.
   - `Tag`: Constants for master property tags (`Tag.FIRE`, `Tag.EXPLOSIVE`, `Tag.ACIDIC`, `Tag.SHOCK`, `Tag.TOXIC`, `Tag.LOUD`, `Tag.TASTY`, `Tag.ANGELIC`, `Tag.LIGHT`, `Tag.PURIFIED`, `Tag.BLEEDING`, `Tag.GASEOUS`, `Tag.SLICK`, `Tag.DARK`).
   - `ThreatProfile`: Dataclass capturing incoming deterministic enemy threat profiles (`threat_stat`, `difficulty`, `threat_tn`, `damage`, `tags`, `impact_size`, `is_aoe`, `cleave`, `range_zones`).
3. **`combat_sim/domain/topology.py`**:
   - `ZoneProfile`: `difficulty`, `tn`, `description`, shorthand formatting.
   - `ZoneTrait`: `trait_type`, `description`, `is_active`, `metadata`.
   - `Zone`: `id`, `name`, `profile`, `cover`, `traits`, `loot_bulk`, `is_flammable`, `is_burning`, `is_blocked`, `directional_cover`, methods for trait attachment/lookup/removal and directional cover queries.
   - `TopologyGraph`: Graph model with adjacency mapping, BFS shortest distance calculation (`get_distance`), BFS path finding (`find_path`), adjacency checks, and zone radius queries (`get_zones_within_distance`).
4. **`combat_sim/domain/equipment.py`**:
   - `Equipment(ABC)`: `name`, `bulk`, `tier`, `break_threshold`, `roll_breaks(roll)`.
   - `Weapon(Equipment)`: Handedness, impact size modifiers, range in zones, weapon traits, tags, prerequisite stats (`min_tough`, `min_brains`), and `get_effective_impact_size(wielder_size)`.
   - `Armor(Equipment)`: `armor_dice` (+1d to +3d), `slink_bane` (0 to 2), `cannot_swim`.
   - `Shield(Equipment)`: `armor_dice`, `enables_parry`, `halves_movement`, `immune_to_piercing`.
   - `Consumable(Equipment)`: Area threat profiles, blast ranges, impact sizes, tags.
   - Full factory catalogue functions: `create_bone_shiv`, `create_notched_sword`, `create_spiked_mace`, `create_heavy_greataxe`, `create_great_hammer`, `create_halberd`, `create_sling`, `create_shortbow`, `create_light_crossbow`, `create_military_longbow`, `create_heavy_arbalest`, `create_repeating_crossbow`, `create_light_armor`, `create_medium_armor`, `create_heavy_armor`, `create_runed_carapace`, `create_pot_lid_shield`, `create_tower_pavise`, `create_godstone_aegis`, `create_spark_bomb`, `create_fire_flask`, `create_smoke_pot`, `create_powder_keg`, `create_mortar_shell`, `create_sol_quartz`.
5. **`combat_sim/domain/quirks.py`**:
   - `Quirk(ABC)` & `TwistModifier`: Modular powers with Grunt costs, action costs, twist modifiers (`Spiteful`, `Loud`, `Efficient`, `Reflexive`).
   - Implementations: `MeatShield` (redirects damage to allied Mob in Zone), `AnkleBite` (+1 automatic Success melee counter-attack on clean Dodge), `PushLuck` / `SecondWind` (rerolls non-1 dice for 1 Grunt), `OpportunityStrike` / `SlipperyQuirk`, `SwallowLoot`, `Butcher`.
6. **`combat_sim/domain/traits.py`**:
   - `EnemyTrait(ABC)`: Lifecycle and resolution hooks (`on_round_start`, `on_round_end`, `on_incoming_attack_modify_difficulty`, `on_incoming_attack_modify_pool`, `on_incoming_damage_modify`, `on_wound_taken`, `on_morale_check_trigger`).
   - Implementations: `ParryingBuckler` (1st melee attack Hard 6, subsequent Normal 5+), `ThickBlubber` (-1d Bane unless [Fire]), `PlateBastion` / `Bastion` (ignores 1 damage unless Piercing/elemental), `PressurizedSteamVent` / `SteamVent` (erupts Slink 5+/2 2 Fire damage hazard on taking a Wound), `VoraciousRegrowth` (heals 1 Wound at round start unless burned/acidified), `DryBones` (Piercing/Cutting/Bows -1d Bane, Bashing/Crushing +1d Boon).
   - Ancestry Handlers: `BeastAncestryTrait`, `UndeadAncestryTrait`, `MonstrosityAncestryTrait`, `FiendAncestryTrait`, `HumanoidAncestryTrait`.
7. **`combat_sim/domain/entities.py`**:
   - `BaseEntity(ABC)`: ID, name, zone_id, size, conditions set, Stagger clearing, status helpers.
   - `GoblinBoss(BaseEntity)`: Tough, Slink, Mouth, Brains, Grunt, Grit ($4 + 2 \times \text{Tough}$), action budget (3 Standard + 1 Free Order), saved reactions, loadout (main hand, off hand, armor, inventory, quirks), carry capacity, movement speed, Slink bane, armor dice summation, Parry authorization.
   - `PlayerMob(BaseEntity)`: Symmetrical Dice-HP array (`health_dice`), single-target damage decrement & spillover, AoE simultaneous multi-die damage, action budget, ordered state, armor rating.
   - `ThreatAttack`: Deterministic attack action generator with threat profiles.
   - `Enemy(BaseEntity)`, `StandardEnemy` (one-hit kill on hits $\ge$ Defence TN, Stagger on partial hit), `EliteEnemy` (Wounds track, Overkill wound conversion $\lfloor \text{Successes} / \text{Defence TN} \rfloor$, Stagger on partial hit, Voracious Regrowth suppression flag), `EnemyMob` (Dice-HP array, deterministic attack scaling $\text{Base} + \text{Size} - 1$, single-target & AoE damage).
8. **`combat_sim/tests/test_domain_m1.py`**:
   - 19 comprehensive unit tests covering all enums, topology BFS, equipment catalogue, quirks & twists, enemy traits & ancestries, and entity state lifecycles.

---

## 2. Logic Chain

1. **Deterministic Foundations & Zero Math Bloat**:
   - By creating `ThreatProfile` and `ThreatAttack`, enemy attacks are modeled with static threat difficulty thresholds and flat damage, ensuring GM never rolls to hit.
   - By structuring `GoblinBoss`, `PlayerMob`, and `Enemy` with clear stat dice and passive armor dice accessors, all defensive resolutions in M2 can execute the two-step Clatter Roll without ambiguous intermediate state.
2. **Symmetrical Mob Health & AoE Vulnerability**:
   - `PlayerMob` and `EnemyMob` maintain physical `health_dice: List[int]`. Single-target attacks decrement the active die and spill over into subsequent dice upon die exhaustion ($<1$).
   - AoE attacks subtract damage simultaneously from all dice in `health_dice`, directly reflecting the devastating anti-swarm dynamics specified in `STAGE 13_Goblin_mob.md`.
3. **Overkill Rule & Stagger Calculation**:
   - `EliteEnemy.take_hit()` computes wounds via $\lfloor \text{Successes} / \text{Effective Defence TN} \rfloor$. If successes are $\ge 1$ but less than Defence TN, it checks if `Impact Size >= Physical Size` to apply `Condition.STAGGERED` (which dynamically reduces Defence TN by 1 until round closure).
4. **Equipment & Modular Quirks Interoperability**:
   - Weapons encapsulate handedness and impact size modifiers (+1 for Heavy, +2 for Crushing), allowing direct evaluation of mass resistance.
   - Shields unlock the `can_parry()` flag on `GoblinBoss`, enabling Tough Parry reactions.
   - Quirks utilize context dictionaries for deterministic trigger checks and resource deductions.

---

## 3. Caveats

- **Combat Engine (M2 Scope)**: The domain models provide state tracking, damage decrements, condition application, and trait hooks; full combat loop orchestration (turn phases, dice pool throwing with exploding 6s and Gobbo Gambles, Clatter Roll resolution, AI decision heuristics) will be implemented in Milestone 2.
- **Scenario Definitions (M5 Scope)**: Pre-built scenarios (Street Skirmish, The Mauler's Den, Tomb of the Highwayman) will be fully assembled in `combat_sim.scenarios` using these M1 domain models and equipment factories.

---

## 4. Conclusion

Milestone 1 (Tactical Domain & Models) is fully implemented, verified, and strictly compliant with the Integrity Mandate. No dummy stubs, facades, or mocks exist. All domain entities, equipment factories, quirks, enemy traits, and topology models are production-ready.

---

## 5. Verification Method

To independently verify Milestone 1:

1. **Module Import & Sanity Check**:
   ```bash
   python -c "import combat_sim.core as core; import combat_sim.domain as domain; print('M1 Package successfully imported!')"
   ```
2. **Run Domain Test Suite**:
   ```bash
   python 05_System_Tools/combat_sim/tests/test_domain_m1.py
   # or with pytest:
   python -m pytest 05_System_Tools/combat_sim/tests/test_domain_m1.py -v
   ```
3. **Verify Expected Output**:
   All 19 test methods pass cleanly:
   - `TestCoreEnumsAndTypes` (Difficulty, Condition, Ancestry, EnemyScale, CoverType, ActionType, ZoneTraitType, ThreatProfile shorthand)
   - `TestTopologyAndRouting` (Zone traits, directional cover, BFS shortest distance, path finding)
   - `TestEquipmentCatalogue` (Light/Medium/Heavy weapons, Ranged weapons, Armor/Shields, Consumables/Explosives)
   - `TestQuirksAndTwists` (Meat Shield, Ankle Bite, Push Luck, Twists, Swallow Loot, Butcher)
   - `TestEnemyTraitsAndAncestries` (Parrying Buckler Hard 6, Thick Blubber, Bastion, Steam Vent, Voracious Regrowth, Dry Bones, Ancestries)
   - `TestEntitiesStateAndBehavior` (Goblin Boss lifecycle, Player Mob spillover & AoE, Standard Enemy 1-hit kill, Elite Overkill & Stagger, Enemy Mob damage scaling)
