# GDR-007: Refined Lair Phase & Population Framework

**Role:** The Researcher & Game Mechanic  
**Status:** PROPOSED  
**Date:** 2026-05-29  
**Target:** `STAGE_Drafts/05_Base/` (Awaiting review and confirmation)

---

## 1. The Core Loop & Time (The Lair Turn)

Time in the campaign is measured in **Lair Turns**. A Lair Turn represents roughly **one week** in-game, divided into two halves: the adventure and the recovery.

```
       +--------------------------------------------+
       |                 LAIR TURN                  |
       +---------------------+----------------------+
                             |
         [FIRST HALF: THE RAID]   [SECOND HALF: THE LAIR PHASE]
         - Bosses & Mobs go      - Homecoming & Casualties
           on a mission.         - Lair Event
                                 - Labor Allocation
                                 - Construction & Upgrades
```

### The Sequence of a Lair Turn
1.  **The Raid (First Half):** The players choose a raid target, travel there, fight, collect Loot/Oddities, and survive.
2.  **Homecoming & XP (Second Half start):** The players return. They pool Loot, update Infamy, and distribute XP. Dead Bosses are added to the **Bone Pile**.
3.  **Lair Event:** The GM draws a random event card representing threats, visitors, or internal goblin drama.
4.  **Labor Phase:** Players count their surviving Grunts and allocate them between recovery, crafting, recruiting, or Lair projects.
5.  **Construction & Expansion:** Players spend pooled Loot/Scrap to clear new rooms or build facilities. Any construction finishes at the end of the turn, ready for the next week.

---

## 2. Digging vs. Expansion: Modular Lair Sites

To avoid forcing every Lair to be underground, we define the Lair by its **Site Type**. The players choose their Lair's Site Type at the start of the campaign. This dictates the theme of expansion and the type of complications they face.

```
     ┌──────────────────────────────────────────────────────────┐
     │                      LAIR SITES                          │
     └──────────────┬───────────────────┬───────────────────────┘
                    │                   │
            ┌───────┴───────┐   ┌───────┴───────┐   ┌───────────┴───┐
            │  THE CAVERNS  │   │ THE FERAL CAMP│   │ THE RUINED KEP│
            │   (Digging)   │   │  (Clearing)   │   │ (Restoring)   │
            └───────────────┘   └───────────────┘   └───────────────┘
```

### The Three Site Types
*   **The Caverns (Underground):** Caverns, mines, or sewers. Expansion is **Digging**. 
    *   *Theme:* Unstable rocks, subterranean beasts, toxic gas.
*   **The Feral Camp (Wilds):** Tents, tree-huts, or swamps. Expansion is **Clearing**.
    *   *Theme:* Aggressive flora/fauna, mudslides, exposure to weather.
*   **The Ruined Keep (Structures):** An old human fortress, tower, or cellar. Expansion is **Restoring**.
    *   *Theme:* Ancient traps, structural collapses, restless spirits.

### The "Clear & Build" Loop
The Lair sheet has a grid of **Slots**. Initially, a few slots are open (containing basic rooms), while the rest are **Locked** (representing collapsed tunnels, thick briars, or blocked hallways).

1.  **Guaranteed Success:** Expanding the Lair is never a random failure. If the players spend the required **Scrap** (e.g., 5 Scrap) and assign **Labor** (e.g., 2 Grunts), the Slot is **always cleared** at the end of the Lair Turn.
2.  **The Clear Roll:** When a Slot is cleared, the active player rolls **1d6**:
    *   **6 (Lucky Find):** The laboring goblins stumble on something useful. Gain +1d6 Loot or a random Tier 1/2 Oddity found in the debris.
    *   **2–5 (Smooth Work):** The slot is cleared without incident.
    *   **1 (Goblin Complication):** The slot is cleared, but the GM rolls on the Site-specific Complication table:
        *   *Caverns (1):* **Cave-in!** A laboring Grunt is injured and cannot work next turn.
        *   *Feral Camp (1):* **Biting Swarm!** The clearing disturbed a nest of giant hornets. The Lair takes a **Bane** on all Labor actions next turn.
        *   *Ruined Keep (1):* **Alarm Triggered!** A mechanical trap went off. The noise increases Lair Alert/Threat by +1.

---

## 3. Population: The Gobbo Pool (The Dice Are Your Workers)

Instead of tracking individual goblins or using abstract worker tokens, the Lair's total population is tracked as a single communal pool of dice: **The Gobbo Pool** (measured in **d6s**). 

For example, a developing Lair might have a total Gobbo Pool of **15d6**.

```
                   ┌───────────────────────────────┐
                   │        COMMUNAL LAIR          │
                   │          GOBBO POOL           │
                   │        (Total: 15d6)          │
                   └───────────────┬───────────────┘
                                   │
                   ┌───────────────┴───────────────┐
                   ▼                               ▼
            [RAIDER MOBS]                   [LABORER DICE]
         - Allocated to Bosses.          - Left behind in the Lair.
         - Form the Mobs for the Raid.   - Rolled to resolve Lair tasks.
         - Risk permanent loss if wiped. - Auto-heal if they survive.
```

### Allocation: Raiders vs. Laborers
At the start of each Lair Turn, before setting out on the Raid, the players collectively allocate their available **d6s**:

*   **Raider Mobs:** Players take dice from the Gobbo Pool to form their Mobs. A player Boss can command a Mob up to a Size equal to their **Grunt** stat.
    *   *Example:* In a 3-player game, if the Bosses have **Grunt 2**, **Grunt 2**, and **Grunt 3**, they can take up to **7d6** total from the pool to act as their Raider Mobs.
*   **Laborer Dice:** The remaining dice in the pool (e.g., **8d6**) stay behind in the Lair to do chores.

---

## 4. Labor Phase: Rolling Your Gobbos

During the Lair Phase, players assign their **Laborer Dice** to specific rooms or projects. To resolve these activities, the players roll the assigned dice pool. Standard exploding dice rules apply (every 6 explodes into another die to roll!). Successes are **4, 5, or 6**.

### Lair Actions & Pools
*   **Gathering Scrap:** Assign any number of Laborer dice and roll them. Every success (4+) generates **1 Scrap** for the Hoard.
*   **Clearing Slots (Construction):** Assign Laborer dice to a locked slot. Each success (4+) adds 1 progress to the room's clearance. Once the successes match the clearance cost (e.g., 5 successes), the slot is cleared. 
    *   *Complications:* For every **1** rolled on a clearance roll, a complication occurs (e.g., cave-in, wild beasts), but progress is not lost.
*   **Recruiting (Growing the Pool):** Gobbos love a crowd. You send a pool of Gobbos out into the wilds to capture or coerce other runts. Assign Laborer dice to recruitment. Roll them. Every **6** rolled (exploding!) recruits **1 new d6**, permanently adding it to the Lair's Gobbo Pool.
    *   *Boss Assist:* A Boss can spend their personal Downtime Action to assist, adding their **Mouth** stat as bonus dice to the recruitment roll.
    *   *Bribes:* The players can spend **5 Loot** from the Hoard to buy shiny junk, granting a **Boon (+1d6)** to the recruitment roll.

---

## 5. Mob Casualties & Auto-Healing

To keep the game moving and avoid punishing bookkeeping:

*   **Resilient Gobbos (Auto-Heal):** If a Raider Mob returns from a Raid with *at least 1 HP remaining on at least one die* (meaning the Mob was not completely wiped out), they immediately **auto-heal back to full Size** at no resource cost.
*   **Wiped Mobs (Permanent Loss):** If a Mob is completely wiped out during the raid (their Size drops to 0), those d6s are **permanently removed** from the Lair's Gobbo Pool. The dice are dead.

### Preventing the Death Spiral (Safety Valves)
If the Lair suffers a catastrophic raid and loses most of its Gobbo Pool, the game does not grind to a halt. We implement three safety systems:

1.  **Communal Runts (The Floor):** The Lair always has a permanent, unkillable underclass of runts. Even if the Gobbo Pool is reduced to 0d6, the Lair has a minimum baseline of **3d6 communal runts**. These runts cannot be used as Laborers at home, but they ensure each player can always bring at least a **Size 1 Runt Mob (1d6)** on a raid.
2.  **Vacant Nest Growth:** During the Homecoming step, if the Lair's Gobbo Pool is less than **3d6 per player** (e.g., under 9d6 in a 3-player game), the Lair automatically gains **1d6** to the pool for free as wandering feral goblins move into the empty nests.
3.  **Lair Capacity Cap:** The Lair's maximum Gobbo Pool size is capped by the Lair's **Infamy** (e.g., Max Pool = 5d6 per player + Lair Infamy). Building rooms like *Breeding Pits* or a *Mud Tavern* raises this cap and grants bonuses to recruitment rolls.

---

## 6. Resource Economy: Scrap vs. Loot

As established in [[GDR-002_Gang_Pillar_And_Lair_Economy.md]], we split wealth into two clean, abstract tracks:

*   **Loot (Shared Pool):** Represents portable gold, jewelry, and coin. Spent to purchase room upgrades, buy items from merchants, or bribe external factions.
*   **Scrap (Shared Pool):** Represents abstract building materials (nails, wood, iron beams, rubble). Passively generated by Lair territory, cleared chambers, and Outposts. Used to clear slots, build structures, and craft base items.

### Crafting Integration
*   To craft a Scrappy weapon, you don't spend individual metal ingots. You simply use the Lair's **Scrap Forge** room, spend 1 Laborer die, and roll your Brains.
*   The system guarantees a functional weapon is produced. The roll determines how many **Taming Successes** you get to reduce its instability (Bite) or add positive traits (see [[34_Crafting]]).

---

## 7. Summary of Choices & Trade-offs

| Choice | High-Raider Strategy | Balanced Strategy | High-Laborer Strategy |
| :--- | :--- | :--- | :--- |
| **Raid Power** | **Max Size Mobs** (huge combat advantage, safe Bosses). | Moderate Mobs (flexible, decent combat power). | Small Mobs/Runts (fragile, Bosses must carry the fight). |
| **Lair Output** | Zero or minimal Labor. Base building and crafting grind to a halt. | Slow but steady base progress; basic gear crafting. | **Maximum Laborer Dice**. Fast construction, heavy crafting engines. |
| **Risk Profile** | High risk of massive population loss if the Mob wipes. | Moderate, manageable risks. | Safe workforce at home, but high risk of Boss death during raids. |
