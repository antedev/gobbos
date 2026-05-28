# GDR-001: Macro Audit & Unified Effects Architecture

* **Status:** ACCEPTED
* **Date:** 2026-05-18
* **Designer(s):** User & Agent (Grill Drill-Down Session)
* **Target Folder:** `STAGE_Drafts/` (for confirmed fixes) and `DEV_Brainstorms/` (for design decisions awaiting implementation)

---

## 1. Context: The State of the Game

A full audit of the repository was conducted. Key findings:

- **STAGE has ~27 files** across 7 subfolders. Core combat, dice, stats, mobs, and crafting are well-developed.
- **PROD is empty.** Nothing has been promoted yet.
- **Three major pillars are entirely missing:** Magic (`08_Magic/`), Lair/Base (`05_Base/`), and Travel (`07_Travel/`) — all empty folders.
- **22 TBD/TODO placeholders** exist across STAGE files.
- **Multiple terminology conflicts** existed (now partially resolved).

---

## 2. Phase 1 Decisions (Macro — Locked)

These are foundational rules that apply across the entire game.

### 2.1 — 1s Never Cancel Successes ✅
- **Rule:** 1s and successes are **completely independent tracks**. You count successes. You count 1s. They never interact.
- **Successes** determine if you pass a test (and how well).
- **1s** only matter for Fumbles (2+ 1s with zero successes).
- **Criticals** trigger at 4+ raw successes. 1s do not reduce the success count.
- **Action Taken:** Fixed the contradictory definition in `06_Keywords Index.md` which said "after deducting any 1s." Now reads: *"Rolling 4 or more successes on a single roll. (Note: 1s never reduce your success count.)"*

### 2.2 — "Bite" Is the Canonical Term ✅
- **Rule:** The instability/drawback rating of an Oddity is called **Bite (B)**, on a scale of B0–B3.
- **Retired Term:** "Defect (D)" — this was the old name. All references in `06_Keywords Index.md` have been updated.
- **Action Taken:** All 7 instances of "Defect" in `06_Keywords Index.md` replaced with "Bite."

### 2.3 — Grunt Is Intentionally the Most Complex Stat ✅
- **Rule:** Grunt is the "swagger economy." It deliberately serves as:
  1. Mob size cap
  2. Spendable resource (+1d before roll, reroll 1s after roll)
  3. Lost on Fumbles (if mob nearby)
  4. Gained by killing enemies, crits, or murdering own goblins
  5. Triggers mob rebellion if it drops too low
- **Design Intent:** This overloaded nature IS the goblin fantasy. Clinging to authority, risking it for desperate gambles, losing face in front of your mob.
- **Deferred:** Specific gain/spend tuning is a Phase 3 (Micro-Level) task.

### 2.4 — Missing Pillars Are Development Gaps, Not Design Decisions ✅
- Magic, Lair, and Travel simply haven't been built yet. No design conflict.

### 2.5 — Equipment Is a Subset of the Crafting Framework ✅
- **Rule:** Equipment and Crafting are one unified system. Found/looted items are pre-built items within the Crafting framework (a specific Quality level with zero Oddities).
- **Crafting is the source of truth** for how items work.
- `33_Equipment.md` needs to be rewritten to align with `34_Crafting.md`.
- A knight's sword is mechanically "Standard-quality Medium Weapon, 0 Oddities."

---

## 3. Phase 2 Decisions (Meso — Stats & Effects System)

### 3.1 — Embrace Imbalance (Design Principle) ✅
- **Rule:** Perfect stat balance is NOT a design goal. Asymmetry between stats is fine and even encouraged.
- **Guardrail:** No single stat path should be so dominant that it makes the others *meaningless*. Natural checks and balances exist (e.g., all-Mouth = lots of weak mobs that die easily, no personal survivability).
- Crafting, Tricks, and (eventually) Magic will produce effects that are sometimes wildly overpowered. That's fine as long as it's not *permanently* overpowered.

### 3.2 — Brains Stat Needs Rework (After Magic) 📌 DEFERRED
- **Problem:** Brains' in-raid value is almost entirely dependent on Magic Words and Contraptions — neither of which exist as systems yet.
- **Intent:** The Brainy Goblin fantasy is a blend of **gadgeteer** (weird contraptions, traps, bombs) and **goblin wizard** (chaotic magic). Cunning/scouting is relevant but less rule-heavy.
- **Key Insight:** Brains' power comes through the *items and abilities it unlocks* (Crafting, Magic), not raw dice rolls. Skipping Brains means missing the Crafting avenue, which is a huge power path.
- **Blocked by:** Magic system development.

### 3.3 — Tier (T1–T5) as Universal Power Rating ✅
- **Rule:** Tier becomes the **shared power-level language** across ALL effect systems in the game:
  - Oddity Tier (on items) — already exists
  - Trick Tier (on characters) — NEW
  - Mutation Tier (on bodies) — future
  - Gang Trick Tier (on gangs) — future
