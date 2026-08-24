# Gobbos Core Rules Specification & Mechanics Mining Report
**Domain Focus**: Core Resolution (1), Attributes & Boss/Gang (2), Action Economy & Turn Flow (3), Zones & Environment (4), Combat Engine (5).
**Miner**: Spec Miner Core 0 (`.agents/spec_miner_core_0/`)
**Date**: 2026-08-24
**Integrity Mode**: Systemic Mechanics Extraction & Content Separation

---

## 1. Executive Summary & Architecture Overview

This report provides the authoritative specification mining analysis for Domains 1 through 5 of the Gobbos TTRPG rules engine. In strict accordance with `GEMINI.md` and the Core Rules Synthesis objectives:
- **Pure Rules Engine Isolation**: All systemic loops, dice mathematics, attribute structures, action pipelines, spatial topology rules, and combat resolutions are extracted and codified.
- **Living Content Separation**: Catalog entries, monster statblocks, exhaustive weapon compendiums, and quirk listings have been decoupled from the rules engine and converted into rigorous, extensible Markdown Schemas.
- **Single-Source Rule Consistency**: Rules defined across stage drafts and production fragments have been unified into definitive, non-conflicting formulas.
- **Mechanical Gap Catalog**: Every ambiguity, missing subsystem, or conflicting notation across the source materials has been flagged with an actionable `[MISSING RULE / GAP]` tag and recommended resolution.

---

## 2. Systemic Mechanics Extraction by Domain

### Domain 1: Core Resolution & Dice Pool Engine

#### 1.1 The D6 Pool Framework
- **Exclusivity**: Gobbos uses standard six-sided dice (**d6**) exclusively.
- **Player-Facing Resolution**: Players roll all dice. The Game Master (GM) never rolls dice for standard tests, attacks, evasion, or hazard checks.
- **Pool Assembly**: A test pool is constructed from:
  $$\text{Dice Pool} = \text{Base Stat / Mob Size} + \text{Boons (+1d, +2d)} - \text{Banes (-1d, -2d)} + \text{Bangaranga Dice}$$
  - For a **Goblin Boss**: Base pool equals the relevant Main Stat (**Tough**, **Slink**, **Brains**, or **Mouth**).
  - For a **Mob**: Base pool equals the Mob's current **Size** (1 to 5) for Tough tests, or a flat **2d6** for Slink, Brains, and Mouth tests.
- **Boon & Bane Rule**: Modifiers add or subtract physical dice in integer increments. Multiple environmental Boons or Banes do not stack beyond a net cap of **+1d** or **-1d** (unless explicitly granted by distinct gear or quirk layers).

#### 1.2 Difficulty & Target Number (TN) Notation
- **Difficulty (Target Face)**: Governs which die faces count as a **Success**:
  - **Easy (4+)**: Die faces **4, 5, 6** are successes.
  - **Normal (5+)**: Die faces **5, 6** are successes (system default).
  - **Hard (6)**: Only die face **6** is a success. *(Per style guide, never write `6+`).*
- **Target Number (TN)**: The total number of successes required to pass the test.
- **Standard Notation**: `[Stat] [Difficulty Face]+/[Required Successes]`
  - Narrative: *A Slink test on a 5 or higher needing 2 successes.*
  - Hybrid Rules: `Slink against the zone profile of 5+ (2 successes)`.
  - Shorthand / Statblock: `Slink 5+/2`, `Tough 4+/1`, `Brains 6/2`.

#### 1.3 Exploding 6s & Critical Successes
- **Exploding 6s**: Every natural **6** rolled is 1 success and immediately grants **+1 bonus d6** rolled into the pool. This explosion chains indefinitely on subsequent 6s.
- **Critical Success**: Occurs whenever a natural 6 explodes and the resulting bonus die also rolls a **6** (a consecutive double-six chain).
  - **Mechanical Reward**: The Boss immediately regains **1 Grunt** (up to maximum) AND gains an immediate bonus non-offensive **Free Action** (a Move, Plunder, or Manipulate action).

#### 1.4 Zero Dice Pools (The Salvage Roll)
- If penalties, conditions, or Banes reduce an active dice pool to **0d6 or fewer dice**, the test automatically fails by default.
- The player makes a desperate **1d6 Salvage Roll**:
  - **Roll 6**: Miraculous salvage; yields exactly **1 Success** (does not explode).
  - **Roll 1**: Catastrophic failure; immediately triggers a **Fumble** (-1 Grunt if Mobs are present in the zone or an adjacent zone).
  - **Roll 2–5**: Fails normally with no additional penalties.

#### 1.5 Gobbo Gamble (1s and Fumbles)
- When a test fails (accumulated successes < TN) but one or more dice show **1s**, the player may declare a **Gobbo Gamble** and reroll all **1s**.
  - **Blessing**: If the new roll brings total successes $\ge$ TN, the test succeeds normally.
  - **Fumble**: If the test still fails after rerolling 1s, the Boss suffers a **Fumble** and loses **1 Grunt**.
  - **Accepting Failure**: If the player chooses not to reroll 1s (or if the failed roll contained no 1s), the action fails normally with 0 Grunt loss.

#### 1.6 The Bangaranga Pool
- **Concept**: A shared communal pool of distinctly colored d6s (e.g. bright red) representing the accumulated noise, hype, and rowdiness of the horde.
- **Seeding at Raid Start**:
  $$\text{Starting Pool} = (1\text{d per Boss}) + (1\text{d per Size 3–4 Mob}) + (2\text{d per Size 5 Mob})$$
- **Hype Triggers (Adding Dice)**:
  - Any player rolls a **Critical Success**: **+1d6**
  - Any player suffers a **Fumble**: **+1d6**
  - Defeating an enemy with `[Notable]` or `[Big Threat]`: **+1d6**
  - Claiming a cache with `[Big Loot]` or `[Hoard]`: **+1d6**
  - Indulging a Gang **Shenanigan** compulsion: **+1d6**
  - Unsupervised Mob Mischief (rolling 1s on Chaos Tick): **+1d6 per 1**
