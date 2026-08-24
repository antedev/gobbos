# Gobbos Combat Simulator — Test Infrastructure Specification

This document defines the 4-tier testing architecture, feature coverage matrix, pass/fail semantics, and test runner instructions for the **Gobbos Combat Simulation & Balance Toolkit** (`05_System_Tools/combat_sim`).

---

## 1. 4-Tier Test Architecture

The test suite is structured into four distinct verification tiers to ensure mathematical fidelity, domain correctness, scenario execution integrity, and opaque-box acceptance compliance:

```
05_System_Tools/combat_sim/tests/
├── Tier 1: Core Mechanics & Math
│   ├── test_dice.py
│   └── test_mob_health.py
├── Tier 2: Domain, Gear & Trait Logic
│   ├── test_equipment_armor.py
│   ├── test_quirks.py
│   └── test_enemy_traits.py
├── Tier 3: Scenario Playout & Integration
│   └── test_scenarios.py
└── Tier 4: E2E Acceptance & Performance Benchmarks
    ├── test_e2e.py
    └── test_performance.py
```

### Tier 1: Core Mechanics & Math Unit Tests
- **Focus**: Pure deterministic and stochastic verification of dice pool resolution, exploding 6s, salvage rolls, Gobbo Gamble 1s rerolls, Bangaranga pool dynamics, and symmetrical Mob dice-HP mechanics.
- **Modules**:
  - `test_dice.py`: Tests `roll_dice`, `resolve_clatter`, `BangarangaPool`, difficulty scaling (Easy 4+, Normal 5+, Hard 6), recursive explosion tracking, and double-explosion critical triggers.
  - `test_mob_health.py`: Tests Mob health dice array transitions, single-target decrement with spillover into subsequent dice, die elimination when $< 1$, AoE/Cleave full-pool simultaneous damage, and cross-gang in-fighting on 1s.

### Tier 2: Domain, Equipment & Trait Unit Tests
- **Focus**: Object models, equipment mechanics, action economy, and special combat reactions.
- **Modules**:
  - `test_equipment_armor.py`: Tests weapon types (Light, Medium, Heavy +1 Impact Size, Crushing +2 Impact Size), Stagger calculations vs Target Size, Shield Tough Parry enablement, Armor Dice passive mitigation, Slink Bane penalties on Medium/Heavy armor, and Ablative Gear Sacrifice.
  - `test_quirks.py`: Tests modular Boss quirks (Meat Shield damage redirection to Mob, Ankle Bite +1 Success counter-attack on Dodge, Second Wind / Push Luck non-1s reroll), and power modifier twists.
  - `test_enemy_traits.py`: Tests Parrying Buckler (Hard 6 first melee attack per round, Normal 5+ subsequent), Thick Blubber (Bane -1d unless Fire), Voracious Regrowth (1 Wound healing at round start, disabled by Fire/Acid), Pressurized Steam Vent (reactive Slink test vs Fire hazard on Wound), Dry Bones (Bashing +1d Boon, Piercing/Cutting -1d Bane), and Boss Overkill wound formulas ($\lfloor \text{Successes}/\text{Defence TN} \rfloor$).

### Tier 3: Scenario Playout & Integration Tests
- **Focus**: Multi-unit, multi-zone scenario playouts exercising full round loops, action economies, and victory conditions.
- **Modules**:
  - `test_scenarios.py`: Validates setup, topology graph connections, unit rosters, step-by-step turn execution, and victory/defeat evaluation for:
    1. *Street Skirmish* (Armored Boss + Size 3 Mob vs Robber Gang & Footpads across 3 street zones).
    2. *The Mauler's Den* (2 Heavy Weapon Bosses + 2 Mobs vs Forest Mauler in 2 cave zones).
    3. *Tomb of the Highwayman* (Boss + Mob vs Armored Highwayman & Rattlebone Skeletons in crypt with Slippery and Shoring traits).

### Tier 4: E2E Acceptance & Performance Benchmarks
- **Focus**: Opaque-box verification of all acceptance criteria and batch simulation throughput benchmarks.
- **Modules**:
  - `test_e2e.py`: Full acceptance criteria verification validating end-to-end combat lifecycles, action economy bounds, event logging dispatch, and statistical report generation.
  - `test_performance.py`: High-throughput performance benchmark verifying $\ge 1,000$ Monte Carlo iterations execute in $< 10.0$ seconds.

---

## 2. Feature Coverage Matrix

All 48 features specified in `PROJECT.md` and `ORIGINAL_REQUEST.md` are mapped to explicit tests:

