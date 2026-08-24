# Magic and Bangaranga

*Goblins do not study dusty, leather-bound grimoires in high towers. We shout words carved into mossy dungeon stones, crush glowing cavern mushrooms in our bare fists, and cling to raw cosmic lightning until our teeth rattle. If you are not risking a catastrophic explosion, you are not really casting.*

---

## 1. The Pure Mechanical Casting Engine

Magic in Gobbos is unstable, highly tactile, and governed by a **Push-Your-Luck (Farkle-style)** pattern-matching dice engine. There are no mana points, spell slots, or daily casting limits. Magic is limited solely by your nerve, your **Brains** attribute, and the imminent danger of your head detonating.

```
       Declare Power Word Tag (1 Standard Action)
                           │
                           ▼
               Roll Brains Dice Pool (d6s)
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      At Least 1 Success?            0 Successes?
             │                           │
             │                           ▼
             │                     Farkle Mishap!
             │                  (Catastrophic Backfire)
             │
             ├───────────────────────────┐
             ▼                           ▼
      SETTLE FOR TIER             PUSH YOUR LUCK!
  (Lock largest matching      (Lock current successes,
   set & resolve effect)      reroll non-success dice)
                                         │
                         ┌───────────────┴───────────────┐
                         ▼                               ▼
                 New Successes?                   0 New Successes?
                         │                               │
                         ▼                               ▼
                 Build Larger Set                 Farkle Mishap!
               (Push again or Settle)          (Spell Fails & Backfires)
```

### Prerequisites to Cast
To channel the unstable currents of magic, a **Goblin Boss** must meet two mechanical requirements:
1.  **Brains Level 3+:** You must possess at least **Brains 3** to unlock **Power Word Slots**. Characters with **Brains 1** or **Brains 2** have 0 slots and cannot cast magic.
2.  **Magical Conduit:** You must possess a magic-focused **Quirk** (such as *Weirdo*, *Bone-Speaker*, or *Shaman*) or wield an active magical **Oddity** (such as a runic staff, crystal skull, or channeling wand).

### Power Word Slots and Memorization
Goblins do not learn rigid spells; they memorize **Power Words** represented by narrative **Tags** (e.g. `[Fire]`, `[Sticky]`, `[Shock]`, `[Spooky]`, `[Slip]`):
*   **Brains Level 1–2:** 0 Power Word Slots (Cannot cast).
*   **Brains Level 3:** **2 Power Word Slots**.
*   **Brains Level 4:** **4 Power Word Slots**.
*   **Brains Level 5:** **6 Power Word Slots**.
*   **Tag Swapping:** Swapping prepared **Power Words** in your slots takes place strictly in the **Lair** during the **Lair Phase** (see [The Lair Loop & Progression](10_The_Lair_Loop_and_Progression.md)). A character can attune to any Tag accessible through personal **Quirks**, carried **Gear**, or **Lair Upgrades**.

---

## 2. The Casting Step-by-Step Procedure

Casting a spell costs **1 Standard Action**. When your **Goblin Boss** casts a spell, execute the following four steps:

### Step 1 — Declare Power Word
Announce the primary **Tag** being channeled from your memorized slots (e.g. `[Fire]`, `[Toxic]`, `[Teleport]`).

### Step 2 — Roll Brains Pool
Assemble a dice pool of **d6s** equal to your **Brains** attribute (plus any optional **Bangaranga Dice** drawn from the pool). Roll against the **Difficulty** set by the **GM** based on the target's resistance or environmental warding:
*   **Easy (4+):** 4, 5, 6 are successes.
*   **Normal (5+):** 5, 6 are successes.
*   **Hard (6):** Only 6s are successes.

>> **RULE: Exploding 6s in Magic**
>> Any **6** rolled on a regular die counts as 1 success and explodes, immediately adding +1 regular die to your un-locked pool. Any **6** rolled on a **Bangaranga Die** explodes twice (+2 regular dice).

### Step 3 — Lock and Push
To maintain the spell, the roll must generate at least **one (1) success**:
*   **Settle:** You choose to stop rolling. Immediately resolve the spell's effect based on your current locked successes.
*   **Push:** You lock all current success dice and reroll all remaining non-success dice to hunt for matching faces and build higher-tier sets.

### Step 4 — The Farkle (Mishap)
If you choose to **Push** your luck and a reroll yields **zero (0) new successes**, the spell collapses into a **Farkle**. The casting fails completely, no spell effect is produced, and you must immediately roll on the **Spell Mishap** table corresponding to the spell's category.

---

## 3. Resolving Spell Tiers and Potency

The mechanical potency and area of effect of a spell are determined strictly by the size of the **largest matching set of success dice** (e.g. two 5s, three 6s, four 4s).

