# Comprehensive Specification & Handoff Report: Gobbos Combat Simulator

**Author**: Explorer Agent (`explorer_scenarios_0`)  
**Mission**: Repository Survey for Combat Simulation Engine, Scenarios, Topologies, Enemies & Traits  
**Date**: 2026-08-23T21:35:00Z  
**Target Specification File**: `c:\Users\ante\Documents\github\gobbos\.agents\explorer_scenarios_0\handoff.md`

---

## 1. Observation

Direct evidence surveyed across the canonical repository files:

### 1.1 Core Enemy Framework, Scales, and Overkill Rule
* **File**: `01_STAGE_Drafts/04_Enemies/20_Enemies.md`
  * **Deterministic Threats (Lines 11–13)**: *"The GM never rolls dice. Enemies do not test for success or roll to hit. Their actions are guaranteed threats. Every attack has an incoming Threat profile and flat Damage... deals its listed damage automatically unless the player resolves a Clatter Roll by spending a saved action to Dodge (testing Slink) or Parry (testing Tough), or absorbs damage with passive Armor Dice."*
  * **Three Enemy Scales (Lines 15–19)**:
    1. Standard Enemies: One-Hit Kill on $\ge$ Defence TN.
    2. Bosses & Elites: Track damage using a Wounds track.
    3. Enemy Mobs: Shared Dice-HP pool (Size $X$ = $X$ physical d6s starting at 6).
  * **Enemy Action Economy (Lines 20–22)**: Default 2 actions per round for Standard, Mob, or Elite. Apex Bosses may have 3 actions or action clocks. Spent reactions reduce active turn action pool.
  * **Enemy Mob Health & Scaling (Lines 86–96)**:
    * Standard single-target damage decrements active die face; when $<1$, die is removed (reducing Mob Size by 1) with excess damage spilling over into next die.
    * AoE / Cleave applies flat damage to *every single die* in the Mob's pool simultaneously.
    * Mob Attack Damage scales deterministically: $\text{Mob Damage} = \text{Base Unit Damage} + (\text{Current Size} - 1)$.
    * Standard attacks without Cleave kill at most 1 unit per action on success.
  * **Boss Overkill Rule (Lines 108–110)**:
    * *"Against Elites and Bosses, you deal 1 Wound for every full multiple of the target's Defence TN scored on a single attack roll (e.g., against Defence 2, scoring 2 successes deals 1 Wound, 4 successes deals 2 Wounds, and 6 successes deals 3 Wounds)."*
    * Formula: $\text{Wounds Dealt} = \lfloor \frac{\text{Successes}}{\text{Defence TN}} \rfloor$.
  * **Mass & Stagger Resistance (Lines 111–118)**:
    * Staggered condition requires $\text{Impact Size} \ge \text{Target Physical Size}$.
    * Impact Size: Standard Attack = Attacker Size (Size 1); Mob = Current Size; Heavy Weapon = $+1$ Impact Size (Size 2); Crushing Weapon = $+2$ Impact Size (Size 3); Explosives/Spells = Tier.
  * **Morale & Swarm Terror (Lines 121–134)**:
    * Triggered at End of Round if enemy group suffers $\ge 50\%$ casualties (or Commander dies).
    * Players roll combined `Swarm Terror` pool against 5+ (successes on 5 or 6). Pool size = total Size of all surviving Mobs + surviving PCs in current and adjacent Zones.
    * Successes $\ge \text{Enemy Morale TN}$ breaks the enemy group (they must spend 2 actions per turn fleeing toward exit).

