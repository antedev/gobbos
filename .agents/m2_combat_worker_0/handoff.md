# Handoff Report — Worker 2 (Tactical & Combat Engine Synthesis)

## 1. Observation

- **Inputs Inspected:**
  - `c:\Users\ante\Documents\github\gobbos\GEMINI.md`: Strict style guide rules for Tier A mechanical definitions, zero math bloat, total de-gendering, slash notation `[Stat] [Face]+/[TN]`, golden rules `>>`, and strict keyword constancy (**Grit** for PCs, **Wounds** for Elite/Boss NPCs, **Health / Health Dice** for Mobs, **Loot** for currency/treasure).
  - `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\analysis.md`: Mined systemic mechanics for spatial topology, Zone Profiles, movement/disengage costs, combat attack pipelines, Overkill rule, Impact Size Stagger calculations, Clatter defense, and formal schemas.
  - `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\analysis.md`: Mined systemic mechanics for Mob anatomy, Size 1–5 scaling, Health Dice pools starting at face 6, Frontline Rule for Mob-on-Mob clashes, Cleave X and AoE damage resolution, Boss command distance matrices, Loitering/Out of Control behavior tables, Scatter reactions and Gambles, Swarm Terror morale checks, Cross-Gang Super-Mobs, and Mob sacrifice maneuvers.
  - `01_STAGE_Drafts/00_Rules/02 Combat.md`, `03_Movement & Zones.md`, `04_Giving orders.md`, `01_Characters & Mobs/13_Goblin_mob.md`, and `03_Loot/33_Equipment.md`.

- **Outputs Written (Exclusive Write Ownership):**
  - `02_PROD_Core_Rules/04_Zones_and_Movement.md` (268 lines, 14.2 KB)
  - `02_PROD_Core_Rules/05_Combat_Engine.md` (302 lines, 16.5 KB)
  - `02_PROD_Core_Rules/06_Mob_Mechanics.md` (254 lines, 14.8 KB)

---

## 2. Logic Chain

1. **Decoupling Living Content from Systemic Rules:**
   - In accordance with R1 in `PROJECT.md` and `ORIGINAL_REQUEST.md`, all specific weapon catalogs, equipment listings, armor shop tables, and monster statblocks were stripped from the rules chapters and replaced with rigorous, standardized Markdown Schemas and explicit `[CONTENT EXTENSION POINT]` hooks (`[CONTENT EXTENSION POINT: Weapons]`, `[CONTENT EXTENSION POINT: Armor & Shields]`, `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`).

2. **Unified Tactical Spatial Engine (`04_Zones_and_Movement.md`):**
   - Codified Zone topology as an abstract node graph with shortest-path integer distance.
   - Authoritatively established the universal Zone Profile Rule: all unlisted physical traversal, jumps, climbs, searches, and manipulations test against the active Zone Profile (`Difficulty+/TN`).
   - Codified movement action rates, Disengage tests (`Slink 5+/Highest Defence TN`), Opportunity Attack mechanics, Partial vs Full Cover, and standardized modular traits/hazards (T1–T3 scaling).
   - Codified background unsupervised Mob resolution via the Chaos Tick and the Gobbo Mischief Table.

3. **Deterministic Combat Engine (`05_Combat_Engine.md`):**
   - Established the single-source Attack Pipeline: Melee (`Tough`) and Ranged (`Slink`) vs static target Defence TN.
   - Formalized Minion One-Hit Kills and the Elite/Boss Overkill rule ($\lfloor \text{Successes} / \text{Defence TN} \rfloor$ Wounds).
   - Formulated the exact Impact Size calculation ($\text{Base Size} + \text{Weapon Modifiers}$) and Mass Resistance Stagger threshold.
   - Formalized the Clatter Defense Roll (simultaneous throw of active Stat Dice and passive Armor Dice vs Threat TN) with the 5d6 mitigation ceiling and Ablative Gear Sacrifice rule.
   - Formalized Group Attacks (swarming up to 3 enemies into 1 attack) and Flanking boons.

