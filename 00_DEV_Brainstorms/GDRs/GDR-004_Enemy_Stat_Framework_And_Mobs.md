# GDR-004: Enemy Stat Framework & Mobs

* **Status:** ACCEPTED
* **Date:** 2026-05-28
* **Designer(s):** User & Antigravity (AI Coding Assistant)
* **Target Folder:** `STAGE_Drafts/04_Enemies/`

---

## 1. The Mechanical Challenge
In the current draft of [20_Enemies.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/04_Enemies/20_Enemies.md), enemies are deterministic and simple. However, they lack flavor and mechanical distinctiveness: a Skeleton felt identical to a Guard, and a Dwarf felt identical to a Goblin, except for minor stat adjustments. 

If we add complex traits to make monsters distinct (such as in Warhammer Fantasy Roleplay 4e), running combat becomes a bookkeeping nightmare for the GM. Furthermore, we lacked a clear, unified system for **Enemy Mobs** (swarms of weak foes) that aligns with the player Mob rules without introducing massive stat-tracking bloat.

---

## 2. Proposed Design

This design establishes a **Three-Layer Enemy Traits Hierarchy** to define creature behaviors, alongside a **Unified Enemy Mob Framework** that keeps GM bookkeeping at absolute zero.

### 2.1. The Three-Layer Enemy Traits Hierarchy
To minimize cognitive load, creature traits are organized into three tiers based on how often they are used and where they are written:

1.  **Ancestries (Broad Archetypes):** Universal, passive rules that GMs can easily memorize because they apply to entire classes of creatures.
    *   *Example: Undead.* All undead are immune to **Morale** checks (they never flee) and immune to the **Terrified** condition.
2.  **Standardized Tags:** Common physical or movement properties shared by multiple creatures across different categories.
    *   *Example: Flying.* Ignores zone terrain hazards; cannot be hit by melee attacks unless the weapon has the `Long` tag.
    *   *Example: Giant.* Deals Cleave damage (applying to all dice in a Mob's pool).
3.  **Unique Statblock Traits:** Specific mechanical behaviors written directly on the creature's stat block. Because they are spelled out on the sheet, the GM never has to flip pages to look up monster-specific rules.
    *   *Example: Skeleton - Dry Bones.* Ranged/piercing attacks suffer a **Bane**; blunt/bashing attacks gain a **Boon**.
    *   *Example: Zombie - Relentless Meat.* When reduced to 0 health, it stays active for one final round (cannot take Move actions) and dies automatically at the start of the next round.
    *   *Example: Dwarf - Stubborn.* Immune to being shoved, moved, or knocked **Prone**.

---

### 2.2. The Enemy Mob Framework
Enemy Mobs represent swarms of weak creatures (like a horde of runts or a squad of town guards) unified under a single set of rules:

*   **Symmetrical Health (Dice-HP):** An Enemy Mob of **Size X** (Size 1–5) is tracked on the table using **X physical D6s** (each starting at 6). Standard spillover damage applies. **Area of Effect (AoE)** and Cleave attacks apply their damage to **every single die** in the Mob.
*   **Deterministic Attacks:** Since the GM never rolls dice, an Enemy Mob's automatic Attack damage scales deterministically: 
    $$\text{Mob Attack Damage} = \text{Base Unit Attack} + (\text{Size} - 1)$$
    *   *Example:* A single Guard deals 1 damage. A **Size 3** Guard Mob deals **3 damage** automatically when it attacks.
*   **Defence & Restricted Cleaving:** Goblins attack an Enemy Mob by testing against the base unit's **Defence TN**. 
    *   By default, a standard player attack kills exactly **one enemy unit** (reducing Mob Size by 1, removing one D6) on a success, regardless of excess successes.
    *   To kill multiple units in a single action, the player must use a **Quirk**, Weapon, or Spell with the `Cleave` or `AoE` trait.
    *   Mob-on-Mob combat cleaves naturally (damage reduces size directly).
*   **The "No Elite Mobs" Guardrail:** Mobs can only consist of standard, one-hit-kill enemies. Elite and Boss enemies (possessing a **Wounds** track) must always be fought as individual units, preventing complex multi-wound tracking within swarms.
*   **Mob Morale Units:** Each point of current **Mob Size** counts as one "unit" when calculating the 50% catastrophic loss threshold to trigger a group **Morale Check**.

---

## 3. Alignment with Design Tenets

1.  **Fun at the Table:** Different monsters force distinct tactical choices (e.g. archers targeting zombies while blunt-wielders shatter skeletons), making combat feel alive.
2.  **Zero Post-Roll Math:** No math is performed after rolling. Enemy mob attacks scale with a simple, static calculation. We explicitly reject traits that subtract successes post-roll (which are identical to simple high Defence anyway).
3.  **Embrace Chaos:** Mobs swarming players and players cleaving mobs with specialized gear creates cinematic swings in combat.
4.  **Goblin Flavor:** Facing structured human shield-walls or relentless undead hordes highlights the scrappy, chaotic underdog nature of playing goblins.

---

## 4. Edge Cases & Rules Lawyer Concerns
*   **GM Rolling:** All reassembly, infection, or survival traits are designed as passive triggers or static status updates. The GM never rolls dice to resolve monster abilities.
*   **Bookkeeping Bloat:** By keeping unique traits written directly on the statblock and restricting Mobs to standard (1-hit kill) units, the GM only tracks physical D6s on the table.

---

## 5. Alternatives Considered
*   **GM Reassembly Rolls:** We rejected having Skeletons roll a d6 to stand back up on their turns. It required GM dice rolling and created tracking confusion.
*   **Success Reduction Traits:** We rejected having Dwarves reduce incoming successes by 1. This violated the zero post-roll math tenet and behaved identically to simple high Defence.

---

>> **GOBLIN VERDICT:** "Dry bones go crunch when ya hit 'em wiv a club, but them soft zombies keep walkin' even after ya poke 'em full of holes. If there's a whole bunch of 'em, they hit harder, but ya can't cleave 'em all unless ya got a really big axe!"
