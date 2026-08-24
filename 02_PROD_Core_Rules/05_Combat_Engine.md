# Combat Engine

*Combat in Gobbos is fast, visceral, and uncompromisingly deterministic. The Game Master never rolls dice to strike or calculate damage; instead, enemies present lethal Threat profiles that goblin Bosses evade through acrobatic dodges, desperate shield parries, or the noisy protection of clattering scrap-iron armor.*

---

## The Attack Pipeline

All attacks in **Gobbos**—whether delivered via a rusty cleaver, a scavenged crossbow, or an explosive pot—follow a unified, single-source resolution pipeline.

```
[Declare Attack] ===> [Assemble Dice Pool] ===> [Roll vs Target Defence TN]
                                                        ||
                        +-------------------------------+-------------------------------+
                        |                               |                               |
                        v                               v                               v
             [Successes >= Defence TN]       [1 <= Successes < Defence]       [0 Successes Scored]
                        |                               |                               |
                        v                               v                               v
               [FULL HIT / OVERKILL]            [STAGGER EVALUATION]            [BOUNCE / MISS]
          - Minion: One-Hit Kill             - Impact Size >= Target Size:     - Strike glances off
          - Elite: Wound = Floor(Succ/TN)       Target is Staggered             harmlessly
          - Mob: Frontline / Decrement       - Impact Size < Target Size:
                                                Mass Resistance (No Stagger)
```

---

## Melee Attacks

A **Melee Attack** represents close-quarters combat against a target occupying the same **Zone**.

### Execution & Dice Pool
*   **Action Cost:** Costs one **Standard Action** during the **Player Active Turn**.
*   **Base Pool:** The attacking Goblin Boss rolls a dice pool equal to their **Tough** stat:
    $$\text{Melee Attack Pool} = \text{Tough} + \text{Boons (+1d)} - \text{Banes (-1d)} + \text{Bangaranga Dice}$$
*   **Target Number (TN):** The attack resolves against the target's static **Defence TN** (typically 1 to 4).

### Resolving Melee Outcomes
1.  **Standard Enemy (Minion):** If accumulated successes meet or exceed the target's **Defence TN** (Successes $\ge$ Defence TN), the minion is instantly defeated and removed from play (**One-Hit Kill**).
2.  **Elite / Boss Enemy (The Overkill Rule):** If successes meet or exceed the target's **Defence TN**, the strike inflicts **1 Wound for every full multiple of the Defence TN** scored on the single roll:
    $$\text{Wounds Dealt} = \left\lfloor \frac{\text{Attack Successes}}{\text{Target Defence TN}} \right\rfloor$$
    *(Example: Against an Elite with Defence 2, rolling 2 or 3 successes deals 1 Wound; rolling 4 or 5 successes deals 2 Wounds; rolling 6 successes deals 3 Wounds).*
3.  **Enemy Mob (Single-Target Melee):** If successes meet or exceed the Mob's **Defence TN**, the strike reduces the face value of the Mob's lowest active health die by the weapon's damage (default 1). If reduced below 1, the die is removed and excess damage spills over into the next lowest die.
4.  **Enemy Mob (Mob-on-Mob Clash):** When a player Mob attacks an enemy Mob, combat resolves via the **Frontline Rule** (see [Mob Mechanics](06_Mob_Mechanics.md)).
5.  **Partial Hit (Stagger):** If the roll yields at least **one (1) success** but fewer than the target's **Defence TN**, the strike deals 0 damage, but triggers an **Impact Size vs. Target Size** comparison to determine if the target is **Staggered**.
6.  **Bounce (Miss):** If the roll yields **zero (0) successes**, the attack bounces harmlessly off the target's armor or parry.

---

## Ranged Attacks

A **Ranged Attack** represents firing projectiles (stones, arrows, bolts, or thrown blades) across one or more **Zones**.

### Execution & Dice Pool
*   **Action Cost:** Costs one **Standard Action** during the **Player Active Turn**.
*   **Base Pool:** The attacking Goblin Boss rolls a dice pool equal to their **Slink** stat:
    $$\text{Ranged Attack Pool} = \text{Slink} + \text{Boons (+1d)} - \text{Banes (-1d)} + \text{Bangaranga Dice}$$
*   **Target Number (TN):** Resolves against the target's static **Defence TN**.

