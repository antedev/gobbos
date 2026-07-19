# Combat and Actions
Combat is a key mechanic in Gobbos. The combat can either be only the PC against some foe, or a more tactical battle with loads of Goblins piling on. 
The combat is structured in a number of rounds, that are repeated until the combat ends. All the players act in the Players Active turn, and then the enemies act in the Enemy Active turn. But both can use Reactions to react to anything that the other does. 

## Actions
Actions represent how much a goblin can accomplish in a round. There are three types of actions:
1.  **Standard Actions:** Every PC has **three (3) Standard Actions** per round, reset at the start of each round. Standard Actions are spent to Move, Attack, Plunder, Manipulate, or Order. They can be saved to be used as Reactions.
2.  **Free Actions:** Minor tasks that cost no Standard Actions (e.g., dropping an item, speaking, or activating passive quirks).
3.  **Reactions:** Actions taken out of turn in response to enemy actions (e.g., Dodge or Parry). You must spend a saved Standard Action to perform a Reaction.
Additionally, PCs have **one (1) Free Order Action** per round (which does not count toward their 3 Standard Actions).

Each Mob has **two (2) actions**, which are also reset at the start of each round, but they only act when Ordered. When they are left to their own devices (see [[Uncontrolled Mobs]]), they act on their own as per a predefined priority list

### Actionlist
#### Move (Mob or PC)
With a Move action, you can move up to your [[Movement]] number of zones. The different conditions of the zones are taken into account, and the movement might be limited or entirely blocked by hazards. If a climb, swim, jump, or other physical feat is required based on the circumstances in the zone, you must typically make a [[Slink]] test. The [[Difficulty]] and [[TN]] default to the established zone profile (e.g., **5+/1**), subject to GM adjustment. 
#### Attack (Mob or PC)
The Attack action can only be used in the Players Active turn. 
To Attack, the player's base dice pool is based on the player's [[Tough]] for [[Melee attack]] and [[Slink]] for [[Ranged attack]], modified by any equipment, Quirks, or other circumstances. 
*   **Kill / Wound:** If you roll successes equal to or greater than the target's current [[Defence]] (acting as the test's [[TN]]), you instantly defeat a standard enemy, deal 1 [[Wound]] to a Boss/Elite (see [Enemies](../04_Enemies/20_Enemies.md)), or reduce a Mob's [[Size]] by the number of successes scored.
*   **Stagger:** If you roll at least **one (1) success** but fewer than the target's current [[Defence]] TN, the attack does not deal damage, but it throws them off balance. The target gains the [[Staggered]] condition until the end of the round.
*   **Bounce:** If you roll **zero (0) successes**, the attack bounces harmlessly off their armor. Nothing happens.
#### Plunder (Mob or PC)
The [[Plunder]] action is to pick up any [[Loot]] at where the Player or the Mob stands.  
#### Dodge / Parry (Reaction)
The Dodge or Parry action can only be used as a [[Reaction]] to an incoming Attack or Environmental effect. Typically this is in the Enemy Active turn. You **must** have saved a Standard Action from your turn to use this. If you are out of actions, you simply take the damage!
*   **Dodge:** Test [[Slink]] (typically **5+/1**). Every success you roll reduces incoming damage by 1.
*   **Parry:** Test [[Tough]] (requires a shield, typically **5+/1**). Every success you roll reduces incoming damage by 1.
*   **Armor:** Armor adds Passive defence dice that do NOT need an action. See more under equipment.
*   **The Math:** Every success you roll reduces the incoming Damage by 1. If any damage remains, your Gobbo or Mob takes it.

**Mob Defense:**
Mobs do not naturally dodge. They are a chaotic swarm and simply absorb damage. However, a Mob's defensive capabilities depend on their equipment and their current combat state (saved actions):
1.  **Armored (Passive):** If a Mob is equipped with Armor, they gain passive defense dice (e.g., **+1d6** or **+2d6**) which are rolled against every incoming attack.
2.  **Saved Actions (Active Defense):** If a Mob has saved actions (because they are [[Loitering]] and only used 1 action on their turn), they can use their saved action as a Reaction to defend. For each saved action spent, the Mob rolls **1d6** Defence.
    *   *Loitering Mobs (1 Saved Action):* Rolls **1d6** Defence.
    *   *Ordered or Out of Control Mobs (0 Saved Actions):* Rolls **0d6** Defence (relying only on passive Armor).
    *   *Bane:* A [[Staggered]] Mob suffers a **Bane (-1d)** to their Defence rolls, reducing a loitering Mob's active defense roll to **0d6**.
