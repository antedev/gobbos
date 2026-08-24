"""Adversarial Empirical Stress-Test Suite for Milestone 1 Domain Models.

Exhaustively verifies:
1. Quirks: Meat Shield redirection, Ankle Bite counter-attack triggers, Push Luck Grunt economy and locking.
2. Traits: Parrying Buckler multi-round difficulty state, Thick Blubber Bane and Fire bypass,
   Voracious Regrowth healing/suppression by Fire/Acid, Steam Vent burst on Wounds.
3. Armor & Shields: Slink bane stacking, Tough Parry authorization, Ablative sacrifice item removal.
4. Boundary & Edge Cases: Zero-resources, dead allies, negative dice bounds, multi-round resets.
"""

from __future__ import annotations

import pytest

from combat_sim.core.types import (
    ActionType,
    Ancestry,
    Condition,
    CoverType,
    Difficulty,
    EnemyScale,
    Tag,
    ThreatProfile,
    WeaponHandedness,
    WeaponTrait,
    ZoneTraitType,
)
from combat_sim.domain.entities import (
    BaseEntity,
    EliteEnemy,
    Enemy,
    EnemyMob,
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
    ThreatAttack,
)
from combat_sim.domain.equipment import (
    Armor,
    Consumable,
    Equipment,
    Shield,
    Weapon,
    create_arbalest,
    create_bone_shiv,
    create_crossbow,
    create_dwarven_great_hammer,
    create_fire_flask,
    create_godstone_aegis,
    create_great_hammer,
    create_greataxe,
    create_halberd,
    create_heavy_arbalest,
    create_heavy_armor,
    create_heavy_greataxe,
    create_light_armor,
    create_light_crossbow,
    create_longbow,
    create_medium_armor,
    create_medium_sword,
    create_military_longbow,
    create_molotov,
    create_mortar_shell,
    create_notched_sword,
    create_pot_lid_shield,
    create_powder_keg,
    create_repeating_crossbow,
    create_runed_carapace,
    create_shield,
    create_shortbow,
    create_sling,
    create_smoke_pot,
    create_sol_quartz,
    create_spiked_mace,
    create_tower_pavise,
)
from combat_sim.domain.quirks import (
    AnkleBite,
    Butcher,
    MeatShield,
    OpportunityStrike,
    PushLuck,
    Quirk,
    SecondWind,
    SlipperyQuirk,
    SwallowLoot,
    TwistModifier,
)
from combat_sim.domain.traits import (
    Bastion,
    BeastAncestryTrait,
    DryBones,
    EnemyTrait,
    FiendAncestryTrait,
    HumanoidAncestryTrait,
    MonstrosityAncestryTrait,
    ParryingBuckler,
    PlateBastion,
    PressurizedSteamVent,
    SteamVent,
    ThickBlubber,
    UndeadAncestryTrait,
    VoraciousRegrowth,
)


# =========================================================================
# 1. QUIRKS EMPIRICAL CHALLENGE SUITE
# =========================================================================

class TestMeatShieldEmpirical:
    """Stress-test Meat Shield redirection across all valid and invalid states."""

    def test_meat_shield_mob_present_same_zone(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=2)
        mob = PlayerMob(id="m1", name="Runts", zone_id="Z1", size=3, is_alive=True)
        meat_shield = MeatShield()

        assert meat_shield.can_trigger(boss, {"allied_mob": mob}) is True
        res = meat_shield.apply(boss, {"allied_mob": mob, "use_grunt": True})
        assert res["success"] is True
        assert res["redirected_to"] == "Runts"
        assert res["resource_spent"] == "grunt"
        assert boss.grunt == 1

    def test_meat_shield_mob_absent_or_none(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=2)
        meat_shield = MeatShield()

        assert meat_shield.can_trigger(boss, None) is False
        assert meat_shield.can_trigger(boss, {}) is False
        assert meat_shield.can_trigger(boss, {"allied_mob": None}) is False

    def test_meat_shield_mob_different_zone(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=2)
        mob_z2 = PlayerMob(id="m1", name="Far Runts", zone_id="Z2", size=3, is_alive=True)
        meat_shield = MeatShield()

        assert meat_shield.can_trigger(boss, {"allied_mob": mob_z2}) is False

    def test_meat_shield_dead_mob(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=2)
        dead_mob = PlayerMob(id="m1", name="Dead Runts", zone_id="Z1", size=0)
        dead_mob.is_alive = False
        meat_shield = MeatShield()

        assert meat_shield.can_trigger(boss, {"allied_mob": dead_mob}) is False

    def test_meat_shield_resource_exhaustion_and_reaction_spending(self):
        # 0 Grunt, 0 Reactions, 0 Actions -> Cannot trigger
        boss_empty = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=0, saved_reactions=0, actions_left=0)
        mob = PlayerMob(id="m1", name="Runts", zone_id="Z1", size=3, is_alive=True)
        meat_shield = MeatShield()

        assert meat_shield.can_trigger(boss_empty, {"allied_mob": mob}) is False

        # 0 Grunt, 1 Saved Reaction -> Spends reaction
        boss_reaction = GoblinBoss(id="b2", name="Boss", zone_id="Z1", grunt=0, saved_reactions=1, actions_left=0)
        assert meat_shield.can_trigger(boss_reaction, {"allied_mob": mob}) is True
        res = meat_shield.apply(boss_reaction, {"allied_mob": mob, "use_grunt": False})
        assert res["resource_spent"] == "saved_reaction"
        assert boss_reaction.saved_reactions == 0

        # 0 Grunt, 0 Saved Reactions, 1 Action Left -> Spends action
        boss_action = GoblinBoss(id="b3", name="Boss", zone_id="Z1", grunt=0, saved_reactions=0, actions_left=1)
        assert meat_shield.can_trigger(boss_action, {"allied_mob": mob}) is True
        res = meat_shield.apply(boss_action, {"allied_mob": mob, "use_grunt": False})
        assert res["resource_spent"] == "action"
        assert boss_action.actions_left == 0


