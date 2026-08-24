"""
Tier 2 Test Suite: Boss Quirks, Talents, and Modular Twists.
Validates Meat Shield damage redirection, Ankle Bite Dodge counter-attack (+1 success),
Push Luck non-1s reroll with Grunt cost, and modular twist modifiers.
"""

from __future__ import annotations

from unittest.mock import MagicMock
import pytest

from combat_sim.domain.quirks import (
    MeatShield,
    AnkleBite,
    PushLuck,
    SecondWind,
    OpportunityStrike,
    SwallowLoot,
    Butcher,
    TwistModifier,
)


class DummyBoss:
    """Test stub representing GoblinBoss state for quirk unit tests."""
    def __init__(self, grunt=2, grit=4, zone_id="Z1", size=1, saved_reactions=0, actions_left=3):
        self.name = "Boss Fizzle"
        self.grunt = grunt
        self.grit = grit
        self.zone_id = zone_id
        self.size = size
        self.saved_reactions = saved_reactions
        self.actions_left = actions_left
        self.is_alive = True


class DummyMob:
    """Test stub representing PlayerMob state for quirk unit tests."""
    def __init__(self, name="Grum Runts", zone_id="Z1", is_alive=True, size=3):
        self.name = name
        self.zone_id = zone_id
        self.is_alive = is_alive
        self.size = size


class DummyEnemy:
    """Test stub representing an enemy entity."""
    def __init__(self, name="Footpad", zone_id="Z1", size=1, defence_tn=1):
        self.name = name
        self.zone_id = zone_id
        self.size = size
        self.defence_tn = defence_tn
        self.is_alive = True


class TestMeatShieldQuirk:
    """Test Meat Shield damage redirection to allied Mob in Zone."""

    def test_meat_shield_triggers_and_redirects(self):
        """Meat Shield redirects damage to allied Mob in same zone and spends 1 Grunt."""
        boss = DummyBoss(grunt=2, zone_id="Z1")
        mob = DummyMob(name="Boyz", zone_id="Z1", is_alive=True)
        quirk = MeatShield()

        context = {"allied_mob": mob, "use_grunt": True}
        assert quirk.can_trigger(boss, context) is True

        res = quirk.apply(boss, context)
        assert res["success"] is True
        assert res["redirected_to"] == "Boyz"
        assert res["resource_spent"] == "grunt"
        assert boss.grunt == 1  # 2 - 1 = 1 Grunt remaining

    def test_meat_shield_spends_saved_reaction_if_no_grunt(self):
        """Meat Shield can spend saved reaction if Grunt is 0."""
        boss = DummyBoss(grunt=0, saved_reactions=1, actions_left=0, zone_id="Z1")
        mob = DummyMob(zone_id="Z1", is_alive=True)
        quirk = MeatShield()

        context = {"allied_mob": mob, "use_grunt": False}
        assert quirk.can_trigger(boss, context) is True

        res = quirk.apply(boss, context)
        assert res["resource_spent"] == "saved_reaction"
        assert boss.saved_reactions == 0

    def test_meat_shield_cannot_trigger_without_mob_in_zone(self):
        """Meat Shield fails to trigger if no allied Mob is in the same Zone."""
        boss = DummyBoss(grunt=2, zone_id="Z1")
        mob_other_zone = DummyMob(zone_id="Z2", is_alive=True)
        quirk = MeatShield()

        context = {"allied_mob": mob_other_zone}
        assert quirk.can_trigger(boss, context) is False

    def test_meat_shield_cannot_trigger_with_dead_mob(self):
        """Meat Shield fails to trigger if Mob in Zone is dead."""
        boss = DummyBoss(grunt=2, zone_id="Z1")
        dead_mob = DummyMob(zone_id="Z1", is_alive=False)
        quirk = MeatShield()

        context = {"allied_mob": dead_mob}
        assert quirk.can_trigger(boss, context) is False


