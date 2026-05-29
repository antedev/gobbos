# Magic

*Goblins don't read dusty, boring spellbooks. We shout words we found carved on cave walls, squeeze glowing mushrooms until they pop, and hold onto the raw power of the cosmos until our fingernails smoke. If you aren't risking a complete detonation, are you even really casting?*

---

## Shouting Power Words

Magic in Gobbos is unstable, highly narrative, and driven by a push-your-luck casting loop. Rather than spending mana points or spell slots, spellcasters channel raw elemental and chaotic forces directly through their minds, balancing the desire for destructive power against the very real danger of their heads exploding.

### Prerequisites to Cast
Not every goblin can channel the unstable threads of magic. To cast a spell, a goblin must meet the following criteria:
1. **Brains 3+:** Your mind must be sharp (or cracked) enough to hold a Power Word in place.
2. **Magical Conduit:** You must possess a magic-focused **Quirk** (such as *Weirdo* or *Shaman*) or be wielding a magical **Oddity** (such as a runic staff, crystal skull, or channeling wand).

### Power Words as Descriptors
Goblins do not learn "spells." Instead, they learn **Power Words**, which are represented by the exact same **Narrative Descriptors (Tags)** used for Quirks, Gang Shenanigans, and Oddity Crafting (e.g., `[Fire]`, `[Sticky]`, `[Shock]`, `[Spooky]`, `[Slip]`). 
* If you have access to a Tag through your character's Quirks, Gear, Lair upgrades, or Gang traits, you can shout it as a Power Word to cast a spell.

---

## The Casting Loop

Casting a spell is a standard Action. When you cast a spell, perform the following steps:

1. **Declare the Power Word:** Announce the primary Tag you are channeling (e.g., `[Fire]`).
2. **Roll the Brains Pool:** Roll a number of **d6** equal to your **Brains** stat. The GM determines the Difficulty (**Easy: 4+**, **Normal: 5+**, **Hard: 6**) based on the environment or the target's resistance.
3. **Lock and Push:** 
   * To succeed at all, you must roll and lock in at least **1 success**.
   * **Settle:** You can stop rolling, immediately resolving the spell's effect using your current locked successes.
   * **Push:** You lock all current successes and reroll all non-success dice to try and build larger matching sets. 
4. **The Farkle:** If you choose to push and a reroll results in **zero new successes**, the spell fails completely. You must immediately roll on the **Spell Mishap** table corresponding to your Power Word's category.

>> **RULE: Exploding Dice & Magic**
>> Any time a **6** is rolled, it explodes. Roll an additional die and add it to your pool of non-locked dice. You can lock this new die if it counts as a success, or reroll it if you choose to Push.

---

## Resolving Spell Effects

The mechanical outcome of a spell is determined by the size of the largest matching set of success dice (e.g., a pair of `5`s, or three `6`s). This matching set determines the **Tier** of the spell's mechanical effect, matching the toolkit in [GDR-003: Unified Modular Powers System](../01_Characters & Mobs/GDR-003_Unified_Modular_Powers_System.md):

* **Single Success (No Pairs):** **T1 Effect** (Minor/Niche).
* **Pair (2-of-a-kind):** **T2 Effect** (Standard).
* **Triple (3-of-a-kind):** **T3 Effect** (Heroic/Area).
* **Quadruple (4-of-a-kind):** **T4 Effect** (Destructive).
* **Quintuple (5-of-a-kind):** **T5 Effect** (Legendary).

### Potency
If you roll multiple successes but none form a pair (e.g., you roll a `4`, `5`, and `6` on an Easy difficulty cast), the spell resolves as a **T1 Effect**. However, each success beyond the first acts as **Potency**, allowing you to choose one:
* Target one additional enemy in the same zone.
* Add **+1 Grit damage** or **+1 success** to the spell's effect.

