# Project: Gobbos TTRPG Modular Core Rules Synthesis

## Architecture
The system is a streamlined, modular, zero-math TTRPG core rulebook located in `02_PROD_Core_Rules/`.
It isolates pure game mechanics and systemic loops from living content catalogs (weapons, equipment catalogs, spell lists, monster bestiaries, quirk compendiums), establishes single-source rule definitions with strict cross-references, embeds standardized structural schemas with `[CONTENT EXTENSION POINT]` tags, and explicitly flags all mechanical gaps with `[MISSING RULE / GAP]` tags.

### Modular Chapter Structure (`02_PROD_Core_Rules/`)
1. `01_Core_Resolution.md` — Core Resolution & Dice Pool Engine (Pool tests, Exploding 6s, Salvage rolls, Gobbo Gamble, Boons & Banes, Bangaranga pool).
2. `02_Boss_Profile_and_Gang.md` — Attributes, Boss Profile & Gang Fundamentals (Main Stats 1–5, Grunt, Grit, Boss creation, Gang archetype, Quirk Schema & `[CONTENT EXTENSION POINT: Boss Quirks & Talents]`).
3. `03_Action_Economy_and_Turn_Flow.md` — Action Economy & Turn Flow (3 Standard Actions + 1 Free Order, Reactions, Free Actions, 5-Phase Round Flow).
4. `04_Zones_and_Movement.md` — Zones, Movement & Environment (Zone Profiles `Difficulty+/TN`, Movement costs, Cover, Modular Zone Traits/Hazards, Chaos Tick).
5. `05_Combat_Engine.md` — Combat Engine (Melee, Ranged, Impact Size & Stagger, Weapon Traits, Clatter Defense, Shield Parry, Group Attacks, Weapon Schema & `[CONTENT EXTENSION POINT: Weapons]`, Armor/Shield Schema & `[CONTENT EXTENSION POINT: Armor & Shields]`, Gear Schema & `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`).
6. `06_Mob_Mechanics.md` — Mob Mechanics (Mob anatomy, Size, Health Dice pool, single-target decrement & spillover, Frontline Rule, Cleave/AoE damage, Boss Orders, Loitering, Out of Control, Morale & Swarm Terror, Dispersal & Rallying).
7. `07_Damage_Grit_and_Wounds.md` — Damage, Grit, Conditions & Wounds (Damage resolution, Grit decrement, Wounds track for Bosses/Elites, Overkill rule, Death & Final Act, Conditions Matrix, Condition & Hazard Schema & `[CONTENT EXTENSION POINT: Environmental Hazards & Conditions]`).
8. `08_Magic_and_Bangaranga.md` — Magic & Bangaranga Framework (Brains push-your-luck pool, Spell Tiers by matching sets, Chaotic Leakage, Bangaranga spending, Rituals, Tag Effect & Spell Schema & `[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]`).
9. `09_The_Raid_Loop.md` — The Raid Loop (4-Phase Raid flow, 5-to-1 Loot Value ladder, Scrap, Infamy Marks, Glory, XP, Post-Raid reckoning, Loot Item Schema & `[CONTENT EXTENSION POINT: Loot & Salvage Items]`).
10. `10_The_Lair_Loop_and_Progression.md` — The Lair Loop & Roguelite Progression (Lair Dashboard, Warren Tier, Gobbo Pool, 4-Step sequence, Labor Safe/Risky, Boss downtime, Generational Boss death & Successor mechanics, Lair Room Schema & `[CONTENT EXTENSION POINT: Lair Rooms & Facilities]`).
11. `11_Journeys_and_Hazards.md` — Journeys & Hazard Resolution (Travel turns, 4 Travel Roles, Route tests, Environmental Attrition, Travel Hazard Schema & `[CONTENT EXTENSION POINT: Journey Hazards & Events]`).
12. `12_Adversaries_and_Threats.md` — Adversaries & Threat Framework (Deterministic threat engine, GM never rolls, Threat TN profiles, Standard vs Elite vs Boss enemies, 3-Layer Trait Hierarchy, Enemy Statblock Schema & `[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]`).

---

