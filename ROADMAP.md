# Gobbos Product Roadmap

**Role: The Product Owner**  
**Release Goal: v1.0 (The Minimum Viable Rulebook)**

This roadmap is organized around the **three core gameplay loops** of Gobbos. By grouping features and tasks by their operational loop rather than raw directories, we keep our design aligned with the core tenets: fast tactical fun, zero post-roll math, high chaos, goblin flavor, and meaningful roguelite progression.

---

## ⚔️ LOOP 1: The Raid (Tactical Skirmish)
*Goal: Solidify the in-raid engine. Players command mobs, use Quirks, and cast volatile magic in active zones.*

### Epic 1: Combat Chassis (Physics & Morale)
*Goal: Establish baseline movement, actions, and morale resolution.*
*   **Feature 1.1: Fleeing & Rallying Mechanics**
    *   [ ] **Task:** Define PC and Mob Fleeing mechanics during active combat (`02 Combat.md`).
    *   [x] **Task:** Solidify Enemy Regrouping/Rallying mechanics (`20_Enemies.md`).
*   **Feature 1.2: Uncontrolled Mob Chaos**
    *   [ ] **Task:** Define "Terrifying Enemy" conditions that trigger uncontrolled panic (`13_Goblin_mob.md`).
    *   [ ] **Task:** Integrate "For Fuck Sake" (Quirks/Chaos) into the Uncontrolled Mob behavior priority list.
*   **Feature 1.3: Zero Dice Pools & Salvage Rolls**
    *   [x] **Task:** Formalize the 0d6 Dice Pool Salvage Roll (rolling 1d6: 6=1 Success, 1=Fumble) into core dice rules (`01_Dice.md`).
    *   *Source:* [Rules Lawyer System Audit Report](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Rules_Lawyer_System_Audit_Report.md)
*   **Feature 1.4: Zone Profiles & Modular Battlefield Traits**
    *   [ ] **Story:** Standardize ICRPG-style Zone Profiles (Difficulty + TN, e.g., Normal:1, Hard:1) for all room traversal and environmental interactions (`03_Movement & Zones.md`).
    *   [ ] **Task:** Implement modular Zone Problems (*Burning, Narrow [Mob Size 2 Cap], Slippery [Prone], Smoky [Cover], Toxic, Deep Water*) and Opportunities (*High Ground, Junk Pile, Shadowy, Shoring*).
    *   *Source:* [GDR-006: Environmental Hazards & Zone Statblocks](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/GDRs/GDR-006_Environmental_Hazards_and_Zone_Statblocks.md), [Researcher Findings: Environmental Hazards](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Researcher_Findings_Environmental_Hazards.md)
*   **Feature 1.5: Static Resistances & Opposed Tests**
    *   [ ] **Task:** Standardize player-facing opposed rolls against static enemy stats (e.g., wrestling vs Toughness, sneaking vs Notice) without GM rolling.
    *   *Source:* [Static Resistances & Opposed Tests](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Static_Resistances_Opposed_Tests.md)

### Epic 2: The Boss Engine (Stats & Quirks)
*Goal: Give players the tools to build and play unique goblin leaders.*
*   **Feature 2.1: The Quirks & Twists Framework**
    *   [x] **Story:** Establish the fundamental modular powers architecture (Acquisition Limits, Costs, and Keywords in `16_Unified_Modular_Powers_System.md`).
    *   [ ] **Task:** Rules Lawyer Audit: Define core mechanics in the index (`06_Keywords Index.md`):
        *   **Grit** (Health and resilience)
        *   **Size** (for PCs vs. Mobs)
        *   **Cover** (Partial vs. Full Cover)
        *   **Standard / Free Actions**
        *   **Status Effects** (Prone, Stunned, Bleeding, Poisoned)
    *   [ ] **Task:** Draft the General, Tough, Slink, Mouth, and Brains Quirk/Twist master tables (`14_Quirks.md`).
    *   *Source:* [Initial Trick List](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Initial_Trick_List.md), [Trick Mechanics Master List](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Trick_Mechanics_Master_List.md)
