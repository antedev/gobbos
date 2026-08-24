# 5-Component Handoff Report: Milestone 2 — Challenger 2

**Author**: Challenger 2 (`m2_challenger_2`)  
**Mission**: Empirical Stress-Testing of Milestone 2 Combat Resolvers and AI Heuristics (`combat_sim/engine/`)  
**Date**: 2026-08-23T21:47:30Z  
**Target File**: `c:\Users\ante\Documents\github\gobbos\.agents\m2_challenger_2\handoff.md`  
**Verdict**: **REQUEST_CHANGES**

---

## 1. Observation

Adversarial stress-testing was conducted across the combat simulation engine in `05_System_Tools/combat_sim`. A comprehensive 24-test verification suite was written and executed in `tests/test_challenger_m2_engine.py`.

### A. Subsystem Verifications (Passed)
1. **Mob Scatter Reactions (`MobReactionResolver.resolve_mob_scatter`)**:
   - Resource hierarchy consumption (Free Orders > Saved Reactions > Standard Actions > Zero Actions) functions accurately.
   - Size penalty scaling ($\text{Mod TN} = \text{Threat TN} + \max(0, \text{Size} - 1)$) verified across Mob Sizes 1 to 8.
   - Distance difficulty thresholds (same zone +1 auto success, normal distance 5+, max distance Mouth + 1 Hard 6, out of range $> \text{Mouth} + 1$) verified.
   - Gamble Trample Disaster on fumble correctly applies $(\text{Threat Damage} + 1)$ AoE damage to all health dice, sets `out_of_control = True`, and inflicts `Condition.STAGGERED` on the Boss in the same zone (while sparing Bosses in other zones).
2. **Environmental Hazards & Fire Propagation (`HazardResolver`)**:
   - Entry hazards for Slippery (Slink vs profile $\to$ Prone), Burning (Slink vs profile $\to$ 2 damage), and Toxic (Tough vs profile $\to$ Weakened) verified for Bosses and Mobs.
   - End-of-round fire spread across linear, star, and firebreak graph topologies verified on $1\text{d}6 \ge 5$.
3. **Tactical AI & Boredom Rule (`BossAI`, `MobAI`)**:
   - Boss AI reaction saving and target prioritization (Standard 1-hit kill enemies prioritized before Elites) verified.
   - Mob AI Boredom rule (maximum 1 Melee Attack action per turn, Move chaining allowed) verified.
   - Unordered Mob tables (Loitering saves 1 reaction; Out of Control saves 0 reactions and rolls frenzy/flee) verified.

### B. Confirmed Implementation Defects (Failures)

