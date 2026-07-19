# 16. Unified Modular Powers System

*Goblins don't follow formulas, unless it is a formula for making things go boom. A bit of glowing scrap, a twitching monster eyeball, a sudden chemical itch in the skin—mix them all together, tape it to a sword, and you have got a plan.*

The **Unified Modular Powers System** is the core framework for all custom abilities, mutations, and specialized gear in Gobbos. It unifies three separate paths of progression under a single rules architecture:
1. **Quirks & Twists:** Personal abilities customized by the Boss, detailed in [14_Quirks.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/14_Quirks.md).
2. **Shenanigans:** The core culture and compulsive traits of a [[Gang]], detailed in [12_Gangs.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/12_Gang.md).
3. **[[Oddities]] & Relics:** Strange materials and magical scrap crafted into custom equipment, detailed in [34_Crafting.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/03_Loot/34_Crafting.md).

---

## 1. The Core Architecture (The 6 Building Blocks)

To ensure mechanical consistency and ease of GM ruling, every custom power, spell, or item is composed of six distinct structural components. These blocks isolate the narrative flavor from the underlying rules variables:

### Category 1: The Modification (What it does)
The actual mechanical change or rule-breaking effect introduced to the game engine.
*   **[[Dice Pool]] Adjustments:**
    *   *Extra Dice:* Adds a number of [[Boon]] dice (**+Xd**) to the test pool.
    *   *Penalty Dice:* Deducts a number of [[Bane]] dice (**-Xd**) from the test pool.
    *   *[[Bangaranga]] Extraction Override:* Allows the wielder to draw dice from the shared [[Bangaranga Pool]] up to their [[Grunt]] stat, regardless of standard test limits.
*   **Probability Engineering:**
    *   *Reroll Permission:* Grants permission to reroll a specified subset of failed dice.
    *   *Specific Face Reroll:* Forces or allows rerolling specific die faces (e.g., rerolling all 1s).
    *   *Spiteful Reroll:* Allows a full reroll of failed dice, but you suffer 1 [[Grit]] damage if the second attempt fails.
*   **Explosion Engineering:**
    *   *Exploding 5s:* Standard tests now explode on both 5s and 6s.
    *   *Double Explosion:* Landing a 6 generates two additional dice instead of one (native to [[Bangaranga dice]]).
    *   *Explosion Removal:* Suppresses explosion mechanics entirely (6s count as successes but do not explode).
*   **Success & Difficulty Gauges:**
    *   *Target Number (TN) Adjustment:* Alters the required successes by a flat number (**+/- X**).
    *   *Difficulty Step Shift:* Shifts the success threshold up or down (Easy 4+, Normal 5+, Hard 6).
    *   *Success Face Override:* Treats a specific face value as a success regardless of difficulty (e.g., treating 4s as successes on Normal tests).
    *   *Fumble Parameter Shift:* Expands the Fumble boundary (e.g., fumbling if you roll any 1s).
*   **Stat & Derived Metric Adjustments:**
    *   *Main Stat Optimization:* Evaluates a main stat ([[Tough]], [[Slink]], [[Brains]], [[Mouth]]) as a flat value for specific triggers.
    *   *Secondary Stat Override:* Applies flat changes to [[Grit]] limits, [[Carry]], [[Movement]], [[Max Mobs]], [[Free Orders]], [[Power Words]], or [[Crafting Capacity]].
*   **Combat Payloads (Damage & Defense):**
    *   *Flat Damage/Success Increment:* Adds automatic successes to attacks (against standard foes) or automatic [[Grit]] or Mob [[Size]] damage (against PCs and Mobs).
    *   *Cleave Damage Vector:* Excess successes beyond defense spill over to damage extra units in a Mob.
    *   *Area of Effect (AoE) Duplication:* Duplicates damage to apply to every single die in a Mob's pool.
    *   *Overkill Multiplier:* Deals an extra Wound for every exact multiple of the target's [[Defence TN]].
    *   *[[Passive Defence]] Dice Grant:* Grants bonus [[passive defence]] dice (**+Xd**).
    *   *[[Passive Defence]] Bypass:* Bypasses the target's [[passive defence]] dice and armor completely.