- **Tapping the Pool & Bangaranga Tax**:
  - Before rolling any test, a Boss may draw Bangaranga dice up to their current **Grunt** stat.
  - **Bangaranga Tax**: If the number of Bangaranga dice taken is **strictly greater than the test's TN**, the player must pay a **1-die Tax** (1 extra die removed from the pool and discarded unrolled).
- **Double Explosion**: Every **6** rolled on a Bangaranga Die counts as 1 success and **explodes twice** (immediately rolls *two* additional standard dice).
- **Overreaching**:
  - Failing a test that used Bangaranga dice costs **1 Grunt**.
  - If the test fails and the final pool contains any **1s**, the hype is exhausted: remove a number of Bangaranga dice from the pool equal to the number of Bangaranga dice taken for the test.

---

### Domain 2: Attributes, Boss Profile & Gang Fundamentals

#### 2.1 Main & Secondary Attributes
Every Goblin Boss possesses four Main Stats (rated **Level 1 to Level 5**), which determine base dice pools and derived secondary metrics:

| Main Stat | Domain & Focus | Derived Secondary Stat 1 | Derived Secondary Stat 2 | Progression Values (Lv 1 $\rightarrow$ 5) |
| :--- | :--- | :--- | :--- | :--- |
| **Tough (T)** | Muscle, brute force, melee attack pool | **Grit** (Health capacity) | **Carry** (Max Bulk capacity) | **Grit**: 3, 4, 4, 5, 5<br>**Carry**: 6, 8, 10, 12, 14 |
| **Slink (S)** | Agility, stealth, ranged attack pool, dodge | **Movement** (Zones per Move action) | **Passive Defence** (Mitigation dice) | **Movement**: 2, 3, 3, 4, 5<br>**Passive Defence**: 0d, 0d, 1d, 1d, 2d |
| **Mouth (M)** | Leadership, shouting orders, mob control | **Max Mobs** (Simultaneous mobs) | **Free Orders** (Commands per round) | **Max Mobs**: 1, 2, 2, 3, 3<br>**Free Orders**: 1, 1, 2, 2, 3 |
| **Brains (B)** | Crafting, alchemy, magic words, awareness | **Power Words** (Spell tag memory) | **Crafting Capacity** (Oddity slots) | **Power Words**: 0, 0, 2, 4, 6<br>**Crafting Capacity**: 1, 2, 3, 4, 5 |

#### 2.2 Grunt & Command Limits
- **Definition**: Grunt represents authority, leadership pressure, and psychological momentum.
- **Maximum Grunt**: Equal to the Boss's **second-highest Main Stat**.
  $$\text{Max Grunt} = \text{SecondHighest}(\text{Tough}, \text{Slink}, \text{Brains}, \text{Mouth})$$
- **Current Grunt**: Fluctuates during a raid between 0 and Max Grunt.
  - **Gaining Grunt**: Critical success (+1), defeating an enemy in same/adjacent zone (+1), successful Assert Dominance (+1).
  - **Losing Grunt**: Test Fumble (-1), failed Bangaranga roll (-1), failed Assert Dominance (-1).
- **Command Limit**: A Boss can only maintain direct control over a Mob whose current **Size** $\le$ the Boss's current **Grunt**.
- **Rebellion Test**: If a Mob's Size exceeds current Grunt, the Boss must pass an immediate command test (**Tough** or **Mouth** against `5+/Size`). On a failure, the Mob breaks command and becomes **Out of Control**.
- **Assert Dominance**: A Boss may spend a Standard Action to make an undefended melee attack against their own controlled Mob. If damage is dealt, the Boss regains **+1 Grunt**. If 0 damage is dealt, the Boss loses **-1 Grunt**.

#### 2.3 Boss Creation Engine
1. **Base Stats**: Set all 4 Main Stats to **1**.
2. **Point Allocation**: Distribute **2 points** across Main Stats (maximum stat at creation is **3**).
   - **Specialist**: 3, 1, 1, 1 (Max Grunt = 1, Role Level = 3).
   - **Generalist**: 2, 2, 1, 1 (Max Grunt = 2, Role Level = 2).
3. **Derive Secondary Stats & Role**: Look up Grit, Carry, Movement, Passive Defence, Max Mobs, Free Orders, Power Words, Crafting Capacity. Determine Role from Primary vs Secondary stat.
4. **Choose 1 Starting Basic Quirk**: Must match a stat where Stat Level $\ge$ Quirk Tier (starts with 0 Twists).
5. **Select Starting Loadout**: Choose Junk (T1) equipment: 1 Melee weapon, 1 optional Ranged weapon, 1 optional Armor/Shield.

#### 2.4 Gang Archetype & Roguelite Legacy
- **The Gang as Class**: The player's persistent leveling entity is the **Gang**, which survives the death of individual Bosses.
- **Infamy Track (Level 1 to 5)**:
  - Advances via **Infamy Marks** earned by contributing Loot (1 Mark per 10 Loot Value) and completing **Gang Agendas** (1 Mark per raid).
  - Milestones: Lv 2 = 3 Marks, Lv 3 = 6 Marks, Lv 4 = 10 Marks, Lv 5 = 15 Marks.
- **Successor Boss Generation**:
  - When a Boss dies, the successor starts with base 1s, +2 starting points, and a pool of **Successor XP** equal to $\text{Infamy Level} \times 4$.
  - Successor Stat Cap: Maximum stat level 4 at creation.
  - **Gang Mark**: Successor inherits 1 permanent tattoo of any Quirk or Twist possessed by the deceased Boss, bypassing stat tier prerequisites.
- **Retirement & Elders**:
  - When any stat reaches **Level 6**, the Boss automatically retires to become an **Elder**, unlocking permanent Lair room upgrades.
- **Gang Shenanigan**: A cultural identity trait granting a **+1d Boon** on aligned tasks, a mandatory narrative compulsion, and a **+1 Bangaranga die** payout when indulged.

---

### Domain 3: Action Economy & Turn Flow