```
Matching Set Size             Spell Tier        Delivery Footprint & Impact
──────────────────────────────────────────────────────────────────────────
Single Success (No Pairs) ──► T1 (Minor)    ──► Touch / Melee (1 Success / 1 Damage)
Pair (2-of-a-kind)        ──► T2 (Standard) ──► Ranged 1 Zone (2 Successes / 2 Damage)
Triple (3-of-a-kind)      ──► T3 (Heroic)   ──► Zone-Wide Area (3 Successes / 3 Damage)
Quadruple (4-of-a-kind)   ──► T4 (Blast)    ──► Multi-Zone Blast (4 Successes / 4 Damage)
Quintuple (5-of-a-kind)   ──► T5 (Legendary)──► Map-Wide Reality Warp / Annihilation
```

### The Five Spell Tiers
*   **T1 Effect (Single Success, No Pairs):** Minor or niche manifestation. Inflicts 1 Grit/Size damage or grants +1 Success to an immediate physical action. Range: Touch / Melee.
*   **T2 Effect (Pair / 2-of-a-kind):** Standard tactical magic. Inflicts 2 Grit/Size damage or applies a sustained condition to 1 target. Range: Ranged (1 Zone).
*   **T3 Effect (Triple / 3-of-a-kind):** Heroic area magic. Inflicts 3 Grit/Size damage or applies a persistent condition across an entire **Zone**. Range: Zone-Wide.
*   **T4 Effect (Quadruple / 4-of-a-kind):** Destructive blast magic. Inflicts 4 Grit/Size damage or applies severe environmental hazards across the target Zone and all adjacent Zones. Range: Blast Area.
*   **T5 Effect (Quintuple / 5-of-a-kind):** Legendary encounter-scale catastrophe. Wipes out standard enemy swarms, collapses large structures, or permanently alters the battlefield topology.

### Potency (Singleton Successes)
If you roll multiple successes that do not form matching pairs (for example, rolling `[4, 5, 6]` on an Easy 4+ test), the spell resolves as a **T1 Effect**. However, every success beyond the first provides **Potency**. For each point of Potency, choose one:
*   **Extra Target:** Strike 1 additional enemy in the delivery area.
*   **Bonus Magnitude:** Add **+1 Damage** (against Grit or Mob health dice) or **+1 Success** to the spell's resolution.

> **Example:** A caster with **Brains 5** casts `[Shock]` against a **5+** profile.
> *   **First Roll:** `[5, 5, 3, 2, 1]` $\rightarrow$ The caster locks the two `5`s (a pair $\rightarrow$ **T2 Effect**).
> *   **The Push:** The caster wants a zone-wide lightning blast. The two `5`s remain locked, and the caster rerolls the `[3, 2, 1]`.
> *   **Second Roll:** `[5, 6, 2]` $\rightarrow$ The roll yields a new `5` and an exploding `6`. The caster locks both. The pool now contains three `5`s (a triple $\rightarrow$ **T3 Effect**) plus one singleton `6` (providing **1 Potency**).
> *   **Final Resolution:** The caster stops. The spell unleashes a **T3 Zone-Wide** shockwave dealing 3 damage to all enemies in the target Zone, plus +1 damage to the enemy commander from the Potency die.

---

## 4. Chaotic Leakage (Side Effects)

Channeling magical energy without precision causes raw power to bleed into the environment. Sets formed by **non-success dice** (dice faces falling below the success threshold) represent **Chaotic Leakage**:
*   **Pair of Non-Successes:** Triggers a **T2 Side Effect**.
*   **Triple of Non-Successes:** Triggers a **T3 Side Effect**.
*   **Quadruple+ of Non-Successes:** Triggers a **T4 Side Effect**.

>> **GOLDEN RULE: Hard Difficulty Volatility**
>> On **Hard (6)** casting tests, non-6 faces are non-successes. Hard casts naturally produce large non-success pools, making **Chaotic Leakage** almost guaranteed unless the caster takes the risk to **Push** and convert those non-successes into successes.

---

## 5. Standardized Mishap and Side Effect Tables

When resolving **Chaotic Leakage** or a **Farkle Mishap**, locate the table matching your **Power Word's** category:

### Category 1: Elemental & Physical
*(Tags: `[Fire]`, `[Sticky]`, `[Shock]`, `[Toxic]`, `[Acidic]`, `[Chilled]`, `[Slick]`)*

