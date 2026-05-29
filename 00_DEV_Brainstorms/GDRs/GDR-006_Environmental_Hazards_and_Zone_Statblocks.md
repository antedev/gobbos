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

This design adapts the "Room Target" mechanic from *Index Card RPG* (ICRPG) into a localized **Zone Profile** system, and defines the structural framework of **Zone Traits**.

### 2.1. Zone Profiles
Every Zone in an encounter is assigned a default **Zone Profile** consisting of a **Difficulty** and a **Target Number (TN)** (e.g., **Normal:1**, **Normal:2**, or **Hard:1**). 

>> **THE ZONE PROFILE RULE:**
>> Any general environmental interaction, traversal, or search check attempted within a Zone defaults to using that Zone's Profile. GMs do not invent DCs for individual tasks; they simply use the Zone Profile.
>> *   *Example:* Climbing a wall, forcing a door, jumping a trench, or searching a junk pile in a Zone with a **Normal:2** profile all require **2 successes** on a **Normal** roll.

GMs can adjust the difficulty level of a specific task based on tools or circumstances (e.g., using professional climbing gear turns a traversal check from **Normal:2** to **Easy:2**), but the base successes needed remain tied to the Zone itself.

---

### 2.2. Zone Traits
A **Zone Trait** is a mechanical modifier or effect associated with a specific Zone. Traits represent either obstacles players must overcome or advantages they can exploit. All traits fall under two general categories:

1.  **Problems (Hazards & Obstacles):** Negative environmental features.
    *   *Triggering:* Problems trigger either passively (continuous effect while occupying the zone), on entry (as soon as a creature enters the zone), or at a specific phase in the round (e.g. End of Round).
    *   *Resolution:* To avoid negative effects, a player must make a saving throw (a relevant stat check, typically **Slink** or **Tough**) against the **Zone Profile**. On a failure, they suffer Wounds, Size damage (for Mobs), or a negative **Condition**. 
    *   *GM Rolling:* GMs never roll to see if a hazard succeeds; the GM simply announces the hazard's trigger and the affected player rolls to resist.
2.  **Opportunities (Tactical Features & Treats):** Interactive or beneficial environmental features.
    *   *Triggering & Resolution:* Opportunities can be passive (e.g., providing Cover or Boons to attacks) or interactive. Goblins can interact with an interactive opportunity by spending a Standard Action (usually **Manipulate** or **Attack**) and testing a relevant stat against the **Zone Profile** to yield a benefit.

---

## 3. Predefined Zone Traits

These are standardized, modular Zone Traits that GMs can "slap" onto any Zone during setup.

### 3.1. Predefined Problems (Hazards & Obstacles)
*   **Burning (Hazard):** The Zone is on fire.
    *   *Trigger:* Entering the Zone, or starting a turn inside it.
    *   *Rules:* Must pass a **Slink** test against the **Zone Profile** or take **1 Wound** (PC) or **1 Size damage** (Mob). Goblins can spend a Standard Action to extinguish the fire on themselves or an adjacent ally.
*   **Narrow (Obstacle):** A tight chokepoint or low crawlspace.
    *   *Trigger:* Passive.
    *   *Rules:* The maximum Mob size that can occupy this Zone without penalty is **Size 2**. Mobs of **Size 3+** suffer a permanent **Bane** (-1d) to all attack rolls and physical tests, and their Movement is capped at **1 Zone**. Giant enemies cannot enter.
*   **Slippery (Obstacle):** Ice, grease, or wet slime.
    *   *Trigger:* Entering the Zone.
    *   *Rules:* Must test **Slink** against the **Zone Profile**. On a failure, the creature falls **Prone** and their movement ends immediately.
*   **Smoky (Obstacle):** Dense smoke, fog, or spores.
    *   *Trigger:* Passive.
    *   *Rules:* Ranged attacks passing through or targeting someone inside this Zone suffer a **Bane** (-1d). The Zone grants **Partial Cover** to anyone inside it.
*   **Toxic (Hazard):** Poison gas, sewer fumes, or acid spray.
    *   *Trigger:* Starting a turn inside the Zone.
    *   *Rules:* Must test **Tough** against the **Zone Profile**. On a failure, they suffer the **Weakened** condition until they spend a Standard Action to catch their breath in a clean zone.
*   **Deep Water (Obstacle):** Flooded area or rapid currents.
    *   *Trigger:* Passive / Interactive.
    *   *Rules:* Traversing this Zone requires a **Move** action to travel only **1 Zone** (ignoring standard movement speed). If forced to swim or stay afloat, creatures must test **Tough** against the **Zone Profile** or begin drowning (taking **1 Wound** per round).