*   **Status State Toggles:**
    *   *Condition Infliction:* Imposes a condition (Weakened, Restrained, Dumb, Silenced, Blinded, Terrified, Stunned, Prone).
    *   *Condition Negation:* Grants immunity to a specific condition.
    *   *Condition Acceleration:* Allows clearing a condition ahead of normal phase boundaries.
*   **Arcane & Magic Vectors:**
    *   *Spell Potency Targeting:* Spell targets one additional enemy in the delivery area per potency unit.
    *   *Spell Potency Escalation:* Adds **+1 Grit/Size damage** or **+1 automatic success** to a spell per potency unit.
    *   *Leakage Venting:* Reduces or cancels the severity of Side Effects from non-success dice.

### Category 2: The Target (What it affects)
The specific rules, stats, actions, or trackers that the modification acts upon. Target mechanics are grouped into five **Target Hubs**:
*   **Stats:** Tough Test, Slink Test, Brains Test, Mouth Test.
*   **Actions & Reactions:** Attack Action (Melee/Ranged), Move Action, Plunder Action, Manipulate Action, [[Order Action]], Dodge Reaction, Parry Reaction, Scatter Order, Opportunity Attack, Disengage, [[Group Attack]].
*   **Horde & Command:** Mob [[Size]], Mob [[Slink]] Normalization, Mob Cognitive Normalization, Boredom Rule, Cross-Gang Command Struggle, In-Fighting Damage.
*   **Campaign & Lair:** [[Zone Profile]] (Base TN), Movement Cost Multiplier, Size Capacity Threshold, Cover State, Hazard Resolution Test, [[Route Test]], [[Travel Event]], **Laden** or [[Over-Laden]] Penalties, Lair labor allocation, Recruitment loops, Slot clearance, Dominance contribution, Supply routes.
*   **Arcane:** Spell Activation Brains Pool, Push-Your-Luck Reroll, Chaotic Leakage (Side Effects), Spell Mishap (Farkle).
*   **Equipment:** Durability Break Roll, [[Scrap Cascade]], [[Oddity]] Ceiling.

### Category 3: The Trigger or Constraint (When it applies)
The specific conditions, circumstances, or events required for the ability to activate:
*   **Environmental Context:**
    *   *Active Hazard:* Target/occupied zone has a damaging trait (e.g. Burning, Toxic Spores).
    *   *Physical Obstacle:* Interacting with terrain impairments (e.g. Rubble, Chasm, vertical cliffs).
    *   *Spatial Bottleneck:* Volume limits (e.g. Narrow space penalizing [[Size]] 3+ mobs).
    *   *Tactical Feature:* Positive cover/terrain features (e.g. pillars, shadow zones).
    *   *Ambient Atmospheric States:* Weather/lighting conditions (e.g. total darkness, heavy rain).
*   **Tactical & Positioning:**
    *   *Spatial Vector Check:* Geometry (e.g. attacking from behind or above).
    *   *Numerical Disadvantage:* Outnumbered by hostiles in the zone.
    *   *Macro Movement State:* Currently Fleeing or in a Tactical Retreat.
    *   *Inventory Burden State:* Carrying weight profile (e.g. completely naked, carrying zero Bulk, or wielding a two-handed weapon).
    *   *Alternative Sensory Check:* Relying on non-visual parameters (e.g. smelling instead of looking).
*   **Target & Adversary:**
    *   *Defensive Tier Match:* Target armor type (e.g. Unarmored, Heavily Armored).
    *   *Volumetric Scale Check:* Target [[Size]] is strictly larger or strictly smaller.
    *   *Ancestry / Faction Specificity:* Target belongs to a specific biological/structural group.
*   **Trigger Events (Post-Roll):**
    *   *Deterministic Success Outcome:* Triggers immediately following a successful test resolution (e.g., successfully dodging an attack).
    *   *Probability Failure State (Fumble):* Triggers if a roll has zero successes and two or more 1s.
    *   *Probability Failure State (Expanded Fumble):* Triggers if a roll contains any 1s.
    *   *Probability Success State (Critical):* Triggers if a roll generates consecutive exploding 6s.
    *   *[[Dice Pool]] Verification:* Evaluates the exact count of 1s in a roll.
*   **Operational & Health States:**
    *   *Direct Damage Gate (Wounding):* Triggers when a sheet registers [[Grit]] or Mob [[Size]] loss.
    *   *Biological Deprivation State:* Deprived of resource inputs (e.g., gross food).
    *   *Uncontrolled Minion Status:* Mob scales past [[Grunt]], breaks line of sight, or fails morale.
    *   *Encumbrance Travel State:* Mob is **Laden** or [[Over-Laden]].
