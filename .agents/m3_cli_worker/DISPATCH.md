## 2026-08-23T21:55:51Z
You are the Implementation Worker for Milestone 3: Interactive CLI Runner & Event Logger.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m3_cli_worker\

You MUST read the authoritative specifications first:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\TEST_INFRA.md

Your mission:
Implement Milestone 3 in `05_System_Tools/combat_sim`:
1. `combat_sim/core/events.py`:
   - `EventType` enum (ROUND_START, ACTION_DECLARED, ROLL_RESOLVED, CLATTER_RESOLVED, DAMAGE_APPLIED, MOB_SCATTER, MOB_TRAMPLE, QUIRK_TRIGGERED, HAZARD_TICKED, MORALE_TRIGGERED, STAGGER_CLEARED, COMBAT_END).
   - `CombatEvent` dataclass with timestamp, round, phase, entity_id, description, details dict.
   - `EventDispatcher` listener registry.
   - `CombatEventFormatter` generating clean, colorized, human-readable turn-by-turn logs.
2. `combat_sim/cli/runner.py`:
   - `InteractiveRunner`: Step-by-step turn-by-turn interactive runner supporting step mode (press Enter to advance step, 'r' to advance round, 'a' to auto-complete) and non-interactive scripted output.
3. `combat_sim/cli/main.py`:
   - Full CLI application entrypoint using `argparse`.
   - Supports:
     - `run --scenario <name> [--interactive] [--seed <int>] [--max-rounds <int>]`
     - `batch --scenario <name> [--iterations <int>] [--seed <int>]`
     - `list-scenarios`
4. `combat_sim/cli/__init__.py`.

Exclusive write ownership: You exclusively own `combat_sim/core/events.py` and all files in `combat_sim/cli/`.
