# GDR-006: Environmental Hazards & Zone Statblocks

* **Status:** PROPOSED
* **Date:** 2026-05-29
* **Designer(s):** User & Antigravity (AI Coding Assistant)
* **Target Folder:** `STAGE_Drafts/00_Rules/` (to expand `03_Movement & Zones.md` and `07_Wounds_Conditions.md`)

---

## 1. The Mechanical Challenge
In Gobbos, movement and combat are resolved using **Zones** (as outlined in [Movement & Zones](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/03_Movement%20&%20Zones.md)). While the rules state that Zones can have attributes representing terrain, cover, or danger, we currently lack:
1.  A unified mechanical standard for GMs to set environmental check difficulties on the fly.
2.  A list of predefined, modular environmental features ("Problems and Opportunities") that can be immediately placed onto a battlefield.

If a GM has to manually determine unique Difficulty and Target Numbers (TN) for every wall, lock, trap, and debris pile in the middle of a chaotic fight, the pacing slows down. Furthermore, we must ensure all hazards resolve without violating the golden rule: **The GM never rolls dice!**

---

## 2. Proposed Design

This design adapts the "Room Target" mechanic from *Index Card RPG* (ICRPG) into a localized **Zone Profile** system, and introduces a library of modular **Zone Traits** (Problems and Opportunities) to easily construct tactical, chaotic battlefields.

### 2.1. The Zone Profile (The "Room TN" Adaptation)
Every Zone in an encounter has a default **Zone Profile** consisting of a **Difficulty** and a **Target Number (TN)** (e.g., **Normal:1**, **Normal:2**, or **Hard:1**). 

>> **THE ZONE PROFILE RULE:**
>> Any general environmental interaction, traversal, or search check attempted within a Zone defaults to using that Zone's Profile. GMs do not invent DCs for individual tasks; they simply use the Zone Profile.
>> *   *Example:* Climbing a wall, forcing a door, jumping a trench, or searching a junk pile in a Zone with a **Normal:2** profile all require **2 successes** on a **Normal** roll.

GMs can adjust the difficulty level of a specific task based on tools or circumstances (e.g., using professional climbing gear turns a traversal check from **Normal:2** to **Easy:2**), but the base successes needed remain tied to the Zone itself.

---

### 2.2. Zone Traits Library: Problems & Opportunities
Zones can be customized with modular, predefined traits. These are split into **Problems** (Hazards/Obstacles) and **Opportunities** (Tactical benefits).

#### Problems (Hazards & Obstacles)
*   **Burning (Hazard):** The Zone is on fire.
    *   *Rules:* Any PC or Mob that enters this Zone, or starts their turn here, must pass a **Slink** test against the **Zone Profile** or take **1 Wound** (PC) or **1 Size damage** (Mob). Goblins can spend a Standard Action to extinguish the fire on themselves or an adjacent ally.
*   **Narrow (Obstacle):** A tight chokepoint or low crawlspace.
    *   *Rules:* The maximum Mob size that can occupy this Zone without penalty is **Size 2**. Mobs of **Size 3+** suffer a permanent **Bane** (-1d) to all attack rolls and physical tests, and their Movement is capped at **1 Zone**. Giant enemies cannot enter.
*   **Slippery (Obstacle):** Ice, grease, or wet slime.
    *   *Rules:* When entering this Zone, a PC or Mob must test **Slink** against the **Zone Profile**. On a failure, they fall **Prone** and their movement ends immediately.
*   **Smoky (Obstacle):** Dense smoke, fog, or spores.
    *   *Rules:* Ranged attacks passing through or targeting someone inside this Zone suffer a **Bane** (-1d). The Zone grants **Partial Cover** to anyone inside it.
*   **Toxic (Hazard):** Poison gas, sewer fumes, or acid spray.
    *   *Rules:* Any PC or Mob starting their turn here must test **Tough** against the **Zone Profile**. On a failure, they suffer the **Weakened** condition until they spend a Standard Action to catch their breath in a clean zone.