### Range in Zones
Ranged weapons measure distance strictly in discrete Zone steps:
*   **1 Zone Range (Close):** Slings, thrown daggers, firepots. Targets creatures in the same Zone or 1 adjacent connected Zone.
*   **2 Zones Range (Standard):** Shortbows, standard crossbows. Targets creatures up to 2 connected Zones away.
*   **3 Zones Range (Long / Heavy):** Heavy arbalests, sniper slings. Targets creatures up to 3 connected Zones away.

### Ranged Environmental Penalties & Cover
*   **Partial Cover:** Targeting a creature behind Partial Cover imposes a **Bane 1 (-1d)** penalty on the attack pool.
*   **Full Cover:** Line of sight is completely blocked; the creature cannot be targeted.
*   **Environmental Obstacles:** Firing through Zones with the `Howling Wind` (`[Gale]`) trait or dense smoke screens (`[Gaseous]`) imposes a **Bane 1 (-1d)** penalty.

---

## Impact Size & Stagger Resolution

When an attack scores at least **one (1) success** but falls short of the target's **Defence TN**, the blow lands with insufficient precision to pierce armor or flesh, but carries physical momentum.

```
[Partial Hit: Successes >= 1 and < Defence TN]
                    ||
                    \/
   [Calculate Attack Impact Size]  vs.  [Target Physical Size]
                    ||
    +---------------+---------------+
    |                               |
    v                               v
[Impact Size >= Target Size]     [Impact Size < Target Size]
Target gains STAGGERED condition   Target has MASS RESISTANCE
(Defence TN -1 until Round End)    (Stagger is completely ignored)
```

### Calculating Impact Size
$$\text{Impact Size} = \text{Attacker Base Size} + \text{Weapon Trait Modifiers}$$

*   **Attacker Base Size:** A Goblin Boss is **Size 1**. A Mob has a base size equal to its current **Mob Size** (1 to 5).
*   **`Heavy` Weapon Trait:** Grants **+1 Impact Size** (e.g. a Size 1 Boss wielding a heavy two-handed maul strikes with **Impact Size 2**).
*   **`Crushing` Weapon Trait:** Grants **+2 Impact Size** (e.g. a Size 1 Boss swinging a wrecking flail strikes with **Impact Size 3**).
*   **Explosives & Spells:** Explosive blast devices and magic attacks possess an Impact Size equal to their **Tier** (Tier 1 = Impact Size 1, Tier 2 = Impact Size 2, Tier 3 = Impact Size 3, Tier 4 = Impact Size 4, Tier 5 = Impact Size 5).

### Stagger Evaluation & Mass Resistance
*   **Stagger Applied ($\text{Impact Size} \ge \text{Target Size}$):** If the attack's Impact Size equals or exceeds the target's physical **Size**, the target is thrown violently off balance and gains the **Staggered** condition until the **Round Closure Phase**.
*   **Mass Resistance ($\text{Impact Size} < \text{Target Size}$):** If the attack's Impact Size is strictly less than the target's physical **Size**, the giant foe absorbs the blow without budging. The target completely ignores the Stagger effect.

>> **THE STAGGERED CONDITION:**
>> A **Staggered** enemy or Boss suffers reduced combat effectiveness:
>> *   **Enemies & Bosses:** Static **Defence TN** is reduced by **1** (to a minimum of 1).
>> *   **Goblin Bosses & PCs:** Suffer a **Bane 1 (-1d)** penalty on active **Dodge** and **Parry** rolls.
>> *   **All Staggered conditions automatically clear on all combatants at the end of each round during the Round Closure Phase.**

---

## Weapon Mechanics & Traits

Weapons provide tactical reach, modify Impact Size, and grant specialized combat properties.

### Structural Properties
*   **Handedness:** One-Handed (**1H**) weapons allow holding a Shield, torch, or Loot item in the off-hand. Two-Handed (**2H**) weapons require both hands to attack and prevent holding off-hand gear.
*   **Bulk Footprint:** Light weapons occupy **Bulk 1**; Medium weapons occupy **Bulk 2**; Heavy weapons occupy **Bulk 3**. Improvised weapons occupy **Bulk 0**.
*   **Quality & Durability:** Weapons belong to a Quality Tier (T1 Junk, T2 Scrappy, T3 Standard, T4 Superior, T5 Legendary). When a player **Fumbles** a test using a weapon, they roll a 1d6 **Break Roll**:
    *   *T1 Junk:* Breaks on a roll of **1–4**.
    *   *T2 Scrappy:* Breaks on a roll of **1–3**.
    *   *T3 Standard:* Breaks on a roll of **1–2**.
    *   *T4 Superior:* Breaks on a roll of **1**.
    *   *T5 Legendary:* **Never breaks**.

### Standard Weapon Traits

