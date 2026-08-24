# Project: Gobbos Combat Simulation & Balance Toolkit

## Architecture
The system is a pure Python tactical combat simulation and balance toolkit located in `05_System_Tools/combat_sim`. It provides:
1. **Core & Types (`combat_sim.core`)**: Dice pool roller with exploding 6s, salvage rolls, Gobbo Gamble 1s reroll, Bangaranga pool, events model, and system enums.
2. **Tactical Domain (`combat_sim.domain`)**: Goblin Bosses, Mobs, Standard/Elite/Mob Enemies, Equipment (Weapons, Armor, Shields, Consumables/Explosives), Quirks, Ancestries, Traits, and Graph-based Zone Topologies.
3. **Combat Engine (`combat_sim.engine`)**: Full 5-phase combat loop (Setup, Round Start, Player Active, Enemy Active, Round Closure), Clatter Roll resolver (active evasion vs passive armor mitigation), Mob health dice array decrement/spillover/AoE duplication, deterministic enemy threats, and tactical AI heuristics.
4. **Scenarios Library (`combat_sim.scenarios`)**: Scenario definitions and pre-built reference encounters (Street Skirmish, The Mauler's Den, Tomb of the Highwayman).
5. **Interactive CLI Runner (`combat_sim.cli`)**: Step-by-step turn-by-turn interactive or automated runner with human-readable, rich event logs.
6. **Monte Carlo Analytics (`combat_sim.analytics`)**: High-performance batch simulation engine (1,000+ runs in <10s) with statistical aggregation, win/loss/TPK rates, Grit and Mob survival distributions, and balance A/B analytics.
7. **Comprehensive Test Suite (`tests/`)**: 4-Tier requirement-driven E2E tests + unit test suite verifying every rule and trait.

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Dice Pool Resolution | D6 dice pool tests vs Easy 4+, Normal 5+, Hard 6 with TN successes | M2 | PROD/STAGE 01_Dice.md |
| 2 | Exploding 6s | Each natural 6 is 1 success and rolls an additional d6 recursively | M2 | PROD/STAGE 01_Dice.md |
| 3 | Critical Double Explosions | Consecutive 6 on bonus die gives +1 Grunt and free non-offensive action | M2 | PROD/STAGE 01_Dice.md |
| 4 | Salvage Roll | Pools <= 0d6 roll 1d6: 6=1 success, 1=Fumble, 2-5=fail | M2 | PROD/STAGE 01_Dice.md |
| 5 | Gobbo Gamble | On failed test with 1s, reroll all 1s; failure causes Fumble (-1 Grunt) | M2 | PROD/STAGE 01_Dice.md |
| 6 | Bangaranga Pool | Communal pool seeding, draw limits, tax if > TN, double exploding 6s, fail drain | M2 | PROD/STAGE 01_Dice.md |
| 7 | Boons and Banes | Situational +/- 1d modifiers with environmental net cap | M2 | STAGE 08_Master_Tag_Index.md |
| 8 | Boss Entity Model | Stats (Tough, Slink, Mouth, Brains, Grunt), Grit tracking, Action budget (3 Standard + 1 Free Order) | M1 | PROD 10_Stats.md |
| 9 | Mob Entity Model | Symmetrical Dice-HP ($X$ d6s at 6), Size tracking, 2-action budget, Boredom rule | M1 | STAGE 13_Goblin_mob.md |
| 10 | Standard Enemy Model | One-hit kill on hits meeting Defence TN, 2 actions, deterministic threats | M1 | STAGE 20_Enemies.md |
| 11 | Elite / Boss Enemy Model | Multi-Wound track, Overkill rule ($\lfloor \text{Successes}/\text{Defence TN} \rfloor$) | M1 | STAGE 20_Enemies.md |
| 12 | Enemy Mob Model | Shared Dice-HP, deterministic attack damage scaling ($\text{Base} + \text{Size} - 1$) | M1 | STAGE 20_Enemies.md |
| 13 | Melee Weapons & Traits | Light (1H), Medium (1H), Heavy (2H, +1 Impact Size), Crushing (+2 Impact Size), Bashing, Cleave | M1 | STAGE 33/35_Equipment.md |
| 14 | Stagger Mechanics | Partial hit inflicts Staggered if $\text{Impact Size} \ge \text{Target Size}$; mass resistance ignores | M2 | STAGE 02 Combat.md |
| 15 | Ranged Weapons | Slings (1 Zone), Shortbow/Crossbow (2 Zones), Arbalest (3 Zones, Heavy), range & cover penalties | M1 | STAGE 33/35_Equipment.md |
| 16 | Armor & Shields | Light (+1d), Medium (+2d, Slink Bane 1), Heavy (+3d, Slink Bane 2), Shields (+1d, Tough Parry enabled) | M1 | STAGE 33/35_Equipment.md |
| 17 | Clatter Roll Defense | Simultaneous Active Stat Dice (Slink Dodge / Tough Parry) + Passive Armor Dice vs Threat TN | M2 | STAGE 02 Combat.md |
| 18 | Ablative Gear Sacrifice | Boss at lethal damage can destroy Shield or Armor to reduce damage to 0 | M2 | STAGE 33_Equipment.md |
| 19 | Mob Gear & Scaling | Mob Armor Bulk = $\text{Size} \times \text{Bulk Rating}$, shared tools, encumbrance capacity | M1 | STAGE 13_Goblin_mob.md |
| 20 | Consumables & Explosives | Spark Bombs (T1), Molotovs (T2), Smoke Pots (T2), Powder Kegs (T3), Mortar Shells (T4), Sol-Quartz (T5) Area Profiles | M1 | STAGE 33/35_Equipment.md |
| 21 | Boss Quirk: Meat Shield | Spend 1 Grunt/Reaction to redirect hit to allied Mob in Zone | M1 | STAGE 14_Quirks.md |
| 22 | Boss Quirk: Ankle Bite | Free melee counter-attack at +1 Success on clean Dodge reaction | M1 | STAGE 14_Quirks.md |
| 23 | Boss Quirk: Push Luck | Spend 1 Grunt to reroll non-1 dice on any test | M1 | STAGE 14_Quirks.md |
| 24 | Ancestry Traits | Beast (Fire/Loud morale triggers), Undead (Morale immune, Holy weakness, Dry Bones resistance), Monstrosity (Mass resistance, Sweeping Cleave) | M1 | STAGE 21_Bestiary.md |
| 25 | Enemy Trait: Parrying Buckler | 1st melee attack received each round is Hard 6; subsequent are Normal 5+ | M1 | STAGE 21_Bestiary.md |
| 26 | Enemy Trait: Thick Blubber | -1d Bane on incoming attacks unless attack has [Fire] tag | M1 | STAGE 21_Bestiary.md |
| 27 | Enemy Trait: Voracious Regrowth | Heals 1 Wound at Round Start unless damaged by [Fire] or [Acidic] in prior round | M1 | STAGE 21_Bestiary.md |
| 28 | Enemy Trait: Steam Vent | Taking a Wound triggers Slink 5+/2 hazard test for 2 Fire damage in Zone | M1 | STAGE 21_Bestiary.md |
| 29 | Zones & Graph Topologies | Interconnected node graph, Zone Profiles (Difficulty+/TN), distance BFS | M1 | STAGE 03_Movement.md |
| 30 | Cover & Zone Traits | Partial Cover, Full Cover, Slippery, Burning, Toxic Spores, Narrow, Pillars, Rubble, Shoring | M1 | STAGE 03_Movement.md |
| 31 | Combat Loop & Phase Flow | 5-phase round structure, action resetting, reaction holding | M2 | STAGE 02 Combat.md |
| 32 | Player Actions Resolution | Move, Melee Attack, Ranged Attack, Plunder, Manipulate, Order | M2 | STAGE 02 Combat.md |
| 33 | Unordered Mob Resolution | Loitering table (1 action spent, 1 saved) and Out of Control table (2 actions spent, 0 saved) | M2 | STAGE 13_Goblin_mob.md |
| 34 | Mob Scatter Reaction | Boss Mouth vs Threat TN + Size penalty; clean move vs Gamble trample disaster | M2 | STAGE 02 Combat.md |
| 35 | Mob Health Decrement & Spillover | Single-target active die reduction, spillover to next die, die removal when < 1 | M2 | STAGE 13_Goblin_mob.md |
| 36 | AoE Multi-Die Damage | AoE/Cleave damage applied simultaneously to ALL dice in Mob pool | M2 | STAGE 13_Goblin_mob.md |
| 37 | Round Closure & Morale | Stagger auto-clear, hazard ticks, fire spread, 50% casualty Swarm Terror checks | M2 | STAGE 20_Enemies.md |
| 38 | Tactical Combat AI | Automated heuristic decision making for Bosses, Mobs, and deterministic Enemies | M2 | R4 specification |
| 39 | Interactive CLI Runner | Turn-by-turn interactive or automated runner with colored, formatted event logs | M3 | R3 specification |
| 40 | Event Logging System | Rich structured events for dice, actions, clatter, wounds, and summaries | M3 | R3 specification |
| 41 | Monte Carlo Batch Engine | High-speed batch execution (1,000+ runs in <10s) with progress reporting | M4 | R4 specification |
| 42 | Statistical Analytics Suite | Win/Loss/TPK rates, Boss Grit distributions, Mob survival metrics, A/B gear analytics | M4 | R4 specification |
| 43 | Scenario: Street Skirmish | Armored Boss (Shield + Sword + Ankle Bite) + Mob vs Robbers & Footpads in 3-zone street | M5 | Acceptance Criteria |
| 44 | Scenario: The Mauler's Den | 2 Bosses (Heavy 2H + Meat Shield) + 2 Mobs vs Forest Mauler in 2-zone cave | M5 | Acceptance Criteria |
| 45 | Scenario: Tomb of the Highwayman | Boss + Mob vs Armored Highwayman (Parrying Buckler) + Skeletons in 2-zone crypt | M5 | Acceptance Criteria |
| 46 | Scenario Registry & CLI Integration | Named scenario loader, custom config builder, CLI scenario arguments | M5 | R1/R3/R4 |
| 47 | 4-Tier E2E Test Suite | Comprehensive opaque-box and trait tests covering all 46 features and scenarios | M6 | Acceptance Criteria |
| 48 | Adversarial Coverage Hardening | Tier 5 white-box adversarial stress tests & extreme edge cases verification | M6 | Acceptance Criteria |

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Tactical Domain & Models | `combat_sim/core/types.py`, `combat_sim/domain/*` (Entities, Equipment, Quirks, Traits, Topologies, Consumables) | None | DONE |
| M2 | Dice & Core Combat Engine | `combat_sim/core/dice.py`, `combat_sim/engine/*` (CombatLoop, ClatterResolver, MobHealth, AI, Morale, Hazards) | M1 | DONE |
| M3 | Interactive CLI Runner & Event Logger | `combat_sim/core/events.py`, `combat_sim/cli/runner.py`, `combat_sim/cli/main.py` | M2 | IN_PROGRESS |
| M4 | Monte Carlo Simulator & Analytics | `combat_sim/analytics/monte_carlo.py`, `combat_sim/analytics/metrics.py` | M2 | PLANNED |
| M5 | Reference Encounters & Scenario Registry | `combat_sim/scenarios/*` (Street Skirmish, The Mauler's Den, Tomb of the Highwayman, Registry) | M1, M2, M3, M4 | PLANNED |
| M6 | Final Milestone: 100% E2E Pass & Tier 5 Hardening | Full test suite execution across Tiers 1-5, performance benchmark (<10s for 1k runs), Forensics Audit | M1, M2, M3, M4, M5, E2E Track | PLANNED |

---

## Interface Contracts

### `combat_sim.core.dice` ↔ `combat_sim.engine`
- `roll_dice(pool_size: int, difficulty: Difficulty, allow_gamble: bool = False, is_salvage: bool = False) -> DiceResult`
  - `DiceResult`: `successes: int`, `faces: List[int]`, `bonus_faces: List[int]`, `is_critical: bool`, `fumble: bool`, `salvage: bool`, `gambled: bool`
- `resolve_clatter(threat_tn: int, stat_dice: int, difficulty: Difficulty, armor_dice: int) -> ClatterResult`
  - `ClatterResult`: `evaded: bool`, `stat_successes: int`, `armor_successes: int`, `mitigated_damage: int`, `stat_faces: List[int]`, `armor_faces: List[int]`

### `combat_sim.domain` ↔ `combat_sim.engine`
- `BaseEntity`: `id: str`, `name: str`, `zone_id: str`, `is_alive: bool`, `conditions: Set[Condition]`
- `GoblinBoss(BaseEntity)`: `tough: int`, `slink: int`, `mouth: int`, `brains: int`, `grunt: int`, `max_grunt: int`, `grit: int`, `max_grit: int`, `actions_left: int`, `free_orders_left: int`, `saved_reactions: int`, `main_hand: Optional[Weapon]`, `off_hand: Optional[Equipment]`, `armor: Optional[Armor]`, `quirks: List[Quirk]`
- `PlayerMob(BaseEntity)`: `size: int`, `health_dice: List[int]`, `actions_left: int`, `is_ordered: bool`, `out_of_control: bool`, `armor_rating: int`
- `Enemy(BaseEntity)`: `enemy_scale: EnemyScale`, `wounds: int`, `max_wounds: int`, `defence_tn: int`, `movement: int`, `morale_tn: int`, `traits: List[EnemyTrait]`, `attacks: List[ThreatAttack]`
- `TopologyGraph`: `zones: Dict[str, Zone]`, `get_distance(z1: str, z2: str) -> int`, `get_adjacent(z: str) -> List[str]`

### `combat_sim.engine` ↔ `combat_sim.cli` & `combat_sim.analytics`
- `CombatEngine`: `setup_encounter(scenario: Scenario) -> CombatState`, `run_round() -> RoundSummary`, `run_to_completion(max_rounds: int = 50) -> CombatSummary`
- `EventDispatcher`: register listener callbacks for `on_action`, `on_roll`, `on_damage`, `on_condition`, `on_round_end`, `on_combat_end`

### `combat_sim.scenarios` ↔ `combat_sim.cli` & `combat_sim.engine`
- `Scenario`: `name: str`, `description: str`, `topology: TopologyGraph`, `allies: List[Union[GoblinBoss, PlayerMob]]`, `enemies: List[Enemy]`, `victory_condition: Callable[[CombatState], bool]`
- `get_scenario(name: str) -> Scenario`

---

## Code Layout

```
05_System_Tools/combat_sim/
├── pyproject.toml
├── README.md
├── combat_sim/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── types.py
│   │   ├── dice.py
│   │   └── events.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities.py
│   │   ├── equipment.py
│   │   ├── quirks.py
│   │   ├── traits.py
│   │   └── topology.py
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── combat.py
│   │   ├── resolver.py
│   │   └── ai.py
│   ├── scenarios/
│   │   ├── __init__.py
│   │   ├── registry.py
│   │   ├── street_skirmish.py
│   │   ├── maulers_den.py
│   │   └── tomb_highwayman.py
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── runner.py
│   │   └── main.py
│   └── analytics/
│       ├── __init__.py
│       ├── monte_carlo.py
│       └── metrics.py
└── tests/
    ├── __init__.py
    ├── test_dice.py
    ├── test_equipment_armor.py
    ├── test_quirks.py
    ├── test_enemy_traits.py
    ├── test_mob_health.py
    ├── test_scenarios.py
    ├── test_performance.py
    └── test_e2e.py
```
