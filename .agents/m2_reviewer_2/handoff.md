# 5-Component Review & Handoff Report: Milestone 2 (Dice & Core Combat Engine)

**Author**: Reviewer 2 (`m2_reviewer_2`)  
**Roles**: Reviewer, Adversarial Critic  
**Date**: 2026-08-23T21:44:00Z  
**Verdict**: **REQUEST_CHANGES**  
**Target File**: `c:\Users\ante\Documents\github\gobbos\.agents\m2_reviewer_2\handoff.md`

---

## 1. Observation

Direct inspection of the Milestone 2 codebase in `05_System_Tools/combat_sim` and test execution results revealed the following observations:

### Observation 1: Missing Import Causing Fatal Runtime Crash in `ai.py`
- **Location**: `05_System_Tools/combat_sim/combat_sim/engine/ai.py`, Lines 23 & 348.
- **Code**:
  ```python
  # ai.py:23
  from combat_sim.engine.resolver import AttackResolver, AttackResult
  ```
  ```python
  # ai.py:347-355
  if isinstance(target, GoblinBoss):
      # Clatter defense
      clatter = ClatterResolver.resolve_boss_defense(
          boss=target,
          attacker=enemy,
          threat=threat,
          allied_mob=next((a for a in allies_in_zone if isinstance(a, PlayerMob)), None),
          topology=topology,
          rng=rng,
      )
  ```
- **Execution Error**: When running tests exercising enemy attacks against a living Goblin Boss (`python -m pytest tests/ -v`), execution crashes with:
  ```
  FAILED tests/test_challenger_m2_engine.py::TestTacticalAIAndCombatEngineLifecycleEmpirical::test_combat_engine_stagger_clearing_and_round_transitions
  NameError: name 'ClatterResolver' is not defined
  combat_sim\engine\ai.py:348: in execute_enemy_turns
      clatter = ClatterResolver.resolve_boss_defense(
  ```
- `ClatterResolver` is called at line 348 without being imported in `ai.py`.

---

### Observation 2: Unimplemented Group Attack Combining in `EnemyAI` (Integrity & Rule Discrepancy)
- **Location**: `05_System_Tools/combat_sim/combat_sim/engine/ai.py`, Lines 302–378.
- **Handoff Claim**: In `m2_combat_worker/handoff.md` (line 40), the worker claimed:
  > "`EnemyAI`: Deterministic target selection, Group Attack swarm combining up to 3 on Boss, Mob focus."
- **Code in `ai.py`**:
  ```python
  # ai.py:302-311
  # Group enemies by Zone to calculate Group Attacks
  for enemy in enemies:
      if not enemy.is_alive or enemy.has_fled:
          continue

      # Check if target in same zone
      allies_in_zone = [a for a in living_allies if a.zone_id == enemy.zone_id and a.is_alive]
      ...
  ```
- **Rule Requirement (`01_STAGE_Drafts/00_Rules/02 Combat.md:55-60`)**:
  > "If multiple enemies surround and attack a Gobbo, the GM should NOT make separate attacks. Instead, they combine into a [[Group Attack]]. While a PC can only be attacked by a maximum of 3 enemies, there is no limit on attacker on a Mob.
  > * The base damage is the primary enemy's Attack stat, **+1 damage** for every additional enemy in the swarm.
  > * The player only spends **one** saved Action to Dodge/Parry the entire [[Group Attack]].
  > *GM Advice:* Avoid splitting enemies into many small attacks against a single PC. This will instantly drain their saved actions and create a frustrating 'death by a thousand cuts.' Swarm them into Group Attacks instead!"
- **Finding**: Despite the comment `# Group enemies by Zone to calculate Group Attacks` at line 302, `EnemyAI.execute_enemy_turns` loops `for enemy in enemies:` individually and triggers a separate single attack for each enemy. This bypasses the Group Attack rule, causing multiple enemies in the same zone to exhaust Boss reactions on the first attack and deal unmitigated damage on subsequent attacks.

---

### Observation 3: Swarm Terror 50% Casualty Calculation Floor Division Error
- **Location**: `05_System_Tools/combat_sim/combat_sim/engine/combat.py`, Line 203.
- **Code**:
  ```python
  # combat.py:202-203
  dead_enemies = [e for e in self.state.enemies if not e.is_alive or e.has_fled]
  if len(dead_enemies) >= max(1, len(self.state.enemies) // 2):
  ```
- **Rule Requirement**: Morale checks are triggered at 50% casualties (half or more of the squad defeated).
- **Finding**: Using integer floor division (`len(enemies) // 2`) triggers the check below 50% when the squad size is odd:
  - For 3 enemies: `3 // 2 == 1`. 1 dead out of 3 (33.3%) triggers the check.
  - For 5 enemies: `5 // 2 == 2`. 2 dead out of 5 (40.0%) triggers the check.
  - Correct 50% threshold requires `math.ceil(len(enemies) / 2)` or `(len(enemies) + 1) // 2`.

---

