# Specification Mining Report: Combat, Mobs, Magic, Enemies & Conditions

**Agent:** Spec Miner 2 (`spec_miner_combat_magic_0`)  
**Working Directory:** `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\`  
**Date:** 2026-08-24  
**Scope:** Deep inspection and systemic extraction of:
1. Mob Mechanics (Anatomy, Size, Health Dice pool, Decrement/Spillover, Frontline Rule, AoE/Cleave resolution, Boss Orders, Loitering, Out-of-Control, Morale/Swarm Terror, Dispersal & Merging).
2. Damage, Grit, Conditions & Wounds (Deterministic threat resolution, Clatter Roll, Grit decrement, Wounds track, Overkill rule, Death & Dying, In-game conditions, Duration & recovery).
3. Magic & Bangaranga Framework (Bangaranga Pool generation, spending & tax, double explosions, overreaching, Farkle casting loop, Spell Tiers, Chaotic Leakage, Tag Effect architecture, Ritual casting).
4. Enemy & NPC Mechanics (Deterministic threat resolution, Zero GM rolls, 3 Enemy scales, 3-layer trait hierarchy: Ancestries, Tags, Statblock traits, Enemy reactions, Enemy Mobs, Morale & Rallying).

---

## 1. Systemic Mechanics Extraction by Domain

### Domain 1: Mob Mechanics

#### 1.1 Anatomy, Size & Metrics
A **Mob** is an abstract squad of lesser goblins under the command of a **Goblin Boss** (Player Character). Mobs do not have individual attribute stats; all capabilities scale from their **Size** (ranging from **Size 1** to **Size 5**).
*   **Size = Combat Dice:** A Mob rolls dice equal to its current Size (**1d6 to 5d6**) for physical combat and Tough tests.
*   **Required Grunt:** Commanding a Mob without penalties requires a Boss with **Grunt $\ge$ Mob Size**.
*   **Loot Capacity:** A Mob has a carrying capacity equal to $\text{Size} \times 4 \text{ Bulk}$ (Size 1 = 4 Bulk, Size 2 = 8 Bulk, Size 3 = 12 Bulk, Size 4 = 16 Bulk, Size 5 = 20 Bulk).
*   **Mob Gear & Armor Bulk:** Outfitting a Mob with Armor costs $\text{Size} \times \text{Armor Bulk Rating}$ (e.g. Light Armor costs $\text{Size} \times 1$ Bulk; Medium Armor costs $\text{Size} \times 2$ Bulk). Equipping tools costs flat Bulk. Carried gear directly reduces the Mob's remaining Loot Capacity.

#### 1.2 Mob Health & Damage Resolution
A Mob's health is physically represented on the table by a pool of **d6s equal to its current Size**, each starting at the **"6" face**. Damage is resolved according to the attack's delivery type:
1.  **Single-Target Attacks:** Applied directly to the Mob's **lowest-value active health die**. If the die is reduced below 1, it is removed from the table (reducing Mob Size by 1), and any excess damage **spills over** into the next lowest die.
2.  **Mob-on-Mob Melee (The Frontline Rule):** When two Mobs clash, the attacking Mob engages a number of health dice equal to its current Size: $\min(\text{Attacker Size}, \text{Defender Size})$. Damage applies simultaneously to the defender's lowest-value health dice up to that engagement cap. Unengaged backline dice suffer **0 damage**.
3.  **Cleaving Attacks (`Cleave X`):** Strikes with `Cleave X` sweep across the frontline, applying their damage simultaneously to **up to X of the Mob's lowest-value health dice**.
4.  **True Area Threats (`[AoE]` & Explosives):** Full-zone hazards, explosions, and breath weapons apply their damage simultaneously to **every single active die** in the Mob's pool without an engagement cap.
5.  **Casualties & Dropping Loot:** If a Mob loses Size and its carried Bulk exceeds its new Loot Capacity, the Boss must immediately declare which loose Loot items or tools are dropped onto the zone floor.

#### 1.3 Action Economy, Boss Orders & Command Flow
A Mob receives **two (2) actions** per round, reset at Round Start. A Mob acts on the Player Active Turn based on its command state:
*   **Command Line of Sight:** The Boss must have direct visual line of sight to the Mob to issue orders.
*   **Command Test Profile:** 
    *   *Base TN:* If Mob Size $\le$ Boss Grunt, **TN 1**. If Mob Size $>$ Boss Grunt, **TN increases by +1 per point of difference** (e.g., Grunt 2 ordering Size 4 Mob requires TN 3).
    *   *Distance:* Same Zone grants **+1 automatic success** (guaranteed success if Size $\le$ Grunt). Distance $\le$ Boss Mouth stat resolves as a **Normal (5+)** test. Distance = Boss Mouth $+ 1$ Zone resolves as a **Hard (6)** test. Distance $>$ Mouth $+ 1$ Zones is impossible.
*   **Action Consumption:** An ordered Mob spends 1 or 2 actions as directed. If ordered to spend only 1 action (e.g. Move), its remaining 1 action is saved for defense reactions.
*   **The Boredom Rule:** A Mob cannot perform the exact same action twice in a single round (e.g., cannot Attack twice or Plunder twice), with the exception of taking two Move actions to flee or charge.

#### 1.4 Unordered Mob States & Behavior Tables
Mobs that receive no orders resolve their actions after all player characters have finished their turns:
*   **Loitering (Under Control, No Orders):** Spends **1 action** rolling 1d6 on the Loitering Table; saves **1 action** for defense.
    *   *1 (Bicker):* Argues and pushes. (1 action spent, 1 action saved).
    *   *2 (Inspect):* Picks nose, stares at walls, draws graffiti. (1 action spent, 1 action saved).
    *   *3 (Snatch):* Plunders loose loot or eats food. (1 action spent, 1 action saved).
    *   *4 (Wander):* Moves 1 Zone in random direction (stays in LOS of Boss). (1 action spent, 1 action saved).
    *   *5 (Snoop):* Peers curiously; grants a Boon (+1d) to next PC notice/trap check. (1 action spent, 1 action saved).
    *   *6 (Taunt):* Screams insults and moons nearest enemy. (1 action spent, 1 action saved).
*   **Out of Control (Broken Command / Panic / Exceeded Grunt):** Spends **both actions** under GM control on the Out of Control Table (0 saved actions):
    *   *1–2 (Panic / Flee):* Flees toward exit if terrifying enemy is present; otherwise squabbles (Mob takes 1 damage and gains Staggered).
    *   *3–4 (Loot / Trash):* Plunders unattended loot or food (food heals 1d6 damage on health dice); otherwise trashes zone scenery.
    *   *5–6 (Frenzy):* Attacks nearest creature in zone (friend or foe!); if empty, wanders 1 Zone toward noise.

#### 1.5 Mob Defense & "Scatter!" Reaction
Mobs cannot naturally dodge. When targeted by an enemy attack:
*   **Passive Armor Dice:** If armored, rolls passive Armor Dice once per attack; each 5+ reduces damage by 1 across all targeted dice.
*   **"Scatter!" Order Reaction:** If the Mob has 1 saved action remaining, the Boss can spend a saved Standard Action (or unused Free Order) to order "Scatter!". The Mob rolls Boss **Mouth** stat dice against the attack's **Threat TN + (Mob Size - 1)**.
    *   *Success:* Mob avoids all damage (0 damage) and scurries 1 Zone into cover.
    *   *Failure:* Mob takes incoming damage, mitigated only by passive Armor Dice.
    *   *Gobbo Gamble on Scatter:* Boss may reroll 1s. If the Gamble fails: Mob takes attack damage + **1 Trample Damage to every single active die in its health pool** + drops 1 Bulk of Loot + becomes Out of Control. If the Boss is in the same zone, the Boss gains the **Staggered** condition.

#### 1.6 Splitting, Merging & Cross-Gang Mobs
*   **Splitting (1 Order Action):** A Mob splits into two smaller Mobs. Boss distributes active dice. Carried tools are assigned to specific sub-mobs; equipped armor rating is retained.
*   **Merging (1 Order / Manipulate Action in Same Zone):** Combines dice pools into one Mob. Total Size cannot exceed Boss Grunt (otherwise triggers immediate Rebellion test: Mouth or Tough `5+/Size`). Equipped armor dilutes by 1 Tier if not all goblins have armor.
*   **Cross-Gang Super-Mob:** Merged from multiple player Gangs. Requires a Grunt test (Tough in same zone, Mouth from afar) for any Boss to issue an order. **In-Fighting:** Whenever a Cross-Gang Mob rolls a dice pool for any check, **every 1 rolled deals 1 damage to the Mob itself**.

---

### Domain 2: Damage, Grit, Conditions & Wounds

#### 2.1 Deterministic Attack Resolution & The Clatter Roll
The GM never rolls to hit or damage. All attacks present a static **Threat Profile** (`Difficulty+/TN`, e.g. `5+/1`, `4+/2`, `6/1`) and flat **Damage**.
When a Goblin Boss is targeted by an attack:
1.  **Saved Action Required:** The Boss must spend a saved Standard Action to actively defend (**Dodge** using Slink, or **Parry** using Tough if wielding a shield or heavy weapon). If 0 saved actions are available, active evasion is impossible and the Boss relies entirely on passive armor.
2.  **The Clatter Roll:** The Boss throws active **Stat Dice** alongside distinct colored **Armor Dice** in a single roll:
    *   *Step 1 (Evasion):* If successes on Stat Dice $\ge$ Attack Threat TN $\rightarrow$ **0 Damage taken** (Clean Dodge/Parry).
    *   *Step 2 (Mitigation):* If Stat Dice fail Threat TN (or 0 saved actions), the attack hits. Every success (**5+**) on **Armor Dice** reduces incoming Damage by 1.
    *   *Step 3 (Grit Loss):* Any unmitigated Damage is deducted directly from the Boss's **Grit**.

#### 2.2 Boss Grit, Health Progression & Death Loop
*   **Grit Pool:** Derived strictly from **Tough** (Level 1 = 3 Grit, Level 2–3 = 4 Grit, Level 4–5 = 5 Grit).
*   **Death State (Grit = 0):** The Boss dies immediately, but triggers **The Final Act (Last Stand)**:
    *   The dying Boss immediately receives **1 Action + 1 Order Action** resolved at **Easy (4+)** difficulty (or automatic success for Orders in range) under the Rule of Cool.
    *   The Boss dies, and all carried gear is dropped in the zone.
*   **Temporary Boss:** During the remainder of the raid, one runt from the player's Gang steps up as a temporary boss (stats = deceased Boss stats - 1, min 1; no quirks).
*   **Respawn in Lair:** The player creates a new Boss from the Gang: Level 1 baseline + 2 advances + **Successor XP ($\text{Gang Infamy} \times 4$)**, 1 inherited Gang Mark Quirk, and a +2 XP catchup boost on the first surviving raid. Most favored gear becomes a **Named Item** (T1 Boon, Gang loyalty).

#### 2.3 Bosses, Elites & The Wounds Track
Elite and Boss enemies do not use Grit; they track damage using a **Wounds Track** (typically 2 to 8 Wounds).
*   **One-Hit Kill on Standard Enemies:** Rolling successes $\ge$ Defence TN instantly eliminates a standard enemy.
*   **The Overkill Rule:** Against Elites and Bosses, an attack inflicts **1 Wound for every full multiple of the target's Defence TN** scored on a single attack roll:
    $$\text{Wounds Dealt} = \left\lfloor \frac{\text{Attack Successes}}{\text{Target Defence TN}} \right\rfloor$$
    *(Example: Against Defence 2, scoring 2–3 successes deals 1 Wound, 4–5 successes deals 2 Wounds, 6+ successes deals 3 Wounds).*

#### 2.4 Impact Size & Stagger Resistance
If an attack scores at least **one (1) success** but fewer than the target's Defence TN, the attack does not deal damage or wounds, but can inflict the **Staggered** condition if the attack has sufficient mass:
*   **Stagger Threshold:** $\text{Impact Size} \ge \text{Target Physical Size}$.
*   **Impact Size Values:**
    *   Standard Boss Attack: Impact Size 1 (or current Mob Size for Mobs).
    *   `Heavy` Weapon Trait: $+1$ Impact Size (Size 1 Boss attacks at Impact Size 2).
    *   `Crushing` Weapon Trait: $+2$ Impact Size (attacks at Impact Size 3).
    *   Spells & Explosives: $\text{Impact Size} = \text{Tier}$ (T1 = Size 1, T2 = Size 2, T3 = Size 3, T4 = Size 4, T5 = Size 5).
*   **Mass Resistance:** If $\text{Impact Size} < \text{Target Physical Size}$, large foes (e.g. Size 2 Bears, Size 3 Trolls, Size 4 Dragons) completely ignore the Stagger effect.

#### 2.5 In-Game Status Conditions
The official systemic conditions and their precise mechanical effects across target types:

| Condition | Goblin Boss (PC) | Goblin Mob | Enemy / NPC |
| :--- | :--- | :--- | :--- |
| **Weakened** | **Bane 1 (-1d)** on Tough tests. | **Bane 1 (-1d)** on Attack rolls. | Attack Threat TN reduced by 1 (min 1). |
| **Restrained** | **Bane 1 (-1d)** on Slink tests; Movement becomes 0. | Cannot Scatter; Movement becomes 0. | Movement becomes 0; Defence TN reduced by 1 (min 1). |
| **Dumb** | **Bane 1 (-1d)** on Brains & Mouth; cannot cast spells or activate Brains quirks. | **Bane 1 (-1d)** on Morale checks; cannot receive complex orders. | Cannot cast spells or use tactical reactions. |
| **Silenced** | **Bane 1 (-1d)** on Mouth; cannot issue verbal orders or cast vocal spells. | Cannot hear orders; **Bane 1 (-1d)** on Morale. | Cannot issue orders or shout warnings. |
| **Blinded** | **Bane 1 (-1d)** on Physical tests; ranged attacks are Hard (6); cannot Dodge. | **Bane 1 (-1d)** on Physical tests; ranged attacks are Hard (6); cannot Scatter. | Attacks become Hard (6); Defence TN reduced by 1. |
| **Terrified** | **Bane 1 (-1d)** on Brains & Mouth; cannot move closer to source of fear. | **Bane 2 (-2d)** on Morale checks; Order tests targeting Mob are Hard (6). | Must spend actions fleeing from source of fear. |
| **Stunned** | Cannot take any Standard Actions, Free Actions, or Reactions. | Cannot take any actions or reactions. | Skips active turn; attacks against target are Easy (4+). |
| **Prone** | **Bane 1 (-1d)** on Slink & Dodge; costs 1 Move action to stand up. | **Bane 1 (-1d)** on Scatter; costs 1 Move action to stand up. | Attacks against target gain +1d; costs 1 Move action to stand up. |
| **Staggered** | **Bane 1 (-1d)** on Dodge and Parry Clatter rolls. | **-1 Armor Die** (or **-1d** on Scatter tests). | Defence TN reduced by **1** (minimum 1). |

#### 2.6 Condition Duration & Recovery
*   **Round-Closure Clearance:** The **Staggered** condition automatically clears on all PCs, Mobs, and Enemies during the **Round Closure Phase**.
*   **Action Clearance (Sustained Conditions):** Conditions inflicted by hazards (e.g. Weakened from gas, Restrained from mud) clear when a character spends a **Standard Action** (Manipulate or catching breath) in a clean zone, or automatically at the end of combat.
*   **Rest & Medical Clearance:** Long-term conditions (e.g. Filth Fever from sewer rats) persist until treated during downtime in the Lair.
*   **Healing Rates:** PCs heal **1 Grit per hour** of quiet rest. Mobs do **not heal** lost Size during raids (dead goblins are dead); after combat, the Boss may freely rearrange health dice values across surviving dice. Mob Size is restored by recruiting in the Lair.

---

### Domain 3: Magic & Bangaranga Framework

#### 3.1 The Bangaranga Pool Engine
The **Bangaranga Pool** is a shared communal pool of distinct red **d6s** representing the rowdy hype, chaos, and noise of the goblin horde.
*   **Raid Seeding:** At raid start, the pool is seeded with:
    *   **+1d** per Goblin Boss.
    *   **+1d** per Size 3 or Size 4 Mob.
    *   **+2d** per Size 5 Mob.
*   **Hype Triggers (Loading the Pool):**
    *   Any player rolls a **Critical Success** (double 6 chain): **+1d6**.
    *   Any player **Fumbles** a test: **+1d6**.
    *   Defeating an enemy with `[Notable]` or `[Big Threat]`: **+1d6**.
    *   Claiming a cache with `[Big Loot]` or `[Hoard]`: **+1d6**.
    *   Mob Chaos Tick on macro node rolls **1s**: **+1d6 per 1 rolled**.
*   **Tapping the Pool & The Bangaranga Tax:** Before rolling any test, a player may take dice from the Bangaranga Pool up to their Boss's **Grunt** stat and add them to their test pool:
    *   *No Tax:* If Bangaranga dice taken $\le$ Test Target Number (TN).
    *   *1 Die Tax:* If Bangaranga dice taken $>$ Test TN, **1 extra die** is removed from the pool and discarded to the box (not rolled).
*   **Double Explosion Rule:** Every **6** rolled on a Bangaranga Die counts as 1 success and **explodes twice** (immediately generating two additional regular dice).
*   **Overreaching & Pool Drainage:**
    *   Failing a test that used Bangaranga dice causes the Boss to **lose 1 Grunt**.
    *   If the failed roll contains any **1s** (even after pushing luck), the Bangaranga Pool is **drained**, permanently discarding a number of dice equal to the number of Bangaranga dice taken for the test.

#### 3.2 The Pure Mechanical Casting Engine
Goblin magic uses a **Push-Your-Luck (Farkle-style)** pattern-matching dice engine. Magic does not use spell slots or mana points.
*   **Prerequisites:** Brains Level 3+ (unlocks **Power Word slots**: Level 3 = 2 slots, Level 4 = 4 slots, Level 5 = 6 slots) and a magical conduit (Quirk or Oddity).
*   **Casting Action:** Costs **1 Standard Action**.
*   **Step 1 — Declare Power Word:** Declare the primary Tag being channeled (e.g. `[Fire]`, `[Sticky]`, `[Shock]`).
*   **Step 2 — Roll Brains Pool:** Roll a number of **d6s equal to Brains stat** against the GM-set Difficulty (Easy 4+, Normal 5+, Hard 6).
*   **Step 3 — Lock & Push:**
    *   Must roll and lock at least **1 success** to continue.
    *   *Settle:* Stop rolling and immediately resolve the spell's effect using current locked successes.
    *   *Push:* Lock all current successes and reroll all non-success dice to build larger matching sets.
*   **Step 4 — The Farkle (Mishap):** If a pushed reroll yields **zero new successes**, the spell fails completely. The caster immediately rolls on the **Spell Mishap** table corresponding to the Tag category.

#### 3.3 Resolving Spell Tiers & Potency
The mechanical power of the spell is determined by the size of the **largest matching set of success dice**:
*   **Single Success (No Pairs):** **T1 Effect** (Minor/Niche).
*   **Pair (2-of-a-kind):** **T2 Effect** (Standard).
*   **Triple (3-of-a-kind):** **T3 Effect** (Heroic / Zone Area).
*   **Quadruple (4-of-a-kind):** **T4 Effect** (Destructive / Blast Area).
*   **Quintuple (5-of-a-kind):** **T5 Effect** (Legendary / Encounter Scale).
*   **Potency (Singletons beyond the first):** If multiple successes are rolled without forming pairs (e.g. `[4, 5, 6]` on Easy), the spell resolves as a T1 Effect, but each extra success acts as **Potency**:
    *   Option A: Target 1 additional enemy in the delivery area.
    *   Option B: Add **+1 Grit damage** or **+1 automatic success** to the spell.

#### 3.4 Chaotic Leakage (Side Effects)
Non-success dice (faces below the Difficulty threshold) represent raw energy leaking out of control:
*   A **pair** of non-success dice triggers a **T2 Side Effect**.
*   A **triple** of non-success dice triggers a **T3 Side Effect**.
*   *Hard Difficulty Volatility:* Hard tests (success only on 6) produce large non-success pools, making leakage nearly certain unless the caster pushes luck to convert non-successes into successes.

#### 3.5 Tag Effect System Architecture
Spells combine three modular vectors:
1.  **Element (Tag Descriptor):** Physical/magical identity (e.g., `[Fire]`, `[Acidic]`, `[Shock]`, `[Sticky]`, `[Spooky]`).
2.  **Delivery (Range & Footprint):** Governed by Tier (T1 = Touch/Melee; T2 = Ranged 1 Zone; T3 = Zone-Wide; T4 = Blast [Own + Adjacent Zones]; T5 = Entire Encounter Map).
3.  **Magnitude & Duration:** Governed by Tier (T1 = 1 Success / 1 Damage / Instant; T2 = 2 Successes / 2 Damage / Sustained Condition; T3 = 3 Successes / 3 Damage / Persistent Condition; T4 = 4 Successes / 4 Damage / Encounter Duration).
*   **Element Synthesis:** When two tags combine, they resolve at downtime/creation into a single static profile with a maximum of 1 mechanical condition.

#### 3.6 Ritual Casting Engine (Systemic Architecture)
*   **Definition:** An extended, cooperative magic casting process used for high-tier magic, Lair warding, cleansing cursed/`[Bonded]` oddities, or crafting permanent enchantments.
*   **Mechanics:**
    *   *Time & Scale:* Takes 1 Lair Phase Turn (or 3 consecutive uninterrupted combat rounds).
    *   *Participants:* 1 Lead Caster (Brains 3+) + up to 1 Assistant per point of Lead Caster's Mouth stat.
    *   *Dice Assembly:* Lead Caster rolls Brains pool + 1d per Assistant + up to Lead Caster's Grunt from Bangaranga Pool.
    *   *Extended Accumulation:* Successes accumulate across steps toward a Ritual Target Number (e.g. TN 5 for T3 Rituals, TN 8 for T4 Rituals).
    *   *No Farkle Disintegration:* A failed roll on a ritual does not wipe accumulated successes; instead, rolling 1s generates Mishap Hazards or consumes extra Scrap/Loot components.

---

### Domain 4: Enemy & NPC Mechanics

#### 4.1 Deterministic Threat Engine
*   **Zero GM Rolls:** The GM never rolls attack rolls, damage rolls, or criticals.
*   **Threat Profiles:** Every enemy action lists a **Threat Profile** (`[Stat] [Target Face]+/[Successes]`, e.g. `Slink 5+/1`, `Tough 4+/2`, `Slink 6/1`) and flat **Damage**.
*   **Player Resolution:** The player defends with a Clatter Roll (Active Stat + Passive Armor Dice).

#### 4.2 Three-Tier Enemy Classification
1.  **Standard Enemies:** One-Hit Kill. Attacker scoring successes $\ge$ Defence TN instantly eliminates the foe.
2.  **Elites & Bosses:** Multi-wound threats tracking a **Wounds Track** (2 to 8 Wounds). Overkill rule inflicts 1 Wound per full multiple of Defence TN.
3.  **Enemy Mobs (Swarms):** Swarms of standard units of **Size 1 to 5**, tracked using **physical d6s equal to Size** (starting at 6).
    *   *Mob Attack Damage:* Scales deterministically: $\text{Damage} = \text{Base Unit Damage} + (\text{Size} - 1)$.
    *   *Frontline Rule:* Attacking a player Mob damages dice up to enemy Mob Size.
    *   *No Elite Mobs Rule:* Mobs can only be composed of standard, 1-hit-kill units. Elites/Bosses must be fought individually.

#### 4.3 Three-Layer Trait Hierarchy
1.  **Layer 1 — Universal Ancestries:** Universal biological/psychological archetypes:
    *   *Beast:* Morale check on Fire/Loud; prioritizes `[Tasty]` targets (+1d Boon); immune to verbal Mouth persuasion.
    *   *Humanoid:* Tactical discipline (uses cover, focuses commanders); standard morale at 50% casualties; drops salvageable scrap/loot.
    *   *Undead:* Immune to Morale and Terrified; immune to Weakened from poison/bleeding; Holy (`[Angelic]`/`[Light]`) attacks deal +1 Success.
    *   *Monstrosity:* Immune to Stagger unless $\text{Impact Size} \ge \text{Size}$; melee attacks naturally Cleave.
    *   *Fiend (Demon):* Immune to Fire; immune to Terrified/Confusing; Holy attacks ignore armor and reduce Defence TN by 1; triggers retaliation reaction on nearby Goblin Fumbles.
2.  **Layer 2 — Standardized Tags:** Physical modifiers (e.g. `[Hardened]`, `[Heavy]`, `[Teeny]`, `[Fast]`, `[Regenerating]`, `[Spiky]`).
3.  **Layer 3 — Unique Statblock Traits:** Custom behaviors printed directly on the sheet. Standard enemies have max 1 unique trait; Elites/Bosses have max 2.

#### 4.4 Enemy Action Economy & Reactions
*   **Action Pool:** Standard enemies, Mobs, and Elites have **two (2) actions** per round by default. Apex Bosses may have 3 actions or automated Action Clocks.
*   **Reaction Deductions:** Any reaction used out of turn deducts 1 action from the enemy's next active turn.
*   **Group Attacks (Enemy Swarms):** Up to 3 standard enemies engaging a single PC combine into a single attack: $\text{Base Damage} + 1 \text{ per extra enemy}$. The PC defends with a single Clatter Roll.

#### 4.5 Morale, Swarm Terror & Rallying
*   **Morale Trigger:** Occurs at Round Closure when an enemy group suffers catastrophic loss (50% casualties/Mob Size lost, or Commander killed).
*   **The Swarm Terror Check:** Players roll a combined **Swarm Terror pool** against the enemy's static **Morale TN**:
    $$\text{Swarm Terror Dice} = \sum \text{Surviving Mob Sizes in Zone/Adjacent} + \sum \text{Surviving Bosses in Zone/Adjacent}$$
    *   Successes $\ge$ Morale TN $\rightarrow$ Enemy group breaks and flees toward the nearest exit for 2 actions per turn.
*   **Commander Rally:** A surviving Enemy Commander can spend 1 action to attempt a Rally, triggering an opposed Swarm Terror roll vs the Commander's Morale TN.

---

## 2. Features Discovered Table

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| 1 | Mob Mechanics | Mob Anatomy & Size | Size 1–5 determines combat dice pool, required Grunt, and 4x Bulk carrying capacity. | Mob Size (1–5) | Combat dice (1d–5d), Grunt limit (1–5), Bulk capacity (4–20). | Size > Grunt triggers Rebellion test (Tough/Mouth `5+/Size`). | `13_Goblin_mob.md` |
| 2 | Mob Mechanics | Frontline Rule (Mob Melee) | Mob melee strikes defender's lowest health dice up to attacker's Size. | Attacker Size, Defender Size, Attack Damage | Simultaneous damage to $\min(\text{Atk Size}, \text{Def Size})$ lowest dice. | Dice reduced $<1$ removed; unengaged dice take 0. | `13_Goblin_mob.md`, `02 Combat.md` |
| 3 | Mob Mechanics | True AoE & Explosive Resolution | AoE attacks apply damage to every active die in a Mob's pool simultaneously. | AoE attack damage | Flat damage applied to all active health dice. | Massive casualties; drops loot exceeding new capacity. | `13_Goblin_mob.md`, `02 Combat.md` |
| 4 | Mob Mechanics | Boss Order Action | Boss commands Mob within visual line of sight. | Boss Mouth, Grunt, Mob Size, Distance | 1 or 2 directed actions executed by Mob. | Exceeding Mouth range increases difficulty to Hard (6); >Mouth+1 is impossible. | `04_Giving orders.md`, `02 Combat.md` |
| 5 | Mob Mechanics | Loitering State & Table | Unordered controlled Mob uses 1 action to loiter (d6 table) and saves 1 action for defense. | 1d6 roll on Loitering Table | Table outcome (Bicker, Inspect, Snatch, Wander, Snoop, Taunt) + 1 saved action. | None; Mob remains controlled. | `13_Goblin_mob.md` |
| 6 | Mob Mechanics | Out of Control State & Table | Uncontrolled Mob spends 2 actions running amok on d6 table under GM control. | 1d6 roll on Out of Control Table | Table outcome (Panic/Flee, Loot/Trash, Frenzy) + 0 saved actions. | May attack allies or flee from combat entirely. | `13_Goblin_mob.md` |
| 7 | Mob Mechanics | "Scatter!" Reaction & Gamble | Boss screams Scatter; Mob rolls Mouth vs Threat TN + (Size - 1) to evade and move 1 Zone. | Boss Mouth, Attack Threat TN, Mob Size | 0 damage taken + 1 Zone movement on success. | Gamble failure: 1 Trample damage to all dice, drops 1 Bulk, Out of Control, Boss Staggered. | `13_Goblin_mob.md`, `02 Combat.md` |
| 8 | Mob Mechanics | Mob Splitting & Merging | Boss splits Mob into smaller squads or merges squads in same zone up to Grunt cap. | Boss Order action, Mob Sizes | New Mob configurations; carried gear & armor distributed/diluted. | Exceeding Grunt on merge triggers immediate Rebellion check. | `13_Goblin_mob.md` |
| 9 | Mob Mechanics | Cross-Gang Super-Mob | Merging Mobs across player Gangs creates volatile swarm; every 1 rolled deals self-damage. | 2+ Gang Mobs, Grunt test | Combined massive dice pool. | Every 1 rolled on dice pool deals 1 damage to Mob itself. | `13_Goblin_mob.md` |
| 10 | Mob Mechanics | Chaos Tick (Macro Node AI) | Unsupervised split-off Mob resolves actions at round end via Size dice roll. | Mob Size dice vs Node Profile | Priority AI progress; 1s generate mischief and seed Bangaranga. | 4+ 1s triggers Mutiny / Rebellion. | `03_Movement & Zones.md` |
| 11 | Mob Mechanics | Mob Sacrifice Maneuvers | Boss orders Mobs into expendable maneuvers (Gobbo Pyramid, Living Bridge, Canary Runt). | Mob Size, Action/Damage cost | Bypasses climbing, crossing, traps, or fall damage. | Living Bridge deals 1 damage; Canary Runt absorbs trap damage. | `13_Goblin_mob.md` |
| 12 | Damage & Grit | Deterministic Threat Resolution | GM never rolls to hit; attacks present static Threat profile and flat Damage. | Enemy Threat (`Stat 5+/TN`), Damage | Player Clatter Roll (Active Stat + Passive Armor). | Failed evasion applies damage mitigated by armor to Grit/Mob. | `20_Enemies.md`, `02 Combat.md` |
| 13 | Damage & Grit | The Clatter Roll | Simultaneous roll of active defense (Slink/Tough) and colored passive Armor Dice. | Slink/Tough pool, Armor Dice pool, Threat TN | 0 damage if Stat $\ge$ TN; otherwise Armor 5+ reduces damage by 1. | 0 saved actions prevents Stat roll; relies solely on Armor dice. | `02 Combat.md`, `10_Stats.md` |
| 14 | Damage & Grit | Grit & Death Loop | Boss tracks Grit (3–5); reaching 0 Grit triggers Final Act (Last Stand) before death. | Tough stat, Incoming damage | Grit reduction; at 0 Grit: 1 Easy action + 1 Order, then death. | Temporary boss takes over; respawn in Lair with Successor XP. | `07_Wounds_Conditions.md`, `15_Level_Up and death.md` |
| 15 | Damage & Grit | Wounds Track & Overkill Rule | Elites/Bosses track Wounds; 1 Wound dealt per full multiple of Defence TN on single attack. | Attack Successes, Target Defence TN | Wounds dealt = $\lfloor \text{Successes} / \text{Defence TN} \rfloor$. | Rolling < Defence TN deals 0 Wounds. | `20_Enemies.md`, `21_Bestiary.md` |
| 16 | Damage & Grit | Impact Size & Stagger Rule | Partial hit (at least 1 success, < Defence TN) inflicts Staggered if Impact Size $\ge$ Target Size. | Weapon traits, Attacker Size, Target Size | Staggered condition applied until Round Closure. | If Impact Size < Target Size, Stagger is completely ignored. | `02 Combat.md`, `07_Wounds_Conditions.md` |
| 17 | Damage & Grit | Standard Conditions Matrix | 9 standardized conditions (Weakened, Restrained, Dumb, Silenced, Blinded, Terrified, Stunned, Prone, Staggered). | Trigger event / hazard | Specific stat/action penalties across PCs, Mobs, and Enemies. | Staggered clears at Round Closure; others require action or rest. | `07_Wounds_Conditions.md`, `08_Master_Tag_Index.md` |
| 18 | Magic & Bangaranga | Bangaranga Pool Seeding & Hype | Communal red d6 pool seeded at raid start and loaded by Crits, Fumbles, Kills, Loots. | Boss count, Mob sizes, Criticals, Fumbles | Shared Bangaranga dice pool. | Pool drained if a Bangaranga roll fails with 1s. | `01_Dice.md` |
| 19 | Magic & Bangaranga | Bangaranga Spending & Tax | Players add Bangaranga dice up to Grunt; pay 1 die tax if dice taken > test TN. | Desired Bangaranga dice, Test TN, Grunt | Bonus dice added to test pool; 6s double explode. | Failing test costs 1 Grunt; 1s drain pool by dice taken. | `01_Dice.md` |
| 20 | Magic & Bangaranga | Push-Your-Luck Farkle Casting | Brains dice pool rolled vs Difficulty; caster locks successes and pushes remaining dice. | Brains stat, Difficulty, Power Word Tag | Matching sets determine Spell Tier (T1–T5). | Pushing and rolling 0 new successes triggers Farkle Mishap. | `00_Magic_Rules.md`, `GDR-005` |
| 21 | Magic & Bangaranga | Spell Tier Matching Sets | Largest matching set of success dice determines Spell Tier (T1 single, T2 pair, T3 triple, T4 quad, T5 quint). | Locked success dice faces | Spell mechanical Tier and area/damage scale. | Singletons provide Potency (+1 target or +1 damage). | `00_Magic_Rules.md` |
| 22 | Magic & Bangaranga | Chaotic Leakage (Side Effects) | Sets of non-success dice trigger elemental, mental, or spatial side effects. | Non-success dice faces | T2 Side Effect (pair), T3 Side Effect (triple). | Hard casting mathematically guarantees leakage unless cleaned. | `00_Magic_Rules.md` |
| 23 | Magic & Bangaranga | Modular Tag System Architecture | Spells combine Tag Descriptor + Tier Footprint/Magnitude + Element Synthesis. | Narrative Tag, Tier (T1–T5) | Modular spell payload and environmental interaction. | Element synthesis capped at 1 mechanical condition. | `08_Master_Tag_Index.md`, `16_Unified_Modular_Powers_System.md` |
| 24 | Magic & Bangaranga | Ritual Casting Engine | Downtime/extended casting involving Lead Caster + Assistants + Bangaranga pool. | Brains pool, Assistants, Bangaranga dice | Accumulated successes toward ritual threshold (TN 5–8). | Failures generate complications/scrap costs rather than Farkle. | Mined requirement / Gap resolution |
| 25 | Enemy Mechanics | Three Enemy Scales | Standard (One-Hit Kill), Elite/Boss (Wounds track), Enemy Mob (Dice-HP). | Unit classification | Symmetrical resolution matching PC engine. | No Elite Mobs guardrail prevents multi-wound swarm bloat. | `20_Enemies.md`, `GDR-004` |
| 26 | Enemy Mechanics | Three-Layer Trait Hierarchy | Layer 1 Ancestries (universal), Layer 2 Tags (physical), Layer 3 Unique Traits (local). | Creature metadata | Rapid GM resolution with zero page flipping. | Standard enemies capped at 1 unique trait; Elites at 2. | `20_Enemies.md`, `21_Bestiary.md` |
| 27 | Enemy Mechanics | Enemy Mob Damage Scaling | Enemy Mob automatic damage = Base Damage + (Size - 1), applied via Frontline Rule. | Enemy Mob Size, Base Damage | Deterministic damage output against player Mobs or Bosses. | Damaged by single-target, Cleave, or AoE attacks symmetrically. | `20_Enemies.md`, `GDR-004` |
| 28 | Enemy Mechanics | Swarm Terror & Enemy Morale | 50% casualties triggers Morale Check; players roll Swarm Terror pool vs Morale TN. | Surviving Mob Sizes + Bosses vs Morale TN | Enemies break and flee toward exits on success. | Enemy Commander can spend action to attempt Rally check. | `20_Enemies.md`, `21_Bestiary.md` |
| 29 | Enemy Mechanics | Group Attacks (Swarms vs PC) | Up to 3 standard enemies combine into 1 attack (+1 damage per extra enemy). | 2–3 attacking enemies | Single incoming strike defended with 1 Clatter Roll. | Prevents action-economy drain and death by 1,000 cuts. | `02 Combat.md` |
| 30 | Enemy Mechanics | Enemy Reactive Deductions | Triggered enemy reactions deduct 1 action from their upcoming active turn. | Reaction trigger (e.g. Parrying Buckler, Steam Vent) | Immediate out-of-turn threat resolution. | Deducts from default 2 actions per round. | `20_Enemies.md` |

---

## 3. Edge Cases Table

| # | Feature | Input | Observed Behavior |
|---|---|---|---|
| 1 | Mob Damage Spillover | Single-target attack deals 4 damage to a Size 2 Mob with dice reading `[2, 5]`. | Damage hits lowest die (`[2]`). 2 damage reduces it to 0 (die removed, Mob becomes Size 1). Remaining 2 damage spills over into `[5]`, reducing it to `[3]`. Surviving pool: `[3]`. |
| 2 | Mob-on-Mob Frontline vs Narrow Zone | Size 4 Mob attacks Size 4 Mob in a `Narrow` corridor with a Frontline Width cap of Size 2. | Even though both Mobs are Size 4, the terrain caps frontline engagement at 2 dice. Only the 2 lowest dice of the defender take damage; 2 backline dice take 0. |
| 3 | AoE Damage on Low-Value Mob Dice | A T3 Fire Bomb deals 3 AoE damage to a Size 3 Mob with dice reading `[1, 2, 4]`. | All 3 dice take 3 damage simultaneously: `[1]` $\rightarrow 0$ (removed), `[2]` $\rightarrow 0$ (removed), `[4]` $\rightarrow 1$. Mob drops from Size 3 to Size 1 (`[1]`). |
| 4 | Scatter Gamble Failure Stampede | Boss Gambles on failed Scatter for Size 3 Mob (`[6, 4, 2]`) and still fails. | Mob takes attack damage + 1 Trample damage to every die (`[5, 3, 1]`), drops 1 Bulk loot, breaks into Out of Control state. Boss in zone becomes Staggered. |
| 5 | Super-Mob Cross-Gang In-Fighting | Cross-Gang Mob rolls 5d6 on an attack and rolls faces `[6, 5, 1, 1, 3]`. | The attack scores 2 successes (6 and 5). However, because two 1s were rolled, the Mob suffers 2 self-inflicted damage to its lowest active health die immediately. |
| 6 | Clatter Roll with 0 Saved Actions | Boss with Light Armor (+1d) is attacked by `Slink 5+/1`, Damage 2, but spent all 3 actions on turn. | Boss cannot roll Slink Stat dice (cannot Dodge). Boss only rolls the 1 Armor Die: if 5+, damage is reduced to 1; if 1–4, Boss takes full 2 Grit damage. |
| 7 | Overkill Multi-Wound Exact Multiple | Boss scores 5 successes against Solar Praetor (Defence 2, Wounds 5). | $\lfloor 5 / 2 \rfloor = 2$ Wounds dealt. The excess 1 success does not deal a partial wound; Praetor takes 2 Wounds. |
| 8 | Impact Size vs Stagger on Giant Monster | Size 1 Boss attacks Size 3 Swamp Troll with a Heavy Warhammer (Impact Size 2) and scores 1 success (Defence TN is 2). | The attack is a partial hit (1 success), but Impact Size 2 is less than Troll Size 3 ($2 < 3$). The Troll has natural mass resistance and ignores Stagger completely. |
| 9 | Farkle on High-Difficulty Hard Cast | Caster rolls 4d6 on Hard (6s only) for `[Fire]`, rolls `[6, 4, 2, 1]`. Locks the `6` and pushes the other 3 dice. Second roll is `[5, 3, 2]`. | Zero new successes (no 6s rolled). The spell Farkles completely: fails to cast, caster loses 2 Grit, and the zone gains a permanent burning hazard. |
| 10 | Bangaranga Double Explosion Chain | Caster spends 1 Bangaranga Die and rolls a `6`. | The 6 is 1 success and explodes twice, generating two new regular d6s. If either regular d6 rolls a 6, it explodes once normally. |
| 11 | Overreaching Bangaranga Pool Drain | Boss takes 2 Bangaranga dice on a 5+/2 test. Final roll is `[4, 3, 1, 1]`. Test fails. | Boss loses 1 Grunt for failing with Bangaranga. Because the roll contained 1s, 2 dice are immediately removed and discarded from the Bangaranga Pool. |
| 12 | Fiend Retaliation on Goblin Fumble | Boss fumbles an attack (rolls two 1s, zero successes) within 1 Zone of Brimstone Fiend. | The Fumble adds +1d to Bangaranga, but immediately triggers the Fiend's *Chaos Retaliation*, granting the Fiend an immediate free *Barbed Shadow-Whip* reaction against the Boss. |
| 13 | Undead Resistance to Piercing Weapons | Boss attacks Rattlebone Skeleton (Defence 2) with a Hunting Bow (`Piercing`). | *Dry Bones* trait applies a Bane (-1d) to the attack roll before rolling. If Boss had used a Heavy Club (`Bashing`), the attack would have gained a Boon (+1d). |
| 14 | Simultaneous Dying Last Stand | Boss reduced to 0 Grit by an attack declared during Enemy Active turn. | Boss triggers Final Act: takes 1 Easy (4+) action + 1 Free Order immediately. Boss orders Mob to attack the killer and throws a Molotov, then dies. |

---

## 4. Formal Content Schemas & Extension Templates

### Schema 1: Tag Effect / Spell Instance Schema

`[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]`

All spells and modular tag powers instantiated in Gobbos must adhere to this structured format. Living compendiums and custom grimoires must define every field according to this template:

```markdown
### [Spell / Tag Power Name]
*   **Primary Tag:** `[Tag Name]` (e.g. `[Fire]`, `[Sticky]`, `[Shock]`, `[Spooky]`, `[Slip]`)
*   **Tag Category:** [Elemental / Physical | Mental / Social | Movement / Space | Metaphysical]
*   **Delivery Type:** [Personal | Touch / Melee | Ranged (1–3 Zones) | Zone-Wide | Blast]
*   **Bangaranga / Action Cost:** 1 Standard Action (Optional: Spend up to Grunt in Bangaranga Dice)
*   **Target Profile:** GM-set Difficulty (Easy 4+, Normal 5+, Hard 6) vs. Target / Environment
*   **Effect by Tier:**
    *   **T1 (Single Success):** [Minor/Niche effect, +1 Success on attack OR 1 Grit/Size damage; Potency options]
    *   **T2 (Pair / 2-of-a-kind):** [Standard effect, +2 Successes OR 2 Grit/Size damage; Sustained condition]
    *   **T3 (Triple / 3-of-a-kind):** [Heroic / Zone-wide effect, +3 Successes OR 3 Grit/Size damage; Persistent condition]
    *   **T4 (Quadruple / 4-of-a-kind):** [Destructive / Blast effect, +4 Successes OR 4 Grit/Size damage; Encounter condition]
    *   **T5 (Quintuple / 5-of-a-kind):** [Legendary / Encounter-scale effect; Instant defeat OR permanent reality warp]
