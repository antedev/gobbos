# Adversaries and Threats

*Gobbos are small, loud, and easily crushed underfoot. The world is infested with towering knights, lumbering trolls, and howling beasts that want nothing more than to wipe your gang off the map. But tall-men fight in rigid formations, and monsters are predictable. Goblins win through numbers, dirty tricks, and chaotic swarm violence.*

---

## 1. Deterministic Threat Resolution Engine

In Gobbos, the Game Master (GM) **never rolls dice**. Adversaries do not test for success, roll to hit, or roll variable damage. Every enemy action is a deterministic, incoming physical threat.

```
                    Adversary Declares Attack
               (Static Threat Profile + Flat Damage)
                                 │
                                 ▼
                     Goblin Boss Clatter Roll
                                 │
                   ┌─────────────┴─────────────┐
                   ▼                           ▼
          Saved Action Available?        0 Saved Actions?
                   │                           │
                   ▼                           ▼
        Roll Active Stat Dice +            Cannot Dodge/Parry!
        Passive Armor Dice                 (Roll Armor Dice Only)
                   │                           │
        ┌──────────┴──────────┐                │
        ▼                     ▼                ▼
   Stat Successes        Stat Successes   Every Armor Die 5+
   >= Threat TN           < Threat TN     Reduces Damage by 1
        │                     │                │
        ▼                     ▼                ▼
    0 Damage             Apply Armor      Remaining Damage
  (Clean Dodge/Parry)    Mitigation       Deducted from Grit
```

### Threat Profiles and Flat Damage
Every enemy attack is defined by a **Threat Profile** (`[Stat] [Target Face]+/[Successes]`) and a flat **Damage** value:
*   **Active Defense (Evasion):** When targeted by an attack, a **Goblin Boss** with a saved **Standard Action** rolls active stat dice (**Slink** to **Dodge**, or **Tough** to **Parry** if wielding a shield or heavy weapon). If the successes rolled meet or exceed the attack's **Threat TN**, the attack misses completely (**0 Damage taken**).
*   **Passive Defense (Armor):** If active evasion fails or the **Goblin Boss** has 0 saved actions, the attack hits. The player rolls passive **Armor Dice**; each die showing **5+** reduces incoming flat **Damage** by **1**.
*   **Unmitigated Damage:** Any remaining damage reduces the target's **Grit** (for Bosses) or removes health dice values (for Mobs).

---

## 2. The Three Enemy Scales

Adversaries are categorized into three distinct mechanical scales to govern how they absorb damage and die:

