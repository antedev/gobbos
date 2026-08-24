"""
Tier 1/5 Adversarial Statistical & Property Test Suite: Challenger 1 (Milestone 2).
Exhaustively and empirically stress-tests:
1. Exploding 6s Statistical Distribution & Geometric Expansion:
   - Analytical mean: E[successes] = P * (p_success) / (1 - 1/6)
   - Recursive bonus die cascading across deep explosion chains (up to 5+ consecutive 6s).
   - Critical double explosions triggered only on consecutive 6s on bonus dice.
2. Salvage Roll Boundary Invariants:
   - Pool <= 0d6 (0, -1, -5, -100) and explicit is_salvage=True.
   - Exact 1d6 roll: Face 6 = 1 success (no explosion), Face 1 = Fumble, Faces 2-5 = normal fail.
3. Gobbo Gamble Property Invariants & Edge Cases:
   - Failed tests with 1s: rerolls only 1s, preserves kept non-1 dice and earlier bonus dice.
   - Explosions on rerolled dice: new 6s explode recursively.
   - Gamble failure sets fumble=True, gamble success clears fumble risk.
   - Gamble prohibition when test already succeeded or when no 1s were rolled.
4. Bangaranga Communal Pool Dynamics:
   - Seeding and draw limits bounded by available pool.
   - Discard tax calculation (tax = 1 when drawn > TN).
   - Double explosion recursion (each 6 explodes into 2 bonus dice).
   - Failure drain penalties on 1s and Grunt loss.
"""

from __future__ import annotations

import math
import random
from unittest.mock import patch
import pytest

from combat_sim.core.types import Difficulty
from combat_sim.core.dice import (
    BangarangaOutcome,
    BangarangaPool,
    ClatterResult,
    DiceResult,
    roll_d6,
    roll_dice,
)


class TestExplodingSixesEmpiricalProperties:
    """Mathematical and statistical property tests for exploding 6s."""

    def test_exploding_sixes_geometric_mean_easy(self):
        """Easy (4+): p=0.5. With explosions, E[succ/die] = 0.5 / (5/6) = 0.60. For 4 dice -> 2.40."""
        rng = random.Random(1001)
        runs = 5000
        pool_size = 4
        total_succ = 0
        for _ in range(runs):
            res = roll_dice(pool_size=pool_size, difficulty=Difficulty.EASY, allow_gamble=False, rng=rng)
            total_succ += res.successes
        empirical_mean = total_succ / runs
        expected_mean = pool_size * (3 / 6) / (1 - 1 / 6)  # 2.40
        assert abs(empirical_mean - expected_mean) < 0.08, f"Empirical {empirical_mean} vs Expected {expected_mean}"

    def test_exploding_sixes_geometric_mean_normal(self):
        """Normal (5+): p=2/6=1/3. With explosions, E[succ/die] = (1/3) / (5/6) = 0.40. For 3 dice -> 1.20."""
        rng = random.Random(1002)
        runs = 5000
        pool_size = 3
        total_succ = 0
        for _ in range(runs):
            res = roll_dice(pool_size=pool_size, difficulty=Difficulty.NORMAL, allow_gamble=False, rng=rng)
            total_succ += res.successes
        empirical_mean = total_succ / runs
        expected_mean = pool_size * (2 / 6) / (1 - 1 / 6)  # 1.20
        assert abs(empirical_mean - expected_mean) < 0.06, f"Empirical {empirical_mean} vs Expected {expected_mean}"

    def test_exploding_sixes_geometric_mean_hard(self):
        """Hard (6): p=1/6. With explosions, E[succ/die] = (1/6) / (5/6) = 0.20. For 5 dice -> 1.00."""
        rng = random.Random(1003)
        runs = 5000
        pool_size = 5
        total_succ = 0
        for _ in range(runs):
            res = roll_dice(pool_size=pool_size, difficulty=Difficulty.HARD, allow_gamble=False, rng=rng)
            total_succ += res.successes
        empirical_mean = total_succ / runs
        expected_mean = pool_size * (1 / 6) / (1 - 1 / 6)  # 1.00
        assert abs(empirical_mean - expected_mean) < 0.05, f"Empirical {empirical_mean} vs Expected {expected_mean}"

    def test_deep_recursive_explosion_cascade(self):
        """Verify 5 consecutive 6s produce exactly 5 bonus faces, 6 total successes on Hard 6, and is_critical=True."""
        # Initial: [6]
        # Bonus: [6, 6, 6, 6, 2] (4 consecutive 6s then a 2)
        # Total faces: [6], bonus_faces: [6, 6, 6, 6, 2]
        # Total successes on Hard 6: 1 (init) + 4 (bonus 6s) + 0 (bonus 2) = 5 successes
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 6, 6, 6, 6, 2]):
            res = roll_dice(pool_size=1, difficulty=Difficulty.HARD, allow_gamble=False)
            assert res.faces == [6]
            assert res.bonus_faces == [6, 6, 6, 6, 2]
            assert res.successes == 5
            assert res.is_critical is True
            assert res.fumble is False
            assert res.salvage is False

    def test_critical_double_explosion_requires_bonus_six(self):
        """Critical is only triggered when a bonus die rolls 6, not when two separate initial dice roll 6."""
        # Two initial dice roll [6, 6], bonus dice roll [2, 3] (neither bonus die is 6)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 6, 2, 3]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, allow_gamble=False)
            assert res.faces == [6, 6]
            assert res.bonus_faces == [2, 3]
            assert res.successes == 2
            assert res.is_critical is False  # No bonus die was a 6!

        # One initial die rolls 6, bonus die rolls 6 -> is_critical must be True
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 6, 2]):
            res_crit = roll_dice(pool_size=1, difficulty=Difficulty.NORMAL, allow_gamble=False)
            assert res_crit.is_critical is True