### Observation 4: Core Engine Components Verified and Working Correctly
- **`combat_sim/core/dice.py`**:
  - `roll_dice`: Exploding 6s recursion with recursive bonus die generation verified.
  - Double explosion critical triggers (`is_critical = True` on consecutive 6 on bonus die) verified.
  - Salvage rolls (1d6 on $\le 0\text{d6}$: 6=1 success [no explosion], 1=fumble, 2–5=fail) verified.
  - Gobbo Gamble (rerolls only 1s on failed tests; continuing failure sets `fumble = True`) verified.
  - `BangarangaPool`: Communal seeding, draw limits, 1-die discard tax when drawn > TN, double-exploding 6s, and failure drain on 1s verified.
  - `resolve_clatter`: Active evasion (Slink Dodge / Tough Parry vs Threat TN) and passive armor mitigation (5+ mitigates 1 damage; non-exploding) verified.
- **`combat_sim/engine/resolver.py`**:
  - `AttackResolver`: Melee/Ranged weapon attacks, Impact Size Stagger calculation, Overkill wound conversion ($\lfloor \text{Successes}/\text{Defence TN} \rfloor$), Mob health single-target decrement/spillover, and Cleave/AoE full-pool damage verified.
  - `ClatterResolver`: Active Dodge/Parry, passive armor mitigation, Ablative Gear Sacrifice on lethal damage, and Meat Shield redirection verified.
  - `MobReactionResolver`: Mob Scatter order resource consumption and Gamble Trample Disaster verified.
  - `HazardResolver`: Zone entry hazards and fire propagation verified.
  - `MoraleResolver`: Swarm Terror pool scaling and Undead morale immunity verified.
- **Mob Boredom Rule in `ai.py`**:
  - `MobAI.execute_ordered_mob_turn` correctly tracks action types and prevents repeating Melee Attack in the same turn, while allowing Move chaining.

---

## 2. Logic Chain

1. **Premise 1**: A combat engine must execute all round phases without unhandled runtime exceptions.
   - *Evidence (Observation 1)*: `ai.py:348` references `ClatterResolver` which is not imported, causing an immediate `NameError` crash whenever an enemy attacks a Goblin Boss during `run_round()`.
2. **Premise 2**: Game mechanics claimed in handoffs and specified in core requirements must be genuinely implemented rather than represented by facade comments.
   - *Evidence (Observation 2)*: In `ai.py:302`, the comment `# Group enemies by Zone to calculate Group Attacks` is followed by individual loop iteration without grouping. The Gobbos rules explicitly require combining up to 3 enemies against a Boss into a single attack with boosted damage ($1 + \text{additional}$) requiring 1 reaction to evade.
3. **Premise 3**: Numerical threshold checks must match rules specifications.
   - *Evidence (Observation 3)*: `combat.py:203` uses integer floor division `// 2`, triggering the 50% casualty Morale check at 33.3% and 40.0% casualties for odd squad sizes.
4. **Conclusion**: While the core mathematical dice engine and domain resolvers are well-designed and feature-complete, the implementation contains a critical runtime crash bug in `ai.py`, an incomplete Group Attack combining implementation in `EnemyAI`, and a casualty calculation threshold bug. Therefore, changes must be requested before Milestone 2 can be approved.

---

## 3. Caveats

- **Web Server Independence**: Per `GEMINI.md`, the web server was not tested or modified.
- **Unit Test Suite**: The initial 253 unit tests in `test_dice.py`, `test_mob_health.py`, `test_equipment_armor.py`, `test_quirks.py`, `test_enemy_traits.py`, `test_scenarios.py`, `test_performance.py`, and `test_e2e.py` passed because the test fixtures either mocked individual resolver methods or ended the encounter during the player turn before an enemy could attack a living Boss. The runtime crash was exposed once multi-round combat with enemy active turns against living Bosses was executed.

---

## 4. Conclusion

**Verdict**: **`REQUEST_CHANGES`**

### Required Fixes:
1. **Fix Missing Import**: Add `ClatterResolver` to the imports from `combat_sim.engine.resolver` in `combat_sim/engine/ai.py` (Line 23).
2. **Implement Group Attack Combining in `EnemyAI`**: In `combat_sim/engine/ai.py` (`EnemyAI.execute_enemy_turns`), group living enemies in the same zone targeting the same Boss (up to a maximum of 3 enemies) or Mob (unlimited enemies) into a single consolidated `ThreatProfile` with `damage = primary_damage + (count - 1)` so the target resolves defense with a single Clatter/Scatter reaction.
3. **Fix 50% Casualty Morale Threshold**: In `combat_sim/engine/combat.py` (Line 203), update the threshold check to `math.ceil(len(self.state.enemies) / 2)` or `(len(self.state.enemies) + 1) // 2`.

---

## 5. Verification Method

1. Run the entire test suite from `05_System_Tools/combat_sim`:
   ```powershell
   python -m pytest tests/ -v
   ```
2. Inspect `combat_sim/engine/ai.py` line 23 to confirm `ClatterResolver` is imported.
3. Inspect `combat_sim/engine/ai.py` `EnemyAI.execute_enemy_turns` to verify enemies in the same zone combine their attacks against a single Boss (max 3) or Mob (unlimited) into a single Group Attack.
4. Run multi-round combat simulation where enemies attack a living Goblin Boss to verify clean execution across all 5 phases without `NameError`.
