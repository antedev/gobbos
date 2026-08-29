# STAGE vs. PROD Comprehensive Gap & Mechanics Audit

*This document serves as the master ledger comparing all legacy and active STAGE draft mechanics against the finalized `02_PROD_Core_Rules/` engine. It details what has been fully codified, what content is queued for modernization, and specific standalone mechanics awaiting review.*

---

## Executive Summary

* **`02_PROD_Core_Rules/` (Chapters 01–12):** Contains the complete, unified **System Engine** (Action Economy, Resolution, Combat, Mobs, Damage/Grit, Magic/Bangaranga, Raid Loop, Lair Loop, Journeys, and Adversaries).
* **`01_STAGE_Drafts/`:** Has been cleaned of redundant engine drafts. It now houses the **4 Content Compendium Queues** (Character Options, Equipment & Crafting, Bestiary & Threats, Tags & Keywords).
* **`03_Archive_Graveyard/Legacy_Engine_Drafts/`:** Stores all superseded legacy drafts for historical reference.

---

## Master Inventory & Status Matrix

| STAGE Source File | System Topic | Status vs. PROD | Key Elements / Action Required |
| :--- | :--- | :---: | :--- |
| `00_Rules/00_Overview.md` | Core Overview | **Superseded** | Fully codified in `01_Core_Resolution.md` and `PROJECT.md`. Archived. |
| `00_Rules/01_Dice.md` | Dice Pool & Math | **Superseded** | Fully codified in `01_Core_Resolution.md` (GM never rolls, slash notation, explosions). Archived. |
| `00_Rules/02 Combat.md` | Combat System | **Superseded** | Fully codified in `03_Action_Economy_and_Turn_Flow.md` & `05_Combat_Engine.md`. Archived. |
| `00_Rules/03_Movement & Zones.md` | Zones & Movement | **Superseded** | Fully codified in `04_Zones_and_Movement.md`. Archived. |
| `00_Rules/04_Giving orders.md` | Mob Commands | **Superseded** | Fully codified in `03_Action_Economy_and_Turn_Flow.md` & `06_Mob_Mechanics.md`. Archived. |
| `00_Rules/05_Raid points.md` | Glory & Loot Value | **Superseded** | Fully codified in `09_The_Raid_Loop.md` & `10_The_Lair_Loop_and_Progression.md`. Archived. |
| `00_Rules/07_Wounds_Conditions.md` | Conditions & Grit | **Superseded** | Fully codified in `07_Damage_Grit_and_Wounds.md`. Archived. |
| `01_Characters/10_Stats.md` | Attributes & Grunt | **Superseded** | Fully codified in `02_Boss_Profile_and_Gang.md`. Archived. |
| `01_Characters/12_Gang.md` | Gang Archetype | **Superseded** | Fully codified in `02_Boss_Profile_and_Gang.md` & `10_The_Lair_Loop_and_Progression.md`. Archived. |
| `01_Characters/13_Boons_and_Banes.md` | Boons/Banes | **Superseded** | Fully codified in `01_Core_Resolution.md`. Archived. |
| `01_Characters/13_Goblin_mob.md` | Mob Health Dice | **Superseded** | Fully codified in `06_Mob_Mechanics.md`. Archived. |
| `01_Characters/15_Level_Up.md` | Progression & Death | **Superseded** | Fully codified in `02_Boss_Profile_and_Gang.md`, `07_Damage_Grit_and_Wounds.md`, `10_The_Lair_Loop_and_Progression.md`. Archived. |
| `03_Loot/31_loot.md` | Exponential Tiers | **Superseded** | Fully codified in `09_The_Raid_Loop.md` & `10_The_Lair_Loop_and_Progression.md`. Archived. |
| `03_Loot/32_Carry Stuff.md` | Carry & Bulk | **Superseded** | Fully codified in `02_Boss_Profile_and_Gang.md` & `04_Zones_and_Movement.md`. Archived. |
| `03_Loot/33_Equipment.md` | Base Weapons/Armor | **Superseded** | Fully codified in `02_Boss_Profile_and_Gang.md` & `05_Combat_Engine.md`. Archived. |
| `04_Enemies/20_Enemies.md` | Threat Framework | **Superseded** | Fully codified in `12_Adversaries_and_Threats.md`. Archived. |
| `05_Base/00_Lair_Rules.md` | Lair Dashboard | **Superseded** | Fully codified in `10_The_Lair_Loop_and_Progression.md`. Archived. |
| `07_Travel/00_Journey_Rules.md` | Travel Loop | **Superseded** | Fully codified in `11_Journeys_and_Hazards.md`. Archived. |
| `08_Magic/00_Magic_Rules.md` | Farkle Magic Loop | **Superseded** | Fully codified in `08_Magic_and_Bangaranga.md`. Archived. |
| **`01_Character_Options/11_Character_Creation.md`** | Character Creation | **Active STAGE Queue** | Contains the **Insta-Gobbo Table** and **Gang Shenanigans** not in PROD. |
| **`01_Character_Options/11a_Roles.md`** | The 16 Roles Matrix | **Active STAGE Queue** | Contains full Level 2–5 skills for all 16 Specialist/Hybrid roles. |
| `01_Character_Options/14_Feats.md` | Feats & Twists | **Active STAGE Queue** | Contains starting feat atoms, twist rules, and tier gating. |
| `01_Character_Options/16_Unified_Modular_Powers_System.md` | Modular Powers Toolkit | **Active STAGE Queue** | The 6-category engine unifying feats, shenanigans, components, and spells. |
| **`02_Equipment_and_Crafting/34_Crafting.md`** | Component Crafting Engine | **PROD Promoted** | Fully audited and codified in `02_PROD_Core_Rules/13_Equipment_and_Crafting.md`. |
| **`02_Equipment_and_Crafting/35_Equipment_Catalogue.md`** | Equipment & Plunder | **PROD Promoted** | Fully audited and codified in `02_PROD_Core_Rules/13_Equipment_and_Crafting.md`. |
| `03_Bestiary_and_Threats/21_Bestiary.md` | Monster Statblocks | **Active STAGE Queue** | Full bestiary of beasts, town guards, undead, monstrosities, fiends. |
| `04_Tags_and_Keywords/06_Keywords_Index.md` | Master Terminology | **Active STAGE Queue** | Master system glossary for quick in-game cross-referencing. |
| `04_Tags_and_Keywords/08_Master_Tag_Index.md` | Tags & Synthesis | **Active STAGE Queue** | Master elemental dictionary and chemical synthesis combinations. |