### 1.2 Universal Ancestries and Special Traits
* **File**: `01_STAGE_Drafts/04_Enemies/21_Bestiary.md`
  * **Beast (Lines 25–30)**:
    * *Instinctive Morale*: Triggers immediate Morale Check if targeted by `[Fire]`, loud explosions (`[Loud]`), or if group size is halved.
    * *Lure Vulnerability*: Prioritizes `[Tasty]` targets above all others and gains $+1d$ Boon on attacks against them.
    * *Mindless Immunity*: Immune to Mouth persuasion and complex magic.
  * **Humanoid (Lines 31–36)**:
    * *Tactical Discipline*: Uses cover, focus fires goblin bosses/commanders, obeys Orders.
    * *Standard Morale*: Normal 50% casualty checks.
    * *Gear Salvage*: Drops Scrap, weapons, and Loot.
  * **Undead (Lines 37–42)**:
    * *Cold & Mindless*: Immune to Morale Checks (fights to destruction) and immune to `Terrified`.
    * *Dead Flesh*: Immune to `Weakened` from poison (`[Toxic]`) and bleeding (`[Bleeding]`).
    * *Holy Vulnerability*: Attacks with `[Angelic]` or `[Light]` deal $+1 \text{ Success}$ against Undead.
  * **Monstrosity (Lines 43–47)**:
    * *Hulking Mass*: Cannot be knocked Prone, shoved, or Staggered unless $\text{Impact Size} \ge \text{Target Size}$.
    * *Sweeping Blows*: Melee attacks naturally Cleave (damages all Goblins and Mob dice in target Zone).
  * **Fiend (Demon) (Lines 48–53)**:
    * *Infernal Body*: Immune to `[Fire]` damage and fire hazards; immune to `Confusing` and `Terrified`.
    * *Purification Weakness*: `[Purified]` or `[Angelic]` attacks ignore armor and reduce Defence TN by 1.
    * *Chaos Opportunism*: Fumble (two or more 1s) by a Goblin within 1 Zone immediately triggers free retaliation reaction.
  * **Specific Trait Mechanics**:
    * **Parrying Buckler** (Armored Highwayman, Line 221): *"The first melee attack committed against the highwayman each round (regardless of whether it hits or misses, and whether made by a Boss or a Mob) must be rolled at Hard (6). Once that first attack resolves, the buckler is committed and all subsequent melee attacks in the same round are resolved at Normal difficulty (5+)."*
    * **Thick Blubber** (Forest Mauler, Line 140): *"Attacks against the bear suffer a Bane (-1d) due to its dense layers of fat and matted fur. Attacks carrying the [Fire] tag bypass this blubber and roll normally without a Bane."*
    * **Plate Armor Bastion** (Ironclad Knight, Line 407): *"The knight ignores the first 1 point of incoming damage from every attack unless the attack possesses the Piercing trait or an elemental Tag ([Fire], [Acidic], [Shock])."*
    * **Pressurized Steam Vent** (Solar Praetor, Line 474): *"Whenever the Praetor takes a Wound, boiling steam erupts across its Zone; all Goblins in the Zone must succeed on a Slink 5+/2 test or take 2 damage from scalding vapor ([Fire])."*
    * **Voracious Regrowth** (Swamp Troll, Line 386): *"The troll recovers 1 lost Wound at the start of each round. If the troll suffered damage with the [Fire] or [Acidic] tag during the previous round, this regeneration is disabled for that round."*
    * **Dry Bones** (Rattlebone Skeleton, Line 265): *"Attacks with the Piercing or Cutting traits (and all ranged bow attacks) suffer a Bane (-1d)... Attacks with the Bashing or Crushing traits gain a Boon (+1d)."*

