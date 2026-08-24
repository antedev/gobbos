# Changes Log — Remediation Worker 0

**Date**: 2026-08-24T19:55:00+02:00  
**Agent**: `remediation_worker_0`  
**Milestone**: Core Rules Synthesis Remediation  
**Status**: All Tasks Complete & Verified

---

## Summary of Remediations Applied

### 1. `02_PROD_Core_Rules/11_Journeys_and_Hazards.md`
- **Mob Travel Dice Harmonization (Line 51)**:
  - Updated Mob non-Tough travel tests (Slink, Brains, Mouth) from `1d6` to the canonical `2d6` baseline established in `01_Core_Resolution.md` and `06_Mob_Mechanics.md`.
- **Boss Grit Damage Replacement (Lines 118, 133, 147)**:
  - Line 118 (Burning hazard): Replaced `1 Wound (Boss)` with `1 Grit damage (Boss)`.
  - Line 133 (Deep Water hazard): Replaced `begin drowning (1 Wound per round)` with `begin drowning (Bosses lose 1 Grit per round; Mobs suffer 1 Size damage per round)`.
  - Line 147 (Shoring collapse): Replaced `take 1 Wound` with `suffer 1 Grit damage for Bosses / 1 Size damage for Mobs`.
- **Standardized Encumbrance Terminology (Lines 86–98)**:
  - Aligned return travel encumbrance thresholds with `06_Mob_Mechanics.md` and `09_The_Raid_Loop.md` (Laden > 50% capacity; Over-Laden at $\ge \text{Size} \times 4$ Bulk up to dragging limit $\text{Size} \times 5$).
- **Un-fenced Extension Point & Gap Tags**:
  - Removed enclosing code blocks around `[CONTENT EXTENSION POINT: Journey Hazards & Events]` and both `[MISSING RULE / GAP: ...]` callouts so they render as clean, accessible markdown callouts.

### 2. `02_PROD_Core_Rules/10_The_Lair_Loop_and_Progression.md`
- **Boss Damage Terminology (Line 326)**:
  - Replaced `failure inflicts 1 Wound on the Boss` with `failure inflicts 1 Grit damage on the Boss`.
- **Un-fenced Extension Point & Gap Tags**:
  - Removed enclosing code blocks around `[CONTENT EXTENSION POINT: Lair Rooms & Facilities]` and all 5 `[MISSING RULE / GAP: ...]` tags.
- **De-Gendering Tightening**:
  - Adjusted singular "their" in Patron Saint appeasement text to "the Gang's".

### 3. `02_PROD_Core_Rules/09_The_Raid_Loop.md`
- **Un-fenced Extension Point & Gap Tags**:
  - Removed enclosing code blocks around `[CONTENT EXTENSION POINT: Loot & Salvage Items]` and all 3 `[MISSING RULE / GAP: ...]` tags.
- **De-Gendering Tightening**:
  - Adjusted singular "their Gang's Private Hoard" to "the Gang's Private Hoard".

### 4. `02_PROD_Core_Rules/06_Mob_Mechanics.md`
- **Squad Terminology Remediation**:
  - Replaced all occurrences of "squad" and "squads" with "Mob", "Mobs", or "follower units" (Lines 9, 17, 36, 39, 45, 90, 99, 204, 206, 209).
- **Anti-Clunk & De-Gendering Tightening**:
  - Replaced singular "their/them" with "you/your/the Boss's" in lines 3, 156, and 170.
- **Un-backticked Gap Tags**:
  - Standardized `[MISSING RULE / GAP: ...]` tags to un-backticked markdown callouts.

### 5. `02_PROD_Core_Rules/03_Action_Economy_and_Turn_Flow.md`
- **Loot Terminology Remediation (Line 170)**:
  - Replaced `visible treasure caches` with `visible **Loot** caches`.
- **Anti-Clunk / De-Gendering (Line 100)**:
  - Replaced `Dodge or Parry for themselves` with `Dodge or Parry in self-defense`.

### 6. `02_PROD_Core_Rules/02_Boss_Profile_and_Gang.md`
- **Grit Descriptor Cleanup (Lines 34, 53, 61)**:
  - Diagram: Changed `Grit (Health Capacity: 3 to 5)` to `Grit (Damage Capacity: 3 to 5)`.
  - Table: Changed `| Tough Level | Grit (Health Capacity) |` to `| Tough Level | Grit (Damage Capacity) |`.
  - Description: Replaced `Your Boss's hit point capacity` with `Your Boss's damage capacity`.
- **Anti-Clunk / De-Gendering (Line 274)**:
  - Replaced `willingly indulges their Shenanigan` with `willingly indulges your Shenanigan`.

### 7. Chapters 04 & 05 Tag Formatting Harmonization
- `02_PROD_Core_Rules/04_Zones_and_Movement.md`: Un-backticked 2 gap tags.
- `02_PROD_Core_Rules/05_Combat_Engine.md`: Un-backticked 3 extension points and 2 gap tags.
