# BRIEFING — 2026-08-24T17:38:05Z

## Mission
Synthesize a complete, streamlined, modular core rules book for the Gobbos TTRPG in `02_PROD_Core_Rules/`, isolating pure mechanics from living content, establishing single-source cross-references, content schemas with `[CONTENT EXTENSION POINT]` tags, and gap markers with `[MISSING RULE / GAP]`.

## 🔒 My Identity
- Archetype: orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: c:\Users\ante\Documents\github\gobbos\.agents\orchestrator
- Original parent: parent
- Original parent conversation ID: 25142fdc-adcc-4819-b4df-99a2fa49e587

## 🔒 My Workflow
- **Pattern**: Project Pattern
- **Scope document**: c:\Users\ante\Documents\github\gobbos\PROJECT.md
1. **Decompose**: Survey authoritative STAGE and PROD drafts across all folders (00_Rules, 01_Characters & Mobs, 03_Loot, 04_Enemies, 05_Base, 07_Travel, 08_Magic), extract pure mechanics, map schemas, and identify gaps.
2. **Dispatch & Execute**:
   - Phase 0: Survey & Schema Mapping (3 Explorers / Spec Miners in parallel).
   - Milestone 1: Core Engine, Resolution, Attributes & Action Economy (`01_Core_Resolution.md`, `02_Boss_Profile_and_Gang.md`, `03_Action_Economy_and_Turn_Flow.md`).
   - Milestone 2: Space, Movement, Combat & Mobs (`04_Zones_and_Movement.md`, `05_Combat_Engine.md`, `06_Mob_Mechanics.md`).
   - Milestone 3: Health, Conditions, Magic & Supernatural (`07_Damage_Grit_and_Wounds.md`, `08_Magic_and_Bangaranga.md`).
   - Milestone 4: Macro Game Loops & Progression (`09_The_Raid_Loop.md`, `10_The_Lair_Loop_and_Progression.md`, `11_Journeys_and_Hazards.md`).
   - Milestone 5: Global Cross-References, Style Verification & Schema Audit.
3. **On failure**: Retry -> Replace -> Skip -> Redistribute -> Redesign.
4. **Succession**: At 16 spawns, write handoff.md, spawn successor.
- **Work items**:
  1. Survey and Scope Mapping [in-progress]
  2. Milestone 1: Core Engine, Resolution, Attributes & Action Economy [pending]
  3. Milestone 2: Space, Movement, Combat & Mobs [pending]
  4. Milestone 3: Health, Conditions, Magic & Supernatural [pending]
  5. Milestone 4: Macro Game Loops & Progression [pending]
  6. Milestone 5: Verification, Gap Audit & Forensic Integrity Check [pending]
- **Current phase**: Phase 0 — Survey & Exploration
- **Current focus**: Parallel Survey of STAGE/PROD drafts across all 11 core systemic domains

## 🔒 Key Constraints
- NEVER write, modify, or create source code files directly (dispatch workers).
- NEVER run build/test commands directly (require workers to do so).
- File-editing tools allowed ONLY for metadata/state files (.md) in .agents/ and project root.
- Audit is a BINARY VETO — violation means milestone failure, no exceptions.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh.
- Always include path to ORIGINAL_REQUEST.md in all dispatches.
- Strict adherence to GEMINI.md Tier A mechanics, total de-gendering, slash notation `[Stat] [Target Face]+/[Successes]`.

## Current Parent
- Conversation ID: 25142fdc-adcc-4819-b4df-99a2fa49e587
- Updated: 2026-08-24T17:38:05Z

## Key Decisions Made
- Clear separation between systemic engine (02_PROD_Core_Rules/) and living catalogs (tagged with `[CONTENT EXTENSION POINT: <Category>]`).
- Universal content schemas for Weapons, Armor, Gear, Quirks, Tag Effects, Spells/Rituals, NPC/Enemy Statblocks, Lair Rooms.
- Systematic gap callout: `[MISSING RULE / GAP: <Description of missing mechanic, why it is needed, and suggested resolution>]`.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| spec_miner_core_0 | teamwork_preview_spec_miner | Phase 0: Core Engine, Resolution, Combat | completed | 1db436d3-36a1-4fd2-b83e-a512a786a161 |
| spec_miner_combat_magic_0 | teamwork_preview_spec_miner | Phase 0: Mobs, Damage, Magic & Enemies | completed | d2f916f2-9a42-4c75-8bf7-89f312d4c5cd |
| spec_miner_loops_0 | teamwork_preview_spec_miner | Phase 0: Raid, Lair, Journeys & Economy | completed | 1cb0c97c-a092-49a7-9dbe-ff62c42e8e88 |
| m1_core_worker_0 | teamwork_preview_worker | Milestone 1: Core Resolution & Profile | completed | d9c38404-a2e7-4a13-8a55-be25716c8088 |
| m2_combat_worker_0 | teamwork_preview_worker | Milestone 2: Spatial, Combat & Mobs | completed | 543213aa-9a8f-426b-b820-6ad1bc42463d |
| m3_magic_threats_worker_0 | teamwork_preview_worker | Milestone 3: Health, Magic & Threats | completed | 7eabd806-0951-42de-b86f-c2c57ef653ce |
| m4_loops_worker_0 | teamwork_preview_worker | Milestone 4: Macro Loops & Progression | completed | 4e33586c-2b6b-4323-b0db-821a341529e1 |
| r1_reviewer_1 | teamwork_preview_reviewer | Review Chapters 01–06 | completed | 232ef916-e896-4cef-8351-af0a07ae715c |
| r1_reviewer_2 | teamwork_preview_reviewer | Review Chapters 07–12 | completed | 0123293f-b94e-4869-8b9b-7278e35a0b03 |
| r1_challenger_1 | teamwork_preview_challenger | Linkage & Schema Challenge | completed | 9d6b68d8-d3fd-45f9-a8ad-3ad8078c0cca |
| r1_challenger_2 | teamwork_preview_challenger | Style & Notation Challenge | completed | 6c390f8f-b08e-4e0b-86e5-334651eef9f5 |
| r1_auditor | teamwork_preview_auditor | Forensic Integrity Audit | completed | 338b511e-6d5a-45ca-853a-350c966ca94d |
| remediation_worker_0 | teamwork_preview_worker | Remediation of Keyword Drift & Formatting | completed | f89fc4b2-fe33-4a50-af3f-e6338efe48d9 |

## Succession Status
- Succession required: no
- Spawn count: 13 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: not started
- Safety timer: none

## Artifact Index
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md — User requirements record
- c:\Users\ante\Documents\github\gobbos\PROJECT.md — Project specification & milestone tracker
- c:\Users\ante\Documents\github\gobbos\GEMINI.md — Official Style & Formatting Guide
- c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\GATE_STATUS.md — Milestone gate tracker
- c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\DISPATCH.md — Dispatch log
- c:\Users\ante\Documents\github\gobbos\.agents\orchestrator\progress.md — Liveness & iteration progress

