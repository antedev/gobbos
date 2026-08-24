# Empirical Challenge Report — Gobbos Core Rules Synthesis

**Challenger**: Challenger 1 (`empirical_challenger`)  
**Target**: `02_PROD_Core_Rules/` (12 Chapters)  
**Date**: 2026-08-24  
**Verdict**: **CHALLENGE_DETECTED**

---

## Challenge Summary

**Overall risk assessment**: **MEDIUM**

The synthesized 12-chapter core rules in `02_PROD_Core_Rules/` represent a major systemic achievement: pure game mechanics are rigorously isolated from living content, all 32 cross-references among the 12 chapters are fully valid and unbroken, 100% of dice checks follow the strict `6` (no `6+`) notation, and all 10 content categories feature formal structural schemas and `[CONTENT EXTENSION POINT]` tags.

However, empirical scrutiny revealed **two actionable challenges** requiring remediation before full release:
1. **Keyword Synonym Ban Violations (Boss Wounds vs. Grit)**: In 4 specific instances across Chapters 10 and 11, the term "Wound" is erroneously applied to Goblin Bosses instead of "Grit" / "Damage".
2. **Missing Rule / Gap Tag Formatting & Fencing Discrepancies**: The syntax and markdown wrapping of `[MISSING RULE / GAP]` tags and `[CONTENT EXTENSION POINT]` tags vary between chapters (single callouts vs. backticks vs. multi-line code blocks in Chapters 09, 10, and 11).

---

## Challenges

### [Medium] Challenge 1: Keyword Synonym Ban Violation — Boss "Wounds" in Chapters 10 and 11

- **Assumption Challenged**: Systemic keyword consistency across all 12 core rules chapters.
- **Attack Scenario / Finding**: The system strictly mandates that Goblin Bosses track **Grit** (3 to 5 points) and *never* track Wounds (which are reserved exclusively for Elite and Boss enemy tracks, per Chapter 07 line 17: *"A Goblin Boss tracks Grit. A Goblin Boss never tracks Health or Wounds"*). However, 4 occurrences in Chapters 10 and 11 assign "Wounds" to Bosses/occupants:
  1. `11_Journeys_and_Hazards.md` (Line 118):
     `*Rule:* Test **Slink** against the **Zone Profile** or suffer **1 Wound** (Boss) / **1 Size damage** (Mob).`
  2. `11_Journeys_and_Hazards.md` (Line 133):
     `Swimming creatures must test **Tough** against the **Zone Profile** each round or begin drowning (**1 Wound** per round).`
  3. `11_Journeys_and_Hazards.md` (Line 147):
     `occupants test **Slink** against the **Zone Profile** or take **1 Wound**`
  4. `10_The_Lair_Loop_and_Progression.md` (Line 326):
     `failure inflicts 1 Wound on the Boss and increases Threat by +1 from the riot.`
- **Blast Radius**: Confuses players and GMs on whether Goblin Bosses possess a wounds track or lose Grit points from environmental hazards and downtime brawls.
- **Mitigation / Remediation**:
  - Replace `1 Wound (Boss)` in `11_Journeys_and_Hazards.md:118` with `1 Damage to Grit (Boss)`.
  - Replace `(**1 Wound** per round)` in `11_Journeys_and_Hazards.md:133` with `(**1 Damage** to Grit / lowest Mob health die per round)`.
  - Replace `or take **1 Wound**` in `11_Journeys_and_Hazards.md:147` with `or take **1 Damage**`.
  - Replace `inflicts 1 Wound on the Boss` in `10_The_Lair_Loop_and_Progression.md:326` with `inflicts 1 Damage to the Boss's Grit`.

---

### [Low] Challenge 2: Inconsistent Formatting and Code-Block Wrapping of `[MISSING RULE / GAP]` & `[CONTENT EXTENSION POINT]` Tags

