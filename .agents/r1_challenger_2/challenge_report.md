# ADVERSARIAL CHALLENGE REPORT: GOBBOS CORE RULES SYNTHESIS

**Challenger**: Challenger 2 (Empirical Reviewer / Rules Lawyer & Layout Specialist)  
**Date**: 2026-08-24T19:50:00Z  
**Target**: `02_PROD_Core_Rules/` (All 12 synthesized chapters: `01_Core_Resolution.md` to `12_Adversaries_and_Threats.md`)  
**Interface Contracts**: `GEMINI.md`, `ORIGINAL_REQUEST.md`

---

## 1. Executive Summary & Verdict

**Overall Risk Assessment**: **MEDIUM**  
**Final Verdict**: **`CHALLENGE_DETECTED`**

### Summary of Audit Dimensions:
| Dimension | Status | Summary Findings |
|---|---|---|
| **1. Style & Slash Notation Audit** | **PASS (100%)** | Zero instances of invalid `6+`. All dice checks strictly adhere to `[Stat] [Face]+/[TN]` (or `[Face]/[TN]` for 6). |
| **2. Header Hierarchy Audit** | **PASS (100%)** | Strict `# H1` $\to$ `## H2` $\to$ `### H3` $\to$ `#### H4` sequence maintained across all 12 chapters with zero skips. |
| **3. De-gendering & Anti-Clunk Audit** | **CHALLENGE DETECTED** | Zero gendered pronouns (`he`, `she`, `him`, `her`, `his`, `hers`) in any of the 12 chapters. However, singular `they/their/them/themselves` instances exist on singular entities (`a goblin`, `a Goblin Boss`, `The player`, `a creature`, `a character`, `The Lead Caster`). |
| **4. Keyword Constancy & Synonym Audit** | **CHALLENGE DETECTED** | Concrete violations found: (a) PC Bosses suffering "Wounds" instead of Grit damage in Chapters 10 and 11; (b) "squad" used for player Mobs in Chapter 06; (c) "treasure caches" used in Chapter 03. |
| **5. Extension Points & Gaps** | **PASS (100%)** | Formal schemas, `[CONTENT EXTENSION POINT: ...]` blocks, and `[MISSING RULE / GAP: ...]` markers are properly formatted and integrated. |

---

## 2. Detailed Empirical Audit Findings

---

### Audit 1: Style & Dice Slash Notation (`[Stat] [Face]+/[TN]`)

**Standard**: `GEMINI.md` mandates that all checks use `[Stat] [Target Face]+/[Required Successes]`, with NO `+` on target 6 (e.g., `Brains 6/2`, `Tough 4+/1`, `Slink 5+/2`).

**Empirical Findings**:
1. **Target 6 Notation**:
   - Exactly zero instances of `6+` used in rules or check statblocks across the 12 chapters.
   - The only match for `6+` in the entire codebase is in `01_Core_Resolution.md:40`, explicitly stating the golden rule:
     > `>> **IMPORTANT:** The numeral **6** represents the absolute ceiling on a standard d6. In accordance with official system notation, **Hard** difficulty is written strictly as **6** (never write `6+`).`
   - Every hard difficulty test correctly uses `6/1` or `6/2` (e.g., `01_Core_Resolution.md:52` `Brains 6/2`, `04_Zones_and_Movement.md:15` `[Narrow] [6/1]`, `11_Journeys_and_Hazards.md:207` `Brains 6/2`).
2. **Target 4 and 5 Notation**:
   - Zero missing `+` on faces 4 and 5 in checks across all 12 chapters.
   - All tests properly formatted as `4+/1`, `4+/2`, `5+/1`, `5+/2`, or `5+/Size`.

**Verdict on Notation**: **PASSED (100% COMPLIANT)**

---

### Audit 2: Header Hierarchy Audit (`#` $\to$ `##` $\to$ `###` $\to$ `####`)

**Standard**: Semantic header hierarchy without skipping levels (H1 $\to$ H2 $\to$ H3, never H1 $\to$ H3 or H2 $\to$ H4).

**Empirical Findings**:
- Every chapter contains exactly one `# H1` top-level title.
- Every section follows strict monotonic descending and ascending header levels:
  - `01_Core_Resolution.md`: H1 $\to$ H2 $\to$ H3 $\to$ H2 $\to$ H3 (0 skips)
  - `02_Boss_Profile_and_Gang.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)
  - `03_Action_Economy_and_Turn_Flow.md`: H1 $\to$ H2 $\to$ H3 $\to$ H2 $\to$ H3 (0 skips)
  - `04_Zones_and_Movement.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)
  - `05_Combat_Engine.md`: H1 $\to$ H2 $\to$ H3 $\to$ H2 $\to$ H3 (0 skips)
  - `06_Mob_Mechanics.md`: H1 $\to$ H2 $\to$ H3 $\to$ H2 $\to$ H3 (0 skips)
  - `07_Damage_Grit_and_Wounds.md`: H1 $\to$ H2 $\to$ H3 $\to$ H2 $\to$ H3 (0 skips)
  - `08_Magic_and_Bangaranga.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)
  - `09_The_Raid_Loop.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)
  - `10_The_Lair_Loop_and_Progression.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)
  - `11_Journeys_and_Hazards.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)
  - `12_Adversaries_and_Threats.md`: H1 $\to$ H2 $\to$ H3 $\to$ H4 $\to$ H2 $\to$ H3 (0 skips)

