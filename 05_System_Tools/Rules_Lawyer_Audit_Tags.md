# Rules Lawyer Audit: Master Tag Index

**Prepared by:** Rules Lawyer Systems Analyst  
**Target Document:** [08_Master_Tag_Index.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/08_Master_Tag_Index.md)  
**Status:** AUDIT COMPLETED. High-priority exploits and terminology mismatches identified.

---

## 1. Terminology Mismatches & Keyword Enforcement
To maintain mechanical consistency with the rest of the draft rulebook, several terms must be aligned:

*   **"Static Armor Reduction" vs. "Passive Defense Dice":**
    *   *The Issue:* In `[Acidic]` (line 51) and `[Petrified]` (line 327), the text refers to "static Armor reduction" and "static armor reduction." However, the equipment rules in [33_Equipment.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/33_Equipment.md) state that armor grants **Passive Defense** dice (e.g. `+1d Passive Defense`).
    *   *The Fix:* Update `[Acidic]` to: *"Destroys 1 Passive Defense die granted by the target's armor."* Update `[Petrified]` to: *"gains +3 Passive Defense dice."*
*   **"Slashing and Piercing" vs. "Cutting and Poking":**
    *   *The Issue:* In `[Hardened]` (line 243), the text refers to "slashing and piercing weapons." However, the weapon rules in [33_Equipment.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/33_Equipment.md) use the Traits `Cutting` and `Poking`.
    *   *The Fix:* Update `[Hardened]` to: *"against `Cutting` and `Poking` attacks."*
*   **Missing Bold Formats:**
    *   *The Issue:* Standard status effects and stats must be bolded.
    *   *The Fix:* Ensure **Stunned**, **Brains**, **Mouth**, **Slink**, **Tough**, **Fumble**, **Successes**, and **Zone** are bolded in all tag descriptions.

---

## 2. Exploits & Infinite Loops

*   **`[Bouncy]` (Line 103) Infinite Miss Loop:**
    *   *The Loop:* As written: *"If a ranged attack using this tag misses, the projectile bounces, making an immediate attack check..."* If the second attack also misses, it triggers another bounce, theoretically leading to infinite rolls on a bad streak.
    *   *The Fix:* Append: *"A projectile can only bounce once per attack."*
*   **`[Linked]` (Line 315) Stack Overflow Loop:**
    *   *The Loop:* If Creature A is linked to Creature B, and Creature B is linked to Creature A, a single point of damage will bounce back and forth infinitely, vaporizing both instantly.
    *   *The Fix:* Append: *"Damage or conditions mirrored by `[Linked]` cannot trigger further `[Linked]` mirrors."*

---

## 3. Ambiguities & GM Interpretation Hazards

*   **`[Shock]` (Line 69) and `[Spiky]` (Line 271) vs. Standard Enemies:**
    *   *The Ambiguity:* These tags deal "1 automatic Grit/Size damage." Standard enemies do not have Grit or Size pools (they are one-hit-kill).
    *   *The Fix:* Clarify that against standard enemies, these deal **1 automatic success** (which meets their Defence TN of 1 and instantly defeats them).
*   **`[Deafening]` (Line 172) vs. Orders:**
    *   *The Ambiguity:* The baseline states the target is immune to "verbal Mouth/Order actions," but doesn't explain the mechanical impact on a Mob.
    *   *The Fix:* Clarify that a deafened Mob **cannot receive Orders** from their Boss.
*   **`[Shiny]` (Line 197) vs. Player Goblins:**
    *   *The Ambiguity:* The baseline targets "greed-obsessed minds." Goblins are notoriously greed-obsessed.
    *   *The Fix:* Explicitly state that this includes player-character Goblins to prevent players from ignoring their own traps.
*   **`[Frenzied]` (Line 236) Out of Melee Range:**
    *   *The Ambiguity:* The baseline forces targets to attack the nearest creature in melee range. If there is no one in melee range, the rules are silent.
    *   *The Fix:* Clarify that the target must spend all actions moving toward the nearest creature to attack them.
*   **`[Puppet]` (Line 257) Action Cost:**
    *   *The Ambiguity:* It states "the caster can spend 1 action" but does not define if it is a Standard Action.
    *   *The Fix:* Clarify: *"The caster spends 1 Standard Action on their turn..."*
*   **`[Poofed]` (Line 330) Tele-Fragging:**
    *   *The Ambiguity:* The target returns "in the same spot." If that spot is occupied, they would "tele-frag" the occupier.
    *   *The Fix:* Clarify: *"If the spot is occupied when they return, they appear in the nearest unoccupied space."*
*   **`[Serene]` (Line 345) Cost to Override:**
    *   *The Ambiguity:* States characters must spend "Grunt or Grit" to override, but does not specify a value.
    *   *The Fix:* Specify: *"must spend 1 Grunt or 1 Grit to perform a violent action."*