| Feature # | Feature Name | Primary Test Module | Key Test Functions |
|---|---|---|---|
| 1 | Dice Pool Resolution | `test_dice.py` | `test_dice_pool_difficulties`, `test_dice_pool_tn_successes` |
| 2 | Exploding 6s | `test_dice.py` | `test_exploding_sixes_recursive`, `test_exploding_sixes_distribution` |
| 3 | Critical Double Explosions | `test_dice.py` | `test_critical_double_explosion_trigger` |
| 4 | Salvage Roll (Zero Dice) | `test_dice.py` | `test_salvage_roll_zero_dice`, `test_salvage_roll_fumble` |
| 5 | Gobbo Gamble | `test_dice.py` | `test_gobbo_gamble_reroll_ones_success`, `test_gobbo_gamble_fumble_penalty` |
| 6 | Bangaranga Pool | `test_dice.py` | `test_bangaranga_pool_tax_and_draw`, `test_bangaranga_double_explosion`, `test_bangaranga_drain_on_fail` |
| 7 | Boons and Banes Modifier Cap | `test_dice.py`, `test_equipment_armor.py` | `test_boons_and_banes_stacking_and_cancellation` |
| 8 | Boss Entity Model & Actions | `test_equipment_armor.py`, `test_e2e.py` | `test_boss_action_budget_reset`, `test_boss_grit_and_grunt` |
| 9 | Mob Entity Model & Symmetrical Dice-HP | `test_mob_health.py` | `test_mob_dice_hp_initialization`, `test_mob_size_tracking` |
| 10 | Standard Enemy (1-Hit Kill) | `test_enemy_traits.py`, `test_scenarios.py` | `test_standard_enemy_one_hit_kill` |
| 11 | Elite / Boss Enemy (Overkill Wounds) | `test_enemy_traits.py` | `test_overkill_wounds_exact_multiples`, `test_overkill_wounds_remainder` |
| 12 | Enemy Mob Model & Attack Scaling | `test_mob_health.py`, `test_scenarios.py` | `test_enemy_mob_attack_damage_scaling` |
| 13 | Melee Weapons & Traits | `test_equipment_armor.py` | `test_melee_weapon_types_and_handedness` |
| 14 | Stagger Mechanics & Impact Size | `test_equipment_armor.py` | `test_stagger_calculation_impact_vs_target_size`, `test_stagger_mass_resistance_negation` |
| 15 | Ranged Weapons & Cover | `test_equipment_armor.py`, `test_scenarios.py` | `test_ranged_weapon_zones_and_cover_banes` |
| 16 | Armor & Shields | `test_equipment_armor.py` | `test_armor_dice_mitigation_on_five_plus`, `test_armor_slink_bane_penalties`, `test_shield_enables_tough_parry` |
| 17 | Clatter Roll Defense | `test_dice.py`, `test_equipment_armor.py` | `test_clatter_clean_dodge`, `test_clatter_mitigation_on_failed_dodge`, `test_clatter_zero_saved_actions` |
| 18 | Ablative Gear Sacrifice | `test_equipment_armor.py` | `test_ablative_gear_sacrifice_negates_lethal_damage` |
| 19 | Mob Gear & Bulk Scaling | `test_equipment_armor.py` | `test_mob_armor_bulk_scaling_and_casualties` |
| 20 | Consumables & Explosive Area Profiles | `test_equipment_armor.py` | `test_explosive_area_threat_profiles_and_impact_size` |
| 21 | Boss Quirk: Meat Shield | `test_quirks.py` | `test_meat_shield_damage_redirection_to_mob`, `test_meat_shield_requires_mob_in_zone` |
| 22 | Boss Quirk: Ankle Bite | `test_quirks.py` | `test_ankle_bite_counter_attack_on_dodge`, `test_ankle_bite_plus_one_success` |
| 23 | Boss Quirk: Push Luck / Second Wind | `test_quirks.py` | `test_push_luck_rerolls_non_ones`, `test_push_luck_grunt_cost` |
| 24 | Ancestry Traits | `test_enemy_traits.py` | `test_ancestry_undead_morale_and_holy_weakness`, `test_ancestry_beast_morale_triggers` |
| 25 | Enemy Trait: Parrying Buckler | `test_enemy_traits.py` | `test_parrying_buckler_first_melee_hard_six`, `test_parrying_buckler_subsequent_normal_five` |
| 26 | Enemy Trait: Thick Blubber | `test_enemy_traits.py` | `test_thick_blubber_bane_penalty`, `test_thick_blubber_fire_tag_bypass` |
| 27 | Enemy Trait: Voracious Regrowth | `test_enemy_traits.py` | `test_voracious_regrowth_heals_wound`, `test_voracious_regrowth_disabled_by_fire_or_acid` |
| 28 | Enemy Trait: Steam Vent | `test_enemy_traits.py` | `test_steam_vent_hazard_reaction_on_wound` |
| 29 | Zones & Graph Topologies | `test_scenarios.py`, `test_e2e.py` | `test_topology_graph_distance_and_movement` |
| 30 | Cover & Zone Traits | `test_scenarios.py` | `test_zone_traits_slippery_and_burning`, `test_zone_traits_shoring_collapse` |
| 31 | Combat Loop & Phase Flow | `test_scenarios.py`, `test_e2e.py` | `test_combat_loop_five_phases` |
| 32 | Player Actions Resolution | `test_scenarios.py`, `test_e2e.py` | `test_player_action_resolution_move_attack_order` |
| 33 | Unordered Mob Resolution | `test_mob_health.py` | `test_unordered_mob_loitering_and_out_of_control` |
| 34 | Mob Scatter Reaction | `test_mob_health.py` | `test_mob_scatter_clean_success`, `test_mob_scatter_gamble_trample_disaster` |
| 35 | Mob Health Decrement & Spillover | `test_mob_health.py` | `test_mob_single_target_damage_and_spillover`, `test_mob_die_removal_when_zero` |
| 36 | AoE Multi-Die Damage | `test_mob_health.py` | `test_mob_aoe_damage_simultaneous_all_dice` |
| 37 | Round Closure & Morale | `test_enemy_traits.py`, `test_scenarios.py` | `test_round_closure_stagger_removal`, `test_swarm_terror_fifty_percent_casualties` |
| 38 | Tactical Combat AI | `test_scenarios.py`, `test_performance.py` | `test_tactical_ai_heuristic_action_selection` |
| 39 | Interactive CLI Runner | `test_e2e.py` | `test_cli_runner_step_by_step_logging` |
| 40 | Event Logging System | `test_e2e.py` | `test_event_dispatcher_and_structured_events` |
| 41 | Monte Carlo Batch Engine | `test_performance.py` | `test_monte_carlo_batch_execution_1000_runs` |
| 42 | Statistical Analytics Suite | `test_performance.py`, `test_e2e.py` | `test_statistical_metrics_win_loss_grit_mob_survival` |
| 43 | Scenario: Street Skirmish | `test_scenarios.py` | `test_scenario_street_skirmish_execution` |
| 44 | Scenario: The Mauler's Den | `test_scenarios.py` | `test_scenario_maulers_den_execution` |
| 45 | Scenario: Tomb of the Highwayman | `test_scenarios.py` | `test_scenario_tomb_highwayman_execution` |
| 46 | Scenario Registry & Loader | `test_scenarios.py`, `test_e2e.py` | `test_scenario_registry_lookup_and_custom_loader` |
| 47 | 4-Tier E2E Test Suite | `test_e2e.py` | `test_full_suite_acceptance_verification` |
| 48 | Adversarial Coverage Hardening | `test_dice.py`, `test_mob_health.py`, `test_e2e.py` | `test_adversarial_zero_and_extreme_pools`, `test_adversarial_invalid_gamble_transitions` |