1. **CRITICAL: `NameError` Runtime Crash in `combat_sim/engine/ai.py` on Enemy Attack**:
   - **File & Line**: `combat_sim/engine/ai.py:348`
   - **Code**:
     ```python
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
   - **Verbatim Error**: `NameError: name 'ClatterResolver' is not defined`
   - **Root Cause**: `ClatterResolver` was omitted from the import statement on line 23 of `combat_sim/engine/ai.py`:
     ```python
     from combat_sim.engine.resolver import AttackResolver, AttackResult  # Missing ClatterResolver
     ```
   - **Impact**: Any encounter where an enemy survives to attack a Goblin Boss in Phase 3 immediately crashes the python runtime with `NameError`.

2. **HIGH: Premature 50% Swarm Terror Morale Trigger on Odd Enemy Squad Counts**:
   - **File & Line**: `combat_sim/engine/combat.py:203`
   - **Code**:
     ```python
     dead_enemies = [e for e in self.state.enemies if not e.is_alive or e.has_fled]
     if len(dead_enemies) >= max(1, len(self.state.enemies) // 2):
         morale_res = MoraleResolver.check_swarm_terror(...)
     ```
   - **Root Cause**: Integer floor division `len(self.state.enemies) // 2` evaluates $\lfloor N / 2 \rfloor$.
     - For $N=3$ enemies: $3 // 2 = 1$. When 1 enemy dies (33.3% casualties), `len(dead_enemies) >= 1` evaluates to `True`, prematurely triggering a 50% loss Morale check.
     - For $N=5$ enemies: $5 // 2 = 2$. When 2 enemies die (40% casualties), `len(dead_enemies) >= 2` evaluates to `True`.
   - **Required Math**: At least 50% casualties requires `len(dead_enemies) * 2 >= len(self.state.enemies)` (or `math.ceil(len(self.state.enemies) / 2)`).

3. **MEDIUM: Negative Incoming Damage Mitigated Invariant**:
   - **File & Line**: `combat_sim/core/dice.py:270`
   - **Code**:
     ```python
     damage_taken = max(0, incoming_damage - armor_succ)
     mitigated_damage = incoming_damage - damage_taken
     ```
   - **Root Cause**: When `incoming_damage < 0` (e.g. `-5`), `damage_taken = 0`, but `mitigated_damage = -5 - 0 = -5`.
   - **Required Math**: `mitigated_damage = max(0, incoming_damage - damage_taken)` (and `incoming_damage = max(0, incoming_damage)`).

---

## 2. Logic Chain

1. **Empirical Reproduction**:
   - In `tests/test_challenger_m2_engine.py::TestEmpiricalDefectReproductions::test_enemy_ai_boss_attack_clatter_name_error_reproduction`, executing `EnemyAI.execute_enemy_turns` against a GoblinBoss triggers `pytest.raises(NameError, match="name 'ClatterResolver' is not defined")`.
   - In `tests/test_challenger_m2_engine.py::TestEmpiricalDefectReproductions::test_50_percent_morale_threshold_integer_division_defect_reproduction`, evaluating `dead_enemies_count >= max(1, total_enemies // 2)` for 1 dead out of 3 confirms that a 33% casualty loss triggers the 50% Swarm Terror Morale check.
2. **Severity Assessment**:
   - Defect 1 is a blocking crash bug for interactive CLI runs (M3), Monte Carlo batch simulations (M4), and all multi-round combat encounters.
   - Defect 2 causes rule deviation in combat balance, causing enemy groups of 3 or 5 to break and flee prematurely.
3. **Conclusion Mandate**:
   - Because of the presence of unhandled runtime crashes and mathematical rule discrepancies, the worker implementation cannot be approved in its current state.

---

## 3. Caveats

- **Scope Boundary**: As Challenger 2, direct code fixes to `combat_sim/engine/` were not applied, honoring the strict review-only constraint.
- **Other Modules**: `combat_sim/core/dice.py` (aside from the negative damage edge case) and `combat_sim/engine/resolver.py` mechanics for Mob Scatter and Hazards demonstrated high algorithmic quality and adherence to rules.

---

## 4. Conclusion

**Verdict: REQUEST_CHANGES**

The combat simulation implementation is well-structured and implements the majority of complex rules (Exploding 6s, Clatter evasion/armor, Mob health arrays, Stagger sizes, Overkill wounds, Quirk triggers, Mob Scatter reactions, and Hazards) with precision. However, the following mandatory fixes are required before Milestone 2 can be approved:

1. **Fix `combat_sim/engine/ai.py`**:
   Add `ClatterResolver` to the import statement from `combat_sim.engine.resolver`.
2. **Fix `combat_sim/engine/combat.py:203`**:
   Change `len(dead_enemies) >= max(1, len(self.state.enemies) // 2)` to `(len(dead_enemies) * 2 >= len(self.state.enemies)) and len(dead_enemies) > 0`.
3. **Fix `combat_sim/core/dice.py:269-270`**:
   Ensure `incoming_damage = max(0, incoming_damage)` and `mitigated_damage = max(0, incoming_damage - damage_taken)`.

---

## 5. Verification Method

To reproduce and independently verify the findings and test suite:

```powershell
cd 05_System_Tools/combat_sim

# Run Challenger 2 empirical stress test suite (24 tests including defect reproductions)
python -m pytest tests/test_challenger_m2_engine.py -v

# Run full project test suite
python -m pytest tests/ -v
```
