# ⚖️ Rules Lawyer Audit: Crafting System vs. Stage Rules

> **Scope:** Cross-referencing `crafting-brainstorm.md`, `creative_genius_crafting_analysis.md`, and `crafting_mechanics_audit.md` against all Stage rules (`01_Dice.md`, `02 Combat.md`, `10_Stats.md`, `33_Equipment.md`, `06_Keywords Index.md`, `07_Wounds_Conditions.md`).
>
> **Directive:** The crafting brainstorms supersede `33_Equipment.md` where there is a conflict, as those rules are undercooked.

---

## 🔴 CRITICAL CONFLICTS (Must resolve before Stage draft)

These are hard contradictions between two or more rule texts that cannot coexist.

### CONFLICT 1 — Quality System: Two Incompatible Models

**Source A (`33_Equipment.md`, lines 12–17):**
> Junk: *"Breaks on 1 on the gear dice, cannot be repaired."*
> Scrappy: *"Breaks on 1 on the gear die, can be repaired."*
> Normal: *"Breaks on a Fumble, can be repaired."*
> Superior: *"Never breaks."*

**Source B (crafting-brainstorm Svar 1 + Svar 5):**
The crafting system defines breakage via a **Usage Die** that degrades when a 1 is rolled, and a **T/D notation** (Tier / Defect) that replaces quality tiers with a two-value shorthand.

**Conflict:** The brainstorm model and the Equipment table use completely different mechanics to define the same concept (when does gear break?). The breakage trigger in `33_Equipment.md` fires on "the gear dice" — a term that does not exist anywhere in the dice rules (`01_Dice.md`). There is no such thing as a "gear die" defined in the system.

**Ruling:** `33_Equipment.md` Quality table is **superseded** by the crafting system per the user's directive. The entire Quality table must be deleted and replaced. The term "gear die" / "gear dice" is undefined and must be removed from all rules.

**Action Required:** Delete the Quality table from `33_Equipment.md`. Replace with the T/D framework from the crafting brainstorm when the Stage draft is written.

---

### CONFLICT 2 — The "Gear Die" Is a Phantom Mechanic

**Source A (`33_Equipment.md`, lines 14–17):**
> Repeatedly references "the gear dice" and "the gear die" as a trigger for breakage.

**Source B (`01_Dice.md`):**
> Defines *exactly* two things that generate dice: the **Dice Pool** (Stat + 1) and **Exploding Dice** (rolling extra d6 on a 6). No "gear die" exists.

**Ruling:** The term "gear die" is an undefined phantom. No player reading `01_Dice.md` and `33_Equipment.md` together would know what die to roll, how many to roll, or when. This is a broken rule, not merely an undercooked one.

**Action Required:** Every reference to "gear die/dice" must be excised from all documents and replaced with a defined mechanic (either the Usage Die from the brainstorm, or the d6 Scrap Cascade roll from the Mechanics Audit).

---

### CONFLICT 3 — "Reaction" vs. "Interrupt" — Terminology Mismatch

**Source A (`02 Combat.md`, line 21):**
> *"The Dodge or Parry action can only be used as a **Reaction** to an incoming Attack..."*

**Source A (`02 Combat.md`, line 44):**
> Refers to *"a Grunt test"* for Cross-Gang Super Mobs.

**Source B (`06_Keywords Index.md`, line 25):**
> *"**Interrupt / Reaction:** [TODO: Resolve Conflict] An action taken out of turn. The system needs to standardize to one term."*

**Source C (`33_Equipment.md`, line 28):**
> Weapon Trait "Slow": *"Allows the enemy to use a **Reaction** to counterattack..."*
> Weapon Trait "Long": *"Allows the wielder to use a **Reaction** to attack..."*

**Ruling:** The game uses "Reaction" throughout `02 Combat.md` and `33_Equipment.md`. The Keywords Index explicitly flags that this is an unresolved conflict with "Interrupt." Since "Reaction" is the dominant term (appears in multiple files), **"Interrupt" should be retired and "Reaction" standardized.** This must be resolved before crafting adds any more uses of these terms — the crafting system's "Overclock" mechanic and "Scrap Cascade" (triggered on gear break) will need to reference this term.

**Action Required:** Remove "Interrupt" from the Keywords Index. Standardize on "Reaction" system-wide. Flag in `06_Keywords Index.md`.

---

## 🟠 MECHANICAL GAPS (Undefined rules the crafting system depends on)