*   **Feature 2.2: Mutations (Chaos Traits)**
    *   [ ] **Story:** Establish how Mutations are acquired (radiation, magical mishaps, potions).
    *   [ ] **Task:** Create a D20 table of chaotic, double-edged physical Gobbo mutations.

### Epic 3: Words of Chaos (Goblin Magic)
*Goal: Build the push-your-luck spellcasting system using Brains dice pools.*
*   **Feature 3.1: Magic Dice Casting (GDR-005)**
    *   [x] **Story:** Finalize the pattern-matching "Lock & Push" casting loop and Success Set matching spell tiers.
    *   [x] **Story:** Define "Chaotic Leakage" side-effects based on non-success sets.
    *   [ ] **Task:** Create the draft files in the magic directory (`01_STAGE_Drafts/08_Magic/`).
    *   *Source:* [GDR-005: Goblin Magic Dice System](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/GDRs/GDR-005_Goblin_Magic_Dice_System.md)
*   **Feature 3.2: Power Words & Mishaps**
    *   [ ] **Story:** Define the master list of Power Words (Narrative Tags) available to mages.
    *   [ ] **Task:** Draft the "Magical Mishap/Fumble" table for when players Farkle on casting.

---

## ⛺ LOOP 2: The Lair & Downtime (Metagame & Crafting)
*Goal: Resolve the downtime loop. Players pool loot, upgrade their base, and scrap-craft custom gear.*

### Epic 4: Greed & Gear (The Economy)
*Goal: Standardize found items, carrying, and base resource rules.*
*   **Feature 4.1: Equipment Alignment**
    *   [ ] **Task:** Rewrite `33_Equipment.md` to define standard weapons/armor as base zero-Oddity chassis.
    *   [ ] **Task:** Resolve `TBD` tags for Weapon traits: `Cutting`, `Poking`, `Short`.
    *   [ ] **Task:** Resolve `TBD` tags for Armor traits: `Light`.
    *   *Source:* [Rules Lawyer Audit: Equipment](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Rules_Lawyer_Audit_Equipment.md), [Equipment Framework Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Equipment_Framework_Brainstorm.md)
*   **Feature 4.2: Power Word Slots**
    *   [x] **Story:** Establish "Power Word Slots" for memorizing magic based on the Brains stat.

### Epic 5: Communal Crafting (Scrap-Taping)
*Goal: Allow Goblins to build unstable custom weapons and armor.*
*   **Feature 5.1: The Custom Gear Loop (GDR-003)**
    *   [x] **Story:** Draft the Crafting Roll (Taming Successes vs. Chaos 1s), Break Roll, Scrap Cascade, and Blueprints (`34_Crafting.md`).
    *   [x] **Story:** Define the Element Synthesis constraint rules.
    *   [ ] **Task:** Rules Lawyer Audit: Validate Bite level balances (B0–B3) and Workshop Level constraints.
    *   *Source:* [GDR-003: Unified Modular Powers System](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/GDRs/GDR-003_Unified_Modular_Powers_System.md), [Crafting Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/crafting-brainstorm.md)
*   **Feature 5.2: Scrap Cascade & Scarred Oddities**
    *   [ ] **Task:** Define the Oddity Survival check upon gear break; surviving Oddities gain +1 permanent Bite as "Scarred Oddities".
    *   *Source:* [Creative Genius Crafting Analysis](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/creative_genius_crafting_analysis.md)
*   **Feature 5.3: Blueprints & Mob-Scale Crafting**
    *   [ ] **Task:** Establish physical, tradeable Blueprints from Reverse Engineering.
    *   [ ] **Task:** Define Mob-Scale consumable crafting (mass-producing 1-raid modifications like burning arrows or spiked bucklers).
    *   *Source:* [Creative Genius Crafting Analysis](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/creative_genius_crafting_analysis.md)
