"""
Tier 2 Test Suite: Equipment, Weapons, Armor, Shields, and Consumables.
Validates weapon handedness, Impact Size modifiers on Stagger, Shield Parry enablement,
Armor Dice mitigation, Slink Bane penalties, Ablative Gear Sacrifice, and Explosives.
"""

from __future__ import annotations

import pytest

from combat_sim.core.types import (
    Difficulty,
    Tag,
    WeaponHandedness,
    WeaponTrait,
)
from combat_sim.domain.equipment import (
    Weapon,
    Armor,
    Shield,
    Consumable,
    create_bone_shiv,
    create_notched_sword,
    create_spiked_mace,
    create_heavy_greataxe,
    create_dwarven_great_hammer,
    create_halberd,
    create_sling,
    create_shortbow,
    create_light_crossbow,
    create_military_longbow,
    create_heavy_arbalest,
    create_repeating_crossbow,
    create_light_armor,
    create_medium_armor,
    create_heavy_armor,
    create_runed_carapace,
    create_pot_lid_shield,
    create_tower_pavise,
    create_godstone_aegis,
    create_spark_bomb,
    create_fire_flask,
    create_smoke_pot,
    create_powder_keg,
    create_mortar_shell,
    create_sol_quartz,
)


class TestMeleeWeaponsAndImpactSize:
    """Test melee weapon properties, handedness, and Impact Size calculation."""

    def test_light_melee_weapon(self):
        """Light weapon: 1H, Bulk 1, Impact Modifier 0, Concealable."""
        shiv = create_bone_shiv()
        assert shiv.handedness == WeaponHandedness.ONE_HAND
        assert shiv.bulk == 1
        assert shiv.impact_size_modifier == 0
        assert shiv.has_trait(WeaponTrait.CONCEALABLE)
        assert shiv.has_trait(WeaponTrait.PIERCING)
        assert shiv.get_effective_impact_size(wielder_size=1) == 1

    def test_medium_melee_weapon(self):
        """Medium weapon: 1H, Bulk 2, Impact Modifier 0."""
        sword = create_notched_sword()
        assert sword.handedness == WeaponHandedness.ONE_HAND
        assert sword.bulk == 2
        assert sword.impact_size_modifier == 0
        assert sword.has_trait(WeaponTrait.CUTTING)
        assert sword.get_effective_impact_size(wielder_size=1) == 1

    def test_heavy_melee_weapon_impact_size(self):
        """Heavy weapon: 2H, Bulk 3, +1 Impact Size modifier."""
        axe = create_heavy_greataxe()
        assert axe.handedness == WeaponHandedness.TWO_HAND
        assert axe.bulk == 3
        assert axe.impact_size_modifier == 1
        assert axe.has_trait(WeaponTrait.HEAVY)
        assert axe.has_trait(WeaponTrait.CLEAVE)
        # Size 1 Boss wielding Heavy weapon has Impact Size 2
        assert axe.get_effective_impact_size(wielder_size=1) == 2
        # Size 3 Mob wielding Heavy weapon has Impact Size 4
        assert axe.get_effective_impact_size(wielder_size=3) == 4

    def test_crushing_heavy_weapon_impact_size(self):
        """Crushing weapon: 2H, Bulk 3, +2 Impact Size modifier."""
        hammer = create_dwarven_great_hammer()
        assert hammer.handedness == WeaponHandedness.TWO_HAND
        assert hammer.impact_size_modifier == 2
        assert hammer.has_trait(WeaponTrait.CRUSHING)
        assert hammer.has_trait(WeaponTrait.BASHING)
        # Size 1 Boss wielding Crushing weapon has Impact Size 3 (can stagger Size 3 monsters)
        assert hammer.get_effective_impact_size(wielder_size=1) == 3

    def test_stagger_calculation_impact_vs_target_size(self):
        """Impact Size >= Target Size inflicts Stagger on partial hits."""
        axe = create_heavy_greataxe()  # Impact modifier +1 -> Impact Size 2
        target_size_2 = 2
        assert axe.get_effective_impact_size(wielder_size=1) >= target_size_2  # Can stagger

    def test_stagger_mass_resistance_negation(self):
        """Impact Size < Target Size fails to stagger (target mass resistance)."""
        sword = create_notched_sword()  # Impact modifier 0 -> Impact Size 1
        target_size_2 = 2
        assert sword.get_effective_impact_size(wielder_size=1) < target_size_2  # Stagger ignored!