*   **Chaotic Leakage (Side Effects):**
    *   *Pair of Non-Successes (T2):* [Minor zone hazard, temporary Bane, or positioning wobble]
    *   *Triple of Non-Successes (T3):* [Dangerous self-inflicted condition, friendly Bane, or space warp]
    *   *Quad of Non-Successes (T4+):* [Zone-wide damage, severe condition, or dimensional fracture]
*   **Farkle / Mishap Outcome:** [Catastrophic consequence triggered when a push yields zero new successes]
*   **Element Synthesis Hooks:** [Predefined synergies when combined with other tags, e.g. `[Tag]` + `[Other]` $\rightarrow$ Result]
```

---

### Schema 2: Enemy & NPC Statblock Schema

`[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]`

All NPC adversaries, monsters, and enemy swarms must be structured according to this deterministic statblock schema:

```markdown
### [Enemy Name]
*[Threat Classification: Standard | Elite | Boss | Enemy Mob] [Ancestry: Beast | Humanoid | Undead | Monstrosity | Fiend | Construct] (Size [0–5])*  
*(If Elite or Boss) **Wounds:** [Wounds Track Value, e.g. 2–8]*  
*(If Enemy Mob) **Mob Size:** [Size 1–5, tracked via X physical d6s]*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **[Defence TN 1–4]** | **[Zones 1–4]** | **[Morale Profile, e.g. 5+/2, Immune]** | `[Tag 1]`, `[Tag 2]` |

