# Forensic Integrity Audit & Handoff Report: Milestone 2 (Dice & Core Combat Engine)

**Target Work Product**: `05_System_Tools/combat_sim/combat_sim/` (`core/dice.py`, `engine/resolver.py`, `engine/ai.py`, `engine/combat.py`)  
**Auditor**: Forensic Auditor (`m2_auditor`)  
**Parent Conversation ID**: `582cc6de-8afe-4ac2-854c-9d22c656f5b2`  
**Date**: 2026-08-23T23:43:30Z  
**Verdict**: **`CLEAN`**

---

## Part 1: Forensic Audit Report

**Work Product**: `combat_sim/core/dice.py`, `combat_sim/engine/resolver.py`, `combat_sim/engine/ai.py`, `combat_sim/engine/combat.py`  
**Profile**: General Project (Development Mode / Strict Integrity Audit)  
**Verdict**: **`CLEAN`**

### Phase Results
- **Hardcoded Output Detection**: **`PASS`** — No static lookup tables, pre-calculated dice rolls, or hardcoded boolean/integer responses exist in source files.
- **Facade Detection**: **`PASS`** — All classes and functions implement genuine, complete computational logic without placeholder `return <constant>` stubs or unimplemented methods.
- **Pre-populated Artifact Detection**: **`PASS`** — No pre-populated test result logs, execution dumps, or fake attestation files exist in the codebase.
- **Self-Certifying Tests**: **`PASS`** — Test assertions validate against official rules specifications (`02_PROD_Core_Rules/`, `01_STAGE_Drafts/`) and analytical probability distributions rather than self-referential tautologies.
- **Execution Delegation / Cheating**: **`PASS`** — Core combat mechanics, dice rolling, exploding recursion, clatter defense, and state machine loops are built purely from scratch using Python standard library primitives (`random`, `math`, `dataclasses`, `typing`).
- **Behavioral Test Execution**: **`PASS`** — Full test suite executed independently with 253 passed tests in 0.68s.

---

## Part 2: 5-Component Handoff Report

### 1. Observation

All 4 target source files were exhaustively inspected line-by-line:

1. **`combat_sim/core/dice.py` (361 lines)**:
   - `roll_d6(rng)`: Discrete integer generation via `random.randint(1, 6)` or `rng.randint(1, 6)`.
   - `DiceResult`: Fully typed dataclass with `successes`, `faces`, `bonus_faces`, `is_critical`, `fumble`, `salvage`, `gambled`, `tn`, and dynamic `is_success` property (`self.successes >= self.tn`).
   - `roll_dice(...)`:
     - Explicit branch for Salvage rolls ($\le 0\text{d6}$ pool): Face 6 yields 1 success without exploding; Face 1 flags `fumble = True`; Faces 2–5 yield normal failure (`lines 162-200`).
     - Standard pool execution with recursive exploding 6s: bonus dice appended to `bonus_faces`, cascading recursion while bonus die equals 6, and setting `is_critical = True` on consecutive 6s (`lines 208-226`).
     - Gobbo Gamble: strictly triggered on `allow_gamble=True`, `successes < tn`, and `1 in faces`; keeps non-1 dice, rerolls 1s with potential recursive explosions; sets `fumble = True` if still failing TN (`lines 228-269`).
   - `BangarangaPool`: Communal seeding, draw limits, 1-die discard tax when drawn count > TN, double explosions (2 bonus dice per 6), and failure drainage on 1s (`lines 55-150`).
   - `resolve_clatter(...)`: Active evasion (Slink Dodge / Tough Parry vs Threat TN at difficulty; meeting TN zeroes damage) and passive armor mitigation (rolling armor dice vs 5+ where each success reduces damage by 1; non-exploding) (`lines 294-361`).

2. **`combat_sim/engine/resolver.py` (690 lines)**:
   - `AttackResolver.resolve_melee_attack`: Base pool calculation (Boss Tough + Versatile 2H / Butcher boon vs Mob attack pool), condition modifiers (Weakened, Blinded), Impact Size calculation, enemy trait pool & difficulty hooks, dice rolling, cross-gang infighting self-damage on 1s, and damage/overkill wound evaluation vs Standard, Elite, and Enemy Mob scales (`lines 70-206`).
   - `AttackResolver.resolve_ranged_attack`: Distance BFS check vs weapon range, Line of Sight / Cover check (Full Cover prevents attacks, Partial Cover inflicts -1d Bane), condition modifiers, trait hooks, dice rolling, and target wound/kill evaluation (`lines 208-320`).
   - `ClatterResolver.resolve_boss_defense`: Meat Shield Quirk check (redirects attack to allied Mob in zone with passive armor mitigation), active defense selection (evaluates Slink Dodge vs Tough Parry, checks shield requirements, applies partial cover boons and condition penalties), passive armor mitigation with Armor Piercing reduction, Ankle Bite counter-attack trigger on clean melee dodge, and Ablative Gear Sacrifice on lethal damage (`lines 322-463`).
   - `MobReactionResolver.resolve_mob_scatter`: Boss Mouth test vs modified Threat TN ($\text{Threat TN} + \text{Mob Size} - 1$), +1 auto success for same zone, distance scaling; clean scatter moves Mob into adjacent zone, whereas Gamble Trample Disaster inflicts $\text{Threat Damage} + 1$ AoE damage to all dice, sets Out of Control, drops loot, and inflicts Stagger on the Boss (`lines 465-556`).
   - `HazardResolver`: Zone entry checks for `SLIPPERY` (Prone), `BURNING` (2 fire damage), and `TOXIC` (Weakened); End of Round fire spread on 5-6 to adjacent flammable zones (`lines 558-630`).
   - `MoraleResolver`: Swarm Terror checks for enemy groups at 50% casualties, rolling Swarm Pool (Mob Size + PCs) vs Enemy Morale TN on 5+; respects Undead morale immunity (`lines 632-690`).