#### 3.1 Action Budgets & Categories
- **Goblin Boss Budget**:
  - **3 Standard Actions** per round (reset at round start).
  - **1 Free Order Action** per round (does not consume Standard Actions; scales with Mouth stat).
  - **Free Actions**: Minor maneuvers (dropping items, speaking, drawing 1 light item once/turn).
  - **Reactions**: Out-of-turn defensive or triggered responses (Dodge, Parry, Scatter, reactive Quirks). **Requires spending a saved Standard Action** (or an unused Free Order for Scatter).
- **Mob Budget**:
  - **2 Actions** per round (reset at round start).
  - Mobs only act when ordered or during unordered resolution.
- **The Boredom Rule**: Mobs cannot perform the exact same action twice in a single round (cannot Attack twice or Plunder twice). *Exception*: Move may be performed twice when fleeing or charging.

#### 3.2 Action Catalog (Standard Actions)
1. **Move (Boss or Mob)**: Cross up to **Movement** rating in discrete Zones.
2. **Attack (Boss or Mob)**: Engage enemy in melee (Tough pool) or ranged (Slink pool).
3. **Plunder (Boss or Mob)**: Pick up and secure loose Loot, Scrap, or items in current Zone.
4. **Manipulate (Boss or Mob)**: Interact with environment, operate machinery, trigger traps, search junk.
5. **Order (Boss only)**: Direct a Mob to spend its 2 actions. Controlled Mobs require no roll.

#### 3.3 The 5-Phase Combat Loop
```
[Phase 0: Setup] -> [Phase 1: Round Start] -> [Phase 2: Player Active Turn]
                         ^                                    |
                         |                                    v
                 [Phase 4: Round Closure] <--- [Phase 3: Enemy Active Turn]
                         |
                         v (If combat ends)
                 [Phase 5: Combat End]
```

- **Phase 0: Combat Setup**: Deploy zone layout, assign Zone Profiles, place initial units, declare visible hazards and Raid Point objectives.
- **Phase 1: Round Start**: Evaluate Start-of-Round condition triggers, spawn reinforcements, update Raid Points.
- **Phase 2: Player Active Turn**:
  1. *Player Declarations*: Bosses take actions in any sequence, move, attack, and issue Orders.
  2. *Unordered Mobs*: Once players finish, Mobs that received no orders resolve behavior:
     - **Loitering Mob**: Spends 1 action rolling on Loitering Table; saves 1 action for defense (1d6 Defence).
     - **Out of Control Mob**: Spends 2 actions rolling on Out of Control Table; saves 0 actions.
  3. *Enemy Reactions*: GM may declare enemy reactions to player movements/attacks.
- **Phase 3: Enemy Active Turn**:
  - Deterministic enemy threat resolution. Standard enemies and Mobs have 2 actions; Apex Bosses have 3 actions.
  - Players resolve defensive **Clatter Rolls** using saved actions, passive Armor Dice, or shout **"Scatter!"**.
- **Phase 4: Round Closure**:
  - Tally active Raid Points.
  - Process End-of-Round condition/hazard ticks (fire spread on 1d6 5–6).
  - Automatically clear all **Staggered** conditions on all units.
  - Resolve **Morale Checks** (Swarm Terror pool vs enemy Morale TN if 50% casualties occurred).
  - Reset all action budgets (3 Standard + Free Orders for Bosses; 2 Actions for Mobs).
- **Phase 5: Combat End & Tactical Retreat**:
  - Triggered when one side is eliminated or flees.
  - **Disengaging**: Leaving a zone with alert enemies requires a `Slink 5+/Highest Defence TN` test. Failure triggers Opportunity Attacks and stops movement. Bulk 3+ items prevent Disengaging.

---

### Domain 4: Zones, Movement & Environment

#### 4.1 Zone Topology & Gridless Movement
- **Spatial Abstraction**: Battlefields are structured as interconnected node graphs of discrete **Zones** (rooms, corridors, clearings, rooftops).
- **Distance**: Measured as integer step hops across connected zones via shortest path.
- **Movement Standard**: 1 Move action allows moving up to the entity's **Movement** stat in Zones (Boss default 2–5 based on Slink; Mob default 2).

#### 4.2 The Zone Profile Rule
Every Zone is assigned a default baseline profile: `Difficulty+/Target Number` (e.g., `5+/1`, `5+/2`, `6/1`).
- **Universal Traversal / Interaction**: Any climb, jump, search, balance, or obstacle check attempted within a Zone defaults to testing against that Zone's Profile. GMs do not invent ad-hoc DCs.
- **Boon/Bane Adjustments**: Tools and positioning apply standard Boons (+1d) or Banes (-1d) to the test pool while preserving the Zone Profile's base threshold.

#### 4.3 Cover Rules
- **Partial Cover**:
  - Attacking a target in Partial Cover imposes **Bane 1 (-1d)** on the attack roll.
  - Defending while in Partial Cover grants **Boon 1 (+1d)** to Dodge tests.
- **Full Cover**: Completely blocks direct line of sight and ranged targeting from that direction.

#### 4.4 Standardized Zone Traits & Environmental Hazards
- **Hazard Damage Scaling**:
  - **T1 Hazard (Minor)**: 1 damage to Grit or active Mob health die on failed test.
  - **T2 Hazard (Dangerous)**: 2 damage to Grit or active Mob health die.
  - **T3 Hazard (Lethal)**: 3 damage or severe condition infliction.

