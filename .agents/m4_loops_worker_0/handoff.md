# Handoff Report — Milestone 4 (Macro Loops & Progression)

**Agent:** Worker 4 (`m4_loops_worker_0`)  
**Assignment:** Synthesize Chapters 09, 10, and 11 in `02_PROD_Core_Rules/`  
**Handoff Type:** Hard (Task Complete)  

---

## 1. Observation

Direct file observations from the codebase, stage drafts, and synthesized production chapters:

1. **Chapter 09 (`02_PROD_Core_Rules/09_The_Raid_Loop.md`):**
   - Synthesized complete 4-Phase Raid structure (Planning & Approach, Infiltration & Assault, Objective & Plunder, Extraction & Escape) based on `01_STAGE_Drafts/00_Rules/05_Raid points.md` and `01_STAGE_Drafts/03_Loot/31_loot.md`.
   - Codified the 5-to-1 exponential Loot Value scale (T1–T5), the Rule of Five smelting/conversion rules, and Scrap generation from infrastructure dismantling (`Tough 5+/1` / `Brains 5+/1`).
   - Standardized Boss Carry capacity ($\text{Carry} = 4 + 2 \times \text{Tough}$ Bulk) and Mob carry limits ($\text{Size} \times 4$ unburdened, $\text{Size} \times 5$ dragging) along with load states (Unburdened, Over-Laden, Dragging, Immobilized) and casualty drops from `32_Carry Stuff.md`.
   - Standardized Scouting resolution on 4+ (0, 1, 2, 3+ successes) and the Alert track (1d6 vs Alert).
   - Standardized post-raid payout: Communal Glory to Shared Boss XP (0/1/2 XP), Personal Glory triggers (+1 XP), and Oddity drafting.
   - Defined Loot & Salvage Item Structural Schema, embedded `[CONTENT EXTENSION POINT: Loot & Salvage Items]`, and flagged 3 mechanical gaps:
     - `[MISSING RULE / GAP: Economy Currency Normalization & Tiered Conversion]`
     - `[MISSING RULE / GAP: Codified Extraction Phase & Chase Mechanics]`
     - `[MISSING RULE / GAP: Private Gang Hoard vs. Communal Hoard Economy]`

2. **Chapter 10 (`02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md`):**
   - Synthesized Lair Dashboard metrics: Warren Tier (1–4), Asset Capacity formula $(\text{Warren Tier} \times 2) + 2$ with over-capacity penalty (+1 Swarm Mood per excess asset per turn), Communal Hoard, Gobbo Pool (Raider Mobs vs Laborer Dice; auto-heal on $\ge 1$ HP; wiped Mobs deleted; 3d6 Communal Runts floor; Vacant Nest Growth +1d6 when $< 3\text{d}6/\text{player}$), Threat Level (0–5, Retaliatory Assault at 5), Swarm Mood (0–5, Mutiny at 5), and the Bone Pile (milestone boons every 4 skulls).
   - Codified the strict 4-Step Lair Sequence: Step 1 Homecoming & Tally, Step 2 Lair Pulse & Complications (including complete 1d66 table), Step 3 Labor Allocation (Safe 2-Dice = 1 auto success vs Risky Push 1-Die on 4+ with 6s explode and 1s injure worker for 1 turn), Step 4 Boss Downtime Actions (The Pitch `Mouth 4+/1`, Laying Low `Slink 4+/1`, Custom Crafting `Brains 4+/1`, The Skim `Slink 4+/1`, Bar Brawl `Tough/Mouth 4+/1`, Beast Taming `Brains/Tough 4+/1`).
   - Codified Modular Asset Framework (`[Person]`, `[Facility]`, `[Ally]`, `[Blueprint]`), Non-Stacking Clause, Loss of Knowledge, Dominance contribution ledger/perks, and Outposts & Macro-Territory.
   - Standardized Roguelite Generational Progression: Next Gobbo Up ($\text{Successor XP} = \text{Gang Infamy} \times 4$, cap 4 at creation), Catch-Up Boost (+2 XP on first survived raid), Inherited Gang Marks (1 Quirk/Twist inherited ignoring stat/tier gates), Named Items & Revenge Quests, Patron Saints of the Bone Pile, and Retirement to Elders at stat Level 6.
   - Defined Lair Room & Facility Structural Schema, embedded `[CONTENT EXTENSION POINT: Lair Rooms & Facilities]`, and flagged 5 mechanical gaps:
     - `[MISSING RULE / GAP: Retaliatory Lair Assault Resolution Engine]`
     - `[MISSING RULE / GAP: Mutiny Resolution Mechanics & Facility Recovery]`
     - `[MISSING RULE / GAP: Asset Decommissioning, Destruction, and Slot Recovery]`
     - `[MISSING RULE / GAP: Mid-Raid Boss Death & Successor Spawning Timing]`
     - `[MISSING RULE / GAP: Formal Patron Saint Ledger & Appeasement Trigger System]`

