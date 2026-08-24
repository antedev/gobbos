## 2026-08-24T17:43:42Z
You are Worker 3 for Gobbos Core Rules Synthesis (Milestone 3).
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m3_magic_threats_worker_0\

Mandatory Inputs:
- Original Request: c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- Style Guide & Rules: c:\Users\ante\Documents\github\gobbos\GEMINI.md
- Spec Miner 2 Analysis: c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\analysis.md
- Project Scope: c:\Users\ante\Documents\github\gobbos\PROJECT.md

Exclusive Write Ownership:
- `02_PROD_Core_Rules/07_Damage_Grit_and_Wounds.md`
- `02_PROD_Core_Rules/08_Magic_and_Bangaranga.md`
- `02_PROD_Core_Rules/12_Adversaries_and_Threats.md`

Your Tasks:
1. Synthesize `02_PROD_Core_Rules/07_Damage_Grit_and_Wounds.md`:
   - Damage Types & Resolution against Grit.
   - Boss Grit Decrement, 0 Grit State, Final Act (1 Easy 4+ Action + 1 Order Action), and Death.
   - Enemy Wounds Track (Standard enemies 1-hit kill; Elites/Bosses 2-8 Wounds).
   - Overkill Rule: `Wounds Dealt = floor(Successes / Defence TN)`.
   - In-Game Conditions Matrix (9 official states: Weakened, Restrained, Dumb, Silenced, Blinded, Terrified, Stunned, Prone, Staggered).
   - Application triggers, duration, and recovery rules (1 Standard Action in clean zone or combat end).
   - Condition & Hazard Structural Schema & `[CONTENT EXTENSION POINT: Environmental Hazards & Conditions]`.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

2. Synthesize `02_PROD_Core_Rules/08_Magic_and_Bangaranga.md`:
   - Pure Systemic Magic Casting Engine: Farkle-style Push-Your-Luck rolling Brains dice pool.
   - Locking successes, pushing for higher matching sets, Farkle Mishap on 0 new successes.
   - Spell Tiers determined by largest matching set of successes (T1 Single, T2 Pair, T3 Triple, T4 Quad, T5 Quint).
   - Power Word Slots & Tag Synthesis (Level 3=2 slots, Level 4=4 slots, Level 5=6 slots).
   - Chaotic Leakage triggered by non-success matching sets (T2 Pair, T3 Triple).
   - Bangaranga integration for supernatural amplification.
   - Ritual Casting mechanics (extended cooperative casting, component costs, failure stakes).
   - Tag Effect & Spell Structural Schema & `[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]`.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

3. Synthesize `02_PROD_Core_Rules/12_Adversaries_and_Threats.md`:
   - Deterministic Threat Resolution Engine (GM NEVER rolls dice; all attacks are static Threat Profiles `Difficulty+/TN` + flat Damage).
   - Standard vs Elite vs Boss enemy scales.
   - Enemy Mob Damage Scaling: `Base Damage + (Size - 1)`.
   - 3-Layer Trait Hierarchy: Layer 1 Ancestries (Beast, Humanoid, Undead, Monstrosity, Fiend), Layer 2 Tags, Layer 3 Unique Traits.
   - Enemy Reactions and Triggered Abilities.
   - Enemy Morale & Swarm Terror Triggers.
   - Enemy & NPC Statblock Structural Schema & `[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]`.
   - Flag gaps with `[MISSING RULE / GAP: ...]`.

Mandatory Integrity Warning:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Adhere strictly to GEMINI.md: Tier A mechanical rules, zero math bloat, total de-gendering, strict slash notation `[Stat] [Target Face]+/[Successes]`, strict keyword constancy.

Write `changes.md` and `handoff.md` in your working directory, and message parent when complete.
