"""
Tier 2 Test Suite: Enemy Traits, Reactions, and Ancestry Logic.
Validates Parrying Buckler Hard 6 first-attack, Thick Blubber Fire bypass,
Voracious Regrowth healing and Fire/Acid disabling, Pressurized Steam Vent,
Dry Bones Bashing/Piercing traits, Plate Bastion, and Overkill Wound calculations.
"""

from __future__ import annotations

import math
import pytest

from combat_sim.core.types import (
    Ancestry,
    Difficulty,
    Tag,
    WeaponTrait,
)
from combat_sim.domain.equipment import (
    create_bone_shiv,
    create_notched_sword,
    create_spiked_mace,
    create_dwarven_great_hammer,
    create_fire_flask,
    create_shortbow,
)
from combat_sim.domain.traits import (
    ParryingBuckler,
    ThickBlubber,
    VoraciousRegrowth,
    PressurizedSteamVent,
    DryBones,
    PlateBastion,
    BeastAncestryTrait,
    UndeadAncestryTrait,
    MonstrosityAncestryTrait,
)


class DummyEnemyEntity:
    """Test stub for enemy entity."""
    def __init__(self, name="Enemy", wounds=3, max_wounds=3, defence_tn=2, zone_id="Z1"):
        self.name = name
        self.wounds = wounds
        self.max_wounds = max_wounds
        self.defence_tn = defence_tn
        self.zone_id = zone_id
        self.last_round_fire_or_acid_damage = False
        self.is_alive = True

    def heal_wound(self, amount: int = 1) -> None:
        self.wounds = min(self.max_wounds, self.wounds + amount)


class DummyAttackContext:
    """Test stub for attack context."""
    def __init__(self, is_melee=True, is_ranged=False, tags=None, traits=None):
        self.is_melee = is_melee
        self.is_ranged = is_ranged
        self.tags = tags or set()
        self.traits = traits or set()


class TestParryingBucklerTrait:
    """Test Parrying Buckler Hard 6 on 1st melee attack, Normal 5+ on subsequent."""

    def test_parrying_buckler_first_melee_hard_six(self):
        """First melee attack received in a round must test vs Hard (6)."""
        enemy = DummyEnemyEntity()
        buckler = ParryingBuckler()
        attack = DummyAttackContext(is_melee=True)

        diff1 = buckler.on_incoming_attack_modify_difficulty(enemy, None, attack, Difficulty.NORMAL)
        assert diff1 == Difficulty.HARD
        assert buckler.buckler_active is False

    def test_parrying_buckler_subsequent_normal_five(self):
        """Subsequent melee attacks in the same round resolve at Normal (5+)."""
        enemy = DummyEnemyEntity()
        buckler = ParryingBuckler()
        attack = DummyAttackContext(is_melee=True)

        # 1st attack commits buckler
        buckler.on_incoming_attack_modify_difficulty(enemy, None, attack, Difficulty.NORMAL)
        # 2nd attack resolves normally
        diff2 = buckler.on_incoming_attack_modify_difficulty(enemy, None, attack, Difficulty.NORMAL)
        assert diff2 == Difficulty.NORMAL

    def test_parrying_buckler_resets_at_round_start(self):
        """Round start resets buckler to active state."""
        enemy = DummyEnemyEntity()
        buckler = ParryingBuckler()
        attack = DummyAttackContext(is_melee=True)

        buckler.on_incoming_attack_modify_difficulty(enemy, None, attack, Difficulty.NORMAL)
        assert buckler.buckler_active is False

        buckler.on_round_start(enemy)
        assert buckler.buckler_active is True

    def test_parrying_buckler_does_not_affect_ranged(self):
        """Ranged attacks are not modified by Parrying Buckler."""
        enemy = DummyEnemyEntity()
        buckler = ParryingBuckler()
        ranged_attack = DummyAttackContext(is_melee=False, is_ranged=True)

        diff = buckler.on_incoming_attack_modify_difficulty(enemy, None, ranged_attack, Difficulty.NORMAL)
        assert diff == Difficulty.NORMAL
        assert buckler.buckler_active is True  # Buckler not consumed by ranged attack!


