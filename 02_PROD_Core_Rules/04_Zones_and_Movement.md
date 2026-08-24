# Zones, Movement, and Environment

*Battlefields in Gobbos are dynamic, chaotic playgrounds where verticality, collapsing scenery, and hazardous obstacles matter far more than measuring inches on a grid. Goblins scurry through pipes, leap across burning chasms, and hide behind crumbling statues to outmaneuver taller, stronger foes.*

---

## Zone Topology & Spatial Abstraction

Tactical combat and exploration in **Gobbos** operate on an abstract node graph rather than a square or hex grid. The physical environment is divided into discrete, bounded spatial units called **Zones**.

```
+-------------------+       +-------------------+       +-------------------+
|      Zone A       |       |      Zone B       |       |      Zone C       |
|    Rooftop Node   |<=====>|  Courtyard Node   |<=====>|  Sewer Pipe Node  |
| [Pillars] [5+/1]  |       | [Burning] [5+/2]  |       |  [Narrow] [6/1]   |
+-------------------+       +-------------------+       +-------------------+
```

### Discrete Tactical Nodes
A **Zone** represents a distinct environmental feature or bounded room, such as a tavern taproom, a raised wooden balcony, a slippery courtyard, a sewer tunnel, or a narrow rooftop. 
*   **Intra-Zone Distance (Engaged):** All creatures, allies, hazards, and loot within the same Zone are considered adjacent and engaged with one another. Moving between targets within the same Zone costs no additional movement.
*   **Inter-Zone Distance (Node Steps):** Distance between separate locations is measured strictly as the integer number of connected Zone boundaries (steps) along the shortest available path.
*   **Adjacency & Connectivity:** Two Zones are adjacent if they share a direct spatial connection (a doorway, an open archway, a flight of stairs, or an open courtyard border). Blocked passages or sheer cliffs require specific actions or tools to cross.

### Tabletop Representation
At the physical gaming table, the environment is managed across two complementary tracking spaces:
1.  **The Macro Minimap (Point-Crawl Nodes):** Tracks the overarching raid location (dungeon, fortress, or town quarter) using connected abstract nodes. A single party token represents the main horde, showing broad exploration routes, locked security gates, and designated extraction points.
2.  **The Clash Cluster (Micro Battleground):** Deployed when combat breaks out. The GM places 3 to 6 modular Zone cards or tactile boundary markers on the table representing the immediate tactical theater. Player Boss miniatures and physical **d6** Mob health dice are placed directly onto these Zone cards.

---

## Zone Profiles

Every Zone on the battlefield possesses an intrinsic baseline difficulty known as its **Zone Profile**, written in standard slash notation: `Difficulty+/Target Number (TN)` (for example, `5+/1`, `5+/2`, or `6/1`).

>> **THE ZONE PROFILE RULE:**
>> Any general physical interaction, traversal feat, jump, climb, search, door-forcing, or balance check attempted within a Zone defaults to testing against that Zone's Profile. The GM does not invent ad-hoc Target Numbers; all unlisted environmental tests resolve against the active Zone Profile.

### Traversal and Interaction Resolution
*   **Baseline Checks:** When you attempt an unscripted physical maneuver (such as scaling a brick wall, jumping a ditch, or prying a floorboard loose), you roll the appropriate attribute pool (**Slink** for agility/traversal, **Tough** for brute force/lifting, or **Brains** for searching/spotting mechanisms) against the Zone Profile.
*   **Applying Boons and Banes:** Situational factors, specialized gear, or adverse conditions apply standard **Boons (+1d)** or **Banes (-1d)** to your dice pool before rolling, while leaving the underlying Zone Profile unchanged.

> **Example:** A crumbling armory has a Zone Profile of `5+/2`. Attempting to climb a broken weapon rack in this Zone requires a Slink test against `5+/2` (needing 2 successes on 5s or 6s). If the Goblin Boss uses a grappling hook, the tool grants a **Boon 1 (+1d)** to the pool, but the test profile remains `5+/2`.