**Special — [Unique Trait 1 Name]:** [Mechanical rule, trigger condition, and resolution. Standard enemies max 1 trait, Elites/Bosses max 2.]  
**Special — [Unique Trait 2 Name (Elite/Boss Only)]:** [Second unique trait or triggered reaction.]

#### Attacks
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **[Attack Name 1]** | `[Stat] [Face]+/[TN]` (e.g. `Slink 5+/1`, `Tough 5+/2`) | [Flat Damage, e.g. 1–4] | [Melee \| Ranged (X Zones) \| Zone-Wide] | [Traits: e.g. Cleave X, Piercing, inflicts Condition on failed evasion] |
| **[Attack Name 2 (Optional)]** | `[Stat] [Face]+/[TN]` | [Flat Damage] | [Range] | [Special effects] |

**Reactions:** [Specific out-of-turn triggers, deducting 1 action from active turn if used.]  
**Flaw Hook / Vulnerability:** [Specific Tag interaction that lowers Defence TN or makes attacks Easy (4+).]  
**Plunder:** [Salvageable Scrap tier, Loot Value tokens, or Oddity parts dropped on defeat.]
```

---

### Schema 3: Condition & Hazard Schema

`[CONTENT EXTENSION POINT: Environmental Hazards & Conditions]`

All status conditions, environmental hazards, and zone impairments must be structured according to this standardized schema:

```markdown
### [Condition / Hazard Name]
*   **Classification:** [Status Condition | Static Environmental Obstacle | Dynamic Zone Hazard | Complex Weather Blueprint]
*   **Associated Tags:** `[Tag 1]`, `[Tag 2]` (e.g. `[Toxic]`, `[Gaseous]`, `[Slick]`)
*   **Severity Tier:** [T1 Minor | T2 Dangerous | T3 Lethal / Catastrophic]
*   **Application Trigger:** [When applied: On hit, entering zone, start of round, failing physical test]
*   **Mechanical Effects:**
    *   *Goblin Boss (PC):* [Specific stat penalty, Bane modifier, movement restriction, or action denial]
    *   *Goblin Mob:* [Specific attack penalty, Scatter restriction, health damage, or Morale Bane]
    *   *Enemy / NPC:* [Specific Defence TN reduction, action loss, or movement cap]
