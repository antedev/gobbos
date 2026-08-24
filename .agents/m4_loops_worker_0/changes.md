# Changes Summary — Milestone 4 (Macro Loops & Progression)

**Author:** Worker 4 (`m4_loops_worker_0`)  
**Domain:** The Raid Loop, Economy, The Lair Loop & Roguelite Progression, Journeys & Hazard Resolution  
**Date:** 2026-08-24  

---

## 1. Files Created & Modified

### `02_PROD_Core_Rules/09_The_Raid_Loop.md` (NEW)
- **Purpose:** Official production rulebook chapter for the four-phase raid structure, zero-math tiered economy, encumbrance mechanics, danger/alert scaling, and post-raid reckoning.
- **Key Systemic Components:**
  - *4-Phase Raid Flow:* Planning & Approach, Infiltration & Assault, Objective & Plunder, Extraction & Escape.
  - *The Raid Economy:* 5-to-1 exponential Loot Value ladder (T1 Junk to T5 Mythic Relic), Rule of Five smelting/barter, Scrap generation & conversion.
  - *Carry Capacity & Load States:* Unburdened, Over-Laden, Dragging, Immobilized; Bulk 3+ item constraints; Mob carry limits ($\text{Size} \times 4$ unburdened, $\text{Size} \times 5$ dragging) and casualty drops.
  - *Danger Scaling & Alert:* Base Danger Rating (1–5), Labor Scouting resolution table (0 to 3+ successes), Alert track and escalation check (1d6 vs Alert).
  - *Post-Raid Reckoning:* Communal Glory conversion to Shared Boss XP (0/1/2 XP), Personal Glory triggers (+1 XP), Oddity drafting by consensus / first pick.
  - *Structural Schema:* Loot & Salvage Item Schema with `[CONTENT EXTENSION POINT: Loot & Salvage Items]`.
  - *Gap Markers Embedded:*
    - `[MISSING RULE / GAP: Economy Currency Normalization & Tiered Conversion]`
    - `[MISSING RULE / GAP: Codified Extraction Phase & Chase Mechanics]`
    - `[MISSING RULE / GAP: Private Gang Hoard vs. Communal Hoard Economy]`

### `02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md` (NEW)
- **Purpose:** Official production rulebook chapter for the Lair dashboard, 4-step downtime sequence, labor allocation, asset lifecycle & Dominance, and generational roguelite progression.
- **Key Systemic Components:**
  - *Lair Dashboard:* Warren Tier (1–4), Asset Capacity formula $(\text{Warren Tier} \times 2) + 2$ with over-capacity mood penalty (+1 Swarm Mood per excess asset per turn), Communal Hoard (Loot Value and Scrap), Gobbo Pool in d6s (Raiders vs Laborer Dice; auto-heal on $\ge 1$ HP; wiped Mobs removed; Communal Runts 3d6 floor; Vacant Nest Growth +1d6 when $< 3\text{d}6/\text{player}$), Threat Level (0–5, Retaliatory Assault at 5), Swarm Mood (0–5, Mob Mutiny at 5), Bone Pile (dead Boss skulls, milestone boons every 4 skulls).
  - *4-Step Lair Phase Sequence:* Step 1 Homecoming & Tally, Step 2 Lair Pulse & Complications (1d66 table), Step 3 Labor Allocation (Safe 2-Dice = 1 auto success vs Risky Push 1-Die on 4+ with 6s explode and 1s injure worker for 1 turn), Step 4 Boss Downtime Actions (The Pitch `Mouth 4+/1`, Laying Low `Slink 4+/1`, Custom Crafting `Brains 4+/1`, The Skim `Slink 4+/1`, Bar Brawl `Tough/Mouth 4+/1`, Beast Taming `Brains/Tough 4+/1`).
  - *Asset Framework & Dominance:* `[Person]`, `[Facility]`, `[Ally]`, `[Blueprint]` lifecycle; Non-Stacking clause; Loss of Knowledge; Dominance contribution ledger, renaming, priority, and kickbacks; Outposts & Macro-Territory garrison and supply run checks.
  - *Roguelite Progression:* Next Gobbo Up ($\text{Successor XP} = \text{Gang Infamy} \times 4$, cap 4 at creation), Catch-Up Boost (+2 XP on first survived raid), Inherited Gang Marks (1 Quirk/Twist ignoring stat/tier gates), Named Items & Revenge Quests, Patron Saints of the Bone Pile, Retirement to Elders at stat Level 6.
  - *Structural Schema:* Lair Room & Facility Schema with `[CONTENT EXTENSION POINT: Lair Rooms & Facilities]`.
  - *Gap Markers Embedded:*
    - `[MISSING RULE / GAP: Retaliatory Lair Assault Resolution Engine]`
    - `[MISSING RULE / GAP: Mutiny Resolution Mechanics & Facility Recovery]`
    - `[MISSING RULE / GAP: Asset Decommissioning, Destruction, and Slot Recovery]`
    - `[MISSING RULE / GAP: Mid-Raid Boss Death & Successor Spawning Timing]`
    - `[MISSING RULE / GAP: Formal Patron Saint Ledger & Appeasement Trigger System]`