3.  **Ordered Scatter (Reaction):** If a Mob with 0 saved actions is targeted by an attack, the Boss can spend a saved action (or an unused Free Order Reaction) to yell at them to "Scatter!". The Mob rolls active defense dice equal to the Boss's [[Mouth]] stat (e.g., if Mouth is 3, the Mob rolls **3d**). If they survive the attack, they may immediately Move 1 Zone to take cover.

### GM Tactics: Group Attacks (Enemy Swarms)
If multiple enemies surround and attack a Gobbo, the GM should NOT make separate attacks. Instead, they combine into a [[Group Attack]]. While a PC can only be attacked by a maximum of 3 enemies, there is no limit on attacker on a Mob
*   The base damage is the primary enemy's Attack stat, **+1 damage** for every additional enemy in the swarm. 
*   The player only spends **one** saved Action to Dodge/Parry the entire Group Attack. 
> *GM Advice:* Avoid splitting enemies into many small attacks against a single PC. This will instantly drain their saved actions and create a frustrating "death by a thousand cuts." Swarm them into Group Attacks instead!

#### Manipulate
The Manipulate action is a catch-all for whenever a Mob or PC tries to interact with an item or the environment in any way. The base dice pool is based on whatever attribute is most relevant to the action, modified by any equipment, Quirks, or other circumstances. The GM sets the [[Difficulty]] and [[TN]] (typically **5+/1**). 

#### Order 
The Order action is used to give commands to your goblins, directing a Mob to use both of their actions for the round. Standard Orders to controlled Mobs do not require a dice roll.
*   **The 3 Mob States:** A Mob is always in one of three states on their turn:
    *   **Ordered:** Direct instructions from the Boss. They spend both actions as ordered (0 saved actions for defense).
    *   **Loitering:** Under control, but receives no orders. Goblins use **1 action** to loiter (roll/choose on the Loitering Table in [Goblin Mobs](../01_Characters%20&%20Mobs/13_Goblin_mob.md)) and save **1 action** for defense (1d6 [[Defence]]).
    *   **Out of Control:** Broken command (out of sight, size exceeds Grunt, or failed morale). They spend both actions running amok under GM control (roll/choose on the Out of Control Table in [Goblin Mobs](../01_Characters%20&%20Mobs/13_Goblin_mob.md)), leaving them with 0 saved actions for defense.
*   **Regaining Control:** To regain control of an Out of Control Mob, the Boss must spend a Standard Action to [[Order]] them, resolving it using the standard command test rules in [Giving Orders](04_Giving%20orders.md). On a success, the Mob becomes controlled and receives their instructions; on a failure, they ignore the Boss and remain Out of Control.
*   **Cross-Gang Super Mobs:** Issuing an Order to a Mob merged from multiple different player Gangs *always* requires a Grunt test (Test [[Tough]] if in the same Zone, or [[Mouth]] from afar).
*   **The Boredom Rule:** Mobs have short attention spans. When acting (Ordered, Loitering, or Out of Control), a Mob cannot perform the exact same action twice (e.g., they cannot Attack twice, or Plunder twice). *Exception:* A Mob *can* take the Move action twice if they are fleeing or charging.
*   **Free Orders & Maximum Mobs:** Your ability to command the swarm is dictated strictly by your [[Mouth]] stat progression (see [[Stat|Stats]]). As you level up Mouth, you can command more Mobs simultaneously, and you are granted additional [[Free Orders]] per round. You never have to spend your Standard Actions to issue these Free Orders!


## Cover
Taking cover behind walls, pillars, or upturned tables protects you from ranged attacks. There are two levels of cover:
*   **Partial Cover:** You are partially blocked (e.g., behind a low barricade, crate, or thick foliage).
    *   **Attacking a target in Partial Cover:** If a PC or Mob attacks a target in Partial Cover, the attack roll suffers a [[Bane]] (-1d).
    *   **Defending while in Partial Cover:** If you are in Partial Cover and are targeted by a ranged attack, you gain a [[Boon]] (+1d) to your [[Dodge]] test.
