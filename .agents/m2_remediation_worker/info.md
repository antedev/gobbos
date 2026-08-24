# Milestone 2 Remediation Worker
Workspace: .agents/m2_remediation_worker/
Scope:
1. In `combat_sim/engine/ai.py`, import `ClatterResolver` from `combat_sim.engine.resolver`.
2. In `combat_sim/engine/ai.py`, implement Group Attack combining in `EnemyAI.execute_enemy_turns` (combine up to 3 attackers in same zone against a Boss into a single attack with +1 damage per extra enemy, 1 reaction; unlimited against Mobs).
3. In `combat_sim/engine/combat.py`, fix 50% casualty Morale check condition to `(len(enemies) + 1) // 2` or `math.ceil(len(enemies) / 2)`.
4. Run `pytest tests/ -v` and ensure all tests pass.
