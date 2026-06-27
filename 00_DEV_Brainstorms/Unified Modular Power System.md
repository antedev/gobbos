# Gobbos TTRPG: Unified Modular Powers System Ruleset

This document establishes the official architectural framework for the **Unified Modular Powers System**[cite: 1]. This engine governs all personal quirks[cite: 1], gang shenanigans[cite: 1], custom equipment abilities[cite: 1], and volatile power words[cite: 1]. 

By breaking abilities down into dry, distinct system components ("Lego bricks"), any player or GM can construct custom content that automatically hooks directly into the core rules without breaking game balance[cite: 1].

---

## The Compilation Syntax Template

Every ability generated within this system must be parsed and written to match this exact structural blueprint[cite: 1]:

**[Activation Cost] + [Constraint] ➔ [Modification] applied to [Target Mechanic] delivered via [Delivery Dynamics] lasting for [Lifespan]**

---

## The 6 Core Categories Explained

### Category 1: The Modification
* **The System Role:** The Mechanical Payload[cite: 1].
* **The Explanation:** The Modification is the raw mathematical payload or rule-breaking variable forced into the game engine[cite: 1]. It has no identity of its own; it doesn't know who is using it, where it is going, or what action it belongs to[cite: 1]. It is simply a packet of probability data waiting to alter a number, bypass a rule, or inflict a state change[cite: 1].
* **The Question it Answers:** *"What physical or mathematical change is happening to the baseline rule structure?"*[cite: 1]
* **Why it is Detached:** Separating the modification from the mechanic it alters allows you to use the exact same mathematical brick (such as a +1d Boon) across completely unrelated parts of the game (such as a melee swing, a wilderness navigation test, or a downtime recruitment roll) without needing to rewrite separate rules for each[cite: 1, 2].

### Category 2: The Target Mechanic
* **The System Role:** The Destination Wire[cite: 1, 2].
* **The Explanation:** The Target Mechanic is the exact destination socket within your rules layout[cite: 1, 2]. Because your game runs on several independent sub-engines (real-time combat rounds[cite: 1], travel roles[cite: 1], downtime lair labor[cite: 1], and automated background mob ticks[cite: 1]), this brick specifies exactly which native rule, roll, pool, or capacity is being hijacked by the Modification[cite: 1, 2].
* **The Question it Answers:** *"Which specific row, column, action, or tracker on the character sheet or lair sheet is receiving this payload?"*[cite: 1, 2]
* **Why it is Detached:** This acts as your system anchor[cite: 1]. Instead of writing hard-coded individual abilities for "Melee Attacking" versus "Ranged Attacking," you write a single standalone modification (like *Double Explosion*) and snap it into whichever target socket you want to augment[cite: 1, 2].

### Category 3: The Constraint / Trigger
* **The System Role:** The Conditional Gatekeeper[cite: 1].
* **The Explanation:** The Constraint or Trigger is a conditional security guard standing at the door of the ability[cite: 1]. It represents a system check that evaluates to a simple **TRUE** or **FALSE** based on the real-time context of the zones, character sheets, or dice outcomes[cite: 1]. If the context matches the checklist (TRUE), the power activates; if it does not (FALSE), the power remains completely dormant[cite: 1].
* **The Question it Answers:** *"Under what exact environmental/tactical conditions, or immediately following what numerical roll result, is this power allowed to trigger?"*[cite: 1]
* **Why it is Detached:** This is your primary narrative injector and engine balancer[cite: 1]. It forces roleplay flavor directly into the math by preventing powerful modifications from being active 100% of the time[cite: 1]. Niche, restrictive constraints (like "only while completely naked" or "only when standing in a Burning zone") naturally lower the point cost of an ability[cite: 1].

### Category 4: The Delivery Dynamics
* **The System Role:** The Spatial Mapping Filter[cite: 1].
* **The Explanation:** Delivery Dynamics control how an ability projects across your abstract battlegrounds[cite: 1]. It tracks two specific spatial vectors: **Range** (the linear distance from the origin point the effect can cross) and **Target Filtering/Area of Effect** (the volumetric footprint of the drop-zone, and who inside that footprint actually suffers the effect versus who is ignored)[cite: 1].
* **The Question it Answers:** *"Where does this effect go, how many zone boundaries can it cross, and does it filter out friends from enemies?"*[cite: 1]
* **Why it is Detached:** Your game relies heavily on gridless zone-based tactical skirmishing and massive squad management[cite: 1]. Detaching delivery dynamics prevents high-tier damage modifications from automatically becoming wide-area nuclear blasts, forcing low-IQ goblins to invest heavily in multiple components if they want to build bombs[cite: 1].

### Category 5: The Activation Cost
* **The System Role:** The Immediate Transaction Toll[cite: 1, 2].
* **The Explanation:** Activation Cost is the immediate economic transaction or resource drain a player must make to flip an ability from "off" to "on"[cite: 1, 2]. It requires a player to pay upfront using the game's various distinct currencies: time currency (actions or reactions from the round economy)[cite: 1], pool currency (spending active Grunt or taking Grit damage)[cite: 1, 2], inventory currency (consuming held scrap)[cite: 1], or structural currency (overclocking a weapon to total vaporization)[cite: 1].
* **The Question it Answers:** *"What must the character sheet immediately spend, lose, or permanently sacrifice to buy this modification?"*[cite: 1, 2]
* **Why it is Detached:** It forces intense tactical choice[cite: 1]. Because your Grunt pool directly sets your maximum commanded Mob size, spending Grunt to activate an ability means a player is deliberately choosing to lose grip over their troops to save their own skin[cite: 1, 2]. Separating costs from lifespans lets you build cheap quick-draw traits or massive, sacrificial powers cleanly[cite: 1].

