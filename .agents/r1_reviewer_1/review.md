# Review Report: Gobbos Core Rules Synthesis (Chapters 01–06)

**Reviewer**: Reviewer 1 (`r1_reviewer_1`) — Roles: Reviewer & Adversarial Critic  
**Date**: 2026-08-24  
**Target Repository**: `02_PROD_Core_Rules/` (Chapters 01 to 06)  
**Mandatory Inputs**: `ORIGINAL_REQUEST.md`, `GEMINI.md`, `PROJECT.md`  

---

## Executive Summary

| Dimension | Assessment | Status |
| :--- | :--- | :---: |
| **Integrity & Authenticity** | Zero hardcoding, zero facade implementations, zero bypasses | **PASS** |
| **Engine vs Content Separation** | Catalogs stripped; formal schemas & `[CONTENT EXTENSION POINT]` tags embedded | **PASS** |
| **Single-Source Authority** | Single definitive rules; valid markdown cross-references across chapters | **PASS** |
| **Mechanical Gap Auditing** | Standardized `[MISSING RULE / GAP]` tags with rationale and suggested resolution | **PASS** |
| **Slash Notation & Math** | Strict `[Stat] [Face]+/[TN]` notation; zero illegal `6+` notation | **PASS** |
| **Structural Hierarchy** | Clean semantic hierarchy (`#` -> `##` -> `###` -> `####`) with zero level skips | **PASS** |
| **Style & Linguistic Strictness** | Total de-gendering largely achieved; minor instances of singular "they" and synonym drift | **MINOR EDITS** |

**Final Verdict**: **APPROVE** (with minor editorial punch-list for subsequent refinement pass)

---

## Detailed Section Evaluations

### 1. Engine vs. Content Separation & Extension Schemas
All six chapters strictly isolate pure systemic rules from living content catalogs. No living weapon tables, monster bestiaries, or full quirk lists are present. All four required structural schemas and content extension hooks are formally defined:
*   `02_Boss_Profile_and_Gang.md` (lines 280–298): **Quirk Structural Schema** & `[CONTENT EXTENSION POINT: Boss Quirks & Talents]`
*   `05_Combat_Engine.md` (lines 143–161): **Formal Weapon Structural Schema** & `[CONTENT EXTENSION POINT: Weapons]`
*   `05_Combat_Engine.md` (lines 192–208): **Formal Armor & Shield Structural Schema** & `[CONTENT EXTENSION POINT: Armor & Shields]`
*   `05_Combat_Engine.md` (lines 234–249): **Formal Gear, Tools & Consumables Schema** & `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`

### 2. Single-Source Authority & Cross-References
*   Every core mechanic is authoritatively defined in a single primary location and cross-referenced with standard relative Markdown links (e.g. `[Mob Mechanics](06_Mob_Mechanics.md)`, `[Action Economy & Turn Flow](03_Action_Economy_and_Turn_Flow.md)`, `[Damage, Grit & Wounds](07_Damage_Grit_and_Wounds.md)`).
*   No conflicting rules or duplicated variant rules exist between chapters.
*   The Action Economy (3 Standard Actions + Free Orders for Bosses; 2 Actions with Boredom Rule for Mobs) matches identically across Chapters 02, 03, 05, and 06.
*   The Clatter Defense roll, Impact Size/Stagger calculation, and Frontline Rule resolve deterministically with zero GM dice rolls.

### 3. Mechanical Gap Analysis
All 12 identified system gaps are tagged with the standardized format:
`[MISSING RULE / GAP: <Description of missing mechanic, why it is needed, and suggested resolution>]`.
*   **Chapter 01 (Core Resolution)**:
    *   *Line 85*: Bangaranga Multi-Explosion Critical Cascade Definition.
    *   *Line 206*: Unified Opposed & Resistance Test Mechanics.
*   **Chapter 02 (Boss Profile & Gang)**:
    *   *Line 212*: Weapon Damage Metric & Loadout Notation Discrepancy.
    *   *Line 214*: Dual-Wielding Melee Weapons.