### 1.3 Zones, Topologies, Cover, and Environmental Traits
* **Files**: `01_STAGE_Drafts/00_Rules/03_Movement & Zones.md` and `00_DEV_Brainstorms/GDRs/GDR-006_Environmental_Hazards_and_Zone_Statblocks.md`
  * **Graph Topology (Lines 52–77)**: Encounter area modeled as connected node graph of abstract gridless Zones. PC movement = 2 Zones per Move action (modified by Slink stat: Slink 1 = 2, Slink 2-3 = 3, Slink 4 = 4, Slink 5 = 5); Mob movement = 2 Zones/Move.
  * **Zone Profile (Lines 81–91)**: Base `Difficulty+/TN` (e.g. `5+/1`, `5+/2`, `6/1`). Used for all environmental tests, hazard checks, search tests in the zone.
  * **Cover (Lines 77–85 in 02 Combat.md & 189–192 in 03_Movement & Zones.md)**:
    * *Partial Cover*: Ranged attacks against target suffer $-1d$ Bane; target gains $+1d$ Boon to Dodge reactions.
    * *Full Cover*: Target cannot be targeted by ranged attacks from that direction/adjacent zone.
  * **Zone Traits & Hazards**:
    * **Slippery (`[Slick]`, Line 154)**: Entering/moving in zone requires Slink test vs Zone Profile; failure knocks creature Prone and ends movement immediately.
    * **Burning (`[Fire]`, `[Gaseous]`, Line 142)**: T2 Hazard. Entering or starting turn in zone requires Slink test vs Zone Profile or take 2 damage to Grit/active Mob die and gain `[Burning]`. Fire spreads to adjacent flammable zones at End of Round on 1d6 roll of 5–6.
    * **Toxic Spores / Gas (`[Toxic]`, `[Gaseous]`, Line 157)**: T2 Hazard. Starting turn in zone requires Tough test vs Zone Profile; failure inflicts Weakened condition ($-1d$ on physical tests) until spending 1 Standard Action in clean zone.
    * **Narrow (Line 127)**: Max Mob size without penalty is Size 2. Mobs Size 3+ suffer $-1d$ Bane to attack rolls and physical tests, and Movement capped at 1 Zone. Giant enemies cannot enter.
    * **Pillars / Statues (Line 130)**: Occupant can declare taking cover as Free Action to gain Full Cover from one specific adjacent Zone.
    * **Rubble (Line 133)**: Costs double movement (costs 2 Zones of movement to cross 1 Zone).
    * **Shoring (Line 199)**: Interactive Opportunity (Standard Action Manipulate Brains vs Profile or Attack Melee vs Profile). Success triggers Crumbling Ceiling (everyone in zone tests Slink vs Profile or takes 3 damage and knocked Prone) and permanently blocks exits to adjacent zones (clearing exit requires Tough test vs Profile). Zone becomes Rubble.
    * **Chasm / Pit (Line 121)**: Slink test to cross; failure takes 3 damage and gains Restrained.

### 1.4 Boss Stats, Equipment, and Quirks
* **Files**: `01_STAGE_Drafts/01_Characters & Mobs/10_Stats.md`, `14_Quirks.md`, `03_Loot/33_Equipment.md`, `00_Rules/02 Combat.md`
  * **Boss Stats**:
    * *Tough (T)*: Level 1 (Grit 3, Carry 6), Level 2 (Grit 4, Carry 8), Level 3 (Grit 4, Carry 10), Level 4 (Grit 5, Carry 12), Level 5 (Grit 5, Carry 14). Used for melee attacks and Parry reactions.
    * *Slink (S)*: Level 1 (Move 2), Level 2 (Move 3), Level 3 (Move 3, Passive Def +1d), Level 4 (Move 4, Passive Def +1d), Level 5 (Move 5, Passive Def +2d). Used for ranged attacks and Dodge reactions.
    * *Mouth (M)*: Level 1 (Max 1 Mob, 1 Free Order), Level 2 (Max 2 Mobs, 1 Free Order), Level 3 (Max 2 Mobs, 2 Free Orders), Level 4 (Max 3 Mobs, 2 Free Orders), Level 5 (Max 3 Mobs, 3 Free Orders). Used for Mob Scatter reactions and ordering.
    * *Brains (B)*: Level 1–5. Used for environmental manipulation and item activation.
    * *Grunt*: Second highest Main Stat. Max Mob Size = Grunt. Fuel for Quirks, rerolls, Bangaranga dice.
  * **Equipment**:
    * *Melee*: Light (1H, Size 0/1), Medium (1H, Size 1), Heavy (2H, $+1$ Impact Size for Stagger).
    * *Ranged*: Sling (1 Zone), Shortbow/Crossbow (2 Zones), Heavy Crossbow/Arbalest (3 Zones, Heavy).
    * *Armor & Shields*: Light (+1d Armor), Medium (+2d Armor, Bane 1 on Slink), Heavy (+3d Armor, Bane 2 on Slink), Shield (+1d Armor, enables Tough Parry reaction).
  * **Quirks**:
    * **Meat Shield**: Spend 1 Grunt/Reaction when hit to shove allied Mob in Zone to take the hit (Mob takes hit, Boss takes 0 damage).
    * **Ankle Bite**: Passive trigger on successful Dodge reaction to make immediate free melee counter-attack against attacker in Zone with $+1 \text{ Success}$.
    * **Second Wind / Push Luck**: Spend 1 Grunt after rolling to reroll all non-1 dice on any critical test.

