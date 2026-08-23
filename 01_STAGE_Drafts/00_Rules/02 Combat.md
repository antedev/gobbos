# Combat and Actions
Combat is a key mechanic in Gobbos. The combat can either be only the PC against some foe, or a more tactical battle with loads of Goblins piling on. 
The combat is structured in a number of rounds, that are repeated until the combat ends. All the players act in the Players Active turn, and then the enemies act in the Enemy Active turn. But both can use Reactions to react to anything that the other does. 

## Actions
Actions represent how much a goblin can accomplish in a round. There are three types of actions:
1.  **Standard Actions:** Every PC has **three (3) Standard Actions** per round, reset at the start of each round. Standard Actions are spent to Move, Attack, Plunder, Manipulate, or Order. They can be saved to be used as Reactions.
2.  **Free Actions:** Minor tasks that cost no Standard Actions (e.g., dropping an item, speaking, or activating passive quirks).
3.  **Reactions:** Actions taken out of turn in response to enemy actions (e.g., Dodge or Parry). You must spend a saved [[Standard Action]] to perform a Reaction.
Additionally, PCs have **one (1) Free [[Order Action]]** per round (which does not count toward their 3 Standard Actions).

Each Mob has **two (2) actions**, which are also reset at the start of each round, but they only act when Ordered. When they are left to their own devices (see [[Uncontrolled Mobs]]), they act on their own as per a predefined priority list

### Actionlist
#### Move (Mob or PC)
With a Move action, you can move up to your [[Movement]] number of zones. The different conditions of the zones are taken into account, and the movement might be limited or entirely blocked by hazards. If a climb, swim, jump, or other physical feat is required based on the circumstances in the zone, you must typically make a [[Slink]] test. The [[Difficulty]] and [[TN]] default to the established [[zone profile]] (e.g., **5+/1**), subject to GM adjustment. 
#### Attack (Mob or PC)
The Attack action can only be used in the Players Active turn. 
To Attack, the player's base [[dice pool]] is based on the player's [[Tough]] for [[Melee attack]] and [[Slink]] for [[Ranged attack]], modified by any equipment, Quirks, or other circumstances. 
*   **Kill / Wound:** If you roll successes equal to or greater than the target's current [[Defence]] (acting as the test's [[TN]]), you instantly defeat a standard enemy, deal 1 [[Wound]] to a Boss/Elite (see [Enemies](../04_Enemies/20_Enemies.md)), or reduce a Mob's [[Size]] by the number of successes scored.
*   **Stagger (Impact Size vs. Target Size):** If you roll at least **one (1) success** but fewer than the target's current [[Defence]] TN, the attack does not deal damage, but it can throw the target off balance. To inflict the [[Staggered]] condition, the attack's **Impact Size** must be equal to or greater than the target's **Physical [[Size]]** (Impact Size >= Target Size):
    *   **Calculating Impact Size:**
        *   *Standard Attacks:* Equal to the attacker's physical [[Size]] (a lone Goblin Boss is **Size 1**; a [[Mob]] uses its current **Mob [[Size]]**).
        *   *`Heavy` Weapon Trait:* Adds **+1** to Impact Size (a Size 1 Goblin swinging a heavy hammer attacks with **Impact Size 2**).
        *   *`Crushing` Weapon Trait:* Adds **+2** to Impact Size (attacks with **Impact Size 3**).
        *   *Explosives & Spells:* An explosion's Impact Size equals its **Tier** (T1 = Size 1, T2 Grenade = Size 2, T3 Powder Keg = Size 3, T4 Mortar/Cannon = Size 4, T5 Reactor = Size 5).
    *   *Result:* If Impact Size >= Target Size, the target gains the [[Staggered]] condition until the end of the round. If Impact Size < Target Size, the target has natural mass resistance and ignores the Stagger effect entirely.
*   **Bounce:** If you roll **zero (0) successes**, the attack bounces harmlessly off their armor. Nothing happens.
#### Plunder (Mob or PC)
The [[Plunder]] action is to pick up any [[Loot]] at where the Player or the Mob stands.  
#### Dodge / Parry (Reaction) & The Clatter Roll
The Dodge or Parry action can only be used as a [[Reaction]] to an incoming Attack or Environmental effect (typically during the Enemy Active turn). You **must** have saved a [[Standard Action]] from your turn to use this. If you have no saved actions, you cannot attempt to evade and must rely entirely on passive armor to absorb the blow!