## Feature Inventory
| # | Feature / Domain | Description | Chapter | Milestone |
|---|------------------|-------------|---------|-----------|
| 1 | Dice Pool Tests | D6 pool vs Easy 4+, Normal 5+, Hard 6 with required successes | `01_Core_Resolution.md` | M1 |
| 2 | Exploding 6s & Crits | Recursive exploding 6s; double explosions grant +1 Grunt / free action | `01_Core_Resolution.md` | M1 |
| 3 | Salvage & Gamble | Salvage roll (1d6 on $\le 0$ pool); Gobbo Gamble on 1s with Fumble risk | `01_Core_Resolution.md` | M1 |
| 4 | Bangaranga Pool | Communal pool seeding, draw limits, 1-die tax if draw $>$ TN, fail drain | `01_Core_Resolution.md` | M1 |
| 5 | Boons & Banes | Situational +/- 1d modifiers with net cap equal to lower profile | `01_Core_Resolution.md` | M1 |
| 6 | Boss Attributes & Stats | Tough, Slink, Brains, Mouth (1-5), Grunt derived, Grit pool | `02_Boss_Profile_and_Gang.md` | M1 |
| 7 | Boss Creation & Gang | Specialist vs Generalist starting stats, Gang as Class archetype | `02_Boss_Profile_and_Gang.md` | M1 |
| 8 | Quirk Schema & Hooks | Quirk template, trigger/cost/effect structure, content hook | `02_Boss_Profile_and_Gang.md` | M1 |
| 9 | Action Economy | 3 Standard Actions + 1 Free Order for Boss; 2 Actions for Mobs | `03_Action_Economy_and_Turn_Flow.md` | M1 |
| 10 | Round Structure | 5-phase turn flow: Setup, Round start, Player Turn, Enemy Turn, Closure | `03_Action_Economy_and_Turn_Flow.md` | M1 |
| 11 | Reactions & Free Actions | Dodge, Parry, Scatter, Free actions, and Reaction holding | `03_Action_Economy_and_Turn_Flow.md` | M1 |
| 12 | Zone Topologies | Interconnected zones, Zone Profiles `Difficulty+/TN`, Movement costs | `04_Zones_and_Movement.md` | M2 |
| 13 | Cover & Zone Traits | Partial/Full cover, Slippery, Burning, Toxic, Narrow, Rubble, Chaos Tick | `04_Zones_and_Movement.md` | M2 |
| 14 | Melee & Ranged Combat | Attack tests, Range in zones, Impact Size vs Target Size for Stagger | `05_Combat_Engine.md` | M2 |
| 15 | Clatter Defense Roll | Simultaneous active evasion (Slink/Tough) + passive Armor Dice | `05_Combat_Engine.md` | M2 |
| 16 | Weapons & Armor Schemas | Formal schemas for Weapons, Armor/Shields, Gear/Tools/Consumables | `05_Combat_Engine.md` | M2 |
| 17 | Mob Anatomy & Health Dice | Dice pool = Size starting at face 6, decrement & spillover | `06_Mob_Mechanics.md` | M2 |
| 18 | Mob Tactical Actions | Orders, Loitering table, Out of Control table, Boredom rule | `06_Mob_Mechanics.md` | M2 |
| 19 | Mob Morale & Dispersal | 50% casualty Swarm Terror pool test, Dispersal, Rallying | `06_Mob_Mechanics.md` | M2 |
| 20 | Damage & Grit Decrement | Flat damage resolution against Grit, 0 Grit Final Act & Death | `07_Damage_Grit_and_Wounds.md` | M3 |
| 21 | Wounds & Overkill | Elite/Boss Wounds track, Overkill rule ($\lfloor \text{Successes}/\text{TN} \rfloor$) | `07_Damage_Grit_and_Wounds.md` | M3 |
| 22 | Conditions Matrix | 9 official states, application, durations, clear conditions | `07_Damage_Grit_and_Wounds.md` | M3 |
| 23 | Condition/Hazard Schema | Formal schema for Conditions, environmental hazards & traps | `07_Damage_Grit_and_Wounds.md` | M3 |
| 24 | Magic Push-Your-Luck | Brains pool rolling, matching sets for Tiers 1-5, Farkle Mishaps | `08_Magic_and_Bangaranga.md` | M3 |
| 25 | Chaotic Leakage & Rituals | Non-success sets cause leakage; extended ritual casting rules | `08_Magic_and_Bangaranga.md` | M3 |
| 26 | Tag Effect / Spell Schema | Element + Delivery + Magnitude/Tier schema, extension point | `08_Magic_and_Bangaranga.md` | M3 |
| 27 | Deterministic Threat Engine | Zero GM rolls, Threat Profiles + flat damage, enemy reactions | `12_Adversaries_and_Threats.md` | M3 |
| 28 | 3-Layer Trait Hierarchy | Ancestry -> Tag -> Unique Statblock traits, Enemy Statblock Schema | `12_Adversaries_and_Threats.md` | M3 |
| 29 | The Raid Loop | 4-Phase Raid structure (Plan, Infiltrate, Plunder, Extract) | `09_The_Raid_Loop.md` | M4 |
| 30 | 5-to-1 Loot Economy | Exponential 5-to-1 Loot Value ladder, Scrap, Infamy Marks, Glory, XP | `09_The_Raid_Loop.md` | M4 |
| 31 | Loot & Salvage Schema | Item schema with Bulk, LV, Scrap, Divisibility, Utility tags | `09_The_Raid_Loop.md` | M4 |
| 32 | Lair Dashboard & Warren | Warren Tier, Asset capacity, communal Gobbo Pool (Raiders/Laborers) | `10_The_Lair_Loop_and_Progression.md` | M4 |
| 33 | 4-Step Lair Sequence | Homecoming/Tally, Pulse/Complications, Labor Safe/Risky, Downtime | `10_The_Lair_Loop_and_Progression.md` | M4 |
| 34 | Roguelite Generation Death | Successor XP ($\text{Infamy} \times 4$), Gang Marks, Bone Pile, Elders | `10_The_Lair_Loop_and_Progression.md` | M4 |
| 35 | Lair Room Schema | Asset schema with Cost, Upkeep, Boon, Volatility, Upgrade Tiers | `10_The_Lair_Loop_and_Progression.md` | M4 |
| 36 | Journeys & Travel Roles | Map-Scrawler, Sniffer, Scavver, Loud-Mouth, Route tests | `11_Journeys_and_Hazards.md` | M4 |
| 37 | Journey Hazard Schema | Hazard schema with terrain tags, role targets, checks, consequences | `11_Journeys_and_Hazards.md` | M4 |

