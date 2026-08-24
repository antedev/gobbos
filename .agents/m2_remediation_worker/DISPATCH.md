## 2026-08-23T21:47:44Z

You are the Remediation Worker for Milestone 2 (Dice & Core Combat Engine).
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m2_remediation_worker\

You MUST read the authoritative specifications and review findings first:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\.agents\m2_reviewer_2\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\m2_challenger_2\handoff.md

Your mission:
Apply the 3 exact fixes requested by the reviewers and challengers:
1. `combat_sim/engine/ai.py`:
   - Import `ClatterResolver` from `combat_sim.engine.resolver` so that `ClatterResolver.resolve_boss_defense` at line 348 does not raise `NameError`.
   - Implement Group Attack combining in `EnemyAI.execute_enemy_turns`: When multiple enemies in the same zone attack a Goblin Boss, combine up to 3 attackers into a single attack with Damage = Base + (count - 1) that requires only 1 reaction from the Boss. When attacking a Mob, any number of enemies can combine.
2. `combat_sim/engine/combat.py`:
   - Fix 50% casualty Morale check condition at line 203: Change `len(dead) >= len(enemies) // 2` to `len(dead) >= math.ceil(len(enemies) / 2)` or `len(dead) >= (len(enemies) + 1) // 2` so that odd-sized squads (e.g. 3 enemies) trigger at 2 dead (66.7%), not 1 dead (33.3%).
3. Run all tests across the repository:
   `python -m pytest tests/ -v`
   Ensure all tests (including `test_challenger_m2_engine.py` and all previous test modules) pass with 0 errors.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A forensic auditor will independently verify your work.

Write your handoff report to:
`c:\Users\ante\Documents\github\gobbos\.agents\m2_remediation_worker\handoff.md`

When done, send a message back with your summary and test results.
