# Tabletop & Map Layout: Mission Statement

The map architecture in **Gobbos** is designed to solve the "Panzer Brigade" dilemma: balancing a massive, chaotic horde of multiple players and 6 to 8 active squads without clogging the physical tabletop or turning a fast-paced rogue-lite delve into a slow traffic jam. 

The layout aims to give a clear, high-level sense of macro-exploration while dropping into highly dynamic, multi-level, gridless tactical theaters only when a fight breaks out.

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

## Key Design Choices Made So Far

### 1. Abstract, Gridless Zones

*   **Environmental Geometry:** Movement and combat range are completely decoupled from square counting or measuring tapes. A zone can be any shape or size, naturally defined by the fiction (e.g., a hallway, a courtyard, a balcony).
*   **High-Velocity Movement:** Standard movement speed is measured flatly by the number of zones crossed. A normal action allows a goblin to cross 2 zones, meaning characters can reposition across entire multi-level environments in a single heartbeat.

### 2. Physical Zone Attributes (Tags)

Every deployed card or tile in a Clash Cluster can be modified by explicit traits that dictate how the rules shift inside that specific space:

*   **Structural Cover:** Zones dictate native protective elements, tracking whether players have access to `[Partial Cover]` (imposing a **Bane** (-1d) on ranged attacks) or `[Full Cover]` (completely blocking line of sight).
*   **Tactical Hazards:** Danger attributes like spreading fire, toxic smoke, or water are assigned directly to the zones themselves, altering movement or dealing damage to anyone inside.
*   **Architecture Limits:** Certain zones possess spatial restrictions like `[Narrow]`, which mechanically prevent massive goblin mobs from pushing through unless the player spends an action to split them into smaller, lower-size squads.

### 3. Physical Boundaries Enforced by Character Stats

The layout of the active zones directly interacts with the core leadership statistics of the goblin bosses:

*   **The Line-of-Sight Snapping:** To issue an active Order to a mob, the boss must physically see at least a portion of the squad. Moving a mob deep into a separate room card where a solid wall blocks visual contact breaks command instantly.
*   **The Shouting Distance Boundary:** Command range is physically mapped to the layout. 
    *   Giving an order to a mob in the same zone succeeds automatically. 
    *   Shouting an order to a mob up to a distance equal to the boss's **Mouth** stat is a **Normal** test. 
    *   Pushing a mob 1 zone further than that shifts the difficulty to **Hard**.
    *   Anything beyond that becomes impossible to control.

### 4. Background Node Resolution (The Chaos Tick)

*   **The Unsupervised Script:** If a greedy player chooses to abandon a mob in a previously cleared node on the minimap to forage for treasure while the main party moves forward, that zone is physically wiped from the main table space.
*   **The Chaos Tick:** The split-off mob is tracked purely on the macro node map. Because they lack a boss to command them, they default entirely to their automated Priority AI list:
    
    1. **Survival**
    2. **Loot/Eat**
    3. **Violence**
    4. **Trash Stuff**
    5. **Wander Off**
    
    The player simply rolls their mob's dice pool directly on the minimap node during the round closure to see what mischief or wealth they generated in the background.

---

## Mechanical Draft: Resolving the Chaos Tick

When a Mob is left unsupervised at a minimap node, the player resolves their actions at the end of each combat round using the **Chaos Tick**.

>> **THE CHAOS TICK RULE:**
>> Roll a number of **d6** equal to the unsupervised Mob's current **Size**. The Target Number and Difficulty default to the cleared zone's Profile (typically **Normal:1**). 
>> *   **Successes (5+):** Count successes to resolve the Priority AI's progress.
>> *   **Ones (1s):** Each **1** rolled represents growing chaos and bickering. Tally the **1s** and consult the **Gobbo Mischief Table** below.
>> *   **The Farkle:** If the roll yields **zero successes** and **two or more 1s**, the Mob fumbles catastrophically, triggering a disastrous event.

### The Gobbo Mischief Table (Tally of 1s)

| 1s Rolled | Mischief Result | Mechanical Outcome |
| :--- | :--- | :--- |
| **0** | **Smooth Operations** | No chaos! Gobbos cooperate perfectly. |
| **1** | **Bickering** | Goblins fight over a shiny rock. The Mob takes **1 damage** to its active health die. |
| **2** | **Tasting Time** | They eat glowing mushrooms or lick rusty gears. The Mob gains the **Weakened** condition. |
| **3** | **Straying** | A few runts wander off into the dark. The Mob's **Size** decreases by 1. |
| **4+** | **Mutiny / Riot** | The Mob tears itself apart or rebels. The Mob becomes **Uncontrolled** and hostile to all Gangs, splitting into two smaller hostile mobs or wandering off the map entirely. |

### Resolution of Successes (5+ on Normal)

*   **0 Successes:** The Mob gets distracted pick-nosing. No progress is made.
*   **1 Success:** The Mob accomplishes a basic task. If foraging, they add **1d6 Scrap** to the Hoard, or they heal **1d6 damage** on their health dice by eating old rations found in the zone.
*   **2 Successes:** They find a cache of useful garbage. Add **2d6 Scrap** to the Hoard, or find a low-grade **Oddity**.
*   **3+ Successes:** Outstanding teamwork! The Mob secures the node, making future travel through it **Safe** (no hazard checks required), and finds a piece of **Standard Loot**.