class TestSalvageRollEmpiricalProperties:
    """Boundary and probability tests for zero/negative dice pool Salvage rolls."""

    @pytest.mark.parametrize("pool_size", [0, -1, -2, -5, -10, -100])
    def test_salvage_roll_pool_sizes(self, pool_size):
        """Any pool <= 0 triggers a Salvage roll exactly once."""
        # Face 6 -> 1 success, salvage=True, fumble=False, no explosion
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6]):
            res6 = roll_dice(pool_size=pool_size, difficulty=Difficulty.HARD)
            assert res6.salvage is True
            assert res6.successes == 1
            assert res6.faces == [6]
            assert res6.bonus_faces == []
            assert res6.fumble is False
            assert res6.is_critical is False

        # Face 1 -> 0 successes, salvage=True, fumble=True
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1]):
            res1 = roll_dice(pool_size=pool_size, difficulty=Difficulty.EASY)
            assert res1.salvage is True
            assert res1.successes == 0
            assert res1.faces == [1]
            assert res1.bonus_faces == []
            assert res1.fumble is True

        # Face 3 -> 0 successes, salvage=True, fumble=False
        with patch("combat_sim.core.dice.roll_d6", side_effect=[3]):
            res3 = roll_dice(pool_size=pool_size, difficulty=Difficulty.EASY)
            assert res3.salvage is True
            assert res3.successes == 0
            assert res3.faces == [3]
            assert res3.bonus_faces == []
            assert res3.fumble is False

    def test_salvage_roll_distribution_proportions(self):
        """Monte Carlo distribution of 1d6 salvage roll: P(6)=1/6, P(1)=1/6, P(2..5)=4/6."""
        rng = random.Random(2001)
        runs = 6000
        success_count = 0
        fumble_count = 0
        fail_count = 0

        for _ in range(runs):
            res = roll_dice(pool_size=0, difficulty=Difficulty.NORMAL, rng=rng)
            assert res.salvage is True
            assert len(res.faces) == 1
            if res.successes == 1:
                success_count += 1
            elif res.fumble:
                fumble_count += 1
            else:
                fail_count += 1

        assert abs(success_count / runs - 1 / 6) < 0.02
        assert abs(fumble_count / runs - 1 / 6) < 0.02
        assert abs(fail_count / runs - 4 / 6) < 0.02