- **Assumption Challenged**: Universal standardization of parser tags across all 12 chapters.
- **Attack Scenario / Finding**: The required gap tag syntax specified in R4 is:
  `[MISSING RULE / GAP: <Description of missing mechanic, why it is needed, and suggested resolution>]`
  Across the 12 files, three divergent styles were identified:
  1. **Chapters 09, 10, 11 (Fenced Code Blocks & Partial Brackets)**:
     Tags are placed inside triple backtick code fences (` ``` `), where the square brackets only enclose `[MISSING RULE / GAP: Title]`, followed by unbracketed markdown bullets (`- Description:`, `- Why it is needed:`, `- Suggested Resolution:`).
     Furthermore, `[CONTENT EXTENSION POINT: ...]` in Chapters 09, 10, 11 is also enclosed in triple backtick code blocks rather than standard markdown headers/paragraphs.
  2. **Chapters 04, 05, 06 (Inline Backticks)**:
     Tags are enclosed in markdown backticks: `` `[MISSING RULE / GAP: Title — Description, Why needed, Suggested resolution]` ``.
  3. **Chapters 01, 02, 03, 07, 08, 12 (Raw Text Bracketed Callouts)**:
     Tags are written as raw bracketed paragraphs `[MISSING RULE / GAP: ...]`. In Chapters 07 (lines 196, 198), 08 (lines 256, 258), and 12 (lines 226, 228), the text describes the resolution rule but omits the explicit tripartite labels ("Description / Why needed / Suggested Resolution").
- **Blast Radius**: Automated documentation linters and digital indexers searching for `[MISSING RULE / GAP: ...]` will fail to capture the full rationale in Chapters 09–11 due to code-fence truncation.
- **Mitigation / Remediation**: Standardize all gap tags across all 12 chapters to uniform un-fenced markdown callouts adhering to the exact syntax specification.

---

## Stress Test Results

| Test Dimension | Scope | Target Files | Expected Behavior | Actual Empirical Result | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Cross-Reference Integrity** | 32 Markdown Links | Chapters 01–12 | 100% of links resolve to existing files and valid anchors | 32 of 32 links valid and unbroken | **PASS** |
| **Living Content Separation** | Catalogs & Tables | Chapters 01–12 | No living weapon tables, grimoires, or bestiaries in core | Pure mechanics isolated; only 2–3 reference instances for schemas | **PASS** |
| **Content Schemas & Extension Points** | 10 Content Categories | Chapters 01–12 | Every category has schema template and extension point tag | 10 of 10 schemas and extension points present | **PASS** |
| **Dice Notation Compliance** | `6` vs `6+` Hard Check | Chapters 01–12 | 0 instances of `6+` for Hard difficulty | 0 illegal instances found (1 rule-explanation instance in 01:40) | **PASS** |
| **Gender-Neutral Mandate** | Pronoun Scan | Chapters 01–12 | 0 instances of gendered pronouns (he/him/his/she/her) | 0 instances found in all 12 synthesized chapters | **PASS** |
| **Header Hierarchy** | Heading Levels | Chapters 01–12 | Strict H1 -> H2 -> H3 with zero skips | 0 heading skips found across all 12 files | **PASS** |
| **Keyword Constancy** | Grit vs Wounds | Chapters 01–12 | Bosses track only Grit; never Wounds | 4 instances of "Wounds" applied to Bosses in Chapters 10 & 11 | **FAIL** |
| **Gap Tag Syntax Consistency** | Gap Callouts | Chapters 01–12 | Uniform standardized single-string bracketed callouts | 3 divergent syntax styles (code fences, backticks, raw callouts) | **FAIL** |

---

## Unchallenged Areas

- **System_Tools / Combat Sim Python codebase**: Out of scope for Core Rules Synthesis challenge (verified under separate tooling tracks).
- **Subdirectories `00_Rules/` and `01_Characters & Mobs/` in `02_PROD_Core_Rules/`**: Identified as legacy staging residue from earlier iterations; not referenced by the 12 active chapters, but recommended for clean removal or archiving to prevent workspace clutter.
