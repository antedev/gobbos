# Goblin Mobs

A Boss is nothing without their Gobbos. A Mob is your weapon, your shield, and your pack mule. But keeping a mob together requires a Boss with enough [[Grunt]]. Otherwise, they simply will not listen, and an ambitious goblin in the ranks might try to take your spot.

## Size = Power
The absolute most important stat for a Mob is its [[Size]]. Size determines everything: how many dice they roll in combat, how much Grunt you need to control them, and how much Loot they carry. 

| Name | Size | Combat Dice | Required Grunt | Loot Capacity |
| :--- | :--- | :--- | :--- | :--- |
| Runts | 1 | 1d6 | 1 | 4 Bulk |
| Group | 2 | 2d6 | 2 | 8 Bulk |
| Troop | 3 | 3d6 | 3 | 12 Bulk |
| Gang | 4 | 4d6 | 4 | 16 Bulk |
| Company | 5 | 5d6 | 5 | 20 Bulk |

*Note: The number of goblins in a Mob is abstract. A Size 1 Mob might be 3-5 goblins, while a Size 5 Mob is a swarming horde of 30+.*

## Mob Equipment & Loot Tradeoff
Mobs can be equipped with scavenged weapons and armor, but this comes at a steep cost to their greed. 
*   **Mob Armor:** Equipping a Mob with Armor grants them passive Defense Dice (e.g., +1d6 or +2d6). Whenever the Mob is attacked, you roll these bonus dice, and every success reduces the incoming damage. 
*   **The Tradeoff:** Every piece of Gear a Mob is equipped with reduces their **Carry / Loot Capacity** by an equal amount of Bulk. A heavily armored Mob will survive longer, but they will not be able to carry the raiding loot back to the lair! A naked, feral Mob will die quickly but can carry a horde of treasure.

### Health & Taking Damage
A Mob's health is tracked physically on the table using a number of D6s equal to its Size (e.g., A Size 3 mob starts with three physical dice turned to the "6" face). 

When a Mob takes standard damage, you turn the face down on one of those dice by the damage amount. When a die drops below 1, that die is removed, and the Mob permanently shrinks 1 point in Size. 
*   **Damage Spillover:** In Gobbos, damage is lethal and always carries over! If a die is removed and there is still incoming damage left over, that remaining damage spills over into the next die. 

> *Example: A Size 3 mob has one die currently reading "2". They take 3 damage. The die is turned to 0 and removed (the mob is now Size 2). The remaining 1 damage spills over to the next die, turning a "6" into a "5".*

**AoE & Cleave Damage (The Mob Killer):**
Mobs are strong against single-target damage, but incredibly weak to Area of Effect (AoE) or Cleave attacks (like a roaring dragon's breath or a wizard's fireball). 
If an attack explicitly has the AoE or Cleave trait, the incoming damage is applied to **EVERY SINGLE DIE** in the Mob.

> *Example: A Fireball deals 3 Damage to a Size 5 Mob. Instead of just reducing one die by 3, you reduce ALL 5 dice by 3. That single fireball just dealt 15 total damage!*

**Dropping Loot:** If a Mob shrinks in Size, their Loot Capacity also drops! If they are suddenly carrying more Bulk than their new Size allows, the controlling PC must immediately choose which Loot is dropped on the floor. 

## Splitting and Merging Mobs
A Boss can dynamically manage their swarm by splitting Mobs apart or merging them together. 

### Splitting a Mob
A Boss can use an [[Order]] to tell a Mob to split instead of taking their normal 2 actions. 
*   **The Math:** A Size 5 mob splits into two smaller mobs (e.g., Size 3 and Size 2). The Boss decides how to distribute the current physical dice.
*   **The Benefit:** Splitting is an excellent way to mitigate AoE/Cleave damage, or to fit Mobs into narrow terrain.

### Merging Mobs
If two Mobs belonging to the same player end their turn in the same Zone, the Boss can use an [[Order]] or [[Manipulate]] action to merge them.
*   **The Math:** You add the D6s together (e.g., a Size 2 and Size 3 Mob become a new Size 5 Mob). 
*   **The Grunt Cap:** The total Size of the new Mob *cannot exceed* the Boss's [[Grunt]]. If a Boss merges a Mob until it exceeds their Grunt, it immediately becomes Uncontrolled (see below).

### The Super-Mob (Cross-Gang Merging)
Mobs from different player Gangs *can* merge if both Bosses agree. This creates a terrifying, chaotic massive dice pool.
*   **The Command Struggle:** The new Super-Mob is extremely volatile. Every time *either* Boss wants to issue an Order to the Super-Mob, it requires a **Grunt test** (Testing [[Tough]] if in the same Zone, or [[Mouth]] from afar).
*   **In-Fighting:** Whenever a Cross-Gang Mob rolls a dice pool for *any reason* (like an Attack roll, or a Manipulate check), **every 1 rolled results in 1 damage to the Mob itself.** They cannot help themselves; they just start stabbing the other gang! This happens regardless of whether the action is successful or not.

### Action Economy & Combat States

A Mob gets **two (2) actions** per round, reset at the start of each round. A Mob's behavior, actions spent, and defensive capabilities are determined strictly by their combat state:

1.  **Ordered:** The Mob receives direct instructions from the Boss (using a Standard Action or Free Order). They use **both actions** as per the player's instructions (e.g., moving and attacking). They have **0 saved actions** left for defense (0d6 [[Defence]]).
2.  **Loitering:** The Mob is under control but receives no orders on their turn. Goblins are naturally distracted and lazy; they use **1 action** to loiter (roll/choose on the **Loitering Table** below) and save **1 action** for defense. When attacked, they spend their saved action to roll 1d6 [[Defence]].
3.  **Out of Control:** The Mob is uncontrolled (see below). They spend **both actions** running amok under GM control (roll/choose on the **Out of Control Table** below), leaving them with **0 saved actions** left for defense (0d6 [[Defence]]).

### Command Limits (Control vs. Out of Control)
A Mob is under command as long as they are within line of sight of their Boss and the Mob's current [[Size]] does not exceed the Boss's maximum [[Grunt]] stat. A Mob immediately becomes [[Out of Control]] if:
1.  **Broken Command:** They break line of sight with their Boss (e.g., they move behind a solid wall or enter a separate room).
2.  **Command Limit Exceeded:** The Mob's [[Size]] increases beyond the Boss's current [[Grunt]] (often due to merging or the Boss losing Grunt from a Fumble).
3.  **Morale Failure:** The Mob fails a group [[Morale Check]] and panics.

#### Regaining Control
To bring an Out of Control Mob back under command, the Boss must spend a Standard Action to [[Order]] them, resolving it using the standard command test rules in [Giving Orders](../00_Rules/04_Giving%20orders.md). On a success, the Mob becomes controlled and receives their instructions; on a failure, they ignore the Boss and remain Out of Control.

---

## Behavior Tables

When a Mob is [[Loitering]] or [[Out of Control]], roll **1d6** on the appropriate table during their turn to determine how they act:

### Loitering Table (d6)
*   **1 (Bicker):** They argue, push, and complain. (Uses 1 action. Saves 1 action for 1d6 [[Defence]]).
*   **2 (Inspect):** They pick their noses, stare at walls, or draw crude graffiti. (Uses 1 action. Saves 1 action for 1d6 [[Defence]]).
*   **3 (Snatch):** They pick up a nearby shiny object or eat a mushroom (resolves as a Plunder action if loot is present; otherwise narrative). (Uses 1 action. Saves 1 action for 1d6 [[Defence]]).
*   **4 (Wander):** They move **one (1) Zone** in a random direction (but they will not willingly leave line of sight of their Boss). (Uses 1 action. Saves 1 action for 1d6 [[Defence]]).
*   **5 (Snoop):** They peer around curiously, granting a [[Boon]] to the next PC who tests to spot hidden traps or doors in the Zone. (Uses 1 action. Saves 1 action for 1d6 [[Defence]]).
*   **6 (Taunt):** They make rude gestures, moon, or scream insults at the nearest enemy. (Uses 1 action. Saves 1 action for 1d6 [[Defence]]).

### Out of Control Table (d6)
*   **1–2 (Panic / Flee):** If there is a **Terrifying Enemy** (any Elite or Boss, any creature with the `[Frightening]` or `[Huge]` tag, or any hazard/enemy that dealt damage to them this round) in their Zone, they spend both actions fleeing toward the nearest exit or cover. Otherwise, they squabble: the Mob takes 1 damage and gains the [[Staggered]] condition. (Uses 2 actions. 0d6 [[Defence]]).
*   **3–4 (Loot / Trash):** If unattended loot or food is present, they plunder it (eating food heals **1d6** damage on their Mob health dice). Otherwise, they spend both actions trashing doors, crates, and furniture in their Zone. (Uses 2 actions. 0d6 [[Defence]]).
*   **5–6 (Frenzy):** They swarm and attack the nearest living creature in their Zone (enemy or ally!). If no creatures are present, they wander **one (1) Zone** toward the nearest noise. (Uses 2 actions. 0d6 [[Defence]]).

---

## Mob Tests & Attributes
Goblins in a Mob do not have individual stats (like [[Tough]], [[Slink]], [[Brains]], or [[Mouth]]). Instead, their dice pool for any non-combat test is resolved using the core [[Stat]] dice rule based on the nature of the test:

*   **Tough Tests (Strength, Endurance, Mass):** Roll [[Size]] dice. A Mob's collective strength and body mass are directly tied to their [[Size]]. Larger Mobs are much better at lifting gates, swimming against currents, or resisting toxic gas.
*   **Slink Tests (Stealth, Dodging, Balance):** Always roll exactly **1d6** (representing a default stat value of 1). A crowd is inherently loud and clumsy. Regardless of the Mob's [[Size]], one goblin tripping cascades to others, making stealth, balance, and quick dodging difficult.
*   **Brains & Mouth Tests (Thinking, Social):** Always roll exactly **1d6** (representing a default stat value of 1). Without their Boss's direct instructions, a Mob is a disorganized mess and cannot coordinate complex tasks or trade.

### Mob Gear Upgrades
Any gear equipped to a Mob that assists with specific tests (like *silent shoes* for Slink tests or *protective masks* for Tough tests against gas) applies its benefits as standard [[Boon|Boons]] (+1d per Boon) to these base rolls.
> **Example:** A Mob equipped with *silent shoes* gains a [[Boon]] (+1d) to Slink tests, rolling **2d6** instead of the base **1d6**.