When targeted by an attack with a listed **Threat** (e.g., `5+/1`) and **Damage** (e.g., `3`), resolve the defense in a single simultaneous throw—the **Clatter Roll**:
*   **Stat Dice:** Roll your active defense dice: [[Slink]] (for Dodge) or [[Tough]] (for Parry with an equipped shield or heavy weapon).
*   **Armor Dice:** Roll any passive bonus dice granted by your equipped [[Armor]] (use distinct colored dice, such as gray or black).

**Resolving the Clatter Roll:**
1.  **Check Stat Dice vs. Threat:** Count successes rolled on your **Stat Dice**. If your successes meet or exceed the attack's **Threat TN**, you achieve a clean Dodge or Parry: **you take 0 Damage**.
2.  **Mitigation on Failed Evasion:** If your Stat Dice fall short of the Threat TN (or if you had 0 saved actions), the evasion fails. You now look at your **Armor Dice**:
    *   Every success (**5+**) rolled on your Armor Dice reduces the incoming Damage by 1.
    *   Any remaining Damage is deducted directly from your [[Grit]].

**Mob Defense & The "Scatter!" Order:**
Mobs do not have individual attributes and cannot naturally dodge. When targeted by an attack, a Mob resolves defense based on its state and orders:
1.  **Passive Armor:** If equipped with Armor, the Mob rolls its passive Armor Dice against incoming damage, with each success reducing damage by 1.
2.  **Active Scatter ("Scatter!" Reaction):** If a Mob is targeted by an attack, the Boss can spend a saved [[Standard Action]] (or an unused Free Order Reaction) to scream "Scatter!". The Mob rolls active defense dice equal to the Boss's [[Mouth]] stat.
    *   **The Size Target Penalty:** Large mobs occupy more space and are sluggish to disperse. Every point of Mob [[Size]] above 1 increases the enemy attack's Threat TN by **+1** for the Scatter test (e.g., a Size 3 Mob faces a +2 TN penalty).
    *   **Clean Scatter:** If the Mouth dice meet the modified Threat TN, the Mob evades completely (0 damage) and immediately moves **1 Zone** into cover.
    *   **Failed Scatter:** If the Mouth dice fail, the Mob takes damage normally, reduced only by any passive Armor Dice successes.
    *   **Mob Gambling (High-Stakes Mouth Gamble):** If the initial Scatter roll falls short, the Boss may use the [[Gobbo Gamble]] to reroll all **1s** on the Mouth dice. 
        *   *If the Gamble succeeds:* The Mob pulls off a miracle dive and takes 0 damage.
        *   *If the Gamble fails:* Panic ensues! The Mob takes the full attack damage, suffers **1 Trample Damage** applied to every single die in the Mob's health pool (like an AoE crush), drops **1 Bulk** of carried [[Loot]], and immediately breaks into the [[Out of Control]] state. If the Boss is present in the same [[Zone]], the Boss is caught in the stampede and gains the [[Staggered]] condition until the end of the round.

### GM Tactics: Group Attacks (Enemy Swarms)
If multiple enemies surround and attack a Gobbo, the GM should NOT make separate attacks. Instead, they combine into a [[Group Attack]]. While a PC can only be attacked by a maximum of 3 enemies, there is no limit on attacker on a Mob
*   The base damage is the primary enemy's Attack stat, **+1 damage** for every additional enemy in the swarm. 
*   The player only spends **one** saved Action to Dodge/Parry the entire [[Group Attack]]. 
> *GM Advice:* Avoid splitting enemies into many small attacks against a single PC. This will instantly drain their saved actions and create a frustrating "death by a thousand cuts." Swarm them into Group Attacks instead!

#### Manipulate
The Manipulate action is a catch-all for whenever a Mob or PC tries to interact with an item or the environment in any way. The base [[dice pool]] is based on whatever attribute is most relevant to the action, modified by any equipment, Quirks, or other circumstances. The GM sets the [[Difficulty]] and [[TN]] (typically **5+/1**). 

#### Order 
The [[Order action]] is used to give commands to your goblins, directing a Mob to use both of their actions for the round. Standard Orders to controlled Mobs do not require a dice roll.
*   **The 3 Mob States:** A Mob is always in one of three states on their turn:
    *   **Ordered:** Direct instructions from the Boss. They spend both actions as ordered (0 saved actions for defense).
    *   **[[Loitering]]:** Under control, but receives no orders. Goblins use **1 action** to loiter (roll/choose on the [[Loitering]] Table in [Goblin Mobs](../01_Characters%20&%20Mobs/13_Goblin_mob.md)) and save **1 action** for defense (1d6 [[Defence]]).
    *   **[[Out of Control]]:** Broken command (out of sight, size exceeds Grunt, or failed morale). They spend both actions running amok under GM control (roll/choose on the [[Out of Control]] Table in [Goblin Mobs](../01_Characters%20&%20Mobs/13_Goblin_mob.md)), leaving them with 0 saved actions for defense.