3. **`combat_sim/engine/ai.py` (380 lines)**:
   - `BossAI`: Action budgeting (reserves 1 Reaction for defense if enemies alive/present), Free Order issuance to allied Mobs, standard action utilization (melee attack prioritizing Standard enemies, ranged attack in range, or pathfinding movement) (`lines 26-149`).
   - `MobAI`: Ordered action resolution obeying the Mob Boredom rule (allows Move twice, max 1 Melee Attack), Loitering table resolution (1 action spent, 1 saved reaction, d6 table), and Out-of-Control table resolution (2 actions spent, 0 saved reactions, d6 table) (`lines 151-283`).
   - `EnemyAI`: Deterministic movement toward nearest ally, attack execution on Boss or Mob with Enemy Mob damage scaling ($\text{Base} + \text{Size} - 1$) (`lines 285-380`).

4. **`combat_sim/engine/combat.py` (277 lines)**:
   - `CombatState`: Snapshot tracking `scenario_name`, `topology`, `allies`, `enemies`, `current_round`, `bangaranga_pool`, `is_combat_over`, `victor`, and `round_history` (`lines 54-74`).
   - `CombatEngine.run_round`: Full 5-phase loop (Phase 1: Action resets and trait `on_round_start`, Phase 2: Player Active Turn and un-ordered Mobs, Phase 3: Enemy Active Turn, Phase 4: Round Closure with Stagger auto-clearing, trait `on_round_end`, Voracious Regrowth fire tracking, 50% casualty Swarm Terror checks, and fire spread, Phase 5: Combat End Evaluation) (`lines 76-241`).
   - `CombatEngine.run_to_completion`: Sequentially executes rounds up to `max_rounds` and tallies final metrics into `CombatSummary` (`lines 243-277`).

5. **Test Suite Verification**:
   - Command: `python -m pytest tests/ -v`
   - Output: `253 passed in 0.68s`
   - 0 failed, 0 errors, 0 warnings.

---

### 2. Logic Chain

1. **Rule Fidelity**: Every mechanic specified in Milestone 2 (`ORIGINAL_REQUEST.md`, `PROJECT.md`, `STAGE_Drafts/`, `PROD_Core_Rules/`) is genuinely implemented in executable Python code.
2. **Deterministic & Stochastic Rigor**:
   - The GM never rolls dice to hit; threats are deterministic `ThreatProfile` objects.
   - Players roll active Slink/Tough evasion and passive Armor Dice.
   - Dice rolling algorithms accurately model exploding 6s recursion and the Gobbo Gamble penalty state machine.
3. **No Cheating or Bypassing**:
   - No mock fixtures exist in runtime production modules.
   - No hardcoded boolean or constant returns were detected.
   - All state transitions (damage decrement, spillover, condition application/clearing, death flags, fire spread, morale routs) are driven by real business logic.
4. **Conclusion**: The codebase satisfies all integrity and technical requirements for Milestone 2.

---

### 3. Caveats

- **Web Server Independence**: In accordance with `GEMINI.md`, the web server in `05_System_Tools/rulebook-site/` was not inspected or modified as it is decoupled from the Python combat simulation toolkit.
- **Future Milestones**: Interactive CLI runner (`M3`), Monte Carlo batch runner (`M4`), and Reference Scenarios (`M5`) depend on this engine and will be audited in subsequent milestone phases.

---

### 4. Conclusion

**Verdict: `CLEAN`**

The Milestone 2 work product (`combat_sim/core/dice.py`, `combat_sim/engine/resolver.py`, `combat_sim/engine/ai.py`, `combat_sim/engine/combat.py`) is authentic, robust, rules-accurate, and free of any integrity violations, facades, or shortcuts.

---

### 5. Verification Method

To independently verify this audit from the workspace root or `05_System_Tools/combat_sim`:

```powershell
cd 05_System_Tools/combat_sim

# 1. Run all Milestone 2 core & engine tests
python -m pytest tests/test_dice.py tests/test_mob_health.py tests/test_equipment_armor.py tests/test_quirks.py tests/test_enemy_traits.py tests/test_engine.py -v

# 2. Run the complete test suite
python -m pytest tests/ -v
```
