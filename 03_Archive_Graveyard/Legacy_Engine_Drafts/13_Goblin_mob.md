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
Mobs can be equipped with scavenged weapons, armor, and utility tools, but this comes at a steep cost to their greed. 

*   **Mob Armor:** Equipping a Mob with Armor grants them passive **Armor Dice** (e.g., **+1d6** or **+2d6**). Whenever the Mob is attacked, you roll these dice **once per incoming attack**. Every success (**5+**) reduces the incoming damage by 1 across all targeted dice before damage is applied. Outfitting a Mob with armor requires sufficient gear for the swarm: Mob Armor costs **Bulk equal to the Armor's Bulk rating multiplied by Mob Size** (e.g., Light Armor costs **Size x 1 Bulk**; Medium Armor costs **Size x 2 Bulk**).
*   **Expedition Tools & Utility Gear:** Tools (such as Ropes, Crowbars, Lanterns, or Shovels) are shared by the squad. Each tool costs its standard flat **Bulk** rating (e.g., 1 Bulk for 1 Rope & Grappling Hook). 1 tool carried in the squad's pack serves the entire Mob.
*   **The Tradeoff:** Every piece of gear a Mob is equipped with reduces their **Carry / [[Loot Capacity]]** by an equal amount of Bulk. A heavily armored Mob will survive longer, but they will not be able to carry the raiding loot back to the lair! A naked, feral Mob will die quickly but can carry a horde of treasure.
*   **Casualties & Equipped Gear:** Equipped **Mob Armor** and **Mob Weapons** scale dynamically with the Mob's current **Size**. When a Mob loses Size from casualties, the armor and weapons of the fallen goblins remain on their corpses on the battlefield. Equipped gear never causes an encumbrance overload when Size drops. Only loose **Loot** and **Expedition Tools** count against the Mob's reduced capacity.

### Health & Taking Damage
A Mob's health is tracked physically on the table using a number of D6s equal to its Size (e.g., a Size 3 Mob starts with three physical dice turned to the "6" face). How damage is applied depends on the source of the attack:

1.  **Single-Target Attacks:** Damage is applied to the Mob's **lowest-value active health die**. If the die drops below 1, that die is removed (reducing the Mob's [[Size]] by 1), and any remaining damage spills over into the next lowest die.
2.  **Mob-on-Mob Melee (The Frontline Rule):** When two Mobs clash in close combat, the attacking Mob strikes a number of health dice equal to its own current [[Size]] ($\min(\text{Attacker Size}, \text{Defender Size})$).
    *   *Lowest Dice First:* Damage is applied to the defender's **lowest-value health dice first** (representing battered frontline runts absorbing the impact).
    *   *Simultaneous Reduction:* Each engaged die suffers the full effective damage. Any die reduced below 1 is removed from the table. Any unengaged dice in the back ranks take **0 damage**.
    *   *(Note: The maximum number of Melee Combat Dice or frontline width may be restricted by zone terrain, such as `Narrow` choke points; see [Movement & Zones](../00_Rules/03_Movement%20&%20Zones.md)).*
3.  **Cleaving Attacks (`Cleave X`):** Attacks made with the `Cleave X` trait (such as a `Cleave 2` Greataxe or a `Cleave 3` Ogre Club) sweep across the frontline, applying their damage simultaneously to **up to X of the Mob's lowest-value health dice**.
4.  **True Area Threats (`[AoE]` & Explosives):** Environmental catastrophes, explosive devices, and dragon breath weapons blanket the entire zone without an engagement cap. Incoming damage is applied to **every single active die** in the Mob's pool simultaneously.

> *Example (Mob-on-Mob Clash): A Size 4 Goblin Mob has dice reading `[6, 4, 2, 1]`. A Size 2 Guard Mob attacks and deals 2 effective damage. The guards are Size 2, so they damage the 2 lowest dice (`[1]` and `[2]`). Both dice take 2 damage and are reduced below 1 and removed. The Goblin Mob is now Size 2, with surviving dice `[6, 4]`.*