### 1.5 Combat Loop, Clatter Roll, and Mob Scatter
* **File**: `01_STAGE_Drafts/00_Rules/02 Combat.md`
  * **Action Economy**: Boss gets 3 Standard Actions + 1 Free Order per round. Mob gets 2 actions when ordered.
  * **Clatter Roll**: Simultaneous throw of Stat Dice (Slink for Dodge / Tough for Parry) and Passive Armor Dice (+1d/+2d/+3d).
    1. If Stat Dice $\ge \text{Threat TN}$, attack is cleanly evaded (0 damage).
    2. If Stat Dice $<\text{Threat TN}$, each 5+ on Armor Dice reduces damage by 1; remainder hits Grit.
  * **Mob Scatter Reaction**: Boss spends saved action or Free Order to roll Mouth dice vs $\text{Threat TN} + (\text{Mob Size} - 1)$.
    * Success: 0 damage and moves 1 Zone into cover.
    * Fail: Takes damage, mitigated only by passive Armor Dice.
    * Mob Gamble (rerolling 1s): If fails, Mob takes full damage $+ 1 \text{ Trample Damage}$ to *all* dice in pool, drops 1 Bulk loot, becomes Out of Control, and Boss gains Staggered.
  * **Group Attack (Enemy Swarms)**: Multiple standard enemies attacking same PC combine into 1 attack: Base Damage $+ 1$ per additional enemy. PC spends only 1 reaction to evade. (Max 3 enemies attack 1 PC; no limit against Mob).
  * **Unordered Mobs**: Mobs without orders roll on Loitering Table (d6 1-6) or Out of Control Table (d6 1-6).

---

## 2. Logic Chain

From the direct textual evidence in Section 1, we establish the necessary domain modeling, scenario configurations, and algorithmic requirements:

### Step 1: Enemy Model & Combat Resolution Logic
* **Observation**: Enemies are deterministic (no GM attack rolls), have static Threat TN and flat Damage, and scale across Standard (1-hit kill), Elite/Boss (Wounds track with Overkill), and Mobs (Dice-HP).
* **Inference**: Enemy attack action simply generates an incoming `Threat(stat, tn, difficulty, damage, traits)`. The target PC resolves a `ClatterRoll(stat_pool, difficulty, armor_dice)`. If `stat_successes >= tn`, damage = 0. Else, `damage_taken = max(0, damage - armor_successes)`.
* **Inference for Boss Wounds & Overkill**: When a PC or Mob attacks an Elite/Boss enemy with Defence TN $D$:
  $$\text{Wounds} = \begin{cases} 0 & \text{if } \text{successes} < D \\ \lfloor \frac{\text{successes}}{D} \rfloor & \text{if } \text{successes} \ge D \end{cases}$$
  If $\text{successes} \ge 1$ and $\text{successes} < D$, check if $\text{Impact Size} \ge \text{Target Size}$; if true, apply `Staggered` condition (which reduces enemy Defence by 1 until end of round).
