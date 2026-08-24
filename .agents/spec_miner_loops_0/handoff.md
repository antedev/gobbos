# Handoff Report: Spec Miner 3 (Loops, Progression, Lair, Journeys & Economy)

**Type:** Hard Handoff  
**Agent:** Spec Miner 3 (`spec_miner_loops_0`)  
**Target:** Parent Orchestrator / Lead Synthesizer  
**Date:** 2026-08-24T17:41:00Z  

---

## 1. Observation

Direct observations extracted from authoritative source files across `01_STAGE_Drafts/`, `02_PROD_Core_Rules/`, and `00_DEV_Brainstorms/`:

1. **Raid Economy & Plunder Scaling (`31_loot.md` lines 11–30, 55–64):**
   > "Every piece of treasure belongs to a Quality Tier (T1–T5) and has a Loot Value (LV) expressed in units of that Tier (e.g., 1x T2, 3x T3, 10x T5)... Each Tier represents a direct 5-to-1 step in concentrated worth... Smelting 5x T2 silver goblets produces 1x T3 gold ingot."
2. **Carry Limits & Tactical Encumbrance (`32_Carry Stuff.md` lines 9–36):**
   > "Your baseline Carry capacity is 4 + (2 x Tough) Bulk... Unburdened: Less than or equal to Carry... Over-Laden: Carry + 1 to Carry + Tough (-1 Zone per Move action, Bane 1 on Slink/Tough)... Dragging: Carry + Tough + 1 to 2x Carry (Fixed 1 Zone, requires both hands, 0 active defense)... Mob Limit: Size x 4 Bulk unburdened; Size x 5 Dragging."
3. **Lair Dashboard & Asset Capacity (`00_Lair_Rules.md` lines 33–42, 48–57):**
   > "A Lair can only maintain a maximum number of Active Assets equal to (Warren Tier × 2) + 2. If the Lair exceeds this limit... Swarm Mood increases by +1 at the start of every Lair Turn for each asset over the cap... The Lair's population is tracked as a single communal dice pool: The Gobbo Pool (measured in d6s)... divided into Raider Mobs and Laborer Dice."
4. **Lair Phase Sequence & Labor Resolution (`00_Lair_Rules.md` lines 80–136):**
   > Four-step sequence: Step 1: Homecoming & Tally; Step 2: The Lair Pulse & Complications; Step 3: Labor Allocation & Operations (Safe 2-Dice = 1 auto success vs. Risky Push 1-Die rolling 4+ with 1s injuring worker); Step 4: Boss Downtime Actions (The Pitch, Laying Low, Custom Crafting, The Skim, Bar Brawl, Beast Taming).
5. **Roguelite Death & Successor Mechanics (`15_Level_Up and death.md` lines 3–16; `12_Gang.md` lines 19–45):**
   > "The successor Boss B starts with Level 1 in all stats, gets 2 starting advances... and receives a starting pool of Successor XP equal to Gang Infamy × 4 to spend on buying stats... no Main Stat can be raised above Level 4 at successor creation... Catch-Up Boost: +2 bonus XP on their first raid... Gang Marks: Successor immediately starts with one Quirk or Twist that the deceased Boss possessed (ignoring stat requirements)."
6. **Journey Mechanics & Roles (`00_Journey_Rules.md` lines 9–60):**
   > Four Travel Roles: Map-Scrawler (Brains), Sniffer (Slink), Scavver (Tough), Loud-Mouth (Mouth). Route Test: Map-Scrawler rolls Brains 5+/1 (Failure: 1 Attrition damage to all Mobs + Bane on Travel Event). Travel Event: GM rolls 1d6 targeting one of the other three roles.
7. **Zone Profiles & Environmental Traits (`GDR-006` lines 23–83):**
   > Every Zone has a Zone Profile (`Difficulty+/TN`). Traits are categorized into Problems (Hazards/Obstacles e.g. Burning, Narrow, Slippery, Smoky, Toxic, Deep Water) and Opportunities (High Ground, Junk Pile, Shadowy, Shoring). Players make saving throws against the Zone Profile; the GM never rolls dice.

---

## 2. Logic Chain

