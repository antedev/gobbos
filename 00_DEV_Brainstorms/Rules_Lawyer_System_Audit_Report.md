# Rules Lawyer System Audit Report

*Date: May 30, 2026*  
*Role: Meticulous TTRPG Systems Analyst*  
*Scope: Full audit of `01_STAGE_Drafts/` rules files*

---

## Executive Summary

This audit is a comprehensive evaluation of the Gobbos TTRPG rules currently residing in `01_STAGE_Drafts/`. Since the `02_PROD_Core_Rules/` directory is currently empty, the STAGE drafts represent the active state of the rules. 

While the core game loops (Tactical Raid, Lair Downtime, and Roguelite Legacy) are mechanically compelling and thematic, several inconsistencies, logical contradictions, terminology drifts, and mathematical errors have emerged due to rapid iterative development. 

This report details **15 specific issues** categorized by system area, assigning a severity level to each, and providing a direct resolution pathway to align the rules with the core **Design Tenets** of the game.

---

## Table of Contents
1. [Core Resolution & Dice Mechanics](#1-core-resolution--dice-mechanics)
2. [Stat Tracks & Progression Anomalies](#2-stat-tracks--progression-anomalies)
3. [Combat, Orders, & Mob Mechanics](#3-combat-orders--mob-mechanics)
4. [Inventory, Carry, & Equipment Discrepancies](#4-inventory-carry--equipment-discrepancies)
5. [Lair, Magic, & System Gaps](#5-lair-magic--system-gaps)
6. [Summary Matrix & Action Plan](#6-summary-matrix--action-plan)

---

## 1. Core Resolution & Dice Mechanics

### Issue 1.1: The 0d6 Dice Pool Rule Location Gap
* **Severity:** Medium
* **Description:** In [00_Journey_Rules.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/07_Travel/00_Journey_Rules.md) (Example 1), a critical core rule is introduced in a sidebar note: 
  > *“In Gobbos, if a dice pool is reduced to 0d6 or less, the test automatically fails, but you still roll 1d6 and need a 6 to salvage it, while a 1 is a fumble.”*
* **Inconsistency:** This resolution rule is entirely absent from [01_Dice.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/01_Dice.md) (where dice pool assembly is defined) and [06_Keywords Index.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/06_Keywords Index.md).
* **Resolution Pathway:** Copy this rule into the "Dice Pool" section of `01_Dice.md` and add it to `06_Keywords Index.md` under "Dice & Tests."

### Issue 1.2: GM Dice Rolling vs. Design Tenets
* **Severity:** Medium
* **Description:** The Gobbos Golden Rule states that the GM never rolls dice in combat or standard checks. However, multiple draft files direct the GM to roll:
  1. In [05_Raid points.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/05_Raid points.md) (Alert Checks): *“the GM rolls 1d6 [to check Alert level].”*
  2. In [00_Journey_Rules.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/07_Travel/00_Journey_Rules.md) (Travel Events): *“The GM rolls 1d6 on the Gobbo Travel Event Table.”*
  3. In [03_Movement & Zones.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/03_Movement & Zones.md) (Burning): *“Fire spreads... on a roll of 5–6 on 1d6 (rolled by the GM or a player).”*
* **Inconsistency:** Direct GM rolling violates the design tenet that the GM's threats are deterministic, and that players roll all the dice. 
* **Resolution Pathway:** Update the text in these files to state that **players roll** for these environmental/procedural occurrences (e.g., *"The active player rolls 1d6 on the Travel Event Table on behalf of the horde"*).

### Issue 1.3: Character Death "Last Act" Resolution Rule
* **Severity:** Low
* **Description:** In [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md), the "Last Act" rule states: *“This action is always Easy, no matter the circumstances.”*
* **Inconsistency:** [01_Dice.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/01_Dice.md) lists Easy, Normal, and Hard difficulties but does not cross-reference or mention this specific death exception. 
* **Resolution Pathway:** Add a brief cross-reference in `01_Dice.md` under "Difficulty and Target Number" noting that character death actions are a default exception (always Easy).

---

## 2. Stat Tracks & Progression Anomalies

### Issue 2.1: Slink Movement Speed vs. Zone Movement Speed
* **Severity:** High
* **Description:** In [03_Movement & Zones.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/03_Movement & Zones.md), it is stated: 
  > *“a normal movement speed is to move 2 Zones per round and action.”*
* **Inconsistency:** This directly contradicts the **Slink** stat tracks in both [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/10_Stats.md) and [11_Character Creation.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/11_Character Creation.md), which define Movement speeds as:
  * **Slink 1:** Movement 4 Zones
  * **Slink 2:** Movement 5 Zones
  * **Slink 3:** Movement 5 Zones
  * **Slink 4:** Movement 6 Zones
  * **Slink 5:** Movement 7 Zones
  Additionally, [02 Combat.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/02 Combat.md) (Move action) says: *"With a Move action, you can move up to your Movement number of zones."* 
  If PCs move 4–7 Zones per action, but the zones guide says "normal movement speed is 2 Zones," there is a massive tactical scaling breakdown.
* **Resolution Pathway:** Clarify that **2 Zones per action** is the base movement speed for **Mobs** (who do not have a Slink score) or unburdened standard enemies, while **Boss PCs** utilize their specific Slink-derived **Movement** score (4 to 7 Zones per action).

### Issue 2.2: Terminology Drift — "Vigor" vs. "Tough"
* **Severity:** Medium
* **Description:** The term **Vigor** appears as a core stat in two locations:
  1. In [00_Magic_Rules.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/08_Magic/00_Magic_Rules.md) (line 113): *“You suffer a Bane on all physical actions (Vigor and Slink) until the end of the encounter.”*
  2. In [GEMINI.md](file:///c:/Users/ante/Documents/github/gobbos/GEMINI.md) (line 98): *“Core Stats & Mechanics: Must be Bold. (e.g., Grit, Boon, Bane, Vigor, Slink, Brain, Renown).”*
* **Inconsistency:** **Vigor** is a legacy stat or typo. The actual Gobbos stat is **Tough**. 
* **Resolution Pathway:** Replace all occurrences of **Vigor** with **Tough** across the rulebooks and templates.

### Issue 2.3: Stat level 6 and Elder Retirement Wording
* **Severity:** Low
* **Description:** In [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/10_Stats.md), the main stats are defined as ranging from **1 to 5**, with Level 5 designated as "(Max)".
* **Inconsistency:** [12_Gang.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/12_Gang.md) and [15_Level_Up and death.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/15_Level_Up and death.md) state that: *"When a Boss reaches Level 6 in any stat, they automatically retire [costing 6 XP]."* This makes Level 6 the trigger point, meaning Level 5 is the maximum *playable* rank, not the absolute stat ceiling.
* **Resolution Pathway:** Update the stat tracks in `10_Stats.md` to append a note: *"Reaching Level 6 in any stat is impossible to play; buying this rank triggers immediate Retirement as an Elder."*

---

## 3. Combat, Orders, & Mob Mechanics

### Issue 3.1: Giving Orders — Standard Orders Roll Contradiction
* **Severity:** High
* **Description:** There is a direct logical contradiction between the combat action definitions and the ordering guide:
  1. In [02 Combat.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/02 Combat.md): *“Standard Orders do not require a dice roll.”*
  2. In [04_Giving orders.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/04_Giving orders.md): *“If they are smaller or equal to your command size, the TN is 1. If they are bigger, the TN goes up... If they are in a zone further away, the test is Normal if the distance is equal or less than your Mouth. One zone further away increases the difficulty to Hard...”*
* **Inconsistency:** If standard orders don't require rolls, then why does the distance check require a roll for any Mob not in the same zone? (Only the same zone grants an automatic success). Additionally, `04_Giving orders.md` never explicitly states **which stat is rolled** for the test, though it implies **Mouth** or **Grunt**.
* **Resolution Pathway:** Reconcile the rules:
  * Clarify that **Orders issued to Mobs in the same Zone never require a roll** (provided the Mob size is <= current Grunt).
  * Clarify that **Orders issued to Mobs in adjacent/remote Zones require a Mouth test** against the designated TN and difficulty.
  * Explicitly write: *"The player rolls a Mouth test"* in `04_Giving orders.md`.

### Issue 3.2: Mob Damage Rearrangement (Healing) Confusion
* **Severity:** Medium
* **Description:** In [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md), the Mob healing example states:
  > *“A 3d6 mob has taken some beating and their damage after the battle are 3,4,2. The Boss can now rearrange the damage dices to 6,2,1 or perhaps 5,4. In the latter case, effectively reducing the size of the mob in order to make it more stable.”*
* **Inconsistency:** Gobbos Mobs track health by turning physical dice faces down. A die is removed only when it drops below 1. 
  * If the dice read `3`, `4`, and `2` (Size 3, Total Health 9), rearranging them to `6`, `2`, and `1` keeps them at Size 3 (Total Health 9).
  * Rearranging them to `5` and `4` voluntarily drops them to Size 2. 
  Since combat power is directly tied to Mob Size (rolling Size in dice for attacks and Tough tests), there is **no mechanical advantage** to voluntarily reducing Mob Size to "make it stable." In fact, doing so is strictly disadvantageous.
* **Resolution Pathway:** Clarify why stability matters. (e.g., if a Mob has a die at `1` and takes *any* environmental damage, that die is destroyed, which might trigger a morale check or drop loot. If they consolidate health into fewer, higher-valued dice, they avoid low-health vulnerabilities at the cost of immediate combat power). Alternatively, remove the voluntary size-reduction option if it serves no practical purpose.

### Issue 3.3: Meat Shield Quirk Damage Discrepancy
* **Severity:** Medium
* **Description:** The **Meat Shield** ability has two different damage scales:
  1. In [13_Boons_and_Banes.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/13_Boons_and_Banes.md): *“redirect an attack meant for you to an adjacent friendly Mob [the Mob takes the attack's standard damage].”*
  2. In [14_Quirks.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/14_Quirks.md): *“The Mob takes the hit instead (losing 1d3 Mob Size), and you take 0 Wounds.”*
* **Inconsistency:** Losing **1d3 Mob Size** is a devastating penalty (equivalent to 1 to 3 fully killed Gobbos, or up to 18 points of damage). Taking the attack's standard damage (usually 1 or 2 damage to a single die face) is far lighter.
* **Resolution Pathway:** Align the two rules. The Mob should simply take the standard damage of the attack, which naturally reduces its dice faces and may (or may not) result in a Size reduction if a die drops below 1.

---

## 4. Inventory, Carry, & Equipment Discrepancies

### Issue 4.1: PC Carry Capacity Example Math Error
* **Severity:** Medium
* **Description:** In [32_Carry Stuff.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/32_Carry Stuff.md), the PC example states:
  > *“Grugor has a Tough of 3. He can carry loot up to a total of bulk of 8 (4 starting + 4 for level 3)...”*
* **Inconsistency:** The core rules and formulas establish a different capacity:
  * The formula in the same file states: *"A Goblin can carry 4 Bulk and then + 2 for each level of Tough."* For Tough 3, this is $4 + (2 \times 3) = 10$ Bulk.
  * The stat tracks in [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/10_Stats.md) and [11_Character Creation.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/11_Character Creation.md) explicitly state: *"Level 3 [Tough]: Carry Capacity 10."*
  The example calculation "4 starting + 4 for level 3 = 8" is incorrect.
* **Resolution Pathway:** Correct the example text: *"Grugor has a Tough of 3. He can carry loot up to a total of 10 Bulk..."* Update the item totals in the example to match this budget.

### Issue 4.2: Mob Carry Capacity Example Math Error
* **Severity:** Medium
* **Description:** In [32_Carry Stuff.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/32_Carry Stuff.md), the Mob example states:
  > *“A large Troop of goblin warriors of size 3 has been plundering... They are within their limit of Bulk 9...”*
* **Inconsistency:** The rules in `32_Carry Stuff.md` and [13_Goblin_mob.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md) state that a Mob's carry capacity is **Size x 4 Bulk**. For a Size 3 Mob, the limit is **12 Bulk**, not 9 (which represents a legacy Size x 3 formula).
* **Resolution Pathway:** Correct the example text: *"A large Troop of goblin warriors of size 3 has a limit of 12 Bulk. They are currently carrying 8 Bulk, which is well within their capacity."*

### Issue 4.3: Weapons "Damage" vs. "Attack Dice Pool Modifier"
* **Severity:** Medium
* **Description:** In [33_Equipment.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/33_Equipment.md) and [11_Character Creation.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/11_Character Creation.md), weapons list a **Damage** value (e.g., Unarmed: `+1d`, Light Melee: `+2d`, Medium Melee: `+3d`, Heavy Melee: `+4d`).
* **Inconsistency:** Gobbos combat is deterministic for enemies—successes equal to Defence instantly kill them. The player rolls `Tough` (Melee) or `Slink` (Ranged) plus the weapon modifier. The weapon modifier adds **dice to the attack roll**, not "damage" to a secondary health bar. Calling this column "Damage" is highly misleading.
* **Resolution Pathway:** Rename the column in equipment tables from **Damage** to **Attack Pool** or **Attack Dice (+d)** to match the system mechanics.

---

## 5. Lair, Magic, & System Gaps

### Issue 5.1: Magic Power Words Learning Progression Gap
* **Severity:** High
* **Description:** In [00_Magic_Rules.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/08_Magic/00_Magic_Rules.md), spellcasters utilize Power Words (Narrative Tags) to cast spells. 
* **Inconsistency:** While there are clear XP rules for learning and upgrading Quirks and Twists, there are **no rules or costs for learning new Power Words**. The text states: *"If you have access to a Tag through Quirks, Gear, Lair upgrades, or Gang traits, you can shout it..."* but offers no progression mechanism for a dedicated mage to expand their vocabulary independently of gear/quirks.
* **Resolution Pathway:** Establish a mechanical cost (e.g., spending XP or Lair research labor) to permanently learn a Power Word/Tag as a spell, or state clearly that Power Words can *only* be channeled if actively present on the Boss's equipped gear or Quirks.

### Issue 5.2: Lair Upgrades vs. Dominance Room Mismatch
* **Severity:** Medium
* **Description:** In [00_Lair_Rules.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/05_Base/00_Lair_Rules.md):
  * The listed structural room upgrades are: `Breeding Pits` (T1/T2), `Mud Tavern`, `Scrap Collector Yard`, and `Dwarven Forge`.
  * The Lair Dominance example list refers to: `Proper Smithy` and `Brewery Cavern`.
* **Inconsistency:** `Proper Smithy` is listed as a Workshop Quality tier in [34_Crafting.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/34_Crafting.md), not a separate Lair Room upgrade. The Lair rooms and their dominance kickbacks do not map consistently between the base rules and the crafting rules.
* **Resolution Pathway:** Harmonize the room lists. Specify that the Workshop is a single Lair room that can be upgraded in Tiers (Open Fire $\rightarrow$ Scrap Forge $\rightarrow$ Proper Smithy $\rightarrow$ Master Workshop $\rightarrow$ Legendary Forge), and that a Gang can claim Dominance over the Workshop itself. Ensure all room examples in the Dominance section exist in the Lair Upgrades database.

### Issue 5.3: Glossary Placeholders [TODOs]
* **Severity:** Low
* **Description:** In [06_Keywords Index.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/06_Keywords Index.md), several critical terms contain placeholders:
  * `Grit: [TODO: Define]`
  * `Size: [TODO: Define for PCs]`
  * `Status Effects: [TODO: Define]`
* **Inconsistency:** Core terms are undefined. Specifically, PC **Size** is used in rules (e.g. `Butcher` Quirk: *"against an enemy whose Size is strictly smaller than yours"*), but a PC's default Size is never stated.
* **Resolution Pathway:** Write out these definitions. Define PC **Size** as a default of **1** (unless modified by mutations or specific heavy gear). Map Status Effects directly to the condition list in `07_Wounds_Conditions.md`.

---

## 6. Summary Matrix & Action Plan

| ID | Title | Component / File | Severity | Action Recommended |
|---|---|---|---|---|
| **1.1** | 0d6 resolution location | `01_Dice.md` | Medium | Copy rule from travel example to core dice rules. |
| **1.2** | GM rolling events | `05_Raid points.md`, `00_Journey_Rules.md` | Medium | Change GM rolls to Player rolls on behalf of the GM. |
| **1.3** | Last Act Easy difficulty | `01_Dice.md`, `07_Wounds_Conditions.md` | Low | Cross-reference Easy difficulty rule in core dice chapter. |
| **2.1** | Slink movement scaling | `03_Movement & Zones.md` | High | Clarify that 2 Zones is Mob speed; PCs use Slink-Movement. |
| **2.2** | Vigor vs. Tough typo | `00_Magic_Rules.md`, `GEMINI.md` | Medium | Rename all occurrences of **Vigor** to **Tough**. |
| **2.3** | Level 6 retirement | `10_Stats.md` | Low | Add note to stat tracks clarifying Level 6 retirement buy. |
| **3.1** | Order action rolls | `02 Combat.md`, `04_Giving orders.md` | High | Harmonize same-zone auto-success vs. remote Mouth tests. |
| **3.2** | Mob healing stability | `07_Wounds_Conditions.md` | Medium | Clarify why consolidating health into fewer dice is useful. |
| **3.3** | Meat Shield damage | `13_Boons_and_Banes.md`, `14_Quirks.md` | Medium | Align: Mob takes normal attack damage, not 1d3 Size loss. |
| **4.1** | Grugor Carry math | `32_Carry Stuff.md` | Medium | Change Tough 3 carry limit in example from 8 to 10. |
| **4.2** | Mob Carry math | `32_Carry Stuff.md` | Medium | Change Size 3 Mob limit in example from 9 to 12. |
| **4.3** | Weapon "Damage" label | `33_Equipment.md`, `11_Character Creation.md` | Medium | Rename "Damage" column to "Attack Pool (+d)". |
| **5.1** | Magic Word learning | `00_Magic_Rules.md` | High | Define how Power Words are acquired/progressed. |
| **5.2** | Lair Rooms vs Workshop | `00_Lair_Rules.md`, `34_Crafting.md` | Medium | Harmonize room names and clarify workshop dominance. |
| **5.3** | Glossary [TODOs] | `06_Keywords Index.md` | Low | Write out definitions for Grit, PC Size, and Status Effects. |

---
*Report compiled by the Rules Lawyer. Ready for refinement and implementation.*