---

## Movement & Tactical Positioning

Movement in **Gobbos** is measured in discrete Zones crossed rather than feet or inches.

### The Move Action
Spending one **Standard Action** on a **Move** action allows a character or Mob to cross a number of connected Zones up to their **Movement** rating:
*   **Goblin Boss Movement:** A Goblin Boss moves a number of Zones equal to their secondary **Movement** stat (ranging from 2 to 5 Zones per Move action, derived from their **Slink** stat; see [Boss Profile & Gang](02_Boss_Profile_and_Gang.md)).
*   **Mob Movement:** A Mob moves a baseline of **2 Zones** per Move action.
*   **Mobility Restrictions:** Difficult terrain, heavy encumbrance, or specific traits can increase movement costs or cap maximum speed.

### Tactical Disengagement & Opportunity Attacks
Leaving a Zone that contains alert, unengaged enemy combatants is inherently dangerous.

1.  **The Disengage Test:** To safely exit a Zone containing active enemies, a Goblin Boss or Mob must declare a Disengage maneuver as part of their Move action and pass a **Slink** test:
    $$\text{Disengage Test} = \text{Slink } 5+ / \text{Highest Enemy Defence TN}$$
2.  **Successful Disengage:** On a success, the unit moves out of the Zone safely along their declared movement path.
3.  **Failed Disengage:** On a failure, the highest **Threat** enemy in the Zone immediately executes an unavoidable **Opportunity Attack** against the escaping unit. Furthermore, the unit's movement is immediately halted, forcing them to remain inside the current Zone for the remainder of the round.
4.  **Bulk 3+ Restriction:** Wielding or hauling a loose object of **Bulk 3** or greater requires both hands and total focus. A character **cannot attempt a Disengage test** while clutching a Bulk 3+ item. To escape, the character must drop the item as a **Free Action**, defeat the threatening enemies, or have a Mob transport the burden.

---

## Cover Mechanics

Obstacles, low masonry, furniture, and environmental barriers provide crucial protection against incoming ranged attacks. Cover is classified into two distinct mechanical levels:

```
[Attacker in Zone A] ===( Ranged Attack )===> [Low Wall] ===> [Defender in Zone B]
                                              (Partial Cover: -1d Attack / +1d Dodge)

[Attacker in Zone A] ===( Line of Sight )===> [Solid Pillar] | [Defender in Zone B]
                                              (Full Cover: Targeting Blocked)
```

### Partial Cover
Partial Cover represents waist-high stone walls, overturned tables, dense thickets, wooden barricades, or clusters of allied goblins.
*   **Attacking into Partial Cover:** Ranged attacks targeting a creature behind Partial Cover suffer a **Bane 1 (-1d)** penalty to the attack dice pool.
*   **Defending behind Partial Cover:** A defender situated behind Partial Cover gains a **Boon 1 (+1d)** to their active **Dodge** (**Slink**) dice pool during a **Clatter Roll** against ranged threats.

### Full Cover
Full Cover represents solid stone pillars, reinforced iron doors, thick masonry walls, or total line-of-sight obstruction.
*   **Targeting Blocked:** A creature behind Full Cover cannot be targeted by direct ranged attacks, single-target spells, or line-of-sight abilities originating from the blocked direction.
*   **Bypassing Full Cover:** An attacker must spend movement to cross into a connected Zone that clears the sightline or flank around the barrier before declaring an attack.

---

## Modular Zone Traits & Hazards

A **Zone Trait** is an environmental modifier attached to a Zone that alters movement, tests, or combat resolution. Traits are modular building blocks that the GM combines to construct dynamic encounter maps.

