# Enemy Stats & Combat Mechanics Draft

*Context: Shifting away from GM-tracked Hit Points to a static "One-Hit Kill" threshold system for 90% of enemies, speeding up combat significantly.*

## Core Philosophy
The GM does not track HP for standard enemies. Goblins are lethal when they swarm, and combat should be resolved instantly. An enemy's survivability is reflected in how hard they are to hit, not how many hits they can take. 

## The 5 Enemy Stats
Every standard enemy has a very simple stat block:
1.  **Attack:** The base physical damage they deal automatically when they attack a Gobbo.
2.  **Defence (Target Number):** The number of successes a Gobbo needs on an Attack roll to instantly kill this enemy.
3.  **Movement:** How many Zones they can cross in an action.
4.  **Range:** Melee (same Zone) or Ranged (X Zones).
5.  **Special:** A unique ability, Boon, or attack difficulty modifier (e.g., "Hard Attack" or "Creates Fire").

### Example Profiles
*   **Angry Farmer:** 
    *   *Attack:* 1 (Pitchfork) | *Defence:* 1 (Unarmored)
    *   *Movement:* 1 | *Range:* Melee | *Special:* None
*   **Human Soldier:** 
    *   *Attack:* 2 (Sword) | *Defence:* 2 (Leather Armor/Shield)
    *   *Movement:* 1 | *Range:* Melee | *Special:* Shield Wall (Requires +1 Success if attacked from the front).
*   **Armored Knight:**
    *   *Attack:* 3 (Greatsword) | *Defence:* 3 (Plate Armor)
    *   *Movement:* 1 | *Range:* Melee | *Special:* **Hard Attack.** The Knight is incredibly skilled; dodging their attacks is a *Hard* difficulty test (Success only on a 6).

## How Combat Flows

### Gobbo Attacks Enemy (The "One-Hit Kill")
A player attacks the Knight (Defence 3). They roll their `Tough` stat for a Melee Attack. 
*   If they roll 3 or more successes, their rusty spear finds a chink in the Knight's plate armor. The Knight instantly dies. 
*   If they roll 1 or 2 successes, the attack simply bounces off the armor. No effect. 
*   *(Note: This makes Gobbos teaming up or Mobs swarming essential for taking down high-Defence targets).*

### Enemy Attacks Gobbo (Dodge & Parry)
Because the GM does not roll dice, an enemy's Attack represents *guaranteed incoming damage*. 

When an enemy targets a Gobbo, the player must use a **Reaction** to survive:
1.  **Dodge:** The player tests `Slink`. 
2.  **Parry:** The player tests `Tough` (requires a weapon/shield). 
*   **The Math:** Every success the player rolls reduces the incoming Attack damage by 1. 
*   *Example:* The Knight attacks a Gobbo. The Knight's Attack is 3, and their Special makes dodging *Hard* (Success on 6s only). The Gobbo rolls 4d6 for Slink, getting two 6s (2 successes). The 3 Damage is reduced by 2. The Gobbo takes 1 Damage. 

### Armor
If a Gobbo wears Armor, it is a static Damage Reduction that applies *after* the Dodge/Parry roll. 
*   *Example:* Same scenario as above. The Gobbo takes 1 Damage. However, the Gobbo is wearing a Bucket Helmet (Armor 1). The 1 Damage is completely negated. 

## Boss Monsters
What about Dragons or Raid Bosses?
They use the same system, but introduce **Wounds**. 
*   **The Dragon (Defence 4, Wounds 3).** 
*   To deal *one* Wound to the Dragon, a Gobbo must roll 4 successes. The Dragon doesn't die until it takes 3 Wounds. 
*   This is the *only* time the GM tracks health, reserving it solely for epic encounters.
