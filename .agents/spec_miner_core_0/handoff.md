# 5-Component Handoff Report: Gobbos Core Rules Specification Mining (Domains 1–5)

**Agent**: Spec Miner Core 0 (`.agents/spec_miner_core_0/`)  
**Recipient**: Parent / Lead Architect (`5c381523-2834-4186-bdde-fd176f430709`)  
**Type**: Hard Handoff (Task Complete)  
**Date**: 2026-08-24  

---

## 1. Observation

Direct examination of the authoritative rules repositories (`01_STAGE_Drafts/00_Rules/`, `01_STAGE_Drafts/01_Characters & Mobs/`, `01_STAGE_Drafts/03_Loot/`, `01_STAGE_Drafts/04_Enemies/`, `02_PROD_Core_Rules/00_Rules/`, and `02_PROD_Core_Rules/01_Characters & Mobs/`) revealed the following concrete systemic facts and verbatim passages:

1. **Dice Pool & Resolution Engine (`PROD 01_Dice.md:7-49`, `STAGE 01_Dice.md:7-62`)**:
   - `PROD 01_Dice.md:13`: *"For an Easy roll, a 4, 5, or 6 is a Success. For a Normal roll, a 5 or 6 is a Success. For a Hard roll, only 6s are a Success."*
   - `PROD 01_Dice.md:35`: *"Every time you roll a 6, it is not only a Success but it allows you to roll an additional die."*
   - `STAGE 01_Dice.md:39-44`: *"If penalties, conditions, or Banes reduce your Dice Pool to 0d6 or less, the test automatically fails by default. However... You still roll a single 1d6 as a Salvage Roll: Roll a 6: The action is miraculously salvaged... Roll a 1: A catastrophic failure occurs—you immediately suffer a Fumble and lose 1 Grunt..."*
   - `PROD 01_Dice.md:45-50`: Gobbo Gamble pushes failed rolls with 1s; re-failing causes -1 Grunt.
   - `PROD 01_Dice.md:80-97`: Bangaranga pool seeding, draw limits up to Grunt, Tax of 1 die if draw $>$ TN, and Double Explosion on 6s.

2. **Attributes & Boss/Gang Model (`PROD 10_Stats.md:1-130`, `STAGE 11_Character Creation.md:1-109`, `STAGE 12_Gang.md:1-115`)**:
   - `PROD 10_Stats.md:3`: Four Main Stats (Tough, Slink, Mouth, Brains) scaling Level 1 to 5.
   - `PROD 10_Stats.md:105`: *"Grunt is equal to your second highest Main Stat."*
   - `STAGE 11_Character Creation.md:23-39`: Base 1s in all stats + 2 starting points (max 3 at creation); specialist (3,1,1,1) vs generalist (2,2,1,1).
   - `STAGE 12_Gang.md:40`: Successor Bosses receive $\text{Infamy} \times 4$ Successor XP and inherit 1 Gang Mark (Quirk tattoo).

3. **Action Economy & Turn Flow (`STAGE 02 Combat.md:7-12`, `STAGE 02 Combat.md:90-138`)**:
   - `STAGE 02 Combat.md:7`: *"Every PC has three (3) Standard Actions per round, reset at the start of each round... Additionally, PCs have one (1) Free Order Action per round..."*
   - `STAGE 02 Combat.md:12`: *"Each Mob has two (2) actions, which are also reset at the start of each round, but they only act when Ordered."*
   - `STAGE 02 Combat.md:77`: *"The Boredom Rule: ...a Mob cannot perform the exact same action twice (e.g., they cannot Attack twice, or Plunder twice). Exception: A Mob can take the Move action twice if they are fleeing or charging."*
   - `STAGE 02 Combat.md:90-97`: 5-Phase combat loop (Setup, Round start, Players active turn, Enemy active turn, Round closure, Combat End).

4. **Zones & Environment (`STAGE 03_Movement & Zones.md:72-202`)**:
   - `STAGE 03_Movement & Zones.md:83-88`: Zone Profile Rule sets default `Difficulty+/TN` for all unlisted physical/traversal tests in a zone.
   - `STAGE 03_Movement & Zones.md:121-202`: Standardized modular traits defined (Slippery, Rubble, Narrow, Chasm, Vertical Cliff, Deep Water, Burning, Crumbling Ceiling, Toxic Spores, Quicksand, Howling Wind, Pillars, Shoring).
   - `STAGE 03_Movement & Zones.md:244-268`: Background node resolution via the Chaos Tick and Gobbo Mischief Table (tally of 1s).

5. **Combat Engine & Defense (`STAGE 02 Combat.md:17-64`, `STAGE 20_Enemies.md:105-120`, `STAGE 33_Equipment.md:75-125`)**:
   - `STAGE 02 Combat.md:20-25`: One-Hit Kill on Standard enemies, Overkill on Elites ($\lfloor \text{Successes}/\text{Defence TN} \rfloor$ Wounds), Frontline Rule on Mobs.
   - `STAGE 02 Combat.md:25-32`, `STAGE 20_Enemies.md:114-120`: Stagger calculation via $\text{Impact Size} \ge \text{Target Physical Size}$ on partial hits ($\ge 1$ success).
   - `STAGE 02 Combat.md:38-47`: Clatter Roll resolves simultaneous Active Stat Dice (Slink Dodge / Tough Parry) + Passive Armor Dice.
   - `STAGE 33_Equipment.md:118`: Shields grant +1d Armor Die AND enable Tough Parry reaction.
   - `STAGE 33_Equipment.md:120-125`: Ablative Shield/Armor Sacrifice cancels lethal damage.
   - `STAGE 02 Combat.md:48-58`: Mob Scatter Reaction (`Mouth vs Threat TN + Size penalty`) and high-stakes Scatter Gamble consequences.

