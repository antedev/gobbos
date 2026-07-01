# Brainstorm: Tag Stress-Testing Scenarios

*Goblins don't play chess; they play "what happens if I strap a magnet to a bomb and drop it down a chimney." If the tag system cannot resolve these crazy plans instantly at the table, it fails. Here, we stress-test our tag catalog against the most chaotic player scenarios imaginable.*

This document runs four complex "stress tests" of player creativity against the **Master Tag Index** to verify that our pre-roll resolution mechanics remain fast, intuitive, and consistent.

---

## Stress Test 1: The "Junk Magnet Bomb"
*   **The Player Plan:** A goblin crafter builds a throw-bomb with `[Magnetic]` and `[Explosive]` tags. They throw it into a zone containing three heavily armored dwarven knights (`Corporeal:Metal`) and one unarmored scout (`Corporeal:Flesh`). They want to yank the knights together and blow them up.
*   **Pre-Roll Profile Resolution:**
    1.  **Tag Interaction (Magnetic):** The bomb has `[Magnetic]`. The GMs check the knights' substance: `Corporeal:Metal`. The `[Magnetic]` tag baseline says: *"Pulls all metal objects/creatures in the zone to the center of the zone, forcing a Bane on their Dodge."*
    2.  **Tag Interaction (Explosive):** The bomb has `[Explosive]`. The baseline says: *"Deals damage to all targets in the zone."*
    3.  **The Cap:** The knights suffer a **Bane (-1d)** to their Dodge check because of the magnetic pull. The scout does not (no metal armor).
*   **The Roll:** The player rolls their bomb attack.
*   **The Result:** The knights are pulled together and take full damage (with a Bane to Dodge). The scout takes standard damage (no Bane). No global lookup was needed—only the bomb's tags and the target's substance.

---

## Stress Test 2: The "Conductive Water Hazard"
*   **The Player Plan:** A wizard casts a `[Wet]` Power Word spell on a stone golem (`Corporeal:Stone`) standing in a puddle. Next round, they shoot it with a `[Shock]` wand.
*   **Pre-Roll Profile Resolution:**
    1.  **Round 1:** The golem is tagged as `[Wet]` (slapped on its profile).
    2.  **Round 2 Attack:** The player attacks with a `[Shock]` weapon.
    3.  **Tag Interaction:** The player checks the weapon tag `[Shock]` against the target's active tags. It sees `[Wet]`.
    4.  **The Rule:** The `[Wet]` + `[Shock]` element synthesis states: *"Conduction: Shakes the target's defenses, making all attack tests against them Easy (4+).'*
*   **The Roll:** The player rolls their attack. Because of conduction, they score successes on 4s, 5s, and 6s.
*   **The Result:** The shock arcs through the water, shattering the golem's defenses. If they hit, the shock arcs to another enemy in the zone.

---

## Stress Test 3: The "Frozen Gravity Hammer"
*   **The Player Plan:** A goblin attacks a charging beast (`Beast`, `Corporeal:Flesh`) using a giant hammer crafted with `[Chilled]` (frost crystal) and `[Crushing]` (gravity coil) traits.
*   **Pre-Roll Profile Resolution:**
    1.  **Base Stats:** Attack uses Tough. Beast has Defence TN 2.
    2.  **Tag vs. Substance/Ancestry (Pre-Roll):**
        *   `[Chilled]`: Reduces target's movement. No Defence modifier.
        *   `[Crushing]`: Massive gravity slows the beast down. The baseline states: *"Makes attacks against the target Easy (4+) due to heavy compression."*
    3.  **Final Roll Profile:** Player rolls their Tough pool against Defence TN 2, with difficulty shifted to **Easy (4+)**.
*   **The Result:** The player hits. The beast takes damage, its movement is reduced to 0, and it is pinned to the ground by gravity.

---

## Stress Test 4: The "Anti-Fey Iron Net"
*   **The Player Plan:** The party is ambushed by a Pixie Queen (`Living:Fey`, `Incorporeal`). The goblin thrower throws a net crafted from cold iron (`[Iron]`) and coated in alchemical glue (`[Sticky]`).
*   **Pre-Roll Profile Resolution:**
    1.  **Base Stats:** Pixie has Defence TN 3. Because it is `Incorporeal`, standard physical net attacks suffer a **Bane (-1d)**.
    2.  **Tag vs. Monster Hooks:**
        *   The net has the `[Iron]` tag. The Pixie's card has: `Flaw Hook: [Iron] (Defence TN becomes 1)`.
        *   The net has `[Sticky]`. The Pixie's card has: `Immune: [Sticky] / Restrained` (due to gaseous form).
    3.  **The Final Profile:** The Defence TN drops from 3 to **1** (due to the Iron flaw). The attack suffers a **Bane (-1d)** (due to Incorporeal substance vs physical net). The sticky glue is ignored.
*   **The Roll:** The player rolls their pool minus 1 die. They need only **1 success** to trap the Pixie Queen.

---

## Conclusion: The Taxonomy Holds

These stress tests prove that:
1.  **Pre-roll calculation is fast:** Modifiers are resolved in a single step before throwing.
2.  **Dynamic tags are self-sufficient:** Players understand their weapons, and GMs resolve interactions using simple, local hooks.
3.  **Extensibility is preserved:** Adding new monsters or tags does not require retrofitting old documents.