**Dropping Loot:** If a Mob shrinks in Size, their [[Loot Capacity]] also drops! If they are suddenly carrying more loose [[Loot]] and tools than their new Size allows, the controlling Boss must immediately choose which Loot is dropped on the floor. 

## Splitting and Merging Mobs
A Boss can dynamically manage their swarm by splitting Mobs apart or merging them together. 

### Splitting a Mob
A Boss can use an [[Order]] to tell a Mob to split instead of taking their normal 2 actions. 
*   **The Math:** A Size 5 mob splits into two smaller mobs (e.g., Size 3 and Size 2). The Boss decides how to distribute the current physical dice.
*   **The Benefit:** Splitting is an excellent way to mitigate AoE/Cleave damage, or to fit Mobs into narrow terrain.
*   **Gear Distribution on Split:** 
    *   *Expedition Tools:* The Boss assigns each carried tool (Ropes, Crowbars) to one specific resulting Mob. Tools cannot be duplicated.
    *   *Mob Armor:* Armor travels with the goblins wearing it. Both split squads retain the same Armor Tier (+1d or +2d), and their carried Bulk reflects their new individual Size (e.g., a Size 2 Mob carrying 4 Bulk of Medium Armor).

### Merging Mobs
If two Mobs belonging to the same player end their turn in the same Zone, the Boss can use an [[Order]] or [[Manipulate]] action to merge them.
*   **The Math:** You add the D6s together (e.g., a Size 2 and Size 3 Mob become a new Size 5 Mob). 
*   **The Grunt Cap:** The total Size of the new Mob *cannot exceed* the Boss's [[Grunt]]. If a Boss merges a Mob until it exceeds their Grunt, it immediately becomes Uncontrolled (see below).
*   **Gear Merging & Armor Dilution:** All carried tools and loot combine into the new Mob's pool. If an armored Mob merges with an unarmored Mob, the new combined Mob only gains the Armor bonus if the total equipped armor covers the new combined Size. Otherwise, the armor is diluted and drops by 1 Tier (e.g., Medium Armor drops to Light Armor).

### The Super-Mob (Cross-Gang Merging)
Mobs from different player Gangs *can* merge if both Bosses agree. This creates a terrifying, chaotic massive [[dice pool]].
*   **The Command Struggle:** The new Super-Mob is extremely volatile. Every time *either* Boss wants to issue an Order to the Super-Mob, it requires a **Grunt test** (Testing [[Tough]] if in the same Zone, or [[Mouth]] from afar).
*   **In-Fighting:** Whenever a Cross-Gang Mob rolls a [[dice pool]] for *any reason* (like an Attack roll, or a Manipulate check), **every 1 rolled results in 1 damage to the Mob itself.** They cannot help themselves; they just start stabbing the other gang! This happens regardless of whether the action is successful or not.

### Action Economy & Mob Defense

A Mob gets **two (2) actions** per round, reset at the start of each round. A Mob's behavior, actions spent, and defensive capabilities are determined strictly by their combat state:

1.  **Ordered:** The Mob receives direct instructions from the Boss (using a [[Standard Action]] or Free Order). They use **both actions** as per the player's instructions (e.g., moving and attacking).
2.  **[[Loitering]]:** The Mob is under control but receives no orders on their turn. Goblins are naturally distracted and lazy; they use **1 action** to loiter (roll/choose on the **[[Loitering]] Table** below) and save **1 action**.
3.  **[[Out of Control]]:** The Mob is uncontrolled (see below). They spend **both actions** running amok under GM control (roll/choose on the **[[Out of Control]] Table** below).