*   **Duration & Persistence:** [Instant | Active Round-Sustained (clears at Round Closure) | Sustained (Action-Clear) | Encounter-Bounded | Lair-Treated]
*   **Removal / Recovery Check:** [Action cost and test required to clear, e.g. Spend 1 Standard Action in clean zone testing Tough 5+/1]
```

---

## 5. Mechanical Gaps, Broken Loops & Ambiguities Inventory

During deep inspection of `01_STAGE_Drafts`, `02_PROD_Core_Rules`, and `00_DEV_Brainstorms`, the following 8 critical gaps and contradictions were identified in the combat, mob, magic, and enemy domains:

### Gap 1: Ritual Magic Casting Mechanics Completely Unspecified
`[MISSING RULE / GAP: Ritual magic is referenced across lore, Master Tag Index (clearing Cursed and Bonded items), and core requirements, but no mechanical rules existed in STAGE or DEV. To maintain the zero-math, high-chaos engine, ritual casting must be defined as an extended cooperative downtime/exploration mechanic: a Lead Caster (Brains 3+) supported by Assistants pooling Brains dice + communal Bangaranga dice toward an accumulated success threshold (TN 5 for T3, TN 8 for T4), where rolled 1s consume extra Scrap/Loot resources rather than causing instant Farkle detonation.]`

### Gap 2: Contradiction in Power Word Slots Progression
`[MISSING RULE / GAP: In 10_Stats.md, Power Word slots are 0 at Brains Level 1 and 2, unlocking at Level 3 with 2 slots, Level 4 with 4 slots, and Level 5 with 6 slots. Conversely, 00_Magic_Rules.md states that Power Word slots equal Brains - 1 (which would grant 1 slot at Level 2). To maintain single-source rule integrity, 10_Stats.md is authoritative: Brains 1–2 have 0 Power Word slots (cannot cast), and magic unlocks strictly at Brains Level 3.]`

### Gap 3: Player Goblin Mob Morale Resolution Undefined
`[MISSING RULE / GAP: While Swarm Terror rules clearly define how players force Morale Checks on enemies at 50% casualties, the exact procedure for how a Player Goblin Mob tests Morale when suffering 50% casualties or encountering a Terrifying enemy is vague. Suggested resolution: When a Player Mob suffers 50% casualties or is exposed to a Terrifying foe, the controlling Boss must pass an immediate Mouth or Grunt test against Normal difficulty (5+/1); on a failure, the Mob breaks command and enters the Out of Control state until rallied.]`

### Gap 4: Rallying Dispersed or Panicked Mobs Lacks Action Cost & Profile
`[MISSING RULE / GAP: When a Mob enters the Out of Control state or flees due to panic, the rules state the Boss must spend an Order action to regain control, but lack explicit distance and difficulty modifiers. Suggested resolution: Regaining control of an Out of Control Mob requires 1 Standard Action (Order) and a Mouth test matching the standard command distance profile (Same zone = Auto success if Size <= Grunt; 1 to Mouth zones = Normal 5+; Mouth + 1 zones = Hard 6). Success restores the Mob to the Ordered state; failure leaves it Out of Control for that round.]`

### Gap 5: Ambiguity Between "1d6 Defence" in Loitering Table and Scatter Reaction
`[MISSING RULE / GAP: In 13_Goblin_mob.md (lines 68, 97–102), the Loitering Table states a loitering mob 'saves 1 action for 1d6 Defence'. However, Gobbos combat rules establish that Mobs cannot naturally dodge and use Boss Mouth Scatter reactions or passive armor. The phrase '1d6 Defence' is a legacy drafting relic that contradicts the Clatter Roll engine. Suggested resolution: Update the Loitering Table text to state 'Uses 1 action. Saves 1 action to enable the Boss to order a Scatter! reaction or defend with passive Armor.']`

### Gap 6: Mid-Combat Damage Dice Redistribution Unclarified
`[MISSING RULE / GAP: 07_Wounds_Conditions.md permits a Boss to freely redistribute physical health dice across surviving dice 'once a battle is concluded', but does not specify if this can be done mid-combat. Suggested resolution: Explicitly state that mid-combat health dice redistribution is forbidden during active combat rounds; it represents resting, bandaging, and regrouping that occurs strictly during the Round Closure phase of Combat End or during downtime.]`

### Gap 7: PC Wounds vs. Grit Terminology Drift
`[MISSING RULE / GAP: In 06_Keywords Index and several early drafts, the keyword 'Wound' was defined as applying to both PCs and Elites. However, core architecture mandates strict keyword constancy: Player Bosses exclusively track Grit (3–5 points); only Elite and Boss NPCs track Wounds; Mobs exclusively track Health Dice. Suggested resolution: Standardize all text so that Player Bosses never possess or take Wounds; they suffer Grit damage. Wounds are exclusive to Elite/Boss monster tracks.]`

### Gap 8: Enemy Reaction Economy Cap
`[MISSING RULE / GAP: While 20_Enemies.md states that enemy reactions deduct 1 action from their upcoming active turn, it does not specify whether an enemy with 0 actions remaining can react. Suggested resolution: Standardize that standard enemies and Elites (with 2 actions per round) can take a maximum of 1 Reaction per round, which immediately expends 1 of their 2 actions. If an enemy has already spent both actions on its turn, it has 0 saved actions and cannot trigger active reactions until actions reset at Round Start.]`

---

## 6. Synthesis Recommendations for PROD

1. **Chapter Separation:**
   - Place all Mob command, size, health dice, frontline combat, and behavior tables into `02_PROD_Core_Rules/01_Characters & Mobs/13_Goblin_mob.md`.
   - Place all Damage resolution, Clatter Roll, Grit, Death & Dying, and Conditions into `02_PROD_Core_Rules/00_Rules/07_Wounds_Conditions.md`.
   - Place pure Magic Casting, Bangaranga engine, Spell Tiers, Leakage, Tag synthesis, and Rituals into `02_PROD_Core_Rules/08_Magic/00_Magic_Rules.md` (with zero specific spell listings, using the Tag Effect Schema).
   - Place deterministic threat mechanics, 3 enemy scales, 3-layer trait hierarchy, and morale into `02_PROD_Core_Rules/04_Enemies/20_Enemies.md` (with zero bestiary statblocks, using the Statblock Schema).
2. **Strict Keyword Adherence:** Enforce Grit (PCs), Wounds (Elite NPCs), Health Dice (Mobs), Loot (treasure), Mob (player squads).
3. **Cross-Referencing:** Ensure all condition, weapon trait, and zone profile references link to single-source definitions in `00_Rules/`.
