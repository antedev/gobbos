# Attributes, Boss Profile & Gang Fundamentals

*Every goblin Boss clawed their way to the top of the muck pile by being slightly meaner, faster, louder, or weirder than the screaming runts around them. But individual bosses are disposable; it is the Gang that endures, hoarding scrap and building a bloody legacy across generations.*

This chapter defines the attributes and secondary metrics of a **Goblin Boss**, the character creation engine, the rules governing authority and **Grunt**, the persistent mechanics of the **Gang as Class Archetype**, and the structural schema for **Quirks**.

---

## Main Attributes (Level 1 to 5)

Every **Goblin Boss** possesses four **Main Stats** rated from **Level 1** to **Level 5**. A rating of Level 1 represents basic goblin competence, while Level 5 represents the pinnacle of goblin prowess.

```
+-----------------------------------------------------------------------------+
|                               MAIN STATS                                    |
|   TOUGH (T)   •   SLINK (S)   •   MOUTH (M)   •   BRAINS (B)                |
+-----------------------------------------------------------------------------+
```

*   **Tough (T)**: Muscle, physical violence, brute resilience, intimidation, and raw lifting power. Tough forms the base dice pool for melee attacks and heavy physical feats.
*   **Slink (S)**: Agility, sleight of hand, stealth, acrobatics, balance, and quick reflexes. Slink forms the base dice pool for ranged attacks and evasion.
*   **Mouth (M)**: Shouting, bullying, bluffing, herd control, and vocal leadership. Mouth forms the base dice pool for commanding Mobs and rallying disorganized goblins.
*   **Brains (B)**: Cunning, trap awareness, salvage valuation, mechanical crafting, and volatile magic words. Brains forms the base dice pool for noticing hidden hazards, disarming mechanisms, crafting gear, and casting spells.

