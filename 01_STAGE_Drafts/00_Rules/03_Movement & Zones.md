# Zones

In Gobbos, **Zones** are used to create a framework for movement, especially in combat. A Zone can be of any shape, but is often clearly defined by the environment, such as a room, a corridor, or a field. Sometimes a larger area is split into multiple Zones if the area is too large, or several smaller areas close to each other are considered a single Zone.

A player's movement is measured in number of Zones, and a normal movement speed is to move 2 Zones per round and action.

---

## Zone Profiles

Every Zone in an encounter is assigned a default **Zone Profile** consisting of a **Difficulty** and a **Target Number (TN)** (e.g., **Normal:1**, **Normal:2**, or **Hard:1**).

>> **THE ZONE PROFILE RULE:**
>> Any general environmental interaction, traversal, or search test attempted within a Zone defaults to using that Zone's Profile. GMs do not invent DCs for individual tasks; they simply use the Zone Profile.
>> *   *Example:* Climbing a wall, forcing a door, jumping a trench, or searching a junk pile in a Zone with a **Normal:2** profile all require **2 successes** on a **Normal** test.

GMs can adjust the Difficulty level of a specific task based on tools or circumstances using standard **Boons** and **Banes** (e.g., using professional climbing gear grants a **Boon** (+1d) to the traversal test, while a rusty lock imposes a **Bane** (-1d) on the test), but the base TN and Difficulty remain tied to the Zone itself.

---

## Zone Traits

A **Zone Trait** is a mechanical modifier or effect associated with a specific Zone. Traits represent either obstacles players must overcome or advantages they can exploit. All traits fall under two general categories:

### Problems (Hazards & Obstacles)
These are negative environmental features.
*   **Triggering:** Problems trigger passively (continuous effect while occupying the zone), on entry (as soon as a creature enters the zone), or at a specific phase in the round (e.g., End of Round).
*   **Resolution:** To avoid negative effects, a player must make a relevant test (typically **Slink** or **Tough**) against the **Zone Profile**. On a failure, they suffer Wounds (Grit Loss), or a negative **Condition**. 
*   **GM Rolling:** GMs never roll to see if a hazard succeeds; the GM simply announces the hazard's trigger and the affected player rolls to resist.
*   **Hazard Damage Scaling:** Environmental hazard damage scales by severity:
    *   **T1 Hazard (Minor):** Deals **1 damage** to a PC's Grit or a Mob's active health die on a failed test.
    *   **T2 Hazard (Dangerous):** Deals **2 damage**.
    *   **T3 Hazard (Lethal):** Deals **3 damage** or applies a severe condition.
    *   *Note:* Extreme catastrophic events (like a collapsing cave-in) can deal direct **Size damage** (removing the Mob's lowest-value D6).

### Opportunities (Tactical Features & Treats)
These are interactive or beneficial environmental features.
*   **Passive Benefits:** Some opportunities provide constant benefits (e.g., providing cover or granting a **Boon** to attacks).
*   **Interactive Benefits:** Goblins can interact with an opportunity by spending a Standard Action (**Manipulate** or **Attack**) and testing a relevant stat against the **Zone Profile** to yield a benefit.

---

## Predefined Zone Traits

GMs can customize battlefields by placing these standardized, modular traits onto Zones.

### 1. Static Environment (Terrain & Obstacles)

*   **Chasm / Pit (T3 Obstacle):** A gaping hole, trench, or cliff edge.
    *   *Trigger:* Attempting to cross, or being pushed toward the edge.
    *   *Rules:* Traversing requires a **Slink** test against the **Zone Profile**. On a failure, the creature falls in, taking **3 damage** and gaining the **Restrained** condition. Clambering out requires spending a Standard Action to test **Tough** against the profile.
*   **Deep Water (Obstacle):** Flooded chambers, sewer channels, or rapid rivers.
    *   *Trigger:* Passive / Interactive (for swimming).
    *   *Rules:* Traversing this Zone requires a **Move** action to travel only **1 Zone** (ignoring standard movement speed). If forced to swim or stay afloat (directly in the water without a boat or bridge), a creature starting their turn in this Zone must test **Tough** against the **Zone Profile** or begin drowning (taking **1 damage** per round).
*   **Narrow (Obstacle):** A tight crawlspace, pipe, or rocky crevice.
    *   *Trigger:* Passive.
    *   *Rules:* The maximum Mob size that can occupy this Zone without penalty is **Size 2**. Mobs of **Size 3+** suffer a **Bane** (-1d) to all attack rolls and physical tests while in this Zone, and their Movement is capped at **1 Zone**. Giant enemies cannot enter.
*   **Pillars / Statues (Tactical Feature):** Solid stone pillars or crumbling carvings.
    *   *Trigger:* Passive.
    *   *Rules:* Anyone occupying this Zone can declare they are taking cover behind a pillar (as a Free Action), granting them **Full Cover** against attacks coming from one specific adjacent Zone.
*   **Rubble (Obstacle):** Loose stones, steep scree, or collapsed vaults.
    *   *Trigger:* Traversing.
    *   *Rules:* Moving through this Zone costs double movement (spending 2 Zones' worth of movement speed to cross).
*   **Vertical Cliff (Obstacle):** A sheer stone wall, scaffold, or ladder.
    *   *Trigger:* Traversing vertically.
    *   *Rules:* Climbing requires a **Move** action and a **Slink** test against the **Zone Profile**. On a failure, the creature falls back to the bottom, taking **1 damage** for every Zone's worth of height fallen and landing **Prone**.

### 2. Dynamic Environment (Hazards & Triggers)

*   **Burning (T2 Hazard):** Spreading fire, hot lava pools, or burning oil.
    *   *Trigger:* Entering the Zone, or starting a turn inside it.
    *   *Rules:* Must pass a **Slink** test against the **Zone Profile** or take **2 damage** to Grit (PC) or active health die (Mob). Fire spreads to adjacent wooden/flammable zones at the End of Round on a roll of 5–6 on **1d6** (rolled by the GM or a player).
*   **Crumbling Ceiling (T3 Hazard):** Loose rock vaults, rotting timber supports, or ice stalactites.
    *   *Trigger:* Announce at Round Start or when triggered by structural damage.
    *   *Rules:* All creatures occupying the Zone must test **Slink** against the **Zone Profile**. On a failure, they take **3 damage** and are knocked **Prone**. After collapsing, the Zone permanently gains the **Rubble** trait.
*   **Howling Wind (T1 Hazard):** Heavy drafts, storm winds, or venting steam.
    *   *Trigger:* Passive.
    *   *Rules:* Ranged attacks passing through or targeting someone inside this Zone suffer a **Bane** (-1d). Moving against the direction of the wind requires a **Tough** test against the profile; on a failure, movement speed is halved.
*   **Quicksand / Mud (T2 Hazard):** Sticky tar pits, thick sewer sludge, or quicksand.
    *   *Trigger:* Entering the Zone.
    *   *Rules:* Must test **Slink** against the **Zone Profile**. On a failure, the creature gains the **Restrained** condition. Breaking free requires spending a Standard Action to test **Tough** against the profile.
*   **Slippery (Obstacle):** Smooth ice, wet grease, or organic slime.
    *   *Trigger:* Entering the Zone.
    *   *Rules:* Must test **Slink** against the **Zone Profile**. On a failure, the creature falls **Prone** and their movement ends immediately.
*   **Toxic Spores / Gas (T2 Hazard):** Poisonous sewer gases, acid clouds, or mold spores.
    *   *Trigger:* Starting a turn inside the Zone.
    *   *Rules:* Must test **Tough** against the **Zone Profile**. On a failure, they suffer the **Weakened** condition until they spend a Standard Action to catch their breath in a clean zone.

### 3. Opportunities (Treats & Cover)

*   **Hedges / Thickets (Tactical Feature):** Heavy brambles, bushes, or hanging tapestries.
    *   *Trigger:* Passive.
    *   *Rules:* Anyone inside this Zone gains **Partial Cover** (ranged attacks targeting them suffer a **Bane** (-1d), and they gain a **Boon** (+1d) to **Dodge** reactions).
*   **Junk Pile (Treat):** Stacks of dungeon scrap, refuse, or broken weapons.
    *   *Trigger:* Interactive (Standard Action: **Manipulate**).
    *   *Rules:* Goblins can search the pile (test **Brains** against the **Zone Profile**). On a success, they find a throw-able object (deals **1 damage** ranged) or a random piece of low-grade loot. Once successfully searched, the Junk Pile is exhausted and cannot be searched again during the raid.
*   **Shadowy (Tactical Feature):** Deep alcoves, heavy curtains, or dim corners.
    *   *Trigger:* Passive.
    *   *Rules:* Goblins attempting to Hide in this Zone gain a **Boon** (+1d) on their stealth-related **Slink** tests.
*   **Shoring (Interactive Opportunity):** Wooden structural beams supporting the ceiling.
    *   *Trigger:* Interactive (Standard Action: **Manipulate** or **Attack**).
    *   *Rules:* Goblins can collapse the beams. Test **Brains** (to sabotage) or make a successful melee attack against the **Zone Profile**. On a success, the Zone immediately gains the **Crumbling Ceiling** hazard (everyone in the zone tests **Slink** or takes **3 damage**), and all exits to adjacent Zones are blocked. Clearing a blocked exit requires spending a Standard Action to successfully test **Tough** against the **Zone Profile**.

---

## Examples of Play

These scenarios illustrate how different hazards, opportunities, and Mob rules play out at the table.

### Example 1: Slipping on the Ice (Slink Tests)
> **Example:** Grub (PC) and his **Size 3** Mob run from town guards into a frozen courtyard designated as **Zone A** (Profile: **Normal:2**; Trait: **Slippery**). 
> * **The PC:** Grub enters the zone and must make a Slink test. Grub has **Slink 2**, rolling **2d6** (Stat). He rolls `5, 5`—two successes! He keeps his footing.
> * **The Mob:** The Mob enters the zone. Mobs roll exactly **1d6** for **Slink** tests. The player rolls `5`—only one success! The Mob fails the test against the **Normal:2** profile. The Mob falls **Prone** and their movement ends immediately in the middle of the ice sheet.

### Example 2: Braving the Toxic Fumes (Tough Tests & Mob Scaling)
> **Example:** Snarl (PC) and her massive **Size 5** Mob are pursuing a dwarf through a sewer pipe designated as **Zone B** (Profile: **Normal:2**; Traits: **Toxic** and **Narrow**). They start their turn in the zone.
> * **The PC:** Snarl has **Tough 2**, rolling **2d6** (Stat). She rolls `6, 3`. The `6` explodes and she rolls another `3`. The total is one success—not enough for the **Normal:2** profile! Snarl fails and gains the **Weakened** condition.
> * **The Mob:** Because it is a Tough test, the Mob rolls **Size** dice (**5d6**). However, the zone has the **Narrow** trait, imposing a permanent **Bane** (-1d) on all physical tests. The Mob's dice pool is reduced to **4d6**. The player rolls `6, 5, 5, 2`. The `6` explodes and rolls a `4`. That is three successes! The Mob easily passes the test and is unaffected by the gas, their sheer numbers and mass helping them pull each other through.

### Example 3: Collapsing the Support (Shoring Opportunity)
> **Example:** Wizgog (PC) is cornered by a heavily armored knight in a crypt (**Zone C**, Profile: **Normal:1**; Trait: **Shoring**). Wizgog wants to collapse the ceiling on the knight.
> * **The Action:** Wizgog spends a Standard Action to smash the rotten wooden support column. Since this is an interactive opportunity, he tests **Brains** (his stat is 3, so he rolls **3d6**) against the zone's **Normal:1** profile.
> * **The Result:** He rolls `5, 2, 1`—one success! The column splinters. The Zone immediately triggers a cave-in (**Crumbling Ceiling**).
> * **The Resisting Tests:** 
>   * Wizgog tests Slink (**2d6**) and rolls `5, 1` (success), jumping clear of the debris.
>   * The Knight tests Slink. The GM rules the heavy armor imposes a **Bane** (-1d). The Knight rolls `3, 2` (failure). The Knight takes **3 damage** and is knocked **Prone**, buried under rubble.
>   * The adjacent exit is blocked, cutting off the knight's allies.