class TestRangedWeapons:
    """Test ranged weapon profiles, ranges in zones, and stat requirements."""

    def test_sling_range_and_fast_throw(self):
        """Sling: 1H, Range 1 Zone, Fast Throw."""
        sling = create_sling()
        assert sling.handedness == WeaponHandedness.ONE_HAND
        assert sling.range_zones == 1
        assert sling.has_trait(WeaponTrait.FAST_THROW)
        assert sling.is_ranged is True

    def test_shortbow_range_and_rapid_shot(self):
        """Shortbow: 2H, Range 2 Zones, Rapid Shot."""
        bow = create_shortbow()
        assert bow.handedness == WeaponHandedness.TWO_HAND
        assert bow.range_zones == 2
        assert bow.has_trait(WeaponTrait.RAPID_SHOT)

    def test_light_crossbow_stat_requirement(self):
        """Light Crossbow: 2H, Range 2 Zones, requires Brains >= 2, Armor Piercing."""
        xbow = create_light_crossbow()
        assert xbow.range_zones == 2
        assert xbow.min_brains == 2
        assert xbow.has_trait(WeaponTrait.ARMOR_PIERCING)

    def test_military_longbow_stat_requirement(self):
        """Military Longbow: 2H, Range 3 Zones, requires Tough >= 2."""
        longbow = create_military_longbow()
        assert longbow.range_zones == 3
        assert longbow.min_tough == 2

    def test_heavy_arbalest_profile(self):
        """Heavy Arbalest: 2H, Range 3 Zones, min Tough 2 & Brains 2, Heavy (+1 Impact Size)."""
        arbalest = create_heavy_arbalest()
        assert arbalest.range_zones == 3
        assert arbalest.min_tough == 2
        assert arbalest.min_brains == 2
        assert arbalest.impact_size_modifier == 1
        assert arbalest.has_trait(WeaponTrait.HEAVY)
        assert arbalest.has_trait(WeaponTrait.ARMOR_PIERCING)

    def test_repeating_crossbow_clockwork_trait(self):
        """Repeating Crossbow: Range 2 Zones, Clockwork Feed (2 attacks per action)."""
        rxbow = create_repeating_crossbow()
        assert rxbow.range_zones == 2
        assert rxbow.has_trait(WeaponTrait.CLOCKWORK)
        assert rxbow.tier == 4


class TestArmorAndShields:
    """Test armor dice scaling, Slink Bane penalties, and Shield Tough Parry unlocking."""

    def test_light_armor(self):
        """Light Armor: +1d Armor Die, 0 Slink Bane, Bulk 1."""
        armor = create_light_armor()
        assert armor.armor_dice == 1
        assert armor.slink_bane == 0
        assert armor.bulk == 1
        assert armor.cannot_swim is False

    def test_medium_armor(self):
        """Medium Armor: +2d Armor Dice, Bane 1 on Slink (-1d), Bulk 2."""
        armor = create_medium_armor()
        assert armor.armor_dice == 2
        assert armor.slink_bane == 1
        assert armor.bulk == 2

    def test_heavy_armor(self):
        """Heavy Armor: +3d Armor Dice, Bane 2 on Slink (-2d), Bulk 3, cannot swim."""
        armor = create_heavy_armor()
        assert armor.armor_dice == 3
        assert armor.slink_bane == 2
        assert armor.bulk == 3
        assert armor.cannot_swim is True

    def test_runed_carapace_masterwork_heavy_armor(self):
        """Runed Carapace (T4): +3d Armor Dice, reduced Bane 1 on Slink."""
        armor = create_runed_carapace()
        assert armor.armor_dice == 3
        assert armor.slink_bane == 1
        assert armor.tier == 4

    def test_shield_parry_enablement(self):
        """Standard Shield: +1d Armor Die, enables Tough Parry reaction, Bulk 1."""
        shield = create_pot_lid_shield()
        assert shield.armor_dice == 1
        assert shield.enables_parry is True
        assert shield.halves_movement is False

    def test_tower_pavise(self):
        """Tower Pavise: +2d Armor Dice, enables Parry, halves movement, Bulk 2."""
        shield = create_tower_pavise()
        assert shield.armor_dice == 2
        assert shield.enables_parry is True
        assert shield.halves_movement is True

    def test_godstone_aegis(self):
        """Godstone Aegis: +2d Armor Dice, enables Parry, immune to piercing, never breaks."""
        shield = create_godstone_aegis()
        assert shield.armor_dice == 2
        assert shield.immune_to_piercing is True
        assert shield.break_threshold == 0
        assert shield.roll_breaks(1) is False