*   **Chapter 03 (Action Economy & Turn Flow)**:
    *   *Line 100*: Free Order Action Permissibility in Self-Defense Reactions.
    *   *Line 211*: Disengage Failure & Opportunity Attack Resolution.
*   **Chapter 04 (Zones & Movement)**:
    *   *Line 191*: Vertical Zone Height and Fall Damage Scaling.
    *   *Line 193*: Zone Capacity Limits for Giant Adversaries.
*   **Chapter 05 (Combat Engine)**:
    *   *Line 313*: Dual-Wielding Light Melee Weapons.
    *   *Line 315*: Ranged Weapon Ammunition Tracking and Depletion.
*   **Chapter 06 (Mob Mechanics)**:
    *   *Line 236*: Mob Weapon Equipping & Scaling Rules.
    *   *Line 238*: Maximum Swarm Terror Pool Ceiling.

### 4. Style, Notation & Formatting Compliance
*   **Slash Notation**: Evaluated across all 6 files. Zero occurrences of `6+` (Hard difficulty is written strictly as `6`).
*   **Header Hierarchy**: Evaluated line-by-line. 100% compliant (`#` -> `##` -> `###` -> `####`) with zero level skips.
*   **Golden Rules & Examples**: Golden rules use `>>` callouts, and examples use `> **Example:**` markdown blockquotes.

---

## Adversarial Review & Stress-Testing

### Challenge 1: The 0-Grunt Specialist Trap
*   **Assumption**: A Specialist Boss (Stats: 3/1/1/1) starts with **Max Grunt = 1**. If they fumble or fail a Bangaranga test, their Current Grunt drops to **0**.
*   **Stress Scenario**: When at 0 Grunt, the Boss's Current Grunt is strictly less than their starting Size 1 Mob. Under `02_Boss_Profile_and_Gang.md:137`, attempting to issue any command forces a **Rebellion Test** (`Tough or Mouth 5+/1`). If they fail, their only Mob becomes Out of Control. If they attempt **Assert Dominance** (`02_Boss_Profile_and_Gang.md:142`) to regain Grunt, dealing 1 damage to a Size 1 Mob with 1 health point kills the Mob outright.
*   **Blast Radius**: Moderate early-game friction for low-Mouth Specialist Bosses.
*   **Assessment & Mitigation**: This creates authentic, humorous goblin desperation and encourages generalist stat builds or careful Grunt management. The rules are mechanically sound and self-contained.

### Challenge 2: Clatter Roll Passive Armor Stacking vs Invulnerability
*   **Assumption**: Stacking Heavy Armor (+3d), Shield (+1d), and High Slink Passive Defence (+2d) could yield 6d mitigation dice, reducing even Boss-level threats to 0 damage.
*   **Stress Scenario**: A max-Slink Boss wearing Heavy Armor rolls 6d on every incoming attack.
*   **Mitigation in Place**: `05_Combat_Engine.md:179` explicitly codifies **The 5d Mitigation Ceiling** (`>> THE 5D MITIGATION CEILING: The total passive mitigation pool rolled on any single Clatter Roll ... is hard-capped at 5d6 Armor Dice`). This guarantees attacks with 6+ Damage will always penetrate.

### Challenge 3: Mob Frontline vs Multi-Cleave Cascades
*   **Assumption**: Large enemy groups dealing Cleave damage could wipe out multiple health dice simultaneously.
*   **Stress Scenario**: An enemy with `Cleave 3` strikes a Size 4 Mob (`[6, 4, 2, 1]`) dealing 2 damage.
*   **Resolution Verified**: Damage applies simultaneously to up to 3 lowest dice (`[1]`, `[2]`, `[4]`). `[1]` and `[2]` are removed; `[4]` is reduced to 2. Die `[6]` is untouched. Clear, deterministic, and fast at the table without arithmetic accumulation.

---

## Findings & Editorial Punch-List