*   **Identity & Structural:**
    *   *Gang Faction Alignment:* Character sheet matches parent faction tag.
    *   *Faction Defiance (Cursed):* Item gang tag doesn't match wielder's rival gang.
    *   *Attribute Tier Gating:* Primary stat score is at or above a designated value.
    *   *Component Mismatch (Ceiling Rule):* [[Oddity]] tier exceeds workshop level.
    *   *Arcane Difficulty Constraint:* Successes are locked strictly to face value 6 (Hard casting).

### Category 4: The Delivery (Who and where it targets)
The range (how far the effect travels) and area of effect (who is caught in the footprint):
*   **Range (Origin to Target):**
    *   *Personal:* Affects only the wielder's space/sheet.
    *   *Touch:* Direct contact in the same zone.
    *   *Melee (Same Zone):* Target is in the same zone.
    *   *Ranged (Adjacent Zone):* Target is exactly 1 zone away.
    *   *Ranged (X Zones):* Target is up to X zones away (governed by stat/weapon).
*   **Area of Effect (AoE Scope):**
    *   *Single Target:* Exactly one distinct entity/pool.
    *   *Zone-Wide:* All units, terrain, and structures in the target zone.
    *   *Blast:* Targets the zone + all adjacent connected zones.
    *   *Encounter Scale:* Alters rules across the entire active battleground node map.
*   **Target Filtering:**
    *   *Personal Only:* Limits effect strictly to the wielder.
    *   *Own Mob Only:* Applies only to the wielder's commanded Mob.
    *   *Any Friendly Mob:* Applies to any allied Mob in the area.
    *   *Friends Only:* Bypasses hostiles in the area.
    *   *Enemies Only:* Bypasses allies in the area.
    *   *Any Whole Mob:* Applies collectively to all health dice in a Mob.
    *   *Multiple Mobs:* Applies across several distinct Mob squads.

### Category 5: The Cost (What it takes to use)
The action, resource ([[Grunt]], [[Grit]], or [[Size]]), or item spent to activate the power:
*   **Action Economy:**
    *   *Passive:* Triggers automatically or constantly active (0 Cost).
    *   *[[Free Action]]:* Instant during active turn for minor triggers.
    *   *[[Standard Action]]:* Consumes 1 of 3 standard combat actions.
    *   *Reaction (Saved Action):* Consumes a saved [[Standard Action]] out of turn.
    *   *Free [[Order Action]]:* Consumes 1 Free Order Mouth allocation.
*   **Personal Resource Pools:**
    *   *Current Grunt Spend:* Deducts 1 to 3 points from current [[Grunt]] pool.
    *   *Grit Loss:* Inflicts flat [[Grit]] damage directly, bypassing defense rolls.
*   **Minion / Mob Resources:**
    *   *Mob Size Sacrifice:* Permanently reduces a Mob's [[Size]] (e.g., by 1 or 1d3).
    *   *Mob Action Consumption:* Mob must spend 1 or both of its actions.
    *   *Garrison Cost:* Leaving a Mob behind, removing them from the Gobbo Pool.
*   **Inventory & Wealth:**
    *   *Scrap / Component Consumption:* Consumes a piece of Scrap or item held in inventory.
    *   *[[Oddity]] Sacrifice:* Permanently erases a component from Lair inventory.
    *   *Bribe / [[Loot Value]] Expenditure:* Deducts raw wealth (e.g. 5 Loot) from hoard.
*   **Equipment Lifecycle:**
    *   *[[Overclock]] Disintegration:* Instantly vaporizes the item chassis.
    *   *Active Bite Level Escalation:* Increases item's instability by +1 Bite.
*   **Downtime Subsystems:**
    *   *Laborer Die Allocation:* Assigns a Lair laborer die to a chore.
    *   *Laborer Die Consumption:* Consumes a laborer die permanently/temporarily.
    *   *Lair Turn Infirmary Lock:* Places a laborer die in the medical tent.
