# Carrying Stuff & Load Capacity

*Greed is a goblin's greatest virtue and heaviest burden. You can find all the shiny crowns, gilded idols, and copper kettles in the world, but they do you no good if you are too weighed down to outrun the angry troll chasing you.*

---

## Goblin Boss Carry Limits

Your capacity to carry weapons, armor, tools, and plunder into and out of a raid is determined directly by your [[Tough]] stat. Your secondary stat **[[Carry]]** defines how many units of [[Bulk]] you can carry unhindered.

### Carry Capacity Progression

| Tough Level | Unburdened Carry Capacity | Over-Laden Threshold | Maximum Dragging Limit (2x Carry) |
| :---: | :---: | :---: | :---: |
| **Level 1** | **6 Bulk** | 7–7 Bulk | 12 Bulk |
| **Level 2** | **8 Bulk** | 9–10 Bulk | 16 Bulk |
| **Level 3** | **10 Bulk** | 11–13 Bulk | 20 Bulk |
| **Level 4** | **12 Bulk** | 13–16 Bulk | 24 Bulk |
| **Level 5** | **14 Bulk** | 15–19 Bulk | 28 Bulk |

*Calculation:* Your baseline **[[Carry]]** capacity is **4 + (2 x Tough) Bulk**.

---

## Load States & Encumbrance

Whenever you pick up new [[Loot]] or gear, add together the total [[Bulk]] of all carried and equipped items to determine your current **Load State**:

| Load State | Carried Bulk | Movement Profile | Physical Test Modifiers | Combat & Defense Effects |
| :--- | :--- | :--- | :--- | :--- |
| **Unburdened** | Less than or equal to **Carry** | Normal ([[Movement]] Zones per [[Move]] action) | None | Full standard actions and reactions. |
| **Over-Laden** | **Carry + 1** to **Carry + Tough** | **-1 Zone** per [[Move]] action (minimum 1 Zone) | **Bane 1 (-1d)** on all physical [[Slink]] and [[Tough]] tests | Cannot perform two [[Move]] actions in the same round. |
| **Dragging** | **Carry + Tough + 1** to **2x Carry** | Fixed at **1 Zone** per [[Move]] action | Automatic failure on stealth and jumping tests | Requires **both hands**; cannot attack with weapons or perform [[Dodge]] / [[Parry]] reactions (0 active defense). |
| **Immobilized** | Greater than **2x Carry** | **0 Zones** (Cannot move) | Automatic failure on all movement tests | Must drop items as a [[Free Action]] to restore mobility. |

---

## The Bulk 3+ Item Rule

Most standard weapons and tools are Bulk 1 or 2, fitting neatly into packs, belt holsters, or single-hand grips. Heavy objects of **Bulk 3 or higher** (such as massive iron chests, great anvils, stone gargoyles, or siege kegs) are clumsy and require special handling:

*   **Two Hands Required:** Hauling a loose Bulk 3+ item requires **two hands**. While holding it, you cannot wield a weapon, hold a shield, or perform somatic spellcasting.
*   **Dropping as a Free Action:** You may drop a carried Bulk 3+ item at any time as a [[Free Action]] (even during an enemy's turn before rolling a [[Dodge]] reaction).
*   **Boss Item Limit:** A [[Goblin Boss]] cannot haul more than half their Tough (Tough / 2, rounded down; minimum 1) in loose Bulk 3+ items at one time. For example, a Boss with Tough 1–3 can haul at most one loose Bulk 3+ item, while a Boss with Tough 4–5 can haul two.

---

## Mob Carrying Capacity

A [[Mob]] of lesser goblins can haul far more plunder than a lone Boss, making them essential pack mules during a raid.

### Mob Capacity & Movement
*   **Unburdened Mob Limit:** A Mob carries up to **Size x 4 Bulk** without any penalties.
*   **Dragging Mob Limit:** A Mob can drag up to **Size x 5 Bulk**. While dragging, the Mob's movement is fixed at **1 Zone per Move action**, and the Mob cannot execute the reactive **"Scatter!"** maneuver.

### Clunky Plunder in Combat (The -1d Fighting Penalty)
Lesser goblins are easily distracted. If a Mob is forced to haul heavy, awkward objects into battle, fewer goblins have their hands free to stab enemies:
*   Every single object of **Bulk 3+** carried by a Mob imposes a **Bane 1 (-1d)** penalty on that Mob's combat attack pool.
*   A Mob can carry a maximum number of Bulk 3+ items equal to its current **Size**.

### Mid-Raid Casualties & Dropped Plunder
If a Mob suffers damage that reduces its **Size**, its carrying capacity drops immediately.
*   If the Mob's carried Bulk now exceeds its new maximum capacity, the controlling [[Goblin Boss]] must **immediately declare which Loot items are dropped** in the current [[Zone]].
*   A Mob can also voluntarily drop Loot as a [[Free Action]] on its turn to clear combat penalties. Picking dropped items back up requires spending 1 [[Plunder]] action per item.

---

## Examples

> **Example (PC Load):**
> Grugor is a goblin Boss with **Tough 3** and **Movement 3**. His baseline **Carry** capacity is **10 Bulk** (4 + 2 x 3).
>
> He enters a crypt wearing Medium Armor (Bulk 2) and carrying a Shortsword (Bulk 2), a Shield (Bulk 1), and a Crowbar (Bulk 1), totaling **6 Bulk** (Unburdened).
>
> In the burial vault, Grugor scoops up a jeweled goblet (Bulk 1, Loot 2) and a heavy sack of silver (Bulk 2, Loot 4). His total load is now **9 Bulk**—still within his 10 Bulk limit, allowing him to move 3 Zones per Move action.
>
> He then finds a solid bronze statue (Bulk 3, Loot 5). Picking it up pushes his total load to **12 Bulk**. Because 12 Bulk falls into his **Over-Laden** bracket (11–13 Bulk for Tough 3), his movement drops from 3 Zones to 2 Zones per Move action, all his physical Slink and Tough tests suffer **Bane 1 (-1d)**, and carrying the Bulk 3 statue occupies both of his hands. If guards arrive, Grugor can drop the statue as a Free Action to draw his sword and regain his full mobility.

> **Example (Mob Plunder & Casualties):**
> Boss Skitter commands a **Size 3 Mob** of spearmen. The Mob can carry up to **12 Bulk** unburdened (3 x 4).
>
> During a raid on a tavern, Skitter orders the Mob to loot an iron beer keg (Bulk 3, Loot 3) and three sacks of cured ham (Bulk 2 each, totaling 6 Bulk). The Mob carries **9 Bulk** total, well within its 12 Bulk limit.
>
> However, because the Mob is hauling one Bulk 3 item (the beer keg), two goblins are occupied holding the barrel, imposing **Bane 1 (-1d)** on the Mob's attack rolls.
>
> An enemy knight charges in and deals enough damage to reduce the Mob from **Size 3 to Size 1**. At Size 1, the Mob's unburdened capacity plummets to **4 Bulk** (1 x 4). The Mob is instantly over capacity (holding 9 Bulk against a 4 Bulk limit). Skitter must immediately choose what to drop. Skitter commands them to dump the heavy beer keg (Bulk 3) and one sack of ham (Bulk 2), leaving the surviving runt clutching the remaining 4 Bulk of ham as the runt scurries away.