## 2026-08-23T21:55:51Z
You are the Implementation Worker for Milestone 4: Monte Carlo Batch Simulator & Statistical Analytics.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m4_analytics_worker\

You MUST read the authoritative specifications first:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\TEST_INFRA.md

Your mission:
Implement Milestone 4 in `05_System_Tools/combat_sim`:
1. `combat_sim/analytics/monte_carlo.py`:
   - `MonteCarloSimulator`: High-throughput batch simulation engine.
   - Supports running $N$ iterations (100 to 10,000+).
   - Performance SLA: Minimum 1,000 iterations must complete in $< 10.0$ seconds.
2. `combat_sim/analytics/metrics.py`:
   - `SimulationMetrics` & `StatisticalAggregator`:
     - Win rate, Loss rate, TPK rate for Goblin Party.
     - Distribution of Boss Grit remaining (mean, median, min, max, stddev).
     - Distribution of surviving Mob size & casualty count.
     - Encounter duration in rounds (mean, median, min, max, stddev).
     - A/B balance comparison analytics (e.g. Shield vs 2H Heavy, Meat Shield vs Ankle Bite).
     - Formatted ASCII summary tables.
3. `combat_sim/analytics/__init__.py`.

Exclusive write ownership: You exclusively own all files in `combat_sim/analytics/`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task.

Test and verify:
`python -m pytest tests/test_performance.py -v -s`
Write your handoff report to:
`c:\Users\ante\Documents\github\gobbos\.agents\m4_analytics_worker\handoff.md`

When done, send a message back with your summary and benchmark numbers.