These are places where the crafting system references a mechanic that doesn't exist yet anywhere in Stage.

### GAP 1 — The Crafting Roll: Pool Undefined

**Problem:** The brainstorm (`crafting-brainstorm.md`, Svar 5, Svar 1) repeatedly says the crafter "rolls their dice pool" during crafting. But `01_Dice.md` states: *"The dice pool is usually equal to their main stat + 1."*

Which stat governs crafting? The Mechanics Audit assumes **Brains**, and this is the logical choice — but it is **not stated anywhere in the Stage rules**. `10_Stats.md` lists Brains as: *"Used for noticing stuff, tinkering, traps, and magic."* The word "crafting" does not appear in the Brains description.

**Action Required:** Add "crafting" explicitly to the Brains stat description in `10_Stats.md`. Define the crafting roll as: **Brains + 1** (plus any Infrastructure/Workshop bonus).

---

### GAP 2 — Utility Slots vs. Crafting Capacity: Two Uses of the Same Number

**Problem (`10_Stats.md`, line 35–40):**
> *"Brains determines your **Utility Slots** (for carrying Magic Words or Contraptions without consuming standard Bulk)."*

**Problem (crafting system):**
The crafting brainstorm defines that the number of Oddity **slots** on a Chassis is gated by **Brains**. The Mechanics Audit (Part 4, Issue 2) correctly identifies this collision, and recommends splitting into two distinct pools — **Utility Slots** (inventory) and **Crafting Capacity** (max Oddities per item) — both numerically equal to Brains but independent.

**Ruling:** This is a legitimate conflict between two undercooked rules. Both the Magic system (`10_Stats.md` explicitly calls out `TODO: These mechanics will be expanded in the upcoming Magic and Crafting rules`) and the Crafting system are trying to use the same mechanical hook. The `TODO` note confirms this is **known and unresolved**. The dual-pool solution from the Mechanics Audit is clean and consistent.

**Action Required:** When `10_Stats.md` is updated, the Brains section must explicitly define both pools. The rule must be: *"Brains = Utility Slots (for Magic Words and Contraptions). Brains also = your maximum Crafting Capacity (max number of Oddities that can be attached to a single item). These are two separate budgets."*

---

### GAP 3 — Fumble in a Crafting Roll: No Rule Exists

**Problem:** The core dice rules (`01_Dice.md`, line 27) state:
> *"If your final result has zero successes, and the physical dice show at least two 1s, you have fumbled! For a PC this could mean loosing Grunt as you humiliate yourself in front of your goblins."*

The crafting brainstorm (Svar 1, line 78) proposes that rolling 1s in the crafting pool triggers "weird effects from a random table." These two outcomes are **incompatible**: standard Fumble costs Grunt; crafting Fumble should cause a "weird effect." There is no explicit rule saying crafting uses a modified Fumble procedure.

Furthermore: Grunt loss requires *"one or more mobs in the same zone or adjacent zone."* The crafter is in their **Lair** during Downtime, likely surrounded by their Mob. So a Fumble during crafting would technically cause Grunt loss AND potentially a chaos table result, with no rule saying which takes priority.

**Action Required:** The Stage draft for crafting **must** explicitly state whether the standard Fumble rule applies during the crafting roll, or whether crafting uses a separate resolution (e.g., Chaos Table for 1s, no Grunt penalty during Downtime). **Recommendation:** State that Fumble rules do **not** apply during Downtime crafting rolls. Instead, each 1 rolled contributes to a "Chaos Result" (a short table of flavor effects, not mechanical penalties). This aligns with Tenet #1 (fun at table) and Tenet #4 (feel like playing goblins).

---

### GAP 4 — Exploding 6s in the Crafting Roll: Ambiguity

**Problem:** The core dice rules (`01_Dice.md`, line 23–24) state:
> *"Every time you roll a 6, it is not only a success but allows you to roll an additional dice."*

The crafting brainstorm states that 6s are spent to **Tame Defects** (reduce D level). If a 6 explodes and generates another die that is also a 6, do *both* 6s count as Taming? Does the second 6 also explode?

If yes: this dramatically improves high-Brains crafter odds and needs to be reflected in probability tables.
If no: you must explicitly say *"In a crafting roll, 6s do not explode"* — which creates an exception to a core rule, violating Tenet #2 (no interpretation after rolling).

