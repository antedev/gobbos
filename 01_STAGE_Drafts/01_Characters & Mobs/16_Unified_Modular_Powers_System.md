# 16. Unified Modular Powers System

*Goblins don't follow formulas, unless it is a formula for making things go boom. A bit of glowing scrap, a twitching monster eyeball, a sudden chemical itch in the skin—mix them all together, tape it to a sword, and you have got a plan.*

The **Unified Modular Powers System** is the core framework for all custom abilities, mutations, and specialized gear in Gobbos. It unifies three separate paths of progression under a single rules architecture:
1. **Quirks & Twists:** Personal abilities customized by the Boss, detailed in [14_Quirks.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/14_Quirks.md).
2. **Shenanigans:** The core culture and compulsive traits of a **Gang**, detailed in [12_Gangs.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/12_Gang.md).
3. **Oddities & Relics:** Strange materials and magical scrap crafted into custom equipment, detailed in [34_Crafting.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/34_Crafting.md).

---

## 1. Descriptors vs. Mechanical Effects

Every modular power is built by combining a narrative flavor with a structural rule.

### Narrative Descriptors (Tags)
Descriptors (written as `[Tag]`) represent the physical or magical manifestation of the power (e.g., `[Fire]`, `[Sticky]`, `[Chilled]`, `[Loud]`, `[Toxic]`, `[Elastic]`, `[Angelic]`, `[Undead]`). 

Descriptors do not contain math. Instead, they define:
* How the power behaves in the fiction (e.g., `[Elastic]` lets a goblin stretch their limbs to reach high places).
* How it interacts with the environment (e.g., `[Chilled]` freezes water; `[Fire]` ignites dry vegetation; `[Loud]` instantly alerts nearby guards).
* How different elements combine during **Element Synthesis**.

### Mechanical Effects (The Toolkit)
Mechanical Effects are the raw math dials of the rules. They are rated from **Tier 1** to **Tier 5** (**T1–T5**). This universal scale matches Boss Stat levels (1–5), Gear Quality (Junk to Legendary), and Workshop levels.

| Tier | Successes / Grit Loss | Range & Area | Duration & Conditions | Narrative & Utility |
|---|---|---|---|---|
| **T1 (Niche/Minor)** | **+1 Success** (on attack) OR **1** **Grit**/**Size** damage (on hit). | **Melee** (Same **Zone**). | **Instant** (Effect resolves immediately). | Move **1 Zone** as part of the action, or bypass a minor physical obstacle (e.g., climb a fence). |
| **T2 (Standard)** | **+2 Successes** (on attack) OR **2** **Grit**/**Size** damage (on hit). | **Ranged: 1 Zone** (Adjacent). | **Sustained** (Basic condition like *Weakened* or *Restrained* until target spends **1 Action** to shake it off). | Medium utility (e.g., stick to walls, breathe underwater, make loud noise that ruins stealth). |
| **T3 (Heroic/Area)** | **+3 Successes** (on attack) OR **3** **Grit**/**Size** damage (on hit); OR heal **2** **Grit**. | **Zone** (Affects all targets in a single **Zone**). | **Persistent** (Severe condition like *Blinded* or *Terrified* until target spends **1 Action** to shake it off). | Zone-wide utility (e.g., ignite a zone, fill it with thick smoke, block exits). |
| **T4 (Destructive)** | **+4 Successes** (on attack) OR **4** **Grit**/**Size** damage (on hit); OR double **successes**. | **Blast** (Affects own + all adjacent **Zones**). | **Encounter** (Condition lasts for the duration of the fight). | Destroys permanent structures, creates new paths, or permanently alters zone boundaries. |
| **T5 (Legendary)** | Target is instantly defeated; OR double **Wounds**. | **Encounter Scale** (Affects entire map). | **Permanent** (Can only be cured in the Lair). | Alter the landscape, summon mythic weather, or permanently warp magic in the region. |

>> **GOLDEN RULE: Applying Successes vs. Grit Loss**
>> To keep the combat fast and respect the deterministic nature of standard enemies, modular math adjusts based on the target:
>> * **Against standard enemies:** The value is added as **automatic successes** directly to the player's attack pool toward meeting the target's **Defence** **Target Number (TN)**.
>> * **Against Bosses, PCs, and Mobs:** The value is subtracted directly as **Grit** Loss (for Bosses and PCs) or **Mob** **Size** damage (for Mobs) on a successful hit.

---