### Category 6: The Lifespan / Duration
* **The System Role:** The Temporal Tracking Window[cite: 1].
* **The Explanation:** The Lifespan or Duration block dictates the exact expiration timeline and structural phase checkpoints that govern an active modification[cite: 1]. It defines how long an altered rule state forces itself onto the system trackers, scaling cleanly from single-roll flashes up to permanent, multi-generational global lair modifications[cite: 1, 2].
* **The Question it Answers:** *"How long must the players and GM manually track this altered state before it automatically clicks back to the default baseline rules?"*[cite: 1]
* **Why it is Detached:** It keeps your tabletop free of tracking clutter[cite: 1]. By treating duration as its own clean Lego brick, you cleanly regulate exactly when status conditions fall off, when temporary equipment tags fall apart, and when macro-upgrades apply permanent changes to the campaign[cite: 1].

---

## The Balancing Engine Framework

To evaluate, balance, and distribute these compiled blocks into character progression loops or downtime crafting, use this uniform point tracking ledger[cite: 1]. Total power tier calculation is deterministic[cite: 1].

### 1. Value Adders (Increase Points)
* **Modifications:** 
    * Minor (+1 point) -> Basic +1d Boon, -1d Bane, or minor single-point tracker tweaks[cite: 1].
    * Standard (+2 points) -> Shifting a Difficulty Step (Normal to Easy)[cite: 1, 2], or standard conditions (Prone, Weakened)[cite: 1].
    * Severe (+4 points) -> Altering explosions (Exploding 5s, Double Explosions)[cite: 1, 2] or critical conditions (Stunned, Terrified)[cite: 1].
    * Catastrophic (+6 points) -> Bypassing passive armor defenses entirely[cite: 1] or executing single-target instant defeats[cite: 1].
* **Delivery Dynamics:** 
    * Isolated (+0 points) -> Personal scale or single isolated target die[cite: 1].
    * Squad-Scale (+2 points) -> Targets an entire single Mob squad concurrently[cite: 1].
    * Zone-Scale (+4 points) -> Blankets an entire abstract local Zone completely[cite: 1].
    * Encounter-Scale (+6 points) -> Affects the entire active micro battleground node map[cite: 1].
* **Lifespan:** 
    * Instant (+0 points) -> Resolves and disappears immediately within the current action loop[cite: 1].
    * Phase/Turn-Bound (+1 point) -> Clears at a milestone checkpoint (e.g., End of Active Turn)[cite: 1].
    * Encounter-Bound (+3 points) -> Lasts across the combat layout until explicitly cleared or combat ends[cite: 1].
    * Permanent (+6 points) -> Forever hardcoded onto an identity or lair sheet[cite: 1, 2].

### 2. Value Discounters (Decrease Points)
* **Constraints & Triggers:**
    * No Constraint (+2 points) -> Functional unconditionally at any point during active gameplay.
    * Broad Context (-1 point) -> Common states ("while in darkness"[cite: 1], "using a Melee weapon"[cite: 1, 2]).
    * Tight Context (-2 points) -> Specific hazards/scales ("while in a Burning zone"[cite: 1], "target is Strictly Smaller"[cite: 1]).
    * Hyper-Specific Trigger (-3 points) -> Low-probability event sequencing ("rolling a Fumble during a pushed spell")[cite: 1, 2].
* **Activation Costs:**
    * Passive / Free (0 points) -> Drains zero resource tickers and zero actions[cite: 1].
    * Standard Action (-1 point) -> Consumes exactly 1 basic combat round action[cite: 1].
    * Resource Drain (-2 points) -> Deducts current Grunt[cite: 1, 2], inflicts Grit damage[cite: 1], or trims a point of Mob Size[cite: 1, 2].
    * Severe Sacrifice (-4 points) -> Demands total asset vaporization (Overclocking gear chassis destruction)[cite: 1].

---

## Universal Acquisition Matrix

Sum the points from your compiled components to determine the ability's final Universal Tier[cite: 1]. This tier mandates the precise stat gating, workshop requirements, and character advancement costs[cite: 1, 2]:

| Calculated Score | Power Level | Required Stat Gate[cite: 1, 2] | Crafted Gear Quality & Workshop Required[cite: 1] | Quirk XP Cost[cite: 1, 2] |
| :---: | :---: | :---: | :---: | :---: |
| **0 to 1** | **Tier 1 (Junk)** | Level 1+ Stat | T1 Oddity / Open Fire (Junk Quality) | 1 XP |
| **2 to 3** | **Tier 2 (Scrappy)** | Level 2+ Stat | T2 Oddity / Scrap Forge (Scrappy Quality) | 2 XP |
| **4 to 5** | **Tier 3 (Standard)** | Level 3+ Stat | T3 Oddity / Proper Smithy (Standard Quality) | 3 XP |
| **6 to 7** | **Tier 4 (Superior)** | Level 4+ Stat | T4 Oddity / Master Workshop (Superior Quality) | 4 XP |
| **8 or higher** | **Tier 5 (Legendary)** | Level 5 Stat | T5 Oddity / Legendary Forge (Legendary Quality) | 5 XP |