# GDR-003: Unified Modular Powers System (Effects & Descriptors)

* **Status:** ACCEPTED
* **Date:** 2026-05-28
* **Designer(s):** User & Antigravity (AI Coding Assistant)
* **Target Folder:** `STAGE_Drafts/01_Characters & Mobs/`

---

## 1. The Mechanical Challenge
In the current setup, there is a high risk of "term bloat" (Quirks, Twists, Shenanigans, Oddities, Relics, Feats, Tricks, and **Boons**/**Banes**). Having multiple independent systems for custom abilities makes the game hard for players to learn and heavy on bookkeeping.

Additionally, we need a system that supports creative freedom (allowing players to invent chaotic goblin abilities, gear, and mob upgrades) while remaining mechanically balanced under the hood without requiring the GM to memorize custom rules for every single combination.

---

## 2. Proposed Design

This design unifies all custom abilities under a single, cohesive architecture: **Narrative Descriptors (Tags)** paired with a **Tiered Mechanical Effects Toolkit**.

### The Three Pillars of Powers
All custom traits belong to one of three pillars:
1. **Quirks & Twists:** Personal Boss powers (Base Quirk + 1 Modifier Twist), as detailed in [14_Quirks.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/14_Quirks.md).
2. **Shenanigans:** Compulsive gang culture, detailed in [12_Gangs.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/12_Gang.md) (grants a static **Boon** and Flaw).
3. **Oddities & Relics:** Equipment-based powers (Oddities attached to gear; legendary bones forming Relics), detailed in [34_Crafting.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/34_Crafting.md).

### The Architecture: Descriptors vs. Effects

#### 1. Narrative Descriptors (Tags)
Descriptors (e.g., `[Sticky]`, `[Chilled]`, `[Loud]`, `[Toxic]`, `[Elastic]`, `[Angelic]`, `[Undead]`) are the narrative skin. They do not contain math. Instead, they define:
* How the power manifests in the fiction (e.g., `[Elastic]` means you can stretch).
* How it interacts with the environment (e.g., `[Chilled]` freezes water; `[Fire]` ignites wood; `[Loud]` ruins stealth).
* How elements combine during **Element Synthesis** (see below).

#### 2. Mechanical Effects (The Toolkit)
Mechanical Effects are the raw math dials of the rules. They are divided into **Tiers (T1–T5)** to align with Boss Stat progression (1–5) and Gear Quality (Junk to Legendary):

| Tier | Successes / Grit Loss | Range & Area | Duration & Conditions | Narrative & Utility |
|---|---|---|---|---|
| **T1 (Niche/Minor)** | **+1 Success** (on attack) OR **1 Grit/Size damage** (on hit). | **Melee** (Same Zone). | **Instant** (Effect resolves immediately). | Move 1 Zone as part of the action, or bypass a minor physical obstacle (e.g., climb a fence). |
| **T2 (Standard)** | **+2 Successes** (on attack) OR **2 Grit/Size damage** (on hit). | **Ranged: 1 Zone** (Adjacent). | **Sustained** (Basic condition like *Weakened* or *Restrained* until target spends 1 Action to shake it off). | Medium utility (e.g., stick to walls, breathe underwater, make loud noise that ruins stealth). |
| **T3 (Heroic/Area)** | **+3 Successes** (on attack) OR **3 Grit/Size damage** (on hit); OR heal **2 Grit**. | **Zone** (Affects all targets in a single Zone). | **Persistent** (Severe condition like *Blinded* or *Terrified* until target spends 1 Action to shake it off). | Zone-wide utility (e.g., ignite a zone, fill it with thick smoke, block exits). |
| **T4 (Destructive)** | **+4 Successes** (on attack) OR **4 Grit/Size damage** (on hit); OR double successes. | **Blast** (Affects own + all adjacent Zones). | **Encounter** (Condition lasts for the duration of the fight). | Destroys permanent structures, creates new paths, or permanently alters zone boundaries. |
| **T5 (Legendary)** | Target is instantly defeated; OR double Wounds. | **Encounter Scale** (Affects entire map). | **Permanent** (Can only be cured in the Lair). | Alter the landscape, summon mythic weather, or permanently warp magic in the region. |

>> **GOBLIN RULE (Applying Successes/Damage):**
>> * When rolled against a standard enemy, "Damage" is added to the attack roll as **automatic successes** toward meeting their Defence TN.
>> * When rolled against a Boss, PC, or Mob, it directly subtracts **Grit** or **Mob Size** on a hit.

### Assembling a Power
When a player learns a Quirk, crafts Custom Gear, or upgrades a Mob, they combine a **Mechanical Effect** of the appropriate Tier with a **Narrative Descriptor (Tag)**:

* **Example 1 (Quirk):** A Boss takes a **Slink** T2 Quirk. They choose the T2 Mechanical Effect (*imposes Restrained*) and the Descriptor `[Sticky]`. The power is called **Sticky Spit**. On a hit, the target is covered in glue, imposing the **Restrained** condition.
* **Example 2 (Oddity):** A Crafter attaches a T3 Core Oddity to a sword. They choose the T3 Mechanical Effect (*Zone Area*) and the Descriptor `[Fire]`. The weapon is a **Flameslasher**. When swung, it sweeps fire across the entire Zone.

---

## 3. Element Synthesis (Combining Descriptors)
When players combine multiple descriptors (on Custom Gear with multiple Oddities or through environmental combos), the outcome is resolved using the following guidelines:

*   **Synthesis at Creation:** To maintain fast-paced combat, all combination effects on custom weapons must be pre-negotiated and written down on the character/item sheet during the Lair downtime phase.
*   **Single Condition Constraint:** A single attack or weapon can never apply more than one mechanical condition.
*   **Synthesis Upgrade:** If two elements with conditions combine, they upgrade into a single, higher-tier condition (e.g., Slink Bane + Tough Bane upgrade to **Restrained** or **Stunned**).
*   **Narrative-Only Secondary Effects:** The second tag provides narrative utility, not combat math.
    * > **Example:** `[Fire]` + `[Sticky]` creates a burning glue that ignites wooden shields, but mechanically it just deals the base fire successes and imposes **Restrained**.

---

## 4. Alignment with Design Tenets

1. **Fun at the Table:** Players get to build whatever crazy weapon or mutation they want (e.g., a "Vampiric Fungal Cannon") simply by picking Tiers and Descriptors.
2. **Zero Post-Roll Math:** The effects translate into standard **Boons**, **Banes**, successes, and conditions. No tracking numbers or tick-counters.
3. **Embrace Chaos:** Combining unexpected tags encourages players to experiment, leading to chaotic emergent outcomes at the table.
4. **Goblin Flavor:** Modularity captures the essence of scrap-crafting and chaotic goblin mutation.

---

## 5. Edge Cases & Rules Lawyer Concerns
* **Bookkeeping Bloat:** To avoid tracking round durations, conditions are resolved using the standard Conditions system in [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md). Shaking off a sustained or persistent condition requires a Boss to spend 1 Action.
* **Combo Limits & Crafting Capacity:** A Boss can have a maximum of 3 Quirks with 1 Twist each. An item can have a maximum number of Oddities equal to the crafter's **Brains** score (Crafting Capacity). This hard-caps the complexity of any single roll.
* **AoE Balancing & Multi-Oddities:** To prevent low-level spam of Mob-vaporizing attacks, an item cannot have both a high-tier damage effect and a wide Area/Blast delivery without paying the modular cost. To build an Area weapon, a player must install both a **Core Oddity** (for successes/damage) and a **Modifier Oddity** (for delivery).
* **Grunt Costs:** Grunt-costed abilities are highly impactful but rare, reflecting the strategic value of **Grunt** (which caps Mob control size).
  * **T1–T2:** Passive, 1 Action, or 1 Grunt.
  * **T3:** 1 Action OR 1 Grunt.
  * **T4:** 1 Action + 1 Grunt OR 2 Grunt.
  * **T5:** 3 Grunt OR triggers an immediate **Overclock** (destroys the item/power).

---

>> **GOBLIN VERDICT:** Tape 'em together, write wot it does on yer paper back in da cave, and throw it at da tall-man! Balanced rules under the hood mean more time for green chaos at the table.