---

## Specific Mechanics & Features Not Covered in PROD (For Future Review)

The following specific rules exist in STAGE drafts but are not yet included or formalized in `02_PROD_Core_Rules/`. These are candidates for review to decide whether they should be promoted into PROD Compendiums or retired:

### 1. Gang Shenanigans (Culture & Compulsions)
* **Source:** `01_STAGE_Drafts/01_Character_Options/11_Character_Creation.md`
* **Mechanic:** At Gang creation, players choose a **Shenanigan Tag** (e.g. *Pyromaniacs, Shiny-Snatchers, Trap-Fiddlers*). It provides both a mechanical Boon during relevant tasks and a chaotic table compulsion.
* **PROD Status:** `02_Boss_Profile_and_Gang.md` establishes the Gang as archetype and Infamy, but omitted the Shenanigans mechanic.
* **Recommendation:** Include in the upcoming `Character_Creation_and_Roles.md` compendium.

### 2. The Insta-Gobbo 1d6 Quick-Start Table
* **Source:** `01_STAGE_Drafts/01_Character_Options/11_Character_Creation.md`
* **Mechanic:** A 1d6 roll table allowing a player whose Boss just died to generate an instant replacement Boss with pre-configured stats, role, feat, and loadout in under 30 seconds.
* **PROD Status:** Not in PROD.
* **Recommendation:** Include in the character creation section of PROD Compendiums.

### 3. The 16 Roles Scaling Skill Tree (Levels 2–5)
* **Source:** `01_STAGE_Drafts/01_Character_Options/11a_Roles.md`
* **Mechanic:** The complete matrix of 16 roles (4 Specialists: *Meat-Wall, Shadow-Lurker, Ring-Leader, Sage-Tinker*; 12 Hybrids: *Raider, Enforcer, Iron-Tinker, Scavenger, Saboteur, Skirmisher, Dread-Boss, Swarm-Caller, Chant-Monger, Mad-Alchemist, Trap-Weaver, Run-Master*) with free scaling role skills from Level 2 to Level 5.
* **PROD Status:** PROD 02 mentions the role names as examples, but does not contain the skill tree.
* **Recommendation:** Modernize to standard Slash Notation and publish as `02_PROD_Core_Rules/Compendiums/Roles_and_Quirks.md`.