| Trait | Category | Mechanical Function |
| :--- | :--- | :--- |
| `Heavy` | Offensive | Adds **+1 to Impact Size** when calculating Stagger. Requires two hands (**2H**). |
| `Crushing` | Offensive | Adds **+2 to Impact Size** when calculating Stagger. Requires two hands (**2H**). |
| `Cleave X` | Offensive | Sweeps across frontline ranks. Deals damage simultaneously to up to **X adjacent standard targets** or up to **X lowest active health dice** in an enemy Mob. |
| `Reach` | Tactical | Allows melee attacks against targets in an adjacent connected Zone without moving into that Zone. |
| `Concealable` | Utility | Compact profile (**Bulk 1**). Can be drawn or stowed as an incidental **Free Action** once per turn. |
| `Versatile` | Tactical | Balanced one-handed profile (**1H**). Can be swung with two hands to gain **+1 Impact Size**. |
| `Piercing` | Tactical | Precision point. Effective against armored foes; suffers **Bane 1 (-1d)** against skeletal Undead. |
| `Bashing` | Tactical | Blunt impact. Grants **Boon 1 (+1d)** to Melee Attack pools against brittle or skeletal Undead. |

---

## Formal Weapon Structural Schema

[CONTENT EXTENSION POINT: Weapons]

All weapon instances, armory catalogues, and custom forge chassis must adhere strictly to this standardized schema:

```markdown
### [Weapon Name]
*   **Category:** [Melee | Ranged | Improvised]
*   **Quality Tier:** [T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary]
*   **Hands Required:** [1H | 2H]
*   **Bulk:** [Integer 0 to 3+]
*   **Range:** [Current Zone (Melee) | 1 Zone | 2 Zones | 3 Zones]
*   **Base Impact Size:** [Wielder Size | Wielder Size + 1 | Wielder Size + 2]
*   **Attack Stat Profile:** [`Tough` (Melee) | `Slink` (Ranged)] vs Target Defence TN
*   **Break Roll Threshold:** [Breaks on 1–4 | Breaks on 1–3 | Breaks on 1–2 | Breaks on 1 | Never breaks]
*   **Built-in Traits:** [`Heavy`, `Crushing`, `Cleave X`, `Reach`, `Concealable`, `Versatile`, `Piercing`, `Bashing`]
*   **Elemental / Material Tags:** [Optional bracketed tags, e.g. `[Fire]`, `[Spiked]`, `[Silvered]`]
*   **Special Mechanical Capabilities:** [Direct Tier A rules permissions or situational boons]
```

---

## Armor & Shields Mechanics

Armor and shields provide passive protection, absorb incoming blows, and enable active parrying reactions.

### Passive Armor Dice
Worn armor provides bonus colored dice (the **Armor Dice pool**) that are thrown alongside active defense dice during a **Clatter Roll**:
*   **Light Armor (Bulk 1 | 0 Bane):** Grants **+1d Armor Die**. Flexible and quiet; imposes zero mobility or stealth penalties.
*   **Medium Armor (Bulk 2 | Bane 1):** Grants **+2d Armor Dice**. Stiff leather or mail; imposes **Bane 1 (-1d)** on all **Slink** tests.
*   **Heavy Armor (Bulk 3 | Bane 2):** Grants **+3d Armor Dice**. Rigid plate; imposes **Bane 2 (-2d)** on all **Slink** tests, and the wearer **cannot swim** (sinks instantly in Deep Water).

### Shield Mechanics
*   **Armor Bonus:** Equipping a Shield (**Bulk 1 | 1H**) grants **+1d Armor Die** to your passive mitigation pool.
*   **Enables Parry Reaction:** Wielding an active Shield unlocks the ability to declare a **Parry** reaction using your **Tough** stat instead of being limited to a Slink Dodge.

### Passive Mitigation Ceiling
>> **THE 5D MITIGATION CEILING:**
>> The total passive mitigation pool rolled on any single Clatter Roll (combining Armor Dice, Shield bonus dice, and Slink Passive Defence dice) is hard-capped at **5d6 Armor Dice** to prevent absolute invulnerability.

### Ablative Gear Sacrifice Rule
When a Goblin Boss suffers an incoming strike with enough unmitigated damage to reduce their **Grit to 0** (or cause immediate death), the Boss may declare an immediate **Gear Sacrifice**:
*   **The Shatter:** The Boss permanently destroys one equipped Shield or suit of Armor on the spot, reducing the item to worthless, unrepairable scrap.
*   **The Salvation:** The sacrifice completely absorbs the lethal impact, reducing the incoming strike's damage to **0**.
*   *(Note: This rule applies strictly to PC Goblin Bosses; Mobs do not track individual ablative gear).*