4. **Dynamic Swarm Engine (`06_Mob_Mechanics.md`):**
   - Defined Mob anatomy and Size metrics (Size 1–5, Combat Dice = Size, Required Grunt, Loot Capacity = Size x 4 Bulk).
   - Structured physical table tracking using d6 pools starting at face 6.
   - Codified all four damage resolution modes: Single-target decrement with spillover, the Frontline Rule ($\min(\text{Atk Size}, \text{Def Size})$ lowest dice engaged), `Cleave X`, and True AoE across all active dice.
   - Codified Boss command flow, distance difficulty scaling, Free Orders, and the Boredom Rule.
   - Codified the complete Loitering (1 action spent, 1 saved) and Out of Control (2 actions spent, 0 saved) behavior tables and Rallying checks.
   - Formalized the Mob Scatter reaction with the high-stakes Scatter Gamble consequences.
   - Codified 50% casualty Swarm Terror Morale checks, Cross-Gang Super-Mobs, and five official Mob Sacrifice Maneuvers.

5. **Exhaustive Gap Cataloging:**
   - Identified, documented, and highlighted 6 mechanical edge cases across the three chapters using standardized `[MISSING RULE / GAP: ...]` callouts.

---

## 3. Caveats

- **Upstream Attributes & Actions:** Secondary stats (Grit, Movement, Carry, Max Mobs, Free Orders) and base action economies (3 Standard Actions + 1 Free Order for Bosses; 2 Actions for Mobs) are defined in Chapters 02 (`02_Boss_Profile_and_Gang.md`) and 03 (`03_Action_Economy_and_Turn_Flow.md`) synthesized by Worker 1. Chapters 04, 05, and 06 reference these definitions without re-inventing conflicting rules.
- **Downstream Damage & Threat Profiles:** Grit reduction, Wounds tracking, Conditions matrices, and deterministic enemy statblocks are expanded in Chapters 07 (`07_Damage_Grit_and_Wounds.md`) and 12 (`12_Adversaries_and_Threats.md`) synthesized by Worker 3.

---

## 4. Conclusion

Milestone 2 synthesis for Worker 2 is 100% complete. Chapters `04_Zones_and_Movement.md`, `05_Combat_Engine.md`, and `06_Mob_Mechanics.md` have been authored in `02_PROD_Core_Rules/` with full mechanical rigor, zero living content bloat, standardized extension schemas, and strict compliance with `GEMINI.md` styling and keyword constancy.

---

## 5. Verification Method

To independently verify the synthesized rules:

1. **File Existence & Integrity Check:**
   - Verify `02_PROD_Core_Rules/04_Zones_and_Movement.md` exists and contains Zone Topology, Zone Profiles, Movement, Cover, Traits, Blueprints, and Chaos Tick.
   - Verify `02_PROD_Core_Rules/05_Combat_Engine.md` exists and contains Melee/Ranged attacks, Overkill rule, Impact Size/Stagger, Weapon traits/schema, Armor/Shield traits/schema, Gear schema, Clatter Roll, and Group Attacks.
   - Verify `02_PROD_Core_Rules/06_Mob_Mechanics.md` exists and contains Mob Anatomy, Health Dice pools, Frontline Rule, Cleave/AoE damage, Boss Orders, Boredom Rule, Loitering/Out of Control tables, Scatter reactions, Swarm Terror morale, Merging/Splitting, and Sacrifice maneuvers.

2. **Style & Linguistic Audit:**
   - Inspect files for total de-gendering ("You", "Your", "The Goblin Boss", "The Mob", "The GM").
   - Confirm all dice notation uses strict slash format `[Stat] [Face]+/[TN]` with zero `6+` instances.
   - Confirm strict keyword constancy: **Grit** (PCs), **Wounds** (Elites), **Health / Health Dice** (Mobs), **Loot** (treasure).
   - Confirm all headers strictly follow H1 -> H2 -> H3 with zero skips.

3. **Content Extension Point & Gap Audit:**
   - Confirm presence of `[CONTENT EXTENSION POINT: Weapons]`, `[CONTENT EXTENSION POINT: Armor & Shields]`, and `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`.
   - Confirm all 6 `[MISSING RULE / GAP: ...]` tags are properly formatted with descriptions and suggested resolutions.
