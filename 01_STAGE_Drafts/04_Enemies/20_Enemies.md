# 20. Enemies

*Goblins are small, weak, and easily squished. The world is full of big, scary things that want to squash them. But a goblin doesn't fight one-on-one—they fight as a screeching horde, using dirty tricks and chaotic numbers to bring down the tall-men.*

---

## 1. Core Enemy Framework

All combat encounters in Gobbos are governed by three overarching rules that define how enemies operate:

### Deterministic Threats
The GM never rolls dice. Enemies do not test for success or roll to hit. Their actions are guaranteed threats. If an enemy attacks a [[Boss]] or [[Mob]], it deals its listed damage automatically unless the player spends a saved action to [[Dodge]] (testing [[Slink]]) or [[Parry]] (testing [[Tough]]).

### The Three Enemy Scales
Enemies are structured into three distinct mechanical types to determine how they take damage and die:
1.  **Standard Enemies:** The default foe. They are **One-Hit Kill**. Rolling successes equal to or greater than their [[Defence]] [[Target Number (TN)]] instantly defeats them.
2.  **Bosses & Elites:** Powerhouses that cannot be killed in a single strike. They track damage using a [[Wound|Wounds]] track.
3.  **Enemy Mobs:** Groups of standard enemies acting as a single unit, using a shared **Dice-HP** pool.

---

## 2. The Stat Block

Every enemy is defined by a standardized, table-based stat block. The top section contains the creature's core metadata, followed by their defense, movement, and morale attributes. Below that are any unique passive or triggered behaviors, followed by their specific combat actions.

### Stat Block Fields
*   **Name & Type:** The name of the enemy and their mechanical scale ([[Standard]], [[Elite]], [[Boss]], or [[Mob]]).
*   **Size:** The physical [[Size]] classification of the enemy. 
*   **Defence:** The number of successes a [[Player]] must roll on an [[Attack]] test to deal a [[Wound]] or instantly kill the enemy.
*   **Movement:** How many environmental [[Zones]] the enemy can cross with a single [[Move]] action. 
*   **Morale:** The **Morale TN** the players roll against when forcing a [[morale check]].
*   **Tags:** Standardized keywords representing physiological or behavioral modifiers.
*   **Special:** Any unique, custom rules or passive abilities.
*   **Attacks:** The combat options the enemy can execute.
    *   **Attack (TN):** The difficulty and [[Target Number (TN)]] a player must roll on their [[Dodge]] or [[Parry]] test to avoid the attack.
    *   **Damage:** The flat amount of damage dealt if the player fails to defend.
    *   **Range:** The distance the attack can reach (Melee or Ranged).
    *   **AoE:** The area of effect, if it hits multiple targets.
    *   **Special:** Any special rules applied when using this attack.

> **Example: Angry Farmer**
> *Standard Humanoid (Size 1)*
> 
> | Defence | Movement | Morale | Tags |
> | :---: | :---: | :---: | :--- |
> | **1** | **1** | **1** | None |
> 
> **Special:** None
> 
> #### [[Attack|Attacks]]
> | Attack | Target (Attack) | Damage | Range | Special |
> | :--- | :---: | :---: | :---: | :--- |
> | **Rusty Pitchfork** | 5+/1 | 1 | Melee | None |

---

## 3. The Trait Hierarchy Framework

To minimize GM cognitive load and prevent rules bloat, all enemy behaviors and custom capabilities are structured into a strict three-layer rules hierarchy. This framework categorizes creature properties based on their scope and how they are resolved during play.

### Layer 1: Ancestries
Every creature belongs to exactly **one** Ancestry, which establishes its core behavioral and psychological foundation.
*   **The Behavioral Foundation:** The Ancestry dictates how the creature reacts to [[Morale Check|Morale Checks]], psychological conditions (such as [[Terrified]] or [[Dumb]]), and natural healing.
*   **GM Resolution:** Ancestry rules are universal. The GM resolves ancestry behaviors using the main rules reference, meaning individual stat blocks do not need to print these rules.

### Layer 2: Standardized Tags
Standardized Tags modify a creature's physical properties, movement, or targeting capabilities. A creature may possess zero, one, or more standardized tags.
*   **The Physical Modifier:** A tag represents a common physiological trait (such as flight, size scaling, passive armor, or stealth). Each tag applies a fixed, standard mechanical modifier to the core combat and movement rules.
*   **GM Resolution:** Tags are standardized keywords. If an enemy has a tag on its stat block, its effect is resolved using the universal tags reference catalog.

