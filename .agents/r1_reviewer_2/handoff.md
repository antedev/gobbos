# Handoff Report — Reviewer 2 (Gobbos Core Rules Chapters 07–12)

## 1. Observation
- **Scope Examined**:
  - `02_PROD_Core_Rules/07_Damage_Grit_and_Wounds.md` (199 lines)
  - `02_PROD_Core_Rules/08_Magic_and_Bangaranga.md` (259 lines)
  - `02_PROD_Core_Rules/09_The_Raid_Loop.md` (284 lines)
  - `02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md` (352 lines)
  - `02_PROD_Core_Rules/11_Journeys_and_Hazards.md` (217 lines)
  - `02_PROD_Core_Rules/12_Adversaries_and_Threats.md` (229 lines)
  - Cross-referenced against `01_Core_Resolution.md`, `02_Boss_Profile_and_Gang.md`, `03_Action_Economy_and_Turn_Flow.md`, `04_Zones_and_Movement.md`, `05_Combat_Engine.md`, and `06_Mob_Mechanics.md`.
- **Direct Findings Observed**:
  1. **Engine vs. Content Separation & Extension Points**: All 6 chapters feature structural markdown templates and formal `[CONTENT EXTENSION POINT]` tags (Chapter 07 Line 173, Chapter 08 Line 227, Chapter 09 Line 254, Chapter 10 Line 302, Chapter 11 Line 194, Chapter 12 Line 194). Zero living content catalogs exist in PROD.
  2. **Gap Tagging**: 16 dedicated `[MISSING RULE / GAP: ...]` markers are properly formatted and placed across Chapters 07–12.
  3. **Style & Total De-Gendering**: 0 occurrences of gendered singular pronouns (`he/she/his/her/him`). 100% compliance with slash notation `[Stat] [Face]+/[TN]` and ceiling notation `6/TN` on Hard 6 checks.
  4. **Cross-Chapter Rule Conflict**: In `11_Journeys_and_Hazards.md` Line 51, Mobs testing Slink/Brains/Mouth are stated to roll `1d6`, whereas `01_Core_Resolution.md` Line 22 and `06_Mob_Mechanics.md` Line 27 establish a universal baseline of `2d6` for non-physical Mob tests.
  5. **Keyword Drift**: In `10_The_Lair_Loop_and_Progression.md` Line 326 and `11_Journeys_and_Hazards.md` Lines 118, 133, 147, the term "Wound" is used when referring to PC Goblin Boss damage, violating the strict Keyword Synonym Ban where PCs exclusively track Grit.

## 2. Logic Chain
1. *Premise 1*: Under single-source authority architecture, a core systemic rule (such as Mob non-physical skill dice pool) must be unified across all chapters.
2. *Premise 2*: In `01_Core_Resolution.md` and `06_Mob_Mechanics.md`, the authoritative baseline for a Mob's Slink, Brains, and Mouth tests is defined as `2d6`.
3. *Premise 3*: `11_Journeys_and_Hazards.md` Line 51 specifies `1d6` for Mobs in those same roles, creating a direct mechanical contradiction for players and GMs resolving travel.
4. *Premise 4*: Under the `GEMINI.md` Style Guide, player characters exclusively track **Grit**, while **Wounds** belong exclusively to Elite/Boss adversaries.
5. *Premise 5*: `10_The_Lair_Loop_and_Progression.md` Line 326 and `11_Journeys_and_Hazards.md` Lines 118, 133, 147 refer to Bosses taking "Wounds", creating terminology confusion with enemy wound tracks.
6. *Conclusion*: These specific discrepancies must be updated to achieve a 100% clean, watertight core rules release.

## 3. Caveats
- Review was conducted exclusively through static and semantic analysis of Markdown source files in `02_PROD_Core_Rules/` and cross-referenced with `STAGE_Drafts/` and `GEMINI.md`.
- No modifications were made to implementation files in `02_PROD_Core_Rules/` in accordance with the strict Review-Only constraint.

## 4. Conclusion
- **Verdict**: **REQUEST_CHANGES**
- **Action Items for Author / Synthesis Agent**:
  1. In `02_PROD_Core_Rules/11_Journeys_and_Hazards.md` Line 51, update Mob non-physical travel tests from `1d6` to `2d6` (or explicitly frame `1d6` as a -1d unled-Mob travel penalty against the baseline 2d6).
  2. In `02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md` Line 326, replace `inflicts 1 Wound on the Boss` with `inflicts 1 Grit damage on the Boss`.
  3. In `02_PROD_Core_Rules/11_Journeys_and_Hazards.md` Lines 118, 133, 147, replace `Wound` with `Grit damage` for Goblin Bosses.
  4. In `02_PROD_Core_Rules/11_Journeys_and_Hazards.md` Lines 86–98, clarify the travel encumbrance terms ("Expedition-Laden" vs "Max-Laden") to avoid semantic overlap with tactical combat "Over-Laden" definitions from Chapter 06.

## 5. Verification Method
1. Inspect `02_PROD_Core_Rules/11_Journeys_and_Hazards.md` Line 51 and confirm dice pool harmonization with `01_Core_Resolution.md` Line 22 and `06_Mob_Mechanics.md` Line 27.
2. Search for the word `Wound` across `02_PROD_Core_Rules/` to verify it is used exclusively for Elite/Boss enemy wound tracks and never applied to Goblin Bosses.
3. Review `review.md` in `.agents/r1_reviewer_2/review.md` for full stress-test analysis.