> **Example:** Fizzle casts `[Fire]` on Normal difficulty (success on 5+) with a **Brains** of 5 (**5d6**).
> * **First Roll:** `[5, 5, 2, 1, 1]` $\rightarrow$ Fizzle has a pair of `5`s. This is currently a **T2 Effect**.
> * **The Push:** Fizzle wants a bigger explosion. He locks the two `5`s and rerolls the other 3 dice.
> * **Second Roll:** `[5, 6, 3]` $\rightarrow$ He rolls a new `5` and a `6`. Since the `6` is a success, he also locks it. He now has three `5`s (a triple $\rightarrow$ **T3 Effect**).
> * **Final Resolution:** Fizzle stops. He unleashes a **T3 Effect** (*Zone Area*) using the `[Fire]` tag, engulfing the entire adjacent zone in flames.

---

## Chaotic Leakage (Side Effects)

Channeling magic is sloppy. Any sets formed by non-success dice (faces that fell below the success threshold) represent magical energy leaking out of control. 
* A **pair** of non-success dice triggers a **T2 Side Effect**.
* A **triple** of non-success dice triggers a **T3 Side Effect**.
* Larger sets of non-success dice trigger higher-tier Side Effects accordingly.

>> **IMPORTANT: Hard Casting is Highly Volatile**
>> Because Hard difficulty (success only on 6) produces more non-success dice, Hard spells are mathematically almost guaranteed to leak energy. To "clean" a spell and remove non-success sets, you must risk Pushing your luck to convert those non-successes into successes (reducing the remaining non-success pool).

---

## Mishap & Side Effect Tables

When you cast magic, find the category that best fits your Power Word's narrative tag:

1. **Elemental / Physical:** Spells that create energy, matter, or physical hazards (e.g., `[Fire]`, `[Sticky]`, `[Shock]`, `[Toxic]`, `[Cold]`).
2. **Mental / Social:** Spells that warp minds, emotions, or spirits (e.g., `[Spooky]`, `[Loud]`, `[Confusing]`, `[Angelic]`, `[Undead]`).
3. **Movement / Space:** Spells that alter velocity, positioning, or physical laws (e.g., `[Slip]`, `[Elastic]`, `[Teleport]`, `[Fast]`).

---

### Category 1: Elemental / Physical

#### Elemental Side Effects (Leakage)
* **T2 Leakage:** The element coats the floor or air in your immediate vicinity. All movement in your Zone suffers a **Bane** until cleared.
* **T3 Leakage:** A sudden backfire scorches or covers you. You suffer a **T2 Condition** matching your tag (e.g., *Burnt* for `[Fire]`, *Weakened* for `[Toxic]`).
* **T4+ Leakage:** A wild vortex of the element fills your Zone. Every creature (friend or foe) in your Zone immediately loses **2 Grit**.

#### Elemental Spell Mishaps (Farkle)
* **Farkle:** The spell detonates in your hands. You fail to cast the spell, lose **2 Grit**, and the zone you occupy gains a permanent hazard matching the tag (e.g., a raging fire zone or a floor covered in sticky sludge).

---

### Category 2: Mental / Social

#### Mental Side Effects (Leakage)
* **T2 Leakage:** Your eyes glow and you speak in overlapping whispers. You cannot speak normally or coordinate with your gang until the end of your next turn.
* **T3 Leakage:** The magical echo frightens nearby creatures. All allies in your Zone suffer a **Bane** on their next action.
* **T4+ Leakage:** The mental pressure causes temporary madness. You suffer the *Confused* or *Terrified* condition, and cannot give orders to your mob.

#### Mental Spell Mishaps (Farkle)
* **Farkle:** Your mind fractures under the strain. You black out for a moment, fail to cast the spell, and suffer a permanent **Bane** to all **Brains** tests until you rest in the Lair.

---

### Category 3: Movement / Space

#### Movement Side Effects (Leakage)
* **T2 Leakage:** Gravity wobbles. You are pulled 1 Zone in a random direction or knocked prone.
* **T3 Leakage:** Space warps unpredictably. You and a random ally or enemy in your Zone swap places.
* **T4+ Leakage:** You become partially out of sync with reality. You suffer a **Bane** on all physical actions (**Vigor** and **Slink**) until the end of the encounter.

#### Movement Spell Mishaps (Farkle)
* **Farkle:** You are violently flung through space. You take **3 Grit damage** as you collide with a wall or obstacle, land prone in an adjacent Zone of the GM's choice, and drop any held items.