>> **IMPORTANT (Retirement at Level 6):** If any Main Stat advances to **Level 6**, the Boss immediately retires from active raiding to become an **Elder** (see [Elders & Retirement](#elders--retirement)).

---

## Secondary Stats & Progression Tracks

Each **Main Stat** governs two derived **Secondary Stats** that scale automatically as the parent stat increases:

```
                  +-------------------> Grit (Damage Capacity: 3 to 5)
                  |
        +-- TOUGH +-------------------> Carry (Max Bulk: 6 to 14)
        |
        |         +-------------------> Movement (Zones per Move: 2 to 5)
        +-- SLINK +
        |         +-------------------> Passive Defence (Mitigation Dice: 0d to 2d)
BOSS ---+
        |         +-------------------> Max Mobs (Simultaneous Mobs: 1 to 3)
        +-- MOUTH +
        |         +-------------------> Free Orders (Commands per Round: 1 to 3)
        |
        |         +-------------------> Power Words (Spell Tag Slots: 0 to 6)
        +-- BRAINS+
                  +-------------------> Crafting Capacity (Oddity Slots: 1 to 5)
```

### Tough Derived Stats: Grit & Carry

| Tough Level | Grit (Damage Capacity) | Carry Capacity (Max Bulk) |
| :---: | :---: | :---: |
| **Level 1** | **3** | **6 Bulk** |
| **Level 2** | **4** | **8 Bulk** |
| **Level 3** | **4** | **10 Bulk** |
| **Level 4** | **5** | **12 Bulk** |
| **Level 5** | **5** | **14 Bulk** |

*   **Grit**: Your Boss's damage capacity. When you suffer unmitigated damage from enemy attacks or hazards, your current **Grit** is reduced point-for-point. When your **Grit** reaches 0, you suffer your **Final Act** and die (see [Damage, Grit and Wounds](07_Damage_Grit_and_Wounds.md)).
*   **Carry Capacity**: The maximum total **Bulk** of weapons, armor, tools, and plunder your Boss can physically carry without penalty. 
    *   **Over-Laden Rule**: If your carried Bulk exceeds your **Carry Capacity**, you suffer **-1 Zone Movement** per Move action and a **Bane 1 (-1d)** on all physical **Slink** and **Tough** tests. You cannot carry more than your Carry Capacity $+ 4$ Bulk under any circumstances.

### Slink Derived Stats: Movement & Passive Defence

| Slink Level | Movement (Zones per Move) | Passive Defence (Armor Mitigation Dice) |
| :---: | :---: | :---: |
| **Level 1** | **2 Zones** | **0d** |
| **Level 2** | **3 Zones** | **0d** |
| **Level 3** | **3 Zones** | **+1d6** |
| **Level 4** | **4 Zones** | **+1d6** |
| **Level 5** | **5 Zones** | **+2d6** |

*   **Movement**: The maximum number of discrete environmental **Zones** your Boss can cross by spending a single **Move** action (see [Zones, Movement & Environment](04_Zones_and_Movement.md)).
*   **Passive Defence**: Innate dodging reflexes that grant passive mitigation dice. These dice are rolled alongside your equipped armor dice in the **Clatter Roll**, reducing incoming damage on rolls of **5+** even if you have saved zero actions to actively Dodge (see [Combat Engine](05_Combat_Engine.md)).

### Mouth Derived Stats: Max Mobs & Free Orders

| Mouth Level | Max Controlled Mobs | Free Orders per Round |
| :---: | :---: | :---: |
| **Level 1** | **1 Mob** | **1 Free Order** |
| **Level 2** | **2 Mobs** | **1 Free Order** |
| **Level 3** | **2 Mobs** | **2 Free Orders** |
| **Level 4** | **3 Mobs** | **2 Free Orders** |
| **Level 5** | **3 Mobs** | **3 Free Orders** |

*   **Max Controlled Mobs**: The maximum number of distinct allied **Mobs** you can maintain under your command simultaneously during an encounter.
*   **Free Orders per Round**: The number of Mob command actions you can issue each round without spending your Boss's **Standard Actions** (see [Action Economy & Turn Flow](03_Action_Economy_and_Turn_Flow.md)).

### Brains Derived Stats: Power Words & Crafting Capacity

| Brains Level | Power Words (Spell Tag Slots) | Crafting Capacity (Oddity Slots) |
| :---: | :---: | :---: |
| **Level 1** | **0 Slots** | **1 Oddity Slot** |
| **Level 2** | **0 Slots** | **2 Oddity Slots** |
| **Level 3** | **2 Slots** | **3 Oddity Slots** |
| **Level 4** | **4 Slots** | **4 Oddity Slots** |
| **Level 5** | **6 Slots** | **5 Oddity Slots** |

*   **Power Words**: The maximum number of volatile magical element and delivery tags your Boss can commit to memory for casting spells (see [Magic & Bangaranga](08_Magic_and_Bangaranga.md)). You must have at least **Brains 3** to memorize Power Words and cast spells.
*   **Crafting Capacity**: The maximum number of specialized **Oddities** (custom mechanical attachments, alchemical coatings, spikes, and contraptions) you can install onto a single crafted item during downtime (see [The Lair Loop and Progression](10_The_Lair_Loop_and_Progression.md)).

---

## Grunt & Command Limits

**Grunt** represents personal authority, intimidation, and psychological command momentum. It determines how large a **Mob** you can intimidate into following orders, and acts as the currency for activating high-tier **Quirks**.

### Calculating Maximum Grunt
A Boss's **Maximum Grunt** is strictly equal to the Boss's **second-highest Main Stat**:

$$\text{Max Grunt} = \text{SecondHighest}(\text{Tough}, \text{Slink}, \text{Brains}, \text{Mouth})$$

> **Example Calculations:**
> *   Stats: **Tough 3**, **Slink 1**, **Brains 1**, **Mouth 1** $\implies$ Second-highest is 1 $\implies$ **Max Grunt = 1**.
> *   Stats: **Tough 2**, **Slink 2**, **Brains 1**, **Mouth 1** $\implies$ Second-highest is 2 $\implies$ **Max Grunt = 2**.
> *   Stats: **Tough 4**, **Slink 3**, **Brains 2**, **Mouth 1** $\implies$ Second-highest is 3 $\implies$ **Max Grunt = 3**.

### Tracking Current Grunt
Unlike the four static Main Stats, **Current Grunt** fluctuates dynamically between **0** and **Max Grunt** during a raid:

*   **Gaining Grunt (+1)**:
    *   Achieving a double-explosion **Critical Success** on any test (+1 Grunt).
    *   Personally slaying an enemy in your current or an adjacent Zone (+1 Grunt).
    *   Successfully dealing damage via **Assert Dominance** (+1 Grunt).
*   **Losing Grunt (-1)**:
    *   Suffering a **Fumble** on any test or failed **Gobbo Gamble** (-1 Grunt).
    *   Failing any test that included drawn **Bangaranga Dice** (-1 Grunt).
    *   Failing to deal damage when attempting **Assert Dominance** (-1 Grunt).

### Mob Command Limits & The Rebellion Test
A **Goblin Boss** can only maintain direct command over a **Mob** whose current **Size** is less than or equal to the Boss's **Current Grunt**:

$$\text{Maximum Commandable Mob Size} \le \text{Current Grunt}$$

*   **Rebellion Test**: If your current **Grunt** drops below the current **Size** of a Mob under your command (or if you attempt to command a Mob larger than your Grunt), you must immediately make a command test:
    $$\text{Tough or Mouth} \quad \text{5+/[Mob Size]}$$
    *   **Success**: The Mob remains intimidated and obeys your command for this round.
    *   **Failure**: The Mob realizes you are weak, breaks command, and immediately becomes **Out of Control** (see [Mob Mechanics](06_Mob_Mechanics.md)).

### Assert Dominance
When your Grunt is low and your Mobs are restless, you can beat your own followers to re-establish fear:
*   **Action Cost**: 1 **Standard Action**.
*   **Execution**: Make an undefended melee attack against a friendly **Mob** under your command in your Zone.
*   **Outcome**:
    *   If the attack deals **$\ge 1$ damage** to the Mob's health dice, your Boss immediately regains **+1 Grunt** (up to Max Grunt).
    *   If the attack rolls **0 successes** (dealing 0 damage), the attack bounces, your goblins laugh at you, and your Boss loses **-1 Grunt**.

---

## Boss Creation Engine

Follow these sequential steps to create a starting **Goblin Boss**:

```
[Step 1: Base Stats (All 1s)]
             |
             v
[Step 2: Allocate 2 Points] ---> Specialist (3/1/1/1) vs Generalist (2/2/1/1)
             |
             v
[Step 3: Derive Secondary Stats & Role]
             |
             v
[Step 4: Choose 1 Starting Basic Quirk (Tier <= Stat Level)]
             |
             v
[Step 5: Select Junk (T1) Loadout]
```

### Step 1: Set Base Stats
Set all four **Main Stats** to **1**:
*   **Tough**: 1
*   **Slink**: 1
*   **Mouth**: 1
*   **Brains**: 1

### Step 2: Distribute Starting Points
You have **2 points** to distribute among your four Main Stats. At character creation, no stat can be increased above **Level 3**.

Choose one of two core archetype distributions:
1.  **Specialist (3, 1, 1, 1)**: Invest both points into one primary stat.
    *   *Result*: Primary Stat = 3, remaining stats = 1.
    *   *Derived Grunt*: **Max Grunt = 1**. (Can command a **Size 1 Mob** at campaign start).
2.  **Generalist (2, 2, 1, 1)**: Invest one point into two different stats.
    *   *Result*: Two Stats at 2, two stats at 1.
    *   *Derived Grunt*: **Max Grunt = 2**. (Can command a **Size 2 Mob** at campaign start).

### Step 3: Derive Secondary Stats & Role
Consult the progression tables above to record your **Grit**, **Carry Capacity**, **Movement**, **Passive Defence**, **Max Mobs**, **Free Orders**, **Power Words**, and **Crafting Capacity**.

Your highest stat and second-highest stat define your starting **Role** (e.g. Tough Specialist = Meat-Wall; Tough/Slink Hybrid = Raider; Slink/Brains Hybrid = Saboteur; Slink/Mouth Hybrid = Ring-Leader; Mouth/Brains Hybrid = Chant-Monger; Brains Specialist = Sage-Tinker).

### Step 4: Choose 1 Starting Basic Quirk
Select **1 Basic Quirk** matching a stat where your Boss's stat level meets or exceeds the Quirk's Tier (starts with 0 Twists).

### Step 5: Select Starting Loadout
Choose starting gear of **Junk (T1)** quality from the scrap pile:
1.  **Melee Weapon (Choose 1)**:
    *   *Light Melee Weapon* (Bulk 1, One-Handed, Impact Size 1).
    *   *Medium Melee Weapon* (Bulk 2, One-Handed, Impact Size 1).
    *   *Heavy Melee Weapon* (Bulk 3, Two-Handed, Impact Size +1).
2.  **Ranged Weapon (Optional, Choose 1)**:
    *   *Sling* (Bulk 1, One-Handed, Range 1 Zone).
    *   *Shortbow* (Bulk 2, Two-Handed, Range 2 Zones).
    *   *Throwing Daggers* (Bulk 1, One-Handed, Range 1 Zone).
3.  **Defense (Optional, Choose 1)**:
    *   *Light Armor* (Bulk 1, +1d Passive Armor Die).
    *   *Shield* (Bulk 1, One-Handed, +1d Passive Armor Die, enables Tough Parry).

[MISSING RULE / GAP: Weapon Damage Metric & Loadout Notation Discrepancy — Legacy character creation drafts incorrectly listed starting weapons with "+2d damage / +3d damage" dice bloat. In the standardized rules engine, all weapon attacks roll the Boss's Tough (melee) or Slink (ranged) dice pool against the target's Defence TN, dealing flat 1 damage or 1 Wound per success threshold. Weapon category dictates Hands, Bulk, Range, and Impact Size (+1 Heavy, +2 Crushing).]

[MISSING RULE / GAP: Dual-Wielding Melee Weapons — Character creation references wielding two Light Melee weapons simultaneously, but requires formal resolution. Suggested Resolution: Wielding an off-hand Light Melee weapon grants a passive Boon 1 (+1d) to melee attack pools or allows splitting scored successes between two distinct targets in the same Zone.]

---

## The Gang as Class Archetype

In **Gobbos**, players do not play isolated lone heroes. The player's persistent, leveling entity is the **Gang**, which survives the death or retirement of individual Bosses.

```
+-----------------------------------------------------------------------------+
|                                 THE GANG                                    |
|   Persistent Entity  •  Infamy Track (1-5)  •  The Hoard  •  The Bone Pile  |
+-----------------------------------------------------------------------------+
```

### 1. Infamy Track (Level 1 to 5)
**Infamy** represents how feared, respected, and notorious your Gang is across the Lair. It acts as the Gang's overall level, scaling from **Infamy 1** to **Infamy 5**.

#### Earning Infamy Marks
A Gang advances its Infamy by earning **Infamy Marks**:
1.  **Loot Contribution**: Every **10 Loot Value** brought back from raids and deposited into the Lair Hoard grants **1 Infamy Mark**.
2.  **Gang Agendas**: Completing a chosen **Gang Agenda** during a raid grants **1 Infamy Mark** (maximum 1 Mark from Agendas per raid).

#### Infamy Milestones & Scaling
| Infamy Level | Cumulative Marks Required | Successor Starting XP | Max Equipped Gang Quirks |
| :---: | :---: | :---: | :---: |
| **Infamy 1** | **0 Marks** | **4 XP** | **1 Gang Quirk** |
| **Infamy 2** | **3 Marks** | **8 XP** | **2 Gang Quirks** |
| **Infamy 3** | **6 Marks** | **12 XP** | **3 Gang Quirks** |
| **Infamy 4** | **10 Marks** | **16 XP** | **4 Gang Quirks** |
| **Infamy 5** | **15 Marks** | **20 XP** | **5 Gang Quirks** |

### 2. Successor Boss Generation (Roguelite Legacy)
When a **Goblin Boss** dies, the Gang promotes the next biggest goblin to take command:
1.  **Base Setup**: The successor begins with base **1** in all four Main Stats, plus the standard **2 starting points**.
2.  **Successor XP**: The successor receives a bonus pool of **Successor XP** equal to $\text{Infamy Level} \times 4$ to purchase additional stat upgrades at standard advancement costs.
3.  **Successor Stat Cap**: A newly generated successor cannot raise any stat above **Level 4** at creation.
4.  **The Gang Mark**: The successor receives a permanent tattoo inked in soot and blood, inheriting **1 Quirk or Twist** possessed by the deceased Boss, completely bypassing stat tier prerequisites.

### 3. The Gang Hoard
**The Hoard** is the Gang's central stockpile of unrefined scrap, stolen tools, spare weapons, and trade wealth stored in the Lair. 
*   Before embarking on a raid, the Gang draws from the Hoard to outfit recruited **Mobs** with weapons, armor, and utility consumables.
*   Loot brought back from raids that is not contributed to Lair infrastructure is melted down into the Hoard (see [The Raid Loop](09_The_Raid_Loop.md)).

### 4. The Bone Pile & Relics
The **Bone Pile** is a literal monument of skulls and bones belonging to the Gang's deceased former Bosses.
*   **Forging Relics**: When a Boss dies, the Gang can recover a bone or token and attach it to a weapon or armor piece to forge a **Relic**.
*   **Relic Boon**: The Relic grants a mechanical Boon (+1d) tied to the deceased Boss's highest Main Stat. A Boss may equip at most **1 Relic** at a time.

### 5. Elders & Retirement
When any **Goblin Boss** reaches **Level 6** in any Main Stat, that Boss automatically retires from active raiding to become an **Elder**. Elders are permanently staffed at Lair facilities to grant persistent bonuses:
*   **Elder of Tough (Training Ring)**: All Mobs commanded by the Gang gain **+1 Passive Armor Die** without consuming Bulk.
*   **Elder of Slink (Shadow Den)**: Reduces the Target Number (**TN**) of all environmental traps by **1** (minimum TN 1).
*   **Elder of Mouth (Council Chambers)**: Increases the Boss's Maximum **Grunt** by **+1**; once per raid, allows rallying all fleeing Mobs in the zone as a Free Action.
*   **Elder of Brains (Tinker Yard)**: Allows installing **+1 extra Oddity** onto crafted custom gear beyond standard Crafting Capacity.

### 6. Gang Shenanigan (Cultural Identity)
Every Gang possesses a defining cultural trait called a **Shenanigan** (e.g. *Pyromaniacs, Shiny-Snatchers, Trap-Trippers, Skull-Bangers*):
*   **The Boon**: Grants a **+1d Boon** on action tests directly aligned with the Shenanigan.
*   **The Compulsion**: When presented with an opportunity to indulge the Shenanigan, the Boss must make a `Brains 5+/1` test to resist.
*   **Feeding the Bangaranga**: Whenever a player willingly indulges your Shenanigan to the tactical detriment of the party, immediately add **+1d6** to the communal **Bangaranga Pool**.

---

## Quirk Structural Schema

Quirks are modular personal abilities that modify dice outcomes, manipulate conditions, or alter the action economy. Every Quirk must conform to the following formal schema:

```markdown
### [CONTENT INSTANCE: Boss Quirk]
**Name**: <Quirk Name>
**Category**: <Tough | Slink | Brains | Mouth | General | Gang Legacy>
**Tier**: <T1 | T2 | T3 | T4 | T5>
**Prerequisite**: <Stat Name> Level >= Tier
**Cost**: <Passive | 1 Grunt | 1 Standard Action | 1 Reaction | 1 Free Order>
**Trigger**: <Passive | On Hit | On Dodge | On Fumble | Start of Turn | Action Declaration>
**Target Hub**: <Self | Allied Mob | Enemy in Zone | Zone Environment>
**Mechanical Effect**: <Direct Tier A rule specifying dice modification, condition, or action bypass>
**Twist Slots**: <1 Twist Max | 0 Twists>
**Keywords**: <[Keywords from Master Index]>
```

### [CONTENT EXTENSION POINT: Boss Quirks & Talents]
*All specific Boss Quirks, talent trees, and Twist modifiers are maintained in the modular Quirks Compendium and attach directly to the core rules via the schema above.*
