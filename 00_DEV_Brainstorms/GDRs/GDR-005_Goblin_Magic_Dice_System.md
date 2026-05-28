# GDR-005: Goblin Magic Dice System

* **Status:** ACCEPTED
* **Date:** 2026-05-28
* **Designer(s):** User & Antigravity (AI Coding Assistant)
* **Target Folder:** `STAGE_Drafts/08_Magic/`

---

## 1. The Mechanical Challenge
In traditional TTRPGs, magic systems are often complex, requiring players to track spell slots, mana pools, or write down complex math equations post-roll. This violates **Tenet 1 (Fun/Fast)** and **Tenet 2 (Zero Post-Roll Math)**. 

Goblins shouldn't be reading dusty books; they should be shouting Power Words, holding unstable magic in their hands, and risking complete detonation for a bigger explosion. We need a magic casting mechanic that is narrative-first, uses our standard **d6** pools, and naturally scales risk with reward without adding numbers to track on the character sheet.

---

## 2. Proposed Design

Goblin magic uses a **Push-Your-Luck (Farkle-style)** dice rolling mechanic based on pattern matching. 

### The Casting Loop
1. **Declare the Spell:** The goblin selects a primary Power Word (Narrative Tag, e.g. `[BOOM]`, `[SHOCK]`, `[SLIP]`) they know.
2. **Roll the Pool:** The player rolls their **Brains** dice pool in **d6s**.
3. **Lock & Push:** To succeed at all, the player must lock in at least one **success** (based on GM difficulty: **Easy: 4+**, **Normal: 5+**, **Hard: 6**).
   * **Settle:** The player stops, resolving the spell with the current dice.
   * **Push:** The player locks their success(es) and rerolls all non-success dice to build bigger matching sets.
4. **The Farkle:** If a pushed reroll results in **zero new successes**, the spell fails completely, and the caster must immediately roll on the **Spell Mishap** table.

### Unified Tag System (Power Words as Descriptors)
Power Words are not a separate list of spells. Instead, they are the exact same **Narrative Descriptors (Tags)** used in [GDR-003: Unified Modular Powers System](GDR-003_Unified_Modular_Powers_System.md) for mutant Quirks, Gang Shenanigans, and Oddity Crafting:
* **One List of Tags:** If a goblin learns the `[Fire]` tag, they can shout it as a Power Word spell, grow a gland that spits it (Quirk), or craft it onto a weapon (Oddity).
* **Unified Progression:** Upgrading the lair or researching new elements unlocks new Tags that immediately benefit mages, crafters, and mutated warriors alike.

### Success sets = Spell Tier
The **Tier** (T1 to T5) of the spell's mechanical effect, as defined in [GDR-003: Unified Modular Powers System](GDR-003_Unified_Modular_Powers_System.md), is determined by the size of the largest matching set of success dice:
* **Single Success (No Pairs):** **T1 Effect** (Niche/Minor).
* **Pair (2-of-a-kind):** **T2 Effect** (Standard).
* **Triple (3-of-a-kind):** **T3 Effect** (Heroic/Area).
* **Quadruple (4-of-a-kind):** **T4 Effect** (Destructive).
* **Quintuple (5-of-a-kind):** **T5 Effect** (Legendary).

> **Example (Pushing for T3):** Fizzle casts `[BOOM]` with 5d6 on Normal (5+ is success). 
> * **First Roll:** `[5, 5, 2, 1, 1]` $\rightarrow$ two successes (pair of `5`s). This is a T2 spell.
> * **The Push:** Fizzle wants a bigger boom. He locks the pair of `5`s and rerolls the remaining 3 dice.
> * **Second Roll:** `[5, 6, 3]` $\rightarrow$ two new successes (`5` and `6`). 
> * **Final Pool:** Three `5`s (a triple $\rightarrow$ **T3 Effect**) and one `6` (extra success). Fizzle stops and unleashes a massive T3 fire blast.

### Non-Success sets = Chaotic Leakage (Side Effects)
Any sets formed by non-success dice (faces that fell below the success threshold) represent magical energy leaking out of control. 
* If the largest set of non-success dice is a **pair**, a **T2 Side Effect** triggers.
* If it is a **triple**, a **T3 Side Effect** triggers.
* **Math Scaling:** Because **Hard** difficulty tests result in more non-success dice, hard spells are mathematically far more likely to trigger chaotic leakage. For example, at a pool of 5d6:
  * On **Easy (4+)**, there is a **31.9%** chance of leakage.
  * On **Normal (5+)**, there is an **83.9%** chance of leakage.
  * On **Hard (6)**, there is a **96.1%** chance of leakage.
* **Cleaning the Spell:** Pushing your luck to convert non-success dice into successes reduces your non-success pool, helping to "clean" the spell and remove leakage sets (at the risk of a Farkle).

---

## 3. Alignment with Design Tenets

1. **Fun at the Table:** Pushing your luck is tense and highly interactive. Players will scream when they roll a quad or moan when they Farkle.
2. **Zero Post-Roll Math:** You only look at success vs. non-success faces and count matching numbers. No arithmetic needed.
3. **Embrace Chaos:** Higher difficulty tests and larger dice pools naturally lead to more volatile magic and side effects, matching the theme of unstable magic.
4. **Goblin Flavor:** Reckless casting, shouting words, and blowing oneself up is the ultimate goblin experience.

---

## 4. Edge Cases & Rules Lawyer Concerns
* **Successes with No Pairs (Potency):** If a caster rolls multiple successes but all are singletons (e.g. `[6, 5, 4]` on Easy), the spell is **T1** (minor effect). However, the *number* of successes acts as potency (e.g., hitting multiple targets, or dealing additional successes of damage/force).
* **Volatile Large Pools:** As shown by probability simulations, rolling 6d6 on Hard is **100% guaranteed** to result in a side effect if cast directly. Mages *must* push their luck to stand any chance of casting clean spells at high power.

---

## 5. Alternatives Considered
* **Mana Pools/Points:** Rejected immediately. Too much bookkeeping and violates the fast-paced, zero-math core tenets of the game.
* **Free Tag Assignment:** Letting players assign sets to any words they know post-roll was considered, but selecting the Power Word *before* rolling keeps the player focused and prevents decision-paralysis at the table.

>> **GOBLIN VERDICT:** Ye shout da word, ye roll da bones. If it ain't leakin' green sparks, ye ain't rollin' enough dice! Try to make it bigger, but don't cry when yer face gets singed.