### Layer 3: Unique Statblock Traits
Unique Statblock Traits are specialized behaviors or combat tactics custom-written for a specific creature type.
*   **The Local Exception:** A unique trait is written directly in the "Special" field of the enemy's stat block. It applies a custom modifier that overrides standard rules when its specific trigger is met.
*   **The Slot Limit:** To prevent rules bloat, standard enemies are strictly limited to a maximum of **one (1) unique statblock trait**. Elites and Bosses may hold a maximum of **two (2) unique statblock traits**.
*   **GM Resolution:** Because unique traits are spelled out directly on the monster's stat block, the GM can read and resolve them in real-time without flipping to other rule documents.

---

## 4. Enemy Mobs (Swarms)

Enemy Mobs represent swarms of standard, weak units acting as a single tactical squad.

### Symmetrical Health (Dice-HP)
An Enemy [[Mob]] of **Size X** (Size 1–5) is tracked using **X physical D6s** on the table, starting at the "6" face. 
*   **Standard Damage:** Damage reduces the face of a single die. Spillover damage applies. 
*   **AoE / Cleave:** [[Area of Effect (AoE)]] and Cleave attacks apply their damage to **every single die** in the Mob's pool simultaneously.
    *   *Cleave Attacks:* A player using a weapon/ability with the `Cleave` trait can distribute their excess **successes** to kill multiple units in the Mob (each multiple of the unit's [[Defence TN]] removes 1 point of Mob Size).
    *   *AoE Attacks:* An `AoE` attack (like a fire bomb) deals its flat damage directly to every die in the Mob's pool.

### Deterministic Damage Scaling
An Enemy [[Mob]]'s automatic damage scales with its size:
$$\text{Mob Damage} = \text{Base Unit Damage} + (\text{Current Size} - 1)$$

### Mob Constraints
*   **No Elite Mobs:** [[Mob|Mobs]] can only consist of standard, one-hit-kill enemies. Elite and Boss enemies must always be fought as individual units.
*   **Mob Morale Units:** Each point of current [[Mob]] [[Size]] counts as one "unit" when calculating the 50% catastrophic loss threshold for group [[Morale Check|Morale Checks]].

---

## 5. Bosses, Elites, and Wounds

Elite units and Bosses utilize a [[Wound|Wounds]] track.
*   To deal 1 [[Wound]] to a Boss, a player must roll **successes** equal to or greater than its [[Defence]] [[Target Number (TN)]] in a single attack.

>> **GOLDEN RULE: The Overkill Rule**
>> For every multiple of the [[Defence]] [[Target Number (TN)]] achieved on a single roll, the Boss takes an additional [[Wound]]. 

---

## 6. Morale & Group Flight

Every enemy group has a static **Morale TN** (e.g. Peasant = **5+/1**, Guard = **5+/3**).

### The Morale Check
A group [[Morale Check]] is triggered at the end of the round if the enemies suffered a catastrophic loss (e.g. losing 50% of their total units/[[Mob]] [[Size]], their Commander dying, or suffering massive explosive damage).

*   **The Roll:** The players roll a combined `Swarm Terror` pool of **d6s** against a target of **5+** (successes on 5 or 6). The number of dice in the pool equals the **total Size of all surviving Mobs + surviving PCs** in the current and adjacent [[Zones]].
*   **The Result:** If the players roll **successes** equal to or greater than the enemy group's **Morale TN**, the enemies break!

### Fleeing
When enemies break, they drop all heavy loot and must use their 2 Actions on their turns to move toward the nearest exit or safety. If their escape path is physically blocked, fleeing enemies will use their actions to shove, smash, or attack whatever stands in their way.

### Regrouping (The Rally)
If there is a surviving **Enemy Commander** who did not break, they can use an action to rally the fleeing troops. This triggers an opposed [[Morale Check]]:
*   The players roll their Swarm Terror pool against the Commander's **Morale TN**. 
    *   *Fiction:* The players roll to represent the Goblins banging their shields, screaming, and actively drowning out the Commander's orders to keep the enemies panicked.
*   If the players succeed, the troops keep running.
*   If the players fail, the Commander successfully rallies the troops, and they stop fleeing.