**Action Required:** The Stage draft must explicitly state the behavior. **Recommendation:** 6s in crafting **do** explode (keeping rules consistent with `01_Dice.md`) and the explosion die **does** generate an additional Taming success. This avoids a rules exception and rewards high-Brains crafters more meaningfully.

---

### GAP 5 — "Gear Breaks" Trigger: When Does It Happen in Custom Gear?

**Problem:** The old `33_Equipment.md` table triggered breakage on "rolling a 1 on the gear die." The brainstorm proposes the Usage Die (degrades when a 1 is rolled in the dice pool). But the core dice rules (`01_Dice.md`, line 26) explicitly state:
> *"Note that rolling a 1 **never cancels out a success**. You simply count your successes and you count your 1s."*

If a 1 in the dice pool triggers gear degradation AND the rule says 1s don't cancel successes, those two rules are consistent with each other. However, the question becomes: does gear degrade on **any** roll (including Manipulate, Brains tests, etc.) or **only on attack rolls**? This is undefined.

**Action Required:** The Stage draft must specify: Custom Gear only degrades on the **Attack roll** (the moment of use under stress). Non-combat use does not trigger degradation. This prevents absurd outcomes like a weapon degrading when you use Brains to pick a lock.

---

### GAP 6 — Scrap Cascade and the "Breaks" Event: No Definition in Stage