### Hazard Severity Tiers
When an environmental hazard inflicts damage due to a failed test or unmitigated trigger, the damage scales by severity tier:
*   **Tier 1 Hazard (Minor):** Deals **1 Damage** to a Boss's **Grit** or a Mob's lowest active health die.
*   **Tier 2 Hazard (Dangerous):** Deals **2 Damage** to a Boss's **Grit** or a Mob's lowest active health die, or inflicts a sustained condition.
*   **Tier 3 Hazard (Lethal / Catastrophic):** Deals **3 Damage** to a Boss's **Grit** or a Mob's lowest active health die, or inflicts an immediate severe condition. Catastrophic hazards (such as collapsing mine shafts) can directly remove an entire Mob health die.

### Predefined Static Obstacles

| Trait Name | Category | Primary Tags | Trigger Timing | Mechanical Rule & Resolution Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Slippery** | Obstacle | `[Slick]` | On Entry / Exit | Any creature entering or leaving this Zone must pass a `Slink` test against the Zone Profile. On a failure, the creature falls **Prone** and their movement ends immediately. |
| **Rubble** | Obstacle | Terrain | Traversing | Difficult ground. Moving through this Zone costs double movement speed (spending 2 Zones of movement capacity per Zone crossed). |
| **Narrow** | Obstacle | Spatial Cap | Passive | Restricts physical capacity and frontline width (default **Size 2**). Mobs exceeding this capacity suffer **Bane 1 (-1d)** on physical tests, their Movement is capped at 1 Zone, and their Melee combat pool is capped at the narrow limit. Giant foes (`[Huge]`, `[Colossal]`) cannot enter. |
| **Chasm / Pit** | Hazard (T3) | Obstacle | Crossing / Shove | Crossing or being pushed into the pit requires a `Slink` test against the Zone Profile. On a failure, the creature plummets, taking **3 Damage** and gaining the **Restrained** condition. Climbing out requires a Standard Action and a successful `Tough` test against the Profile. |
| **Vertical Cliff** | Obstacle | Elevation | Vertical Move | Scaling a sheer wall or scaffolding requires a Move action and a `Slink` test against the Zone Profile. On a failure, the climber falls, taking 1 Damage per Zone height fallen and landing **Prone**. |
| **Deep Water** | Obstacle | `[Wet]` | Passive / Move | Traversing requires a Move action to cross only 1 Zone. Swimming without a boat or flotation gear requires testing `Tough` against the Zone Profile at round start or taking 1 drowning damage per round. |
| **Pillars / Statues** | Opportunity | Cover | Passive / Free Action | A creature occupying this Zone may declare they are ducking behind a pillar as a **Free Action**, gaining **Full Cover** against attacks originating from one designated adjacent Zone. |
| **Hedges / Thickets** | Opportunity | Cover | Passive | Thick vegetation provides passive **Partial Cover** to all occupants against ranged attacks originating outside the Zone. |
| **Shadowy** | Opportunity | Stealth | Passive | Deep darkness and heavy alcoves grant a **Boon 1 (+1d)** to all stealth-related `Slink` tests made within this Zone. |
| **Junk Pile** | Opportunity | Treat | Interactive | A character can spend a Standard Action (**Manipulate**) to search the debris (`Brains` vs Zone Profile). On a success, they salvage an improvised throwing weapon (1 Damage ranged) or 1d6 Scrap. Exhausted after one successful search. |

### Predefined Dynamic Hazards