| Trait Name | Category | Primary Tags | Trigger Timing | Mechanical Rule & Test Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Slippery** | Obstacle | `[Slick]` | On Entry / Exit | `Slink` test vs Zone Profile. On failure: fall **Prone**, movement ends immediately. |
| **Rubble** | Obstacle | Terrain | Traversing | Movement costs double (costs 2 Zones of movement speed per zone crossed). |
| **Narrow** | Obstacle | Spatial Cap | Passive | Caps zone physical capacity and frontline width (default Size 2). Mobs exceeding capacity suffer **Bane 1 (-1d)** on physical tests, movement capped at 1 Zone, Melee dice pool capped at narrow limit. Giant foes cannot enter. |
| **Chasm / Pit** | Hazard (T3) | Obstacle | Crossing / Shove | `Slink` test vs Zone Profile. On failure: fall in, take **3 damage**, gain **Restrained**. Climbing out requires 1 action and `Tough` test vs Profile. |
| **Vertical Cliff** | Obstacle | Elevation | Vertical Move | Move action + `Slink` test vs Zone Profile. On failure: fall, take 1 damage per zone height, land **Prone**. |
| **Deep Water** | Obstacle | `[Wet]` | Passive / Move | Move action crosses only 1 Zone. Swimming without boat requires `Tough` test vs Profile or drown (1 damage/round). |
| **Burning** | Hazard (T2) | `[Fire]`, `[Gaseous]` | Entry / Turn Start | `Slink` test vs Zone Profile or take **2 damage** and gain Burning state. Attacks in zone get **+1 Success**. Spreads to flammable zones at End of Round on 1d6 (5–6). |
| **Crumbling Ceiling** | Hazard (T3) | `[Crushing]` | Round Start / Sabotage | `Slink` test vs Zone Profile or take **3 damage** and land **Prone**. Zone permanently becomes **Rubble**. |
| **Toxic Spores** | Hazard (T2) | `[Toxic]`, `[Gaseous]` | Turn Start | `Tough` test vs Zone Profile or gain **Weakened** condition (**-1d** on all action tests). |
| **Quicksand / Mud** | Hazard (T2) | `[Wet]`, `[Sinking]` | On Entry | `Slink` test vs Zone Profile or gain **Restrained**. Escaping takes 1 action and `Tough` test vs Profile. |
| **Howling Wind** | Hazard (T1) | `[Gale]` | Passive | Ranged attacks suffer **Bane 1 (-1d)**. Moving against wind requires `Tough` test or movement speed is halved. |
| **Pillars / Statues** | Opportunity | Cover | Passive / Free Action | Free Action to declare Full Cover against 1 designated adjacent zone. |
| **Shoring** | Opportunity | Structural | Manipulate / Attack | Test `Brains` or melee attack vs Zone Profile. On success: triggers Crumbling Ceiling and blocks exits (clearing blocked exit requires `Tough` test vs Profile). |

#### 4.5 Background Node Resolution (The Chaos Tick)
- When a Mob is left unsupervised at an inactive macro map node, it is resolved at each End of Round via the **Chaos Tick**:
  - Roll **d6s equal to Mob Size** against the node's Zone Profile (`5+/1`).
  - **Successes (5+)**: Progress Priority AI (1 = heal 1d6 on health dice or find 1d6 Scrap; 2 = find 2d6 Scrap or low-grade Oddity; 3+ = secure node as Safe and claim Standard Loot).
  - **Ones (1s)**: Each 1 rolled adds **+1d6** to the Bangaranga Pool and consults the **Gobbo Mischief Table**:
    - *0 Ones*: Smooth operations.
    - *1 One*: Bickering (Mob takes 1 damage to active health die).
    - *2 Ones*: Tasting Time (Mob gains **Weakened** condition).
    - *3 Ones*: Straying (Mob loses **1 Size**).
    - *4+ Ones*: Mutiny / Riot (Mob becomes **Uncontrolled** and hostile).
  - **The Farkle**: Zero successes and $\ge 2$ ones triggers a disastrous failure.

---

### Domain 5: Combat Engine

#### 5.1 Attack Declarations & Resolution Pipeline
1. **Base Pool Assembly**: Attacker rolls `Tough` (Melee) or `Slink` (Ranged) + Boons/Banes.
2. **Hit Evaluation vs Target Defence TN**:
   - **Standard Enemy**: Successes $\ge \text{Defence TN} \implies$ **One-Hit Kill**.
   - **Elite / Boss Enemy**: Successes $\ge \text{Defence TN} \implies$ Deals $\lfloor \text{Successes} / \text{Defence TN} \rfloor$ **Wounds** (**The Overkill Rule**).
   - **Enemy Mob (Single-Target)**: Successes $\ge \text{Defence TN} \implies$ Reduces lowest active health die by attack damage; excess spills over.
   - **Enemy Mob (Mob-on-Mob Melee - Frontline Rule)**: Attacking Mob rolls Size pool. Successes $\ge \text{Defence TN} \implies$ Applies damage simultaneously to defender's lowest health dice up to $\min(\text{Attacker Size}, \text{Defender Size})$.
3. **Stagger Resolution (Partial Hits)**:
   - If successes $\ge 1$ but $< \text{Defence TN}$:
     - If $\text{Impact Size} \ge \text{Target Physical Size} \implies$ Target gains **Staggered** condition until End of Round.
     - If $\text{Impact Size} < \text{Target Physical Size} \implies$ Target possesses mass resistance and ignores Stagger.
4. **Bounce**: If 0 successes are scored, attack bounces harmlessly.

#### 5.2 Impact Size Calculation
$$\text{Impact Size} = \text{Attacker Base Size} + \text{Weapon Trait Modifiers}$$
- **Goblin Boss / Standard Humanoid**: Base Size 1.
- **Mob**: Base Size equal to current Mob Size (1 to 5).
- **`Heavy` Weapon Trait**: **+1 Impact Size** (e.g. Size 1 Boss attacks with Impact Size 2).
- **`Crushing` Weapon Trait**: **+2 Impact Size** (attacks with Impact Size 3).
- **Explosives & Spells**: Impact Size equals **Tier** (T1=1, T2=2, T3=3, T4=4, T5=5).

#### 5.3 The Clatter Roll (Boss Defense)
When targeted by an incoming attack with a listed **Threat Profile** (`Threat [Face]+/[TN]`) and flat **Damage**:
1. **Simultaneous Dice Roll**:
   - **Active Stat Dice**: Roll `Slink` (Dodge) or `Tough` (Parry with Shield/Heavy weapon). *Requires 1 saved Standard Action.*
   - **Passive Armor Dice**: Roll bonus dice from equipped Armor (+1d Light, +2d Medium, +3d Heavy), Shield (+1d), and Slink Passive Defence (+1d to +2d).
