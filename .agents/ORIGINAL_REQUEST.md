# Original User Request

## 2026-08-23T21:23:18Z

A Python-based combat simulation and balance toolkit for the Gobbos TTRPG, implementing the official stage rules for Goblin Bosses (with equipment, weapons, armor, and quirks/talents), player Mobs, Enemies (with special traits, ancestries, and reactions), and abstract Zone topologies, supporting both detailed step-by-step encounter playouts and batch Monte Carlo statistical analysis.

Working directory: System_Tools/combat_sim
Integrity mode: development

## Requirements

### R1. Tactical Domain, Equipment, Quirks & Encounter Configuration
Model all core Gobbos combat entities, equipment, quirks, and environments in Python:
- **Goblin Bosses**: Stats (Tough, Slink, Brains, Mouth, Grunt), Grit tracking, 3 Standard Actions + 1 Free Order per round, and customizable loadouts (weapons, armor, shields, quirks).
- **Equipment, Weapons & Armor**:
  - *Melee Weapons*: Light (1H, Size 0/1), Medium (1H), Heavy (2H, `+1` Impact Size for Stagger calculation), and weapon traits (e.g. `Bashing` granting +1d against skeletons, `Cleave`).
  - *Ranged Weapons*: Slings (1 Zone), Shortbows/Crossbows (2 Zones), Arbalests (3 Zones, Heavy).
  - *Armor & Shields*: Light Armor (+1d Armor Die), Medium Armor (+2d Armor Dice, Bane 1 on Slink), Heavy Armor (+3d Armor Dice, Bane 2 on Slink), Shields (+1d Armor Die and enables Tough Parry reaction).
  - *Mob Gear*: Mob Armor scaling (Bulk = Size $\times$ rating, passive armor dice), shared tools, and explosives/consumables (Spark Bombs, Molotovs, Powder Kegs with Area Threat profiles).
- **Boss Quirks / Talents**: Modular special abilities (trigger, cost, mechanical effect), including:
  - *Meat Shield*: Spend Grunt/Reaction when hit to shove an allied Mob in the zone to take the hit.
  - *Ankle Bite*: Passive trigger on successful Dodge reaction to make an immediate counter-attack with +1 Success.
  - *Second Wind / Push Luck*: Spend Grunt to reroll non-1 dice on a critical test.
- **Enemies & Special Traits**: Deterministic threats across Standard, Elite/Boss (Wounds track with Overkill rule), and Enemy Mobs, plus active special traits and ancestries:
  - *Ancestry Traits*: Beasts (Fire/Loud morale triggers), Undead (Morale immune, Holy weakness, Piercing/Cutting resistance), Monstrosity (Sweeping Cleave, Stagger mass resistance).
  - *Unique Traits & Reactions*: Parrying Buckler (first melee attack each round is Hard 6), Thick Blubber / Bastion (damage reduction or Bane on attackers), Retaliatory Spite / Steam Vent (reactive damage/hazard when wounded), and Voracious Regrowth (heals Wounds at round start unless burned/acidified).
- **Zones & Topologies**: Interconnected graph of Zones, each with a Zone Profile (`Difficulty+/TN`), Cover (Partial/Full), and standard traits/hazards (Slippery, Burning, Toxic Spores, Narrow, Pillars, Rubble).
- **Scenario Definitions**: Support defining encounters (units, loadouts, quirks, starting zones, zone connections, traits, objectives) via clean Python code or structured configuration.

### R2. Rules-Accurate Gobbos Combat Engine
Implement the complete Gobbos combat loop:
- **Dice System**: D6 dice pool tests against difficulty thresholds (Easy 4+, Normal 5+, Hard 6), exploding 6s (and criticals on double explosion), Salvage rolls (1d6 on $\le 0$ dice), and the Gobbo Gamble (rerolling 1s on failed tests, suffering Fumbles and $-1$ Grunt if still failing).
- **Player Active Turn**: Boss and Mob action economy (Move, Melee/Ranged Attack, Plunder, Manipulate, Order), equipment trait resolution, Quirk activations, and un-ordered Mob resolution (Loitering and Out-of-Control d6 tables).
- **Enemy Active Turn**: Deterministic enemy attacks (GM never rolls to hit); Player Clatter Rolls (active Slink/Tough evasion vs. Threat TN, passive Armor Dice reducing damage on 5+); Mob "Scatter!" reaction via Boss Mouth test with Size penalties and Gobbo Gamble panic consequences; enemy special triggers.
- **Round Closure & Morale**: Removal of Staggered condition, end-of-round hazard ticks, enemy regeneration/reinforcements, and 50% casualty Swarm Terror Morale checks.

