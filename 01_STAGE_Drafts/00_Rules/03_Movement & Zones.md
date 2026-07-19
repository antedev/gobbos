# Movement, Zones, & Map Layout

The map architecture in **Gobbos** is designed to solve the "Panzer Brigade" dilemma: balancing a massive, chaotic horde of multiple players and 6 to 8 active squads without clogging the physical tabletop or turning a fast-paced rogue-lite delve into a slow traffic jam. 

The layout gives a clear, high-level sense of macro-exploration while dropping into highly dynamic, multi-level, gridless tactical theaters only when a fight breaks out.

---

## The Tabletop Layout (Visual Sketch)

At the physical gaming table, the components are arranged to keep macro-exploration and micro-skirmishes visually separated, ensuring clear command lines and zero clutter:

```
+---------------------------------------------------------------------------------+
|                                 THE GAMING TABLE                                |
+---------------------------------------------------------------------------------+
|                                                                                 |
|   [ Lair Sheet & Communal Hoard ]                     [ GM Screen ]             |
|   Tracks pooled Loot, Scrap, and Lair rooms.          Reference tables,         |
|                                                       encounter notes.          |
|                                                                                 |
|   +-----------------------------+         +---------------------------------+   |
|   |     MACRO MINIMAP           |         |        ACTIVE CLASH CLUSTER     |   |
|   |     (Point-Crawl Nodes)     |         |        (Micro Battleground)     |   |
|   |                             |         |                                 |   |
|   |  [Node A] <-- (Locked) -->  |         |   +---------+     +---------+   |   |
|   |     |                       |         |   | Zone 1  |     | Zone 2  |   |   |
|   |     v                       |         |   | Balcony |<--->| Hallway |   |   |
|   |  [Node B] (Horde Token)     |         |   | [Cover] |     | [Narrow]|   |   |
|   |     |                       |         |   +---------+     +---------+   |   |
|   |     v                       |         |        ^               ^        |   |
|   |  [Node C] (Active Encounter)|         |        |               |        |   |
|   |                             |         |        v               v        |   |
|   |                             |         |   +-------------------------+   |   |
|   |                             |         |   |         Zone 3          |   |   |
|   |                             |         |   |        Courtyard        |   |   |
|   |                             |         |   |        [Burning]        |   |   |
|   |                             |         |   +-------------------------+   |   |
|   +-----------------------------+         +---------------------------------+   |
|                                                                                 |
|                                                                                 |
|   [Player 1: Boss + Mob]        [Player 2: Boss + Mob]     [Player 3: Boss + Mob] |
|   - Boss Character Sheet        - Boss Character Sheet     - Boss Character Sheet |
|   - Mob D6 Health Tracker       - Mob D6 Health Tracker    - Mob D6 Health Tracker|
|   - Active Quirks & Gear        - Active Quirks & Gear     - Active Quirks & Gear |
|                                                                                 |
+---------------------------------------------------------------------------------+
```

---

## Core Architectural Concept: The Hybrid Map System

The physical table is split into two distinct visual tracking spaces: the macro-world where the horde travels, and the active micro-world where the blood spills.

### 1. The Macro Minimap (The Point-Crawl Blueprint)

Instead of a sprawling, room-by-room grid layout, the overall raid location (castle, village, or crypt) is tracked on a central node map.

*   **The Scale:** Individual goblin tokens do not live here. Instead, a single token representing the bulk of the horde moves along connected nodes.
*   **The Function:** It shows the pathways between major sections of the raid, locked doorways, known hazards, and designated escape zones used for tactical retreats. It tracks the progression of the raid at a glance without requiring any drawn architecture.

### 2. The Micro Battleground (Interconnected Clash Clusters)

When an encounter triggers at a node, the GM deploys a localized "Clash Cluster" consisting of 3 to 4 abstract, interconnected physical tiles or cards to represent the immediate environment.

*   **The Scale:** This is where the actual goblin boss miniatures and physical piles of **d6** squad dice are placed to resolve combat.
*   **The Fluidity:** A single battle easily bleeds across these local zones. For example, a street skirmish can seamlessly transition into a house interior or climb up onto a rooftop zone in real-time.

---

## Abstract, Gridless Zones