class TestConsumablesAndExplosives:
    """Test Consumables, Throwables, and Area Threat Profiles."""

    def test_spark_bomb(self):
        """Spark Bomb: T1, 1 Dmg, Threat 4+/1, Blast Range 0, [Explosive], Impact Size 1."""
        bomb = create_spark_bomb()
        assert bomb.tier == 1
        assert bomb.damage == 1
        assert bomb.blast_range == 0
        assert bomb.is_explosive is True
        assert bomb.impact_size == 1
        assert bomb.threat.difficulty == Difficulty.EASY
        assert bomb.threat.threat_tn == 1
        assert bomb.threat.is_aoe is True

    def test_fire_flask_molotov(self):
        """Fire Flask: T2, 2 Dmg, Threat 5+/1, Blast Range 1, [Fire], Impact Size 2."""
        molotov = create_fire_flask()
        assert molotov.tier == 2
        assert molotov.damage == 2
        assert molotov.blast_range == 1
        assert Tag.FIRE in molotov.tags
        assert molotov.impact_size == 2
        assert molotov.threat.difficulty == Difficulty.NORMAL
        assert molotov.threat.threat_tn == 1

    def test_smoke_pot(self):
        """Smoke Pot: T2, 0 Dmg, Threat 4+/1, Blast Range 1, [Gaseous, Dark]."""
        smoke = create_smoke_pot()
        assert smoke.damage == 0
        assert Tag.GASEOUS in smoke.tags
        assert Tag.DARK in smoke.tags

    def test_powder_keg(self):
        """Powder Keg: T3, 3 Dmg, Threat 5+/2, Blast Range 1, [Explosive], Impact Size 3."""
        keg = create_powder_keg()
        assert keg.tier == 3
        assert keg.damage == 3
        assert keg.blast_range == 1
        assert keg.impact_size == 3
        assert keg.threat.difficulty == Difficulty.NORMAL
        assert keg.threat.threat_tn == 2

    def test_siege_mortar_shell(self):
        """Mortar Shell: T4, 4 Dmg, Threat 5+/3, Blast Range 2, [Explosive], Impact Size 4."""
        shell = create_mortar_shell()
        assert shell.tier == 4
        assert shell.damage == 4
        assert shell.blast_range == 2
        assert shell.impact_size == 4
        assert shell.threat.threat_tn == 3

    def test_sol_quartz_core(self):
        """Sol-Quartz Core: T5, 5 Dmg, Threat 6/3, Blast Range 3, [Explosive, Light], Impact Size 5."""
        sol = create_sol_quartz()
        assert sol.tier == 5
        assert sol.damage == 5
        assert sol.blast_range == 3
        assert sol.impact_size == 5
        assert sol.threat.difficulty == Difficulty.HARD
        assert sol.threat.threat_tn == 3


class TestEquipmentBreakRolls:
    """Test gear break thresholds on Fumble."""

    def test_tier_break_thresholds(self):
        """T1 breaks on 1-4, T2 on 1-3, T3 on 1-2, T4 on 1, T5 never."""
        t1_item = create_bone_shiv()
        assert t1_item.roll_breaks(4) is True
        assert t1_item.roll_breaks(5) is False

        t2_item = create_notched_sword()
        assert t2_item.roll_breaks(3) is True
        assert t2_item.roll_breaks(4) is False

        t3_item = create_dwarven_great_hammer()
        assert t3_item.roll_breaks(2) is True
        assert t3_item.roll_breaks(3) is False

        t4_item = create_repeating_crossbow()
        assert t4_item.roll_breaks(1) is True
        assert t4_item.roll_breaks(2) is False

        t5_item = create_godstone_aegis()
        assert t5_item.roll_breaks(1) is False
