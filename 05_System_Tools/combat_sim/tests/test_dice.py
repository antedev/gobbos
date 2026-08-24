"""
Tier 1 Test Suite: Core Mechanics & Dice Pool System.
Validates exploding 6s, critical double explosions, salvage rolls,
Gobbo Gamble 1s rerolls & fumbles, Bangaranga pool dynamics, and Clatter rolls.
"""

from __future__ import annotations

import random
from unittest.mock import patch
import pytest

from combat_sim.core.types import Difficulty
from combat_sim.core.dice import (
    DiceResult,
    ClatterResult,
    BangarangaPool,
    roll_dice,
    resolve_clatter,
)


class TestDicePoolBasics:
    """Test core d6 dice pool resolutions across difficulties."""

    def test_dice_pool_difficulties(self):
        """Verify Easy 4+, Normal 5+, and Hard 6 threshold evaluation."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[4, 5, 3]):
            res_easy = roll_dice(pool_size=3, difficulty=Difficulty.EASY, allow_gamble=False)
            assert res_easy.successes == 2  # 4 and 5 meet Easy 4+
            assert not res_easy.fumble
            assert not res_easy.salvage

        with patch("combat_sim.core.dice.roll_d6", side_effect=[4, 5, 3]):
            res_normal = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, allow_gamble=False)
            assert res_normal.successes == 1  # only 5 meets Normal 5+
            assert not res_normal.fumble

        with patch("combat_sim.core.dice.roll_d6", side_effect=[4, 5, 3]):
            res_hard = roll_dice(pool_size=3, difficulty=Difficulty.HARD, allow_gamble=False)
            assert res_hard.successes == 0  # neither 4 nor 5 meets Hard 6
            assert not res_hard.fumble

    def test_dice_pool_tn_successes(self):
        """Verify target number (TN) of successes evaluation."""
        # 3 dice rolling [5, 5, 2] -> 2 successes vs Normal 5+
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=2, allow_gamble=False)
            assert res.successes == 2
            assert res.is_success  # Met TN 2


class TestExplodingSixes:
    """Test recursive exploding 6s and critical double explosions."""

    def test_exploding_sixes_recursive(self):
        """Verify that rolling a 6 adds a success and immediately rolls a bonus d6 recursively."""
        # Initial roll: [6, 2]. The 6 explodes into [6]. That 6 explodes into [5].
        # Total faces: initial [6, 2], bonus [6, 5]
        # Successes on Normal 5+: 6 (init), 6 (bonus), 5 (bonus) = 3 successes.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 2, 6, 5]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, allow_gamble=False)
            assert res.successes == 3
            assert 6 in res.faces
            assert 6 in res.bonus_faces
            assert 5 in res.bonus_faces
            assert res.is_critical is True  # 6 followed by 6 on bonus die

    def test_single_six_no_critical(self):
        """Verify a single 6 exploding into a non-6 gives +1 bonus roll without critical."""
        # Initial roll: [6, 3]. Bonus roll: [2].
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 3, 2]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, allow_gamble=False)
            assert res.successes == 1  # only the initial 6
            assert res.bonus_faces == [2]
            assert res.is_critical is False

    def test_exploding_sixes_distribution(self):
        """Stochastic test verifying positive explosion bias over large sample."""
        random.seed(42)
        total_successes = 0
        runs = 2000
        for _ in range(runs):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, allow_gamble=False)
            total_successes += res.successes
        avg_succ = total_successes / runs
        # Expected on 3d6 at 5+ with explosions: 3 * (1/3) / (1 - 1/6) = 1.2
        assert 1.05 < avg_succ < 1.35


class TestSalvageRoll:
    """Test zero dice pool Salvage roll rules."""

    def test_salvage_roll_success_on_six(self):
        """When pool <= 0d6, 1d6 salvage roll on 6 grants exactly 1 success and does NOT explode."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6]):
            res = roll_dice(pool_size=0, difficulty=Difficulty.NORMAL, is_salvage=True)
            assert res.salvage is True
            assert res.successes == 1
            assert res.bonus_faces == []  # Salvage 6 does NOT explode
            assert res.fumble is False

    def test_salvage_roll_failure_on_two_to_five(self):
        """Salvage roll on 2-5 is a normal failure (no fumble, 0 successes)."""
        for face in [2, 3, 4, 5]:
            with patch("combat_sim.core.dice.roll_d6", side_effect=[face]):
                res = roll_dice(pool_size=-2, difficulty=Difficulty.NORMAL)
                assert res.salvage is True
                assert res.successes == 0
                assert res.fumble is False

    def test_salvage_roll_fumble_on_one(self):
        """Salvage roll on 1 causes a Fumble."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1]):
            res = roll_dice(pool_size=-1, difficulty=Difficulty.NORMAL)
            assert res.salvage is True
            assert res.successes == 0
            assert res.fumble is True


class TestGobboGamble:
    """Test Gobbo Gamble (pushing 1s) on failed tests."""

    def test_gobbo_gamble_reroll_ones_success(self):
        """Failed test with 1s rerolls only the 1s; success clears fumble risk."""
        # Initial: [1, 1, 4] vs Normal 5+/2 -> 0 successes (fails TN 2).
        # Gamble rerolls the two 1s -> [5, 6]. The 6 explodes into [3].
        # Total successes: 5, 6 = 2 successes -> Success!
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 1, 4, 5, 6, 3]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=2, allow_gamble=True)
            assert res.gambled is True
            assert res.successes == 2
            assert res.is_success is True
            assert res.fumble is False

    def test_gobbo_gamble_fumble_penalty(self):
        """Failed gamble that still does not meet TN results in a Fumble."""
        # Initial: [1, 3] vs Normal 5+/1 -> 0 successes.
        # Gamble rerolls the 1 -> [2]. Total successes = 0.
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 3, 2]):
            res = roll_dice(pool_size=2, difficulty=Difficulty.NORMAL, tn=1, allow_gamble=True)
            assert res.gambled is True
            assert res.successes == 0
            assert res.is_success is False
            assert res.fumble is True

    def test_gamble_not_triggered_when_test_already_succeeded(self):
        """If initial roll already meets TN, Gobbo Gamble is not triggered even if 1s are present."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 5, 5]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=2, allow_gamble=True)
            assert res.gambled is False
            assert res.successes == 2
            assert res.is_success is True
            assert res.fumble is False

    def test_gamble_not_allowed_without_ones(self):
        """If test fails but contains no 1s, gamble cannot be triggered."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[2, 3, 4]):
            res = roll_dice(pool_size=3, difficulty=Difficulty.NORMAL, tn=1, allow_gamble=True)
            assert res.gambled is False
            assert res.successes == 0
            assert res.fumble is False


class TestBangarangaPool:
    """Test Bangaranga communal dice pool mechanics."""

    def test_bangaranga_pool_tax_and_draw(self):
        """Drawing more dice than TN imposes a 1-die discard tax."""
        pool = BangarangaPool(initial_dice=5)
        # Test requires TN 1, player draws 2 dice (drawn > TN -> tax = 1 die)
        drawn = pool.draw(count=2, tn=1)
        assert drawn == 2
        # Remaining: 5 - (2 drawn + 1 tax) = 2
        assert pool.available_dice == 2

    def test_bangaranga_pool_draw_without_tax(self):
        """Drawing <= TN incurs zero tax."""
        pool = BangarangaPool(initial_dice=5)
        drawn = pool.draw(count=2, tn=2)
        assert drawn == 2
        assert pool.available_dice == 3

    def test_bangaranga_double_explosion(self):
        """6s rolled on Bangaranga dice explode TWICE (generate 2 bonus dice)."""
        pool = BangarangaPool(initial_dice=5)
        # Roll 1 Bangaranga die: rolls 6.
        # Explodes twice into [5, 4].
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6, 5, 4]):
            res = pool.roll_bangaranga_test(drawn_dice=1, difficulty=Difficulty.NORMAL)
            assert res.successes == 2  # 6 (initial) + 5 (bonus)
            assert len(res.bonus_faces) == 2

    def test_bangaranga_drain_on_fail(self):
        """Failing a test with Bangaranga dice and 1s drains drawn dice from the communal pool."""
        pool = BangarangaPool(initial_dice=5)
        drawn = pool.draw(count=2, tn=1)  # 5 - (2+1) = 2 remaining
        # Roll yields [1, 2] -> failure with 1
        with patch("combat_sim.core.dice.roll_d6", side_effect=[1, 2]):
            res = pool.resolve_test_outcome(drawn_dice=drawn, faces=[1, 2], successes=0, tn=1)
            assert res.grunt_loss == 1
            assert res.pool_drained == 2


class TestClatterRoll:
    """Test Clatter Roll active evasion vs passive armor mitigation."""

    def test_clatter_clean_dodge(self):
        """Active stat successes >= Threat TN completely evades attack (0 damage taken)."""
        # Threat TN = 2, Threat Damage = 3
        # Slink 3d6 rolls [5, 5, 2] (2 successes >= 2 TN)
        # Armor 2d6 rolls [5, 6] (irrelevant because evaded)
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2, 5, 6]):
            res = resolve_clatter(
                threat_tn=2,
                stat_dice=3,
                difficulty=Difficulty.NORMAL,
                armor_dice=2,
                incoming_damage=3,
            )
            assert res.evaded is True
            assert res.stat_successes == 2
            assert res.damage_taken == 0

    def test_clatter_mitigation_on_failed_dodge(self):
        """Failed active stat evasion falls back to armor dice (5+ reduces damage by 1)."""
        # Threat TN = 2, Threat Damage = 3
        # Slink 2d6 rolls [5, 2] (1 success < 2 TN -> Evasion fails)
        # Armor 2d6 rolls [5, 6] (2 successes on 5+ -> mitigates 2 damage)
        # Damage taken = 3 - 2 = 1
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 2, 5, 6]):
            res = resolve_clatter(
                threat_tn=2,
                stat_dice=2,
                difficulty=Difficulty.NORMAL,
                armor_dice=2,
                incoming_damage=3,
            )
            assert res.evaded is False
            assert res.stat_successes == 1
            assert res.armor_successes == 2
            assert res.damage_taken == 1

    def test_clatter_zero_saved_actions(self):
        """With 0 saved actions, active stat dice are 0; only passive armor dice roll."""
        # Threat TN = 1, Threat Damage = 2
        # Stat dice = 0 (cannot roll)
        # Armor 3d6 rolls [5, 5, 2] (2 successes on 5+ -> mitigates 2 damage)
        # Damage taken = max(0, 2 - 2) = 0
        with patch("combat_sim.core.dice.roll_d6", side_effect=[5, 5, 2]):
            res = resolve_clatter(
                threat_tn=1,
                stat_dice=0,
                difficulty=Difficulty.NORMAL,
                armor_dice=3,
                incoming_damage=2,
            )
            assert res.evaded is False
            assert res.stat_successes == 0
            assert res.armor_successes == 2
            assert res.damage_taken == 0


class TestAdversarialDiceCases:
    """Adversarial and extreme edge case testing."""

    def test_adversarial_negative_and_zero_pool(self):
        """Negative pools correctly trigger salvage roll without crash."""
        with patch("combat_sim.core.dice.roll_d6", side_effect=[6]):
            res = roll_dice(pool_size=-10, difficulty=Difficulty.NORMAL)
            assert res.salvage is True
            assert res.successes == 1

    def test_adversarial_large_pool(self):
        """Large dice pool rolls without stack overflow or explosion loops."""
        random.seed(1234)
        res = roll_dice(pool_size=50, difficulty=Difficulty.NORMAL, allow_gamble=False)
        assert res.successes >= 0
        assert len(res.faces) == 50