* **Inference for Mob Health**: Mob holds `List[int]` representing d6 faces (e.g. `[6, 6, 6]`).
  * Single-target attack: Decrement current active die by damage. While active die $\le 0$ and pool not empty, pop die (Size decreases by 1) and apply remainder to next die.
  * AoE / Cleave attack: Subtract damage from *every* die in `List[int]`, then filter out all dice $\le 0$. Size becomes `len(remaining_dice)`.

### Step 2: Ancestry & Trait Trigger Logic
* **Observation**:
  * Beast: Morale triggered immediately on Fire/Loud attacks or 50% loss.
  * Undead: Morale immune, Terrified immune, Toxic/Bleeding immune, Angelic/Light attacks grant $+1$ Success.
  * Monstrosity: Stagger immune unless $\text{Impact Size} \ge \text{Target Size}$; Melee attacks naturally Cleave.
  * Parrying Buckler: Track `buckler_active` boolean per round. Reset to `True` at round start. If `buckler_active` and incoming attack is Melee, difficulty is `Hard (6)` and set `buckler_active = False`. Subsequent melee attacks in round are `Normal (5+)`.
  * Thick Blubber: If incoming attack lacks `[Fire]` tag, apply $-1d$ Bane to attacker pool.
  * Voracious Regrowth: At Round Start, if enemy has lost Wounds and did not take Fire or Acidic damage in previous round, heal 1 Wound.
  * Pressurized Steam Vent: On taking $\ge 1$ Wound, all Goblins in same Zone must test `Slink 5+/2` or take 2 Fire damage.
  * Dry Bones: Attacks with `Piercing`, `Cutting`, or ranged bows suffer $-1d$ Bane; attacks with `Bashing` or `Crushing` gain $+1d$ Boon.

### Step 3: Zone Graph & Environmental Hazard Resolution Logic
* **Observation**: Topologies are connected graphs of Zones with profiles (`Difficulty+/TN`), Cover properties, and modular traits (Slippery, Burning, Toxic, Narrow, Pillars, Rubble, Shoring).
* **Inference**: Graph modeled as adjacency mapping: `Zone -> Set[Zone]`. Range distance = shortest path length (BFS).
* **Inference for Trait Triggers**:
  * `Slippery`: On `entity.move_to(zone)`, entity rolls `Slink` vs `zone.profile`. On failure, entity gains `Prone` and movement terminates in that zone.
  * `Burning`: On `entity.enter(zone)` or `entity.round_start(zone)`, entity rolls `Slink` vs `zone.profile`. On failure, takes 2 damage and gains `[Burning]`. End of round: for each burning zone, roll 1d6 for adjacent flammable zones; if $\ge 5$, ignite adjacent zone.
  * `Toxic`: On `entity.round_start(zone)`, entity rolls `Tough` vs `zone.profile`. On failure, inflicts `Weakened` condition ($-1d$ on physical tests).
  * `Narrow`: If `mob.size > 2`, mob suffers $-1d$ Bane on attacks/tests and max movement = 1.
  * `Partial Cover`: Ranged attacks targeting zone suffer $-1d$ Bane; Dodge reactions in zone gain $+1d$ Boon.
  * `Full Cover` (Pillars): Block ranged line-of-sight from designated adjacent zone.
  * `Shoring`: Standard Action Manipulate (`Brains` vs `profile`) or Melee Attack (`Tough` vs `profile`). On success: all entities in zone test `Slink` vs `profile` or take 3 damage + Prone; zone gains `Rubble` and exits to adjacent zones become blocked.

### Step 4: Three Pre-Built Reference Encounters Specification
From the user request and repository bestiary statblocks:

