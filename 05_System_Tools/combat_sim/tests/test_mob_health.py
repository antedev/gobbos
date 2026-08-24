"""
Tier 1/2 Test Suite: Mob Health Dice Mechanics and Swarm Dynamics.
Validates symmetrical dice-HP tracking, single-target damage decrement & spillover,
die removal when < 1, AoE/Cleave full-pool simultaneous damage,
enemy mob attack damage scaling, and cross-gang in-fighting.
"""

from __future__ import annotations

import pytest

from combat_sim.domain.entities import PlayerMob, EnemyMob, GoblinBoss


class TestMobHealthBasics:
    """Test symmetrical Dice-HP initialization and state tracking."""

    def test_mob_dice_hp_initialization(self):
        """Mob of Size X initializes with X d6s at face 6."""
        mob = PlayerMob(id="M1", name="Grum Runts", zone_id="Z1", size=3)
        assert mob.size == 3
        assert mob.health_dice == [6, 6, 6]
        assert mob.is_alive is True

    def test_mob_size_tracking(self):
        """Size is dynamically synchronized with health dice count."""
        mob = PlayerMob(id="M1", name="Grum Runts", zone_id="Z1", health_dice=[6, 4])
        assert mob.size == 2
        assert mob.is_alive is True


class TestSingleTargetDamageAndSpillover:
    """Test single-target active die reduction, spillover, and die removal."""

    def test_single_target_damage_no_spillover(self):
        """Damage smaller than active die face reduces only the active die."""
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[6, 6, 6])
        dealt = mob.take_single_target_damage(2)
        assert dealt == 2
        assert mob.health_dice == [4, 6, 6]
        assert mob.size == 3
        assert mob.is_alive is True

    def test_mob_single_target_damage_and_spillover(self):
        """Damage exceeding active die eliminates active die and spills over to next."""
        # [2, 6, 6] taking 4 damage:
        # Active die (2) takes 2 dmg -> eliminated.
        # Remainder (2 dmg) reduces next die (6) -> 4.
        # Result: [4, 6], Size 2.
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[2, 6, 6])
        dealt = mob.take_single_target_damage(4)
        assert dealt == 4
        assert mob.health_dice == [4, 6]
        assert mob.size == 2
        assert mob.is_alive is True

    def test_mob_die_removal_when_zero(self):
        """When all dice drop to 0, Mob is wiped out (size=0, is_alive=False)."""
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[2, 3])
        dealt = mob.take_single_target_damage(5)
        assert dealt == 5
        assert mob.health_dice == []
        assert mob.size == 0
        assert mob.is_alive is False

    def test_excess_damage_beyond_total_health(self):
        """Excess damage beyond mob total health does not crash or corrupt state."""
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[2, 2])
        dealt = mob.take_single_target_damage(10)
        assert dealt == 4  # Total HP was 4
        assert mob.health_dice == []
        assert mob.size == 0
        assert mob.is_alive is False


class TestAoEMultiDieDamage:
    """Test AoE and Cleave simultaneous damage across all health dice."""

    def test_mob_aoe_damage_simultaneous_all_dice(self):
        """AoE damage applies flat damage to EVERY die in the health pool simultaneously."""
        # Size 4 Mob with [6, 6, 6, 6] taking 3 AoE damage:
        # All 4 dice become 3 -> [3, 3, 3, 3]. Total HP lost = 12!
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[6, 6, 6, 6])
        dealt = mob.take_aoe_damage(3)
        assert dealt == 12
        assert mob.health_dice == [3, 3, 3, 3]
        assert mob.size == 4
        assert mob.is_alive is True

    def test_aoe_damage_partial_die_elimination(self):
        """AoE damage eliminates dice that drop <= 0 while reducing surviving dice."""
        # [2, 3, 5] taking 3 AoE damage:
        # Die 1 (2 - 3 <= 0) -> removed
        # Die 2 (3 - 3 <= 0) -> removed
        # Die 3 (5 - 3 = 2) -> survives as 2
        # Result: [2], Size 1
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[2, 3, 5])
        dealt = mob.take_aoe_damage(3)
        assert dealt == 8  # Initial HP was 10, final HP is 2 -> 8 lost
        assert mob.health_dice == [2]
        assert mob.size == 1
        assert mob.is_alive is True

    def test_aoe_damage_complete_wipeout(self):
        """Massive AoE damage wipes all dice simultaneously."""
        mob = PlayerMob(id="M1", name="Runts", zone_id="Z1", health_dice=[3, 4, 2])
        dealt = mob.take_aoe_damage(5)
        assert dealt == 9
        assert mob.health_dice == []
        assert mob.size == 0
        assert mob.is_alive is False


class TestEnemyMobDamageScaling:
    """Test Enemy Mob attack damage scaling based on surviving Size."""

    def test_enemy_mob_attack_damage_scaling(self):
        """Enemy Mob damage = Base Damage + (Current Size - 1)."""
        # Base damage = 1
        mob = EnemyMob(id="EM1", name="Robber Gang", zone_id="Z1", size=3, base_damage=1)
        assert mob.get_mob_damage() == 3  # 1 + (3 - 1) = 3

        # Take damage reducing Size to 2
        mob.take_single_target_damage(6)
        assert mob.size == 2
        assert mob.get_mob_damage() == 2  # 1 + (2 - 1) = 2

        # Take damage reducing Size to 1
        mob.take_single_target_damage(6)
        assert mob.size == 1
        assert mob.get_mob_damage() == 1  # 1 + (1 - 1) = 1


class TestCrossGangInFighting:
    """Test Cross-Gang Super-Mob self-inflicted damage on 1s."""

    def test_cross_gang_infighting_damage_on_ones(self):
        """Cross-gang mob suffers 1 internal damage for every 1 rolled on dice tests."""
        mob = PlayerMob(id="M1", name="Cross-Gang Mob", zone_id="Z1", health_dice=[6, 6, 6, 6, 6])
        rolled_faces = [1, 1, 5, 5, 6]  # Two 1s rolled

        ones_count = rolled_faces.count(1)
        assert ones_count == 2

        # 2 self-damage applied
        dealt = mob.take_single_target_damage(ones_count)
        assert dealt == 2
        assert mob.health_dice == [4, 6, 6, 6, 6]