2. **Resolution**:
   - **Clean Evasion**: If Stat Dice successes $\ge$ Threat TN $\implies$ **0 Damage taken**.
   - **Mitigation on Failed Evasion (or 0 saved actions)**:
     - Each success (**5+**) on Armor Dice reduces incoming damage by **1**.
     - Remaining damage is deducted directly from **Grit**.
3. **Ablative Gear Sacrifice (Optional)**: If unmitigated damage would reduce Grit to 0, the Boss may permanently destroy an equipped Shield or Armor suit to reduce the strike's damage to **0**.

#### 5.4 Mob Defense & The "Scatter!" Reaction
1. **Passive Armor**: If equipped, Mob rolls Armor Dice once per attack; each success (**5+**) reduces damage by 1 across all targeted dice.
2. **Active Scatter Reaction**: If the Mob has $\ge 1$ unused action remaining, the Boss spends a saved Standard Action (or unused Free Order) to order a Scatter:
   - Boss rolls **Mouth** dice pool against modified Threat TN:
     $$\text{Scatter TN} = \text{Threat TN} + (\text{Mob Size} - 1)$$
   - **Clean Scatter**: Mouth successes $\ge$ Scatter TN $\implies$ **0 Damage taken**, Mob moves **1 Zone** into cover.
   - **Failed Scatter**: Takes damage normally, mitigated only by passive Armor Dice.
   - **Scatter Gamble**: Boss may reroll 1s on Mouth dice. If the Gamble fails:
     - Mob takes full attack damage.
     - Mob takes **1 Trample Damage to EVERY active health die**.
     - Mob drops **1 Bulk** of carried Loot.
     - Mob immediately becomes **Out of Control**.
     - If Boss is in the same Zone, Boss gains **Staggered** condition.

#### 5.5 Group Attacks (Swarm Rules)
- When multiple standard enemies attack a single PC:
  - Base damage equals primary enemy attack damage + **1 damage per additional enemy** in the swarm.
  - The PC spends only **1 saved action** to resolve a single Clatter Roll against the entire combined swarm attack.
  - Targeting Cap: A maximum of 3 enemies may swarm a single PC. (Swarming against Mobs has no limit).

---

## 3. Formal Markdown Schemas for Content Extension Points

### 3.1 Weapon Schema
```markdown
### [CONTENT INSTANCE: Weapon]
**Name**: <Weapon Name>
**Category**: <Melee | Ranged | Improvised>
**Quality**: <T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary>
**Hands**: <1H | 2H | Worn>
**Bulk**: <Integer 0 to 4+>
**Range**: <Current Zone (Melee) | X Zones (Ranged)>
**Base Impact Size**: <Wielder Size | Wielder Size + 1 | Wielder Size + 2>
**Attack Profile**: <Tough (Melee) | Slink (Ranged)> vs Target Defence TN
**Break Roll**: <Breaks on 1-4 | Breaks on 1-3 | Breaks on 1-2 | Breaks on 1 | Never breaks>
**Traits**: <List of static traits: Heavy, Crushing, Cleave X, Concealable, Versatile, Reach, Piercing>
**Tags**: <Optional bracketed elemental/material tags, e.g. [Fire], [Shock]>
**Special Capabilities**: <Direct, unambiguous mechanical rules and permissions>
```

### 3.2 Armor & Shield Schema
```markdown
### [CONTENT INSTANCE: Armor / Shield]
**Name**: <Armor or Shield Name>
**Category**: <Light Armor | Medium Armor | Heavy Armor | Shield | Heavy Shield>
**Quality**: <T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary>
**Slot / Hands**: <Worn | 1H>
**Bulk**: <Integer 1 to 3> (For Mobs: Bulk Rating x Mob Size)
**Passive Armor Dice**: <+1d | +2d | +3d>
**Mobility Modifiers**: <None | Bane 1 (-1d) on Slink | Bane 2 (-2d) on Slink, Cannot Swim>
**Break Roll**: <Breaks on 1-4 | Breaks on 1-3 | Breaks on 1-2 | Breaks on 1 | Never breaks>
**Special Properties**: <e.g. Enables Tough Parry reaction, Ablative Sacrifice eligible>
**Tags**: <Optional material/elemental tags, e.g. [Reinforced], [Spiked]>
```

### 3.3 Gear & Tools Schema
```markdown
### [CONTENT INSTANCE: Gear / Tool / Consumable]
**Name**: <Item Name>
**Category**: <Adventuring Tool | Utility Gear | Consumable / Explosive | Loot Plunder>
**Quality**: <T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary>
**Bulk**: <Integer 0 to 4+>
**Usage / Lifespan**: <Permanent | Expended on Use (Consumable) | 1 Exploration Phase>
**Break Roll**: <Breaks on 1-4 | Breaks on 1-3 | Breaks on 1-2 | Breaks on 1 | Never breaks>
**Mechanical Function**: <Permission rule, Difficulty step shift (Hard->Normal->Easy), or Boon (+1d)>
**Area Threat Profile** *(Consumables/Explosives only)*: `Threat [Face]+/[TN]`, [Damage], `[Tags]`, Blast Range: <Current Zone | X Zones>, Impact Size: <Tier 1-5>
**Loot Value** *(Plunder only)*: <Tier 1-5 Value tokens>
```

### 3.4 Boss Quirk Schema
```markdown
### [CONTENT INSTANCE: Boss Quirk]
**Name**: <Quirk Name>
**Category**: <Tough | Slink | Brains | Mouth | General | Gang Legacy>
**Tier**: <T1 | T2 | T3 | T4 | T5>
**Prerequisite**: <Stat Name> Level $\ge$ Tier
**Cost**: <Passive | 1 Grunt | 1 Standard Action | 1 Reaction | 1 Free Order>
**Trigger**: <Passive | On Hit | On Dodge | On Fumble | Start of Turn | Action Declaration>
**Target Hub**: <Self | Allied Mob | Enemy in Zone | Zone Environment>
**Mechanical Effect**: <Precise Tier A rule specifying dice modification, condition, or action economy bypass>
**Twist Slots**: <1 Twist Max | 0 Twists>
**Keywords**: <[Keywords from Master Index]>
```

