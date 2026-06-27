# Brainstorm: Enemy & NPC Modular Threat Framework

*Goblins don't fight fair, but neither do the things trying to eat them. A troll isn't just big; it's sticky, rubbery, and smells like a swamp that has been dead for a week. To capture this without making the GM roll a single die, we need threats that feel active, reactive, and beautifully chaotic.*

This brainstorm explores how to expand the **Unified Modular Powers System** to Enemies, Elites, and Bosses. Because the GM never rolls dice, enemy abilities cannot use player-style rolls. Instead, they operate as **Deterministic Threats**, **Roll Obstacles**, **Behavioral Schedules (Automata)**, and **Reaction Loops**, all tied together by the same element/trait tags used by the players.

---

## The Core Design Goals

1. **Zero GM Dice Rolls:** Every enemy ability must be resolved either deterministically (automatic damage/conditions) or by prompting a player roll (Dodge/Parry/Morale).
2. **Symmetrical Architecture:** Use a similar structure to the 6-block player blueprint so that designing an enemy feels familiar and interfaces cleanly with the player's gear and spells.
3. **Low GM Cognitive Load:** The system must run on simple priority loops or schedules that require no mental math or complex decision-making during a chaotic battle.
4. **Tag Synergy:** Enemy properties should utilize the same narrative descriptors (`[Fire]`, `[Sticky]`, `[Undead]`) as player gear, enabling emergent **Element Synthesis** in both directions.

---

## Proposal 1: Symmetrical Enemy "Threat Blocks"
Just as player powers use the 6-block blueprint, we can adapt the framework for enemies into a **Modular Threat Block**:

```markdown
### [Threat/Ability Name]
*   **Target:** [Who or what does this affect? (e.g., Player Grit, Mob Size, a specific Zone)]
*   **Threat Effect:** [The deterministic modification to the rules (e.g., -2d Bane, +1 TN, automatic Condition)]
*   **Trigger/Reaction:** [What event fires this? (e.g., Player Fumbles, Player enters Zone, Enemy takes a Wound)]
*   **Delivery:** [The range and area of effect (e.g., Melee, Ranged 1 Zone, Zone-Wide, Blast)]
*   **Schedule/Cost:** [How does the enemy pay for/rate-limit this? (e.g., Once per Encounter, ticks on Round Clock)]
*   **Duration:** [How long does the rule modification persist? (e.g., Sustained, End of Round, Permanent)]
```

### Adapting the 6 Blocks to GM Language:

1. **The Target:** Instead of stats like Brains or Mouth, enemies target **Player Action Pools**, **Grit**, **Mob Size**, **Zone Profiles** (TN), or **Bangaranga Pools**.
2. **Threat Effect (The "Anti-Modification"):** 
   - *Roll Impediments:* Grants the player a **Bane** (**-1d** to **-3d**) on certain tests.
   - *Difficulty Spikes:* Shakes up success parameters. E.g., **Hard Tests** (successes on 6s only) or **Fumble Expansion** (fumble on 1s and 2s).
   - *Deterministic Payloads:* Automatic damage or conditions (e.g., "Deals 1 Grit/Size damage at the end of the round if you remain in the Zone").