3. **Chapter 11 (`02_PROD_Core_Rules/11_Journeys_and_Hazards.md`):**
   - Synthesized the Journey Loop & Travel Stages (1 to 3 Stages).
   - Codified the 4 Travel Roles: Map-Scrawler (**Brains**), Sniffer (**Slink**), Scavver (**Tough**), Loud-Mouth (**Mouth**), including Mob roll rules (Tough rolls Size in d6s; Slink/Brains/Mouth roll exactly 1d6).
   - Codified Stage Resolution: Step 1 Route Test (**Brains 5+/1**; failure deals 1 Mob Attrition + Bane on Travel Event); Step 2 Travel Event (1d6 table targeting specific roles).
   - Codified Return Journey Loot Burden: Laden Mobs ($> 50\%$ carry: Bane on Slink/Tough, Route Test requires +1 success); Over-Laden Mobs (100% carry: no armor defense, auto 1 damage on failed Route Tests, discard 2 Bulk loot when fleeing or Mob becomes Uncontrolled).
   - Codified the Environmental Hazards & Zone Profiles framework: Zone Profile `Difficulty+/TN` (e.g., `4+/1`, `5+/1`, `5+/2`, `6/2`), Predefined Problems (Burning, Narrow, Slippery, Smoky, Toxic, Deep Water), and Predefined Opportunities (High Ground, Junk Pile, Shadowy, Shoring).
   - Defined Journey Hazard & Event Structural Schema, embedded `[CONTENT EXTENSION POINT: Journey Hazards & Events]`, and flagged 2 mechanical gaps:
     - `[MISSING RULE / GAP: Journey Terrain Difficulty Mapping & Transit Alert Coupling]`
     - `[MISSING RULE / GAP: Mob Attrition Damage vs. Single Health Die Tracking]`

---

## 2. Logic Chain

1. **Mechanics vs. Content Separation:** Living item lists, extensive building catalogs, and endless hazard encounters were separated from core rules. Each chapter provides the pure systemic engine rules, followed by a formal Markdown Schema and an explicit `[CONTENT EXTENSION POINT]` marker for future expansions.
2. **Zero Math Bloat:** Currency uses the 5-to-1 exponential tier ladder and token tallies rather than copper/silver/gold fractional math. Carry capacity uses simple derived Bulk thresholds ($4 + 2 \times \text{Tough}$, $\text{Size} \times 4$).
3. **De-gendering & Style Compliance:** All rules written in Tier A active present tense, addressing the reader in second-person "You" or using explicit imperative nouns ("The Goblin Boss", "The Mob", "The GM"). All dice check profiles strictly follow `[Stat] [Target Face]+/[Successes]` with no `+` on target 6.
4. **Single-Source Integrity:** Mechanics cross-reference primary definitions in `01_Core_Resolution.md`, `04_Zones_and_Movement.md`, `05_Combat_Engine.md`, and `06_Mob_Mechanics.md` without duplicating or conflicting with other chapters.
5. **Gap Traceability:** All 10 systemic gaps identified by Spec Miner 3 have been formally embedded into their respective chapters with detailed descriptions, explanations of necessity, and actionable suggested resolutions.

---

## 3. Caveats

- **No Living Content Bloat:** These chapters intentionally do not include full lists of dozens of custom weapons, oddities, room catalogs, or bestiary entries. Those are intended to plug into the provided `[CONTENT EXTENSION POINT]` blocks in modular compendiums.
- **Future Integration:** Cross-chapter links use standard markdown relative paths (`04_Zones_and_Movement.md`, `05_Combat_Engine.md`, etc.), which align with the flat layout in `02_PROD_Core_Rules/` defined in `PROJECT.md`.

---

## 4. Conclusion

Milestone 4 synthesis is complete, fully verified, and meets all requirements in `ORIGINAL_REQUEST.md`, `GEMINI.md`, `PROJECT.md`, and `spec_miner_loops_0/analysis.md`. The files are ready for final whole-book audit in Milestone 5.

---

## 5. Verification Method

To independently verify the deliverables:

1. **File Existence & Placement:**
   ```pwsh
   Test-Path c:\Users\ante\Documents\github\gobbos\02_PROD_Core_Rules\09_The_Raid_Loop.md
   Test-Path c:\Users\ante\Documents\github\gobbos\02_PROD_Core_Rules\10_The_Lair_Loop_and_Progression.md
   Test-Path c:\Users\ante\Documents\github\gobbos\02_PROD_Core_Rules\11_Journeys_and_Hazards.md
   ```
2. **Schema & Extension Point Validation:**
   - Confirm `[CONTENT EXTENSION POINT: Loot & Salvage Items]` in Chapter 09.
   - Confirm `[CONTENT EXTENSION POINT: Lair Rooms & Facilities]` in Chapter 10.
   - Confirm `[CONTENT EXTENSION POINT: Journey Hazards & Events]` in Chapter 11.
3. **Gap Marker Validation:**
   - Search for `[MISSING RULE / GAP:` across `02_PROD_Core_Rules/09_The_Raid_Loop.md`, `10_The_Lair_Loop_and_Progression.md`, and `11_Journeys_and_Hazards.md` to confirm all 10 gaps are present.
4. **Style & Notation Audit:**
   - Verify slash notation compliance (`[Stat] [Face]+/[TN]`, `6/[TN]`).
   - Verify 0 gendered pronouns and zero singular "they/their".