### Minor Finding 1: Singular "They/Their" Instances
*   **Rule Reference**: `GEMINI.md` Section 3 ("Total De-Gendering: gendered pronouns and singular 'they' are entirely banned. Use Direct Second-Person Address (You/Your) or Explicit Imperative Nouns").
*   **Identified Locations**:
    *   `01_Core_Resolution.md:106`: "...doubling down on their worst dice" -> "...doubling down on the player's worst dice" / "...doubling down on your worst dice".
    *   `01_Core_Resolution.md:175`: "...to add to their active dice pool" -> "...to add to the active dice pool" / "...to add to your active dice pool".
    *   `02_Boss_Profile_and_Gang.md:3`: "...clawed their way..." -> "...clawed a path to the top..."
    *   `02_Boss_Profile_and_Gang.md:274`: "...indulges their Shenanigan..." -> "...indulges a Shenanigan..."
    *   `03_Action_Economy_and_Turn_Flow.md:3`: "...who spends their momentum wisely..." -> "...who spends momentum wisely..."
    *   `04_Zones_and_Movement.md:52, 53, 62, 63, 83, 106, 112, 144`: Replace occurrences of "their/them" referring to a single creature/Boss/unit with direct address ("your") or imperative nouns ("the Goblin Boss's", "the creature's").
    *   `05_Combat_Engine.md:35, 57, 119, 183, 282, 283`: Replace "their Tough stat", "their Slink stat", "reduce their Grit" with "the Boss's Tough stat" / "your Tough stat", etc.

### Minor Finding 2: Keyword Constancy (Grit vs Health / Hit Points)
*   **Rule Reference**: `GEMINI.md` Section 3 ("Grit vs. Health: Player hit points are strictly Grit. Never refer to a PC's survival tracker as health, hit points, or stamina").
*   **Identified Locations**:
    *   `02_Boss_Profile_and_Gang.md:34`: `Grit (Health Capacity: 3 to 5)` -> `Grit (Capacity: 3 to 5)`
    *   `02_Boss_Profile_and_Gang.md:53`: `Grit (Health Capacity)` -> `Grit (Capacity)`
    *   `02_Boss_Profile_and_Gang.md:61`: "Your Boss's hit point capacity." -> "Your Boss's survival capacity."

### Minor Finding 3: Keyword Constancy (Mob vs Squad / Unit)
*   **Rule Reference**: `GEMINI.md` Section 3 ("Mob vs. Squad/Unit: A collection of lesser goblins under a player's command is exclusively a Mob. Never call them a squad, swarm, group, or unit").
*   **Identified Locations**:
    *   `06_Mob_Mechanics.md:9`: "...an abstract squad of lesser goblins..." -> "...an abstract collective of lesser goblins..."
    *   `06_Mob_Mechanics.md:36`: "...squad's carrying capacity..." -> "...Mob's carrying capacity..."
    *   `06_Mob_Mechanics.md:39`: "...every runt in the squad..." -> "...every runt in the Mob..."
    *   `06_Mob_Mechanics.md:45`: "Shared Expedition Tools: Squad tools..." -> "Shared Expedition Tools: Mob tools..."
    *   `06_Mob_Mechanics.md:99`: "...(or a portion of the squad)..." -> "...(or a portion of the Mob)..."
    *   `06_Mob_Mechanics.md:204, 206, 209`: "two smaller squads", "both squads", "merged into a single squad" -> "two smaller Mobs", "both Mobs", "merged into a single Mob".

### Minor Finding 4: Keyword Constancy (Loot vs Treasure)
*   **Rule Reference**: `GEMINI.md` Section 3 ("Loot & Loot Value: When discussing the tangible mechanic of treasure value, it must always be called Loot or Loot Value").
*   **Identified Location**:
    *   `03_Action_Economy_and_Turn_Flow.md:170`: "...visible treasure caches." -> "...visible **Loot** caches."

---

## Conclusion & Next Steps

The synthesized rules in Chapters 01–06 are robust, cohesive, mathematically elegant, and faithfully implement the zero-math, high-chaos vision of the Gobbos TTRPG. 
*   **Verdict**: **APPROVE**
*   **Actionable Recommendation**: The author/editor should apply the minor editorial punch-list during the final polishing pass to ensure 100% keyword and de-gendering compliance.