---

## 3. Pass/Fail Semantics & Rules Compliance

### Zero Facade Rule
Every test in this suite exercises real underlying game rules and state transformations. No mock facades, hardcoded pass booleans, or trivial tautologies (`assert True`) are permitted.

### Deterministic Seeding & Stochastic Validation
- Unit tests validating specific rule branches use fixed random seeds or controlled test mocks to assert exact face values, explosion cascades, and Clatter resolutions.
- Monte Carlo tests assert statistical confidence bounds (e.g. exploding 6s mean success rate matches analytical Poisson/geometric expansion).

### Failure Escalation Protocol
If a test fails due to a discrepancy in the implementation, the failure is reported with:
1. Expected result derived from official rule text (`01_STAGE_Drafts/` or `02_PROD_Core_Rules/`).
2. Actual output from the implementation.
3. Specific file and line number in `combat_sim/`.

---

## 4. Test Runner Instructions

### Prerequisites
Ensure Python 3.10+ is available with `pytest` installed:
```powershell
python -m pip install pytest pytest-cov
```

### Running the Entire Suite
To run all 8 test modules:
```powershell
python -m pytest 05_System_Tools/combat_sim/tests/ -v
```

### Running by Tier
- **Tier 1 (Core Mechanics & Math)**:
  ```powershell
  python -m pytest 05_System_Tools/combat_sim/tests/test_dice.py 05_System_Tools/combat_sim/tests/test_mob_health.py -v
  ```
- **Tier 2 (Domain, Equipment & Traits)**:
  ```powershell
  python -m pytest 05_System_Tools/combat_sim/tests/test_equipment_armor.py 05_System_Tools/combat_sim/tests/test_quirks.py 05_System_Tools/combat_sim/tests/test_enemy_traits.py -v
  ```
- **Tier 3 (Scenarios Integration)**:
  ```powershell
  python -m pytest 05_System_Tools/combat_sim/tests/test_scenarios.py -v
  ```
- **Tier 4 (Acceptance & Performance Benchmark)**:
  ```powershell
  python -m pytest 05_System_Tools/combat_sim/tests/test_e2e.py 05_System_Tools/combat_sim/tests/test_performance.py -v
  ```

### Performance Benchmark Execution
To execute the 1,000+ iteration benchmark and verify the $< 10.0$s SLA:
```powershell
python -m pytest 05_System_Tools/combat_sim/tests/test_performance.py -v -s
```
