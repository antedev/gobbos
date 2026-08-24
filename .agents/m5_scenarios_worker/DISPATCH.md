## 2026-08-23T21:55:51Z
You are the Implementation Worker for Milestone 5: Pre-Built Reference Encounters & Scenario Registry.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m5_scenarios_worker\

You MUST read the authoritative specifications first:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\TEST_INFRA.md
- c:\Users\ante\Documents\github\gobbos\.agents\explorer_scenarios_0\handoff.md

Your mission:
Implement Milestone 5 in `05_System_Tools/combat_sim`:
1. `combat_sim/scenarios/street_skirmish.py`:
   - Pre-built reference scenario: Armored Boss (Garg: Sword + Shield + Ankle Bite, Medium Armor) + Size 3 Mob vs Robber Gang (Enemy Mob Size 3) and 2 Footpads (Footpad A with Rusty Shiv, Footpad B with Thrown Cobblestone) across a 3-zone street topology (Street West, Street Center with Partial Cover, Alley East with Narrow).
2. `combat_sim/scenarios/maulers_den.py`:
   - Pre-built reference scenario: 2 Bosses (Skag: 2H Greataxe + Meat Shield, Grub: 2H Greatclub + Meat Shield, Light Armor) + 2 Mobs (Size 2 & Size 3) vs Forest Mauler (Elite Bear, 3 Wounds, Defence 2, Thick Blubber, Crushing Claws Cleave) across a 2-zone cave topology (Den Entrance Narrow, Main Den with Rubble and Pillars).
3. `combat_sim/scenarios/tomb_highwayman.py`:
   - Pre-built reference scenario: Boss (Wizgog: Spiked Mace Bashing + Push Luck, Light Armor) + Size 3 Mob vs Armored Highwayman (Elite, 2 Wounds, Defence 2, Parrying Buckler, Heavy Cleave) and 2 Rattlebone Skeletons (Dry Bones) across a 2-zone crypt topology (Crypt Antechamber with Slippery, Burial Vault with Shoring).
4. `combat_sim/scenarios/registry.py`:
   - `ScenarioRegistry` with `register`, `get_scenario(name)`, `list_scenarios()`, and factory registration for all 3 reference encounters.
5. `combat_sim/scenarios/__init__.py`.

Exclusive write ownership: You exclusively own all files in `combat_sim/scenarios/`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task.

Test and verify:
`python -m pytest tests/test_scenarios.py -v`
Write your handoff report to:
`c:\Users\ante\Documents\github\gobbos\.agents\m5_scenarios_worker\handoff.md`

When done, send a message back with your summary and test results.
