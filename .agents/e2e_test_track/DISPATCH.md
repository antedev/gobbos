## 2026-08-23T21:27:25Z
You are the E2E Testing Track Engineer for the Gobbos Combat Simulator.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\e2e_test_track\

You MUST read the authoritative original user request and project scope first:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_rules_0\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_gear_0\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\explorer_scenarios_0\handoff.md

Your mission:
1. Author `c:\Users\ante\Documents\github\gobbos\TEST_INFRA.md` at project root documenting the 4-tier test architecture, feature coverage matrix, pass/fail semantics, and runner instructions.
2. Author the comprehensive test suite in `05_System_Tools/combat_sim/tests/`:
   - `test_dice.py` (exploding 6s, salvage rolls, Gobbo Gamble 1s rerolls & fumbles, Bangaranga pool).
   - `test_equipment_armor.py` (weapon impact size stagger, shield Tough parry enablement, armor dice mitigation, Slink bane penalties, ablative gear sacrifice).
   - `test_quirks.py` (Meat Shield mob redirection, Ankle Bite Dodge counter-attack +1 success, Push Luck non-1s reroll).
   - `test_enemy_traits.py` (Parrying Buckler Hard 6 first-attack, Thick Blubber fire bypass, Voracious Regrowth round healing & fire disable, Steam Vent wound reaction, Dry Bones Bashing/Piercing traits, Overkill wound calculation).
   - `test_mob_health.py` (symmetrical dice-HP, single-target decrement & spillover, die removal <1, AoE/Cleave full-pool simultaneous damage, cross-gang in-fighting).
   - `test_scenarios.py` (Street Skirmish, The Mauler's Den, Tomb of the Highwayman execution & victory conditions).
   - `test_performance.py` (1,000+ Monte Carlo iterations in <10 seconds benchmark).
   - `test_e2e.py` (Full opaque-box acceptance criteria verification).
3. Once the test infrastructure and test files are written, publish `c:\Users\ante\Documents\github\gobbos\TEST_READY.md` at project root.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All test cases must be genuine and strictly adhere to official Gobbos rules. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A forensic auditor will independently verify your work.

Write your completion report to:
`c:\Users\ante\Documents\github\gobbos\.agents\e2e_test_track\handoff.md`

When complete, send a message back with summary and artifact paths.