**Verdict on Header Hierarchy**: **PASSED (100% COMPLIANT)**

---

### Audit 3: Keyword Constancy & Synonym Audit

**Standard**: `GEMINI.md` strict keyword constancy rules:
1. **Grit vs. Health vs. Wounds**: PC Goblin Bosses track **Grit** (3 to 5 points). PC Bosses never track *Health* or *Wounds*. **Health / Health Dice** belongs exclusively to **Mobs**. **Wounds** belong exclusively to **Elite / Boss Adversaries**.
2. **Mob vs. Squad/Unit**: A collection of lesser goblins under a player's command is exclusively a **Mob**. Never call them a *squad*, *swarm*, *group*, or *unit* (unless explicitly utilizing indexed exceptions like **Enemy Swarm** or **Group Attack**).
3. **Loot vs. Generic Treasure**: Tangible treasure value is strictly **Loot** or **Loot Value**.

**Empirical Challenges Detected**:

#### Challenge 3.1 [HIGH]: PC Bosses inflicted with "Wounds" in Hazards & Lair Rules
- **Observation 1**: `10_The_Lair_Loop_and_Progression.md`, Line 326:
  `2. Tyrant's Beatdown: A Boss makes an opposed Tough 5+/2 or Mouth 5+/2 test as a Downtime Action... failure inflicts 1 Wound on the Boss and increases Threat by +1 from the riot.`
  *Issue*: "inflicts 1 Wound on the Boss" directly contradicts `07_Damage_Grit_and_Wounds.md:17` and `07_Damage_Grit_and_Wounds.md:198`, which state that PC Bosses never track Wounds.
  *Remediation*: Change to `failure inflicts 1 damage to the Boss's Grit`.
- **Observation 2**: `11_Journeys_and_Hazards.md`, Line 118:
  `*Rule:* Test Slink against the Zone Profile or suffer 1 Wound (Boss) / 1 Size damage (Mob).`
  *Issue*: "suffer 1 Wound (Boss)" violates the keyword rule.
  *Remediation*: Change to `suffer 1 damage to Grit (Boss) / 1 Size damage (Mob)`.
- **Observation 3**: `11_Journeys_and_Hazards.md`, Line 133:
  `*Rule:* ...drowning (1 Wound per round).`
  *Remediation*: Change to `drowning (1 damage to Grit or lowest Mob health die per round)`.
- **Observation 4**: `11_Journeys_and_Hazards.md`, Line 147:
  `*Rule:* ...take 1 Wound...`
  *Remediation*: Change to `take 1 damage to Grit or lowest Mob health die`.

#### Challenge 3.2 [MEDIUM]: Use of "Squad" for Player Mobs in Chapter 06
- **Observation**: `06_Mob_Mechanics.md` contains multiple references to player Mobs as "squad" or "squads":
  - Line 9: `A Mob is an abstract squad of lesser goblins...` $\to$ Change to `A Mob is a collective mob of lesser goblins...`
  - Line 17: `| Runts Squad | 1 | 1d6 | 1 | 4 Bulk |` $\to$ Change to `| Runt Mob | 1 | 1d6 | 1 | 4 Bulk |`
  - Line 36: `...consumes the squad's carrying capacity.` $\to$ Change to `...consumes the Mob's carrying capacity.`
  - Line 39: `...every runt in the squad.` $\to$ Change to `...every runt in the Mob.`
  - Line 45: `Squad tools (such as Ropes...` $\to$ Change to `Mob tools (such as Ropes...`
  - Line 99: `...(or a portion of the squad)...` $\to$ Change to `...(or a portion of the Mob)...`
  - Line 204: `...split a Mob into two smaller squads:` $\to$ Change to `...split a Mob into two smaller Mobs:`
  - Line 206: `...(both squads retain the armor tier)... assigned to one of the split squads.` $\to$ Change to `...(both Mobs retain the armor tier)... assigned to one of the split Mobs.`
  - Line 209: `...merged into a single squad...` $\to$ Change to `...merged into a single Mob...`

#### Challenge 3.3 [LOW]: Minor Drift to "treasure caches" in Chapter 03
- **Observation**: `03_Action_Economy_and_Turn_Flow.md`, Line 170:
  `3. Objective Declaration: The GM declares active Raid Point objectives and visible treasure caches.`
  *Remediation*: Change to `visible Loot caches`.

---

### Audit 4: De-gendering & Anti-Clunk Audit

**Standard**: `GEMINI.md` mandates total de-gendering:
- Complete ban on gendered pronouns (`he`, `she`, `him`, `her`, `his`, `hers`).
- Complete ban on singular `they/their/them/themselves` for players/characters.
- Required replacements: Second person **You / Your** or explicit nouns (**The Goblin Boss**, **The Mob**, **The GM**, **The Player**).

