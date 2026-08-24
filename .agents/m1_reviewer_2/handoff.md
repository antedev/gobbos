# Milestone 1: Tactical Domain & Models - Reviewer 2 Independent Audit Report

**Agent**: Reviewer 2 (`m1_reviewer_2`)  
**Date**: 2026-08-23T21:35:00Z  
**Milestone**: M1 - Tactical Domain & Models  
**Target Subsystem**: `05_System_Tools/combat_sim/combat_sim/core/types.py`, `05_System_Tools/combat_sim/combat_sim/domain/*`  
**Verdict**: **`APPROVE`**

---

## 1. Observation

A comprehensive code inspection and adversarial review was conducted across the Milestone 1 codebase and test suites:

1. **Core Data Types & Enums (`combat_sim/core/types.py`)**:
   - `Difficulty(IntEnum)`: Defines `EASY = 4`, `NORMAL = 5`, `HARD = 6`. Correctly formats labels (`4+`, `5+`, `6` without redundant `+` on 6 pursuant to Gobbos notation rules). `meets_threshold(face)` correctly evaluates $\ge$ condition.
   - `Condition(str, Enum)`: Complete 9-condition set (`WEAKENED`, `RESTRAINED`, `DUMB`, `SILENCED`, `BLINDED`, `TERRIFIED`, `STUNNED`, `PRONE`, `STAGGERED`).
   - `Ancestry(str, Enum)`: All 5 ancestries (`BEAST`, `HUMANOID`, `UNDEAD`, `MONSTROSITY`, `FIEND`).
   - `EnemyScale(str, Enum)`: `STANDARD`, `ELITE`, `MOB`.
   - `CoverType(str, Enum)`: `NONE`, `PARTIAL`, `FULL`.
   - `ActionType(str, Enum)`: All 9 combat actions (`MOVE`, `MELEE_ATTACK`, `RANGED_ATTACK`, `PLUNDER`, `MANIPULATE`, `ORDER`, `DODGE`, `PARRY`, `SCATTER`).
   - `ZoneTraitType(str, Enum)`: All 7 environmental traits (`SLIPPERY`, `BURNING`, `TOXIC`, `NARROW`, `PILLARS`, `RUBBLE`, `SHORING`).
   - `WeaponTrait(str, Enum)` & `Tag`: Complete trait index including `BASHING`, `CLEAVE`, `PIERCING`, `CUTTING`, `REACH`, `VERSATILE`, `ARMOR_PIERCING`, `HEAVY`, `CRUSHING`, `CONCEALABLE`, `FAST_THROW`, `RAPID_SHOT`, `CLOCKWORK`, and property tags (`[Fire]`, `[Explosive]`, `[Acidic]`, `[Shock]`, `[Toxic]`, `[Loud]`, `[Tasty]`, `[Angelic]`, `[Light]`, `[Purified]`, `[Bleeding]`, `[Gaseous]`, `[Slick]`, `[Dark]`).
   - `ThreatProfile`: Immutable frozen dataclass capturing deterministic enemy threat profiles with shorthand formatting (`Tough 5+/2 (2 Dmg)`).