#### Elemental Side Effects (Leakage)
*   **T2 Leakage:** The element coats the floor in your **Zone**. All movement into or out of the **Zone** suffers a **Bane 1 (-1d)** until the end of the round.
*   **T3 Leakage:** Sudden backfire. The caster suffers the corresponding **T2 Condition** (e.g. **Weakened** from `[Toxic]`, **Restrained** from `[Sticky]`, or 1 fire damage from `[Fire]`).
*   **T4+ Leakage:** A wild elemental vortex engulfs your **Zone**. Every creature in the **Zone** (friend and foe) immediately loses **2 Grit** (or suffers 2 damage to Mob health dice).

#### Elemental Spell Mishap (Farkle)
*   **Mishap Outcome:** The spell detonates violently in your hands. The spell fails completely. The caster loses **2 Grit**, and the occupied **Zone** gains a permanent hazardous terrain tag matching the element (e.g. `[Burning]` or `[Toxic]`).

---

### Category 2: Mental & Social
*(Tags: `[Spooky]`, `[Loud]`, `[Confusing]`, `[Angelic]`, `[Vile]`, `[Soporific]`)*

#### Mental Side Effects (Leakage)
*   **T2 Leakage:** Sensory overload. Your eyes glow and you speak in overlapping whispers. You cannot issue verbal commands or coordinate with your **Mob** until the end of your next turn.
*   **T3 Leakage:** Psychic backlash. All allies in your **Zone** suffer a **Bane 1 (-1d)** on their next action test.
*   **T4+ Leakage:** Mental fracture. The caster gains the **Terrified** or **Dumb** condition, fleeing from the nearest ally or enemy for 1 round.

#### Mental Spell Mishap (Farkle)
*   **Mishap Outcome:** Your mind snaps under magical pressure. The spell fails, you black out until the end of the round (suffering the **Stunned** condition), and you suffer a **Bane 1 (-1d)** to all **Brains** tests until resting in the **Lair**.

---

### Category 3: Movement & Spatial
*(Tags: `[Slip]`, `[Elastic]`, `[Teleport]`, `[Fast]`, `[Bouncy]`, `[Weightless]`)*

#### Movement Side Effects (Leakage)
*   **T2 Leakage:** Gravitational wobble. The caster is violently yanked 1 **Zone** in a random direction and falls **Prone**.
*   **T3 Leakage:** Spatial swap. The caster and a random creature (friend or foe) in the same or adjacent **Zone** instantly swap physical positions.
*   **T4+ Leakage:** Dimensional phase. The caster becomes partially detached from reality, suffering a **Bane 1 (-1d)** on all physical tests (**Tough** and **Slink**) until combat ends.

#### Movement Spell Mishap (Farkle)
*   **Mishap Outcome:** Catastrophic kinetic ejection. The spell fails. You are hurled through the air into an adjacent **Zone**, take **2 Grit Damage** from the physical impact, drop all carried hand gear, and land **Prone**.

---

## 6. Bangaranga Integration in Spellcasting

A spellcaster can tap the communal **Bangaranga Pool** (see [Core Resolution](01_Core_Resolution.md)) to supercharge their magical channeling:
*   **Drawing Dice:** Before rolling **Step 2**, you may take a number of **Bangaranga Dice** up to your **Goblin Boss's** **Grunt** attribute and add them to your **Brains** casting pool.
*   **The Bangaranga Tax:** If the number of Bangaranga dice taken exceeds the test's **Target Number (TN)**, **1 extra die** must be removed from the pool and discarded back to the box as a tax.
*   **Double Explosions:** Every **6** rolled on a **Bangaranga Die** counts as a success and **explodes twice**, immediately granting two additional regular dice to the casting pool.
*   **Overreaching & Drain Risk:**
    *   If a spell that used Bangaranga dice fails or suffers a **Farkle**, the caster loses **1 Grunt**.
    *   If the failed roll contains any **1s** (even after pushing luck), the **Bangaranga Pool** is drained, immediately discarding dice equal to the number of Bangaranga dice taken.

---

## 7. Ritual Casting Mechanics

Ritual Magic represents extended, cooperative spellcasting used for monumental supernatural feats: purifying **`[Cursed]`** or **`[Bonded]`** oddities, warding the **Lair**, erecting permanent elemental barriers, or crafting magical artifacts.

```
  Lead Caster (Brains 3+) + Up to Mouth Assistants + Bangaranga Pool
                                  │
                                  ▼
                     Extended Assembly Dice Pool
              (Brains + 1d per Assistant + Bangaranga)
                                  │
                                  ▼
                     Cooperative Test Sequence
               (Accumulate successes toward Ritual TN)
                                  │
                ┌─────────────────┴─────────────────┐
                ▼                                   ▼
        Successes >= Ritual TN                  1s Rolled?
                │                                   │
                ▼                                   ▼
        Ritual Complete!                    Material Attrition
    (Curse Broken / Lair Warded)      (Lose Scrap & Spawn Hazards)
```