| Trait Name | Category | Primary Tags | Trigger Timing | Mechanical Rule & Resolution Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Burning** | Hazard (T2) | `[Fire]`, `[Gaseous]` | Entry / Turn Start | Imposes active `[Fire]` (attacks in Zone score **+1 Success**) and `[Gaseous]` (ranged attacks suffer **Bane 1**). Entering or starting a turn here requires a `Slink` test vs Zone Profile; failure deals **2 Damage** and inflicts Burning. Spreads to flammable adjacent Zones at Round Closure on a 1d6 roll of 5–6. |
| **Crumbling Ceiling** | Hazard (T3) | `[Crushing]` | Round Start / Trigger | All occupants must test `Slink` against the Zone Profile. On a failure, they take **3 Damage** and are knocked **Prone**. After resolving, the Zone permanently gains the **Rubble** trait. |
| **Howling Wind** | Hazard (T1) | `[Gale]` | Passive | All ranged attacks passing into or through this Zone suffer a **Bane 1 (-1d)**. Moving against the wind requires a `Tough` test vs Profile; on a failure, movement speed is halved. |
| **Toxic Spores / Gas** | Hazard (T2) | `[Toxic]`, `[Gaseous]` | Turn Start | All creatures starting their turn in this Zone must test `Tough` against the Zone Profile. On a failure, they suffer the **Weakened** condition (**Bane 1 (-1d)** on physical tests) until they spend a Standard Action catching breath in a clean Zone. |
| **Quicksand / Mud** | Hazard (T2) | `[Wet]`, `[Sinking]` | On Entry | Entering or moving inside this Zone requires a `Slink` test against the Zone Profile. On a failure, the creature gains the **Restrained** condition. Escaping requires spending a Standard Action to test `Tough` against the Profile. |
| **Shoring** | Opportunity | Structural | Interactive | Goblins can deliberately collapse timber supports by spending a Standard Action (**Manipulate** or **Attack**) testing `Brains` or Melee attack vs Zone Profile. On a success, the Zone immediately triggers a **Crumbling Ceiling** hazard and all exits become blocked. Clearing a blocked exit requires a Standard Action testing `Tough` vs Profile. |

---

## Environmental Blueprints (Weather & Composite Hazards)

The GM can construct complex, encounter-wide weather patterns or atmospheric hazards by combining modular tags into unified environmental blueprints:

*   **Blizzard (T2 Hazard | `[Chilled]`, `[Blinding]`, `[Slick]`):** Freezing winds halve movement speed (`[Chilled]`), blinding snow makes ranged attacks **Hard (6)** and prevents Dodge reactions (`[Blinding]`), and icy footing requires a `Slink` test vs Zone Profile upon moving or fall **Prone** (`[Slick]`).
*   **Thunderstorm (T2 Hazard | `[Wet]`, `[Shock]`):** Heavy rain douses mundane flames and soaks all occupants (`[Wet]`). Any electrical damage or spark effect conducted through wet targets makes all incoming attacks against them **Easy (4+)** for 1 round (`[Shock]`).
*   **Smog Marsh (T2 Hazard | `[Wet]`, `[Toxic]`, `[Dark]`):** Foul sewer sumps conduct lightning (`[Wet]`), noxious marsh gas forces a `Tough` test vs Profile at round start or inflicts **Weakened** (`[Toxic]`), and dense gloom imposes **Bane 1 (-1d)** on notice and attack tests (`[Dark]`).
*   **Tornado / Gale Vortex (T3 Hazard | `[Gale]`, `[Weightless]`, `[Loud]`):** Howling vortex deflects ranged attacks (`[Gale]`), roaring winds drown out verbal orders and stealth (`[Loud]`), and updrafts lift creatures off the ground (`[Weightless]`). Stabilizing or exiting requires a `Tough` test against the Zone Profile.
*   **Acid Mire (T2 Hazard | `[Acidic]`, `[Slick]`):** Corrosive sludge destroys 1 passive Armor Die on a hit or failed hazard test (`[Acidic]`), and slick chemical mud forces a `Slink` test on entry or the creature falls **Prone** (`[Slick]`).

---

## Background Node Resolution (The Chaos Tick)

When a player chooses to split their forces and leave an unsupervised Mob behind at an inactive macro map node (for example, to guard a captured chokepoint, harvest a scrap pile, or hold a rear exit), that node is removed from active micro-combat tracking.

```
[Active Micro Combat Cluster] <======= Macro Distance =======> [Background Node: Size 3 Mob]
(Played out in tactical rounds)                                (Resolved via Chaos Tick at Round Closure)
```

