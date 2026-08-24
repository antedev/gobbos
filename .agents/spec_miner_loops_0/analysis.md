# Comprehensive Specification Mining Report: Loops, Progression, Lair, Journeys & Economy

**Author:** Spec Miner 3 (`spec_miner_loops_0`)  
**Domain:** The Raid Loop, Economy, The Lair Loop & Roguelite Progression, Journeys & Hazard Resolution  
**Authority Sources Examined:**
- `01_STAGE_Drafts/03_Loot/31_loot.md`, `32_Carry Stuff.md`, `33_Equipment.md`, `34_Crafting.md`, `35_Equipment_Catalogue.md`
- `01_STAGE_Drafts/05_Base/00_Lair_Rules.md`
- `01_STAGE_Drafts/07_Travel/00_Journey_Rules.md`
- `01_STAGE_Drafts/00_Rules/00_Overview.md`, `01_Dice.md`, `02 Combat.md`, `03_Movement & Zones.md`, `05_Raid points.md`, `06_Keywords Index.md`, `07_Wounds_Conditions.md`
- `01_STAGE_Drafts/01_Characters & Mobs/10_Stats.md`, `11_Character Creation.md`, `11a_Roles.md`, `12_Gang.md`, `13_Goblin_mob.md`, `15_Level_Up and death.md`, `16_Unified_Modular_Powers_System.md`
- `00_DEV_Brainstorms/GDRs/GDR-002_Gang_Pillar_And_Lair_Economy.md`, `GDR-006_Environmental_Hazards_and_Zone_Statblocks.md`
- `00_DEV_Brainstorms/Lair_System_Refined_Framework.md`, `Lair_Mechanics_Game_Engineering_Audit.md`
- `GEMINI.md` Style Guide & `ORIGINAL_REQUEST.md`

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Raid Economy | Exponential Plunder Tiers (T1–T5) | All treasure is graded on a 5-to-1 exponential ladder (5x T1 = 1x T2, etc.). | Plunder items, Tier (T1–T5), Loot Value (LV) units | Concentrated wealth tokens in character tally boxes | Low-tier hoarding cannot skip tier gates without 5-to-1 smelting | `31_loot.md:9-32` |
| 2 | Raid Economy | Rule of Five (Smelting & Barter) | Goblins can combine 5 tokens of Tier X into 1 token of Tier X+1, or break 1 token of Tier X+1 into 5 tokens of Tier X. | 5 tokens Tier X (Up) or 1 token Tier X+1 (Down) | 1 token Tier X+1 or 5 tokens Tier X | Non-multiples of 5 cannot be traded up | `31_loot.md:55-64` |
| 3 | Raid Economy | Dual Resource Economy (Loot vs. Scrap) | Wealth is split into liquid wealth (Loot: coins, jewels) and raw building matter (Scrap: iron, wood, pipes). | Extracted items, dismantling | Communal Hoard balances | Loot cannot directly replace Scrap for chassis crafting without smelting | `00_Lair_Rules.md:43-47`, `GDR-002:21-25` |
| 4 | Raid Economy | Equipment & Mob Pricing | Mundane items cost 1 token of matching Quality Tier. Outfitting a Mob costs 1 token of desired Tier per Mob Size point. | Target item Tier, Mob Size | Deducted Loot tokens | Workshop Quality prerequisite must be met for T3+ | `31_loot.md:66-88` |
| 5 | Raid Loop | Carry Capacity & Load States | Bosses have Carry = `4 + (2 * Tough)` Bulk; Mobs have `Size * 4` Bulk. Load states determine movement speed and test modifiers. | Carried Bulk vs. Carry threshold | Load State: Unburdened, Over-Laden, Dragging, Immobilized | Over-Laden: -1 Zone speed, Bane 1 on Slink/Tough; Dragging: 1 Zone max, no active defense | `32_Carry Stuff.md:7-36` |
| 6 | Raid Loop | Bulk 3+ Item Constraints | Items of Bulk 3+ require two hands, cannot be carried with active Disengage, and give Mobs -1d attack Bane per Bulk 3+ item. | Carried item Bulk $\ge 3$ | Two-handed requirement, Disengage lockout, Mob Bane | Mob Size limit: Mob can carry at most its Size in Bulk 3+ items | `32_Carry Stuff.md:38-66` |
| 7 | Raid Loop | Mid-Raid Dropped Plunder | When Mob Size shrinks from damage, excess carried Bulk beyond new capacity must be immediately dropped in current Zone. | Mob Size reduction, current carried Bulk | Dropped Loot items in Zone | Picking dropped loot back up requires 1 Plunder action per item | `32_Carry Stuff.md:62-66` |
| 8 | Raid Loop | Scouting & Raid Points | Allocating Laborer dice to Scouting reveals Base Danger Rating, Main Objective (3-5 RP), Targets of Opportunity (+2 RP each), Secret Bypasses. | Allocated Laborer dice pool (4+ test) | Revealed Raid Points, Danger Rating, Bypasses | 0 successes: Going in blind (Bane on first Zone entry test) | `05_Raid points.md:20-33` |
| 9 | Raid Loop | Alert Track & Escalation | GM tracks Alert starting at Base Danger Rating (1-5). Checks made on Zone move, Target completion, or rest. | 1d6 vs. Alert Level | Complication triggered + Alert increases by +1 if roll $\le$ Alert | Roll > Alert: party remains undetected | `05_Raid points.md:36-48` |
| 10 | Raid Loop | Raid Payout & Glory Conversion | Pooled Raid Points convert to Shared Boss XP (1-4 RP: 0 XP; 5-9 RP: 1 XP; 10+ RP: 2 XP). Personal Glory grants +1 XP for specific chaotic acts. | Pooled Raid Points, Personal Glory criteria | Shared XP, Personal XP | Max 1 Personal Glory XP per raid | `15_Level_Up and death.md:54-77` |
| 11 | Raid Loop | Oddity Drafting & First Pick | Physical Oddities are drafted by Player Consensus at raid end. Mobs physically hauling gear out give their controlling Gang First Pick. | Extracted Oddities, Mob carry ledger | Claimed Oddities assigned to Gang inventories | Contested items resolved via player consensus or Lair brawl | `15_Level_Up and death.md:87-93`, `31_loot.md:52` |
| 12 | Lair Loop | Lair Dashboard & Warren Tier | Lair tracked on 6 metrics: Warren Tier (1-4), Asset Capacity `(Tier * 2) + 2`, Communal Hoard, Gobbo Pool, Threat Level (0-5), Swarm Mood (0-5), Bone Pile. | Lair sheet state, Warren Tier | Active asset limit, regional heat, morale thresholds | Exceeding Asset Capacity increases Swarm Mood by +1 per excess asset per turn | `00_Lair_Rules.md:9-77` |
| 13 | Lair Loop | The Gobbo Pool (Workforce) | Population measured in d6s, split each Lair Turn into Raider Mobs (taken on raid) and Laborer Dice (working at base). | Total Gobbo Pool d6s, Boss Grunt limits | Raider Mobs vs. Laborer Dice | Mobs surviving with $\ge 1$ HP auto-heal to full Size; Size 0 wiped Mobs are permanently removed | `00_Lair_Rules.md:48-57` |
| 14 | Lair Loop | Population Safety Valves | Lair has permanent Communal Runts floor (3d6, cannot labor). If pool is under 3d6/player, Vacant Nest Growth adds +1d6 free during Homecoming. | Surviving Gobbo Pool vs. player count | Restored minimum runts, +1d6 recruit | Prevents total soft-lock after catastrophic wipe | `00_Lair_Rules.md:54-57` |
| 15 | Lair Loop | Lair Phase Sequence (4 Steps) | Step 1: Homecoming & Tally; Step 2: Lair Pulse & Complications (1d66 table); Step 3: Labor Allocation & Operations; Step 4: Boss Downtime Actions. | Lair Phase trigger between raids | Resolved recovery, complications, passive yields, labor, downtime | Strict 4-step sequence | `00_Lair_Rules.md:80-136` |
| 16 | Lair Loop | Labor Allocation (Safe vs. Push) | Laborer Dice committed to Scrap, Recruiting, Scouting, Excavating. Safe: 2 dice = 1 auto success; Push: 1 die rolls 4+ (6 explodes, 1 injures worker). | Committed Laborer Dice, Task selection | Generated Scrap, Runts, Scouting successes, Project clearance | Push roll of 1 places die in medical tent for 1 turn | `00_Lair_Rules.md:123-127` |
| 17 | Lair Loop | Boss Downtime Actions | Each active Boss takes 1 action: The Pitch (Mouth 4+/1), Laying Low (Slink 4+/1), Custom Crafting (Brains 4+/1), The Skim (Slink 4+/1), Bar Brawl (Tough/Mouth 4+/1), Beast Taming. | Boss Action declaration, Stat test | Mood reduction, Threat reduction, crafted gear, stolen loot, Dominance shift | Skim roll containing 1s: caught, 0 Loot, +1 Swarm Mood | `00_Lair_Rules.md:128-136` |
| 18 | Lair Loop | Modular Asset Framework | Knowledge/facilities held in 4 types: [Person], [Facility], [Ally], [Blueprint]. Each defines Boon, Bane, Dominance Kickback. Non-stacking clause. | Asset card/entry, construction cost | Mechanical boons, passive yields, crafting unlocks | Loss of asset immediately disables associated capability | `00_Lair_Rules.md:139-170` |
| 19 | Lair Loop | Dominance & Inter-Gang Politics | Gangs track cumulative contributions (Loot, Scrap, Labor) on asset ledger. Highest contributor holds Dominance (Naming, Priority, Kickback). | Gang investment records | Dominant Gang designation & exclusive kickback | Tied contributions mean Disputed asset (no kickback) until broken by investment or Bar Brawl | `00_Lair_Rules.md:173-188` |
| 20 | Lair Loop | Outposts & Macro-Territory | Conquered sites converted to Outposts by garrisoning 1d6 permanently from Gobbo Pool. Generates passive yields; requires Supply Run checks. | Secured dungeon site, 1d6 garrison | Flat passive yield per Lair Turn | Hostile route failure of all 1s: Outpost besieged | `00_Lair_Rules.md:280-290` |
| 21 | Progression | Gang Infamy & Marks | Gang progression level (Infamy 1 to 5). Earn 1 Infamy Mark per 10 Loot contributed or per completed Gang Agenda (1/raid). Thresholds: 3, 6, 10, 15 marks. | Contributed Loot, Completed Agendas | Infamy Level (1–5), max Gang Quirks equipped | Max 1 Agenda Mark per raid | `12_Gang.md:19-45` |
| 22 | Progression | "Next Gobbo Up" (Death & Successor) | Dead Boss replaced by successor: starts with 1 in all stats + 2 advances, plus Successor XP = `Infamy * 4` (stat cap 4 at creation). | Deceased Boss, Gang Infamy | Newly rolled Boss with scaled XP | Successor cannot start as Elder (stat 6) or exceed stat 4 | `15_Level_Up and death.md:3-8`, `12_Gang.md:40-42` |
| 23 | Progression | Catch-Up Boost & Gang Marks | Successor gains +2 bonus XP on first survived raid. Successor receives 1 Quirk/Twist from deceased Boss as a Gang Mark with zero stat/tier gates. | Successor creation, deceased Boss quirk list | +2 bonus XP post-raid, inherited signature Quirk | Inherited Quirk counts toward 3 personal quirks limit | `15_Level_Up and death.md:9-16` |
| 24 | Progression | Named Items & Revenge Quests | Deceased Boss's favored item becomes Named Item with T1 Boon reflecting death/stat. If lost, enemy killer wields it on future raids. | Dead Boss favored gear, cause of death / top stat | Imbued magical named weapon/armor | Rival Gang wielding it triggers rebellion (crits become fumbles) | `15_Level_Up and death.md:18-26` |
| 25 | Progression | Bone Pile & Patron Saints | Dead Bosses added as Skulls. Every 4 Skulls unlocks Lair ancestral boon. Successor can adopt 1 Patron Saint for situational boon with behavioral catch. | Dead Bosses, Bone Pile track | Lair Ancestral Boons, personal Patron Saint boon | Violating Saint's behavioral catch disables boon | `00_Lair_Rules.md:72-77`, `15_Level_Up and death.md:27-36` |
| 26 | Progression | Retirement (Elders) | Boss reaching stat level 6 automatically retires to become an Elder of that stat, granting passive or staffed Lair facility boons. | Stat reaches 6 | Retired Elder asset, player rolls fresh successor Boss | Retired Boss no longer raids | `15_Level_Up and death.md:95-109`, `12_Gang.md:78-88` |
| 27 | Journeys | Journey Loop & Abstract Stages | GM sets route destination and 1 to 3 Stages. Players assign 4 Travel Roles, traverse each Stage (Route Test + Travel Event), and arrive. | Journey destination, 1–3 Stages | Party arrives at raid with accumulated attrition, conditions, or boons | GM never rolls dice during journeys | `00_Journey_Rules.md:9-18` |
| 28 | Journeys | Four Travel Roles | Roles: Map-Scrawler (Brains), Sniffer (Slink), Scavver (Tough), Loud-Mouth (Mouth). Mobs can fill vacant roles (Tough = Size; other stats = 1d6). | Boss / Mob assignments to 4 roles | Role test dice pools | All 4 roles must be filled | `00_Journey_Rules.md:20-36` |
| 29 | Journeys | Stage Resolution (Route Test & Event) | Map-Scrawler rolls Brains 5+/1. Fail: 1 Attrition to all Mobs + Bane on Travel Event. GM rolls 1d6 Event targeting one of the other 3 roles. | Map-Scrawler Brains roll, 1d6 Event roll | Traversal progress, Mob damage, conditions, boons | Failed Route Test imposes Attrition and Bane on Event test | `00_Journey_Rules.md:39-60` |
| 30 | Journeys | Return Journey & Loot Weight | Laden Mobs (>50% carry capacity): Bane on Slink/Tough, Route Test TN +1. Over-Laden Mobs (100% capacity): no passive defense vs hazards, auto 1 damage on route fail. | Carried Loot Bulk vs. Mob Carry capacity | Travel modifiers, risk of Mob becoming Uncontrolled if loot not dropped | Fleeing/dodging hazards requires dropping 2 Bulk loot or Mob becomes Uncontrolled | `00_Journey_Rules.md:63-80` |
| 31 | Hazards | Zone Profiles & Zone Traits | Zones defined by Profile (`Difficulty+/TN`, e.g. `5+/1`). Traits classified as Problems (Hazards/Obstacles) and Opportunities (Features/Treats). | Zone Profile, Zone Traits | Standardized traversal/environmental TN, triggered hazards | GM never rolls to hit; players roll saving throws against Zone Profile | `GDR-006:23-83` |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | Exponential Plunder | Player brings back 20x T1 junk buttons and wants to buy a T3 broadsword (Cost: 1x T3). | Illegal. 20x T1 smelts into 4x T2 via Rule of Five (needs 5x T2 = 25x T1 to smelt into 1x T3). Player is 5x T1 short. |
| 2 | Mob Carry Casualties | Size 3 Mob carrying 11 Bulk (limit 12) takes 2 Size damage from an attack, dropping to Size 1 (limit 4 Bulk). | Immediate drop. Controlling Boss must immediately declare which 7 Bulk of items are dropped in current Zone. |
| 3 | Bulk 3+ & Disengage | Boss holding a Bulk 3 bronze idol attempts to perform a Disengage action to flee melee enemies. | Disengage is blocked. Boss must drop the idol as a Free Action before disengaging, defeat the enemies, or take Opportunity Attacks. |
| 4 | Gobbo Pool Depletion | Entire raiding party wipes (all Raider Mobs reduced to Size 0). Total Gobbo Pool is reduced to 0d6. | Communal Runts safety valve activates: Lair maintains baseline 3d6 runts. Players can always field Size 1 Runt Mobs. Vacant Nest Growth adds +1d6 next Homecoming. |
| 5 | Lair Asset Cap Overload | Tier 1 Lair (Asset Cap: 4) possesses 6 active assets. | Swarm Mood increases by +2 at the start of every Lair Turn until excess assets are demolished or Warren Tier is upgraded. |
| 6 | Dominance Tie | Two Gangs contribute exactly 15 Scrap and 5 Loot to the Scrap Forge. | Asset is Disputed. Neither Gang gains the Dominance Kickback until one Gang invests more resources or wins a Bar Brawl. |
| 7 | Successor Creation Cap | Gang reaches Infamy 5. Deceased Boss replaced by successor who receives 20 Successor XP (5 * 4). | Player spends XP but cannot raise any Main Stat above Level 4 at creation, and cannot start as an Elder (Level 6). |
| 8 | Travel Role Mob Testing | Player assigns a Size 3 Mob to fill the Map-Scrawler role (Brains test). | Mob rolls exactly 1d6 (base stat 1), NOT 3d6. Mobs only roll their Size in dice for Tough (Scavver) tests. |
| 9 | Over-Laden Return Travel | Over-Laden Mob carrying 12 Bulk in a swamp fails a Route Test. | Mob takes 1 party Attrition damage PLUS 1 extra exhaustion damage, and cannot roll passive armor defense against the subsequent Travel Event. |
| 10 | The Skim Downtime Fumble | Boss rolling Slink 4+/1 to skim Loot rolls `4, 1, 1` (success with two 1s). | The 1s trigger discovery: the Boss is caught, receives 0 Loot, and Swarm Mood immediately increases by +1. |

