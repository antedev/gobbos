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
# Orchestrator Handoff: Gobbos TTRPG Modular Core Rules Synthesis

**Date**: 2026-08-24T19:56:00+02:00  
**Parent Agent ID**: `25142fdc-adcc-4819-b4df-99a2fa49e587`  
**Working Directory**: `c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\`  
**Scope**: Complete Core Rules Synthesis in `02_PROD_Core_Rules/`  

---

## 1. Milestone State

| # | Milestone | Scope | Deliverables | Gate Status |
|---|-----------|-------|--------------|-------------|
| M0 | Survey & Schema Mining | `01_STAGE_Drafts/` & `02_PROD_Core_Rules/` | 3 Spec Mining analysis reports | DONE |
| M1 | Core Engine, Profile & Actions | Chapters 01, 02, 03 | `01_Core_Resolution.md`, `02_Boss_Profile_and_Gang.md`, `03_Action_Economy_and_Turn_Flow.md` | PASSED |
| M2 | Space, Movement, Combat & Mobs | Chapters 04, 05, 06 | `04_Zones_and_Movement.md`, `05_Combat_Engine.md`, `06_Mob_Mechanics.md` | PASSED |
| M3 | Health, Magic & Threats | Chapters 07, 08, 12 | `07_Damage_Grit_and_Wounds.md`, `08_Magic_and_Bangaranga.md`, `12_Adversaries_and_Threats.md` | PASSED |
| M4 | Macro Loops & Progression | Chapters 09, 10, 11 | `09_The_Raid_Loop.md`, `10_The_Lair_Loop_and_Progression.md`, `11_Journeys_and_Hazards.md` | PASSED |
| M5 | Verification & Forensic Audit | All 12 Chapters in `02_PROD_Core_Rules/` | 2 Reviewer reports, 2 Challenger reports, 1 Forensic Audit (`CLEAN`), Remediation report | PASSED |

---

## 2. Active Subagents
- All 13 subagents across Survey, Implementation, Review, Challenge, Audit, and Remediation have completed and retired.
- Active subagents: None (0 running).

---

## 3. Pending Decisions / Blockers
- None. All 12 core rulebook chapters are completely synthesized, verified, remediated, and audited.

---

## 4. Key Artifacts Produced

### Production Core Rulebook (`02_PROD_Core_Rules/`)
1. `01_Core_Resolution.md` (D6 pool engine, difficulty thresholds, exploding 6s, Salvage roll, Gobbo Gamble, Bangaranga pool engine).
2. `02_Boss_Profile_and_Gang.md` (Main stats 1–5, Grunt, Grit, Boss creation, Gang archetype, Quirk Schema & `[CONTENT EXTENSION POINT: Boss Quirks & Talents]`).
3. `03_Action_Economy_and_Turn_Flow.md` (Boss 3 actions + 1 Free Order, Mob 2 actions & Boredom rule, Reactions, 5-Phase Round flow).
4. `04_Zones_and_Movement.md` (Zone topology, Zone Profiles `Difficulty+/TN`, Movement, Partial/Full Cover, Traits/Hazards, Chaos Tick).
5. `05_Combat_Engine.md` (Melee/Ranged attack pipeline, Overkill rule, Impact Size/Stagger, Clatter defense roll, Group attacks, Weapon Schema & `[CONTENT EXTENSION POINT: Weapons]`, Armor/Shield Schema & `[CONTENT EXTENSION POINT: Armor & Shields]`, Gear Schema & `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`).
6. `06_Mob_Mechanics.md` (Mob anatomy, Size, Health Dice pool starting at face 6, decrement & spillover, Frontline rule, Cleave/AoE, Loitering & Out of Control tables, Scatter reaction & gamble, Swarm Terror morale).
7. `07_Damage_Grit_and_Wounds.md` (Damage resolution against Grit, 0 Grit Final Act & Death, Enemy Wounds track, Overkill formula, 9-Condition Matrix & recovery, Condition/Hazard Schema & `[CONTENT EXTENSION POINT: Environmental Hazards & Conditions]`).
8. `08_Magic_and_Bangaranga.md` (Farkle Push-Your-Luck Brains pool casting, matching sets for Tiers 1–5, Chaotic Leakage, Bangaranga spending, Rituals, Tag Effect/Spell Schema & `[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]`).
9. `09_The_Raid_Loop.md` (4-Phase Raid flow, 5-to-1 exponential Loot Value ladder, Scrap, Infamy, Glory, XP, Carry capacity, Loot & Salvage Schema & `[CONTENT EXTENSION POINT: Loot & Salvage Items]`).
10. `10_The_Lair_Loop_and_Progression.md` (Lair Dashboard, Warren Tier, Gobbo Pool, 4-Step sequence, Safe vs Risky labor, Boss downtime, Generational Boss death & Successor mechanics, Lair Room Schema & `[CONTENT EXTENSION POINT: Lair Rooms & Facilities]`).
11. `11_Journeys_and_Hazards.md` (Journey loop, 4 Travel Roles, Route tests, Travel events, Environmental Attrition, Journey Hazard Schema & `[CONTENT EXTENSION POINT: Journey Hazards & Events]`).
12. `12_Adversaries_and_Threats.md` (Deterministic Threat resolution, GM never rolls, Threat TN profiles, 3 enemy scales, Enemy Mob scaling, 3-Layer Trait Hierarchy, Enemy Statblock Schema & `[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]`).

### State & Verification Metadata
- `PROJECT.md`: Project master architecture, feature inventory, chapter breakdown, and milestone plan.
- `.agents/orchestrator/GATE_STATUS.md`: Authoritative gate records with forensic audit verification.
- `.agents/orchestrator/BRIEFING.md`: Working memory and team registry.
- `.agents/orchestrator/progress.md`: Liveness progress record.