6. **Notational & Mechanical Conflicts Identified**:
   - `STAGE 11_Character Creation.md:93-95` lists starting weapons with `+2d damage`, `+3d damage`, `+4d damage`, directly contradicting the core engine in `STAGE 02 Combat.md` and `STAGE 33_Equipment.md:16` (*"GOLDEN RULE: No Math Bloat"* and flat 1 damage/Wound scaling).
   - No formal dual-wielding rules exist despite `STAGE 11_Character Creation.md:47` giving "Two Light Melee Weapons" to Raiders.
   - No ammunition depletion or tracking mechanics exist for non-sling ranged weapons.
   - No explicit cap on stacked passive armor mitigation dice exists.

---

## 2. Logic Chain

1. **From Core Resolution & Style Guide to Engine Rules**:
   - `GEMINI.md` mandates zero post-roll math and pure D6 pools. All tests resolve strictly by comparing rolled faces against Difficulty thresholds (4+, 5+, 6) and counting successes against static Target Numbers (TN).
   - The existence of Exploding 6s, Critical double-explosions, Salvage 1d6 rolls on $\le 0$ pools, Gobbo Gambles on 1s, and Bangaranga hype pools forms a complete, closed-form dice engine without requiring any GM-side dice rolling.

2. **From Entity Models to Action Budgets**:
   - Boss entities are defined by 4 Main Stats (T, S, M, B) scaling 1–5, with Max Grunt derived from the second-highest stat.
   - The action economy strictly balances 3 Standard Actions + 1 Free Order for Bosses against 2 Actions for Mobs (governed by the Boredom Rule and Command limits).
   - Mobs without orders deterministically branch into Loitering (1 action used, 1 saved for 1d6 Defence) or Out of Control (2 actions running amok, 0 saved).

3. **From Spatial Abstraction to Tactical Topologies**:
   - The Zone Profile rule (`Difficulty+/TN`) provides a universal resolution hook for all environmental interactions, eliminating arbitrary GM target numbers.
   - Cover operates as a clean Boon/Bane modifier (Partial: +1d Dodge / -1d Attack; Full: line of sight blocked), integrating seamlessly with the Boon/Bane net cap rule.

4. **From Combat Interactions to Defense & Stagger**:
   - The Clatter Roll elegantly unifies active evasion (Stat dice meeting Threat TN) and passive mitigation (Armor dice successes reducing damage) into a single roll.
   - The Impact Size vs Target Size formula provides a robust, non-math-heavy gate for the Staggered condition, allowing heavy weapons and explosives to physically disrupt larger foes while preserving monster mass resistance.

5. **From Content Separation to Modular Schemas**:
   - Living weapon catalogs, armor listings, tool tables, and quirk compendiums were successfully stripped from the core mechanics and modeled as extensible Markdown Schemas with standardized `[CONTENT EXTENSION POINT]` hooks.

---

## 3. Caveats

1. **Magic & Bangaranga High Spells**: Magic tag synthesis and Power Word casting parameters interface with Brains and the Bangaranga pool, but the exhaustive Power Word lexicon belongs to Domain 8 (Magic).
2. **Enemy Bestiary & Specific Trait Catalogs**: The deterministic threat framework and enemy scales are fully documented, but individual monster statblocks belong to Domain 6 (Bestiary).
3. **Lair Smelting & Economy Math**: Gang Infamy milestones and Successor XP formulas are established, but specific Lair Room construction costs belong to Domain 10 (The Lair).

---

## 4. Conclusion

The specification mining for Domains 1 through 5 is complete, comprehensive, and fully documented in `analysis.md`.
- **Systemic Purity**: All core mechanics are isolated from living catalogs.
- **Extensible Architecture**: 4 formal Content Schemas (Weapons, Armor/Shields, Gear/Tools, Boss Quirks) are designed and ready for compendium modularization.
- **Actionable Gap Remediation**: 10 distinct mechanical gaps and notation discrepancies have been formally cataloged with `[MISSING RULE / GAP]` tags and recommended systemic resolutions.

---

## 5. Verification Method

To independently verify all findings and validate the analysis:

1. **Verify Extracted Mechanics & Rules Purity**:
   - Inspect `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\analysis.md` across Sections 1 to 6.
   - Confirm all 5 assigned domains are fully addressed without embedding living item/quirk catalogs.

2. **Verify Schema & Extension Points**:
   - Review Section 3 of `analysis.md` to confirm the presence and field completeness of:
     - Weapon Schema
     - Armor & Shield Schema
     - Gear & Tools Schema
     - Boss Quirk Schema

3. **Verify Gap Callout Syntax**:
   - Search `analysis.md` for `[MISSING RULE / GAP:` to confirm all 10 identified gaps match the required format: `[MISSING RULE / GAP: <Description, why needed, suggested resolution>]`.

4. **Verify Style Guide Adherence**:
   - Check that all dice test shorthand strictly adheres to `GEMINI.md` (`5+/1`, `4+/2`, `6/1` without `6+`).
   - Check that character terminology strictly uses Goblin Boss, Mob, Grit, Grunt, and Loot without banned synonyms.