class TestThickBlubberTrait:
    """Test Thick Blubber Bane (-1d) and Fire tag bypass."""

    def test_thick_blubber_bane_penalty(self):
        """Attacks without [Fire] tag suffer -1d Bane on attacker pool."""
        enemy = DummyEnemyEntity()
        blubber = ThickBlubber()
        sword = create_notched_sword()

        modified_pool = blubber.on_incoming_attack_modify_pool(enemy, None, sword, current_pool=4)
        assert modified_pool == 3

    def test_thick_blubber_fire_tag_bypass(self):
        """Attacks with [Fire] tag bypass Thick Blubber and roll full pool."""
        enemy = DummyEnemyEntity()
        blubber = ThickBlubber()
        molotov = create_fire_flask()

        modified_pool = blubber.on_incoming_attack_modify_pool(enemy, None, molotov, current_pool=4)
        assert modified_pool == 4


class TestVoraciousRegrowthTrait:
    """Test Voracious Regrowth round healing and Fire/Acid disabling."""

    def test_voracious_regrowth_heals_wound(self):
        """Swamp Troll recovers 1 lost Wound at Round Start when not burned."""
        enemy = DummyEnemyEntity(wounds=1, max_wounds=3)
        regrowth = VoraciousRegrowth()
        enemy.last_round_fire_or_acid_damage = False

        regrowth.on_round_start(enemy)
        assert enemy.wounds == 2

    def test_voracious_regrowth_disabled_by_fire_or_acid(self):
        """Swamp Troll does NOT heal if damaged by [Fire] or [Acidic] in prior round."""
        enemy = DummyEnemyEntity(wounds=1, max_wounds=3)
        regrowth = VoraciousRegrowth()
        enemy.last_round_fire_or_acid_damage = True

        regrowth.on_round_start(enemy)
        assert enemy.wounds == 1  # No healing occurred


class TestPressurizedSteamVentTrait:
    """Test Pressurized Steam Vent reaction upon taking a Wound."""

    def test_steam_vent_hazard_reaction_on_wound(self):
        """Taking 1+ Wounds triggers Slink 5+/2 hazard test for 2 Fire damage in Zone."""
        enemy = DummyEnemyEntity(zone_id="Vault")
        vent = PressurizedSteamVent()

        result = vent.on_wound_taken(enemy, wounds_taken=1, source=None)
        assert result is not None
        assert result["steam_vent_burst"] is True
        assert result["damage"] == 2
        assert Tag.FIRE in result["tags"]
        assert result["threat_tn"] == 2
        assert result["zone_id"] == "Vault"

    def test_steam_vent_does_not_trigger_on_zero_wounds(self):
        """Taking 0 Wounds produces no steam vent reaction."""
        enemy = DummyEnemyEntity()
        vent = PressurizedSteamVent()
        assert vent.on_wound_taken(enemy, wounds_taken=0, source=None) is None