### R3. Interactive Step-by-Step Encounter Runner
Provide a CLI runner to step through an encounter round-by-round or action-by-action with readable, formatted event logs showing:
- Active phase and current round state.
- Action declarations, target selections, zone movement, weapon/quirk usage.
- Exact dice rolls (individual faces, explosions, Clatter resolutions, Gambles).
- Health/Grit/Wound changes, armor mitigations, and condition updates.
- End-of-combat summary (victor, surviving units, casualties, total rounds).

### R4. Monte Carlo Batch Simulator & Statistical Analytics
Provide a batch execution mode capable of running $N$ iterations (e.g., 100 to 10,000 runs) of an encounter scenario with automated tactical AI heuristics, outputting aggregate statistics:
- Win / Loss / TPK rates for the Goblin party.
- Distribution of Boss Grit remaining and Mob casualties/survival sizes.
- Average encounter duration in rounds.
- Impact of specific equipment (e.g. Shields vs Heavy 2H), Quirks, and Enemy special traits on party survival.

## Acceptance Criteria

### Engine, Equipment & Trait Fidelity
- [ ] Programmatic unit tests verify exploding 6s, Salvage roll logic, Gobbo Gamble 1s reroll & fumble consequences, and Clatter roll (evasion vs. armor mitigation).
- [ ] Programmatic unit tests verify Equipment rules: Weapon Impact Size modifiers on Stagger, Shield Parry enablement, and Armor Dice mitigation with Slink Bane penalties.
- [ ] Programmatic unit tests verify Boss Quirks (e.g. Meat Shield damage redirection, Ankle Bite Dodge counter-attack).
- [ ] Programmatic unit tests verify Enemy Traits (e.g. Parrying Buckler Hard 6 first-attack rule, Troll Regrowth & Fire disabling, Overkill Wound calculation).
- [ ] Programmatic unit tests verify Mob health dice mechanics: single-target damage decrement, spillover into subsequent dice, die removal when $<1$, and AoE damage applied simultaneously across all dice in the pool.

### Simulation Execution & Scenario Coverage
- [ ] Includes pre-built reference encounters exercising equipment, quirks, and enemy traits:
  1. *Street Skirmish*: Armored Boss (Shield + Sword + Ankle Bite quirk) + Size 3 Mob vs. Robber Gang & Footpads in a multi-zone street with Partial Cover.
  2. *The Mauler's Den*: 2 Bosses (Heavy weapons + Meat Shield quirk) + 2 Mobs vs. Forest Mauler (Elite Bear with Thick Blubber and Crushing Claws Cleave).
  3. *Tomb of the Highwayman*: Boss & Mob vs. Armored Highwayman (Parrying Buckler) & Rattlebone Skeletons in a crypt with Slippery and Shoring traits.
- [ ] CLI command can run any reference scenario in step-by-step mode and output complete, human-readable turn-by-turn combat logs.
- [ ] CLI command can run batch Monte Carlo simulation (minimum 1,000 iterations) for any scenario, completing in under 10 seconds and displaying clear statistical metrics.

## 2026-08-24T17:36:53Z

Synthesize a complete, streamlined, modular core rules book for the Gobbos TTRPG in `02_PROD_Core_Rules/`. The document must isolate pure game mechanics and systemic loops from living content (weapons, equipment catalogs, spell lists, monster bestiaries, quirk compendiums), establish a clean logical reading order with single-source rule definitions and cross-references, embed explicit `[CONTENT EXTENSION POINT]` tags along with standard structural schemas/templates (defining the attributes, parameters, and format required when creating content instances), and mark mechanical gaps with `[MISSING RULE / GAP]` tags.

Working directory: `c:\Users\ante\Documents\github\gobbos`
Integrity mode: development

