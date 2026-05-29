# Researcher Findings: Environmental Hazards & Zone Statblocks

**Role:** The Researcher
**Objective:** Analyze the "Room Target Number" (Room TN) mechanic from *Index Card RPG* (ICRPG) and propose a unified, modular "Zone Statblock" system for Gobbos to represent environmental hazards, obstacles, and opportunities without adding GM cognitive load.

---

## 1. How ICRPG's "Room Target" Works
In *Index Card RPG* (ICRPG) by Runehammer Games, the **Target Number (TN)**—often simply called the **Target**—is a core mechanic used to simplify and accelerate gameplay:
*   **Unified Difficulty:** Instead of setting different Difficulty Classes (DCs) for every monster, trap, or lock in an encounter, the Game Master (GM) sets a single Target Number for the entire scene/room (written clearly on an index card for all players to see).
*   **Universal Application:** This single number applies to all rolls in that room: attacking a monster, climbing a wall, dodging a trap, or picking a lock.
*   **Tactical Modifiers:** If an action is particularly easy, the target is **Easy** (effective Target is **reduced by 3**). If an action is particularly difficult, the target is **Hard** (effective Target is **increased by 3**).
*   **D.E.W. (Danger, Energy, Wonder):** ICRPG design recommends that every room has active Danger (hazards), Energy (timers prompting action), and Wonder (interactive elements or treasures).

---

## 2. Adapting the Concept to Gobbos: "Zone Profiles"
Gobbos uses zone-based tactical movement rather than a grid (see [Movement & Zones](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/03_Movement%20&%20Zones.md)). Rather than a single Target Number for an entire dungeon, we can localize this concept by giving each **Zone** an **Environmental Profile** (combining **Difficulty** and **TN**).

### The Zone Profile
Each Zone on the GM's map is assigned a default profile:
*   **Normal:1** (Supreme Average): Standard rooms, clear streets, simple caves.
*   **Normal:2** (Challenging Terrain): Sewer canals, rocky slopes, crumbling ruins.
*   **Hard:1** (Dangerous/Hostile): Heavy winds, active battlegrounds, slick ice.

>> **THE GOLDEN RULE OF ZONE PROFILES:**
>> Any generic environmental action, traversal check, or search attempted within a Zone defaults to that Zone's Profile (e.g., test **Slink** against **Normal:2** to climb out of the sewer water), unless a specific object (like a high-security lockbox or a unique monster) explicitly overrides it.

This keeps prep at absolute zero: the GM only needs to write down a single profile for each Zone on their sketch map.

---

## 3. Predefined Zone Traits: Problems & Opportunities
To easily customize the battlefield, a GM can slap modular traits onto any Zone. These are split into **Problems** (Hazards/Obstacles) and **Opportunities** (Tactical benefits). 

All traits are resolved passively or through player rolls; **the GM never rolls dice** to activate environmental effects.

### Predefined Problems (Hazards & Obstacles)

| Trait | Category | Mechanical Rules |
| :--- | :--- | :--- |
| **Burning** | Hazard | Any PC or Mob that enters this Zone, or starts their turn here, must pass a **Slink** test against the **Zone Profile** or take **1 Wound** (PC) or **1 Size damage** (Mob). Goblins can spend a Standard Action to douse a burning comrade. |
| **Narrow** | Obstacle | The maximum Mob size that can occupy this Zone without penalty is **Size 2**. Mobs of larger sizes suffer a permanent **Bane** (-1d) to all attacks and physical tests, and their Movement speed is capped at **1 Zone**. Giant enemies cannot enter. |
| **Slippery** | Obstacle | When entering this Zone, a PC or Mob must test **Slink** against the **Zone Profile**. On a failure, they fall **Prone** and their movement ends immediately. |
| **Smoky** | Obstacle | The Zone is filled with dense smoke or gas. Ranged attacks passing through or targeting someone inside this Zone suffer a **Bane** (-1d). The Zone grants **Partial Cover** to anyone inside it. |
| **Toxic** | Hazard | Any PC or Mob starting their turn here must test **Tough** against the **Zone Profile**. On a failure, they suffer the **Weakened** condition until they spend a Standard Action to catch their breath in a clean zone. |
| **Deep Water** | Obstacle | Movement through this Zone is reduced. Goblins must spend a Standard Action (**Move**) to travel **1 Zone** (instead of their normal speed). If forced to swim, they must test **Tough** against the **Zone Profile** or begin drowning (taking **1 Wound** per round). |

### Predefined Opportunities (Tactical Features & Treats)

| Trait | Category | Mechanical Rules |
| :--- | :--- | :--- |
| **High Ground** | Opportunity | Ranged attacks made from this Zone gain a **Boon** (+1d). Melee attacks made by enemies outside this Zone against targets inside this Zone suffer a **Bane** (-1d). |
| **Junk Pile** | Opportunity | Goblins can spend a Standard Action (**Manipulate**) to search the pile (test **Notice** against the **Zone Profile**). On a success, they roll on the Trash Table or find a throwable rock (deals **1 damage** ranged). |
| **Shadowy** | Opportunity | Dark corners, heavy curtains, or alcoves. Goblins attempting to Hide in this Zone gain a **Boon** (+1d) on their **Slink** tests. |
| **Shoring** | Opportunity | Columns, support beams, or structural braces. Goblins can spend a Standard Action (**Manipulate**) to collapse the shoring. Doing so triggers a cave-in: the Zone gains the **Crumbling** hazard and blocks exit paths. |

---

## 4. Example: The Sewer Escape (GM Prep Map)
Here is how a GM prepares a quick encounter using this system:

*   **Zone A: The Guard Post**
    *   *Profile:* **Normal:1**
    *   *Traits:* None. (Clear floor, standard lights).
*   **Zone B: The Narrow Sewage Pipe**
    *   *Profile:* **Normal:2**
    *   *Traits:* **Narrow**, **Smoky** (sewer gas).
*   **Zone C: The Flooded Reservoir**
    *   *Profile:* **Hard:1**
    *   *Traits:* **Deep Water**, **Junk Pile** (floating trash).

> **Example of Play:**
> Grub and his Mob of Size 3 run from the guards into **Zone B: The Narrow Sewage Pipe**. Because Zone B has the **Narrow** trait, Grub's Mob is too big! Grub must either split the Mob, or the Mob suffers a **Bane** on all attacks and physical tests, and their movement speed drops to 1 Zone. Furthermore, because it is **Smoky**, the guards trying to shoot crossbows at them from Zone A suffer a **Bane** because Grub has Partial Cover. 