### Ritual Parameters
*   **Time & Scale:** A ritual requires **1 Lair Phase Turn** in the **Lair** (or 3 consecutive, uninterrupted combat rounds during a raid).
*   **Lead Caster:** Must possess **Brains 3+** and the relevant **Power Word** Tag.
*   **Assistants:** Up to a number of goblins equal to the Lead Caster's **Mouth** stat may assist. Each assistant contributes **+1d** to the ritual pool.
*   **Communal Fuel:** The Lead Caster may draw up to their **Grunt** in **Bangaranga Dice** to fuel the ritual.

### Extended Accumulation Engine
Rituals do not use the single-round Farkle loop. Instead, the Lead Caster rolls the assembled pool against **Normal (5+)** difficulty, accumulating successes across steps toward a **Ritual Target Number**:
*   **Tier 3 Ritual (Cleansing Minor Curses / Basic Wards):** Requires **5 Accumulated Successes**.
*   **Tier 4 Ritual (Cleansing Bonded Relics / Fortress Wards):** Requires **8 Accumulated Successes**.
*   **Tier 5 Ritual (Major Reality Transmutation / Artifact Crafting):** Requires **12 Accumulated Successes**.

### Ritual Complications and Resource Attrition
Because rituals are grounded, stable workings, failing a single roll does not destroy accumulated successes:
*   **The Cost of Failure:** Every **1** rolled during a ritual step consumes extra resources: the party must immediately discard **1 Scrap** (or 1 Bulk of carried **Loot**) per 1 rolled, or suffer a **T2 Chaotic Leakage Hazard** in the ritual chamber.
*   **Interruption:** If the Lead Caster suffers unmitigated damage or gains the **Stunned** condition during the ritual, the working collapses, wasting all invested materials.

---

## 8. Tag Effect and Spell Structural Schema

[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]

All modular tag effects, living spell compendiums, and grimoire expansions must follow this formal structural schema:

```markdown
### [Spell / Tag Power Name]
*   **Primary Tag:** `[Tag Name]` (e.g. `[Fire]`, `[Sticky]`, `[Shock]`, `[Spooky]`, `[Slip]`)
*   **Tag Category:** [Elemental / Physical | Mental / Social | Movement / Spatial | Metaphysical]
*   **Delivery Type:** [Personal | Touch / Melee | Ranged (1–3 Zones) | Zone-Wide | Blast]
*   **Bangaranga / Action Cost:** 1 Standard Action (Optional: Draw up to Grunt in Bangaranga Dice)
*   **Target Profile:** GM-set Difficulty (Easy 4+, Normal 5+, Hard 6) vs Target / Environment
*   **Effect by Tier:**
    *   **T1 (Single Success):** [Minor/Niche effect, +1 Success on attack OR 1 Grit/Size damage; Potency options]
    *   **T2 (Pair / 2-of-a-kind):** [Standard effect, +2 Successes OR 2 Grit/Size damage; Sustained condition]
    *   **T3 (Triple / 3-of-a-kind):** [Heroic / Zone-wide effect, +3 Successes OR 3 Grit/Size damage; Persistent condition]
    *   **T4 (Quadruple / 4-of-a-kind):** [Destructive / Blast effect, +4 Successes OR 4 Grit/Size damage; Encounter condition]
    *   **T5 (Quintuple / 5-of-a-kind):** [Legendary / Encounter-scale effect; Instant defeat OR permanent reality warp]
*   **Chaotic Leakage (Side Effects):**
    *   *Pair of Non-Successes (T2):* [Minor zone hazard, temporary Bane, or positioning wobble]
    *   *Triple of Non-Successes (T3):* [Dangerous self-inflicted condition, friendly Bane, or spatial warp]
    *   *Quadruple+ of Non-Successes (T4+):* [Zone-wide damage, severe condition, or dimensional fracture]
*   **Farkle / Mishap Outcome:** [Catastrophic consequence triggered when a push yields zero new successes]
*   **Element Synthesis Hooks:** [Predefined synergies when combined with other tags, e.g. `[Tag]` + `[Other]` -> Result]
```

---

## 9. Mechanical Gaps and System Clarifications

[MISSING RULE / GAP: Power Word slot progression is strictly bound to Brains Level 3+ (Level 3 = 2 slots, Level 4 = 4 slots, Level 5 = 6 slots). Any early draft reference to Brains 2 granting Power Word slots is deprecated; Brains 1 and 2 characters possess 0 slots and cannot cast magic.]

[MISSING RULE / GAP: Ritual casting mechanics were previously absent from stage drafts despite multiple references to cleansing curses and warding lairs. The extended cooperative accumulation engine (Lead Caster + Assistants + Bangaranga vs TN 5/8/12) is the authoritative rule for non-combat extended magic.]