### 4. Component Bite Rating (F0–F3) & Stability
* **Source:** `01_STAGE_Drafts/02_Equipment_and_Crafting/34_Crafting.md`
* **Mechanic:** Components attached to custom gear possess a **Tier (T1–T5)** and a **Flaw (F0–F3)** rating. Higher bite means greater drawback/instability (F0 = Pure, F1 = Irritating, F2 = Painful/Grit cost, F3 = Dangerous/Catastrophic). Installing an Component above the Lair's Workshop Tier adds **+1 Flaw per tier difference**.
* **PROD Status:** PROD 10 mentions component slots and workshops, but does not codify the Flaw rating math.
* **Recommendation:** Include in `02_PROD_Core_Rules/Compendiums/Equipment_and_Crafting.md`.

### 5. Boss Relics (Dead Boss Relic Harvesting)
* **Source:** `01_STAGE_Drafts/02_Equipment_and_Crafting/34_Crafting.md`
* **Mechanic:** When a Goblin Boss dies, their bones can be salvaged in the Lair to craft a specialized **Boss Relic** (always T1–T2, F0–F1) whose magical tags reflect how that Boss died (e.g. burned by a dragon $\rightarrow$ `[Fire]` Boss Relic).
* **PROD Status:** PROD 07 and PROD 10 mention the Bone Pile and Named Items, but not the explicit Boss Relic crafting recipe.
* **Recommendation:** Keep as a high-flavor crafting option in the Crafting Compendium.

### 6. Mundane Equipment Break Rolls
* **Source:** `01_STAGE_Drafts/02_Equipment_and_Crafting/35_Equipment_Catalogue.md`
* **Mechanic:** When a test using mundane gear suffers a **Fumble**, roll a 1d6 Break Roll: Junk breaks on 1–4, Scrappy on 1–3, Standard on 1–2, Superior on 1, and Legendary never breaks.
* **PROD Status:** Mentioned in PROD 05 in passing, but the full table is in STAGE.
* **Recommendation:** Include in `Equipment_and_Crafting.md`.

### 7. Mob Bulk Outfitting Cost
* **Source:** `01_STAGE_Drafts/03_Loot/31_loot.md`
* **Mechanic:** Purchasing standardized equipment for an entire Mob costs **1 token of the desired Tier per point of Mob Size** (e.g. Size 3 Mob with T2 Scrappy Spears costs 3x T2).
* **PROD Status:** Not explicitly stated in PROD 06 or PROD 10.
* **Recommendation:** Include in the Mob equipment guidelines.

### 8. Element Synthesis Matrix
* **Source:** `01_STAGE_Drafts/04_Tags_and_Keywords/08_Master_Tag_Index.md`
* **Mechanic:** Formal rules for combining tags dynamically in zones or crafting (e.g. `[Fire]` + `[Sticky]` = Burning Glue; `[Toxic]` + `[Chilled]` = Numbing Venom; `[Wet]` + `[Shock]` = Conduction; `[Wet]` + `[Fire]` = Steam Cloud).
* **PROD Status:** PROD 08 mentions combining power words, but the master chemical synthesis chart is in STAGE.
* **Recommendation:** Modernize and publish as `02_PROD_Core_Rules/Compendiums/Master_Tag_Index.md`.

---

## Next Steps for Staging & Production Promotion

When ready, we can tackle the active STAGE queues one compendium at a time:
1. **Compendium 1:** `02_Equipment_and_Crafting/` $\rightarrow$ Create `02_PROD_Core_Rules/Compendiums/Equipment_and_Crafting.md`.
2. **Compendium 2:** `03_Bestiary_and_Threats/` $\rightarrow$ Create `02_PROD_Core_Rules/Compendiums/Bestiary_and_Threats.md`.
3. **Compendium 3:** `01_Character_Options/` $\rightarrow$ Create `02_PROD_Core_Rules/Compendiums/Roles_and_Quirks.md`.
4. **Compendium 4:** `04_Tags_and_Keywords/` $\rightarrow$ Create `02_PROD_Core_Rules/Compendiums/Master_Tag_Index.md`.