2. **Entity Lifecycle & Combatants (`combat_sim/domain/entities.py`)**:
   - `GoblinBoss`:
     - Grit dynamically initialized to $4 + 2 \times \text{Tough}$ (e.g. Tough 2 yields Max Grit 8).
     - Full action economy tracked: 3 Standard Actions + 1 Free Order + reaction saving/consumption.
     - Carry capacity calculated dynamically ($4 + 2 \times \text{Tough} + \text{Quirk bonuses}$).
     - Passive Armor Dice properly aggregates equipped armor and shields.
     - Slink Bane penalty extracted from armor.
     - `can_parry()` verified via shield check.
     - Damage and healing clamp correctly; death status updates cleanly when Grit $\le 0$.
   - `PlayerMob` & `EnemyMob`:
     - Symmetrical Dice-HP array (`health_dice: List[int]`) initialized to `[6] * size`.
     - Single-target damage decrement (`take_single_target_damage`) reduces active die and cleanly spills over into subsequent dice, popping exhausted dice ($\le 0$).
     - AoE damage (`take_aoe_damage`) applies simultaneous reduction across all dice in pool.
     - Size dynamically synchronizes with remaining dice count; alive state toggles to `False` upon pool exhaustion.
     - `EnemyMob.get_mob_damage()` computes $\text{Base Damage} + \max(0, \text{Size} - 1)$.
   - `StandardEnemy` & `EliteEnemy`:
     - `StandardEnemy`: One-hit kill on hits $\ge \text{Defence TN}$; applies Stagger on partial hits if $\text{Impact Size} \ge \text{Size}$.
     - `EliteEnemy`: Implements Overkill wound conversion ($\lfloor \text{Successes} / \text{Effective Defence TN} \rfloor$). Tracks Wounds and invokes `on_wound_taken` hooks. Stagger dynamically reduces Defence TN by 1 (min 1).

3. **Equipment & Consumable Factories (`combat_sim/domain/equipment.py`)**:
   - Weapons: Handedness, impact size modifiers (+1 for Heavy, +2 for Crushing), range in zones (0 to 3), and stat prerequisites (`min_tough`, `min_brains`).
   - Armor & Shields: Tier-appropriate Armor Dice (+1d to +3d), Slink Bane modifiers (0 to 2), Cannot Swim flags, Shield Parry enablement, and Tower Pavise movement halving.
   - 25 standard equipment catalogue factory functions providing concrete, production-ready instances.
   - Fumble break threshold evaluation logic (`roll_breaks`).

4. **Boss Quirks & Modular Twists (`combat_sim/domain/quirks.py`)**:
   - `MeatShield`: Evaluates presence of alive allied Mob in same zone; supports resource spending via Grunt, saved reaction, or standard action; outputs redirection metadata.
   - `AnkleBite`: Passive clean-dodge trigger vs melee attacker in same zone, granting free counter-attack with +1 automatic Success.
   - `PushLuck` / `SecondWind`: Validates available Grunt; identifies non-1 indices for reroll while keeping 1s locked for Gobbo Gamble.
   - `TwistModifier`: Modular twists (`Efficient` reducing Grunt cost, `Reflexive` converting to Free Action, `Spiteful`, `Loud`).

5. **Enemy Traits & Ancestries (`combat_sim/domain/traits.py`)**:
   - `ParryingBuckler`: Modifies first melee attack in round to Hard 6; subsequent melee attacks resolve at Normal 5+; resets at round start; does not alter ranged attacks.
   - `ThickBlubber`: Imposes -1d Bane on incoming attacks unless carrying `Tag.FIRE` / `"[Fire]"`.
   - `PlateBastion` / `Bastion`: Ignores first 1 damage per attack unless Piercing or elemental tags (`[Fire]`, `[Acidic]`, `[Shock]`).
   - `PressurizedSteamVent` / `SteamVent`: On taking $\ge 1$ Wound, outputs Slink 5+/2 2 Fire damage zone hazard threat.
   - `VoraciousRegrowth`: Heals 1 lost Wound at round start unless suppressed by Fire/Acid in the prior round.
   - `DryBones`: Imposes -1d Bane on Piercing/Cutting/Ranged bows; grants +1d Boon on Bashing/Crushing weapons.
   - Ancestries: Handlers for Beast (morale triggers on Fire/Loud/50%), Undead (morale immune), Monstrosity (cleave/mass resistance), Fiend, and Humanoid.

6. **Graph Topologies (`combat_sim/domain/topology.py`)**:
   - `ZoneProfile` & `Zone`: Multi-trait management, directional cover support, burning state.
   - `TopologyGraph`: BFS shortest distance (`get_distance`), shortest path finding (`find_path`), adjacency checks, and zone radius queries (`get_zones_within_distance`).