*   **Tactical Trade-Offs:**
    *   *Loot / Bulk Jettison:* Immediately dropping Bulk/treasure to validate action.
    *   *Mandatory Friendly Targeting:* Targeting a friendly Mob to trigger a loop (e.g., Asserting Dominance).
    *   *Action Restriction (Disengage):* Requires spending a [[standard action]] to safely exit zone.
*   **Risk & Pool Penalties:**
    *   *Push-Your-Luck Reroll Lock:* Locks successes, forces reroll of non-successes.
    *   *[[Bangaranga Pool]] Drainage Tax:* Drainage of [[Bangaranga dice]] on fail.
    *   *Forced Hazard Roll Trigger:* Triggers unrolled GM check on a complication table.

### Category 6: The Duration (How long it lasts)
The timeline showing when the modified effect ends:
*   **Tactical Scale (Combat & Round-Based):**
    *   *Instant:* Resolves immediately with no lingering state.
    *   *Active Round-Sustained:* Persists until End of Turn, Start of Round, or Round Closure.
    *   *Sustained (Manual Clear):* Lasts until an action/test clears it.
    *   *Round-Bounded:* Persists for X rounds.
    *   *Encounter-Bounded:* Lasts until Combat End.
*   **Frequency Gates (Charging Systems):**
    *   *Round-Frequency Limit:* Limits activation to X times per round.
    *   *Encounter-Frequency Limit:* Limits activation to X times per fight.
    *   *Raid-Frequency Limit:* X charges per exploration map, resetting at Lair.
    *   *Campaign Usage Limit:* Absolute total uses before breaking.
*   **Strategic Scale (Macro & Campaign):**
    *   *Journey Stage-Bounded:* Active during wilderness travel, clearing at destination.
    *   *Raid-Bounded:* Persists for entire raid, breaks during Homecoming.
    *   *Lair Turn-Bounded:* Active strictly during Lair weekly downtime phase.
    *   *Permanent (Character Lifecycle):* Hard-coded to PC until death/retirement.
    *   *Permanent (Gang / Lair Scale):* Irreversibly alters Lair or Gang sheets.

---

## 2. Core Target Hubs

To prevent rules bloat and keep scripting simple, all target mechanics are grouped into five **Target Hubs**:

1.  **Stats:** Modifies tests using [[Tough]], [[Slink]], [[Brains]], or [[Mouth]].
2.  **Actions & Reactions:** Modifies Attack Actions, Dodge Reactions, Parry Reactions, or [[Passive Defence]].
3.  **Horde & Command:** Modifies Mob [[Size]], [[Max Mobs]], [[Free Orders]], or Mob [[Morale]].
4.  **Campaign & Lair:** Modifies Lair labor rolls, travel route tests, or [[Carry]] capacity.
5.  **Arcane:** Modifies magic words casting, push rerolls, or spell mishap resolution.

---

## 3. The T1–T5 Mechanical Toolkit (Pre-Bundled Blocks)

To simplify play, the rules pre-bundle the positive building blocks (**Modification**, [[Delivery]], and [[Duration]]) into five standard **Tiers (T1–T5)**. This universal scale aligns with Boss stats, gear quality, and Lair workshop tiers:

| Tier | Successes / Grit Loss | Range & Area | Duration & Conditions | Narrative & Utility |
|---|---|---|---|---|
| **T1 (Niche/Minor)** | **+1 Success** (on attack) OR **1** [[Grit]]/[[Size]] damage (on hit). | [[Melee]] (Same [[Zone]]). | **Instant** (Effect resolves immediately). | Move 1 [[Zone]] as part of the action, or bypass a minor physical obstacle (e.g., climb a fence). |
| **T2 (Standard)** | **+2 Successes** (on attack) OR **2** [[Grit]]/[[Size]] damage (on hit). | **Ranged: 1 Zone** (Adjacent). | **Sustained** (Basic condition like *Weakened* or *Restrained* until target spends 1 [[Action]] to shake it off). | Medium utility (e.g., stick to walls, breathe underwater, make loud noise that ruins stealth). |
| **T3 (Heroic/Area)** | **+3 Successes** (on attack) OR **3** [[Grit]]/[[Size]] damage (on hit); OR heal **2** [[Grit]]. | [[Zone]] (Affects all targets in a single [[Zone]]). | [[Persistent]] (Severe condition like *Blinded* or *Terrified* until target spends 1 [[Action]] to shake it off). | Zone-wide utility (e.g., ignite a zone, fill it with thick smoke, block exits). |
| **T4 (Destructive)** | **+4 Successes** (on attack) OR **4** [[Grit]]/[[Size]] damage (on hit); OR double **successes**. | **Blast** (Affects own + all adjacent [[Zones]]). | [[Encounter]] (Condition lasts for the duration of the fight). | Destroys permanent structures, creates new paths, or permanently alters zone boundaries. |
| **T5 (Legendary)** | Target is instantly defeated; OR double Wounds. | **Encounter Scale** (Affects entire map). | **Permanent** (Can only be cured in the Lair). | Alter the landscape, summon mythic weather, or permanently warp magic in the region. |

