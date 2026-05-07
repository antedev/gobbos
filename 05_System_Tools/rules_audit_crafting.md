# Rules Lawyer Audit: Crafting Framework Brainstorm
**Target:** `00_DEV_Brainstorms/crafting_framework_brainstorm.md`

## 1. The Sling / Zero-Dice Exploit
**The Loophole:** `33_Equipment.md` states that Slings, Throwing Axes, and Throwing Daggers grant `+0d` Damage. The proposed Crafting Framework relies on gear breaking when rolling a `1` on the **Gear Dice**.
*   **The Exploit:** If a Base Item has `+0d`, you roll no gear dice. Therefore, you can **never** roll a 1 on a gear die. A player can attach 5 Oddities to a Sling and create an infinitely durable, god-tier weapon that never breaks.
*   **The Fix:** You must introduce a single "Quality Die" rolled alongside the attack, regardless of extra gear dice. Or, base the break chance on the base action dice pool instead of the gear dice.

## 2. The Heavy Weapon Paradox
**The Loophole:** Currently, gear breaks if a 1 is rolled on *any* gear die (e.g., "Breaks on 1-2 on the gear dice"). Light Weapons give `+2d`, Heavy Weapons give `+4d`. 
*   **The Exploit (Self-Sabotage):** By rolling 4 dice, a Heavy Weapon is mathematically twice as likely to shatter in your hands as a Light Weapon. If a player puts 2 Oddities on a Heavy Weapon (breaking on 1-3), rolling 4 dice means it has a massive **93.75% chance of destroying itself** on its very first swing. Players will mathematically realize that crafting is only viable on Light Weapons.
*   **The Fix:** Change the breaking threshold so it only triggers if the *overall action is a Fumble*, or use a dedicated single Quality Die (e.g., roll 1d6 of a different color: 1 = break). 

## 3. The Utility Slot Encumbrance Clash
**The Loophole:** `10_Stats.md` states that Utility Slots are for "carrying Magic Words or Contraptions *without consuming standard Bulk*." The Brainstorm suggests spending Utility Slots to attach Oddities to weapons. 
*   **The Exploit:** If a player has a Heavy Weapon (Bulk 3) and attaches an Oddity to it (costing a Utility Slot), does the entire weapon become a "Contraption" and therefore consume 0 Bulk? If so, players will attach Oddities to heavy armor and weapons to bypass the Carry Capacity limits entirely.
*   **The Fix:** Decouple Oddities from Utility Slots. Rule explicitly: "You can attach a maximum number of Oddities to a single item equal to your Brains stat. Oddities do not cost Utility Slots. The combined item maintains its original Bulk (unless an Oddity explicitly states otherwise, like 'Floaty' or 'Heavy')."

## 4. Keyword and Terminology Consistency
**The Mismatches:**
*   *"passive defense dice"* in the Draft should be capitalized exactly as **Passive Defence Dice** (`10_Stats.md`).
*   *"Screeching Whistle: Forces a morale/rout test on Mobs."* There is no formal "rout" test defined. Replace with: "Forces the Mob to take a Grunt test, or they rebel." (`10_Stats.md` mentions rebels/Grunt tests).
*   *"Chilling Frost-Stone: loses 1 action next turn due to shivering."* Replace narrative shivering with formal mechanics: "The target gains the **Fatigued** condition (-1d on all tests)." (`07_Wounds_Conditions.md`).
*   *"Venom Gland: Deals damage over time."* Needs integration with the **Poisoned** keyword in `07_Wounds_Conditions.md`.
*   *"Spiked Carapace: 1 bleeding wound."* Needs to map directly to a formal Condition or explicitly state `-1 Grit`.

## Summary Judgment
The framework succeeds at being fast and containing post-roll math. However, relying on **Gear Dice** for durability logic fundamentally breaks math when players have 0 gear dice or too many gear dice. Moving to a dedicated **Quality Die** (one separate d6 rolled with the pool) fixes all mathematical exploits instantly.
