## 2026-08-24T17:43:42Z

You are Worker 2 for Gobbos Core Rules Synthesis (Milestone 2).
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m2_combat_worker_0\

Mandatory Inputs:
- Original Request: c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- Style Guide & Rules: c:\Users\ante\Documents\github\gobbos\GEMINI.md
- Spec Miner 1 Analysis: c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\analysis.md
- Spec Miner 2 Analysis: c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\analysis.md
- Project Scope: c:\Users\ante\Documents\github\gobbos\PROJECT.md

Exclusive Write Ownership:
- `02_PROD_Core_Rules/04_Zones_and_Movement.md`
- `02_PROD_Core_Rules/05_Combat_Engine.md`
- `02_PROD_Core_Rules/06_Mob_Mechanics.md`

Your Tasks:
1. Synthesize `02_PROD_Core_Rules/04_Zones_and_Movement.md`:
   - Zone Topology & Graph abstraction (Zones as tactical nodes).
   - Zone Profiles: `Difficulty+/TN` for unlisted physical actions.
   - Movement costs (1 Move action = 1 Zone; Slink modifiers).
   - Cover mechanics: Partial Cover (+1d Dodge / -1d Ranged Attack) vs Full Cover (blocks line of sight).
   - Modular Zone Traits & Hazards: Slippery, Rubble, Narrow, Chasm, Vertical Cliff, Deep Water, Burning, Toxic Spores, etc.
   - Chaos Tick & Background Node resolution (Mischief table).
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

2. Synthesize `02_PROD_Core_Rules/05_Combat_Engine.md`:
   - Melee Attacks: Tough vs Target Defence TN.
   - Ranged Attacks: Slink vs Target Defence TN, Range in Zones (1, 2, 3 Zones), Cover penalties.
   - Impact Size vs Target Size Stagger calculation on partial hits (>= 1 success, < Defence TN).
   - Weapon Traits: Bashing, Cleave, Crushing, Reach, etc.
   - Weapon Structural Schema & `[CONTENT EXTENSION POINT: Weapons]`.
   - Armor & Shields: Armor Dice, Slink Bane, Shield Tough Parry enablement, Ablative Sacrifice rule.
   - Armor & Shield Structural Schema & `[CONTENT EXTENSION POINT: Armor & Shields]`.
   - Gear, Tools & Consumables Structural Schema & `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`.
   - Clatter Defense Roll: Simultaneous Active Stat Dice (Slink Dodge / Tough Parry) + Passive Armor Dice vs Threat TN.
   - Group Attacks & Flanking mechanics.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

3. Synthesize `02_PROD_Core_Rules/06_Mob_Mechanics.md`:
   - Mob Anatomy & Health Dice pool (Physical d6s = Size, starting at face 6).
   - Single-target damage decrement & spillover into subsequent dice.
   - Frontline Rule (Mob vs Mob clashes damage min(Attacker, Defender) dice simultaneously; backline takes 0).
   - Cleave X & Area Threat / AoE damage applied simultaneously across all active dice.
   - Boss Order Action, Command Limits, Boredom Rule.
   - Unordered Mobs: Loitering Table (1 action spent, 1 saved for defense/scatter) and Out of Control Table (2 actions spent, 0 saved).
   - Mob Scatter Reaction (Boss Mouth vs Threat TN + Size penalty) and Scatter Gamble consequences.
   - Morale Checks & 50% casualty Swarm Terror pool test (`Sum(Surviving Mob Sizes) + Sum(Bosses)` vs Morale TN).
   - Mob Dispersal and Rallying.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.