#### Mob Defense & The "Scatter!" Order
Mobs cannot naturally dodge. When targeted by an incoming attack:
*   **Passive Armor:** If equipped with Armor, the Mob rolls its passive Armor Dice (5s/6s reduce incoming damage).
*   **The "Scatter!" Reaction:** The Boss can spend a saved Reaction to yell "Scatter!", rolling Stat dice equal to the Boss's [[Mouth]] stat against the attack's **Threat TN**.
    *   **Size Target Penalty:** Large swarms are clumsy to disperse. Every point of Mob [[Size]] above 1 increases the attack's Threat TN by **+1** (e.g., a Size 3 Mob suffers +2 TN).
    *   **Success:** The Mob evades completely (0 damage) and immediately scurries **1 Zone** into cover.
    *   **Failure:** The Mob takes incoming damage, mitigated only by passive Armor Dice.
    *   **Mob Gambling:** The Boss can use the [[Gobbo Gamble]] to reroll **1s** on the Mouth dice. If the Gamble still fails, panic breaks out: the Mob takes the attack damage, suffers **1 Trample Damage** to *every single die* in its health pool (like an AoE crush), drops **1 Bulk** of Loot, and becomes [[Out of Control]]. If the Boss is in the same [[Zone]], the Boss is caught in the mob stampede and becomes [[Staggered]].

### Command Limits (Control vs. Out of Control)
A Mob is under command as long as they are within line of sight of their Boss and the Mob's current [[Size]] does not exceed the Boss's maximum [[Grunt]] stat. A Mob immediately becomes [[Out of Control]] if:
1.  **Broken Command:** They break line of sight with their Boss (e.g., they move behind a solid wall or enter a separate room).
2.  **Command Limit Exceeded:** The Mob's [[Size]] increases beyond the Boss's current [[Grunt]] (often due to merging or the Boss losing Grunt from a Fumble).
3.  **Morale Failure:** The Mob fails a [[Morale Check]] and panics (or becomes an Orphaned Mob if the Boss is incapacitated).
4.  **Scatter Gamble Failure:** The Boss fails a [[Gobbo Gamble]] while ordering the Mob to Scatter.

#### Mob Morale Checks
*   **Trigger:** Evaluated during Round Closure if the Mob suffered 50% casualties during the round, or immediately if the controlling Boss is incapacitated.
*   **Active Boss:** The Boss tests [[Mouth]] or [[Grunt]] against **5+/1** (or **5+/2** if facing a `[Terrifying]` enemy). On failure, the Mob becomes [[Out of Control]] for 1 round.
*   **Incapacitated Boss (Orphaned Mob):** The Mob has no leader to keep discipline. They **automatically fail without rolling** and immediately enter the [[Out of Control]] state at the start of the next round.

#### Regaining Control
To bring an [[Out of Control]] Mob back under command, the Boss must spend a [[Standard Action]] to [[Order]] them, resolving it using the standard command test rules in [Giving Orders](../00_Rules/04_Giving%20orders.md). On a success, the Mob becomes controlled and receives their instructions; on a failure, they ignore the Boss and remain [[Out of Control]].

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

## Mob Tests & Hazard Resolution
Goblins in a Mob do not have individual stats (like [[Tough]], [[Slink]], [[Brains]], or [[Mouth]]). When an ordered Mob makes a non-combat test against a [[Zone Profile]] or obstacle, assemble their [[dice pool]] using the following core framework:

*   **Tough Tests (Strength, Endurance, Mass, Resisting Toxins):** Roll dice equal to the Mob's current **[[Size]]** (**1d6 to 5d6**). A large Mob has tremendous mass, collective leverage, and muscle.
*   **Slink Tests (Stealth, Dodging, Balance on Ice, Climbing):** Always roll a base of **2d6**. A crowd of goblins has enough natural agility to manage basic traversal, but remains prone to clumsiness.
*   **Brains & Mouth Tests (Searching Junk, Deciphering, Social):** Always roll a base of **2d6**. Without the Boss's direct intellect, a Mob has a baseline cunning but lacks specialized expertise.