---

## The Bangaranga Pool (The Rowdy Crowd Engine)

Gobbos don't fight out of professional discipline; they fight out of rowdy excitement. When the crowd gets hyped by awesome stunts, hilarious disasters, or massive payouts, their collective noise and rowdiness builds up. This is represented by a physical bowl in the center of the table containing a shared pool of dice: the **Bangaranga Pool**.

### 1. Seeding the Pool (Start of Raid)

At the start of a raid, the Bangaranga Pool is seeded with a baseline level of chaotic energy based on the size and composition of the raiding party:

*   **Rowdy Baseline:** The pool starts with **1 die** for each player Boss in the raid party.
*   **Crowd Bonus:** Add **+1 die** for each Mob of **Size 3 or 4** (Troop/Gang) in the raid party.
*   **Riot Bonus:** Add **+2 dice** for each Mob of **Size 5** (Company) in the raid party.

>> **Example Starting Pool:**
>> A 3-player raid party has one Size 3 Mob, one Size 4 Mob, and one Size 2 Mob. The starting Bangaranga Pool is **5 dice** (3 baseline + 1 + 1 + 0). This ensures the party starts rowdy and can use the pool immediately!

### 2. Loading the Bangaranga Pool (Hype Triggers)

Dice are added to the physical Bangaranga Pool during a raid when notable events hype up the horde:

*   **Critical Successes:** Any player rolls a Critical Success (**4+ successes** on a single roll). (+1 Bangaranga Die).
*   **Fumbles:** Any player fumbles a test (zero successes and two or more 1s). The mob finds the failure hilarious! (+2 Bangaranga Dice).
*   **Defeating a Notable Enemy:** Defeating an enemy with the `[Notable]` or `[Big Threat]` tag (telegraphed by the GM or encounter profile). (+1 Bangaranga Die).
*   **Claiming a Big Loot Cache:** Looting a chest, room, or zone with the `[Big Loot]` or `[Hoard]` tag. (+1 Bangaranga Die).
*   **Chaos Ticks:** When an unsupervised Mob rolls **1s** during their background Node Resolution, their rowdy background partying adds to the noise. (Each **1** rolled adds **1 Bangaranga Die**).

### 3. Tapping the Pool & The Bangaranga Tax

Before rolling any test, a player can choose to take a number of dice from the Bangaranga Pool (up to a maximum equal to their Boss's **Grunt** stat) and add them to their current test's dice pool. 

However, using the crowd's energy for mundane tasks is considered "cheating" and costs a premium:

*   **No Tax:** If the number of Bangaranga dice taken is **less than or equal to the Target Number (TN)** of the test, it costs nothing extra.
*   **The Bangaranga Tax (+1 Die):** If the number of Bangaranga dice taken is **greater than the test's TN**, it costs **1 extra die** from the pool as a tax. This tax die is simply removed from the pool and discarded back to the box (not rolled).
*   **Tax Availability:** If the pool does not contain enough dice to cover both the dice rolled and the tax die, the player cannot take that many dice.

>> **Example (TN 2 Test):**
>> *   If you take **1 or 2 Bangaranga dice**, it costs no tax. You simply take them from the pool and roll them.
>> *   If you want to take **3 Bangaranga dice** (to guarantee success), 3 is greater than the TN of 2. You must pay a **1 die tax**. This requires a total of **4 dice** to be present in the pool. 3 dice are rolled, 1 die is discarded, and 4 dice are removed from the pool in total.

### 3. Rolling Bangaranga Dice

Bangaranga Dice must be of a distinct color (e.g., bright red or green). They carry wild, festive power:

*   **Double Exploding 6s:** Every **6** rolled on a Bangaranga Die counts as **1 success**, but it **explodes twice** (meaning you immediately roll *two* additional regular dice instead of one, which can themselves succeed or explode normally!).

### 4. The Disappointment of Failure (The Blowback)

*   **Riding the Wave (Success):** If the overall test **succeeds** (reaches the Target Number), the rowdy energy is harnessed perfectly. The crowd cheers, you look awesome, and any negative dice (1s) are completely ignored.
*   **Disappointed Gobbos (Failure):** If the overall test **fails**, the crowd is deeply disappointed that you failed to make use of their Bangaranga energy:
    *   **Grunt Loss:** You lose **1 Grunt** instantly as the goblins mock your flat performance, temporarily reducing your maximum command size.
    *   **Party Fouls:** If the failed roll also included any **1s** on the Bangaranga dice, the disappointed crowd gets out of control. You must roll **1d6** on the **Party Foul Table** below:
        
        | Roll | Party Foul | Mechanical Outcome |
        | :--- | :--- | :--- |
        | **1-2** | **Crowd-Surf Fail** | The mob tries to shove you around, but drops you. You land **Prone** and take **1 damage**. |
        | **3-4** | **Tomato Shower** | Gobbos hurl trash and rotten fruit. You suffer a **Bane** (-1d) on your next action. |
        | **5-6** | **Sticky Fingers** | In the commotion, a goblin pickpockets you. A random item in your inventory is stolen and carried by the mob until you spend an action to snatch it back. |