1. **Scenario 1: Street Skirmish**
   * **Topology**: 3 connected zones: `Street West` (Profile: `5+/1`), `Street Center` (Profile: `5+/1`, Trait: `Partial Cover` barricades), `Alley East` (Profile: `5+/1`, Trait: `Narrow`).
   * **Goblin Party**:
     * Boss "Garg": Tough 2, Slink 2, Mouth 2, Brains 1, Grunt 2, Grit 4. Equipment: Medium Melee Sword (1H), Shield (+1d Armor, Tough Parry enabled), Medium Armor (+2d Armor, -1d Slink Bane). Quirk: `Ankle Bite` (on successful Dodge, free melee counter-attack at $+1 \text{ Success}$). Starting Zone: `Street West`.
     * Mob "Runts": Size 3 (3d6 @ 6 HP), Light Gear. Starting Zone: `Street West`.
   * **Enemies**:
     * Robber Gang (Enemy Mob Size 3, Defence 1, Movement 2, Morale 5+/2, Attack: Club & Shiv Swarm `Slink 5+/1`, 3 Dmg). Starting Zone: `Street Center`.
     * Footpad A (Standard Humanoid, Size 1, Defence 1, Movement 2, Morale 5+/1, Attack: Rusty Shiv `Slink 5+/1`, 1 Dmg; Pocket Sand 1/encounter). Starting Zone: `Street Center`.
     * Footpad B (Standard Humanoid, Size 1, Defence 1, Movement 2, Morale 5+/1, Attack: Thrown Cobblestone `Slink 5+/1`, 1 Dmg Ranged 1 Zone). Starting Zone: `Alley East`.

2. **Scenario 2: The Mauler's Den**
   * **Topology**: 2 connected zones: `Den Entrance` (Profile: `5+/2`, Trait: `Narrow`), `Main Den` (Profile: `5+/2`, Traits: `Rubble`, `Pillars`).
   * **Goblin Party**:
     * Boss "Skag": Tough 3, Slink 1, Mouth 2, Brains 1, Grunt 2, Grit 4. Equipment: Two-Handed Greataxe (Heavy, +1 Impact Size = 2), Light Armor (+1d Armor). Quirk: `Meat Shield` (Spend 1 Grunt/Reaction when hit to shove allied Mob in Zone to take hit). Starting Zone: `Den Entrance`.
     * Boss "Grub": Tough 3, Slink 2, Mouth 1, Brains 1, Grunt 2, Grit 4. Equipment: Two-Handed Greatclub (Heavy, +1 Impact Size = 2), Light Armor (+1d Armor). Quirk: `Meat Shield`. Starting Zone: `Den Entrance`.
     * Mob "Skag's Boyz": Size 2 (2d6 @ 6 HP). Starting Zone: `Den Entrance`.
     * Mob "Grub's Crew": Size 3 (3d6 @ 6 HP). Starting Zone: `Den Entrance`.
   * **Enemies**:
     * Forest Mauler (Cave Bear): Elite Beast (Size 2, 3 Wounds, Defence 2, Movement 2, Morale 5+/3). Traits: `Thick Blubber` (-1d Bane to attacks against bear unless Fire), `Enraged Roar` (1st Wound triggers Brains 5+/1 fear test on all Goblins in Zone). Attacks: Crushing Claws (`Tough 5+/2`, 3 Dmg, Cleave), Bear Hug (`Slink 4+/2`, 2 Dmg, Restrained). Starting Zone: `Main Den`.