## Requirements

### R1. Engine vs. Content Delimitation & Content Schemas
Extract pure systemic game mechanics from all current materials (`01_STAGE_Drafts/` and existing `02_PROD_Core_Rules/`) while completely stripping out living content catalogs (equipment stat tables, weapon compendiums, exhaustive quirks, spell lists, monster statblocks). For every content category (Weapons, Armor, Gear, Quirks, Tag Effects, Spells/Rituals, NPC/Enemy Statblocks, Lair Rooms), provide:
1. A clear mechanical explanation of how that category functions in the game engine.
2. A formal outline/template (schema/class definition) showing all required attributes, tags, and formatting rules for instantiating new content items.
3. An explicit `[CONTENT EXTENSION POINT: <Category>]` marker indicating where compendium expansions plug in.

### R2. Modular Multi-File Chapter Structure in PROD
Organize the core rules in `02_PROD_Core_Rules/` into clean, logically sequenced chapters covering all necessary systemic domains:
- Core Resolution & Dice Pool Engine
- Attributes, Boss Profile & Gang Fundamentals
- The Action Economy & Turn Flow
- Zones, Movement, and Environment
- Combat Engine (Melee, Ranged, Defense, Reactions, Group Attacks)
- Mob Mechanics (Commanding, Mob Health/Dice, Morale, Dispersal)
- Damage, Grit, Conditions & Wounds
- Magic & Bangaranga Framework (the mechanical rules for spellcasting/wild magic without the spell lists)
- The Raid Loop (Loot Value, Scrap, Infamy, Raid Points)
- The Lair Loop (Investment, Upgrades, Character Death & Roguelite Progression)
- Journeys & Hazard Resolution

### R3. Single-Source Rule Definitions & Consistent Cross-Referencing
Every game mechanic must be authoritatively defined in exactly one primary chapter/section. All other sections that interact with that mechanic must cross-reference it rather than redefining or summarizing it with conflicting language. Where situational rules alter a standard rule, explicitly label them as exceptions.

### R4. Mechanical Gap Analysis & Missing Rule Markers
Audit the entire system for missing, incomplete, or ambiguous rules required for complete gameplay. Explicitly flag each gap with a standardized callout:
`[MISSING RULE / GAP: <Description of missing mechanic, why it is needed, and suggested resolution>]`.

### R5. Strict Style Guide & Keyword Compliance
All written rules must strictly follow the Tier A mechanical guidelines in `GEMINI.md`:
- Purely objective, direct, active present-tense instructional language (no melodramatic prose mixed into rules).
- Total de-gendering (second person "You" / explicit imperative nouns like "The Goblin Boss", "The Mob", "The GM").
- Standard slash notation for checks (`[Stat] [Target Face]+/[Successes]`).
- Zero tolerance for synonym drift (e.g. Grit vs. Health, Mob vs. Squad, Loot vs. generic treasure).

## Acceptance Criteria

### Content Separation & Structural Schemas
- [ ] No living content tables (full weapon lists, bestiaries, quirk catalogs, specific spell listings) exist within the core rule chapters.
- [ ] Every content type includes a structured template/schema defining its attributes, data fields, and tags before referencing the extension point.
- [ ] Every modular hook where content attaches contains an explicit `[CONTENT EXTENSION POINT]` block.

### Rule Integrity & Single-Source Architecture
- [ ] Every mechanical rule is fully explained in one place and referenced elsewhere via standard Markdown links.
- [ ] No contradictory rules or ambiguous duplicates exist across the chapters in `02_PROD_Core_Rules/`.
- [ ] Any situational rule variance is clearly marked as an exception to the baseline mechanic.

### Gap Visibility & Actionability
- [ ] All missing rules, broken loops, or undefined states are explicitly highlighted with `[MISSING RULE / GAP]` markers.

### Style & Format Adherence
- [ ] 100% of dice checks follow the `[Stat] [Target Face]+/[Successes]` slash notation (with no `+` on target 6).
- [ ] Header hierarchy strictly follows H1 -> H2 -> H3 with zero skips.
- [ ] Formatting matches `GEMINI.md` Golden Rules (`>>`) and Example blocks (`> **Example:**`).