---

## Milestones & Execution Plan

| # | Milestone | Scope | Deliverables | Dependencies | Status |
|---|-----------|-------|--------------|--------------|--------|
| 0 | Phase 0: Survey & Schema Mining | STAGE/PROD repository survey | Extraction reports & schemas | none | DONE |
| 1 | Milestone 1: Core Engine, Profile & Actions | Chapters 01, 02, 03 | `01_Core_Resolution.md`, `02_Boss_Profile_and_Gang.md`, `03_Action_Economy_and_Turn_Flow.md` | M0 | PLANNED |
| 2 | Milestone 2: Spatial, Combat & Mobs | Chapters 04, 05, 06 | `04_Zones_and_Movement.md`, `05_Combat_Engine.md`, `06_Mob_Mechanics.md` | M1 | PLANNED |
| 3 | Milestone 3: Health, Magic & Threats | Chapters 07, 08, 12 | `07_Damage_Grit_and_Wounds.md`, `08_Magic_and_Bangaranga.md`, `12_Adversaries_and_Threats.md` | M1, M2 | PLANNED |
| 4 | Milestone 4: Macro Loops & Progression | Chapters 09, 10, 11 | `09_The_Raid_Loop.md`, `10_The_Lair_Loop_and_Progression.md`, `11_Journeys_and_Hazards.md` | M1 | PLANNED |
| 5 | Milestone 5: Verification & Gap Audit | Full rulebook audit | Integrity check, cross-reference validation, style audit | M1, M2, M3, M4 | PLANNED |

---

## Code Layout & File Placement
All core rules chapters MUST be written to `02_PROD_Core_Rules/`:
- `02_PROD_Core_Rules/01_Core_Resolution.md`
- `02_PROD_Core_Rules/02_Boss_Profile_and_Gang.md`
- `02_PROD_Core_Rules/03_Action_Economy_and_Turn_Flow.md`
- `02_PROD_Core_Rules/04_Zones_and_Movement.md`
- `02_PROD_Core_Rules/05_Combat_Engine.md`
- `02_PROD_Core_Rules/06_Mob_Mechanics.md`
- `02_PROD_Core_Rules/07_Damage_Grit_and_Wounds.md`
- `02_PROD_Core_Rules/08_Magic_and_Bangaranga.md`
- `02_PROD_Core_Rules/09_The_Raid_Loop.md`
- `02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md`
- `02_PROD_Core_Rules/11_Journeys_and_Hazards.md`
- `02_PROD_Core_Rules/12_Adversaries_and_Threats.md`

