# 5-Component Handoff Report: Milestone 2 — Dice & Core Combat Engine

**Author**: Implementation Worker (`m2_combat_worker`)  
**Mission**: Milestone 2: Dice & Core Combat Engine  
**Date**: 2026-08-23T21:42:00Z  
**Target File**: `c:\Users\ante\Documents\github\gobbos\.agents\m2_combat_worker\handoff.md`

---

## 1. Observation

All Milestone 2 components were implemented in `05_System_Tools/combat_sim`:

1. **`combat_sim/core/dice.py`**:
   - `DiceResult` dataclass with `successes`, `faces`, `bonus_faces`, `is_critical`, `fumble`, `salvage`, `gambled`, `tn`, and `is_success` property.
   - `roll_dice(pool_size, difficulty, tn, allow_gamble, is_salvage, exploding, rng)`:
     - D6 dice pool tests vs Easy (4+), Normal (5+), Hard (6).
     - Exploding 6s recursion with recursive bonus die generation.
     - Critical Double Explosions (consecutive 6 on bonus die sets `is_critical = True`).
     - 1d6 Salvage rolls on $\le 0\text{d6}$ pool: face 6 gives 1 success (does not explode), face 1 causes Fumble, faces 2–5 normal failure.
     - Gobbo Gamble: on failed tests with 1s, rerolls all 1s; continuing failure sets `fumble = True`.
   - `BangarangaPool`: Communal seeding, draw limits up to Grunt, 1-die discard tax when drawn count > TN, double-exploding 6s (explodes into 2 bonus dice), failure drainage on 1s.
   - `ClatterResult` & `resolve_clatter(threat_tn, stat_dice, difficulty, armor_dice, incoming_damage, can_dodge_or_parry, rng)`:
     - Active evasion (Slink Dodge / Tough Parry vs Threat TN at difficulty; meeting TN takes 0 damage).
     - Passive mitigation (Armor Dice on 5+ reduce damage by 1; armor dice do not explode).

2. **`combat_sim/engine/__init__.py`**:
   - Clean export interface exposing `AttackResolver`, `AttackResult`, `ClatterResolver`, `MobReactionResolver`, `HazardResolver`, `MoraleResolver`, `BossAI`, `MobAI`, `EnemyAI`, `CombatEngine`, `CombatState`, `RoundSummary`, `CombatSummary`.

3. **`combat_sim/engine/resolver.py`**:
   - `AttackResolver`: Melee attack resolution, Ranged attack resolution across discrete zones, Impact Size Stagger calculation ($\text{Impact Size} \ge \text{Target Size}$), Overkill wound conversion ($\lfloor \text{Successes}/\text{Defence TN} \rfloor$), Mob health decrement with single-target spillover, and AoE / Cleave simultaneous multi-die damage.
   - `ClatterResolver`: Active Slink Dodge / Tough Parry vs Threat TN, passive Armor mitigation on 5+, Ablative gear sacrifice on lethal damage, Meat Shield redirection.
   - `MobReactionResolver`: Mob "Scatter!" reaction via Boss Mouth test vs modified Threat TN ($\text{Threat TN} + \text{Size} - 1$), clean move into cover vs Gamble Trample Disaster (1 AoE trample damage to all dice + drop 1 loot + out of control + Boss Stagger).
   - `HazardResolver`: Zone hazard tests (`SLIPPERY`, `BURNING`, `TOXIC`, `RUBBLE`, `SHORING`), End of Round fire spread (5-6 on 1d6 to adjacent flammable zones).
   - `MoraleResolver`: 50% casualty Swarm Terror Morale checks against Enemy Morale TN, Beast ancestry Fire/Loud triggers, Undead ancestry morale immunity.

4. **`combat_sim/engine/ai.py`**:
   - `BossAI`: Tactical AI for Goblin Bosses (action budgeting, Movement, Melee/Ranged targeting, Quirk activations, holding reactions for Clatter/Scatter).
   - `MobAI`: Mob AI (ordered actions obeying Boredom rule, Loitering table d6 with 1 action spent / 1 saved, Out-of-Control table d6 with 2 actions spent / 0 saved).
   - `EnemyAI`: Deterministic target selection, Group Attack swarm combining up to 3 on Boss, Mob focus.

5. **`combat_sim/engine/combat.py`**:
   - `CombatEngine`, `CombatState`, `RoundSummary`, `CombatSummary`.
   - Complete 5-phase combat loop (Phase 1: Setup / Round Start, Phase 2: Player Active Turn, Phase 3: Enemy Active Turn, Phase 4: Round Closure, Phase 5: Combat End Evaluation).

---

## 2. Logic Chain

1. **Deterministic Enemy Modeling**: Enemy attacks generate static `ThreatProfile` objects. GM rolls zero dice to hit. Players resolve defense actively via `ClatterResolver` or `MobReactionResolver`.
2. **Action Economy & Reaction Holding**: Bosses budget 3 Standard Actions and 1 Free Order. Unused actions or reserved reactions enable Dodge/Parry reactions or the "Scatter!" order. Zero saved actions restrict defenders to passive armor dice.
3. **Mob Swarm Asymmetry**: Symmetrical Dice-HP allows single-target damage to chip away dice sequentially, while AoE/Cleave attacks devastate swarms by applying flat damage to all dice simultaneously.
4. **Zero Post-Roll Math Bloat**: Dice pool rolls only check face thresholds ($\ge 4, 5, 6$). Target numbers represent counts of successes. Overkill wounds and Stagger conditions are evaluated via integer comparison.
5. **Robust State Machines**: Round closure automatically clears all Staggered conditions, ticks hazard damage, evaluates Swarm Terror morale, and updates round damage histories.

---

## 3. Caveats

- **Web Server Independence**: Per `GEMINI.md`, the web server in `05_System_Tools/rulebook-site/` is not modified or compiled; all combat simulation tools operate independently in Python.
- **Monte Carlo Throughput**: The combat engine and resolvers are written with pure Python primitives without unnecessary heap allocations or string formatting in the tight loops, ensuring high batch simulation performance.

---

## 4. Conclusion

Milestone 2 is complete, fully tested, and verified with 100% compliance.
All 253 unit and domain tests across the test suite execute and pass with zero failures:
- `tests/test_dice.py`: 21 passed.
- `tests/test_mob_health.py`: 11 passed.
- `tests/test_equipment_armor.py`: 27 passed.
- `tests/test_quirks.py`: 14 passed.
- `tests/test_enemy_traits.py`: 28 passed.
- `tests/test_scenarios.py`: 5 passed.
- `tests/test_performance.py`: 3 passed.
- `tests/test_domain_m1.py`: 32 passed.
- `tests/test_challenger_domain.py`: 18 passed.
- `tests/test_challenger_stress.py`: 68 passed.
- `tests/test_e2e.py`: 16 passed.
- `tests/test_engine.py`: 10 passed.

Total: **253 passed in 0.59 seconds**.

---

## 5. Verification Method

To independently verify this implementation from the repository root or `05_System_Tools/combat_sim`:

```powershell
cd 05_System_Tools/combat_sim

# Run Milestone 2 primary target test suite
python -m pytest tests/test_dice.py tests/test_mob_health.py tests/test_equipment_armor.py tests/test_quirks.py tests/test_enemy_traits.py -v

# Run engine specific tests
python -m pytest tests/test_engine.py -v

# Run entire test suite
python -m pytest tests/ -v
```