*   **Deep Water (Obstacle):** Flooded area or rapid currents.
    *   *Rules:* Traversing this Zone requires a **Move** action to travel only **1 Zone** (ignoring standard movement speed). If forced to swim or stay afloat, creatures must test **Tough** against the **Zone Profile** or begin drowning (taking **1 Wound** per round).

#### Opportunities (Tactical Features & Treats)
*   **High Ground (Tactical Feature):** A ledge, platform, or pile of crates.
    *   *Rules:* Ranged attacks made from this Zone gain a **Boon** (+1d). Melee attacks made by enemies outside this Zone against targets inside this Zone suffer a **Bane** (-1d).
*   **Junk Pile (Treat):** Scrap metal, discarded weapons, or rubble.
    *   *Rules:* Goblins can spend a Standard Action (**Manipulate**) to search the pile (test **Notice** against the **Zone Profile**). On a success, they find a throw-able object (deals **1 damage** ranged) or a random piece of low-grade loot.
*   **Shadowy (Tactical Feature):** Dark alcoves or heavy curtains.
    *   *Rules:* Goblins attempting to Hide in this Zone gain a **Boon** (+1d) on their **Slink** tests.
*   **Shoring (Interactive):** Structural supports or pillars.
    *   *Rules:* Goblins can spend a Standard Action (**Manipulate**) to collapse the supports. This triggers a cave-in: the Zone gains the **Crumbling** hazard (a random target must test **Notice** against the **Zone Profile** each round or take **1 Wound**) and blocks all movement to adjacent zones until cleared.

---

## 3. Alignment with Design Tenets

1.  **Fun at the Table:** Gives players and Mobs tactical, interactive toys on the battlefield (pushing enemies into fires, hiding in shadows, throwing junk).
2.  **Zero Post-Roll Math:** Modified rolls use the standard **Boon** and **Bane** systems, and difficulties map directly to **Easy/Normal/Hard** success states. No arithmetic is needed after dice are cast.
3.  **Embrace Chaos:** Hazards like **Slippery** mud or **Burning** oil can cause sudden, dramatic shifts in positioning and health, forcing players to adapt.
4.  **Goblin Flavor:** Goblins are small, so the **Narrow** constraint affects large enemy Mobs or Giant foes much more severely than a scrappy crew of runts. Searching a **Junk Pile** for garbage to throw is quintessentially goblinoid.

---

## 4. Edge Cases & Rules Lawyer Concerns
*   **GM Roll Mitigation:** All hazards are resolved using player-facing saving throws. GMs never roll to see if a hazard hits; they simply announce the trigger, and the affected player rolls to resist.
*   **Mob Damage Scaling:** Environmental hazards like **Burning** or **Crumbling** deal **1 Wound** to a PC or **1 Size damage** (killing one goblin unit) to a Mob. This ensures damage types remain consistent across the system.
*   **Mob Prone Interaction:** If a Mob is knocked **Prone** by slipping, it suffers **-1d on Dodge** and must spend **1 Move action** of its next Order to stand back up, mirroring PC rules.

---

## 5. Alternatives Considered
*   **Global Room Target:** We considered a single Target Number for the entire combat map (direct ICRPG port). However, Gobbos' zone-based layout makes it far more interesting to have different zones feel physically distinct (e.g., fighting on dry land vs. wading through sewer sludge).
*   **Dynamic GM Threat Rolls:** We rejected having fires or cave-ins roll "attack dice" against the players, as it violates the tenet of the GM never rolling dice in combat.

---

>> **GOBLIN VERDICT:** "If ya run into the fiery zone, yer pants catch fire! But if ya hide in the smoky zone, the tall-men can't shoot ya with their bows. Just don't bring the whole mob into the narrow pipe or you'll get stuck like a fat pig!"