## 2. Modularity & Core Assembly

To build a power, a player chooses one Narrative Descriptor and attaches it to a Mechanical Effect of the appropriate Tier.

> **Example (Quirk):** Grub has a **Slink** of 2. They select a **Slink** **T2** **Quirk**. They combine the **T2** Mechanical Effect (*imposes a Sustained condition*) with the Descriptor `[Sticky]` to create the **Sticky Spit** **Quirk**. When activated, the target is covered in glue and gains the *Restrained* condition.
>
> **Example (Oddity):** A crafter builds a **T3** weapon using a fire crystal. They choose the **T3** Mechanical Effect (*Zone Area*) and the Descriptor `[Fire]`. The weapon is a **Flameslasher**. When swung, it sweeps fire across the entire **Zone**.

### Balancing Area of Effect (AoE) Powers
Area attacks are highly lethal in Gobbos because **Area of Effect (AoE)** or **Cleave** damage applies to **every single die** in a **Mob**'s pool (see [13_Goblin_mob.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md)).
*   **The Multi-Oddity Rule:** An item or power cannot possess both a high-tier damage effect and a wide Area/Blast delivery without paying the modular cost.
*   To build an Area-damage weapon, a player must install both a **Core** **Oddity** (representing the successes/damage) and a **Modifier** **Oddity** (representing the Area/Blast delivery).
*   Because a goblin's **Brains** stat caps their **Crafting Capacity** (max Oddities per item), low-**Brains** goblins cannot build wide-area high-tier weapons. A **Brains** 1 goblin can only build a single-target **T3** weapon. A **Brains** 3+ goblin is required to combine a **T3** **Core** and a **T3** Area **Modifier**.

---

## 3. Element Synthesis

When players combine multiple descriptors (e.g., custom gear with multiple Oddities or environmental combos), the outcome is resolved using the following guidelines:

### Resolution at Creation
To prevent combat speed-bumps, **Element Synthesis must be resolved at the point of weapon creation/customization**, rather than negotiated during combat rounds. The player designs the combination during downtime, the GM approves the emergent synergy, and a static final statblock is written onto the item sheet.

### Single Condition Constraint
A single attack or weapon can never apply more than one mechanical condition.

### Synthesis Upgrade
If two elements with conditions combine, they upgrade into a single, higher-tier condition from the standard conditions list:
*   A **Slink** **Bane** + **Tough** **Bane** upgrade to **Restrained** (**Slink** 0, **Movement** 0) or **Stunned** (Cannot act).
*   A `[Toxic]` element + `[Chilled]` element combines into **Numbing Venom** (imposes **Restrained**).

### Narrative-Only Secondary Effects
The second tag provides narrative utility and environmental interaction, not extra combat math.
*   `[Fire]` + `[Sticky]` creates a burning glue that ignites wooden shields, but mechanically it just deals the base fire **successes** and imposes *Restrained*.

### Standard Condition Mapping
Narrative tags must map directly onto the standardized condition system in [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md):
*   `[Toxic]` or `[Sickening]` $\rightarrow$ imposes *Weakened* (**-1d** **Tough** / **-1d** Attack).
*   `[Sticky]`, `[Chilled]`, or `[Entangled]` $\rightarrow$ imposes *Restrained* (**-1d** **Slink** / **-1d** Dodge, **Movement** 0).
*   `[Terrifying]` or `[Horrific]` $\rightarrow$ imposes *Terrified* (**-1d** **Brains**/**Mouth**, cannot approach).
*   *Other tags* not covered by the matrix default to a simple **Bane** on tests involving a specific stat (e.g., `[Loud]` $\rightarrow$ a **Bane** on **Slink**/Sneak tests), which automatically clears at the end of combat.

---

## 4. Grunt Costs & Activation Economy

To use a modular power or active **Oddity**, a Boss must pay its associated activation cost. Because **Grunt** is a limited pool that determines maximum **Mob** command **Size** (see [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/10_Stats.md)), spending **Grunt** is a significant strategic sacrifice.

*   **T1–T2 Powers:** May be **Passive**, cost **1 Action**, or cost **1 Grunt**.
*   **T3 Powers:** Cost **1 Action** OR **1 Grunt**.
*   **T4 Powers:** Cost **1 Action** + **1 Grunt** OR **2 Grunt**.
*   **T5 Powers:** Cost **3 Grunt** OR trigger an immediate **Overclock** (completely destroying the item or power after resolution).