### 1. Standard Enemies (One-Hit Kill)
Standard enemies represent individual grunts, peasants, city guards, footpads, and minor monsters:
*   **One-Hit Kill:** When a player's attack scores successes equal to or greater than the standard enemy's **Defence TN**, the enemy is killed instantly and removed from the map.
*   **No Wounds:** Standard enemies do not possess a wounds track. Rolling fewer successes than **Defence TN** inflicts 0 damage (though it may inflict the **Staggered** condition if **Impact Size** meets or exceeds the target's physical **Size**).

### 2. Elites and Bosses (The Wounds Track)
Elites and Bosses represent formidable champions, armored commanders, and colossal apex predators:
*   **The Wounds Track:** Elites and Bosses track survivability using a **Wounds Track** (typically **2 to 8 Wounds**).
*   **The Overkill Rule:** An attack deals **1 Wound for every full multiple of the target's Defence TN** scored on a single attack roll:

$$\text{Wounds Dealt} = \left\lfloor \frac{\text{Attack Successes}}{\text{Target Defence TN}} \right\rfloor$$

>> **GOLDEN RULE: No Fractional Wounds**
>> Leftover successes that do not form a complete multiple of the enemy's **Defence TN** are discarded. They do not carry over to subsequent attacks.

### 3. Enemy Mobs (Swarms)
Enemy Mobs represent coordinated squads of standard foes acting as a single unit (e.g. a squad of 4 Town Watchmen or a swarm of 5 Giant Rats):
*   **Symmetrical Health Dice:** An Enemy **Mob** of **Size X** is tracked using **X physical d6s** on the table, each starting at the **"6" face**.
*   **Damage Resolution:** Single-target strikes damage the Mob's lowest active health die, spilling over to the next lowest die when a die reaches 0 and is removed.
*   **Frontline Rule:** Melee attacks from a player **Mob** apply damage simultaneously to a number of enemy health dice equal to the attacking Mob's current **Size**.
*   **Area Threats (`[AoE]`):** Full-zone explosive or breath hazards apply flat damage to **every single active die** in the Enemy Mob's pool simultaneously.
*   **The No Elite Mobs Rule:** Mobs can only consist of standard, one-hit-kill units. Elite and Boss enemies must always be fought as individual entities.

---

## 3. Enemy Mob Damage Scaling

An Enemy Mob's automatic attack damage scales deterministically with its current **Size**:

$$\text{Enemy Mob Damage} = \text{Base Unit Damage} + (\text{Current Mob Size} - 1)$$

*   **Attacking a Player Mob:** The Enemy Mob delivers this damage across the frontline, affecting a number of player goblin health dice equal to the Enemy Mob's current **Size** (targeting the lowest-value dice first).
*   **Attacking a Goblin Boss:** The Enemy Mob delivers this total damage as a single combined strike, which the **Goblin Boss** defends against using a single **Clatter Roll**.

---

## 4. The Three-Layer Trait Hierarchy

To eliminate rulebook page-flipping and prevent rules bloat during combat, all adversary behaviors are organized into a strict three-layer hierarchy.

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: UNIVERSAL ANCESTRIES                               │
│ (Beast, Humanoid, Undead, Monstrosity, Fiend)               │
│ • Universal biological/psychological rules                  │
│ • Resolved by GM without printing on individual statblocks  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: STANDARDIZED TAGS                                  │
│ (`[Hardened]`, `[Heavy]`, `[Fast]`, `[Regenerating]`, etc.) │
│ • Universal physical modifiers from Master Tag Index        │
│ • Compact keyword notation on statblocks                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: UNIQUE STATBLOCK TRAITS                            │
│ (Custom monster mechanics, reactions, and special triggers) │
│ • Standard Enemies: Maximum 1 Unique Trait                  │
│ • Elites & Bosses: Maximum 2 Unique Traits                  │
│ • Printed directly on the creature's statblock              │
└─────────────────────────────────────────────────────────────┘
```

### Layer 1: Universal Ancestries
Every adversary belongs to exactly one **Ancestry**, establishing its core psychological and biological baseline:

#### 1. Beast
*   **Morale Vulnerability:** Triggers an immediate **Morale Check** if exposed to sudden `[Fire]` or `[Loud]` tags in its **Zone**.
*   **Predatory Instinct:** Gains a **Boon 1 (+1d)** to attack targets with the `[Tasty]` or `[Bleeding]` tag, prioritizing them over all other targets.
*   **Social Immunity:** Immune to verbal **Mouth** manipulation or intimidation.

#### 2. Humanoid
*   **Tactical Discipline:** Utilizes cover and prioritizes attacking enemy commanders (**Goblin Bosses**).
*   **Standard Morale:** Subject to group **Morale Checks** upon suffering 50% casualties or the death of a leader.
*   **Plunder:** Drops salvageable weapons, armor, and **Loot** upon defeat.

#### 3. Undead
*   **Morale & Fear Immunity:** Completely immune to **Morale Checks** and the **Terrified** condition.
*   **Biological Immunity:** Immune to the **Weakened** condition caused by poison or disease; immune to `[Bleeding]`.
*   **Holy Vulnerability:** Attacks carrying the `[Angelic]` or `[Light]` tags deal **+1 Success** (lowering effective **Defence TN** by 1).

#### 4. Monstrosity
*   **Mass & Stagger Resistance:** Immune to the **Staggered** condition from partial hits unless the attack's **Impact Size** meets or exceeds the monster's physical **Size** ($\text{Impact Size} \ge \text{Size}$).
*   **Natural Cleave:** All melee attacks possess the `Cleave 2` trait (or higher), sweeping across multiple frontline health dice.

#### 5. Fiend (Demon)
*   **Fire & Terror Immunity:** Immune to damage and hazards with the `[Fire]` tag; immune to **Terrified** and **Dumb** conditions.
*   **Holy Bane:** Attacks carrying the `[Angelic]` tag ignore passive armor and reduce the Fiend's **Defence TN** by 1.
*   **Chaos Retaliation:** When a **Player** rolls a **Fumble** within 1 **Zone** of a Fiend, the Fiend immediately triggers a free reaction attack against that player.

### Layer 2: Standardized Tags
Tags represent universal physical modifiers (e.g. `[Hardened]`, `[Heavy]`, `[Teeny]`, `[Fast]`, `[Regenerating]`, `[Spiky]`). Their mechanical effects are identical across items, environments, and creatures (see [Combat Engine](05_Combat_Engine.md)).

### Layer 3: Unique Statblock Traits
Unique traits represent specialized combat maneuvers, reactions, or unique abilities printed directly on the creature's statblock:
*   **Standard Enemies:** Limited to a maximum of **one (1) unique statblock trait**.
*   **Elites and Bosses:** Limited to a maximum of **two (2) unique statblock traits**.

---

## 5. Enemy Action Economy, Reactions, and Group Attacks

### Action Economy
*   **Standard Action Pool:** On the Enemy Active Turn, each enemy unit (Standard, Mob, or Elite) receives **two (2) actions** per round to spend on **Move**, **Attack**, or **Manipulate** actions.
*   **Apex Bosses:** Colossal Bosses may possess traits granting **three (3) actions** or multi-phase action clocks.

### Enemy Reactions
Adversaries can trigger specialized reactions (such as parrying shields, retaliatory strikes, or steam vents) outside their active turn:
*   **Action Deduction:** Triggering an active reaction immediately expends **1 action** from the enemy's upcoming active turn.
*   **Reaction Cap:** Standard enemies and Elites may perform a maximum of **one (1) reaction per round**, and only if they have at least 1 saved action remaining. If an enemy has already spent both actions on its turn, it cannot trigger active reactions until actions reset at Round Start.

### Group Attacks (Enemy Swarms vs Bosses)
To prevent overwhelming action-economy drain and endless individual rolls when multiple standard enemies surround a single **Goblin Boss**:
*   **Combined Strike:** Up to **three (3) standard enemies** in melee range of the same **Goblin Boss** combine their attacks into a single strike.
*   **Damage Formula:** $\text{Combined Damage} = \text{Base Damage} + 1 \text{ per additional attacking enemy}$.
*   **Single Defense:** The **Goblin Boss** defends against the combined blow using a single **Clatter Roll**.

---

## 6. Enemy Morale, Swarm Terror, and Rallying

### The Morale Trigger
An enemy group must make an immediate **Morale Check** during the **Round Closure Phase** if they suffer catastrophic collapse:
1.  The enemy group loses **50% or more of its total units** (or 50% of an Enemy Mob's starting **Size**).
2.  The enemy group's **Commander** is slain.

### The Swarm Terror Check
The players roll a combined **Swarm Terror Pool** against the enemy group's static **Morale TN** (testing against **5+** difficulty):

$$\text{Swarm Terror Dice} = \sum \text{Surviving Mob Sizes in Zone/Adjacent} + \sum \text{Surviving Bosses in Zone/Adjacent}$$

*   **Success ($\text{Successes} \ge \text{Morale TN}$):** The enemy group breaks! The enemies drop heavy gear and must spend **two (2) Move actions** on their turns fleeing toward the nearest exit.
*   **Failure ($\text{Successes} < \text{Morale TN}$):** The enemies hold their ground and continue fighting.

### The Commander Rally
If an **Enemy Commander** survives and did not break, the commander may spend **1 Standard Action** on its turn to attempt a **Rally**:
*   **Opposed Roll:** The players roll their current **Swarm Terror Pool** against the Commander's **Morale TN**.
*   **Resolution:** If the players succeed, the goblin shouting and shield-banging drowns out the commander, and the troops continue fleeing. If the players fail, the commander restores order, and the troops return to combat.

---

## 7. Adversary and NPC Statblock Structural Schema

[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]

All living bestiary compendiums, monster catalogs, and NPC adversaries must follow this deterministic statblock schema:

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
| **[Attack Name 1]** | `[Stat] [Face]+/[TN]` (e.g. `Slink 5+/1`, `Tough 5+/2`) | [Flat Damage, e.g. 1–4] | [Melee | Ranged (X Zones) | Zone-Wide] | [Traits: Cleave X, Piercing, inflicts Condition on failed evasion] |
| **[Attack Name 2 (Optional)]** | `[Stat] [Face]+/[TN]` | [Flat Damage] | [Range] | [Special effects] |

**Reactions:** [Specific out-of-turn triggers, deducting 1 action from active turn if used.]  
**Flaw Hook / Vulnerability:** [Specific Tag interaction that lowers Defence TN or makes attacks Easy (4+).]  
**Plunder:** [Salvageable Scrap tier, Loot Value tokens, or Oddity parts dropped on defeat.]
```

---

## 8. Mechanical Gaps and System Clarifications

[MISSING RULE / GAP: Enemy reaction economy is capped at 1 reaction per round for Standard and Elite foes. An enemy must have at least 1 saved action remaining to react; an enemy that spent both actions on its turn cannot react until Round Start.]

[MISSING RULE / GAP: The Swarm Terror pool formula sums both surviving Mob Sizes and surviving Goblin Bosses in the combat zone and adjacent zones. This ensures high-chaos goblin swarms exert psychological pressure proportional to their collective presence.]