3. **Scenario 3: Tomb of the Highwayman**
   * **Topology**: 2 connected zones: `Crypt Antechamber` (Profile: `5+/1`, Trait: `Slippery`), `Burial Vault` (Profile: `5+/2`, Trait: `Shoring`).
   * **Goblin Party**:
     * Boss "Wizgog": Tough 2, Slink 3, Mouth 2, Brains 2, Grunt 2, Grit 4. Equipment: Heavy Bashing Spiked Mace (1H, Bashing trait = +1d Boon vs Dry Bones), Light Armor (+1d Armor). Quirk: `Push Luck` (Spend 1 Grunt to reroll non-1s). Starting Zone: `Crypt Antechamber`.
     * Mob "Tomb Diggers": Size 3 (3d6 @ 6 HP), Light Armor (+1d Armor). Starting Zone: `Crypt Antechamber`.
   * **Enemies**:
     * Armored Highwayman: Elite Humanoid (Size 1, 2 Wounds, Defence 2, Movement 1, Morale 5+/2). Traits: `Parrying Buckler` (1st melee attack each round is Hard 6, subsequent Normal 5+), `Heavy Cleave` (Inflicts Staggered on failed Parry). Attack: Steel Broadsword (`Tough 5+/2`, 2 Dmg). Starting Zone: `Burial Vault`.
     * Skeleton A (Rattlebone Skeleton): Standard Undead (Size 1, Defence 2, Movement 1, Morale Immune). Trait: `Dry Bones` (Piercing/Bows -1d Bane, Bashing +1d Boon). Attack: Notched Scimitar (`Tough 5+/1`, 1 Dmg). Starting Zone: `Burial Vault`.
     * Skeleton B (Rattlebone Skeleton): Standard Undead (Size 1, Defence 2, Movement 1, Morale Immune). Trait: `Dry Bones`. Attack: Notched Scimitar (`Tough 5+/1`, 1 Dmg). Starting Zone: `Crypt Antechamber`.

### Step 5: Technical Performance & Monte Carlo Analytics
* **Performance Requirement**: Minimum 1,000 Monte Carlo iterations completing in $<10$ seconds.
  * Pure Python simulation design: Fast dice generation using standard random generator, state structs/dataclasses with minimal memory allocations, no string formatting or I/O in the batch loop.
  * Event listener pattern: Interactive CLI attaches an `EventLogger` that prints colored, formatted turn steps. Monte Carlo attaches a lightweight `MetricsCollector` that records outcomes (victory, rounds, remaining grit, mob size) with zero CLI overhead.
* **Statistical Metrics**:
  * Win Rate (% Goblin Party Victory), Defeat/TPK Rate (% Goblin Bosses Dead or Fled).
  * Boss Grit Remaining Distribution (Mean, Median, Min, Max).
  * Mob Casualties & Final Size Distribution (Mean surviving size, % Mobs wiped).
  * Combat Duration in Rounds (Mean, StdDev, Min, Max).
  * Feature A/B Impact: Delta Win Rate when equipping Shield vs 2H Heavy, Delta Win Rate with Meat Shield vs Ankle Bite, effect of Parrying Buckler on boss survival.

---

## 3. Caveats

1. **Bangaranga Pool in Batch Simulation**: While the Bangaranga Pool is a core table mechanic, in batch tactical simulations it can either be modeled with standard greedy draw rules (draw up to Grunt when TN $\ge 2$) or parameterized as a toggleable option to measure baseline gear balance vs chaotic party resource balance.
2. **Mob Boredom Rule Implementation**: The rule stating Mobs cannot perform the exact same action twice per turn (e.g. cannot Attack twice) is standard. Movement is the sole exception (can Move twice to charge/flee). The simulation AI must enforce this.
3. **Group Attack Cap**: In standard rules, at most 3 enemies swarm a single Goblin Boss, but any number can swarm a Mob. The AI target selection must enforce this cap to avoid artificial single-boss focus fire.

---

## 4. Conclusion

All mechanical, statistical, topological, and scenario requirements for the Gobbos Combat Simulator are thoroughly defined and grounded in official STAGE drafts. 