---

## Domain 1: The Raid Loop & Economy (Deep Systemic Extraction)

### 1. Raid Macro Structure (The 4 Raid Phases)
The Raid Loop governs all tactical gameplay outside the Lair, operating in four distinct phases:
1. **Phase 1: Planning & Approach (The Journey):** Players select a scouted Raid Target, review known Objectives and Danger Ratings, allocate Raider Mobs from the Gobbo Pool, assign Travel Roles, and traverse travel Stages to reach the site.
2. **Phase 2: Infiltration & Assault (Entry & Navigation):** Gobbos breach the site. Starting Alert is equal to the Base Danger Rating (T1–T5). Players navigate interconnected Zones, bypass environmental obstacles, engage enemy sentries, and manage the Alert Track.
3. **Phase 3: Objective & Plunder (Tactical Execution):** Players complete the Main Objective (3–5 Raid Points), pursue optional Targets of Opportunity (+2 Raid Points each), dismantle infrastructure for Scrap, and spend Standard Actions (**Plunder**) to secure loose Loot and Oddities.
4. **Phase 4: Extraction & Escape (The Return):** Once objectives are secured (or Alert escalates to catastrophic levels), the party declares Extraction. Gobbos must haul their physical plunder through the return journey while managing encumbrance, Attrition, and pursuing forces.

