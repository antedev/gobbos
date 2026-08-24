# Orchestrator Soft Handoff (State Dump) — Generation 1 to Generation 2

## 1. Observation & Milestone State
- **Phase 0 (Survey & Scope Mapping)**: COMPLETE. Full feature inventory (48 features), architecture, milestones, interface contracts, and code layout documented in `c:\Users\ante\Documents\github\gobbos\PROJECT.md`.
- **E2E Testing Track**: COMPLETE. `TEST_INFRA.md` and `TEST_READY.md` published at project root; 8 comprehensive test modules authored in `05_System_Tools/combat_sim/tests/`.
- **Milestone 1 (Tactical Domain & Models)**: COMPLETE & PASSED. Verified by 2 Reviewers, 2 Challengers, and 1 Forensic Auditor (`CLEAN` audit). Code in `combat_sim/core/types.py` and `combat_sim/domain/*`.
- **Milestone 2 (Dice & Core Combat Engine)**: Implemented (`combat_sim/core/dice.py`, `combat_sim/engine/resolver.py`, `combat_sim/engine/ai.py`, `combat_sim/engine/combat.py`). Iteration 1 Gate resulted in 3 approvals (Reviewer 1 APPROVE, Challenger 1 APPROVE, Forensic Auditor CLEAN) and 2 REQUEST_CHANGES (Reviewer 2, Challenger 2).

### Specific Remediation Required for Milestone 2:
1. **`combat_sim/engine/ai.py`**:
   - Add missing import of `ClatterResolver` from `combat_sim.engine.resolver` to fix `NameError` on line 348.
   - Implement Group Attack combining in `EnemyAI.execute_enemy_turns`: When multiple standard/mob enemies in the same zone attack the same Goblin Boss, combine up to 3 attackers into a single incoming attack ($\text{Damage} = \text{Base} + (\text{count} - 1)$, costing the Boss only 1 reaction). Any number of enemies can combine against a Mob.
2. **`combat_sim/engine/combat.py`**:
   - Fix 50% casualty Morale check calculation at line 203: Replace integer floor division `len(dead) >= len(enemies) // 2` with ceiling division `len(dead) >= math.ceil(len(enemies) / 2)` or `(len(enemies) + 1) // 2` to prevent premature triggers on odd-sized squads.

---

## 2. Logic Chain & Technical Context
- The package structure is located at `05_System_Tools/combat_sim`.
- All tests are runnable with `python -m pytest tests/ -v` from `05_System_Tools/combat_sim`.
- The Forensic Auditor has verified that all domain and engine implementations contain genuine business logic with zero hardcoding or facades.
- All interface contracts defined in `PROJECT.md` are strictly respected across `core`, `domain`, and `engine`.

---

## 3. Active Subagents & Pending Decisions
- **Active Subagents**: None (all 16 spawned subagents in Generation 1 have completed their tasks).
- **Pending Decisions**: None. The exact remediation steps for Milestone 2 are crystal clear.

---

## 4. Remaining Work & Concrete Next Steps for Successor
1. **Milestone 2 Remediation (Iteration 2)**:
   - Spawn a Worker (`m2_remediation_worker`) to apply the 3 fixes in `ai.py` and `combat.py` and run `pytest tests/ -v`.
   - Run Milestone 2 Gate: Spawn 2 Reviewers, 2 Challengers, and 1 Forensic Auditor. Verify all criteria pass.
2. **Milestone 3: Step-by-Step Interactive CLI Runner & Event Logger**:
   - Implement `combat_sim/core/events.py`, `combat_sim/cli/runner.py`, and `combat_sim/cli/main.py`.
   - Support formatted, rich turn-by-turn logs showing phases, actions, dice rolls, clatter resolutions, wound changes, and combat summaries.
   - Gate verification (Reviewers, Challengers, Auditor).
3. **Milestone 4: Monte Carlo Batch Simulator & Statistical Analytics Engine**:
   - Implement `combat_sim/analytics/monte_carlo.py` and `combat_sim/analytics/metrics.py`.
   - Ensure high performance (1,000+ iterations in <10 seconds SLA) and rich statistical tables (Win/Loss/TPK, Grit distribution, Mob survival size distribution, round duration, A/B balance metrics).
   - Gate verification.
4. **Milestone 5: Reference Encounters & Scenario Registry**:
   - Implement `combat_sim/scenarios/street_skirmish.py`, `combat_sim/scenarios/maulers_den.py`, `combat_sim/scenarios/tomb_highwayman.py`, and `combat_sim/scenarios/registry.py`.
   - Gate verification.
5. **Milestone 6: Final Acceptance & Adversarial Verification (Tier 5)**:
   - Run 100% of all E2E test suites (Tiers 1–4).
   - Run Tier 5 white-box adversarial stress tests.
   - Perform final Forensic Integrity Audit.
   - Send completion message to parent (`194cdb01-c1df-4386-9edb-6a9997d8a3f8`).

---

## 5. Key Artifacts Index
- `c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md` — Authoritative user request
- `c:\Users\ante\Documents\github\gobbos\PROJECT.md` — Master project plan, feature inventory, contracts, milestones
- `c:\Users\ante\Documents\github\gobbos\TEST_INFRA.md` — 4-Tier test architecture
- `c:\Users\ante\Documents\github\gobbos\TEST_READY.md` — Test suite readiness declaration
- `c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\GATE_STATUS.md` — Gate status records
- `c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\progress.md` — Progress tracker
- `c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\BRIEFING.md` — Persistent briefing