---

## 4. Mechanical Gap Analysis & Missing Rule Callouts

During inspection of `01_STAGE_Drafts/` and `02_PROD_Core_Rules/`, the following 10 critical mechanical gaps and inconsistencies were identified:

1. `[MISSING RULE / GAP: Unified Opposed & Resistance Test Mechanics — The core engine specifies that the GM never rolls dice, but opposed situations (such as stealth vs alert guards, intimidation, or NPC resistance) lack a standardized formula. Suggested Resolution: Define that all NPC resistance is represented as a static Difficulty face and Defence/Resistance TN (e.g. Alert Guard Notice is 5+/2), and the player rolls their active stat pool against that static profile.]`

2. `[MISSING RULE / GAP: Weapon Damage Metric & Starting Loadout Notation Discrepancy — In 11_Character Creation.md, weapons are listed with "+2d damage / +3d damage", whereas the core engine in 02 Combat.md and 33_Equipment.md specifies that attacks roll the character's base Tough/Slink pool and deal flat 1 damage/Wound per success threshold without "+Xd damage" dice bloat. Suggested Resolution: Strip "+Xd damage" from character creation files, standardizing that all weapon attacks roll the Boss's Tough/Slink pool, modified only by Boons/Banes, with weapon category dictating Hands, Bulk, Range, and Impact Size (+1 Heavy, +2 Crushing).]`

3. `[MISSING RULE / GAP: Ranged Weapon Ammunition Tracking — Rules state slings use scavenged stones, but bows, crossbows, and arbalests lack explicit ammunition rules (e.g. whether arrows/bolts consume Bulk or if ammo is abstract and only depleted on Fumbles). Suggested Resolution: Standardize that mundane quivers occupy 1 Bulk (providing unlimited standard ammo for 1 raid), or ammo is abstract and a Fumble on a ranged attack expends/breaks the active ammunition supply.]`

4. `[MISSING RULE / GAP: Disengage Failure & Opportunity Attack Resolution — The Disengage rule states a Slink 5+/Highest Defence test is required, but does not explicitly specify how Opportunity Attacks resolve if the test fails (e.g., whether all enemies in the zone execute deterministic attacks immediately and movement is halted, or if the Gobbo still moves but takes the damage). Suggested Resolution: Specify that on a failed Disengage test, the highest Threat enemy in the zone makes an immediate Opportunity Attack, and the character's movement ends immediately inside the current zone.]`

5. `[MISSING RULE / GAP: Mob Weapon Outfitting & Trait Scaling — Mob rules fully specify Mob Armor scaling (Bulk = Size x Armor Bulk) and Tools (flat Bulk), but omit the formal rules for equipping Mobs with upgraded weapons (e.g., Heavy Greatclubs or Cleaving Polearms). Suggested Resolution: Define that equipping a Mob with specialized weapons costs Size x Weapon Bulk, granting the entire Mob the weapon's traits (e.g. Heavy grants +1 Impact Size to the Mob's attacks, or Cleave allows damaging additional unengaged frontline dice).]`

6. `[MISSING RULE / GAP: Passive Armor Mitigation Cap & Stacking Rules — With Armor (+1d to +3d), Shields (+1d to +2d), Slink Passive Defence (+1d to +2d), and Elder buffs (+1d), mitigation pools can reach 6d-8d dice. There is no explicit stacking ceiling. Suggested Resolution: Formally define the mitigation dice pool as Armor Dice + Shield Dice + Slink Passive Defence, with a hard cap of 5d6 mitigation dice on any single Clatter Roll to prevent invulnerability.]`

7. `[MISSING RULE / GAP: Dual-Wielding Melee Weapons — Character creation mentions equipping two Light Melee weapons, but the Combat Engine (02 Combat.md) and Equipment rules (33_Equipment.md) contain no rule for dual-wielding. Suggested Resolution: Define that wielding an off-hand Light Melee weapon grants either a passive Boon 1 (+1d) to Melee Attack tests or allows splitting successes across two adjacent targets in the same zone.]`

8. `[MISSING RULE / GAP: Mob Encumbrance & Over-Laden Thresholds — PC Bosses suffer -1 Movement and Bane 1 (-1d) on physical tests when Over-Laden (Bulk > Carry). Mob rules specify dropping loot when Size drops, but lack clear rules for when carried Bulk exceeds baseline Loot Capacity. Suggested Resolution: Define that an Over-Laden Mob (carrying Bulk > Size x 4) suffers -1 Zone Movement per Move action and a Bane 1 (-1d) on all Slink and Tough tests.]`

9. `[MISSING RULE / GAP: Free Order Action Permissibility in Self-Defense Reactions — Rules clarify that Free Orders can be saved to issue a reactive "Scatter!" command to a Mob, but does not explicitly state whether an unused Free Order can be spent by the Boss to Dodge or Parry for themselves. Suggested Resolution: Explicitly state that Free Orders can ONLY be used for Mob command actions (such as giving an Order during your turn or shouting "Scatter!" as a reaction); personal Boss reactions (Dodge/Parry) strictly require saving a Standard Action.]`

10. `[MISSING RULE / GAP: Bangaranga Multi-Explosion Critical Cascade Definition — When rolling Bangaranga Dice, rolling a 6 explodes into two regular dice. The rules do not explicitly define whether a 6 rolled on either of those two bonus dice constitutes a Critical Success (granting +1 Grunt and a free action) or if Criticals require consecutive 6s on the same branch. Suggested Resolution: Clarify that any bonus die generated from an exploding 6 that rolls a 6 is treated as a Critical Success, granting +1 Grunt (up to max) and exploding recursively as normal dice, but a single test can grant at most +1 Grunt and 1 bonus action regardless of how many double-sixes occur.]`

---

