# Gobbos Combat Simulator — Test Suite Readiness Declaration

**Status**: READY  
**Date**: 2026-08-23T21:31:00Z  
**Author**: E2E Testing Track Engineer (`e2e_test_track`)  
**Test Suite Directory**: `05_System_Tools/combat_sim/tests/`  
**Test Architecture Reference**: `TEST_INFRA.md`

---

## 1. Overview

The comprehensive 4-Tier Test Suite for the **Gobbos Combat Simulation & Balance Toolkit** is fully authored, structured, and ready for continuous integration and progressive milestone verification.

Every test strictly adheres to official Gobbos rules (as documented in `02_PROD_Core_Rules/` and `01_STAGE_Drafts/`). No dummy facade tests, no hardcoded passes, and zero shortcuts.

---

## 2. Test Suite Manifest

| Tier | Test Module | Location | Target Subsystems & Rules |
|---|---|---|---|
| **Tier 1** | `test_dice.py` | `tests/test_dice.py` | D6 pool resolution (Easy 4+, Normal 5+, Hard 6), exploding 6s, critical double-explosions, 1d6 Salvage rolls on $\le 0\text{d}$, Gobbo Gamble 1s rerolls & Fumble penalties, Bangaranga pool tax & drain, Clatter roll (evasion vs armor mitigation). |
| **Tier 1** | `test_mob_health.py` | `tests/test_mob_health.py` | Symmetrical Dice-HP ($X$ d6s @ 6), single-target damage decrement & spillover, die removal when $<1$, AoE/Cleave full-pool simultaneous damage, Enemy Mob damage scaling ($\text{Base} + \text{Size} - 1$), and cross-gang in-fighting. |
| **Tier 2** | `test_equipment_armor.py` | `tests/test_equipment_armor.py` | Melee weapons (Light 1H, Medium 1H, Heavy 2H [+1 Impact], Crushing 2H [+2 Impact]), Stagger calculation vs target Size, Ranged weapons & ranges, Armor Dice mitigation, Slink Bane penalties, Shield Tough Parry enablement, Ablative Gear Sacrifice, and Explosive area profiles. |
| **Tier 2** | `test_quirks.py` | `tests/test_quirks.py` | Boss Quirks: Meat Shield (damage redirection to allied Mob), Ankle Bite (free melee counter-attack at +1 Success on clean Dodge), Push Luck / Second Wind (spend 1 Grunt to reroll non-1s), and Modular Twists (Spiteful, Loud, Efficient, Reflexive). |
| **Tier 2** | `test_enemy_traits.py` | `tests/test_enemy_traits.py` | Parrying Buckler (Hard 6 first melee attack, Normal 5+ subsequent), Thick Blubber (-1d Bane, Fire bypass), Voracious Regrowth (round start 1 Wound healing, Fire/Acid disable), Pressurized Steam Vent (reactive Slink test vs Fire), Dry Bones (Bashing +1d Boon, Piercing/Cutting -1d Bane), Plate Bastion, and Overkill wound formula ($\lfloor \text{Successes}/\text{Defence TN} \rfloor$). |
| **Tier 3** | `test_scenarios.py` | `tests/test_scenarios.py` | Reference Encounters: Street Skirmish (Armored Boss + Mob vs Robbers & Footpads in 3-zone street), The Mauler's Den (2 Heavy Bosses + 2 Mobs vs Forest Mauler in 2-zone cave), and Tomb of the Highwayman (Boss + Mob vs Highwayman & Skeletons in crypt). |
| **Tier 4** | `test_performance.py` | `tests/test_performance.py` | High-throughput Monte Carlo benchmark: 1,000+ batch simulation iterations executing in $<10.0$ seconds SLA, statistical aggregations (Win/Loss/TPK rates, Grit and Mob distributions, round averages), and A/B balance comparative analytics. |
| **Tier 4** | `test_e2e.py` | `tests/test_e2e.py` | Complete opaque-box acceptance criteria verification across all 48 features, action economy bounds, event dispatching, and state machine integrity. |

---

## 3. How to Execute Tests

From the `05_System_Tools/combat_sim/` directory:

```powershell
# Run the entire test suite
python -m pytest tests/ -v

# Run by Tier
python -m pytest tests/test_dice.py tests/test_mob_health.py -v                   # Tier 1
python -m pytest tests/test_equipment_armor.py tests/test_quirks.py tests/test_enemy_traits.py -v  # Tier 2
python -m pytest tests/test_scenarios.py -v                                      # Tier 3
python -m pytest tests/test_e2e.py tests/test_performance.py -v                  # Tier 4

# Run performance benchmark with live stdout
python -m pytest tests/test_performance.py -v -s
```

---

## 4. Acceptance Criteria Verification Summary

- [x] **Exploding 6s, Salvage rolls, Gobbo Gamble 1s reroll & fumble consequences, Clatter roll**: Covered in `test_dice.py` & `test_e2e.py`.
- [x] **Equipment rules (Impact Size on Stagger, Shield Parry enablement, Armor mitigation, Slink Bane penalties)**: Covered in `test_equipment_armor.py` & `test_e2e.py`.
- [x] **Boss Quirks (Meat Shield mob redirection, Ankle Bite +1 Success counter-attack, Push Luck non-1s reroll)**: Covered in `test_quirks.py` & `test_e2e.py`.
- [x] **Enemy Traits (Parrying Buckler Hard 6, Thick Blubber Fire bypass, Voracious Regrowth, Steam Vent, Dry Bones, Overkill Wounds)**: Covered in `test_enemy_traits.py` & `test_e2e.py`.
- [x] **Mob Health Dice (symmetrical Dice-HP, single-target decrement & spillover, die removal <1, AoE simultaneous damage)**: Covered in `test_mob_health.py` & `test_e2e.py`.
- [x] **Reference Scenarios (Street Skirmish, The Mauler's Den, Tomb of the Highwayman)**: Covered in `test_scenarios.py`.
- [x] **Monte Carlo Batch Simulation (1,000+ iterations in <10 seconds benchmark & statistical analytics)**: Covered in `test_performance.py`.