- **Each delivery mechanism has its own gatekeeping:**
  - Oddities: gated by Workshop Quality + Bite as self-balancing drawback
  - Tricks: gated by Stat prerequisites (see 3.5)
  - Mutations: TBD
- **Design Goal:** Reusing the same power-rating system everywhere reduces cognitive load. Players learn one scale, not three.

### 3.4 — Boons & Banes Evolves Into Unified Effect Vocabulary ✅
- **Rule:** `13_Boons_and_Banes.md` transforms from early scaffolding into the **authoritative library of atomic mechanical effects**.
- All Tricks, Oddity Tags, Mutations, and Gang effects draw from this shared vocabulary.
- A "+1d when attacking from behind" effect could appear as a Trick, an Oddity Tag, or a Gang Specialty — using the same underlying grammar.
- GMs and players use this as a reference for **power-level calibration** when creating custom content.

### 3.5 — Trick Tier Gated by Stat Level ✅
- **Rule:** To learn a Trick of Tier X, your relevant stat must be ≥ X.
  - Example: A T3 "Head Chopper" requires Tough ≥ 3.
  - Example: A T2 "Spider Climber" requires Slink ≥ 2.
- This mirrors how Workshop Quality gates Oddity Tier in crafting.
- Stat progression literally unlocks access to higher-tier abilities.

### 3.6 — Brains Gates Oddity USE, Not Stockpiling ✅
- **Crafting Capacity** (Brains score) = max Oddities you can **install on one item**.
- **Stockpiling** Oddities in the Lair = a Lair/Hoard system concern (not Brains).
- **Carrying** Oddities on a raid = governed by Bulk.

### 3.7 — Two-Track Trick Architecture (Roguelite Core) ✅
- **Personal Tricks:** Small cap (target: 3–5 slots). Gated by stat level. Can be upgraded to higher Tiers as stats grow. **Die with the character.**
- **Gang Tricks:** Inherited from dead/retired Bosses. Gated by Infamy. Don't count against personal cap. **Persist across generations.**
- **The roguelite loop:**
  1. Early game — fresh Boss, few T1–T2 personal Tricks.
  2. Mid game — personal Tricks at T3, stats climbing, progress slowing.
  3. Soft wall — stats near cap, personal Tricks maxed. Growth plateaus.
  4. Glorious death/retirement — Boss's signature Trick becomes a Gang Trick.
  5. New Boss — starts with fresh personal slots BUT inherits all accumulated Gang Tricks.
- **Power floor protection:** Equipment persists across deaths (Named Items, Gang Hoard). So power level doesn't drop catastrophically on respawn.
- **Stat head start:** New Bosses get Stat Advances equal to Gang Infamy (already in rules). Could be expanded: faster leveling, or more advances from larger Bone Piles.
- **Old rule retired:** The "max Tricks = total sum of all stats" formula (which could reach 17) is replaced by the small personal cap.

---

## 4. Pinned Items (To Be Resolved Later)

| Pin | Topic | Context |
|---|---|---|
| 📌 | **Rename "Tricks"** | User doesn't love the name. Needs something more goblin-flavored. |
| 📌 | **Rename "Oddities"** | Possibly not the best name either. |
| 📌 | **Player cooperation vs. competition** | Can you craft for another player? Trade Tricks? Implications for Gang rivalries. |
| 📌 | **Grunt gain/spend tuning** | Phase 3 balancing task. The economy is right in spirit, may need numerical tuning. |
| 📌 | **Equipment ↔ Crafting rewrite** | `33_Equipment.md` needs full alignment with `34_Crafting.md`. |

---

## 5. Files Modified During This Session

| File | Change |
|---|---|
| `06_Keywords Index.md` L10 | Fixed Critical definition: removed "after deducting any 1s" |
| `06_Keywords Index.md` L47–61 | Replaced all "Defect (D)" with "Bite (B)" |

---

## 6. Remaining Drill-Down Pillars

Phase 2 continues with:
1. **Tricks** — Architecture locked. Needs actual Trick tables built using the new Tier + unified effect vocabulary.
2. **Equipment** — Stale. Needs Crafting alignment. Weapon/Armor traits (Cutting, Poking, etc.) half-TBD.
3. **Combat** — Minor gaps (Fleeing, Cover). Otherwise solid.
4. **Death & Progression** — Multiple Go/No-Go decisions (My Mob My Loot, Raid Boss MVP, Elder Benefits).

>> **GOBLIN VERDICT:** "Da old boss used to call fings by two different names and nobody knew wot woz wot. Now we got ONE word for how bity somefing is, ONE way to measure how strong a power is, and da rules for who gets to keep wot when ya die. Dis is da foundation. Now we build da actual Tricks tables and stop talkin' about it."