class TestDryBonesTrait:
    """Test Dry Bones Bashing/Crushing Boon and Piercing/Cutting Bane."""

    def test_dry_bones_bashing_boon(self):
        """Bashing weapons gain +1d Boon vs Dry Bones skeletons."""
        enemy = DummyEnemyEntity()
        dry_bones = DryBones()
        mace = create_spiked_mace()  # Bashing trait

        modified_pool = dry_bones.on_incoming_attack_modify_pool(enemy, None, mace, current_pool=3)
        assert modified_pool == 4

    def test_dry_bones_crushing_boon(self):
        """Crushing weapons gain +1d Boon vs Dry Bones skeletons."""
        enemy = DummyEnemyEntity()
        dry_bones = DryBones()
        hammer = create_dwarven_great_hammer()  # Crushing & Bashing

        modified_pool = dry_bones.on_incoming_attack_modify_pool(enemy, None, hammer, current_pool=3)
        assert modified_pool == 4

    def test_dry_bones_piercing_bane(self):
        """Piercing weapons suffer -1d Bane vs Dry Bones skeletons."""
        enemy = DummyEnemyEntity()
        dry_bones = DryBones()
        shiv = create_bone_shiv()  # Piercing trait

        modified_pool = dry_bones.on_incoming_attack_modify_pool(enemy, None, shiv, current_pool=3)
        assert modified_pool == 2

    def test_dry_bones_ranged_bow_bane(self):
        """Ranged bows suffer -1d Bane vs Dry Bones skeletons."""
        enemy = DummyEnemyEntity()
        dry_bones = DryBones()
        bow = create_shortbow()  # Ranged bow

        modified_pool = dry_bones.on_incoming_attack_modify_pool(enemy, None, bow, current_pool=3)
        assert modified_pool == 2


class TestPlateBastionTrait:
    """Test Plate Armor Bastion damage reduction and elemental/piercing bypass."""

    def test_bastion_reduces_normal_damage(self):
        """Bastion ignores first 1 point of normal damage."""
        enemy = DummyEnemyEntity()
        bastion = PlateBastion()
        assert bastion.on_incoming_damage_modify(enemy, None, damage=3) == 2

    def test_bastion_bypassed_by_piercing(self):
        """Piercing weapons bypass Bastion."""
        enemy = DummyEnemyEntity()
        bastion = PlateBastion()
        traits = {WeaponTrait.PIERCING}
        assert bastion.on_incoming_damage_modify(enemy, None, damage=3, traits=traits) == 3

    def test_bastion_bypassed_by_fire_tag(self):
        """Elemental attacks bypass Bastion."""
        enemy = DummyEnemyEntity()
        bastion = PlateBastion()
        tags = {Tag.FIRE}
        assert bastion.on_incoming_damage_modify(enemy, None, damage=3, tags=tags) == 3


class TestOverkillWoundsCalculation:
    """Test Boss & Elite Overkill Wound conversion rule: floor(Successes / Defence TN)."""

    @pytest.mark.parametrize(
        "successes,defence_tn,expected_wounds",
        [
            (0, 2, 0),
            (1, 2, 0),  # 1 < 2 -> 0 Wounds (Stagger evaluation only)
            (2, 2, 1),  # Exact multiple -> 1 Wound
            (3, 2, 1),  # 1 Wound with remainder
            (4, 2, 2),  # 2 Wounds
            (5, 2, 2),
            (6, 2, 3),  # 3 Wounds
            (2, 3, 0),  # 2 < 3 -> 0 Wounds
            (3, 3, 1),
            (6, 3, 2),
        ],
    )
    def test_overkill_wounds_formula(self, successes, defence_tn, expected_wounds):
        """Calculate wounds dealt to Elite/Boss enemies."""
        wounds_dealt = successes // defence_tn if defence_tn > 0 else 0
        assert wounds_dealt == expected_wounds


class TestAncestryTraits:
    """Test Ancestry morale and weakness handlers."""

    def test_undead_ancestry_morale_immunity(self):
        """Undead are immune to morale checks."""
        enemy = DummyEnemyEntity()
        undead = UndeadAncestryTrait()
        assert undead.on_morale_check_trigger(enemy, "50_percent_loss") is False
        assert undead.on_morale_check_trigger(enemy, "commander_dead") is False

    def test_beast_ancestry_morale_triggers(self):
        """Beasts trigger morale on Fire, Loud, or 50% loss."""
        enemy = DummyEnemyEntity()
        beast = BeastAncestryTrait()
        assert beast.on_morale_check_trigger(enemy, "fire") is True
        assert beast.on_morale_check_trigger(enemy, "loud") is True
        assert beast.on_morale_check_trigger(enemy, "50_percent_loss") is True
        assert beast.on_morale_check_trigger(enemy, "normal_hit") is False