## 5. Discovered Features Table

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| 1 | Dice Engine | D6 Pool Test | Rolling d6 pool vs Difficulty face and TN | Pool size, Difficulty (4+, 5+, 6), TN | Success count, Pass/Fail | 0 successes = Fail | PROD 01_Dice.md |
| 2 | Dice Engine | Exploding 6s | 6 is a success and rolls an extra d6 recursively | Natural 6 on any die | +1 Success, +1 bonus die | None | PROD 01_Dice.md |
| 3 | Dice Engine | Critical Success | 6 exploding into another 6 (double-six chain) | Natural 6 + bonus 6 | +1 Grunt, +1 Free non-offensive action | Capped at Max Grunt | PROD 01_Dice.md |
| 4 | Dice Engine | Salvage Roll | Desperate 1d6 roll when pool $\le$ 0d6 | Pool $\le$ 0d6 | 6=1 Success, 1=Fumble, 2-5=Fail | 1 loses 1 Grunt near Mobs | STAGE 01_Dice.md |
| 5 | Dice Engine | Gobbo Gamble | Rerolling 1s on failed tests | Failed test with $\ge 1$ ones | Rerolled 1s, new success total | Still failing = Fumble (-1 Grunt) | PROD 01_Dice.md |
| 6 | Dice Engine | Bangaranga Seeding | Starting pool based on party composition | Boss count, Mob sizes | Initial communal d6 pool | None | PROD 01_Dice.md |
| 7 | Dice Engine | Bangaranga Tapping & Tax | Drawing dice up to Grunt; tax if > TN | Desired dice, Grunt, test TN | Added pool dice, discarded tax die | Insufficient pool = cannot take | PROD 01_Dice.md |
| 8 | Dice Engine | Bangaranga Double Explosion | 6 on Bangaranga die explodes into 2 regular dice | Natural 6 on Bangaranga die | +1 Success, +2 bonus dice | None | PROD 01_Dice.md |
| 9 | Dice Engine | Overreaching | Penalties for failing with Bangaranga dice | Failed test using Bangaranga dice | -1 Grunt; 1s drain equal pool dice | Pool reduced by dice drawn | PROD 01_Dice.md |
| 10 | Attributes | Main & Secondary Stats | 4 stats (T, S, B, M) scaling 1-5 yielding 8 secondary stats | Stat level (1-5) | Grit, Carry, Move, Passive Def, Max Mobs, Free Orders, Power Words, Crafting | Max level 5 (Lv6 = Retire) | PROD 10_Stats.md |
| 11 | Attributes | Grunt Authority | Authority tracker equal to 2nd highest stat | 2nd highest Main Stat | Max Mob size, Max Bangaranga draw | 0 Grunt = command collapse | PROD 10_Stats.md |
| 12 | Attributes | Rebellion Test | Opposed check when Mob Size > current Grunt | Mob Size, Mouth/Tough pool | Controlled or Uncontrolled | Fail = Mob becomes Out of Control | PROD 10_Stats.md |
| 13 | Attributes | Assert Dominance | Undefended strike against own Mob to regain Grunt | Boss melee attack vs own Mob | Deal damage = +1 Grunt | 0 damage dealt = -1 Grunt | PROD 10_Stats.md |
| 14 | Boss Creation | Point Allocation & Role | Base 1s + 2 points; Specialist vs Generalist | Chosen distribution | Stats, Starting Role & Skill Level | Stat cap 3 at creation | STAGE 11_Character Creation.md |
| 15 | Gang Archetype | Infamy & Successors | Persistent Gang level; successor XP = Infamy x 4 | Infamy (1-5), Agendas, Loot | Successor XP, Gang Mark tattoo | Stat cap 4 on successor | STAGE 12_Gang.md |
| 16 | Gang Archetype | Elders & Bone Pile | Lv6 retirement and relics from glorious dead | Stat reaching 6; dead Boss | Lair room passive buffs, Relics | Elders cannot raid | STAGE 12_Gang.md |
| 17 | Action Economy | 3 Standard + 1 Free Order | Boss round action budget reset at round start | Round start trigger | 3 Standard Actions, 1 Free Order | Unsaved actions lost at round end | STAGE 02 Combat.md |
| 18 | Action Economy | Mob 2-Action Budget | Mob action budget (Ordered, Loitering, Out of Control) | Order status, Round start | 2 Actions executed or saved | 0 actions = cannot react | STAGE 02 Combat.md |
| 19 | Action Economy | The Boredom Rule | Mob cannot repeat exact same action in a round | Declared mob actions | Action validated | Move is sole repeat exception | STAGE 02 Combat.md |
| 20 | Turn Flow | 5-Phase Combat Loop | Setup, Round Start, Player Active, Enemy Active, Round Closure | Combat state | Phase progression | None | STAGE 02 Combat.md |
| 21 | Combat Engine | One-Hit Kill Minions | Standard enemies die on successes $\ge$ Defence TN | Attack successes, Defence TN | Enemy removed from play | Successes < TN = partial/miss | STAGE 02 Combat.md |
| 22 | Combat Engine | Overkill Rule | Elites take 1 Wound per full multiple of Defence TN | Attack successes, Defence TN | Wounds dealt = $\lfloor \text{Succ} / \text{TN} \rfloor$ | Remainder discarded | STAGE 20_Enemies.md |
| 23 | Combat Engine | Frontline Rule (Mob-on-Mob) | Damage applied to lowest dice up to attacker Size | Attacker Size, Defender dice | Simultaneous die reduction | Unengaged backline takes 0 | STAGE 13_Goblin_mob.md |
| 24 | Combat Engine | Cleave Trait (`Cleave X`) | Attacks damage up to X lowest dice or targets | Attack roll, Cleave rating X | X dice simultaneously damaged | Overkill applies to Elites | STAGE 06_Keywords Index.md |
| 25 | Combat Engine | Stagger Resolution | Partial hits inflict Staggered if Impact $\ge$ Target Size | Impact Size, Target Size, Succ $\ge 1$ | Staggered condition (-1d Def / -1 TN) | Impact < Target = immune | STAGE 02 Combat.md |
| 26 | Combat Engine | Clatter Roll | Simultaneous Active Stat + Passive Armor mitigation | Threat TN, Stat pool, Armor dice | Clean evasion (0 dmg) or Armor mitigation | Grit loss on remaining damage | STAGE 02 Combat.md |
| 27 | Combat Engine | Ablative Gear Sacrifice | Destroying Shield or Armor to cancel lethal strike | Lethal damage, equipped gear | Gear destroyed, damage reduced to 0 | Gear permanently lost | STAGE 33_Equipment.md |
| 28 | Combat Engine | Scatter Reaction | Boss Mouth test to evade AoE/threat for Mob | Saved reaction, Mouth pool, Size | Mob takes 0 dmg & scurries 1 Zone | Gamble fail = stampede trample | STAGE 02 Combat.md |
| 29 | Combat Engine | Group Attacks | Combining multiple enemies into 1 attack (+1 dmg/ally) | Swarm count, Base enemy attack | Single combined strike (1 Dodge needed) | Max 3 enemies against PC | STAGE 02 Combat.md |
| 30 | Zones & Movement | Zone Profile Rule | Zone Difficulty+/TN acts as default DC for all tests | Zone Profile, Player action | Test resolved vs Profile | GMs cannot invent ad-hoc DCs | STAGE 03_Movement & Zones.md |
| 31 | Zones & Movement | Cover Rules | Partial Cover (Bane to hit / Boon to Dodge); Full Cover | Obstacle positioning, Ranged attack | Modified dice pool / Target blocked | None | STAGE 02 Combat.md |
| 32 | Zones & Movement | Disengage & Opportunity | Slink 5+/Highest Defence to leave melee safely | Slink pool, Highest Defence TN | Safe exit or Opportunity Attacks | Bulk 3+ prevents Disengage | STAGE 02 Combat.md |
| 33 | Zones & Movement | Background Chaos Tick | Resolving abandoned unsupervised Mobs on minimap | Mob Size, Zone Profile | Priority AI progress, Mischief on 1s | $\ge 2$ ones + 0 succ = Farkle | STAGE 03_Movement & Zones.md |
| 34 | Equipment | Weapon Quality & Break Roll | Mundane gear breaks on Fumble based on Quality | Fumble trigger, Quality Tier (T1-T5) | 1d6 Break Roll vs threshold | T1 breaks 1-4; T5 never breaks | STAGE 33_Equipment.md |
| 35 | Equipment | Explosives Area Threat | Standard Area Threat Profile (`Threat+/TN`, Dmg, Tags) | Item Tier, Blast Zone | Blast damage & Stagger across Zone | None | STAGE 33_Equipment.md |