### Fumbles & Pushing 1s on Mob Tests
If a Mob fails a test and one or more dice show **1s**, the controlling **Goblin Boss** can choose to push their luck and reroll all **1s**. If the rerolled test still fails, the effort suffers a [[Fumble]], and the **Goblin Boss loses 1 [[Grunt]]** as their authority takes the blame for the blunder.

### Mob Hazard Consequences
When a Mob fails a test against an environmental obstacle or hazard:
*   **Slippery / Slick Surfaces:** The Mob slips and crashes into a dog-pile, gaining the **[[Prone]]** condition. Their movement ends immediately inside the zone, and they must spend 1 Action on their next turn to stand back up.
*   **Chasms & Heights:** The lead runts plummet over the edge. The Mob suffers standard Hazard Damage (1–3 damage applied to its active Mob health dice) and lands **[[Prone]]** at the bottom.
*   **Toxic Spores / Gas Clouds:** The Mob gags and chokes, gaining the **[[Weakened]]** condition (**Bane 1 (-1d)** on all physical tests).
*   **Deep Mud / Quicksand:** The Mob gets bogged down, gaining the **[[Restrained]]** condition. Escaping requires 1 Action and a successful [[Tough]] test (rolling **Size dice**).

### Mob Gear Upgrades & Tools
Equipping a Mob with relevant tools modifies their base test pools:
*   **Permission Tools (Ropes, Torches):** Bypasses the need for a roll entirely once set up (e.g., swarming up an anchored climbing rope requires no test).
*   **Boon Tools (Crowbars, Crampons, Camo-Tarps):** Grants **+1d** to the test pool (e.g., a Mob with *crampons* rolls **3d6** on Slippery tests).
*   **Difficulty Tools (Lockpicks):** Shifts the test Difficulty (e.g., from Hard to Normal).

---

## Mob Sacrifice Maneuvers

When a Gang lacks the proper tools (or wants to save precious [[Bulk]] capacity for heavy [[Loot]]), a **Goblin Boss** can order their **Mob** to perform disposable goblin maneuvers. 

Sacrifice maneuvers utilize the expendable bodies of lesser goblins to bypass dungeon hazards, assist the Boss, or clear obstacles:

| Maneuver Name | Minimum Mob Size | Action & Damage Cost | Mechanical Benefit |
| :--- | :---: | :--- | :--- |
| **Gobbo Pyramid** *(Living Ladder)* | **Size 2** | **1 Mob Action** | Goblins stack onto shoulders. The Boss or an allied character climbs **1 vertical Zone** without needing a rope or making a climbing test. |
| **Living Bridge** *(Chasm Crosser)* | **Size 3** | **1 Mob Action** + **1 Mob Health Damage** | Goblins link arms and bite belts across a pit or gap. Allied Bosses walk across safely without making any test. The Mob takes 1 damage to its active health die from trample strain. |
| **Canary Runt** *(Trap Tripper)* | **Size 1** | **1 Mob Health Damage** | A single runt is sent sprinting ahead into a discrete triggered trap (pressure plates, tripwires, falling dart blocks) or across untested ice. The trap triggers, clearing the path safely for the rest of the gang. *(Note: Cannot clear persistent ambient Zone traits like gas clouds or burning zones).* |
| **Meat Cushion** *(Soft Landing)* | **Size 1** | **Mob Reaction** (Cost: Mob takes Fall Damage) | If a Boss falls into a Zone occupied by an allied Mob, the Mob cushions the fall. The Boss takes **0 damage**. The Mob absorbs the impact, taking the full falling damage across its health dice. |
| **Gnaw the Hinges** *(Crowbar Substitute)* | **Size 2** | **1 Mob Action** | The Mob tears at locked iron doors or chest hinges with teeth and crude shivs. Roll a standard [[Tough]] test (**Size dice**). If the test fails after pushing 1s, the Mob takes **1 damage** from chipped teeth, crushed fingers, and falling debris. |