---

## 2. Logic Chain

1. **Zero Integrity Violations Confirmed**:
   - Every domain class implements genuine state and arithmetic calculation logic (no hardcoded return values, facade stubs, dummy mocks, or bypassed rules).
   - Test suites in `tests/test_domain_m1.py`, `tests/test_equipment_armor.py`, `tests/test_quirks.py`, `tests/test_enemy_traits.py`, and `tests/test_mob_health.py` execute genuine assertions against live object instances.

2. **Mathematical and Rules Rigor**:
   - **Mob Spillover**: Verified that iterative decrement loops through the health dice array correctly. For an initial pool of `[2, 6, 6]` taking 4 single-target damage:
     $$\text{Die 1: } 2 - 4 \le 0 \implies \text{eliminated, remaining dmg = } 2$$
     $$\text{Die 2: } 6 - 2 = 4 \implies \text{survives as 4}$$
     $$\text{Result: } [4, 6] \implies \text{Size } 2$$
   - **Mob AoE Simultaneous Damage**: Verified that list comprehension applies flat damage subtraction across all elements simultaneously. For `[6, 6, 6, 6]` taking 3 AoE damage, all dice drop to 3, dealing $4 \times 3 = 12$ total HP damage.
   - **Overkill & Stagger**: Verified that $\lfloor \text{Successes} / \text{Effective Defence TN} \rfloor$ accurately calculates multi-wound damage on Bosses/Elites. Partial hits ($\ge 1$ success but $<\text{Defence TN}$) apply `Condition.STAGGERED` if and only if $\text{Impact Size} \ge \text{Target Size}$, accurately respecting mass resistance.

3. **Boundary Condition Robustness**:
   - Excessive single-target or AoE damage beyond total mob HP terminates cleanly when the dice list is exhausted, avoiding `IndexError` or negative sizes.
   - Clamping functions (`max(0, ...)`, `min(max_stat, ...)`) are applied across all damage, healing, grunt modifications, and movement evaluations.
   - Disconnected graph nodes return `-1` distance and `[]` paths without infinite looping due to strict BFS visited set tracking.

---

## 3. Caveats

- **Combat Engine Execution (M2 Scope)**: The tactical domain models provide data structures, damage resolution hooks, and trait modification hooks. Full combat phase execution, dice throwing (exploding 6s, salvage rolls, Gobbo Gambles), Clatter Roll resolution, and tactical AI heuristics belong to Milestone 2.
- **Scenario Composition (M5 Scope)**: Scenario definitions in `combat_sim.scenarios` will compose these M1 models into ready-to-run encounters during Milestone 5.

---

## 4. Conclusion

The Milestone 1 implementation is architecturally sound, thoroughly tested, mathematically rigorous, and strictly compliant with all authoritative Gobbos game design tenets and engineering constraints.

**Explicit Verdict**: **`APPROVE`**

---

## 5. Verification Method

To independently verify the Milestone 1 implementation:

1. **Direct Domain Verification Execution**:
   ```bash
   python 05_System_Tools/combat_sim/tests/test_domain_m1.py
   ```
2. **Pytest Verification across M1 Suites**:
   ```bash
   pytest 05_System_Tools/combat_sim/tests/test_domain_m1.py \
          05_System_Tools/combat_sim/tests/test_equipment_armor.py \
          05_System_Tools/combat_sim/tests/test_quirks.py \
          05_System_Tools/combat_sim/tests/test_enemy_traits.py \
          05_System_Tools/combat_sim/tests/test_mob_health.py -v
   ```
3. **Key Invalidation Conditions**:
   - Any failure in single-target spillover or AoE full-pool damage reduction.
   - Inability to compute Overkill wound conversion $\lfloor \text{Successes} / \text{Defence TN} \rfloor$.
   - Any regression in trait lifecycle hooks (Parrying Buckler, Thick Blubber, Bastion, Steam Vent, Voracious Regrowth, Dry Bones).