In Gobbos, [[Zones]] are used to create a framework for movement, especially in combat. A Zone can be of any shape, but is often clearly defined by the environment, such as a room, a corridor, or a field. 

A player's movement is measured in number of Zones, and a normal movement speed is to move 2 Zones per round and action.

---


## Zone Profiles

Every Zone in an encounter is assigned a default [[Zone Profile]] consisting of a [[Difficulty]] and a [[Target Number (TN)]] (e.g., **5+/1**, **5+/2**, or **6/1**).

>> **THE ZONE PROFILE RULE:**
>> Any general environmental interaction, traversal, or search test attempted within a Zone defaults to using that Zone's Profile. GMs do not invent DCs for individual tasks; they simply use the Zone Profile.
>> *   *Example:* Climbing a wall, forcing a door, jumping a trench, or searching a junk pile in a Zone with a **5+/2** profile all require **2 successes** on a [[Normal]] (5+) test.

GMs can adjust the Difficulty level of a specific task based on tools or circumstances using standard [[Boon|Boons]] and [[Bane|Banes]] (e.g., using professional climbing gear grants a [[Boon]] (+1d) to the traversal test, while a rusty lock imposes a [[Bane]] (-1d) on the test), but the base TN and Difficulty remain tied to the Zone itself.

---

## Zone Traits

A [[Zone Trait]] is a mechanical modifier or effect associated with a specific Zone. Traits represent either obstacles players must overcome or advantages they can exploit. All traits fall under two general categories:

### Problems (Hazards & Obstacles)
These are negative environmental features.
*   **Triggering:** Problems trigger passively (continuous effect while occupying the zone), on entry (as soon as a creature enters the zone), or at a specific phase in the round (e.g., End of Round).
*   **Resolution:** To avoid negative effects, a player must make a relevant test (typically [[Slink]] or [[Tough]]) against the [[Zone Profile]]. On a failure, they suffer Wounds (Grit Loss), or a negative [[Condition]]. 
*   **GM Rolling:** GMs never roll to see if a hazard succeeds; the GM simply announces the hazard's trigger and the affected player rolls to resist.
*   **Hazard Damage Scaling:** Environmental hazard damage scales by severity:
    *   **T1 Hazard (Minor):** Deals 1 damage to a PC's Grit or a Mob's active health die on a failed test.
    *   **T2 Hazard (Dangerous):** Deals **2 damage**.
    *   **T3 Hazard (Lethal):** Deals **3 damage** or applies a severe condition.
    *   *Note:* Extreme catastrophic events (like a collapsing cave-in) can deal direct **Size damage** (removing the Mob's lowest-value D6).

### Opportunities (Tactical Features & Treats)
These are interactive or beneficial environmental features.
*   **Passive Benefits:** Some opportunities provide constant benefits (e.g., providing cover or granting a [[Boon]] to attacks).
*   **Interactive Benefits:** Goblins can interact with an opportunity by spending a Standard Action ([[Manipulate]] or [[Attack]]) and testing a relevant stat against the [[Zone Profile]] to yield a benefit.

---

## Predefined Zone Traits

GMs can customize battlefields by placing these standardized, modular traits onto Zones.

### 1. Static Environment (Terrain & Obstacles)

*   **Chasm / Pit (T3 Obstacle):** A gaping hole, trench, or cliff edge.
    *   *Trigger:* Attempting to cross, or being pushed toward the edge.
    *   *Rules:* Traversing requires a [[Slink]] test against the [[Zone Profile]]. On a failure, the creature falls in, taking **3 damage** and gaining the [[Restrained]] condition. Clambering out requires spending a Standard Action to test [[Tough]] against the profile.
*   **Deep Water (Obstacle):** Flooded chambers, sewer channels, or rapid rivers.
    *   *Trigger:* Passive / Interactive (for swimming).
    *   *Rules:* Traversing this Zone requires a [[Move]] action to travel only 1 [[Zone]] (ignoring standard movement speed). If forced to swim or stay afloat (directly in the water without a boat or bridge), a creature starting their turn in this Zone must test [[Tough]] against the [[Zone Profile]] or begin drowning (taking 1 damage per round).
*   **Narrow (Obstacle):** A tight crawlspace, pipe, or rocky crevice.
    *   *Trigger:* Passive.
    *   *Rules:* The maximum Mob size that can occupy this Zone without penalty is **Size 2**. Mobs of **Size 3+** suffer a [[Bane]] (-1d) to all attack rolls and physical tests while in this Zone, and their Movement is capped at 1 [[Zone]]. Giant enemies cannot enter.
*   **Pillars / Statues (Tactical Feature):** Solid stone pillars or crumbling carvings.
    *   *Trigger:* Passive.
    *   *Rules:* Anyone occupying this Zone can declare they are taking cover behind a pillar (as a Free Action), granting them [[Full Cover]] against attacks coming from one specific adjacent Zone.
*   **Rubble (Obstacle):** Loose stones, steep scree, or collapsed vaults.
    *   *Trigger:* Traversing.
    *   *Rules:* Moving through this Zone costs double movement (spending 2 Zones' worth of movement speed to cross).
*   **Vertical Cliff (Obstacle):** A sheer stone wall, scaffold, or ladder.
    *   *Trigger:* Traversing vertically.
    *   *Rules:* Climbing requires a [[Move]] action and a [[Slink]] test against the [[Zone Profile]]. On a failure, the creature falls back to the bottom, taking 1 damage for every Zone's worth of height fallen and landing [[Prone]].

### 2. Dynamic Environment (Hazards & Triggers)

*   **Burning (T2 Hazard):** *Spreading fire, hot lava pools, or burning oil.* | `[Fire]`, `[Gaseous]`
    *   *Trigger:* Entering the Zone, or starting a turn inside it.
    *   *Rules:* The Zone imposes the active states of `[Fire]` (attacks deal **+1 Success**; ignites Zone) and `[Gaseous]` (ranged attacks suffer a [[Bane]]). Anyone entering or starting their turn in this Zone must pass a [[Slink]] test against the [[Zone Profile]] or take **2 damage** to Grit (PC) or active health die (Mob) and gain the [Burning] state. Fire spreads to adjacent wooden/flammable zones at the End of Round on a roll of 5–6 on **1d6** (rolled by the GM or a player).
*   **Crumbling Ceiling (T3 Hazard):** *Loose rock vaults, rotting timber supports, or ice stalactites.* | `[Crushing]`
    *   *Trigger:* Announce at Round Start or when triggered by structural damage.
    *   *Rules:* The Zone imposes the active state of `[Crushing]` (restricted movement, attacks are Easy). All creatures occupying the Zone must test [[Slink]] against the [[Zone Profile]]. On a failure, they take **3 damage** and are knocked [[Prone]]. After collapsing, the Zone permanently gains the **Rubble** trait.
*   **Howling Wind (T1 Hazard):** *Heavy drafts, storm winds, or venting steam.* | `[Gale]`
    *   *Trigger:* Passive.
    *   *Rules:* The Zone imposes the active state of `[Gale]`. All ranged attacks passing through or targeting someone inside this Zone suffer a [[Bane]] (-1d). Moving against the direction of the wind requires a [[Tough]] test against the profile; on a failure, movement speed is halved.
*   **Quicksand / Mud (T2 Hazard):** *Sticky mud or waterlogged silt.* | `[Wet]`, `[Sinking]`
    *   *Trigger:* Entering the Zone.
    *   *Rules:* The Zone imposes the active states of `[Wet]` (conducts electricity, extinguishes fire) and `[Sinking]` (downward drag). Any creature entering or moving in the Zone must test [[Slink]] against the [[Zone Profile]]. On a failure, they gain the [[Restrained]] condition. Breaking free requires spending a Standard Action to test [[Tough]] against the profile.
*   **Slippery (Obstacle):** *Smooth ice, wet grease, or organic slime.* | `[Slick]`
    *   *Trigger:* Entering the Zone.
    *   *Rules:* The Zone imposes the active state of `[Slick]`. Any creature attempting to move into or out of the Zone must test [[Slink]] against the [[Zone Profile]]. On a failure, they fall [[Prone]] and their movement ends immediately.
*   **Toxic Spores / Gas (T2 Hazard):** *Poisonous sewer gases, acid clouds, or mold spores.* | `[Toxic]`, `[Gaseous]`
    *   *Trigger:* Starting a turn inside the Zone.
    *   *Rules:* The Zone imposes the active states of `[Toxic]` (inflicts [[Weakened]] condition) and `[Gaseous]` (creates dark screen). All creatures starting their turn inside this Zone must test [[Tough]] against the [[Zone Profile]]. On a failure, they suffer the [[Weakened]] condition until they spend a Standard Action to catch their breath in a clean zone.

### 3. Environmental Blueprints (Weather & Complex Hazards)

GMs can construct complex, dynamic weather events or composite environmental hazards by layering multiple tags. The combined rules resolve simultaneously based on the active tags:

*   **Blizzard (T2 Hazard):** *A freezing, howling storm of snow and wind that swallows all sight.* | `[Chilled]`, `[Blinding]`, `[Slick]`
    *   *Rules:* The Zone is treated as freezing, blind, and slippery. Movement is halved (`[Chilled]`), ranged attacks are Hard and Dodge reactions are impossible (`[Blinding]`), and moving requires a [[Slink]] test against the profile or the creature falls [[Prone]] (`[Slick]`).
*   **Tornado (T3 Hazard):** *A roaring vortex of wind that sweeps debris and creatures into the air.* | `[Gale]`, `[Weightless]`, `[Loud]`
    *   *Rules:* The wind lifts creatures off the ground (`[Weightless]`), creating a deafening roar that fails stealth and verbal orders (`[Loud]`), while deflecting all ranged attacks (`[Gale]`). Creatures are swept up and tossed about; leaving the zone or stabilizing requires a [[Tough]] test against the [[Zone Profile]].
*   **Hurricane (T3 Hazard):** *Torrential rain combined with brutal, slamming winds.* | `[Wet]`, `[Gale]`, `[Loud]`
    *   *Rules:* Rain douses all fire and conducts sparks (`[Wet]`), violent wind gusts deflect ranged attacks (`[Gale]`), and the storm's noise drowns out all orders and stealth attempts (`[Loud]`).
*   **Sandstorm (T2 Hazard):** *Thick, choking clouds of abrasive sand and dust.* | `[Blinding]`, `[Gale]`
    *   *Rules:* Vision is blocked entirely (`[Blinding]`), making ranged attacks Hard and Dodge impossible, while high-velocity winds deflect projectiles and blow away loose items (`[Gale]`).
*   **Thunderstorm (T2 Hazard):** *Soaking downpour paired with crackling static electricity.* | `[Wet]`, `[Shock]`
    *   *Rules:* Everything is completely soaked (`[Wet]`). Any static spark or electrical attack instantly triggers the `[Shock]` tag's conduction effect, making all attacks against wet targets in the Zone **Easy (4+)** for 1 round.
*   **Wildfire (T2 Hazard):** *Searing heat, open flames, and thick screens of smoke.* | `[Fire]`, `[Gaseous]`, `[Loud]`
    *   *Rules:* Flames deal automatic damage and place burning effects (`[Fire]`), choking smoke obscures vision and blocks ranged attacks (`[Gaseous]`), and the roaring timber prevents quiet action (`[Loud]`).
*   **Flash Flood (T2 Hazard):** *A sudden wall of high-velocity water.* | `[Wet]`, `[Fast]`
    *   *Rules:* Water washes away chemicals and coatings (`[Wet]`) while rushing down-zone, allowing creatures to move 1 Zone as a Free Action (`[Fast]`) but carrying unattended items and creatures away in the torrent at the End of Round unless they pass a [[Tough]] test.
*   **Earthquake / Cave-In (T3 Hazard):** *Violent shaking and falling stone debris.* | `[Vibrating]`, `[Crushing]`
    *   *Rules:* The ground shakes violently, disrupting spellcasting and notice checks (`[Vibrating]`), while falling rocks pin creatures and slow movement to a maximum of 1 Zone (`[Crushing]`).
*   **Smog Marsh (T2 Hazard):** *A swamp filled with thick sewer gas where light dies.* | `[Wet]`, `[Toxic]`, `[Dark]`
    *   *Rules:* Waterlogged sumps conduct electricity (`[Wet]`), sewer gas inflicts the [[Weakened]] condition (`[Toxic]`), and poor visibility imposes a **Bane (-1d)** on attacks and notice checks (`[Dark]`).
*   **Haunted Woods (T2 Hazard):** *A dark forest filled with uncanny dread and phantom hands.* | `[Terrifying]`, `[Haunted]`
    *   *Rules:* Eldritch whispers inflict the [[Terrified]] condition (`[Terrifying]`), while phantom hands impose a **Bane (-1d)** to Slink and Mouth tests (`[Haunted]`).
*   **Acid Mire (T2 Hazard):** *A factory waste dump that slips and melts boots off.* | `[Acidic]`, `[Slick]`
    *   *Rules:* Acidic runoff eats away at armor reduction on a hit (`[Acidic]`), while slippery mud causes creatures to fall [[Prone]] on a failed Slink test (`[Slick]`).

### 4. Opportunities (Treats & Cover)

*   **Hedges / Thickets (Tactical Feature):** Heavy brambles, bushes, or hanging tapestries.
    *   *Trigger:* Passive.
    *   *Rules:* Anyone inside this Zone gains [[Partial Cover]] (ranged attacks targeting them suffer a [[Bane]] (-1d), and they gain a [[Boon]] (+1d) to [[Dodge]] reactions).
*   **Junk Pile (Treat):** Stacks of dungeon scrap, refuse, or broken weapons.
    *   *Trigger:* Interactive (Standard Action: [[Manipulate]]).
    *   *Rules:* Goblins can search the pile (test [[Brains]] against the [[Zone Profile]]). On a success, they find a throw-able object (deals 1 damage ranged) or a random piece of low-grade loot. Once successfully searched, the Junk Pile is exhausted and cannot be searched again during the raid.
*   **Shadowy (Tactical Feature):** Deep alcoves, heavy curtains, or dim corners.
    *   *Trigger:* Passive.
    *   *Rules:* Goblins attempting to Hide in this Zone gain a [[Boon]] (+1d) on their stealth-related [[Slink]] tests.
*   **Shoring (Interactive Opportunity):** Wooden structural beams supporting the ceiling.
    *   *Trigger:* Interactive (Standard Action: [[Manipulate]] or [[Attack]]).
    *   *Rules:* Goblins can collapse the beams. Test [[Brains]] (to sabotage) or make a successful melee attack against the [[Zone Profile]]. On a success, the Zone immediately gains the **Crumbling Ceiling** hazard (everyone in the zone tests [[Slink]] or takes **3 damage**), and all exits to adjacent Zones are blocked. Clearing a blocked exit requires spending a Standard Action to successfully test [[Tough]] against the [[Zone Profile]].

---

## Examples of Play

These scenarios illustrate how different hazards, opportunities, and Mob rules play out at the table.

### Example 1: Slipping on the Ice (Slink Tests)
> **Example:** Grub (PC) and his **Size 3** Mob run from town guards into a frozen courtyard designated as **Zone A** (Profile: **5+/2**; Trait: **Slippery**). 
> * **The PC**: Grub enters the zone and must make a Slink test. Grub has **Slink 2**, rolling **2d6** (Stat). He rolls `5, 5`—two successes! He keeps his footing.
> * **The Mob**: The Mob enters the zone. Mobs roll exactly **1d6** for [[Slink]] tests. The player rolls `5`—only one success! The Mob fails the **5+/2** Slink test. The Mob falls [[Prone]] and their movement ends immediately in the middle of the ice sheet.

### Example 2: Braving the Toxic Fumes (Tough Tests & Mob Scaling)
> **Example:** Snarl (PC) and her massive **Size 5** Mob are pursuing a dwarf through a sewer pipe designated as **Zone B** (Profile: **5+/2**; Traits: [Toxic] and **Narrow**). They start their turn in the zone.
> * **The PC**: Snarl has **Tough 2**, rolling **2d6** (Stat). She rolls `6, 3`. The `6` explodes and she rolls another `3`. The total is one success—not enough for the **5+/2** profile! Snarl fails the test and gains the [[Weakened]] condition.
> * **The Mob**: Because it is a Tough test, the Mob rolls [[Size]] dice (**5d6**). However, the zone has the **Narrow** trait, imposing a permanent [[Bane]] (-1d) on all physical tests. The Mob's dice pool is reduced to **4d6**. The player rolls `6, 5, 5, 2`. The `6` explodes and rolls a `4`. That is three successes! The Mob easily passes the test and is unaffected by the gas, their sheer numbers and mass helping them pull each other through.

### Example 3: Collapsing the Support (Shoring Opportunity)
> **Example:** Wizgog (PC) is cornered by a heavily armored knight in a crypt (**Zone C**, Profile: **5+/1**; Trait: **Shoring**). Wizgog wants to collapse the ceiling on the knight.
> * **The Action**: Wizgog spends a Standard Action to smash the rotten wooden support column. Since this is an interactive opportunity, he tests [[Brains]] (his stat is 3, so he rolls **3d6**) against the zone's **5+/1** profile.
> * **The Result**: He rolls `5, 2, 1`—one success! The column splinters. The Zone immediately triggers a cave-in (**Crumbling Ceiling**).
> * **The Resisting Tests**: 
>   * Wizgog tests Slink (**2d6**) and rolls `5, 1` (success), jumping clear of the debris.
>   * The Knight tests Slink. The GM rules the heavy armor imposes a [[Bane]] (-1d). The Knight rolls `3, 2` (failure). The Knight takes **3 damage** and is knocked [[Prone]], buried under rubble.
>   * The adjacent exit is blocked, cutting off the knight's allies.

---

## Background Node Resolution (The Chaos Tick)

If a player chooses to abandon a Mob in a previously cleared node on the macro minimap (for example, leaving them behind to forage for treasure or guard a chokepoint while the main party moves forward), that node is physically swept from the main table's active tactical space. 

Because they lack a Boss to command them, the split-off Mob is tracked purely on the macro node map. They default entirely to their automated Priority AI list:

1. **Survival**
2. **Loot/Eat**
3. **Violence**
4. **Trash Stuff**
5. **Wander Off**

### Resolving the Chaos Tick

At the end of each combat round, the player resolves the unsupervised Mob's actions using the **Chaos Tick**.

>> **THE CHAOS TICK RULE:**
>> Roll a number of **d6** equal to the unsupervised Mob's current [[Size]]. The Target Number and Difficulty default to the cleared zone's Profile (typically **5+/1**). 
>> *   **Successes (5+)**: Count successes to resolve the Priority AI's progress.
>> *   **Ones (1s)**: Each **1** rolled represents growing chaos and bickering. Tally the **1s** and consult the **Gobbo Mischief Table** below. Each **1** also adds **1 die** to the communal [[Bangaranga Pool]] as the background racket hypes up the horde.
>> *   **The Farkle**: If the roll yields **zero successes** and **two or more 1s**, the Mob fumbles catastrophically, triggering a disastrous event.

### The Gobbo Mischief Table (Tally of 1s)

| 1s Rolled | Mischief Result | Mechanical Outcome |
| :--- | :--- | :--- |
| **0** | **Smooth Operations** | No chaos! Gobbos cooperate perfectly. |
| **1** | **Bickering** | Goblins fight over a shiny rock. The Mob takes 1 damage to its active health die. |
| **2** | **Tasting Time** | They eat glowing mushrooms or lick rusty gears. The Mob gains the [[Weakened]] condition. |
| **3** | **Straying** | A few runts wander off into the dark. The Mob's [[Size]] decreases by 1. |
| **4+** | **Mutiny / Riot** | The Mob tears itself apart or rebels. The Mob becomes [[Uncontrolled]] and hostile to all Gangs, splitting into two smaller hostile mobs or wandering off the map entirely. |

### Resolution of Successes (5+ on Normal)

*   **0 Successes:** The Mob gets distracted pick-nosing. No progress is made.
*   **1 Success:** The Mob accomplishes a basic task. If foraging, they add 1d6 [[Scrap]] to the Hoard, or they heal **1d6 damage** on their health dice by eating old rations found in the zone.
*   **2 Successes:** They find a cache of useful garbage. Add 2d6 [[Scrap]] to the Hoard, or find a low-grade [[Oddity]].
*   **3+ Successes:** Outstanding teamwork! The Mob secures the node, making future travel through it **Safe** (no hazard checks required), and finds a piece of **Standard Loot**.
