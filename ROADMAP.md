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
*   **Feature 2.2: Mutations (Chaos Traits)**
    *   [ ] **Story:** Establish how Mutations are acquired (e.g., radiation, magical mishaps, potions).
    *   [ ] **Task:** Create a D20 table of chaotic, double-edged physical Gobbo mutations.

### Epic 3: Words of Chaos (Goblin Magic)
*Goal: Build the push-your-luck spellcasting system using Brains dice pools.*
*   **Feature 3.1: Magic Dice Casting (GDR-005)**
    *   [x] **Story:** Finalize the pattern-matching "Lock & Push" casting loop and Success Set matching spell tiers.
    *   [x] **Story:** Define "Chaotic Leakage" side-effects based on non-success sets.
    *   [ ] **Task:** Create the draft files in the magic directory (`01_STAGE_Drafts/08_Magic/`).
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
*   **Feature 4.2: Power Word Slots**
    *   [x] **Story:** Establish "Power Word Slots" for memorizing magic based on the Brains stat.

### Epic 5: Communal Crafting (Scrap-Taping)
*Goal: Allow Goblins to build unstable custom weapons and armor.*
*   **Feature 5.1: The Custom Gear Loop (GDR-003)**
    *   [x] **Story:** Draft the Crafting Roll (Taming Successes vs. Chaos 1s), Break Roll, Scrap Cascade, and Blueprints (`34_Crafting.md`).
    *   [x] **Story:** Define the Element Synthesis constraint rules.
    *   [ ] **Task:** Rules Lawyer Audit: Validate Bite level balances (B0–B3) and Workshop Level constraints.

### Epic 6: Base Building (The Lair Boardgame)
*Goal: Upgrade the shared base using pooled gold and turf dominance rules.*
*   **Feature 6.1: Communal Rooms**
    *   [x] **Story:** Establish the Lair Currency logic (Raw Loot Value vs. physical salvage like an Anvil).
    *   [x] **Task:** Create a draft of Lair upgrade rooms in the base directory (`01_STAGE_Drafts/05_Base/`).
*   **Feature 6.2: Gang Dominance**
    *   [x] **Story:** Define rules for how Gangs assert dominance over specific upgrades to claim exclusive bonuses.

---

## 💀 LOOP 3: The Legacy & Generation Leap (Roguelite Core)
*Goal: Drive the "Next Gobbo Up" metagame. Boss deaths fuel Gang power and new character advances.*

### Epic 7: The Bone Pile & Patron Saints
*Goal: Ensure character death is rewarding and leaves a permanent mark.*
*   **Feature 7.1: Ancestral Legacy**
    *   [ ] **Story:** Draft a table of 10 Patron Saint Boons and Catches based on dead PC histories (`15_Level_Up and death.md`).
    *   [ ] **Task:** Define how Named Items inherit magical traits upon a Boss's death.
    *   [ ] **Task:** Draft the Bone Oddity trait creation table.

### Epic 8: Gang Progression
*Goal: Standardize the Gang as the persistent leveling "Class".*
*   **Feature 8.1: Infamy & Shenanigans**
    *   [ ] **Task:** Define the "Frenzy/Go-go-go" pool reward rules when players trigger "For Fuck Sake" Shenanigan compulsions (`12_Gang.md`).
    *   [ ] **Task:** Draft rules for Gang-specific personal raid missions (Agendas).
*   **Feature 8.2: Retirement**
    *   [ ] **Story:** Standardize Elder Benefits by drafting a table of 3–5 passive gang boons (`15_Level_Up and death.md`).

---

## 🗺️ Campaign & GM Tools
*Goal: Help the GM generate adventures and run enemies easily.*

### Epic 9: Travel & Adventure
*Goal: Structure travel and raids.*
*   **Feature 9.1: Hex & Point Crawl Travel**
    *   [x] **Story:** Define macro-movement and food attrition mechanics for large mobs on the road (`01_STAGE_Drafts/07_Travel/`).
*   **Feature 9.2: Raid Extraction**
    *   [ ] **Story:** Define objective scaling and extraction points.

### Epic 10: GM Arsenal
*Goal: Monster stat blocks and encounter generation.*
*   **Feature 10.1: Unified Mobs & Scale (GDR-004)**
    *   [x] **Story:** Establish the three-layer enemy trait hierarchy (Ancestries, Standard Tags, Unique Statblock Traits).
    *   [x] **Story:** Finalize the deterministic Enemy Mob attack formula and Dice-HP mechanics (`20_Enemies.md`).
*   **Feature 10.2: Bestiary & Hazards**
    *   [ ] **Task:** Stat 5 common minion units and 3 Boss/Elite monsters using the Wounds overkill rule.
    *   [ ] **Task:** Create random Loot Tables (Shiny vs. Useful) and Trap/Hazard tables.

### Epic 11: Physical Play Tools
*   [ ] **Task:** Design the Boss Character Sheet (with the Bone Pile tracker).
*   [ ] **Task:** Design the Mob/Gang Tracker Sheet.