**Empirical Findings**:
1. **Gendered Pronouns**: **ZERO (0) instances** of `he`, `she`, `him`, `her`, `his`, `hers`, `himself`, `herself` found across all 12 chapters. (100% compliant).
2. **Inanimate & Plural Pronouns**: Plural nouns (e.g. `Players`, `Enemies`, `Runts`, `items`, `dice`, `conditions`) use `they/them/their/themselves`, which is grammatically standard.
3. **Singular "They/Their/Them" Instances (Violations of Anti-Clunk Rule)**:
   - `01_Core_Resolution.md:106`: `When an initial roll fails, a goblin can push luck by doubling down on their worst dice.` $\to$ Fix: `...by doubling down on your worst dice.`
   - `01_Core_Resolution.md:175`: `Before rolling any test, a Goblin Boss may draw dice from the Bangaranga Pool to add to their active dice pool:` $\to$ Fix: `...to add to your active dice pool:`
   - `02_Boss_Profile_and_Gang.md:274`: `Whenever a player willingly indulges their Shenanigan...` $\to$ Fix: `Whenever you willingly indulge your Shenanigan...`
   - `03_Action_Economy_and_Turn_Flow.md:100`: `...whether an unused Free Order can be spent by the Boss to Dodge or Parry for themselves.` $\to$ Fix: `...for the Boss's own person.`
   - `04_Zones_and_Movement.md:52`: `...up to their Movement rating:` $\to$ Fix: `...up to its Movement rating (for Mobs) or your Movement rating (for Bosses):`
   - `04_Zones_and_Movement.md:53`: `...derived from their Slink stat...` $\to$ Fix: `...derived from the Boss's Slink stat...`
   - `04_Zones_and_Movement.md:106`: `...and their movement ends immediately.` $\to$ Fix: `...and movement ends immediately.`
   - `04_Zones_and_Movement.md:112`: `...declare they are ducking behind a pillar...` $\to$ Fix: `...declare ducking behind a pillar...`
   - `04_Zones_and_Movement.md:115`: `...they salvage an improvised throwing weapon...` $\to$ Fix: `...the character salvages an improvised throwing weapon...`
   - `04_Zones_and_Movement.md:144`: `When a player chooses to split their forces...` $\to$ Fix: `When you choose to split your forces...`
   - `05_Combat_Engine.md:35 & 57`: `The attacking Goblin Boss rolls a dice pool equal to their Tough/Slink stat:` $\to$ Fix: `...equal to the Boss's Tough/Slink stat:`
   - `05_Combat_Engine.md:119`: `When a player Fumbles a test using a weapon, they roll a 1d6 Break Roll:` $\to$ Fix: `When you Fumble a test using a weapon, roll a 1d6 Break Roll:`
   - `05_Combat_Engine.md:183`: `...reduce their Grit to 0...` $\to$ Fix: `...reduce the Boss's Grit to 0...`
   - `05_Combat_Engine.md:282`: `...actions on their active turn...` $\to$ Fix: `...actions on the Boss's active turn...`
   - `05_Combat_Engine.md:283`: `The player rolls their active Stat Dice...` $\to$ Fix: `The player rolls active Stat Dice...`
   - `06_Mob_Mechanics.md:156`: `...on their turn...` $\to$ Fix: `...on the Boss's turn...`
   - `06_Mob_Mechanics.md:170`: `...rolls a dice pool equal to their Mouth stat.` $\to$ Fix: `...equal to the Boss's Mouth stat.`
   - `08_Magic_and_Bangaranga.md:172`: `...supercharge their magical channeling:` $\to$ Fix: `...supercharge your magical channeling:`
   - `08_Magic_and_Bangaranga.md:210`: `The Lead Caster may draw up to their Grunt...` $\to$ Fix: `The Lead Caster may draw up to Grunt...`
   - `10_The_Lair_Loop_and_Progression.md:348`: `...attune to exactly 1 Patron Saint from their Gang's Bone Pile...` $\to$ Fix: `...from the Gang's Bone Pile...`

---

## 3. Recommended Remediation Plan

To bring the synthesized core rules to 100% perfection, apply the following surgical adjustments:

1. **Fix Keyword Drift in Chapters 10 and 11**:
   - Replace "Wound (Boss)" / "1 Wound on the Boss" with "1 damage to Grit (Boss)" in `10_The_Lair_Loop_and_Progression.md:326` and `11_Journeys_and_Hazards.md:118, 133, 147`.
2. **Purge "Squad" in Chapter 06**:
   - Replace all 9 occurrences of "squad/squads" in `06_Mob_Mechanics.md` with "Mob/Mobs".
3. **Purge Singular "They/Their"**:
   - Replace singular "they/their/them/themselves" with second person ("you/your") or explicit nouns ("the Boss's", "the Mob's").

---

## 4. Conclusion

The synthesized 12-chapter core rules are exceptionally well structured, mathematically rigorous, and strictly adhere to dice slash notation and header hierarchy. Addressing the minor keyword drift (Boss Wounds, Mob Squad) and singular pronouns will make `02_PROD_Core_Rules/` 100% watertight.