class TestAnkleBiteEmpirical:
    """Stress-test Ankle Bite counter-attack trigger conditions."""

    def test_ankle_bite_trigger_matrix(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1")
        melee_foe_z1 = StandardEnemy(id="e1", name="Melee Foe", zone_id="Z1")
        melee_foe_z2 = StandardEnemy(id="e2", name="Melee Foe Far", zone_id="Z2")
        ranged_foe_z1 = StandardEnemy(id="e3", name="Ranged Foe", zone_id="Z1")
        ankle_bite = AnkleBite()

        # Clean Dodge + Melee + Same Zone -> Triggers!
        ctx_valid = {"is_clean_dodge": True, "is_melee": True, "attacker": melee_foe_z1}
        assert ankle_bite.can_trigger(boss, ctx_valid) is True
        res = ankle_bite.apply(boss, ctx_valid)
        assert res["free_counter_attack"] is True
        assert res["bonus_successes"] == 1
        assert res["target"] == melee_foe_z1

        # Failed Dodge -> Fails
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": False, "is_melee": True, "attacker": melee_foe_z1}) is False

        # Ranged attack in same zone -> Fails (must be melee)
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": True, "is_melee": False, "attacker": ranged_foe_z1}) is False

        # Melee attack from different zone (e.g. Reach across zone) -> Fails (must be same zone)
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": True, "is_melee": True, "attacker": melee_foe_z2}) is False

        # Missing attacker or None context -> Fails
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": True, "is_melee": True, "attacker": None}) is False
        assert ankle_bite.can_trigger(boss, None) is False


class TestPushLuckEmpirical:
    """Stress-test Push Luck Grunt economy and non-1s reroll indexing."""

    def test_push_luck_grunt_cost_and_state_updates(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=3)
        push_luck = PushLuck()

        # Roll [1, 2, 4, 1, 6] -> non-1s are indices 1, 2, 4
        ctx = {"faces": [1, 2, 4, 1, 6]}
        assert push_luck.can_trigger(boss, ctx) is True
        res = push_luck.apply(boss, ctx)
        assert res["reroll_indices"] == [1, 2, 4]
        assert res["locked_indices"] == [0, 3]
        assert res["grunt_spent"] == 1
        assert boss.grunt == 2

    def test_push_luck_all_ones_rejected(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=2)
        push_luck = PushLuck()

        # Roll [1, 1, 1] -> all 1s must not trigger Push Luck (locked for Gobbo Gamble)
        assert push_luck.can_trigger(boss, {"faces": [1, 1, 1]}) is False

    def test_push_luck_zero_grunt_rejected(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=0)
        push_luck = PushLuck()
        assert push_luck.can_trigger(boss, {"faces": [2, 3, 5]}) is False

    def test_push_luck_efficient_twist(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1", grunt=0)
        push_luck = PushLuck()
        push_luck.add_twist(TwistModifier.efficient())
        assert push_luck.get_effective_grunt_cost() == 0
        assert push_luck.can_trigger(boss, {"faces": [2, 3, 5]}) is True
        res = push_luck.apply(boss, {"faces": [2, 3, 5]})
        assert res["grunt_spent"] == 0
        assert boss.grunt == 0


# =========================================================================
# 2. ENEMY TRAITS EMPIRICAL CHALLENGE SUITE
# =========================================================================

class TestParryingBucklerEmpirical:
    """Stress-test Parrying Buckler difficulty modulation and multi-round resets."""

    def test_parrying_buckler_multi_round_and_ranged_interleaving(self):
        enemy = EliteEnemy(id="e1", name="Highwayman", zone_id="Z1")
        buckler = ParryingBuckler()
        enemy.add_trait(buckler)

        melee_sword = create_notched_sword()
        ranged_bow = create_shortbow()

        # Round 1: Buckler starts active
        assert buckler.buckler_active is True

        # Ranged attack 1 does not trigger or consume buckler
        diff_r = buckler.on_incoming_attack_modify_difficulty(enemy, None, ranged_bow, Difficulty.NORMAL)
        assert diff_r == Difficulty.NORMAL
        assert buckler.buckler_active is True

        # Melee attack 1 triggers Hard 6 and expends buckler
        diff_m1 = buckler.on_incoming_attack_modify_difficulty(enemy, None, melee_sword, Difficulty.NORMAL)
        assert diff_m1 == Difficulty.HARD
        assert buckler.buckler_active is False

        # Melee attack 2 in same round is Normal 5+
        diff_m2 = buckler.on_incoming_attack_modify_difficulty(enemy, None, melee_sword, Difficulty.NORMAL)
        assert diff_m2 == Difficulty.NORMAL
        assert buckler.buckler_active is False

        # Round 2 Start: Buckler resets to active
        buckler.on_round_start(enemy)
        assert buckler.buckler_active is True

        # Melee attack 1 in Round 2 triggers Hard 6 again
        diff_m3 = buckler.on_incoming_attack_modify_difficulty(enemy, None, melee_sword, Difficulty.NORMAL)
        assert diff_m3 == Difficulty.HARD
        assert buckler.buckler_active is False


class TestThickBlubberEmpirical:
    """Stress-test Thick Blubber Bane on non-fire attacks and bypass on fire."""

    def test_thick_blubber_pool_modification(self):
        enemy = EliteEnemy(id="e1", name="Forest Mauler", zone_id="Z1")
        blubber = ThickBlubber()
        enemy.add_trait(blubber)

        axe = create_heavy_greataxe()
        molotov = create_fire_flask()
        flame_blade = Weapon(name="Torch Blade", tags={Tag.FIRE})

        # Non-fire physical attack suffers -1d Bane
        assert blubber.on_incoming_attack_modify_pool(enemy, None, axe, current_pool=4) == 3
        # Pool size 1 becomes 0
        assert blubber.on_incoming_attack_modify_pool(enemy, None, axe, current_pool=1) == 0
        # Pool size 0 stays 0
        assert blubber.on_incoming_attack_modify_pool(enemy, None, axe, current_pool=0) == 0

        # Fire flask bypasses Thick Blubber
        assert blubber.on_incoming_attack_modify_pool(enemy, None, molotov, current_pool=4) == 4
        # Weapon with Tag.FIRE bypasses Thick Blubber
        assert blubber.on_incoming_attack_modify_pool(enemy, None, flame_blade, current_pool=4) == 4


class TestVoraciousRegrowthEmpirical:
    """Stress-test Voracious Regrowth healing and elemental suppression."""

    def test_voracious_regrowth_healing_and_suppression(self):
        troll = EliteEnemy(id="e1", name="Mire Troll", zone_id="Z1", wounds=1, max_wounds=3)
        regrowth = VoraciousRegrowth()
        troll.add_trait(regrowth)

        # Unburned troll heals 1 wound at round start
        troll.last_round_fire_or_acid_damage = False
        regrowth.on_round_start(troll)
        assert troll.wounds == 2

        # Full health troll does not heal beyond max_wounds
        troll.wounds = 3
        regrowth.on_round_start(troll)
        assert troll.wounds == 3

        # Burned troll does not heal
        troll.wounds = 1
        troll.last_round_fire_or_acid_damage = True
        regrowth.on_round_start(troll)
        assert troll.wounds == 1

    def test_voracious_regrowth_tag_detection_on_hit(self):
        troll = EliteEnemy(id="e1", name="Mire Troll", zone_id="Z1", wounds=3, max_wounds=3, defence_tn=1)
        regrowth = VoraciousRegrowth()
        troll.add_trait(regrowth)

        # Hit by normal attack
        troll.take_hit(successes=1, impact_size=1, tags=set())
        assert troll.current_round_fire_or_acid_damage is False
        assert troll.wounds == 2

        # Hit by fire attack
        troll.take_hit(successes=1, impact_size=1, tags={Tag.FIRE})
        assert troll.current_round_fire_or_acid_damage is True
        assert troll.wounds == 1


class TestSteamVentEmpirical:
    """Stress-test Pressurized Steam Vent hazard trigger on Wounds."""

    def test_steam_vent_hazard_burst_on_wound(self):
        praetor = EliteEnemy(id="e1", name="Solar Praetor", zone_id="Crypt", wounds=4, max_wounds=4, defence_tn=2)
        vent = PressurizedSteamVent()
        praetor.add_trait(vent)

        # Partial hit with 1 success: 0 wounds, staggered -> No vent burst
        res1 = praetor.take_hit(successes=1, impact_size=2)
        assert res1["wounds_dealt"] == 0
        assert res1["staggered"] is True
        assert len(res1["trait_reactions"]) == 0

        # Overkill hit with 4 successes: 4 // 1 (staggered defence 1) = 4 wounds -> Triggers vent burst!
        res2 = praetor.take_hit(successes=4, impact_size=2)
        assert res2["wounds_dealt"] == 4
        assert len(res2["trait_reactions"]) == 1
        burst = res2["trait_reactions"][0]
        assert burst["steam_vent_burst"] is True
        assert burst["threat_difficulty"] == Difficulty.NORMAL
        assert burst["threat_tn"] == 2
        assert burst["damage"] == 2
        assert Tag.FIRE in burst["tags"]
        assert burst["zone_id"] == "Crypt"


# =========================================================================
# 3. ARMOR & SHIELDS EMPIRICAL CHALLENGE SUITE
# =========================================================================

class TestArmorShieldsEmpirical:
    """Stress-test armor Slink bane stacking, Tough Parry authorization, and Ablative gear removal."""

    def test_armor_slink_bane_and_dice_stacking(self):
        # Light Armor + Shield
        boss_light = GoblinBoss(
            id="b1", name="Light Boss", zone_id="Z1", tough=1, slink=2,
            armor=create_light_armor(), off_hand=create_shield()
        )
        assert boss_light.get_armor_dice() == 2  # 1 (light) + 1 (shield)
        assert boss_light.get_slink_bane() == 0
        assert boss_light.can_parry() is True

        # Medium Armor + Tower Pavise
        boss_medium = GoblinBoss(
            id="b2", name="Medium Boss", zone_id="Z1", tough=1, slink=2,
            armor=create_medium_armor(), off_hand=create_tower_pavise()
        )
        assert boss_medium.get_armor_dice() == 4  # 2 (medium) + 2 (tower pavise)
        assert boss_medium.get_slink_bane() == 1
        assert boss_medium.can_parry() is True

        # Heavy Armor + No Shield (2H Greataxe)
        boss_heavy = GoblinBoss(
            id="b3", name="Heavy Boss", zone_id="Z1", tough=2, slink=2,
            armor=create_heavy_armor(), main_hand=create_greataxe(), off_hand=None
        )
        assert boss_heavy.get_armor_dice() == 3  # 3 (heavy) + 0
        assert boss_heavy.get_slink_bane() == 2
        assert boss_heavy.can_parry() is False

    def test_tough_parry_authorization(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="Z1")

        # No off-hand
        boss.off_hand = None
        assert boss.can_parry() is False

        # Dual-wielding weapons
        boss.off_hand = create_bone_shiv()
        assert boss.can_parry() is False

        # Standard Pot-Lid Shield
        boss.off_hand = create_pot_lid_shield()
        assert boss.can_parry() is True

        # Godstone Aegis
        boss.off_hand = create_godstone_aegis()
        assert boss.can_parry() is True

    def test_ablative_sacrifice_item_removal(self):
        boss = GoblinBoss(
            id="b1",
            name="Armored Boss",
            zone_id="Z1",
            tough=2,
            slink=3,
            armor=create_heavy_armor(),
            off_hand=create_tower_pavise(),
        )

        # Baseline state
        assert boss.get_armor_dice() == 5  # 3 (heavy) + 2 (pavise)
        assert boss.get_slink_bane() == 2
        assert boss.can_parry() is True
        # Base speed with Slink 3 is 3; Tower Pavise halves speed (3 // 2 = 1)
        assert boss.get_movement_speed() == 1

        # Ablative Sacrifice 1: Shield destroyed/sacrificed to absorb fatal blow
        boss.off_hand = None

        # State updates immediately upon shield sacrifice
        assert boss.get_armor_dice() == 3  # Shield dice gone
        assert boss.can_parry() is False   # Can no longer Parry
        assert boss.get_slink_bane() == 2  # Armor still imposes bane 2
        assert boss.get_movement_speed() == 3  # Movement no longer halved!

        # Ablative Sacrifice 2: Heavy Armor destroyed/sacrificed
        boss.armor = None

        # State updates immediately upon armor sacrifice
        assert boss.get_armor_dice() == 0  # No armor dice remaining
        assert boss.get_slink_bane() == 0  # Slink bane removed
        assert boss.get_movement_speed() == 3
