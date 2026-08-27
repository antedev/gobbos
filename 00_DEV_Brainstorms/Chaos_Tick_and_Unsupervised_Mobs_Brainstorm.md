# Brainstorm: The Chaos Tick & Unsupervised Mobs

*Preserved from 04_Zones_and_Movement.md for future evaluation and potential reintroduction in a more fitting chapter (such as Mob Mechanics, Base Building, or Raid Phase transitions).*

---

## Overview Concept

When a player chooses to split their forces and leave an unsupervised Mob behind at an inactive macro map node (for example, to guard a captured chokepoint, harvest a scrap pile, or hold a rear exit), that node is removed from active micro-combat tracking.

>> **Active vs. Background Tracking:** Active tactical zones are tracked in micro-combat rounds, while unsupervised mobs at distant macro nodes resolve their actions via the **Chaos Tick** (evaluated at scene end, dungeon transition, or Raid Phase closure rather than every combat round).

---

## Unsupervised Mob Priority AI

Without direct Boss supervision, an unsupervised Mob automatically follows its base instinct priority list:
1. **Survival:** Flee from overwhelming threats or lethal hazards.
2. **Loot & Eat:** Scavenge loose food, mushrooms, shiny objects, and Scrap.
3. **Violence:** Attack vulnerable stragglers or pick fights with nearby rivals.
4. **Trash Stuff:** Vandalize architecture, smash furniture, and dismantle machinery.
5. **Wander Off:** Scurry into adjacent corridors following noise or smell.

---

## Legacy Chaos Tick Mechanics (For Revision)

### Resolving the Chaos Tick
The controlling player rolls a number of **d6s equal to the unsupervised Mob's current Size**. The test resolves against **Normal (5+/1)** difficulty:
* **Successes (5+):** Tally successes to determine task progress and loot secured.
* **Ones (1s):** Each **1** rolled represents growing insubordination and friction. Tally all **1s** rolled, add **+1 die per 1 rolled** to the communal **Bangaranga Pool**, and consult the **Gobbo Mischief Table**.
* **The Farkle:** Rolling **zero successes** and **two or more 1s** triggers a catastrophic failure, causing the Mob to mutiny, trigger a trap, or wander off the map.

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