**Problem:** The Mechanics Audit proposes a Scrap Cascade rule (roll 1d6 per attached Oddity when the item breaks). However, "the item breaks" has no currently defined trigger in Stage. The old `33_Equipment.md` table used "the gear die" (which doesn't exist). Without a defined break event, the Scrap Cascade has no activation condition.

**Action Required:** Define what "gear breaking" means mechanically for Custom Gear. **Proposed rule:** *"Custom Gear is destroyed when its Quality Die (if using a Usage Die) reaches its minimum face, OR when a weapon Attack roll produces a Fumble."*. The Scrap Cascade then triggers immediately.

---

### GAP 7 — The Overclocking Action: Not Defined as an Action Type

**Problem:** The Mechanics Audit proposes "Overclock" as a pre-roll declaration. `02 Combat.md` defines three action types: Standard Action, Free Order, and Reaction. Overclock does not fit cleanly into any of these. It is a **modifier declared before the Attack roll**, not an action itself.

**Action Required:** Define Overclock as a **declaration made before spending the Attack action**, not as a separate action. Syntactically: *"Before declaring an Attack Action, you may declare an Overclock..."* This preserves action economy and doesn't add a fourth action type.

---

### GAP 8 — Downtime Phase: Not Defined Anywhere in Stage

**Problem:** The crafting brainstorm (Prompt 3, line 162) and Creative Genius Analysis both reference the "Lair Phase" and "Downtime" as the context for crafting. **No Downtime or Lair Phase rules exist in Stage.** The `01_STAGE_Drafts/05_Base/` folder is empty.

**Action Required:** Before the Crafting Stage draft can be fully self-contained, a minimal Downtime/Lair Phase skeleton must exist in `05_Base/`. Crafting rules should reference it. At minimum, the Downtime section needs to define: what activities are available, whether time is a resource, and whether Downtime actions are limited.

---

## 🟡 TERMINOLOGY ISSUES (Rules are inconsistent in language)

These don't break mechanics but will cause confusion at the table.

### TERM 1 — "Dice Pool" vs. unnamed concept

The core rules (`01_Dice.md`) never names the rolling mechanic beyond "dice pool." The brainstorm (Prompt 2, line 92) notes: *"Och kalla det inte 'pölar' för dice pools, det låter dumt."* This Swedish session note reveals the design intent is to avoid the term "dice pool" in final rules text. However, `01_Dice.md` uses it (line 22). This should be standardized to a consistent term — the rules currently just say "your dice pool" which is fine in English, but the heading section `01_Dice.md` should use the same term consistently throughout.

**Not a blocker.** Flag for text layout review.

---

### TERM 2 — "Weapon Traits" vs. "Item Traits" vs. "Tags"

`33_Equipment.md` uses "Weapon Traits" (line 19) and "Armor Traits" (line 32) for properties.
`06_Keywords Index.md` uses "Item Traits" (line 32) as a `[TODO]` placeholder.
The crafting brainstorm uses "Tags" throughout as the name for Oddity properties.

These are three names for the same concept. A unified term must be chosen:
- **Tags** — short, goblin-appropriate, aligns with brainstorm
- **Traits** — more traditional TTRPG terminology, already in `33_Equipment.md`

**Action Required:** Choose one term system-wide. **Recommendation: "Tags."** It's shorter, more goblin-flavored, and used consistently in the crafting brainstorm. Update `33_Equipment.md` weapon/armor sections to say "Tags" not "Traits." Update `06_Keywords Index.md` to define "Tags" rather than "Item Traits."

---

### TERM 3 — "Grit" vs. "Wounds" vs. "HP"

`10_Stats.md` defines **Grit** as health (line 44). `07_Wounds_Conditions.md` uses "wounds" (line 1, 2, heading). The Conditions table in `07_Wounds_Conditions.md` uses "Wound" in the title but the condition "Weakened" says *"-1d on Tough"* — it doesn't reduce Grit. 

The crafting brainstorm (`crafting-brainstorm.md` Svar 5, line 248) describes a D2 Defect as *"Vapnet bränner dig (kostar lite HP)"* — using "HP," not "Grit." The Mechanics Audit translates this as "costs HP (Grit)."

**Action Required:** Standardize on **Grit** exclusively. Every reference to "wounds," "HP," or "health" in all documents must become "Grit." The `07_Wounds_Conditions.md` title should be "Grit & Conditions."

---

### TERM 4 — "Mob Size" Referenced Without Consistent Definition

`10_Stats.md` (line 47) states: *"Grunt 3 means you can command a maximum Size 3 Mob."* 
`02 Combat.md` (line 8) says *"Each Mob has two (2) actions."* 
`13_Goblin_mob.md` presumably defines Mob Size in detail (not audited here), but the Keywords Index (line 16–17) says *"Size: [TODO: Define for PCs]"* — confirming it is still incomplete.

**Action Required:** Before crafting's "Mob-Scale Crafting" (even as a Brains Trick) is drafted, Mob Size must be formally defined. The Brains Trick proposal gates on Mob size/mechanics that are currently undefined.

---

## 🟢 CLEAN / APPROVED (No conflicts found)

These crafting proposals have **no conflicts** with existing Stage rules:

| Proposal | Status | Notes |
|---|---|---|
| Three-Layer Resource Model | ✅ Clean | No conflict. Slots naturally into existing Loot framework. |
| "Build Always Succeeds" Principle | ✅ Clean | No conflict. Aligns with all Tenets. |
| T/D Notation | ✅ Clean | Elegant. No conflicts. Needs the Defect scale defined. |
| Reverse Engineering | ✅ Clean | Maps to Manipulate action in `02 Combat.md`. |
| Blueprints as Social Currency | ✅ Clean | Slots into Loot system as a special item type. |
| Scrap Cascade Formula (d6 survival roll) | ✅ Clean | Once "gear break" trigger is defined (see GAP 6). |
| Cursed Relics / Bonded Tag | ✅ Clean | Lightweight. Just a Tag. |
| Bone Oddities | ✅ Clean | Direct extension of Named Item / Patron Saint keywords. |
| Modifier-Type Oddities (Katalysatorer) | ✅ Clean | Good design space. No conflicts. |

---

## Summary: Action Items Prioritized

| Priority | Issue | Blocking Stage? |
|---|---|---|
| 🔴 1 | Define and delete the phantom "gear die/dice" term everywhere | Yes |
| 🔴 2 | Delete old Quality table from `33_Equipment.md` | Yes |
| 🔴 3 | Standardize "Reaction" (retire "Interrupt") in Keywords Index | Yes |
| 🟠 4 | Define the crafting roll explicitly (Brains + 1, Workshop bonus) | Yes |
| 🟠 5 | Split Brains into Utility Slots + Crafting Capacity in `10_Stats.md` | Yes |
| 🟠 6 | Decide: Fumble rule in crafting? Or Chaos Table? | Yes |
| 🟠 7 | Decide: Do 6s explode in crafting, and do explosion dice Tame? | Yes |
| 🟠 8 | Define "gear break" trigger for Custom Gear | Yes |
| 🟠 9 | Define "Overclock" as a pre-Attack declaration, not a separate Action | Yes |
| 🟡 10 | Create Downtime/Lair Phase skeleton in `05_Base/` | Partial |
| 🟡 11 | Standardize "Tags" system-wide (retire "Traits" and "Item Traits") | No |
| 🟡 12 | Standardize "Grit" system-wide (retire "HP," "wounds," "health") | No |
| 🟡 13 | Define Mob Size formally before Mob-Scale Crafting can be drafted | Partial |