1. **Extraction of Pure Mechanics:** By comparing `01_STAGE_Drafts/` against `GEMINI.md` and `ORIGINAL_REQUEST.md`, all pure game engines were isolated from exhaustive catalog content:
   - The 4-Phase Raid Loop and exponential 5-to-1 Loot Value ladder.
   - The 4-Step Lair Phase and modular Asset lifecycle ([Person], [Facility], [Ally], [Blueprint]).
   - The 4-Role Journey resolution loop and Zone Profile environmental engine.
   - The Roguelite generational progression loop (Infamy, Successor XP multiplier `Infamy * 4`, Gang Marks, Bone Pile, Patron Saints, Elders).
2. **Content Separation into Structural Schemas:** All living content tables (room directories, loot catalogs, travel encounter tables) were successfully abstracted into three formal Markdown Schemas:
   - **Lair Room / Asset Schema** (Category, Tier, Cost, Prerequisites, Upkeep, Boon, Active Function, Volatility/Catch, Dominance Kickback, Upgrade Tiers).
   - **Loot Item / Salvage Schema** (Category, Tier, Bulk, Loot Value, Scrap Yield, Divisibility, Special Utility/Crafting Tag).
   - **Journey Hazard / Event Schema** (Hazard Type, Terrain Tag, Target Role, Trigger, Check & Difficulty, Failure Consequence, Success Outcome, Mitigating Action).
3. **Identification of Mechanical Gaps:** Cross-auditing the files revealed 10 concrete systemic gaps and currency ambiguities:
   - Currency tier mismatch between 5-to-1 exponential Loot Tiers (`31_loot.md`) and flat integer costs in Lair rules (`00_Lair_Rules.md`) and Infamy Mark generation (`12_Gang.md`).
   - Undefined resolution and failure consequences for Threat Level 5 Retaliatory Assaults.
   - Undefined suppression mechanisms for Swarm Mood 5 Mutiny.
   - Lack of asset demolition / slot recovery rules.
   - Ambiguity surrounding mid-raid Boss death and runt promotion timing.
   - Lack of codified Extraction/Chase mechanics between plunder and return journeys.
   - Missing criteria and appeasement tracking for Patron Saints.
   - Unscaled Journey route difficulties and lack of transit-to-raid Alert coupling.
   - Undefined spending mechanics for Gang Private Hoards vs. Communal Hoards.
   - Ambiguity regarding Mob Attrition damage distribution across health dice pools.

---

## 3. Caveats

- **No Living Content Implementation:** Per instructions, this report abstracts living content tables into schemas and pure systemic rules; specific room lists, item compendiums, and bestiaries are deliberately omitted.
- **Synthesizer Authority on Currency Normalization:** A specific formula for normalizing flat Lair costs to T1 Base Loot / Scrap was proposed in `analysis.md`, but the lead synthesizer/orchestrator retains authority on exact numeric balancing.

---

## 4. Conclusion

The specification mining for Domain 1 (The Raid Loop & Economy), Domain 2 (The Lair Loop & Roguelite Progression), and Domain 3 (Journeys & Hazard Resolution) is complete, comprehensive, and fully documented in `analysis.md`. The domain is ready for immediate modular synthesis into `02_PROD_Core_Rules/`.

---

## 5. Verification Method

To independently verify the findings in this report:
1. **Inspect Analysis Report:** View `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_loops_0\analysis.md` to review the full feature matrix, edge cases, systemic mechanics extractions, 3 content schemas, and 10 gap analyses.
2. **Cross-Check Source References:**
   - Verify 5-to-1 Loot Value and Rule of Five in `01_STAGE_Drafts/03_Loot/31_loot.md`.
   - Verify Carry capacity formulas and Bulk 3+ item rules in `01_STAGE_Drafts/03_Loot/32_Carry Stuff.md`.
   - Verify Lair Dashboard, Gobbo Pool, and 4-Step sequence in `01_STAGE_Drafts/05_Base/00_Lair_Rules.md`.
   - Verify Successor XP formula (`Infamy * 4`), Gang Marks, and Bone Pile in `01_STAGE_Drafts/01_Characters & Mobs/15_Level_Up and death.md` and `12_Gang.md`.
   - Verify Travel Roles, Route Tests, and Return Loot Weight in `01_STAGE_Drafts/07_Travel/00_Journey_Rules.md`.
   - Verify Zone Profiles and Environmental Traits in `00_DEV_Brainstorms/GDRs/GDR-006_Environmental_Hazards_and_Zone_Statblocks.md`.
