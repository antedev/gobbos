## 2026-08-24T17:43:42Z
You are Worker 1 for Gobbos Core Rules Synthesis (Milestone 1).
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m1_core_worker_0\

Mandatory Inputs:
- Original Request: c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- Style Guide & Rules: c:\Users\ante\Documents\github\gobbos\GEMINI.md
- Spec Miner 1 Analysis: c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\analysis.md
- Project Scope: c:\Users\ante\Documents\github\gobbos\PROJECT.md

Exclusive Write Ownership:
- `02_PROD_Core_Rules/01_Core_Resolution.md`
- `02_PROD_Core_Rules/02_Boss_Profile_and_Gang.md`
- `02_PROD_Core_Rules/03_Action_Economy_and_Turn_Flow.md`

Your Tasks:
1. Synthesize `02_PROD_Core_Rules/01_Core_Resolution.md`:
   - D6 Dice Pool Engine, Difficulty Thresholds (Easy 4+, Normal 5+, Hard 6), Success Target Numbers (TN).
   - Exploding 6s and Critical Double Explosions (+1 Grunt & Free Action).
   - Salvage Roll (1d6 on <=0d6 pools: 6=1 success, 1=Fumble & -1 Grunt, 2-5=fail).
   - Gobbo Gamble (rerolling 1s on failed tests; failing again causes Fumble & -1 Grunt).
   - Boons and Banes (+/-1d, Net Cap rule).
   - Bangaranga Pool Engine (seeding, drawing up to Grunt, 1-die tax if draw > TN, double exploding 6s, fail penalty & drain).
   - Flag gaps with `[MISSING RULE / GAP: <Description, why needed, suggested resolution>]` (e.g. Opposed Test tie-breaker formula).

2. Synthesize `02_PROD_Core_Rules/02_Boss_Profile_and_Gang.md`:
   - Main Stats (Tough, Slink, Brains, Mouth) scaling Level 1 to 5.
   - Secondary Stats: Grunt (second highest Main Stat), Grit (base 3, +1 at Tough 4, +2 at Tough 5), Movement (Zones = Slink), Carry Capacity.
   - Boss Creation & Archetype selection (Specialist 3/1/1/1 vs Generalist 2/2/1/1).
   - The Gang as Class Archetype (Gang Identity, Mob recruitment, starting equipment, Gang Hoard).
   - Quirk Structural Schema & `[CONTENT EXTENSION POINT: Boss Quirks & Talents]`.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

3. Synthesize `02_PROD_Core_Rules/03_Action_Economy_and_Turn_Flow.md`:
   - Boss Action Budget: 3 Standard Actions + 1 Free Order Action per round.
   - Mob Action Budget: 2 Actions per round (governed by Boredom Rule).
   - Standard Action Types: Move, Attack (Melee/Ranged), Plunder, Manipulate, Order.
   - Free Actions & Free Order mechanics.
   - Reactions: Dodge, Parry, Scatter, and reaction holding rules.
   - 5-Phase Turn Flow: Setup, Round Start, Player Active Turn, Enemy Active Turn, Round Closure.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

Mandatory Integrity Warning:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Adhere strictly to GEMINI.md: Tier A mechanical rules, zero math bloat, total de-gendering, strict slash notation `[Stat] [Target Face]+/[Successes]`, strict keyword constancy.

Write `changes.md` and `handoff.md` in your working directory, and message parent when complete.