### 2. The Multi-Tiered Currency & Progression Economy
The Gobbos economy operates without fractional copper/silver math. It integrates five distinct mechanical resources:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            THE GOBBOS ECONOMY                               │
├───────────────────┬─────────────────────────────────────────────────────────┤
│ CURRENCY / METRIC │ PRIMARY FUNCTION & SOURCE                               │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 1. Loot Value (LV)│ Exponential Tiered Wealth (T1–T5). Extracted from raids │
│                   │ in physical items. Smelted via Rule of Five. Used to   │
│                   │ purchase equipment, bribe factions, fund Lair assets.   │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 2. Scrap          │ Abstract physical building matter (iron, wood, pipes).  │
│                   │ Scavenged during raids or produced by Lair facilities.  │
│                   │ Used for room construction, excavating, and gear bases. │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 3. Infamy Marks   │ Gang progression milestones. Earned by contributing     │
│                   │ 10 LV to the Communal Hoard or completing Gang Agendas. │
│                   │ Determines Successor XP pool and equipped Gang Quirks.  │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 4. Raid Points    │ Weightless glory points earned by completing raid       │
│    (Glory)        │ objectives. Pooled at raid end to award Shared Boss XP. │
├───────────────────┼─────────────────────────────────────────────────────────┤
│ 5. Boss XP        │ Individual experience points spent to raise Main Stats. │
│                   │ Derived from pooled Raid Points, Personal Glory (+1),   │
│                   │ and Successor starting pools.                           │
└───────────────────┴─────────────────────────────────────────────────────────┘
```

#### The Exponential 5-to-1 Plunder Scale
* **T1 Junk / Pocket Scrap:** Base unit (= 1x T1). Nails, buttons, tin cups.
* **T2 Scrappy Plunder:** 1x T2 = 5x T1. Silver cutlery, iron shivs, copper kettles.
* **T3 Standard Fine Treasure:** 1x T3 = 5x T2 = 25x T1. Gold chalices, broadswords, silk.
* **T4 Superior Masterwork:** 1x T4 = 5x T3 = 125x T1. Dwarven rune-hammers, altar idols.
* **T5 Legendary Mythic Relic:** 1x T5 = 5x T4 = 625x T1. Godstone shards, dragon crowns.
* **The Rule of Five:** 5 tokens of Tier X combine into 1 token of Tier X+1. 1 token of Tier X+1 breaks down into 5 tokens of Tier X.

### 3. Carry Mechanics, Bulk & Tactical Encumbrance
* **Boss Carry:** Baseline unburdened capacity = `4 + (2 * Tough) Bulk`.
* **Mob Carry:** Baseline unburdened capacity = `Size * 4 Bulk`. Maximum dragging capacity = `Size * 5 Bulk`.
* **Load State Matrix:**
  * *Unburdened ($\le$ Carry):* Full movement speed, zero test penalties.
  * *Over-Laden (Carry + 1 to Carry + Tough):* -1 Zone speed (min 1 Zone), Bane 1 (-1d) on all physical Slink and Tough tests, cannot double-move in a single round.
  * *Dragging (Carry + Tough + 1 to 2x Carry):* Fixed 1 Zone movement, requires two hands, auto-fails stealth and jumping, 0 active defense (cannot Dodge or Parry).
  * *Immobilized (> 2x Carry):* 0 Zones movement speed; must drop items as a Free Action.
* **Bulk 3+ Rules:** Requires two hands, prevents executing Disengage actions, imposes -1d attack Bane on Mobs per item carried. Boss can carry at most `Tough / 2` (min 1) loose Bulk 3+ items.
* **Casualty Drops:** If a Mob shrinks in Size, excess Bulk must be dropped immediately in the current Zone.

### 4. Danger Scaling, Alert & Objective Resolution
* **Base Danger Rating (T1–T5):** Sets starting Alert and baseline hazard difficulty for the raid site.
* **Labor Scouting:** Laborer dice test against 4+:
  * *0 Successes:* Blind Entry (Bane on first Zone entry test).
  * *1 Success:* Danger Rating + Main Objective revealed (3–5 Raid Points).
  * *2 Successes:* +1 Target of Opportunity revealed (+2 Raid Points).
  * *3+ Successes:* +2 Targets of Opportunity revealed (+4 Raid Points total) + Secret Bypass (Boon on first Zone entry test).
* **The Alert Clock:** GM rolls 1d6 upon Zone entry, Target completion, or rest. Roll $\le$ current Alert level triggers a complication and increases Alert by +1 permanently.

---

## Domain 2: The Lair Loop & Roguelite Progression (Deep Systemic Extraction)

### 1. The Lair Dashboard & Core Metrics
1. **Warren Tier (1–4) & Asset Capacity:** Maximum active assets = `(Warren Tier * 2) + 2`. Exceeding this cap increases Swarm Mood by +1 per excess asset per turn.
2. **The Gobbo Pool (Workforce):** Total population tracked in d6s. Divided each Lair Turn into **Raider Mobs** (commanded by Bosses) and **Laborer Dice** (home base workforce).
3. **The Communal Hoard:** Central storage for pooled Loot Value and Scrap.
4. **Threat Level (0–5):** Regional heat. At 5, triggers an immediate Retaliatory Assault against the Lair.
5. **Swarm Mood (0–5):** Goblin morale. At 5, triggers Mob Mutiny (grunts demand 5 Loot/Mob upfront; 1 facility locked).
6. **The Bone Pile:** Ancestral memorial. Every 4 Skulls unlocks a permanent Lair ancestral boon.

### 2. The 4-Step Lair Phase Sequence
* **Step 1: Homecoming & Tally:** Deposit Loot and Scrap into Communal Hoard. Add dead Bosses to Bone Pile. Surviving Mobs with $\ge 1$ HP auto-heal to full Size. Evaluate Vacant Nest Growth (+1d6 if pool < 3d6/player).
* **Step 2: The Lair Pulse & Complications:** Evaluate Threat and Swarm Mood. GM rolls 1d66 on Lair Complications Table.
* **Step 3: Labor Allocation & Passive Operations:** Collect automatic yields from facilities and Outposts. Assign Laborer Dice to Scavenging Scrap, Recruiting Runts, Scouting Targets, or Excavating Projects using Safe (2 dice = 1 success) or Push (1 die rolls 4+, 6 explodes, 1 injures worker) rules.
* **Step 4: Boss Downtime Actions:** Each Boss executes 1 action:
  * *The Pitch:* Mouth 4+/1 (or spend 5 Loot) to reduce Swarm Mood by 1.
  * *Laying Low:* Slink 4+/1 (or spend 5 Loot) to reduce Threat Level by 1.
  * *Custom Crafting:* Brains roll (`Brains + 1` dice, 6s tame Bite, 1s add Chaos quirks) to assemble gear.
  * *The Skim:* Slink 4+/1 to divert up to Slink rating in Loot to Gang Private Hoard (rolling 1s = caught, 0 Loot, +1 Swarm Mood).
  * *Bar Brawl / Power Play:* Tough 4+/1 or Mouth 4+/1 to shift 1 point of contribution on an asset ledger.
  * *Beast Taming:* Brains 4+/1 or Tough 4+/1 to attach beast tags to Mobs.

### 3. Modular Asset Framework & Dominance
* **Asset Types:**
  * `[Person]`: Elders (loyal, frail), Specialists (demand Loot upkeep), Captives (flight risk, increase Threat).
  * `[Facility]`: Physical workshops, dens, nurseries, fortifications built with Loot and Scrap.
  * `[Ally]`: Befriended monsters and patron factions.
  * `[Blueprint]`: Physical schematics (Bulk 0) produced by Reverse Engineering.
* **Asset Rules:** Non-Stacking Clause (identical mechanical boons do not stack), Loss of Knowledge (destroying or losing an asset immediately disables its function).
* **Dominance System:** Gangs track cumulative contributions (Loot, Scrap, Labor) on an asset's ledger. The Gang with highest contribution holds Dominance: receives naming rights, priority access, and the exclusive **Dominance Kickback**. Ties cause Disputed status.

### 4. Character Death & Roguelite Legacy Mechanics
* **Next Gobbo Up:** Death does not restart progress from zero. Successor Boss starts with 1 in all Main Stats, receives 2 starting advances, plus a Successor XP pool = `Gang Infamy * 4` (stat cap 4 at creation; cannot start as Elder).
* **Catch-Up Boost:** Successor gains +2 bonus XP on their first survived raid.
* **Gang Marks:** Successor inherits 1 Quirk or Twist from the deceased Boss, ignoring stat and tier requirements (counts toward 3 personal quirks limit).
* **Named Items:** Deceased Boss's favored equipment gains a T1 Boon reflecting their death or highest stat. Reclaimed if dragged home; claimed by enemy killer if party wipes (fueling Revenge Quests).
* **Patron Saints:** Player may select 1 deceased Boss from the Bone Pile as a Patron Saint, gaining a specific situational boon while following an in-game behavioral catch.
* **Retirement (Elders):** Raising any stat to 6 triggers automatic Retirement. The Boss becomes an Elder, granting passive Gang boons or staffed Lair facility upgrades (Elder of Tough, Slink, Mouth, Brains).

---

## Domain 3: Journeys & Hazard Resolution (Deep Systemic Extraction)

### 1. The Journey Loop & Travel Stages
Travel is resolved in 1 to 3 abstract Stages before arriving at the raid site:
1. **Establish Route:** GM sets destination and number of Stages (1 = Short, 2 = Medium, 3 = Long/Perilous).
2. **Assign Travel Roles:** Party assigns 4 roles:
   * **Map-Scrawler** (Tests Brains): Navigation and route finding.
   * **Sniffer** (Tests Slink): Scouting ahead, detecting ambushes and traps.
   * **Scavver** (Tests Tough): Clearing physical obstacles, foraging, hauling supplies.
   * **Loud-Mouth** (Tests Mouth): Maintaining march discipline, quelling panic and bickering.
   * *Mobs in Roles:* Mobs testing Tough (Scavver) roll their current Size in dice. Mobs testing Slink, Brains, or Mouth roll exactly 1d6.
3. **Traverse Stages:** For each Stage, resolve:
   * *1. The Route Test:* Map-Scrawler rolls Brains 5+/1. Success: clear path. Failure: 1 Attrition damage to all party Mobs + Bane 1 (-1d) on the upcoming Travel Event test.
   * *2. The Travel Event:* GM rolls 1d6 on the Travel Event Table targeting one of the other three roles.
4. **Arrive at Raid:** Party enters the raid site with accumulated Attrition, boons, or conditions.

### 2. Return Journeys & Encumbrance Weight
Dragging plunder back through the wilds increases travel difficulty:
* **Laden Mobs (> 50% Carry Capacity):** Bane 1 (-1d) on all Slink and Tough tests during travel; Map-Scrawler Route Test requires +1 success (e.g., 5+/2).
* **Over-Laden Mobs (100% Carry Capacity):** Suffer Laden penalties; cannot roll passive armor defense against travel hazards; take 1 automatic damage on failed Route Tests; must drop 2 Bulk loot when fleeing hazards or become Uncontrolled.

### 3. Environmental Hazards & Zone Statblocks
Encounter environments are standardized using the **Zone Profile** and **Zone Traits** framework:
* **Zone Profile:** Every Zone has a default difficulty code (e.g., `5+/1`, `5+/2`, `4+/2`). All general environmental interactions, climbing, jumping, and search checks default to this profile.
* **Problems (Hazards & Obstacles):** Negative features triggering passively, on entry, or at round end. Resolved via player saving throws (Slink or Tough) against the Zone Profile. GM never rolls dice!
  * *Burning (Hazard):* Slink vs. Zone Profile or take 1 Wound (Boss) / 1 Size damage (Mob).
  * *Narrow (Obstacle):* Max Size 2 Mobs without penalty. Size 3+ suffer Bane 1 (-1d) on attacks/physical tests and 1 Zone speed cap.
  * *Slippery (Obstacle):* Slink vs. Zone Profile or fall Prone.
  * *Smoky (Obstacle):* Ranged attacks suffer Bane 1 (-1d); grants Partial Cover.
  * *Toxic (Hazard):* Tough vs. Zone Profile or gain Weakened condition.
  * *Deep Water (Obstacle):* Move action travels only 1 Zone; Tough test or begin drowning (1 Wound/round).
* **Opportunities (Features & Treats):** Interactive or tactical features:
  * *High Ground:* +1d Boon to ranged attacks made from zone; -1d Bane to melee attacks entering zone.
  * *Junk Pile:* Manipulate action (Notice vs. Zone Profile) finds throwable weapon or scrap.
  * *Shadowy:* +1d Boon to Slink stealth tests.
  * *Shoring:* Manipulate or Attack action collapses supports, creating Crumbling hazard and blocking passage.

---

## Formal Markdown Schemas for Content Instances

### 1. Lair Room / Asset Schema

```markdown
### [Asset Name]
- **Category / Type:** [Person: Elder | Person: Specialist | Person: Captive | Facility: Industry | Facility: Swarm | Facility: Beasts | Facility: Defense | Ally: Outcast | Blueprint]
- **Tier:** [Tier 1–4]
- **Construction Cost:** [X Base Loot, Y Base Scrap (or "None / Recruited / Discovered")]
- **Requirements & Prerequisites:** [Warren Tier X, Territory / Mine / Dungeon required, or specific Elder staffed]
- **Upkeep:** [None | X Loot per Lair Turn | 1 Laborer Die per turn]
- **Passive Benefit (Boon):** [Exact mechanical modification or passive yield per Lair Turn]
- **Active Function / Crafting Station:** [Downtime Action enabled, Quality unlock, or Taming modifier]
- **Volatility & Cost (Bane / Catch):** [Complication trigger, flight risk, mutiny risk, or hazard]
- **Dominance Kickback:** [Exclusive mechanical perk granted to the Gang holding Dominance]
- **Upgrade Tiers:** [Path to upgrade to higher Tier and associated costs]
```

### 2. Loot Item / Salvage Schema

```markdown
### [Item Name]
- **Category:** [Pocket Scrap | Scrappy Plunder | Fine Treasure | Masterwork | Mythic Relic | Oddity | Chassis | Consumable]
- **Quality Tier:** [T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary]
- **Bulk:** [0 | 1 | 2 | 3 | 4+]
- **Loot Value (LV):** [Quantity of Tier units, e.g. 1x T2, 3x T3, 10x T5]
- **Scrap Yield:** [Quantity of Scrap recovered if smelted/dismantled in Lair]
- **Divisibility:** [Divisible (can be split into individual tokens) | Indivisible (single solid object)]
- **Special Utility / Crafting Tag:** [Attached Oddity (Tier/Bite), Weapon/Armor Tag, or Blueprint schematic]
- **Description:** [Brief Tier B/C physical description]
```

### 3. Journey Hazard / Event Schema

```markdown
### [Hazard / Event Name]
- **Hazard Type:** [Environmental Obstacle | Ambush & Predator | Weather & Attrition | Social & Infighting | Trap & Debris]
- **Zone / Terrain Tag:** [Underground / Sewer | Forest / Wilds | Mountain / Chasm | Ruins / Keep | Swamp / Mire | Wasteland]
- **Target Role:** [Map-Scrawler (Brains) | Sniffer (Slink) | Scavver (Tough) | Loud-Mouth (Mouth)]
- **Trigger Condition:** [Route Test Failure | Travel Event Roll (1–6) | High Loot Weight]
- **Hazard Check & Difficulty:** [Stat tested against Target Number, e.g., Slink 5+/1 or Tough 5+/2]
- **Failure Consequence:** [Exact mechanical penalty: Mob Attrition damage, Boss Grit loss, Lost Bulk, Condition applied, or Alert increase]
- **Success Outcome:** [Hazard bypassed, Mob healed, Boon granted, or bonus Loot secured]
- **Mitigating Action / Avoidance:** [Equipment, Oddity, or alternative cost that bypasses the roll]
```

---

## Comprehensive Mechanical Gap Analysis

The following 10 mechanical gaps, currency inconsistencies, and broken loops were identified during domain extraction:

### `[MISSING RULE / GAP: Economy Currency Normalization & Tiered Conversion]`
- **Description:** `31_loot.md` defines Loot Value on a 5-to-1 exponential scale (T1–T5). However, `00_Lair_Rules.md` lists flat costs like "10 Loot, 15 Scrap" for room construction and "5 Loot" for Downtime bribes/pitches, without specifying the Tier of Loot required. Furthermore, `12_Gang.md` grants 1 Infamy Mark per "10 Loot Value" contributed. If a single T5 Relic equals 6,250 T1 units, contributing one T5 item would grant 625 Infamy Marks, instantly maxing Gang Infamy 40 times over.
- **Why it is needed:** The macro progression and Lair construction loops collapse into either hyper-inflation or complete ambiguity if currency tiers are not strictly normalized.
- **Suggested Resolution:** 
  1. Define all flat Lair construction and upkeep costs in **T1 Base Scrap** and **T1 Base Loot** (or require matching Tier tokens: e.g., Tier 2 rooms cost T2 tokens, Tier 3 rooms cost T3 tokens).
  2. Normalize Infamy Mark generation to require **10x T1** for Infamy 1, **10x T2** for Infamy 2, **10x T3** for Infamy 3, etc., or award 1 Infamy Mark per completed raid contribution threshold regardless of excess raw tier value.

### `[MISSING RULE / GAP: Retaliatory Lair Assault Resolution Engine]`
- **Description:** `00_Lair_Rules.md` states that reaching Threat Level 5 triggers a "Retaliatory Assault" against the Lair, after which Threat resets to 2. However, there are no mechanical rules for how this assault is resolved: there are no enemy force statblocks, no rules for how defense facilities (like Trapped Palisade rolling 3d6) apply damage, no mass-combat roll framework, and no defined consequences if the players lose the defense (e.g., destroyed rooms, slaughtered Gobbo Pool, stolen Hoard).
- **Why it is needed:** Threat Level 5 is the primary external pressure clock in the game. Without resolution and failure rules, regional heat has zero teeth.
- **Suggested Resolution:** Establish a formal 3-step Lair Defense procedure:
  1. Determine Enemy Assault Force based on Warren Tier and Threat level.
  2. Automated Defense Phase: Roll active Defense Facilities (e.g. 3d6 from Palisade) and assign Laborer Dice to inflict damage before breach.
  3. Tactical Skirmish / Breach Phase: If enemies survive, resolve a quick skirmish in the Lair Entrance Zone using Bosses and Raider Mobs. If defeated, the Lair suffers 1 destroyed Asset, loses 1d6 from the Gobbo Pool, and loses half its Communal Hoard.

### `[MISSING RULE / GAP: Mutiny Resolution Mechanics & Facility Recovery]`
- **Description:** At Swarm Mood 5, a "Mob Mutiny" locks one random Lair facility and forces grunts to demand upfront bribes of 5 Loot per Mob to embark on raids. The rules do not define how a locked facility is unlocked, what happens if the players refuse to pay bribes, or how mutiny is suppressed without money.
- **Why it is needed:** Mutiny is the internal pressure clock. Players need actionable mechanical paths (e.g. intimidation, brawling, sacrificing elders) to break a strike.
- **Suggested Resolution:** Codify Mutiny suppression options:
  1. *Bribe:* Pay 5 T1 Loot per Mob to clear the raid lockout.
  2. *Tyrant's Beatdown:* A Boss makes an opposed **Tough 5+/2** or **Mouth 5+/2** test as a Downtime Action. Success reduces Swarm Mood to 3 and unlocks the facility; failure inflicts 1 Wound on the Boss and increases Threat by +1 from the riot.

### `[MISSING RULE / GAP: Asset Decommissioning, Destruction, and Slot Recovery]`
- **Description:** A Lair can maintain up to `(Tier * 2) + 2` active assets. If players wish to replace an obsolete Tier 1 facility with an advanced Tier 3 workshop, there are no rules for demolishing, dismantling, or selling off existing assets, nor is it clear if dismantling returns Scrap to the Hoard.
- **Why it is needed:** Hard asset caps force players to cycle assets as they level up.
- **Suggested Resolution:** Add a **Dismantle Asset** Downtime action: spending 1 Laborer Die dismantles an existing facility, frees the asset slot immediately, and recovers 50% of its base Scrap cost into the Communal Hoard.

### `[MISSING RULE / GAP: Mid-Raid Boss Death & Successor Spawning Timing]`
- **Description:** `15_Level_Up and death.md` describes the "Next Gobbo Up" successor generation rules. However, it does not specify what happens *in the middle of a raid* when a Boss dies. Does the player sit out the rest of the session? Does the next biggest runt in their Mob immediately promote to Boss status mid-combat? If promoted mid-raid, what are their starting Grit and action limits?
- **Why it is needed:** Player elimination during tactical skirmishes ruins table engagement and violates Tenet 1 (Fun at the Table).
- **Suggested Resolution:** Implement the **"Instant Promotion"** rule: If a Boss dies during combat and commands an active Mob, the player immediately promotes the leading runt of that Mob into a makeshift Boss (with 3 Grit, 1 in all stats, and current Mob Size reduced by 1). Full successor generation and XP allocation take place during Homecoming. If no Mob survives, the player controls unassigned Mobs or runts until Homecoming.

### `[MISSING RULE / GAP: Codified Extraction Phase & Chase Mechanics]`
- **Description:** While Journey rules handle travel to and from the site, there is no mechanical framework for the transition between combat/plunder and extraction. If Alert reaches high levels, there are no rules for whether enemies chase the party into the return journey, or how players disengage from the dungeon node to start the return stages.
- **Why it is needed:** The "Extraction / Escape" phase is one of the four foundational raid pillars in the design tenets, but currently lacks dedicated mechanics.
- **Suggested Resolution:** Define the **Extraction Trigger**: Once the party declares Extraction, each Zone between their current location and the entrance must be traversed. If Alert is 4+, each exit transition triggers an immediate **Slink 5+/1** evasion test; failure inflicts 1 Attrition damage on all Mobs and carries +1 Alert into the Return Journey.

### `[MISSING RULE / GAP: Formal Patron Saint Ledger & Appeasement Trigger System]`
- **Description:** `15_Level_Up and death.md` introduces Patron Saints from the Bone Pile with situational boons and behavioral appeasement catches. However, there are no rules governing: (a) how many Patron Saints a Gang can maintain; (b) the exact mechanical trigger for losing/restoring the boon; (c) the minimum criteria for a dead Boss to qualify as a Saint vs. a generic Skull.
- **Why it is needed:** Patron Saints provide key roguelite meta-progression, but currently read as loose flavor suggestions.
- **Suggested Resolution:** 
  1. A Boss can attune to exactly **1 Patron Saint** from their Gang's Bone Pile during character creation/Homecoming.
  2. Qualifying as a Saint requires the dead Boss to have reached at least **Level 3 in one stat** or earned at least **5 Lifetime Glory**.
  3. If the active Boss violates the Saint's behavioral catch during a raid, the boon is disabled for the remainder of that raid and the subsequent Lair Phase.

### `[MISSING RULE / GAP: Journey Terrain Difficulty Mapping & Transit Alert Coupling]`
- **Description:** `00_Journey_Rules.md` sets a flat Route Test of `Brains 5+/1`, with no scaling for difficult wilderness (mountains, swamps, tundra) vs. easy roads. Furthermore, travel complications (such as the Loud-Mouth screaming or failing a Shadow Ambush) do not feed into the starting Alert level of the upcoming raid.
- **Why it is needed:** Travel should feel mechanically tied to the raid environment and create tactical stakes for loud failures during transit.
- **Suggested Resolution:** 
  1. Map Terrain Types to Route Test profiles: Mild Wilds = `5+/1`, Harsh Swamp/Mountains = `5+/2`, Perilous Wasteland = `6/2`.
  2. Travel Failures that generate noise or reveal tracks add **+1 to Starting Alert** at the raid location.

### `[MISSING RULE / GAP: Private Gang Hoard vs. Communal Hoard Economy]`
- **Description:** `00_Lair_Rules.md` introduces "The Skim" Downtime Action allowing a Boss to secretly steal Loot into their "Gang's Private Hoard". However, the rules never define what a Gang's Private Hoard can be spent on versus the Communal Hoard, or whether Private Hoard wealth counts toward Infamy Marks.
- **Why it is needed:** Without distinct mechanical uses (e.g. buying personal gear/oddities without table consensus, hiring private bodyguards, or purchasing Dominance), the Skim action has no tactical purpose.
- **Suggested Resolution:** Clarify that the **Communal Hoard** is spent strictly by group consensus for Lair upgrades and shared outfitting, while a **Gang's Private Hoard** is spent exclusively by that player to purchase personal gear, bribe Elders for personal perks, or buy unshared Mob upgrades. Wealth in the Private Hoard only grants Infamy Marks when deposited into the Communal Hoard.

### `[MISSING RULE / GAP: Mob Attrition Damage vs. Single Health Die Tracking]`
- **Description:** In `00_Journey_Rules.md`, Route Test failure deals "1 Attrition (every Mob takes 1 damage to its active health die)". However, Mob damage rules in `13_Goblin_mob.md` track Mob health using a pool of d6s. The travel rules do not clarify whether Attrition damage spills over between dice, or if a Size 3 Mob with three full d6s just ticks down its lowest die.
- **Why it is needed:** Inconsistent damage application across travel and combat creates confusion for table runners.
- **Suggested Resolution:** Explicitly state that Travel Attrition applies standard combat damage resolution: damage reduces the current lowest health die of the Mob's pool; when a die reaches 0, it is removed and Mob Size decreases by 1.

---

## Conclusion

This report completes the systemic extraction for Domain 1 (The Raid Loop & Economy), Domain 2 (The Lair Loop & Roguelite Progression), and Domain 3 (Journeys & Hazard Resolution). All living content tables have been abstracted into standardized Markdown Schemas with explicit extension points, and all 10 systemic gaps and currency ambiguities have been formally identified and resolved.