*   **Feature 5.4: Master d66 Oddities Table**
    *   [ ] **Task:** Implement the master catalog of 36 distinct Oddities with Tiers, Bites, and Rebounds.
    *   *Source:* [Crafting Framework & Oddities Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/crafting_framework_brainstorm.md)

### Epic 6: Base Building (The Lair Boardgame)
*Goal: Upgrade the shared base using pooled gold and turf dominance rules.*
*   **Feature 6.1: Communal Rooms & Labor Engine**
    *   [x] **Story:** Establish the Lair Currency logic (Raw Loot Value vs. physical salvage).
    *   [x] **Task:** Create a draft of Lair upgrade rooms and Gobbo Pool labor assignment (`01_STAGE_Drafts/05_Base/00_Lair_Rules.md`).
    *   *Source:* [Lair System Refined Framework](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_System_Refined_Framework.md), [Lair Mechanics Game Engineering Audit](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_Mechanics_Game_Engineering_Audit.md)
*   **Feature 6.2: Gang Dominance**
    *   [x] **Story:** Define rules for how Gangs assert dominance over specific upgrades to claim exclusive kickbacks.
    *   *Source:* [GDR-002: Gang Pillar & Lair Economy](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/GDRs/GDR-002_Gang_Pillar_And_Lair_Economy.md)
*   **Feature 6.3: The "Pitch" Mechanic (Mouth vs. Wallet)**
    *   [x] **Task:** Draft rules for pitching raids to Grunts (pay upfront from Hoard vs. Mouth test promising riches; failure spikes Mob Mutiny).
    *   *Source:* [Lair Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_Brainstorm.md)
*   **Feature 6.4: The Loot "Skim" (Lair Tax Evasion)**
    *   [x] **Task:** Draft Slink test mechanics for hiding choice loot from Lair tax collectors into the Gang's private Hoard.
    *   *Source:* [Lair Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_Brainstorm.md)
*   **Feature 6.5: Lair Downtime Activities Menu**
    *   [x] **Task:** Define 1–2 Downtime Actions per Boss: Goblin Bar Fights (Tough test for Infamy/Loot), Rumormongering (bribe for dungeon intel), and Wild Beast Taming (Tough/Brains test to unlock mount archetypes).
    *   *Source:* [Lair Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_Brainstorm.md), [Researcher Findings: Base Building](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Researcher_Findings_Base_Building.md)

---

## 💀 LOOP 3: The Legacy & Generation Leap (Roguelite Core)
*Goal: Drive the "Next Gobbo Up" metagame. Boss deaths fuel Gang power and new character advances.*

### Epic 7: The Bone Pile & Patron Saints
*Goal: Ensure character death is rewarding and leaves a permanent mark.*
*   **Feature 7.1: Ancestral Legacy & Patron Saints**
    *   [ ] **Story:** Draft a table of 10 Patron Saint Boons and Catches based on dead PC histories (`15_Level_Up and death.md`).
    *   [ ] **Task:** Define how Named Items inherit magical traits upon a Boss's death.
    *   *Source:* [Gang Mechanics Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md)
*   **Feature 7.2: Generational Grudges & Phobias**
    *   [ ] **Task:** Define rules where a Boss's manner of death inflicts a permanent Grudge (+1d attack) and Phobia (-1d morale) on the Gang's next generation.
    *   *Source:* [Gang Mechanics Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md)
*   **Feature 7.3: The Deeds & Scars Advancement Framework**
    *   [ ] **Task:** Draft in-raid chaotic Deeds required to unlock high-tier Quirks, and a 0-Grit survival Scar Table for permanent bodily alterations.
    *   *Source:* [Research: Deeds & Award Mechanics](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Research_Deeds_Award_Mechanics.md)
*   **Feature 7.4: Bone Oddities & Ancestral Relics**
    *   [ ] **Task:** Define mechanics for harvesting bones from dead Bosses in the Bone Pile to craft custom Relic Oddities.
    *   *Source:* [Gang Mechanics Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md), [Creative Genius Crafting Analysis](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/creative_genius_crafting_analysis.md)