### 3.2. Predefined Opportunities (Tactical Features & Treats)
*   **High Ground (Tactical Feature):** A ledge, platform, or pile of crates.
    *   *Trigger:* Passive.
    *   *Rules:* Ranged attacks made from this Zone gain a **Boon** (+1d). Melee attacks made by enemies outside this Zone against targets inside this Zone suffer a **Bane** (-1d).
*   **Junk Pile (Treat):** Scrap metal, discarded weapons, or rubble.
    *   *Trigger:* Interactive (Standard Action: **Manipulate**).
    *   *Rules:* Goblins can spend a Standard Action (**Manipulate**) to search the pile (test **Notice** against the **Zone Profile**). On a success, they find a throw-able object (deals **1 damage** ranged) or a random piece of low-grade loot.
*   **Shadowy (Tactical Feature):** Dark alcoves or heavy curtains.
    *   *Trigger:* Passive.
    *   *Rules:* Goblins attempting to Hide in this Zone gain a **Boon** (+1d) on their **Slink** tests.
*   **Shoring (Interactive):** Structural supports or pillars.
    *   *Trigger:* Interactive (Standard Action: **Manipulate** or **Attack**).
    *   *Rules:* Goblins can spend a Standard Action to collapse the supports. This triggers a cave-in: the Zone gains the **Crumbling** hazard (a random target must test **Notice** against the **Zone Profile** each round or take **1 Wound**) and blocks all movement to adjacent zones until cleared.

---

## 4. Examples of Play

> **Example:** Grub and his Mob of Size 3 run from the town guards into a sewer tunnel designated as **Zone B**. The GM has set Zone B's profile to **Normal:2** and given it the **Narrow** and **Smoky** traits. Because Zone B has the **Narrow** trait, Grub's Mob is too big! Grub must either split the Mob, or the Mob suffers a **Bane** (-1d) on all attacks and physical tests, and their movement speed drops to 1 Zone. However, because the sewer tunnel is **Smoky**, the guards trying to shoot crossbows at them from the adjacent room suffer a **Bane** (-1d) because Grub's Mob has Partial Cover.

---

## 5. Alignment with Design Tenets

1.  **Fun at the Table:** Gives players and Mobs tactical, interactive toys on the battlefield (pushing enemies into fires, hiding in shadows, throwing junk).
2.  **Zero Post-Roll Math:** Modified rolls use the standard **Boon** and **Bane** systems, and difficulties map directly to **Easy/Normal/Hard** success states. No arithmetic is needed after dice are cast.
3.  **Embrace Chaos:** Hazards like **Slippery** mud or **Burning** oil can cause sudden, dramatic shifts in positioning and health, forcing players to adapt.
4.  **Goblin Flavor:** Goblins are small, so the **Narrow** constraint affects large enemy Mobs or Giant foes much more severely than a scrappy crew of runts. Searching a **Junk Pile** for garbage to throw is quintessentially goblinoid.

---

## 6. Edge Cases & Rules Lawyer Concerns
*   **GM Roll Mitigation:** All hazards are resolved using player-facing saving throws. GMs never roll to see if a hazard hits; they simply announce the trigger, and the affected player rolls to resist.
*   **Mob Damage Scaling:** Environmental hazards like **Burning** or **Crumbling** deal **1 Wound** to a PC or **1 Size damage** (killing one goblin unit) to a Mob. This ensures damage types remain consistent across the system.
*   **Mob Prone Interaction:** If a Mob is knocked **Prone** by slipping, it suffers **-1d on Dodge** and must spend **1 Move action** of its next Order to stand back up, mirroring PC rules.

---

## 7. Alternatives Considered
*   **Global Room Target:** We considered a single Target Number for the entire combat map (direct ICRPG port). However, Gobbos' zone-based layout makes it far more interesting to have different zones feel physically distinct (e.g., fighting on dry land vs. wading through sewer sludge).
*   **Dynamic GM Threat Rolls:** We rejected having fires or cave-ins roll "attack dice" against the players, as it violates the tenet of the GM never rolling dice in combat.

---

>> **GOBLIN VERDICT:** "If ya run into the fiery zone, yer pants catch fire! But if ya hide in the smoky zone, the tall-men can't shoot ya with their bows. Just don't bring the whole mob into the narrow pipe or you'll get stuck like a fat pig!"
