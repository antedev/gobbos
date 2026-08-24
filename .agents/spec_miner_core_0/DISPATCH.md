# DISPATCH LOG

## 2026-08-24T17:38:46Z
You are Spec Miner 1 for the Gobbos Core Rules Synthesis.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\
Mandatory inputs:
- Original Request: c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- Style Guide & Rules: c:\Users\ante\Documents\github\gobbos\GEMINI.md
- Source Drafts to inspect: `01_STAGE_Drafts/00_Rules/`, `01_STAGE_Drafts/01_Characters & Mobs/`, `02_PROD_Core_Rules/00_Rules/`, `02_PROD_Core_Rules/01_Characters & Mobs/`

Your assigned domain:
1. Core Resolution & Dice Pool Engine (Pool tests, TN thresholds 4+, 5+, 6, Exploding 6s, Double Explosions, Salvage Rolls, Gobbo Gamble, Fumble tables/mechanics).
2. Attributes, Boss Profile & Gang Fundamentals (Tough, Slink, Brains, Mouth, Grunt, Grit, Boss creation, Gang as class archetype).
3. Action Economy & Turn Flow (3 Standard Actions + 1 Free Order, Reactions: Dodge, Parry, Scatter, Free Actions, Turn phases: Player Active Turn, Enemy Active Turn, End of Round).
4. Zones, Movement & Environment (Zone topology, Zone Profiles Difficulty+/TN, Movement costs, Cover: Partial/Full, Zone Traits/Hazards: Slippery, Burning, Toxic, Narrow, Rubble).
5. Combat Engine (Melee, Ranged, Impact Size / Stagger calculation, Weapon Traits: Bashing, Cleave, etc., Armor mitigation dice & Slink Bane, Shield Parry reaction, Group Attacks, Clatter Rolls).

Your tasks:
1. Thoroughly inspect all draft and prod files in your assigned domain.
2. Extract all pure systemic mechanics (rules engine) while stripping out hardcoded living catalogs (full weapon lists, specific quirk lists, specific equipment catalogs).
3. Design formal Markdown Schemas/Templates for content instances that plug into your domain:
   - Weapon Schema (Name, Category, Hands, Range in Zones, Bulk, Impact Size, Traits, Attack Profile)
   - Armor & Shield Schema (Name, Category, Armor Dice, Slink Bane, Bulk, Special Traits)
   - Gear & Tools Schema (Name, Category, Bulk, Mechanical Effect, Usage/Consumable)
   - Boss Quirk Schema (Name, Trigger, Cost/Grunt, Mechanical Effect, Keywords)
4. Identify every single mechanical gap, ambiguity, or missing rule in your domain. Format each as:
   `[MISSING RULE / GAP: <Description of missing mechanic, why it is needed, and suggested resolution>]`
5. Write your complete, detailed analysis report to `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\analysis.md` and your handoff to `c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_core_0\handoff.md`.
6. Send a message to parent when done with a concise summary and path to your handoff file.