---

## 6. Edge Cases & Boundary Conditions

| # | Feature | Boundary Input / Scenario | Observed Systemic Behavior |
|---|---|---|---|
| 1 | Dice Pool | Pool reduced to negative dice (e.g. -2d6) | Triggers Salvage Roll (exactly 1d6 rolled). Roll of 6 gives 1 success; roll of 1 fumbles; 2–5 fails. |
| 2 | Bangaranga Tax | Test TN is 1, player takes 1 Bangaranga die | Takes $\le$ TN (1 $\le$ 1), so tax is 0 dice. Exactly 1 die is drawn and rolled. |
| 3 | Bangaranga Tax | Test TN is 1, player takes 2 Bangaranga dice | Takes $>$ TN (2 $>$ 1), so tax is 1 die. Requires 3 total dice in pool (2 rolled, 1 discarded). |
| 4 | Critical Success | Non-exploding Salvage roll lands on 6 | Salvage rules state "This die does not explode." No bonus die rolled, no Critical triggered. |
| 5 | Grunt Loss | Boss at 0 Grunt fumbles a test | Grunt remains at 0 (cannot drop below 0), but all controlled Mobs immediately trigger Rebellion tests. |
| 6 | Boss Death | Grit drops to 0 during combat | Boss immediately gains 1 Final Action + 1 Final Order Action (always Easy 4+), then dies. Gear drops in zone. |
| 7 | Stagger Resistance | Size 1 Goblin attacks Size 3 Troll with Light Weapon | Impact Size = 1. Target Size = 3. On 1 success (< Defence), Impact < Target $\implies$ 0 damage and NO Stagger. |
| 8 | Stagger Resistance | Size 1 Goblin attacks Size 3 Troll with T3 Powder Keg | Impact Size = 3 (T3). Target Size = 3. On partial blast, Impact $\ge$ Target $\implies$ Troll is Staggered. |
| 9 | Frontline Clash | Size 2 Guard Mob attacks Size 4 Goblin Mob (`[6, 4, 2, 1]`) dealing 2 damage | Attacker Size = 2. Engages 2 lowest dice (`[1]` and `[2]`). Both take 2 damage and are removed. Mob becomes Size 2 (`[6, 4]`). |
| 10 | AoE vs Mob | T2 Molotov (2 damage, `[Fire]`, AoE) hits Size 4 Mob (`[6, 4, 2, 1]`) | AoE has no engagement cap: ALL 4 dice suffer 2 damage $\implies$ dice become `[4, 2, 0, -1]`. Mob becomes Size 2 (`[4, 2]`). |
| 11 | Scatter Gamble | Boss gambles 1s on Mob Scatter and fails | Mob takes attack damage + 1 Trample damage to EVERY die + drops 1 Bulk loot + becomes Out of Control. |
| 12 | Clatter Roll | Attacker has Threat `5+/1`, 3 Damage. Defender has 0 saved actions, Light Armor (+1d) | Stat Dice = 0 (cannot dodge). Rolls 1 Armor Die: rolls a 5 (1 success). Mitigates 1 damage; takes 2 Grit damage. |
| 13 | Disengage | Goblin holding Bulk 3 Golden Idol attempts to Disengage | Rule strictly bans Disengage while clutching Bulk 3+ items. Must drop idol as Free Action or fight. |
| 14 | Narrow Choke | Size 4 Mob enters Narrow Zone (Capacity Size 2) | Suffers Bane 1 (-1d) on physical tests, Movement capped at 1 Zone, Melee combat pool capped at 2d6. |
| 15 | Cross-Gang Mob | Merged Super-Mob rolls attack pool containing three 1s | In-fighting trigger: Mob immediately inflicts 3 self-damage across its health dice, regardless of hit success. |