>> **GOLDEN RULE: Applying Successes vs. Damage**
>> To keep combat fast and respect the deterministic nature of standard enemies, modular math adjusts based on the target:
>> * **Against standard enemies**: The value is added as **automatic successes** directly to the player's attack pool toward meeting the target's [[Defence]] [[Target Number (TN)]].
>> * **Against Bosses, PCs, and Mobs**: The value is subtracted directly as [[Grit]] loss (for Bosses and PCs) or Mob [[Size]] damage (for Mobs) on a successful hit.

---

## 4. Non-Combat & Campaign Tiering

While the combat-focused matrix is the default player-facing interface, custom Quirks and [[Oddities]] that modify non-combat loops (such as travel routes, downtime labor, or item durability) are tiered using these guidelines:

*   **Tier 1 (Niche/Minor):** Modifies a single-target, minor non-combat utility (e.g., granting a [[Boon]] to a specific travel role, or reducing an item's Bulk by 1).
*   **Tier 2 (Standard):** Modifies a standard non-combat mechanic (e.g., shifting a travel test difficulty step, or reducing an item's active Bite level by 1).
*   **Tier 3 (Heroic/Area):** Modifies a group-wide or zone-wide campaign metric (e.g., granting **+1 success** to Lair labor rolls, or allowing a Mob to ignore the **Laden** travel penalty).
*   **Tier 4 (Destructive):** Modifies macro-campaign structures (e.g., preventing any gear breakage on a [[fumbled]] attack, or allowing a Mob to ignore [[Over-Laden]] travel penalties).
*   **Tier 5 (Legendary):** Permanently alters campaign systems globally (e.g., granting a permanent Lair labor bonus, or generating permanent Lair resources).

---

## 5. Modularity & Assembly

To build a power, a player chooses one **Narrative Descriptor (Tag)** (detailed in the [Master Tag Index](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/08_Master_Tag_Index.md)) and attaches it to a **Mechanical Effect (Tier)** of the appropriate level.

### Scaling Rules: Tag Baselines vs. Power Tiers
To prevent mathematical stacking conflicts, custom powers scale as follows:
*   **Math Override:** Custom powers use the **Tier's successes, damage, or healing values** instead of the tag's baseline successes/damage.
*   **Persistent Baselines:** The tag's baseline conditions (e.g. *Restrained*), environmental behaviors, and element syntheses still apply in full.
*   *Example (T1 Fire Dagger):* A T1 power deals +1 success/damage, matching `[Fire]`'s baseline +1 success.
*   *Example (T3 Fire Sword):* A T3 power deals +3 successes/damage, overriding `[Fire]`'s +1 success baseline. The sword now deals +3 successes and ignites the zone on a hit.

### Narrative Descriptors (Tags)
Descriptors (written as `[Tag]`) represent the physical or magical manifestation of the power (e.g., `[Fire]`, `[Sticky]`, `[Chilled]`, `[Loud]`, `[Toxic]`, `[Elastic]`, `[Angelic]`, `[Undead]`). Descriptors do not contain math. Instead, they define:
* How the power behaves in the fiction (e.g., `[Elastic]` lets a goblin stretch their limbs to reach high places).
* How it interacts with the environment (e.g., `[Chilled]` freezes water; `[Fire]` ignites dry vegetation).
* How different elements combine during **Element Synthesis**.

### The Power Blueprint Template
GMs and developers write abilities using this standardized [[blueprint]] card:

```markdown
### [Power/Item Name]
*   **Targets:** [Which core rules, stats, or trackers does this modify?]
*   **Modification:** [What baseline rule is altered, bypassed, or injected?]
*   **Delivery:** [Who or what does this affect, at what range, or across what area?]
*   **Trigger/Constraint:** [Under what specific tactical triggers or conditions does this activate?]
*   **Cost:** [What resources, actions, or structural sacrifices are paid to use it?]
*   **Duration:** [How long does this altered rule-state persist before clearing?]
```

> **Example (Quirk):** Grub has a [[Slink]] of 2. They select a [[Slink]] **T2** [[Quirk]]. They combine the **T2** Mechanical Effect (*imposes a Sustained condition*) with the Descriptor `[Sticky]` to create the **Sticky Spit** [[Quirk]]. When activated, the target is covered in glue and gains the *Restrained* condition.
>
> **Example ([[Oddity]]):** A crafter builds a **T3** weapon using a fire crystal. They choose the **T3** Mechanical Effect (*Zone Area*) and the Descriptor `[Fire]`. The weapon is a **Flameslasher**. When swung, it sweeps fire across the entire [[Zone]].

### The Activation Cost Economy
To use an active modular power or [[Oddity]], a Boss must pay its associated activation cost. Because [[Grunt]] is a limited pool that determines maximum commanded Mob [[Size]], spending [[Grunt]] is a significant tactical sacrifice:
*   **T1–T2 Powers:** May be [[Passive]], cost 1 [[Action]], or cost 1 [[Grunt]].
*   **T3 Powers:** Cost 1 [[Action]] OR 1 [[Grunt]].
*   **T4 Powers:** Cost 1 [[Action]] + 1 [[Grunt]] OR 2 [[Grunt]].
*   **T5 Powers:** Cost 3 [[Grunt]] OR trigger an immediate [[Overclock]] (completely destroying the gear chassis upon resolution).

### Balancing Area of Effect (AoE) Powers
Area attacks are highly lethal in Gobbos because [[Area of Effect (AoE)]] or [[Cleave]] damage applies to **every single die** in a [[Mob]]'s pool (see [13_Goblin_mob.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/13_Goblin_mob.md)).
*   **The Multi-[[Oddity]] Rule:** An item or power cannot possess both a high-tier damage effect and a wide Area/Blast delivery without paying the modular cost.
*   To build an Area-damage weapon, a player must install both a **Core** [[Oddity]] (representing the successes/damage) and a **Modifier** [[Oddity]] (representing the Area/Blast delivery).
*   Because a goblin's [[Brains]] stat caps their [[Crafting Capacity]] (max [[Oddities]] per item), low-[[Brains]] goblins cannot build wide-area high-tier weapons. A [[Brains]] 1 goblin can only build a single-target **T3** weapon. A [[Brains]] 3+ goblin is required to combine a **T3** **Core** and a **T3** Area **Modifier**.

---

## 6. Element Synthesis

When players combine multiple descriptors (e.g., [[custom gear]] with multiple [[Oddities]] or environmental combos), the outcome is resolved using the following guidelines:

### Resolution at Creation
To prevent combat speed-bumps, **Element Synthesis must be resolved at the point of weapon creation/customization**, rather than negotiated during combat rounds. The player designs the combination during downtime, the GM approves the emergent synergy, and a static final statblock is written onto the item sheet.

### Single Condition Constraint
A single attack or weapon can never apply more than one mechanical condition.

### Synthesis Upgrade
If two elements with conditions combine, they upgrade into a single, higher-tier condition from the standard conditions list:
*   A [[Slink]] [[Bane]] + [[Tough]] [[Bane]] upgrade to [[Restrained]] ([[Slink]] 0, [[Movement]] 0) or [[Stunned]] (Cannot act).
*   A `[Toxic]` element + `[Chilled]` element combines into **Numbing Venom** (imposes [[Restrained]]).

### Narrative-Only Secondary Effects
The second tag provides narrative utility and environmental interaction, not extra combat math.
*   `[Fire]` + `[Sticky]` creates a burning glue that ignites wooden shields, but mechanically it just deals the base fire **successes** and imposes *Restrained*.

### Standard Condition Mapping
Narrative tags map directly to the condition baseline rules established in the [Master Tag Index](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/08_Master_Tag_Index.md). Refer to the Tag Index to find specific condition effects (such as [[Stunned]], [[Weakened]], [[Restrained]], [[Terrified]], or [[Blinded]]). Any tag not listed in the index defaults to a simple situational [[Bane]] on tests involving a relevant stat.