### `02_PROD_Core_Rules/11_Journeys_and_Hazards.md` (NEW)
- **Purpose:** Official production rulebook chapter for travel turns, the four travel roles, route tests, travel events, return journey loot burden, and the environmental hazards / zone profiles framework.
- **Key Systemic Components:**
  - *Journey Loop & Stages:* 1 to 3 Stages (Short, Medium, Long/Perilous).
  - *4 Travel Roles:* Map-Scrawler (**Brains**), Sniffer (**Slink**), Scavver (**Tough**), Loud-Mouth (**Mouth**); Mob assignment rules (Tough rolls Size in d6s; Slink/Brains/Mouth roll exactly 1d6).
  - *Stage Resolution:* Step 1 Route Test (**Brains 5+/1**; failure deals 1 Mob Attrition + Bane on Travel Event); Step 2 Travel Event (1d6 table targeting specific roles).
  - *Return Journeys & Loot Burden:* Laden Mobs ($> 50\%$ carry: Bane on Slink/Tough, Route Test requires +1 success); Over-Laden Mobs (100% carry: no passive armor defense, auto 1 damage on failed Route Tests, discard 2 Bulk loot when fleeing or Mob becomes Uncontrolled).
  - *Zone Profiles & Traits Framework:* Zone Profile (`Difficulty+/TN`, e.g. `4+/1`, `5+/1`, `5+/2`, `6/2`). Problems (Burning, Narrow, Slippery, Smoky, Toxic, Deep Water); Opportunities (High Ground, Junk Pile, Shadowy, Shoring).
  - *Structural Schema:* Journey Hazard & Event Schema with `[CONTENT EXTENSION POINT: Journey Hazards & Events]`.
  - *Gap Markers Embedded:*
    - `[MISSING RULE / GAP: Journey Terrain Difficulty Mapping & Transit Alert Coupling]`
    - `[MISSING RULE / GAP: Mob Attrition Damage vs. Single Health Die Tracking]`

---

## 2. Style & Integrity Verification

- **Tier A Mechanical Rules:** 100% objective, direct instructional text in active present tense.
- **Zero Math Bloat:** 5-to-1 exponential tier scale, token tallies, no coin division or arithmetic.
- **Total De-Gendering:** 100% compliant; zero gendered pronouns, zero singular "they/their/them" referencing singular entities.
- **Slash Notation:** 100% of check profiles follow `[Stat] [Target Face]+/[Successes]` with no `+` on 6 (e.g., `Brains 5+/1`, `Tough 4+/1`, `Brains 6/2`).
- **Keyword Constancy:** Strict adherence to **Loot**, **Loot Value**, **Scrap**, **Mob**, **Grit**, **Grunt**, **Size**, **Bulk**, **Bangaranga Pool**, **Target Number (TN)**.
