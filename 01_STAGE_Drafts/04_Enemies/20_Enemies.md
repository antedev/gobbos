# Enemies

The GM does not roll dice in Gobbos. Therefore, enemies are entirely deterministic. They don't test for success; their stats represent guaranteed threats that the players must actively survive and overcome. 

## The Enemy Stat Block
Every standard enemy has a simple 5-Stat block:

1.  **Attack:** The base physical damage they deal automatically when they attack a Gobbo or Mob.
2.  **Defence (Target Number):** The number of successes a Gobbo needs to roll on an Attack test to instantly kill this enemy.
3.  **Movement:** How many Zones they can cross in a single action.
4.  **Range:** Melee (same Zone) or Ranged (X Zones).
5.  **Special:** A unique ability, behavior, or attack difficulty modifier.

> *Example: Angry Farmer*
> *Attack: 1 (Pitchfork) | Defence: 1 (Unarmored)*
> *Movement: 1 | Range: Melee | Special: None*

## Action Economy 
Like PCs, standard Enemies get **2 Actions** per round (usually Move and Attack). They always act during the *Enemy Active Turn*. They can not use both action to Attack. 

### Enemy Equipment
Enemies do not use the player bulk or equipment rules. An enemy's Attack and Defence stats already account for their weapons and armor. 

> *Example: An Armored Knight has Defence 3 because they wear plate mail, and Attack 3 because they swing a greatsword. The GM does not track the durability of the Knight's gear.*

If a PC loots an enemy, the GM translates that flavor into PC mechanics (e.g., "You loot the Knight and find a *Heavy Iron Sword*: Bulk 2, +1d6 Attack").

---

## Bosses & Wounds
The "One-Hit Kill" system applies to 90% of the foes you fight. However, massive monsters and Elite Bosses use **Wounds**.

*   A Boss has a standard **Defence TN**, but also a **Wounds** track.
*   To deal *one* Wound to a Boss, a player must roll successes equal to or greater than its Defence TN in a single attack. 

> *Example: A Cave Troll has Defence 3, Wounds 3. A Gobbo attacks and rolls 3 successes. The Troll loses 1 Wound.*

**The Overkill Rule:** For every multiple of the Defence TN achieved on a single roll, the Boss takes an additional Wound. Rolling 6 successes against a Defence 3 Troll deals 2 Wounds!

---

## Morale 
Not every enemy fights to the death. Goblins win by being a terrifying, chaotic green swarm. Every enemy group has a static **Morale TN**. (e.g., Peasant = TN 1, Guard = TN 3, Undead = Immune (They are already dead, so they can fight to the death)).

### The Morale Check
A Morale Check is triggered at the end of the round if the enemies suffered a catastrophic loss (e.g., losing 50% of their numbers, their Captain dying, or suffering massive explosive damage).

*   **The Roll:** The players roll a combined `Swarm Terror` pool of D6s. The number of dice equals the **Total Size of all surviving Mobs + Surviving PCs** in the current and adjacent Zones. 
*   **The Result:** If the players roll successes equal to or greater than the Enemy's Morale TN, the enemies break!

> *Example: There are 2 PCs alive, and they share a Size 4 Mob and a Size 2 Mob. A Morale Check triggers against the remaining Guards (TN 3). The players roll a massive pool of 8d6 (2 PCs + 6 Mob Size). They get four successes. The Guards break!*

### Fleeing
When enemies break, they drop all heavy loot (not weapon and armour, unless it makes it easier to flee) and must use their 2 Actions on their turns to frantically move toward the nearest exit or safety. 

### Regrouping (The Rally)
TDB: Needs to be revisited. 
Broken enemies will keep running until they leave the map. However, if there is a surviving **Enemy Commander** (like a Boss or Captain) who did *not* break, they can use an action to scream at the fleeing troops. This triggers a new, opposed Morale Check:
*   The Gobbos roll their Swarm Terror pool against the Commander's Morale TN. 
*   If the Gobbos triumph again, the troops keep running.
*   If the Gobbos fail, the Commander successfully rallies the troops, and they stop fleeing.
