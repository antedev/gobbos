## 2026-08-24T17:51:40Z

You are the Remediation Worker for Gobbos Core Rules Synthesis.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\remediation_worker_0\

Mandatory Inputs:
- Style Guide & Rules: c:\Users\ante\Documents\github\gobbos\GEMINI.md
- Reviewer 2 Handoff: c:\Users\ante\Documents\github\gobbos\.agents\r1_reviewer_2\handoff.md
- Challenger 1 Handoff: c:\Users\ante\Documents\github\gobbos\.agents\r1_challenger_1\handoff.md
- Challenger 2 Handoff: c:\Users\ante\Documents\github\gobbos\.agents\r1_challenger_2\handoff.md

Your Tasks:
Apply the following surgical line-by-line remediations across `02_PROD_Core_Rules/`:

1. In `02_PROD_Core_Rules/11_Journeys_and_Hazards.md`:
   - Line 51: Change Mob non-Tough travel tests from `1d6` to `2d6` to strictly match the baseline in `01_Core_Resolution.md` and `06_Mob_Mechanics.md`.
   - Lines 118, 133, 147: Replace all references to PC Boss "Wound" / "1 Wound" with "Grit damage" / "lose 1 Grit" (Bosses track Grit, only Elites/Monsters track Wounds).
   - Lines 86–98: Standardize encumbrance terminology to match `06_Mob_Mechanics.md` and `09_The_Raid_Loop.md`.
   - Remove any markdown code fences surrounding `[MISSING RULE / GAP: ...]` and `[CONTENT EXTENSION POINT: ...]` tags so they appear as clear un-fenced markdown callouts.

2. In `02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md`:
   - Line 326: Replace "Wounds" with "Grit loss" or "Grit damage" for PC Bosses.
   - Remove any markdown code fences surrounding `[MISSING RULE / GAP: ...]` and `[CONTENT EXTENSION POINT: ...]` tags so they appear as un-fenced markdown callouts.

3. In `02_PROD_Core_Rules/09_The_Raid_Loop.md`:
   - Remove any markdown code fences surrounding `[MISSING RULE / GAP: ...]` and `[CONTENT EXTENSION POINT: ...]` tags so they appear as un-fenced markdown callouts.

4. In `02_PROD_Core_Rules/06_Mob_Mechanics.md`:
   - Replace any remaining occurrences of "squad" / "squads" with "Mob" / "Mobs" or "follower units".

5. In `02_PROD_Core_Rules/03_Action_Economy_and_Turn_Flow.md`:
   - Replace "treasure caches" with "Loot caches".

6. In `02_PROD_Core_Rules/02_Boss_Profile_and_Gang.md`:
   - Clean up `Grit (Health Capacity)` to `Grit (Damage Capacity)` or simply `Grit`.

Mandatory Integrity Warning:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work.

Write `changes.md` and `handoff.md` in your working directory and message parent when complete.