---

## Formal Armor & Shield Structural Schema

[CONTENT EXTENSION POINT: Armor & Shields]

All protective gear instances and shields must adhere strictly to this schema:

```markdown
### [Armor / Shield Name]
*   **Category:** [Light Armor | Medium Armor | Heavy Armor | Shield | Heavy Pavise]
*   **Quality Tier:** [T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary]
*   **Slot / Hands:** [Worn (Body) | 1H (Held)]
*   **Bulk:** [Integer 1 to 3] (For Mobs: Bulk Rating x Mob Size)
*   **Passive Armor Dice:** [+1d | +2d | +3d]
*   **Mobility Penalties:** [None | Bane 1 (-1d) on Slink | Bane 2 (-2d) on Slink, Cannot Swim]
*   **Break Roll Threshold:** [Breaks on 1–4 | Breaks on 1–3 | Breaks on 1–2 | Breaks on 1 | Never breaks]
*   **Special Mechanical Properties:** [e.g. Enables Tough Parry reaction, Ablative Sacrifice eligible]
*   **Elemental / Material Tags:** [Optional bracketed tags, e.g. `[Reinforced]`, `[Spiked]`, `[Insulated]`]
```

---

## Gear, Tools & Consumables Mechanics

Expedition tools, alchemical explosives, and utility gear provide non-combat problem solving and area threat projection.

### Design Mandate: Difficulty & Permissions
Tools never grant "+1 flat math modifiers" to die faces. Instead, tools operate through three clear mechanisms:
1.  **Narrative Permission:** Enables a task that is otherwise physically impossible (e.g. a 30 ft rope allows climbing sheer cliffs).
2.  **Difficulty Step Shift:** Reduces test Difficulty (e.g. Quality Lockpicks shift lockpicking from **Hard (6)** to **Normal (5+)**).
3.  **Dice Boons:** Adds physical dice to the test pool (**Boon 1 (+1d)**).

### Consumables & Explosive Area Threat Profiles
Explosives (grenades, molotovs, powder kegs) do not roll single-target attack pools. When thrown or detonated, they project an **Area Threat Profile** across their target Zone:
$$\text{Area Threat Profile} = \text{Threat } [Difficulty]+/ [TN], \text{ [Damage]}, \text{ } [Tags], \text{ Blast Range: } X \text{ Zones}, \text{ Impact Size: } Y$$

*   **PC Bosses in Blast Zone:** Must resolve an immediate **Clatter Roll** (Dodge vs Threat TN) or suffer full blast damage to Grit.
*   **Mobs in Blast Zone:** May execute an active **Scatter** reaction or suffer blast damage applied simultaneously to all health dice.
*   **Standard Minions in Blast Zone:** Instantly destroyed if the explosive's Threat TN $\ge$ Minion Defence TN.
*   **Elite Enemies in Blast Zone:** Take 1 Wound if Threat TN $\ge$ Defence TN, and gain **Staggered** if blast Impact Size $\ge$ Enemy Size.

---

## Formal Gear, Tools & Consumables Schema

[CONTENT EXTENSION POINT: Gear, Tools & Consumables]

All adventuring gear, tools, and consumables must adhere strictly to this schema:

```markdown
### [Item Name]
*   **Category:** [Adventuring Tool | Utility Gear | Consumable / Explosive | Loot Plunder]
*   **Quality Tier:** [T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary]
*   **Bulk:** [Integer 0 to 4+]
*   **Usage Lifespan:** [Permanent | Single-Use Expended | 1 Exploration Phase]
*   **Break Roll Threshold:** [Breaks on 1–4 | Breaks on 1–3 | Breaks on 1–2 | Breaks on 1 | Never breaks]
*   **Mechanical Function:** [Permission rule, Difficulty step shift, or Boon (+1d)]
*   **Area Threat Profile** *(Consumables only)*: `Threat [Face]+/[TN]`, [Damage], `[Tags]`, Blast Range: [X Zones], Impact Size: [Tier 1–5]
*   **Loot Value** *(Plunder only)*: [Tier 1–5 Value tokens]
```

---

## The Clatter Defense Roll

The **Clatter Roll** is the core defensive mechanic in **Gobbos**. When an enemy strikes during the **Enemy Active Turn**, the GM announces the attack's **Threat Profile** (`Threat [Face]+/[TN]`) and flat **Damage**. The defending Goblin Boss resolves defense in a single simultaneous throw.