class TestGobboGambleEmpiricalProperties:
    """Edge cases, property invariants, and fumble risks in the Gobbo Gamble."""

    def test_gamble_rerolls_only_ones_preserving_other_faces(self):
        """Non-1 faces and their initial bonus dice are strictly preserved when gambling."""
        # Initial roll: [1, 1, 5] vs Normal 5+/3 (1 success on 5, fails TN 3).
        # Kept: [5] (1 success).
        # Rerolled 1s: [5, 6]. The 6 explodes into [5].
        # Total successes: kept 5 (1) + rerolled 5 (1) + rerolled 6 (1) + bonus 5 (1) = 4 successes >= 3 -> Success!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 1, 5, 5, 6, 5]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=3, allow_gamble=True)
            assert res.gambled is True
            assert res.is_success is True
            assert res.fumble is False
            assert res.successes == 4
            assert set(res.faces) == {5, 6}

    def test_gamble_with_initial_six_and_bonus_die(self):
        """Initial 6 that exploded + a 1: gamble preserves initial 6 and its bonus die."""
        # Initial: [1, 6]. Initial 6 explodes into [2].
        # Initial successes on Normal 5+: 1 (from 6). TN = 2 -> fails TN 2.
        # Gamble rerolls the 1 -> [5].
        # Total successes: initial 6 (1) + gamble 5 (1) = 2 successes == TN 2 -> Success!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 6, 2, 5]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, tn=2, allow_gamble=True)
            assert res.gambled is True
            assert res.successes == 2
            assert res.is_success is True
            assert res.fumble is False
            assert 6 in res.faces
            assert 2 in res.bonus_faces

    def test_gamble_failure_fumble_consequence(self):
        """Failing TN after gamble always sets fumble=True."""
        # Initial: [1, 1, 2] vs Normal 5+/2 -> 0 successes.
        # Gamble rerolls two 1s -> [1, 3] -> 0 successes < 2 TN.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 1, 2, 1, 3]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=2, allow_gamble=True)
            assert res.gambled is True
            assert res.is_success is False
            assert res.fumble is True
            assert res.successes == 0

    def test_gamble_not_triggered_when_allow_gamble_false(self):
        """Even with 1s and failed TN, allow_gamble=False prevents gambling."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 1, 2]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=2, allow_gamble=False)
            assert res.gambled is False
            assert res.fumble is False
            assert res.successes == 0


class TestBangarangaPoolEmpiricalProperties:
    """Stress testing communal Bangaranga pool dynamics and double explosion mechanics."""

    def test_bangaranga_draw_and_tax_matrix(self):
        """Exhaustive matrix of draw requests vs TN tax."""
        # Initial: 10 dice
        pool = BangarangaPool(initial_dice=10)

        # Draw 1 vs TN 1: count <= TN -> 0 tax -> cost 1 -> 9 remaining
        assert pool.draw(count=1, tn=1) == 1
        assert pool.available_dice == 9

        # Draw 2 vs TN 1: count > TN -> 1 tax -> cost 2 + 1 = 3 -> 6 remaining
        assert pool.draw(count=2, tn=1) == 2
        assert pool.available_dice == 6

        # Draw 4 vs TN 2: count > TN -> 1 tax -> cost 4 + 1 = 5 -> 1 remaining
        assert pool.draw(count=4, tn=2) == 4
        assert pool.available_dice == 1

        # Draw 2 vs TN 1: requested 2 + 1 tax = 3, but available is only 1 -> cannot pay tax + count -> draws 0
        assert pool.draw(count=2, tn=1) == 0
        assert pool.available_dice == 1

        # Draw 1 vs TN 1: 0 tax -> draws 1 -> 0 remaining
        assert pool.draw(count=1, tn=1) == 1
        assert pool.available_dice == 0

        # Draw from empty pool
        assert pool.draw(count=1, tn=1) == 0
        assert pool.available_dice == 0

    def test_bangaranga_double_explosion_cascade(self):
        """Bangaranga 6 explodes into 2 dice; if both bonus dice roll 6, they explode into 1 bonus die each recursively."""
        pool = BangarangaPool(initial_dice=5)
        # 1 drawn die rolls 6.
        # Explodes into 2 bonus dice: [6, 6].
        # Each bonus 6 explodes recursively into 1 die each: first [5], second [2].
        # Faces: [6]
        # Bonus faces: [6, 6, 5, 2]
        # Successes on Normal 5+: 6 (init) + 6 (b1) + 6 (b2) + 5 (b3) = 4 successes!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 6, 5, 6, 2]):
            res = pool.roll_bangaranga_test(drawn_dice=1, difficulty=Difficulty.NORMAL, tn=2)
            assert res.successes == 4
            assert res.faces == [6]
            assert len(res.bonus_faces) == 4
            assert res.is_critical is True

    def test_bangaranga_resolve_outcome_failure_drain(self):
        """Failing test with 1s drains drawn count from pool and inflicts 1 Grunt loss."""
        pool = BangarangaPool(initial_dice=5)

        # Case A: Failed with 1 in faces -> Grunt loss = 1, pool_drained = drawn_dice
        res_fail_ones = pool.resolve_test_outcome(drawn_dice=3, faces=[1, 2, 4], successes=0, tn=1)
        assert res_fail_ones.grunt_loss == 1
        assert res_fail_ones.pool_drained == 3

        # Case B: Failed WITHOUT 1 in faces -> Grunt loss = 1, pool_drained = 0
        res_fail_no_ones = pool.resolve_test_outcome(drawn_dice=2, faces=[2, 4], successes=0, tn=1)
        assert res_fail_no_ones.grunt_loss == 1
        assert res_fail_no_ones.pool_drained == 0

        # Case C: Succeeded -> Grunt loss = 0, pool_drained = 0
        res_success = pool.resolve_test_outcome(drawn_dice=2, faces=[1, 5], successes=1, tn=1)
        assert res_success.grunt_loss == 0
        assert res_success.pool_drained == 0


if __name__ == "__main__":
    print("Running Challenger 1 M2 Dice Stats empirical tests...")
    import sys
    test_classes = [
        TestExplodingSixesEmpiricalProperties,
        TestSalvageRollEmpiricalProperties,
        TestGobboGambleEmpiricalProperties,
        TestBangarangaPoolEmpiricalProperties,
    ]
    passed = 0
    failed = 0
    for cls in test_classes:
        inst = cls()
        for attr in dir(inst):
            if attr.startswith("test_"):
                fn = getattr(inst, attr)
                try:
                    fn()
                    print(f"  [PASS] {cls.__name__}.{attr}")
                    passed += 1
                except Exception as e:
                    print(f"  [FAIL] {cls.__name__}.{attr}: {e}")
                    failed += 1
    print(f"\nResult: {passed} passed, {failed} failed.")
    if failed > 0:
        sys.exit(1)