3. **Triggers (The GM's Reactivity):** Since the GM doesn't roll, the enemy reacts to player actions or roll results:
   - *On Player Fumble:* The classic retaliatory strike.
   - *On Player Strike (Thorns):* Damaging the enemy triggers a splash or explosion.
   - *On State Change:* Activates when the enemy drops to half Wounds, or when a Mob size is halved.
4. **Delivery:** Symmetrical to player rules. Melee, Ranged, Zone-Wide, or Blast.
5. **Schedule/Cost (The Automata):** Enemies don't have "Grunt" pools. Instead, they use a **Round Clock** or **Priority Queue** (see below).
6. **Duration:** Symmetrical. Instant, Sustained (players must spend an action to shake it off), or Round/Encounter-bounded.

---

## Proposal 2: The "Schedule" (Simple Automata Clocks)
For Bosses and Elites, we can implement a **Schedule**—a simple, deterministic script that runs on a countdown timer or a priority queue. This makes the boss feel like an active puzzle.

### Option A: The Action Clock (The Tick-Tock Boss)
The enemy has a numbered track. At the end of every round, the clock ticks forward.
*   **Dragon Clock:**
    *   **Round 1 (Sweep):** Tail Sweep. Everyone in Melee range must Dodge (Slink) or Parry (Tough) or take 2 damage and be knocked **Prone**.
    *   **Round 2 (Breathe):** Inhale. The dragon's throat glows. Fire tags are laid out in the front Zone.
    *   **Round 3 (Release):** Breath of Fire. The front Zone suffers a **T4 Blast** dealing 4 automatic damage (reduced by Slink Dodge). Reset Clock to 1.

### Option B: The Priority Queue (The Tactical AI)
A simple "If-Then" checklist that the GM resolves in order. The first condition met is the action the enemy takes.
*   **Elven Ranger AI:**
    1. **Fleeing?** If a Gobbo is in Melee range, spend 1 Action to *Disengage* and 1 Action to *Move* to an adjacent zone with cover.
    2. **Low Health ally?** If an allied soldier is wounded, fire a healing potion arrow (Range: 2 Zones, heals 1 Wound).
    3. **Default:** Fire a piercing arrow at the Gobbo Boss carrying the most Loot (Range: 3 Zones, 2 Damage, Parry test is **Hard**).

---

## Proposal 3: Symmetrical Tag-Based Synthesis (Interactive Environment)
One of the coolest elements of Gobbos is the interaction of physical descriptors (`[Sticky]`, `[Fire]`, `[Heavy Armored]`, `[Spooky]`). We can write enemy abilities as simple modifications of these tags.

By using the **Element Synthesis** table symmetrically, we get emergent gameplay out of very short rules text:

| Enemy Tag | Deterministic Effect | Player Synergy / Interaction |
|---|---|---|
| `[Acidic]` | When hit in Melee, attacker takes **1 Grit** damage unless they sacrifice a weapon/shield durability. | A player using a `[Glass]` weapon instantly shatters it, but a `[Stone]` weapon is immune. |
| `[Ghostly]` | Physical attacks suffer **+2 TN** successes to hit. | `[Magical]` or `[Holy]` weapons bypass this completely. |
| `[Sticky]` | Attacks automatically inflict the **Restrained** condition. | Any `[Fire]` source or `[Slick]` grease immediately clears this condition. |
| `[Heated]` | Deals **1 automatic damage** to anyone entering Melee. | `[Chilled]` or `[Water]` tags extinguish this for 1 round. |
| `[Rubbery]` | Blunt physical attacks are bounced back. | `[Piercing]` or `[Slashing]` attacks work normally. |

### How this reduces rules text:
Instead of writing out long text for a *Gelatinous Ooze*:
> **Ooze Statblock:**
> *   **Attack:** 1 | **Defence:** 1 | **Movement:** 1
> *   **Tags:** `[Sticky]`, `[Acidic]`, `[Rubbery]`
> *   *Special:* **Split:** If hit by a `[Slashing]` attack, the Ooze does not die. Instead, it splits into two Oozes of the same stats.

Because the GM and players already know what `[Sticky]`, `[Acidic]`, and `[Rubbery]` do from the universal tags list, the statblock is tiny, readable, and highly interactive.

---

## Brainstorming Options for the Framework

To choose the best approach, let's look at three ways to bundle these mechanics:

### Option 1: The "Anti-Blueprint" (High Symmetry)
*   **Concept:** Every monster ability is written using the exact same 6-block card format as player abilities.
*   **Pros:** Perfect symmetry. If a player uses a spell to tame a monster, the GM can hand them the card, and it reads exactly like their own Quirks or Gang features.
*   **Cons:** Might be too verbose for a GM running multiple types of monsters in a single combat scene.

### Option 2: The "Behavior / Reaction" Split (Tactical Focus)
*   **Concept:** Split enemy abilities into **Behavior** (what they do on their turn automatically via AI schedule) and **Reactions** (what happens when players attack them or interact with their Zone).
*   **Pros:** Highly functional at the table. When it is the enemy's turn, the GM looks at **Behavior**. When players are attacking, the GM looks at **Reactions**.
*   **Cons:** Loses the direct 1:1 mapping with the player modular system.

### Option 3: The "Tag & Stat Overlays" (Minimalist Focus)
*   **Concept:** Keep statblocks to a single line. The enemy has standard stats, and all their abilities are represented by 1 to 3 Tags. The rules for these tags are printed in a single cheat sheet on the GM screen.
*   **Pros:** Fastest combat resolution. Zero reading required during the fight once tags are memorized.
*   **Cons:** Harder to write highly unique, narrative "set-piece" boss fights without adding extra special text.

---

## Creative Recommendation: The "Triptych" Threat Block
To get the best of all worlds, we could design the NPC/Enemy ability framework around a three-part structure: **Schedule (Active)**, **Hazard (Reactive)**, and **Tags (Passive)**.

1.  **Passive (Tags):** Direct physical properties (e.g. `[Heated]`, `[Sticky]`, `[Heavy Armored]`) that interact symmetrically with player actions and elements.
2.  **Active (The Schedule):** Simple deterministic actions they perform on their turn, governed by a priority checklist or a round clock.
3.  **Reactive (The Hazards):** Interrupts or modifications to player rolls (e.g. "If you Fumble: [Effect]").

This structure maintains the design tenets of Gobbos: **Fun at the table**, **No GM math**, and **Embracing chaotic goblin energy**.