```
[Incoming Threat: Threat 5+/1, Damage 3]
                   ||
                   \/
   [Simultaneous Throw: The Clatter Roll]
   - Active Stat Dice: 2d Slink (Dodge) [Saved Action Spent]
   - Passive Armor Dice: 2d Armor (Medium Armor)
                   ||
                   \/
  [Step 1: Check Active Stat Dice vs Threat TN]
   - Slink scores >= 1 success? ======> CLEAN DODGE (0 Damage Taken)
   - Slink scores 0 successes?  ======> EVASION FAILS (Proceed to Step 2)
                   ||
                   \/
  [Step 2: Check Passive Armor Dice]
   - Each 5+ on Armor Dice reduces Damage by 1.
   - Example: 1 Armor success reduces Damage from 3 to 2.
                   ||
                   \/
  [Step 3: Deduct Remaining Damage from Grit]
   - Boss takes 2 Damage to Grit.
```

### Step-by-Step Clatter Roll Procedure

1.  **Saved Action Declaration:** To roll active **Stat Dice**, the Boss must spend one saved **Standard Action** (declaring a **Dodge** using `Slink`, or a **Parry** using `Tough` if equipped with a Shield).
    *   *Zero Saved Actions:* If the Boss spent all 3 actions on their active turn, they cannot roll Stat Dice and must rely entirely on passive Armor Dice.
2.  **Simultaneous Throw:** The player rolls their active Stat Dice alongside their distinct colored **Armor Dice** (plus any Slink Passive Defence dice) in a single roll.
3.  **Evaluating Active Evasion:**
    *   If successes on active **Stat Dice** meet or exceed the incoming **Threat TN**, the Boss achieves a **Clean Dodge/Parry**: **0 Damage is taken**.
4.  **Evaluating Armor Mitigation:**
    *   If active Stat Dice fall short of the Threat TN (or if 0 saved actions were available), the attack hits.
    *   Every success (**5+**) rolled on the **Armor Dice** reduces incoming Damage by **1**.
5.  **Grit Decrement:** Any remaining unmitigated damage is deducted directly from the Boss's **Grit** (see [Damage, Grit & Wounds](07_Damage_Grit_and_Wounds.md)).

---

## Group Attacks & Flanking

To prevent table slowdown and avoid draining all player reaction actions against large swarms of lesser foes, the GM uses **Group Attacks**.

### Group Attack (Enemy Swarm) Rules
When multiple standard minions gang up on a single Goblin Boss:
*   **Consolidated Attack:** The GM combines up to **3 standard enemies** into a single incoming strike.
*   **Damage Scaling:** The attack uses the primary enemy's Threat profile, and deals:
    $$\text{Group Damage} = \text{Base Enemy Damage} + (1 \text{ Damage per additional enemy})$$
*   **Single Defense Resolution:** The defending Boss spends only **one (1) saved Standard Action** to resolve a single Clatter Roll against the entire combined swarm attack.
*   **Targeting Cap:** A maximum of 3 standard enemies may combine against a single PC Boss. (Attacks against player Mobs have no grouping cap).

### Flanking & Crossfire Boons
*   **Flanking in Melee:** If two allied Bosses (or a Boss and an allied Mob) engage the same enemy from different approach vectors or surround a foe within a Zone, both attackers gain a **Boon 1 (+1d)** on their Melee Attack rolls.
*   **Crossfire in Ranged:** If ranged attackers target an enemy from two separate connected Zones, ranged attacks against that target gain a **Boon 1 (+1d)**.

---

## Mechanical Gap Analysis & Missing Rules

[MISSING RULE / GAP: Dual-Wielding Light Melee Weapons — Character creation permits equipping two Light Melee weapons, but the core combat rules lack an explicit mechanical rule for dual-wielding. Suggested Resolution: Wielding a secondary off-hand Light Melee weapon grants either a passive Boon 1 (+1d) to Melee Attack pools or allows splitting successes across two distinct adjacent targets in the same Zone on a single Attack action.]

[MISSING RULE / GAP: Ranged Weapon Ammunition Tracking and Depletion — Rules specify slings use scavenged stones, but bows and crossbows lack explicit ammunition management. Suggested Resolution: Standardize that a mundane Quiver/Bolt Case occupies Bulk 1 (providing sufficient ammunition for an entire raid). Fumbling a ranged attack roll with a bow or crossbow expends or breaks the active ammunition supply, requiring a Manipulate action in a Junk Pile or spending 1 Scrap to restock.]