class TestAnkleBiteQuirk:
    """Test Ankle Bite free melee counter-attack on clean Dodge."""

    def test_ankle_bite_triggers_on_clean_dodge_in_melee(self):
        """Clean Dodge vs melee attacker in same zone triggers Ankle Bite with +1 Success."""
        boss = DummyBoss(zone_id="Z1")
        attacker = DummyEnemy(name="Guard", zone_id="Z1")
        quirk = AnkleBite()

        context = {
            "is_clean_dodge": True,
            "is_melee": True,
            "attacker": attacker,
        }
        assert quirk.can_trigger(boss, context) is True

        res = quirk.apply(boss, context)
        assert res["free_counter_attack"] is True
        assert res["bonus_successes"] == 1
        assert res["target"] == attacker

    def test_ankle_bite_does_not_trigger_on_failed_dodge(self):
        """Failed Dodge does not trigger Ankle Bite."""
        boss = DummyBoss(zone_id="Z1")
        attacker = DummyEnemy(zone_id="Z1")
        quirk = AnkleBite()

        context = {"is_clean_dodge": False, "is_melee": True, "attacker": attacker}
        assert quirk.can_trigger(boss, context) is False

    def test_ankle_bite_does_not_trigger_on_ranged_attack(self):
        """Clean Dodge against ranged attack across zones does not trigger Ankle Bite."""
        boss = DummyBoss(zone_id="Z1")
        ranged_attacker = DummyEnemy(zone_id="Z2")
        quirk = AnkleBite()

        context = {
            "is_clean_dodge": True,
            "is_melee": False,
            "attacker": ranged_attacker,
        }
        assert quirk.can_trigger(boss, context) is False


class TestPushLuckQuirk:
    """Test Push Luck / Second Wind reroll of non-1 dice."""

    def test_push_luck_rerolls_non_ones(self):
        """Push Luck spends 1 Grunt and rerolls non-1 dice, leaving 1s locked."""
        boss = DummyBoss(grunt=2)
        quirk = PushLuck()

        # Rolled [1, 3, 4] -> non-1s are indices 1 and 2
        context = {"faces": [1, 3, 4]}
        assert quirk.can_trigger(boss, context) is True

        res = quirk.apply(boss, context)
        assert res["reroll_indices"] == [1, 2]
        assert res["locked_indices"] == [0]
        assert res["grunt_spent"] == 1
        assert boss.grunt == 1

    def test_push_luck_cannot_trigger_at_zero_grunt(self):
        """Push Luck cannot trigger if Boss has 0 Grunt."""
        boss = DummyBoss(grunt=0)
        quirk = PushLuck()
        context = {"faces": [2, 3, 4]}
        assert quirk.can_trigger(boss, context) is False

    def test_second_wind_alias(self):
        """Second Wind is identical in behavior to Push Luck."""
        boss = DummyBoss(grunt=1)
        quirk = SecondWind()
        assert quirk.name == "Second Wind"
        assert quirk.grunt_cost == 1


class TestModularTwists:
    """Test modular Twist modifiers (Spiteful, Loud, Efficient, Reflexive)."""

    def test_efficient_twist_reduces_grunt_cost(self):
        """Efficient twist reduces quirk Grunt cost by 1 (min 0)."""
        quirk = MeatShield()
        assert quirk.grunt_cost == 1
        assert quirk.get_effective_grunt_cost() == 1

        quirk.add_twist(TwistModifier.efficient())
        assert quirk.get_effective_grunt_cost() == 0

    def test_reflexive_twist_converts_action(self):
        """Reflexive twist makes action cost free."""
        quirk = MeatShield()
        quirk.action_cost = 1
        assert quirk.is_free_action() is False

        quirk.add_twist(TwistModifier.reflexive())
        assert quirk.is_free_action() is True

    def test_other_passive_quirks(self):
        """Verify SwallowLoot, OpportunityStrike, and Butcher passive behaviors."""
        boss = DummyBoss(size=2)
        small_enemy = DummyEnemy(size=1)
        large_enemy = DummyEnemy(size=2)

        butcher = Butcher()
        assert butcher.can_trigger(boss, {"target": small_enemy}) is True
        assert butcher.can_trigger(boss, {"target": large_enemy}) is False
        assert butcher.apply(boss)["boon_dice"] == 1

        swallow = SwallowLoot()
        assert swallow.apply(boss)["bonus_unencumbered_bulk"] == 2

        slippery = OpportunityStrike()
        assert slippery.apply(boss)["ignores_opportunity_attacks"] is True