### Unsupervised Mob Priority AI
Without direct Boss supervision, an unsupervised Mob automatically follows its base instinct priority list:
1.  **Survival:** Flee from overwhelming threats or lethal hazards.
2.  **Loot & Eat:** Scavenge loose food, mushrooms, shiny objects, and Scrap.
3.  **Violence:** Attack vulnerable stragglers or pick fights with nearby rivals.
4.  **Trash Stuff:** Vandalize architecture, smash furniture, and dismantle machinery.
5.  **Wander Off:** Scurry into adjacent corridors following noise or smell.

### Resolving the Chaos Tick
At the end of each combat round during the **Round Closure Phase**, the controlling player resolves the background Mob's actions by rolling the **Chaos Tick**:

>> **THE CHAOS TICK RULE:**
>> The player rolls a number of **d6s equal to the unsupervised Mob's current Size**. The test resolves against the background node's assigned Zone Profile (defaulting to **5+/1**):
>> *   **Successes (5+):** Tally successes to determine task progress and loot secured.
>> *   **Ones (1s):** Each **1** rolled represents growing insubordination and friction. Tally all **1s** rolled, add **+1 die per 1 rolled** to the communal **Bangaranga Pool**, and consult the **Gobbo Mischief Table**.
>> *   **The Farkle:** Rolling **zero successes** and **two or more 1s** triggers a catastrophic failure, causing the Mob to mutiny, trigger a trap, or wander off the map.

### The Gobbo Mischief Table

| 1s Rolled | Mischief Result | Mechanical Consequence |
| :---: | :--- | :--- |
| **0** | **Smooth Operations** | Perfect discipline! The Mob works together without internal fighting. |
| **1** | **Bickering** | Goblins fight over a shiny rock. The Mob takes **1 Damage** to its lowest active health die. |
| **2** | **Tasting Time** | The runts lick glowing moss or eat questionable sludge. The Mob gains the **Weakened** condition. |
| **3** | **Straying** | Several goblins get distracted and wander into dark pipes. The Mob's **Size decreases by 1**. |
| **4+** | **Mutiny / Riot** | Complete breakdown of authority! The Mob becomes **Out of Control** and permanently hostile to all Gangs, turning into an independent threat or vanishing with all carried gear. |

### Chaos Tick Success Progress

| Successes (5+) | Operational Outcome & Scavenged Payout |
| :---: | :--- |
| **0 Successes** | Distracted and idle. The Mob makes zero progress on their assignment. |
| **1 Success** | Basic task accomplished. If foraging, the Mob secures **1d6 Scrap**, or heals **1d6 damage** on its health dice by scavenging rations. |
| **2 Successes** | Productive haul. The Mob gathers **2d6 Scrap** or unearths a low-grade **Oddity** chassis. |
| **3+ Successes** | Masterful looting! The Mob completely clears and secures the node (making future traversal **Safe** with no hazard tests required) and secures **1 Standard Loot item**. |

---

## Mechanical Gap Analysis & Missing Rules

[MISSING RULE / GAP: Vertical Zone Height and Fall Damage Scaling — While falling from cliffs specifies 1 damage per Zone height, rules do not define maximum terminal fall damage or the exact interaction with Mob cushioning when falling onto enemies. Suggested Resolution: Cap falling damage at 5 damage (terminal velocity within dungeon scale). If a Boss or creature falls onto an enemy in a lower Zone, resolve as an improvised Attack with Impact Size equal to the height fallen; on a hit, damage is split equally between the falling creature and the target.]

[MISSING RULE / GAP: Zone Capacity Limits for Giant Adversaries — Narrow traits restrict Mobs and ban giant foes, but standard open Zones lack explicit entity capacity caps. In extreme scenarios, multiple player Mobs and enemy swarms could crowd into a single node. Suggested Resolution: Define standard open Zones as having a soft capacity of Size 10 total units. Exceeding Size 10 in a single Zone imposes Bane 1 (-1d) on all physical Dodge and traversal tests due to chaotic overcrowding.]