*   **Full Cover:** You are completely hidden behind a solid obstacle (e.g., a stone pillar, wall, or closed door).
    *   You cannot be targeted by ranged attacks from that direction. An attacker must move to clear their line of sight or bypass the obstacle before they can attack.


## The Combat loop
The combat follows a structured loop, that is repeated until the combat ends. 
0. Combat Setup
1. Round start
2. Players active turn
3. Enemy active turn
4. Round closure 
5. Combat End
### Combat Setup
The GM sets up any combat at the start of the combat. This typically include a map of the environment, where the goblins and their enemy stands. The GM should point out any obvious places where there is environmental hazard, special conditions or so. However, not all might be visible to the players at once. There might be hidden traps, enemies in hiding or loot that is hidden. 
The GM should also mention what the objectives of the battle, in regards to where there are  [[Raid-Points]] to be gain.
The Setup happens once, and the rest of the steps are looped until you get to the Combat End. 
### Round start
Make a quick assessment on the status, who is where, who is hiding, and such to give everyone a fair view of the battlefield. 
#### Conditions
Any Conditions with Start of Round-activations happens now for all participants. 
#### Reinforcments
If any side gets reinforcements they are placed on the board now in a suitable zone. 
#### Points
The GM updates if there are any changes to the points to be awarded, such as a new location being discovered or a special character now appeared. 
### Players active turn
On the Players *active* turn, they can use any actions they want to move, plunder, attack, or execute other shenanigans.
1.  **Player Actions:** All player characters take their actions in any order. This is when Bosses can move, attack, or issue orders to control their Mobs.
2.  **Unordered Mobs:** Once all players have finished taking their actions, any Mobs that were **not ordered** this turn (both [[Loitering]] and [[Out of Control]] Mobs) resolve their behaviors. Roll on the appropriate behavior table for each.
During this phase, the GM may use enemy reactions to respond to players or mobs (e.g., taking opportunity shots or counter-attacking). 
### Enemy active turn
On the Enemies active turn, they can use whatever action they have left, which might have been spent on reactions. 
In this phase the Players might react to anything a enemy is doing, if they saved up any actions from their active phase. 
### Round closure
#### Points
Raid points are calculated, including currently held as well as confirmed, based on objectives and the basic Raid rules. 
#### Conditions
All around the table are recommended to do a short assessment of the current standing. How hurt any mobs are, where the enemies are and whatever conditions they might have. Any conditions with End of Round abilities is carried out now. Additionally, all [[Staggered]] conditions on PCs, Mobs, and Enemies are automatically removed. 
#### Moral check
The GM and the players do a Morale Check if needed, to see if some or all flees. Few opponents fight to the death, unless there is no alternatives (or they are immune to Morale)
#### Environmental effects
The GM checks for any changes in the Environment, such as spreading fire or smoke. Perhaps the a damn has been broken floods the battlefield or a fissure in the ground spews out lava. Note down any zones affected by these changes. 
#### Reset actions
If the combatants are still willing to fight, go back to the Round start, and resets everyone's actions.
### Combat End 
If there are no one fighting on one side, or one side gives up or flees, the Combat ends. 
#### Fleeing (Tactical Retreat)
Goblins are cowards at heart, and running away is a highly viable survival strategy.
*   **Escape Zones:** To flee an encounter, a PC or Mob must move into a designated escape zone or exit.
*   **Disengaging & Opportunity Attacks:** If a PC or Mob attempts to leave a Zone containing alert enemies, they trigger a reactionary Opportunity Attack from each enemy in the zone. To prevent this, they must spend a Standard Action to Disengage, testing [[Slink]] against a difficulty of **5+** and successes required equal to the highest enemy [[Defence]] TN (denoted as **5+/Defence**). On a success, they may move out of the Zone safely.
*   **Carrying Bulk:** Goblins fleeing with heavy treasure are slowed. Standard movement and dragging penalties for [[Bulk]] apply while fleeing. A PC or Mob can choose to drop their loot as a Free Action to restore full movement speed.
*   **Mob Fleeing:** Mobs flee when given a "Scatter" or "Retreat" Order, or automatically when a failed [[Morale Check]] triggers group panic.

