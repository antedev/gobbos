# ⚙️ Game Engineer Audit: Crafting System Analysis

> Reviewing: [crafting_creative_analysis.md](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/crafting_creative_analysis.md)  
> Cross-referenced against: Stage rules ([01_Dice.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/01_Dice.md), [02 Combat.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/02%20Combat.md), [10_Stats.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters%20%26%20Mobs/10_Stats.md), [33_Equipment.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/33_Equipment.md), [07_Wounds_Conditions.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/07_Wounds_Conditions.md)), the [rules audit](file:///c:/Users/ante/Documents/github/gobbos/05_System_Tools/rules_audit_crafting.md), and the [archived crafting rules](file:///c:/Users/ante/Documents/github/gobbos/03_Archive_Graveyard/34_Crafting.md).

---

## Verdict: The Creative Analysis Is Strong — But Several Ideas Need Mechanical Stress-Testing

The Creative Genius identified the right keeper ideas and proposed exciting new directions. This audit examines each proposal against the **existing Stage rules** to find conflicts, exploits, missing mechanical definitions, and integration points. I'll also weigh in on the Tier question with hard probability context.

---

## Part 1: Auditing the "Golden" Keeper Ideas

### ✅ 1. Three-Layer Resource Model — APPROVED
No mechanical conflicts. The separation of Base Resources / Oddities / Infrastructure maps cleanly onto existing systems:
- Base Resources → pairs with the Quality table in `33_Equipment.md`
- Oddities → pairs with the "Item Traits" keyword (currently `[TODO]` in `06_Keywords Index.md`)
- Infrastructure → pairs with Lair Upgrades (currently empty in `01_STAGE_Drafts/05_Base/`)

### ✅ 2. "Build Always Succeeds" — APPROVED, with a note
Mechanically sound. Aligns with Tenet #2 (no math after dice roll) because the crafting roll *modifies the output* rather than determining pass/fail.

> [!NOTE]
> This creates a subtle design commitment: **there is no "crafting failure state."** Every combination of Oddity + Chassis must produce *something*. The GM scaffolding framework (from [crafting_framework_brainstorm.md](file:///c:/Users/ante/Documents/github/gobbos/00_DEV_Brainstorms/crafting_framework_brainstorm.md)) — "Determine Skeleton → Apply Tags → Define Exploit/Rebound" — becomes mandatory, not optional. This should be promoted to a first-class rule.

### ✅ 3. T/D Notation — APPROVED, mechanically elegant
Two numbers. No formulas. Immediately interpretable. This is the kind of design that *scales* — a GM can stat an Oddity in 5 seconds.

**One mechanical gap:** The notation describes the Oddity, but does not describe the **positive effect magnitude**. A `(T3 / D0)` Suncrystal and a `(T3 / D3)` Demon Heart both cap at Tier 3 effects — but should the Demon Heart be *stronger* because you're paying more risk? Two options:

| Approach | Rule | Consequence |
|---|---|---|
| **A) T = power cap, D is independent** | Both T3 items give T3 effects. The Demon Heart just also hurts you. | Clean, simple. But players will always prefer T3/D0 items, making high-D items strictly worse. |
| **B) Effective power = T + D bonus** | High Defect items can *exceed* their Tier in power. A T3/D3 item could produce a T4 or T5 effect. | Risky items become tempting. Creates the "deal with the devil" tension. But requires defining what T4+ effects even look like. |

> [!IMPORTANT]
> **Recommendation:** Go with **A** for simplicity, but add a single rule: *"When crafting with a D3 Oddity, you may choose to leave 1 point of Defect un-tamed to gain +1 Tier to the positive effect."* This lets players voluntarily accept danger for power, which is peak goblin decision-making, without complicating the base system.

### ⚠️ 4. Spending 6s to "Tame" the Defect — APPROVED WITH CONCERNS

The idea is mechanically beautiful in *concept*, but collides with the existing dice system in ways that need resolving.

**Problem 1: What dice pool does the crafting roll use?**
The current dice rules (`01_Dice.md`) say: *"The dice pool is usually equal to their main stat + 1."* For crafting, that stat would be **Brains**. At Brains 1 (starting), you roll **2d6**. The probability of rolling at least one 6 on 2d6 is only **30.6%**. This means:

| Brains | Pool | P(at least one 6) | P(two 6s) |
|---|---|---|---|
| 1 | 2d6 | 30.6% | 2.8% |
| 2 | 3d6 | 42.1% | 7.0% |
| 3 | 4d6 | 51.8% | 13.2% |
| 4 | 5d6 | 59.8% | 19.6% |
| 5 | 6d6 | 66.5% | 26.3% |

A Brains 1 goblin trying to tame a D2 Oddity (needing two 6s) has a **2.8% chance** of fully taming it. Even a Brains 5 genius only has 26.3%. This means **high-Defect items are effectively unusable without extreme luck or multiple crafting attempts.**

**Problem 2: Do exploding 6s count?**
The core dice rules say 6s explode. If a crafting 6 explodes, does the *explosion die* also count as a taming 6? If yes, the probabilities shift significantly upward. If no, you need to explicitly state this is an exception to the core exploding mechanic — which violates Tenet #2 (no post-roll interpretation).

**Problem 3: What about 1s in the crafting roll?**
The brainstorm (Svar 1) suggested 1s in the crafting pool trigger "weird effects" from a random table. But the core rules say two or more 1s with zero successes = **Fumble**, and Fumbles cost Grunt. Does crafting follow standard Fumble rules? If so, a Brains 1 goblin crafting in their base can *lose Grunt* from a bad crafting roll, which feels punitive for a downtime activity. 

> [!WARNING]
> **Required decisions before this can move to Stage:**
> 1. Define the crafting dice pool explicitly (Brains + 1? Brains + Workshop bonus? Flat pool from Infrastructure tier?)
> 2. Clarify if exploding 6s generate taming successes
> 3. Decide if Fumble rules apply to crafting, or if crafting uses a simplified success/chaos interpretation
> 4. Consider allowing **multiple crafting attempts** on the same item during downtime (spending more time = more rolls = more chances to tame defects). This solves the probability problem naturally and ties into the "time as opportunity cost" concept from the brainstorm.

### ✅ 5. Reverse Engineering — APPROVED
No mechanical conflicts. Dovetails with the existing "Manipulate" action (`02 Combat.md`) — reverse engineering during a raid could be a Brains-based Manipulate action. During downtime, it's automatic (build always succeeds philosophy).

---

## Part 2: Auditing the New Proposals

### 🆕 1. Blueprints as Social Currency — MECHANICALLY SOUND ✅
No conflicts with existing rules. Blueprints naturally slot into the Loot system as a special loot type with `Usage: Blueprint` attribute. They have value (tradeable), bulk (presumably 0 or 1), and a clear usage.

**One addition:** Blueprints should have a **Brains requirement** to use. You can *own* a Blueprint for a T4 weapon, but if your Brains is only 2, you can't execute it. This prevents low-Brains combat monsters from also being master crafters, which preserves stat specialization.

### 🆕 2. Scrap Cascade + Scarred Oddities — NEEDS MECHANICAL DEFINITION ⚠️

The idea is great, but "a chance to survive" is not a rule. We need to define:

**Proposal:** When Custom Gear breaks, roll 1d6 per attached Oddity:
- **1–(current Defect):** The Oddity is **destroyed**.
- **(Defect+1)–6:** The Oddity **survives** but gains +1 Defect (becomes Scarred).

This means a D0 Oddity (pure, stable) *always* survives its first break (it can't roll below 1, and 1–6 all pass since the Defect is 0). But it becomes D1. A D3 Oddity has a 50/50 shot of dying. A D5 Oddity (after multiple scars) has only a 16.7% chance of survival. The escalating Defect naturally kills off old Oddities — no bookkeeping needed beyond updating the D number.

| Defect | Survival Chance | After Survival, New Defect |
|---|---|---|
| D0 | 100% | D1 |
| D1 | 83.3% | D2 |
| D2 | 66.7% | D3 |
| D3 | 50.0% | D4 |
| D4 | 33.3% | D5 |
| D5 | 16.7% | D6 (destroyed on next break) |

This is clean, uses a single d6, requires zero math (just compare the roll to a number), and creates a narrative arc for each Oddity. **Strongly recommended.**

### 🆕 3. Cursed Relics / Bonded Gear — APPROVED AS EDGE CASE ✅
This doesn't need its own mechanical subsystem. It's just a **tag**: `[Bonded]`. When an Oddity has the Bonded tag, it cannot be removed without a specific condition (defined by the GM when the item is found). This is a narrative tool, not a mechanical system. Keep it lightweight.

### 🆕 4. Mob-Scale Crafting — NEEDS CAREFUL BALANCING ⚠️

This is the proposal I'm most cautious about. The existing Mob equipment system (`33_Equipment.md` + Lair Brainstorm) is already a resource sink — you pay Loot per Mob Size to equip them. Adding a *second* crafting layer on top risks:

1. **Decision paralysis during downtime.** Players already need to: heal, craft personal gear, equip mobs with standard gear, do town activities. Adding "also craft special mob ammo" is another plate to spin.
2. **Balance problem.** If Burning Arrows give +1d to a Mob's attack, and a Mob rolls `Size × d6`, then a Size 3 Mob with +1d gets 4d6. That's the same as bumping their equipment tier. Is this cheaper than just buying better weapons? It needs to cost *more* than standard equipment upgrades, or it invalidates the existing system.

**Recommendation:** Don't make this a separate crafting system. Instead, make it a **Brains Trick**: 
> *"**Mob Tinker** [Prerequisite: Brains 3] — During the Lair Phase, you may spend 1 Oddity (consumed) to grant one of your Mobs a temporary tag for the next raid. The Mob's weapons gain the Oddity's positive effect, but the tag is lost after the raid or if the Mob is destroyed."*

This gates it behind character investment, makes it consumable (preserving the scarcity loop), and doesn't require new subsystems.

### 🆕 5. Death Loop → Bone Oddities — APPROVED, NATURALLY FITS ✅

The existing rules *already* support this. `06_Keywords Index.md` defines:
- **Pile of Bones:** The resting place for glorious dead PCs.
- **Patron Saint:** A dead PC's spirit granting a situational boon.
- **Named Item:** Gear imbued with a dead PC's spirit, with minor magical properties.

Bone Oddities are just a crafting-system expression of the Named Item concept. A dead Boss's bone becomes an Oddity with tags derived from how they died. It slots directly into the T/D notation:

- **Grurr's Jawbone** (died fighting a troll): `[Grudge: Troll, Organic] (T2 / D0)` — Low tier (it's a bone, not a magic crystal), but zero defect (it's blessed by ancestral loyalty). The *purity* of a Bone Oddity is the mechanical reward for death.

> [!TIP]
> **Design implication:** Bone Oddities should always be `D0` or `D1`. They are small, personal, *reliable* power. The counterbalance is that their Tier is low (T1–T2). You're not building a superweapon from a bone — you're adding a dependable, sentimental edge. This makes them mechanically distinct from "big power, big risk" Oddities found in the wild.

### 🆕 6. Overclocking — APPROVED, BUT NEEDS RULES ⚠️

The concept is excellent and aligns with Tenet #3. But "massively amplified" and "double damage" aren't rules. Here's a concrete proposal:

> **Overclock (Action):** Declare before rolling. Your Custom Gear's Oddity effects are amplified to their maximum possible interpretation (GM adjudicates, but should be generous — Rule of Cool). After resolving the action, the gear is permanently destroyed. All attached Oddities are lost (no Scrap Cascade, no survival roll). 
>
> *Additionally:* The Overclock attack ignores the target's Passive Defence Dice entirely.

Why "ignores Passive Defence"? Because the archived `34_Crafting.md` already had this as the "Overclocked" result on the Quality Die — so it's a familiar effect being reused. And it's *devastating* without requiring us to define what "double damage" means for every possible tag combination.

**Cost consideration:** Should Overclocking cost Grunt? I'd say **no** — the gear destruction IS the cost. Adding a Grunt cost on top would make players never use it. The whole point is that it's free to activate but irreversibly expensive in consequences.

---

## Part 3: The Tier Count Question — An Engineer's Take

The Creative Analysis laid out the 3 vs 5 vs 6 argument well. Here's my mechanical perspective:

### The Hidden Variable: How Many Tiers Do You Actually Need Content For?

Every tier needs:
1. A **narrative flavor** (what *is* Tier 4 material?)
2. A **mechanical distinction** (how does Tier 4 differ from Tier 3 in play?)
3. A **progression gate** (what Lair Upgrade / quest unlocks Tier 4?)
4. **Oddities at that tier** (you need actual items for players to find)

| Tiers | Content Required | Risk |
|---|---|---|
| 3 | 3 material descriptions, 3 workshop levels, ~12 Oddities per tier = 36 total | Too shallow? |
| 5 | 5 material descriptions, 5 workshop levels, ~8 Oddities per tier = 40 total | Tiers 3/4 hard to differentiate |
| 6 | 6 material descriptions, 6 workshop levels, ~6 Oddities per tier = 36 total | Spreads Oddities thin |

### The Mechanical Test: Brains as Gate

If `Brains = Max Tier you can work`, then:

| Brains | Tier Access | Campaign Phase |
|---|---|---|
| 1 | T1 only | Starting — garbage weapons, pure goblin junk |
| 2 | T1–T2 | Early — first "real" materials, iron and wood |
| 3 | T1–T3 | Mid — monster parts, rare crystals |
| 4 | T1–T4 | Late — dwarven steel, demon organs |
| 5 | T1–T5 | Endgame — legendary, mythical components |

This maps cleanly to 5 tiers. The problem with 6 is that `06_Keywords Index.md` already states: *"A player character who reaches a stat of 6 automatically retires."* So Brains 6 = retirement. There would be **no PC who can work with Tier 6 material** — it would require an Elder to do it, which is either a cool design feature (retirement crafters!) or a frustrating dead end.

### The d6 Loot Table Argument

The "roll 1d6 for random scrap tier" feature is genuinely useful. But you don't need 6 *material* tiers to get it. You could have 5 material tiers and use the d6 table like this:

| d6 Roll | Result |
|---|---|
| 1 | Garbage (T1 Scrap) |
| 2 | Goblin Junk (T1 Oddity, random) |
| 3 | Decent Stuff (T2 Scrap) |
| 4 | Quality Material (T3 Scrap) |
| 5 | Rare Find (T3 Oddity, random) |
| 6 | Remarkable (T4+ Scrap or Oddity — roll again for specifics) |

This gives you a d6 table with 5 tiers of material. Best of both worlds.

### My Recommendation: 5 Tiers

- Maps 1:1 with Brains (zero extra rules)
- Enough granularity for a long campaign
- Room to expand to 6 if stats ever go to 6
- d6 loot tables still work with creative mapping
- Content requirements are manageable

---

## Part 4: Unresolved Conflicts with Existing Stage Rules

These are mechanical conflicts that **must** be resolved before crafting moves to Stage, regardless of which creative direction is chosen:

### 🔴 1. Quality System Collision
`33_Equipment.md` defines Quality as: *"Junk: Breaks on 1-2 on the gear dice. Goblin Made: Breaks on 1 on the gear die."* The crafting system proposes a completely different durability model (T/D notation + Quality Die or Usage Die). **These two systems cannot coexist.** When crafting rules move to Stage, the Quality section of `33_Equipment.md` must be rewritten to use the new system.

### 🔴 2. Utility Slot Definition
`10_Stats.md` says Brains gives "Utility Slots" for *"carrying Magic Words or Contraptions without consuming standard Bulk."* The crafting system proposes Brains gates the number of Oddities you can attach. These are **two different uses of the same stat.** The rules audit already flagged this — Oddities should NOT consume Utility Slots (or you lose all your magic capacity by crafting). 

**Recommendation:** Brains provides two separate budgets:
- **Utility Slots** (for Magic Words and Contraptions — inventory)
- **Crafting Capacity** (max Oddities per item — not an inventory cost, just a complexity limit)

Both are numerically equal to Brains, but they are independent pools.

### 🔴 3. The Keywords Index Has Placeholders
`06_Keywords Index.md` has `[TODO]` entries for "Item Traits" and "Status Effects." Crafting will generate both of these (Oddity tags = Item Traits, Defects = potential Status Effects). These TODOs should be resolved *as part of* the crafting system design, not separately.

### 🟡 4. Carry Capacity Interaction
If Oddities don't add Bulk (as recommended), but a Chassis still has its base Bulk, then a custom Heavy Weapon (Bulk 3) with 3 Oddities still weighs Bulk 3. This is fine. But some Oddities (like "Heavy Core" from the d66 table in `crafting_framework_brainstorm.md`) explicitly add +1 Bulk. The rules need to state: *"An Oddity's tag may modify the Base Item's Bulk. The final Bulk of Custom Gear is the Base Item's Bulk, plus or minus any Oddity Bulk modifiers."*

---

## Summary Table

| Proposal | Engineer Verdict | Key Issue |
|---|---|---|
| Three-Layer Model | ✅ Approved | — |
| Build Always Succeeds | ✅ Approved | GM scaffold framework must be a rule, not optional |
| T/D Notation | ✅ Approved | Define whether high-D items can exceed their Tier |
| 6s Tame Defects | ⚠️ Needs work | Probability too low at low Brains; define pool, exploding, fumbles |
| Reverse Engineering | ✅ Approved | — |
| Blueprints | ✅ Approved | Add Brains requirement to use |
| Scrap Cascade | ✅ Approved | Use the d6 survival roll proposal above |
| Cursed Relics | ✅ Approved | Just a [Bonded] tag, keep lightweight |
| Mob-Scale Crafting | ⚠️ Rework | Make it a Brains Trick, not a subsystem |
| Bone Oddities | ✅ Approved | Always D0–D1, always T1–T2 for balance |
| Overclocking | ✅ Approved | Define as "ignores Passive Defence + GM-amplified effect" |
| **5 Tiers** | ✅ Recommended | Maps to Brains, d6 tables still work |

---

## Recommended Next Steps

1. **Decide the Tier count** (I recommend 5)
2. **Define the crafting dice pool** (most urgent mechanical gap)
3. **Rewrite Quality in `33_Equipment.md`** to use the new system (resolve the collision)
4. **Write the Brains Tricks** that were left TBD — this is the natural moment
5. **Build a probability simulation** for the "tame defect with 6s" mechanic across all Brains levels, to validate that the curve feels right (I can set this up in `05_System_Tools/` if needed)
