# Changes Summary — Worker 1 (Core Rules Synthesis: Chapters 01, 02, 03)

**Author**: Worker 1 (`.agents/m1_core_worker_0/`)  
**Scope**: Core Resolution, Boss Profile & Gang, Action Economy & Turn Flow  
**Date**: 2026-08-24  

---

## 1. Files Written

1. `02_PROD_Core_Rules/01_Core_Resolution.md`
   - **Domain**: Core Resolution & Dice Pool Engine
   - **Key Mechanics Codified**:
     - Standard d6 exclusivity and player-facing resolution (GM never rolls).
     - Dice pool assembly: Base Stat / Mob Size + Boons - Banes + Bangaranga dice.
     - Difficulty thresholds (Easy 4+, Normal 5+, Hard 6) and Target Number (TN) required successes.
     - Strict slash notation: `[Stat] [Target Face]+/[Successes]` (never `6+`).
     - Recursive exploding 6s and Critical Success double explosions (+1 Grunt & 1 Free non-offensive Action).
     - Zero dice pool Salvage Roll (1d6: 6=Success, 1=Fumble & -1 Grunt, 2-5=Fail).
     - Gobbo Gamble (rerolling 1s on failed tests; failing again triggers Fumble and -1 Grunt).
     - Boons (+1d) and Banes (-1d) with the 1-to-1 cancellation and Net Cap rule (+/-1d max situational modifier).
     - The Bangaranga Pool Engine: Party composition seeding, Hype triggers (+1d6), Tapping up to Grunt, Bangaranga Tax (1 discarded die if draw > TN), Double Exploding 6s (explodes into 2 regular dice), and Overreaching fail penalties & drain.
     - Static resistance profiles for GM/adversary interactions.
   - **Gaps Flagged**:
     - `[MISSING RULE / GAP: Bangaranga Multi-Explosion Critical Cascade Definition]`
     - `[MISSING RULE / GAP: Unified Opposed & Resistance Test Mechanics]`

2. `02_PROD_Core_Rules/02_Boss_Profile_and_Gang.md`
   - **Domain**: Attributes, Boss Profile & Gang Fundamentals
   - **Key Mechanics Codified**:
     - Four Main Stats (Tough, Slink, Mouth, Brains) scaling Level 1 to Level 5 (Level 6 = Elder retirement).
     - Eight derived Secondary Stats with complete progression tables:
       - Tough: Grit (3, 4, 4, 5, 5) & Carry (6, 8, 10, 12, 14 Bulk) + Over-Laden rule.
       - Slink: Movement (2, 3, 3, 4, 5 Zones) & Passive Defence (0d, 0d, 1d, 1d, 2d mitigation dice).
       - Mouth: Max Mobs (1, 2, 2, 3, 3) & Free Orders per Round (1, 1, 2, 2, 3).
       - Brains: Power Words (0, 0, 2, 4, 6 spell slots) & Crafting Capacity (1, 2, 3, 4, 5 oddity slots).
     - Grunt engine: Max Grunt = Second-highest Main Stat; dynamic tracking (0 to Max Grunt); gaining Grunt (+1) and losing Grunt (-1).
     - Mob Command Limits ($\text{Mob Size} \le \text{Current Grunt}$) and Rebellion Test (`Tough/Mouth 5+/Size`).
     - Assert Dominance action (1 Standard Action undefended strike against own Mob).
     - Sequential 5-Step Boss Creation Engine: Base 1s, 2 points allocation (Specialist 3/1/1/1 vs Generalist 2/2/1/1), derived stats, 1 starting Basic Quirk, Junk (T1) loadout.
     - The Gang as Class Archetype: Infamy Track (Levels 1–5), Infamy Marks (10 Loot Value / Gang Agendas), Successor Boss Generation (Base 1s + 2 pts + Successor XP $\text{Infamy} \times 4$, stat cap 4), Gang Mark legacy tattoo, The Hoard, The Bone Pile & Relics, Elders & facility staffing, and Gang Shenanigans.
     - Boss Quirk formal Markdown Schema & Content Hook.
   - **Gaps Flagged**:
     - `[MISSING RULE / GAP: Weapon Damage Metric & Loadout Notation Discrepancy]`
     - `[MISSING RULE / GAP: Dual-Wielding Melee Weapons]`
   - **Content Extension Points**:
     - `[CONTENT EXTENSION POINT: Boss Quirks & Talents]`

3. `02_PROD_Core_Rules/03_Action_Economy_and_Turn_Flow.md`
   - **Domain**: Action Economy & Turn Flow
   - **Key Mechanics Codified**:
     - Round Action Budgets: Boss (3 Standard Actions + 1–3 Free Orders + Free Actions), Mob (2 Actions governed by The Boredom Rule).
     - The Boredom Rule: Mobs cannot repeat the same action twice per round (sole exception: Move when charging/fleeing).
     - Standard Action Catalog: Move, Attack (Melee/Ranged), Plunder, Manipulate (including player-triggered traps), Order.
     - Mob States: Ordered, Loitering (1 action on table, 1 action saved for defense), Out of Control (2 actions on table, 0 actions saved for defense), and Regaining Control command test.
     - Free Actions & Free Orders mechanics.
     - Reactions & Holding Actions: Requirement to save Standard Actions on player turn to Dodge/Parry on enemy turn; 0 saved actions = Armor only.
     - Reaction Catalog: Dodge (Slink), Parry (Tough + Shield/Heavy), Scatter (Boss Mouth test), and reactive Quirks.
     - Structured 5-Phase Round Flow: Phase 0 Setup, Phase 1 Round Start, Phase 2 Player Active Turn, Phase 3 Enemy Active Turn, Phase 4 Round Closure.
     - Combat End, Fleeing, and Disengaging mechanics (`Slink 5+/Highest Defence TN`), Opportunity Attacks, and Bulk 3+ heavy loot restriction.
   - **Gaps Flagged**:
     - `[MISSING RULE / GAP: Free Order Action Permissibility in Self-Defense Reactions]`
     - `[MISSING RULE / GAP: Disengage Failure & Opportunity Attack Resolution]`

---

## 2. Style & Architectural Verification

- **Tier A Mechanical Rules**: Pure instructional present tense with zero math bloat.
- **Total De-Gendering**: Second-person "You" / explicit imperative nouns ("The Goblin Boss", "The Mob", "The GM").
- **Slash Notation Standard**: 100% compliant with `[Stat] [Target Face]+/[Required Successes]` (e.g. `Slink 5+/2`, `Tough 4+/1`, `Brains 6/2`).
- **Keyword Constancy**: Strictly maintained across all three chapters (Grit for Boss health, Health/Health Dice for Mobs, Mob for follower units, Loot/Loot Value for treasure).
- **Single-Source Rule Architecture**: All concepts defined authoritatively in their primary chapters and cross-referenced with Markdown links.
- **Content Separation**: All living content catalogs decoupled into formal Markdown Schemas and modular extension points.