### Epic 8: Gang Progression
*Goal: Standardize the Gang as the persistent leveling "Class".*
*   **Feature 8.1: Infamy & Shenanigans**
    *   [ ] **Task:** Define the "Frenzy/Go-go-go" Bangaranga reward rules when players trigger "For Fuck Sake" Shenanigan compulsions (`12_Gang.md`).
    *   [ ] **Task:** Draft rules for Gang-specific personal raid missions (Agendas).
    *   *Source:* [Gang Mechanics Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md)
*   **Feature 8.2: Retirement & Elder Benefits**
    *   [ ] **Story:** Standardize Elder Benefits by drafting a table of 3–5 passive gang boons (`15_Level_Up and death.md`).
    *   *Source:* [Lair System Research Deep Dive](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_System_Research_Deep_Dive.md)
*   **Feature 8.3: Mob Mutiny Gauge & Pre-Raid Wagers**
    *   [ ] **Task:** Define the Mob Mutiny meter (tracking failed orders and high Infamy ego) and pre-raid Inter-Gang Wagers.
    *   *Source:* [Gang Mechanics Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md)
*   **Feature 8.4: Mob Veterans & Demand Escalation**
    *   [ ] **Task:** Draft rules for surviving Mobs gaining Veteran Traits while demanding higher loot cuts.
    *   *Source:* [Lair Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_Brainstorm.md)

---

## 🗺️ Campaign & GM Tools
*Goal: Help the GM generate adventures and run enemies easily.*

### Epic 9: Travel & Adventure
*Goal: Structure travel and raids.*
*   **Feature 9.1: Hex & Point Crawl Travel**
    *   [x] **Story:** Define macro-movement and food attrition mechanics for large mobs on the road (`01_STAGE_Drafts/07_Travel/00_Journey_Rules.md`).
*   **Feature 9.2: Dedicated Travel Roles & Laden Logistics**
    *   [ ] **Task:** Formalize the 4 travel roles (Map-Scrawler, Sniffer, Scavver, Loud-Mouth) and Laden/Over-Laden return penalties with panic loot jettisoning.
    *   *Source:* [TargetMechanic.csv](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/TargetMechanic.csv), [Journey Rules](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/07_Travel/00_Journey_Rules.md)
*   **Feature 9.3: Raid Extraction & Supply Outpost Interception**
    *   [ ] **Story:** Define objective scaling and Outpost Supply Interception danger checks.
    *   *Source:* [Lair System Refined Framework](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Lair_System_Refined_Framework.md)

### Epic 10: GM Arsenal
*Goal: Monster stat blocks and encounter generation.*
*   **Feature 10.1: Unified Mobs & Scale (GDR-004)**
    *   [x] **Story:** Establish the three-layer enemy trait hierarchy (Ancestries, Standard Tags, Unique Statblock Traits).
    *   [x] **Story:** Finalize the deterministic Enemy Mob attack formula and Dice-HP mechanics (`20_Enemies.md`).
    *   *Source:* [GDR-004: Enemy Stat Framework & Mobs](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/GDRs/GDR-004_Enemy_Stat_Framework_And_Mobs.md)
*   **Feature 10.2: Enemy Automata (Tick-Tock Clocks & Priority AI)**
    *   [ ] **Task:** Standardize deterministic round action clocks and 3-step priority AI lists for Boss/Elite monsters.
    *   *Source:* [Enemy Threat Framework Brainstorm](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/Enemy_Modular_Threat_Framework_Brainstorm.md)
*   **Feature 10.3: Bestiary & Hazards**
    *   [ ] **Task:** Stat 5 common minion units and 3 Boss/Elite monsters using the Wounds overkill rule.
    *   [ ] **Task:** Create random Loot Tables (Shiny vs. Useful) and Trap/Hazard tables.

### Epic 11: Physical Play Tools
*   [ ] **Task:** Design the Boss Character Sheet (with the Bone Pile tracker).
*   [ ] **Task:** Design the Mob/Gang Tracker Sheet.
