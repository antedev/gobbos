## 2026-08-24T17:38:46Z
You are Spec Miner 2 for the Gobbos Core Rules Synthesis.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\
Mandatory inputs:
- Original Request: c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- Style Guide & Rules: c:\Users\ante\Documents\github\gobbos\GEMINI.md
- Source Drafts to inspect: `01_STAGE_Drafts/01_Characters & Mobs/`, `01_STAGE_Drafts/04_Enemies/`, `01_STAGE_Drafts/08_Magic/`, damage/condition rules, and enemy rules across STAGE and PROD.

Your assigned domain:
1. Mob Mechanics (Mob anatomy, Size, Health Dice pool, Health Dice decrement & spillover, Area Threat / AoE damage resolution against Mobs, Boss Order actions, Loitering table, Out-of-Control table, Morale checks, Swarm Terror at 50% casualties, Mob Dispersal and Rallying).
2. Damage, Grit, Conditions & Wounds (Damage resolution, Grit decrement, Wounds track for Bosses/Elites, Overkill rule, Death & Dying state, In-Game States/Conditions: Stunned, Staggered, Weakened, Restrained, Dumb, Silenced, Blinded, Terrified, Prone; Duration and recovery rules).
3. Magic & Bangaranga Framework (Pure mechanical casting engine: Bangaranga Pool generation, spending Bangaranga, Wild Magic surges/misfires/catastrophes, Tag Effect system architecture: combining Element + Delivery + Magnitude/Tier, Ritual casting mechanics — WITHOUT full spell catalogs).
4. Enemy & NPC Mechanics (Deterministic threat resolution, GM never rolls, Threat TN profiles, Standard vs Elite vs Boss enemies, Enemy Ancestries & Special Traits mechanics, Enemy Reactions).

Your tasks:
1. Thoroughly inspect all draft and prod files in your assigned domain.
2. Extract all pure systemic mechanics while stripping out living catalogs (specific spell lists, enemy bestiaries).
3. Design formal Markdown Schemas/Templates for content instances:
   - Tag Effect / Spell Schema (Name, Tags, Delivery Type, Bangaranga Cost, Target TN / Profile, Effect by Tier T1-T3, Fumble / Hazard Risk)
   - Enemy / NPC Statblock Schema (Name, Threat Classification, Base TN, Threat Dice / Damage, Wounds / Health, Special Traits & Ancestries, Reactions, Morale Trigger)
   - Condition & Hazard Schema (Condition Name, Mechanical Effect, Application Trigger, Removal / Recovery Check)
4. Identify every mechanical gap, broken loop, or ambiguity in your domain. Format each as:
   `[MISSING RULE / GAP: <Description of missing mechanic, why it is needed, and suggested resolution>]`
5. Write your complete analysis report to `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\analysis.md` and your handoff to `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_combat_magic_0\handoff.md`.
6. Send a message to parent when done with a concise summary and path to your handoff file.
