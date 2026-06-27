# Developer Guide & Systems Audit: The Modular Power Blueprint
**Target:** `00_DEV_Brainstorms/Unified Modular Power System.md` and 6 `.csv` files  
**Date:** June 23, 2026  
**Auditor:** Antigravity (Rules Lawyer, Systems Analyst & Game Mechanics Engineer)

---

## Part 1: Systems Evaluation (Game Mechanics)

### 1. Verdict: Keep and Refine

**Verdict:** **DO NOT DITCH.** 

Decomposing game abilities into distinct "Lego bricks" is an excellent backend framework for developer alignment, GM adjudication, and content expansion. It guarantees that any new Quirk, magic spell, or crafted item hooks directly into the core engine variables without introducing term bloat or mechanics conflicts.

Rather than a mathematical points system, this blueprint works best as a **Developer Design Card** template to draft and archive custom content.

### 2. The Power Blueprint Template
Use this template to draft and archive any new Quirk, Oddity, spell, or Mob trait:

```markdown
### [Power/Item Name]
*   **Target Sockets:** [Which core rules, stats, or trackers does this modify?]
*   **The Change:** [What baseline rule is altered, bypassed, or injected?]
*   **The Reach:** [Who or what does this affect, at what range, or across what area?]
*   **The Timing:** [Under what specific tactical triggers or conditions does this activate?]
*   **The Cost:** [What resources, actions, or structural sacrifices are paid to use it?]
*   **The Duration:** [How long does this altered rule-state persist before clearing?]
```

---

## Part 2: Rules Lawyer Audit (Systems Alignment)

This section evaluates how the variables defined in the six `.csv` files align with the active rulebooks in `PROD_Core_Rules/` and `STAGE_Drafts/`. 

### 1. Terminology Mismatches (Keyword Consistency)
To maintain searchability and prevent rules confusion, several variables in the `.csv` files must be renamed to match their exact keywords in the core rules:

| CSV Variable Name | Correct Rules Keyword | Source File Reference |
| :--- | :--- | :--- |
| `Movement Speed (Zone Velocity)` | **Movement** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |
| `Max Mobs Limit` | **Max Mobs** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |
| `Free Orders Allocation` | **Free Orders** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |
| `Power Word Slots` | **Power Words** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |
| `Crafting Capacity Limit` | **Crafting Capacity** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |
| `Current/Max Grunt Pool` | **Grunt** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |
| `Mob Size (Tough Pool)` | **Size** | [13_Goblin_mob.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md) |
| `Passive Defense` (US Spelling) | **Passive Defence** | [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) |

---

### 2. Phantom Rules (Non-Existent Mechanics)
The following variables in [TargetMechanic.csv](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/TargetMechanic.csv) refer to mechanics that do not exist in the Stage drafts:
*   **`Chaos Tick Rule` (Row 30)** and **`Mischief Table Tally` (Row 31):**
    *   *The Conflict:* Under [13_Goblin_mob.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md), Uncontrolled Mobs act on their "Inherent Nature" priorities (Survival > Loot > Violence). There are no background roll mechanics for "Chaos Ticks" or "Mischief Talley Accumulators."
    *   *The Fix:* Either delete these two target mechanics or draft the underlying subsystems in the Mob rules.

---

### 3. The "Grit" vs. "Wounds" Mismatch
There is a minor logical leak in the core drafts regarding player health:
*   [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/02_PROD_Core_Rules/01_Characters & Mobs/10_Stats.md) tracks player health via **Grit** (e.g., Level 1 Tough = 3 **Grit**).
*   [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md) states: "When a PC's wound reaches 0 he is dead."
*   [20_Enemies.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/04_Enemies/20_Enemies.md) uses **Wounds** exclusively to track elite/Boss enemy health pools.
*   *The Fix:* To maintain keyword integrity, [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md) should be cleaned to use **Grit** for PCs/Bosses (e.g., "When a PC's **Grit** reaches 0..."), reserving **Wounds** strictly for elite enemy health blocks.

---

### 4. Attack Payload Definitions
To ensure deterministic enemies function properly, the framework must explicitly define the modification **Flat Damage/Success Increment**:
*   **Against standard enemies:** The modification adds **automatic successes** to the player's attack pool toward meeting the target's Defence TN.
*   **Against Bosses, PCs, and Mobs:** The modification subtracts **Grit** (for PCs/Bosses) or Mob **Size** (for Mobs) directly on a successful hit.
This matches the golden rule in [16_Unified_Modular_Powers_System.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md).

---

### 5. Action Economy Clarifications
*   **Reactions:** Gobbos does not have a separate "Reaction" action type. A Reaction is simply a saved Standard Action used out of turn. The activation cost `Reaction (Saved Action)` matches this, but the developer guidelines should explicitly note that Reactions draw from the round's 3 Standard Actions.
*   **Free Order Action:** Fits perfectly with Mouth stat progression rules and combat order economies.