*   **Regaining Control:** To regain control of an [[Out of Control]] Mob, the Boss must spend a [[Standard Action]] to [[Order]] them, resolving it using the standard command test rules in [Giving Orders](04_Giving%20orders.md). On a success, the Mob becomes controlled and receives their instructions; on a failure, they ignore the Boss and remain [[Out of Control]].
*   **Cross-Gang Super Mobs:** Issuing an Order to a Mob merged from multiple different player Gangs *always* requires a Grunt test (Test [[Tough]] if in the same Zone, or [[Mouth]] from afar).
*   **The Boredom Rule:** Mobs have short attention spans. When acting (Ordered, [[Loitering]], or [[Out of Control]]), a Mob cannot perform the exact same action twice (e.g., they cannot Attack twice, or Plunder twice). *Exception:* A Mob *can* take the Move action twice if they are fleeing or charging.
*   **[[Free Orders]] & Maximum Mobs:** Your ability to command the swarm is dictated strictly by your [[Mouth]] stat progression (see [[Stat|Stats]]). As you level up Mouth, you can command more Mobs simultaneously, and you are granted additional [[Free Orders]] per round. You never have to spend your Standard Actions to issue these [[Free Orders]]!


## Cover
Taking cover behind walls, pillars, or upturned tables protects you from ranged attacks. There are two levels of cover:
*   **[[Partial Cover]]:** You are partially blocked (e.g., behind a low barricade, crate, or thick foliage).
    *   **Attacking a target in [[Partial Cover]]:** If a PC or Mob attacks a target in [[Partial Cover]], the attack roll suffers a [[Bane]] (-1d).
    *   **Defending while in [[Partial Cover]]:** If you are in [[Partial Cover]] and are targeted by a [[ranged attack]], you gain a [[Boon]] (+1d) to your [[Dodge]] test.
*   **[[Full Cover]]:** You are completely hidden behind a solid obstacle (e.g., a stone pillar, wall, or closed door).
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
[[Raid points]] are calculated, including currently held as well as confirmed, based on objectives and the basic Raid rules. 
#### Conditions
All around the table are recommended to do a short assessment of the current standing. How hurt any mobs are, where the enemies are and whatever conditions they might have. Any conditions with End of Round abilities is carried out now. Additionally, all [[Staggered]] conditions on PCs, Mobs, and Enemies are automatically removed. 
#### Moral check
The GM and the players do a [[Morale Check]] if needed, to see if some or all flees. Few opponents fight to the death, unless there is no alternatives (or they are immune to Morale)
#### Environmental effects
The GM checks for any changes in the Environment, such as spreading fire or smoke. Perhaps the a damn has been broken floods the battlefield or a fissure in the ground spews out lava. Note down any zones affected by these changes. 
#### Reset actions
If the combatants are still willing to fight, go back to the Round start, and resets everyone's actions.
### Combat End 
If there are no one fighting on one side, or one side gives up or flees, the Combat ends. 
#### Fleeing (Tactical Retreat)
Goblins are cowards at heart, and running away is a highly viable survival strategy.
*   **Escape Zones:** To flee an encounter, a PC or Mob must move into a designated escape zone or exit.
*   **Disengaging & Opportunity Attacks:** If a PC or Mob attempts to leave a Zone containing alert enemies, they trigger a reactionary Opportunity Attack from each enemy in the zone. To prevent this, they must spend a [[Standard Action]] to Disengage, testing [[Slink]] against a difficulty of **5+** and successes required equal to the highest enemy [[Defence]] TN (denoted as **5+/Defence**). On a success, they may move out of the Zone safely.
*   **Carrying Bulk:** Goblins fleeing with heavy treasure are slowed. Standard movement and dragging penalties for [[Bulk]] apply while fleeing. A PC or Mob can choose to drop their loot as a [[Free Action]] to restore full movement speed.
*   **Mob Fleeing:** Mobs flee when given a "Scatter" or "Retreat" Order, or automatically when a failed [[Morale Check]] triggers group panic.

