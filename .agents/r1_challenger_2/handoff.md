# HANDOFF REPORT: CHALLENGER 2 (EMPIRICAL REVIEW)

**Agent**: Challenger 2 (Empirical Reviewer / Rules Lawyer & Layout Specialist)  
**Date**: 2026-08-24T19:50:45Z  
**Type**: Hard Handoff (Task Complete)  
**Target Scope**: `02_PROD_Core_Rules/` (Chapters 01 to 12)  
**Interface Contracts**: `GEMINI.md`, `ORIGINAL_REQUEST.md`

---

## 1. Observation

Direct programmatic and systematic text inspection of all 12 chapters in `02_PROD_Core_Rules/` yielded the following verified facts:

### A. Style & Dice Slash Notation
- **Target 6 Checks**: Zero instances of invalid `6+` in any check. The only instance of `6+` in `02_PROD_Core_Rules/` is in `01_Core_Resolution.md:40`, which explicitly mandates:
  > `>> **IMPORTANT:** The numeral **6** represents the absolute ceiling on a standard d6. In accordance with official system notation, **Hard** difficulty is written strictly as **6** (never write `6+`).`
  All target 6 checks are written as `Brains 6/2`, `[Narrow] [6/1]`, etc.
- **Target 4 & 5 Checks**: 100% of checks use standard `[Stat] [Face]+/[TN]` notation (e.g., `Slink 5+/2`, `Tough 4+/1`, `Brains 5+/1`).

### B. Header Hierarchy
- Across all 12 files (`01_Core_Resolution.md` to `12_Adversaries_and_Threats.md`), all headers strictly follow `# H1` $\to$ `## H2` $\to$ `### H3` $\to$ `#### H4` without skipping any level.

### C. Keyword Constancy Violations (Synonym Drift)
1. **PC Bosses Suffering "Wounds"**:
   - `10_The_Lair_Loop_and_Progression.md`, Line 326:
     > `2. Tyrant's Beatdown: A Boss makes an opposed Tough 5+/2 or Mouth 5+/2 test as a Downtime Action... failure inflicts 1 Wound on the Boss and increases Threat by +1 from the riot.`
   - `11_Journeys_and_Hazards.md`, Line 118:
     > `*Rule:* Test **Slink** against the **Zone Profile** or suffer **1 Wound** (Boss) / **1 Size damage** (Mob).`
   - `11_Journeys_and_Hazards.md`, Line 133:
     > `*Rule:* ...drowning (**1 Wound** per round).`
   - `11_Journeys_and_Hazards.md`, Line 147:
     > `*Rule:* ...The Zone gains the **Crumbling** hazard (occupants test **Slink** against the **Zone Profile** or take **1 Wound**)...`
2. **Player Mobs Referred to as "Squad"**:
   - `06_Mob_Mechanics.md`, Lines 9, 17, 36, 39, 45, 99, 204, 206, 209:
     > Line 9: `A **Mob** is an abstract squad of lesser goblins...`
     > Line 17: `| Runts Squad | 1 | 1d6 | 1 | 4 Bulk |`
     > Line 36: `...consumes the squad's carrying capacity.`
     > Line 45: `* **Shared Expedition Tools:** Squad tools (such as Ropes...`
     > Line 204: `A Boss can spend one **Order Action** to split a Mob into two smaller squads:`
     > Line 206: `...(both squads retain the armor tier)... assigned to one of the split squads.`
     > Line 209: `Two allied Mobs occupying the same Zone can be merged into a single squad...`
3. **Loot Referred to as "Treasure Caches"**:
   - `03_Action_Economy_and_Turn_Flow.md`, Line 170:
     > `3. Objective Declaration: The GM declares active Raid Point objectives and visible treasure caches.`

### D. De-Gendering & Anti-Clunk Mandate
- **Gendered Pronouns**: Zero instances of `he`, `she`, `him`, `her`, `his`, `hers`, `himself`, `herself` across all 12 chapters.
- **Singular "They/Their/Them/Themselves"**: Detected on singular agents in `01_Core_Resolution.md:106, 175`, `02_Boss_Profile_and_Gang.md:274`, `03_Action_Economy_and_Turn_Flow.md:100`, `04_Zones_and_Movement.md:52, 53, 106, 112, 115, 144`, `05_Combat_Engine.md:35, 57, 119, 183, 282, 283`, `06_Mob_Mechanics.md:156, 170`, `08_Magic_and_Bangaranga.md:172, 210`, `10_The_Lair_Loop_and_Progression.md:348`.

---

## 2. Logic Chain

1. `GEMINI.md` defines the strict keyword rules: (a) Goblin Bosses track **Grit** (never Wounds or Health); (b) player goblin units are strictly **Mobs** (never squads); (c) plunder value is strictly **Loot**; (d) singular "they" is banned in favor of second person "you/your" or explicit role nouns.
2. In `07_Damage_Grit_and_Wounds.md:17`, the rule explicitly codifies:
   > `* **The Synonym Ban:** A Goblin Boss tracks Grit. A Goblin Boss never tracks Health or Wounds. Health Dice are used exclusively by Mobs, and Wounds are tracked exclusively by Elite and Boss enemies.`
3. Observations C.1 directly contradict this rule by assigning "Wounds" to Goblin Bosses in Chapters 10 and 11.
4. Observations C.2 directly violate the Mob vs Squad keyword mandate by referring to player Mobs as "squad" in Chapter 06.
5. Observations D violate the strict singular "they" ban by using singular "they/their/them/themselves" instead of "you/your" or explicit nouns.
6. Therefore, the appropriate verdict is **`CHALLENGE_DETECTED`**, supported by exact line references and remediation recommendations.

---

## 3. Caveats

- Inanimate plural entities (such as dice, tags, items, conditions) and collective groups (such as players, enemies, runts) legitimately use plural pronouns (`they`, `them`, `their`, `themselves`), which does not violate the gender ban.
- The root files (Chapters 01 to 12) represent the single source of truth; legacy subdirectories (`00_Rules/`, `01_Characters & Mobs/`) should be deleted or archived to avoid clutter.

---

## 4. Conclusion

- **Verdict**: **`CHALLENGE_DETECTED`**
- **Actionable Steps for Resolution**:
  1. Update `10_The_Lair_Loop_and_Progression.md` (line 326) and `11_Journeys_and_Hazards.md` (lines 118, 133, 147) to replace "Wound (Boss)" with "damage to Grit (Boss)".
  2. Update `06_Mob_Mechanics.md` (lines 9, 17, 36, 39, 45, 99, 204, 206, 209) to replace "squad/squads" with "Mob/Mobs".
  3. Update `03_Action_Economy_and_Turn_Flow.md` (line 170) to replace "treasure caches" with "Loot caches".
  4. Replace singular "they/their" instances with second person ("you/your") or explicit nouns ("the Boss's").

---

## 5. Verification Method

To independently verify these findings:
1. Grep for `\bWound\b` in `10_The_Lair_Loop_and_Progression.md` and `11_Journeys_and_Hazards.md`.
2. Grep for `\bsquad\b` in `06_Mob_Mechanics.md`.
3. Grep for `\b6\+` across all markdown files in `02_PROD_Core_Rules/`.
4. Inspect `challenge_report.md` in `.agents/r1_challenger_2/` for full line-by-line itemization.
