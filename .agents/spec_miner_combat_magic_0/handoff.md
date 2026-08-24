# Handoff Report: Spec Miner 2 (Combat, Mobs, Magic, Enemies, Conditions)

**Agent:** `spec_miner_combat_magic_0`  
**To:** `orchestrator` (`5c381523-2834-4186-bdde-fd176f430709`)  
**Working Directory:** `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\`  
**Date:** 2026-08-24  
**Type:** Hard Handoff (Task Complete)

---

## 1. Observation

Direct observations extracted from the authoritative codebase and draft specifications across `01_STAGE_Drafts/`, `02_PROD_Core_Rules/`, and `00_DEV_Brainstorms/`:

1.  **Mob Health & Frontline Mechanics (`01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md:26-37`):**
    *   Health is tracked via physical d6s equal to Size, starting at face 6.
    *   Single-target damage hits lowest die; excess spills over.
    *   Mob-on-Mob frontline clash engages $\min(\text{Attacker Size}, \text{Defender Size})$ lowest dice simultaneously; unengaged backline dice suffer 0 damage.
    *   `Cleave X` damages up to $X$ lowest dice simultaneously; `[AoE]` damages all active dice simultaneously.
2.  **Mob Command & Loitering vs. Scatter Discrepancy (`01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md:63-79, 96-108` vs `01_STAGE_Drafts/00_Rules/02 Combat.md:48-58`):**
    *   Mobs receive 2 actions per round. Ordered mobs spend 1–2 actions.
    *   Loitering table text verbatim states: `(Uses 1 action. Saves 1 action for 1d6 Defence)`.
    *   Combat rules state: Mobs cannot naturally dodge; active defense is the "Scatter!" reaction using Boss Mouth stat dice against $\text{Threat TN} + (\text{Mob Size} - 1)$, requiring 1 saved Mob action + saved Boss reaction.
    *   Failing a Scatter Gamble deals attack damage + 1 Trample damage to every die in Mob pool + drops 1 Bulk loot + triggers Out of Control + Staggers Boss in same zone.
3.  **Damage, Clatter Roll & Death Loop (`01_STAGE_Drafts/00_Rules/02 Combat.md:38-47`, `01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md:1-12`, `02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md:13-24`):**
    *   Bosses track Grit (3–5 based on Tough). Incoming attacks are deterministic: Threat Profile (`Difficulty+/TN`) and flat Damage.
    *   Clatter Roll resolves active Stat (Slink/Tough) alongside colored Armor Dice: meeting Threat TN = 0 damage; failing triggers Armor Dice (5+ reduces damage by 1); remainder hits Grit.
    *   At 0 Grit, Boss triggers Final Act (1 Easy 4+ Action + 1 Order Action), drops gear, and dies.
4.  **Wounds Track & Overkill Rule (`01_STAGE_Drafts/04_Enemies/20_Enemies.md:105-120`, `01_STAGE_Drafts/04_Enemies/21_Bestiary.md:15-17`):**
    *   Standard enemies are One-Hit Kill ($\text{Successes} \ge \text{Defence TN}$).
    *   Elites and Bosses use a Wounds track (2–8 Wounds).
    *   Overkill Rule verbatim: $\text{Wounds Dealt} = \lfloor \text{Attack Successes} / \text{Defence TN} \rfloor$.
    *   Stagger threshold: Partial hit (at least 1 success, $<$ Defence TN) inflicts Staggered only if $\text{Impact Size} \ge \text{Target Physical Size}$.
5.  **Conditions Matrix (`01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md:17-29`):**
    *   9 official conditions: Weakened, Restrained, Dumb, Silenced, Blinded, Terrified, Stunned, Prone, Staggered.
    *   Staggered automatically clears during Round Closure; environmental conditions clear upon spending 1 Standard Action in a clean zone or at combat end.
6.  **Magic Casting Engine & Contradiction (`01_STAGE_Drafts/08_Magic/00_Magic_Rules.md:11-59`, `00_DEV_Brainstorms/GDRs/GDR-005_Goblin_Magic_Dice_System.md:21-57` vs `02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md:85-96`):**
    *   Casting is a Farkle-style Push-Your-Luck engine rolling Brains pool. Must lock $\ge 1$ success to continue. Pushing and getting 0 new successes triggers Farkle Mishap.
    *   Largest matching set of successes determines Spell Tier (T1 single, T2 pair, T3 triple, T4 quad, T5 quint).
    *   Non-success matching sets trigger Chaotic Leakage (T2 pair, T3 triple).
    *   Contradiction: `00_Magic_Rules.md:13` states Power Word slots equal $\text{Brains} - 1$; `10_Stats.md:85-96` states Brains 1–2 have 0 slots, Level 3 has 2, Level 4 has 4, Level 5 has 6.
    *   Ritual casting is referenced in `00_Rules/08_Master_Tag_Index.md:308, 377` and `03_Loot/34_Crafting.md:153` but completely missing systemic mechanical rules.
7.  **Bangaranga Pool Engine (`02_PROD_Core_Rules/00_Rules/01_Dice.md:51-103`):**
    *   Seeded at raid start (+1d per Boss, +1d per Size 3–4 Mob, +2d per Size 5 Mob).
    *   Loaded by Crits (+1d), Fumbles (+1d), Notable Kills (+1d), Hoard Loot (+1d), Chaos Tick 1s (+1d per 1).
    *   Spend up to Grunt; 1 die tax if dice taken $>$ TN. 6s double explode (add 2 dice). Failing with Bangaranga costs 1 Grunt; 1s drain pool by dice taken.
8.  **Deterministic Enemies & Swarm Terror (`01_STAGE_Drafts/04_Enemies/20_Enemies.md:11-23, 93-143`, `01_STAGE_Drafts/04_Enemies/21_Bestiary.md:21-55`):**
    *   Zero GM rolls. Threat profile + flat damage.
    *   Enemy Mobs scale damage: $\text{Base} + (\text{Size} - 1)$.
    *   50% casualties triggers Morale Check: players roll Swarm Terror pool ($\sum \text{Surviving Mob Sizes} + \sum \text{Surviving Bosses}$) vs static Morale TN.
    *   Three-layer trait hierarchy: Layer 1 Ancestries (Beast, Humanoid, Undead, Monstrosity, Fiend), Layer 2 Tags, Layer 3 Unique Statblock Traits (Max 1 for Standard, Max 2 for Elites/Bosses).

---

## 2. Logic Chain

1.  **From Observation 1 & 2:** Mob mechanics in Gobbos rely on abstract physical dice that scale linearly with Size. The Frontline Rule prevents single-target attacks from wiping entire squads while ensuring that AoE attacks remain terrifyingly lethal. The legacy phrase "1d6 Defence" in the Loitering table is an artifact from an older draft that conflicts with the Clatter Roll and Scatter reaction; it must be standardized to "saves 1 action to enable a Scatter! reaction or passive armor mitigation."
2.  **From Observation 3 & 4:** Combat eliminates all GM rolling by framing incoming monster attacks as static Threat thresholds resolved by player Clatter Rolls. The Overkill Rule cleanly allows single heavy strikes to wound massive bosses without requiring arithmetic damage pools. Impact Size ensures large monsters cannot be cheesed with minor staggers.
3.  **From Observation 5:** Conditions cleanly map to the four main stats (Tough, Slink, Brains, Mouth) plus movement and actions. A single attack or element synthesis is capped at 1 condition to avoid calculation clutter.
4.  **From Observation 6 & 7:** Magic is unified with the Tag system (Power Words are Tags; Effect Tiers are matching sets). The contradiction in Power Word slots is resolved in favor of the authoritative `10_Stats.md` table (Level 3 unlocks 2 slots). The missing Ritual casting mechanics must be formalized as an extended cooperative downtime/exploration mechanic.
5.  **From Observation 8:** Adversary mechanics achieve complete balance between low GM cognitive load and tactical variety via the 3-Layer Trait Hierarchy (Ancestry $\rightarrow$ Tag $\rightarrow$ Unique Trait) and deterministic damage scaling for Enemy Mobs.

---

## 3. Caveats

*   **Living Catalogs:** As per instructions, specific spell compendiums (e.g. 50 distinct spell cards) and full bestiaries (e.g. 30 monster statblocks) were stripped out to formulate pure systemic rules and structural schemas.
*   **Equipment Catalog:** Detailed weapon/armor listings are in the domain of Spec Miner 1 (`spec_miner_gear_0`), but their mechanical hooks (Armor Dice, Cleave X, Impact Size, Weapon Traits) were fully integrated and verified here.
*   **Web Server:** No web server changes or code compilation were executed, in strict compliance with user instructions.

---

## 4. Conclusion

The combat, mob, magic, enemy, and condition systems form a robust, mathematically sound, zero-math TTRPG engine. All 30 discovered features have been cataloged with inputs, outputs, and edge cases. 3 formal content schemas have been designed for extension points:
1.  **Tag Effect / Spell Schema** (`[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]`)
2.  **Enemy & NPC Statblock Schema** (`[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]`)
3.  **Condition & Hazard Schema** (`[CONTENT EXTENSION POINT: Environmental Hazards & Conditions]`)

8 critical mechanical gaps and contradictions were identified and resolved with actionable recommendations for the core rules synthesis in `02_PROD_Core_Rules/`.

---

## 5. Verification Method

To independently verify all findings and extracted mechanics:
1.  **Inspect Analysis Report:** View `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\analysis.md`.
2.  **Verify Mob Frontline & Scatter:** Cross-reference `01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md:26-37` and `01_STAGE_Drafts/00_Rules/02 Combat.md:48-58`.
3.  **Verify Overkill & Enemy Scaling:** Cross-reference `01_STAGE_Drafts/04_Enemies/20_Enemies.md:93-120` and `00_DEV_Brainstorms/GDRs/GDR-004_Enemy_Stat_Framework_And_Mobs.md`.
4.  **Verify Magic Pattern Engine & Slots Contradiction:** Cross-reference `01_STAGE_Drafts/08_Magic/00_Magic_Rules.md:13, 40-59` against `02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md:85-96`.
5.  **Verify Bangaranga Pool Engine:** Cross-reference `02_PROD_Core_Rules/00_Rules/01_Dice.md:51-103`.

**Invalidation Conditions:**
*   Any claim that GMs roll dice in Gobbos invalidates Domain 4 findings.
*   Any claim that Bosses track Wounds instead of Grit invalidates Domain 2 findings.
*   Any claim that Magic uses spell slots or mana points invalidates Domain 3 findings.