The software design should be structured as follows:
```
System_Tools/combat_sim/
├── combat_sim/
│   ├── __init__.py
│   ├── core/
│   │   ├── dice.py          # D6 dice pools, exploding 6s, salvage roll, gobbo gamble
│   │   ├── events.py        # Event types & dispatcher for logging/analytics
│   │   └── types.py         # Enums (Difficulty, Trait, Condition, Ancestry, ActionType)
│   ├── domain/
│   │   ├── entities.py      # BaseEntity, GoblinBoss, PlayerMob, Enemy, EliteBoss, EnemyMob
│   │   ├── equipment.py     # Weapon, Armor, Shield, Explosive (Bulk, Hands, Traits)
│   │   ├── quirks.py        # Quirk, Twist (Meat Shield, Ankle Bite, Push Luck)
│   │   └── topology.py      # Zone, ZoneProfile, ZoneTrait, Cover, TopologyGraph
│   ├── engine/
│   │   ├── combat.py        # CombatEngine, CombatLoop, RoundManager
│   │   ├── resolver.py      # ClatterResolver, AttackResolver, HazardResolver, MoraleResolver
│   │   └── ai.py            # Heuristic tactical AI for Bosses, Mobs, and Enemies
│   ├── scenarios/
│   │   ├── registry.py      # Scenario loader & builder registry
│   │   ├── street_skirmish.py
│   │   ├── maulers_den.py
│   │   └── tomb_highwayman.py
│   ├── cli/
│   │   ├── runner.py        # Interactive step-by-step CLI runner with colored event logs
│   │   └── main.py          # Entrypoint for CLI commands
│   └── analytics/
│       ├── monte_carlo.py   # High-speed batch simulation runner (1000+ runs < 10s)
│       └── metrics.py       # Statistical aggregators, tables, and comparative reports
└── tests/
    ├── test_dice.py
    ├── test_equipment_armor.py
    ├── test_quirks.py
    ├── test_enemy_traits.py
    ├── test_mob_health.py
    ├── test_scenarios.py
    └── test_performance.py
```

---

## 5. Verification Method

To independently verify this specification and the forthcoming implementation:

1. **Unit Test Suite**:
   * Run: `python -m pytest System_Tools/combat_sim/tests`
   * Target Verifications:
     * `test_dice.py`: Exploding 6s on 4+/5+/6, double explosion on Bangaranga, Salvage roll logic on $\le 0$ dice, Gobbo Gamble 1s reroll and Fumble on continued failure.
     * `test_equipment_armor.py`: Weapon Impact Size $+1/+2$ on Stagger, Shield Tough Parry enablement, Armor Dice passive mitigation with Slink Bane penalties.
     * `test_quirks.py`: Meat Shield damage redirection to allied Mob in Zone, Ankle Bite $+1 \text{ Success}$ counter-attack on Dodge.
     * `test_enemy_traits.py`: Parrying Buckler Hard 6 first melee attack vs Normal 5+ subsequent attacks; Thick Blubber Bane vs Fire bypass; Troll Regrowth round start healing & Fire/Acid suppression; Overkill wound formula ($\lfloor \text{Succ}/D \rfloor$).
     * `test_mob_health.py`: Single-target damage decrement & spillover, die removal when $<1$, AoE/Cleave damage applied simultaneously across all dice in pool.
2. **Reference Encounters CLI Playout**:
   * Run: `python -m combat_sim.cli.main run --scenario street_skirmish --interactive`
   * Run: `python -m combat_sim.cli.main run --scenario maulers_den --interactive`
   * Run: `python -m combat_sim.cli.main run --scenario tomb_highwayman --interactive`
   * Inspect: Human-readable step-by-step output logs every round, action, dice roll, Clatter roll, and state transition.
3. **Monte Carlo Performance Benchmark**:
   * Run: `python -m combat_sim.cli.main batch --scenario street_skirmish --iterations 1000`
   * Verify: Execution completes in $< 10.0$ seconds and displays complete statistical summary (Win/Loss/TPK, Boss Grit distribution, Mob survival size distribution, Mean rounds).
