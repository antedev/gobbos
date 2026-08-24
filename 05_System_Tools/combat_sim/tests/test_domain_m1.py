"""Milestone 1 Tactical Domain & Models Verification Suite.

Validates all required enums, domain entities, equipment catalogue, quirks,
traits, and graph topology models against the authoritative specifications.
"""

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
    create_spark_bomb,
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
from combat_sim.domain.topology import (
    TopologyGraph,
    Zone,
    ZoneProfile,
    ZoneTrait,
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


class TestCoreEnumsAndTypes:
    """Verify exact values and members of all core tactical enums."""

    def test_difficulty_enum(self):
        assert Difficulty.EASY == 4
        assert Difficulty.NORMAL == 5
        assert Difficulty.HARD == 6
        assert Difficulty.EASY.label == "4+"
        assert Difficulty.NORMAL.label == "5+"
        assert Difficulty.HARD.label == "6"
        assert Difficulty.NORMAL.meets_threshold(5) is True
        assert Difficulty.NORMAL.meets_threshold(4) is False

    def test_condition_enum(self):
        expected_conditions = {
            "WEAKENED", "RESTRAINED", "DUMB", "SILENCED",
            "BLINDED", "TERRIFIED", "STUNNED", "PRONE", "STAGGERED"
        }
        actual_names = {c.name for c in Condition}
        assert expected_conditions.issubset(actual_names)

    def test_ancestry_enum(self):
        expected_ancestries = {"BEAST", "HUMANOID", "UNDEAD", "MONSTROSITY", "FIEND"}
        actual_names = {a.name for a in Ancestry}
        assert expected_ancestries.issubset(actual_names)

    def test_enemy_scale_enum(self):
        expected_scales = {"STANDARD", "ELITE", "MOB"}
        actual_names = {s.name for s in EnemyScale}
        assert expected_scales.issubset(actual_names)

    def test_cover_type_enum(self):
        expected_covers = {"NONE", "PARTIAL", "FULL"}
        actual_names = {c.name for c in CoverType}
        assert expected_covers.issubset(actual_names)

    def test_action_type_enum(self):
        expected_actions = {
            "MOVE", "MELEE_ATTACK", "RANGED_ATTACK", "PLUNDER",
            "MANIPULATE", "ORDER", "DODGE", "PARRY", "SCATTER"
        }
        actual_names = {a.name for a in ActionType}
        assert expected_actions.issubset(actual_names)

    def test_zone_trait_type_enum(self):
        expected_traits = {
            "SLIPPERY", "BURNING", "TOXIC", "NARROW",
            "PILLARS", "RUBBLE", "SHORING"
        }
        actual_names = {t.name for t in ZoneTraitType}
        assert expected_traits.issubset(actual_names)

    def test_threat_profile_shorthand(self):
        threat = ThreatProfile(
            threat_stat="Tough",
            difficulty=Difficulty.NORMAL,
            threat_tn=2,
            damage=3,
            is_aoe=False
        )
        assert threat.shorthand == "Tough 5+/2 (3 Dmg)"

        aoe_threat = ThreatProfile(
            threat_stat="Slink",
            difficulty=Difficulty.EASY,
            threat_tn=1,
            damage=2,
            is_aoe=True
        )
        assert aoe_threat.shorthand == "Slink 4+/1 (2 Dmg AoE)"


class TestTopologyAndRouting:
    """Verify Zone, ZoneProfile, ZoneTrait, and TopologyGraph routing."""

    def test_zone_profile_and_traits(self):
        profile = ZoneProfile(difficulty=Difficulty.NORMAL, tn=2)
        assert profile.shorthand == "5+/2"

        zone = Zone(id="z1", name="Crypt Chamber", profile=profile)
        assert zone.has_trait(ZoneTraitType.SLIPPERY) is False

        trait = ZoneTrait(trait_type=ZoneTraitType.SLIPPERY, description="Wet mossy flagstones")
        zone.add_trait(trait)
        assert zone.has_trait(ZoneTraitType.SLIPPERY) is True
        assert zone.get_trait(ZoneTraitType.SLIPPERY) == trait

        zone.remove_trait(ZoneTraitType.SLIPPERY)
        assert zone.has_trait(ZoneTraitType.SLIPPERY) is False

    def test_directional_cover(self):
        zone = Zone(id="z2", name="Pillared Hall", cover=CoverType.NONE)
        zone.set_directional_cover("z1", CoverType.FULL)
        assert zone.get_cover_from("z1") == CoverType.FULL
        assert zone.get_cover_from("z3") == CoverType.NONE

    def test_graph_bfs_and_connectivity(self):
        graph = TopologyGraph()
        z1 = Zone(id="z1", name="West")
        z2 = Zone(id="z2", name="Center")
        z3 = Zone(id="z3", name="East")
        z_isolated = Zone(id="z_iso", name="Isolated Vault")

        for z in (z1, z2, z3, z_isolated):
            graph.add_zone(z)

        graph.connect("z1", "z2")
        graph.connect("z2", "z3")

        assert graph.are_adjacent("z1", "z2") is True
        assert graph.are_adjacent("z2", "z1") is True
        assert graph.are_adjacent("z1", "z3") is False

        assert graph.get_distance("z1", "z1") == 0
        assert graph.get_distance("z1", "z2") == 1
        assert graph.get_distance("z1", "z3") == 2
        assert graph.get_distance("z1", "z_iso") == -1

        assert graph.find_path("z1", "z3") == ["z1", "z2", "z3"]
        assert graph.find_path("z1", "z_iso") == []

        nearby = graph.get_zones_within_distance("z1", 1)
        assert set(nearby) == {"z1", "z2"}
        all_reachable = graph.get_zones_within_distance("z1", 2)
        assert set(all_reachable) == {"z1", "z2", "z3"}


class TestEquipmentCatalogue:
    """Verify equipment factory functions, traits, impact sizes, and armor profiles."""

    def test_melee_weapons(self):
        shiv = create_bone_shiv()
        assert shiv.handedness == WeaponHandedness.ONE_HAND
        assert shiv.bulk == 1
        assert shiv.has_trait(WeaponTrait.CONCEALABLE)
        assert shiv.get_effective_impact_size(1) == 1

        sword = create_notched_sword()
        assert sword.handedness == WeaponHandedness.ONE_HAND
        assert sword.bulk == 2
        assert sword.is_melee is True

        greataxe = create_greataxe()
        assert greataxe.handedness == WeaponHandedness.TWO_HAND
        assert greataxe.bulk == 3
        assert greataxe.has_trait(WeaponTrait.HEAVY)
        assert greataxe.has_trait(WeaponTrait.CLEAVE)
        # Heavy adds +1 Impact Size
        assert greataxe.get_effective_impact_size(1) == 2

        hammer = create_dwarven_great_hammer()
        assert hammer.has_trait(WeaponTrait.CRUSHING)
        assert hammer.has_trait(WeaponTrait.BASHING)
        # Crushing adds +2 Impact Size
        assert hammer.get_effective_impact_size(1) == 3

        halberd = create_halberd()
        assert halberd.has_trait(WeaponTrait.REACH)
        assert halberd.has_trait(WeaponTrait.CLEAVE)

    def test_ranged_weapons(self):
        sling = create_sling()
        assert sling.range_zones == 1
        assert sling.has_trait(WeaponTrait.FAST_THROW)
        assert sling.is_ranged is True

        bow = create_shortbow()
        assert bow.range_zones == 2
        assert bow.has_trait(WeaponTrait.RAPID_SHOT)

        xbow = create_crossbow()
        assert xbow.range_zones == 2
        assert xbow.min_brains == 2
        assert xbow.has_trait(WeaponTrait.ARMOR_PIERCING)

        longbow = create_longbow()
        assert longbow.range_zones == 3
        assert longbow.min_tough == 2

        arbalest = create_arbalest()
        assert arbalest.range_zones == 3
        assert arbalest.has_trait(WeaponTrait.HEAVY)
        assert arbalest.has_trait(WeaponTrait.ARMOR_PIERCING)

        repeater = create_repeating_crossbow()
        assert repeater.has_trait(WeaponTrait.CLOCKWORK)

    def test_armor_and_shields(self):
        light = create_light_armor()
        assert light.armor_dice == 1
        assert light.slink_bane == 0
        assert light.cannot_swim is False

        medium = create_medium_armor()
        assert medium.armor_dice == 2
        assert medium.slink_bane == 1

        heavy = create_heavy_armor()
        assert heavy.armor_dice == 3
        assert heavy.slink_bane == 2
        assert heavy.cannot_swim is True

        runed = create_runed_carapace()
        assert runed.armor_dice == 3
        assert runed.slink_bane == 1

        shield = create_shield()
        assert shield.armor_dice == 1
        assert shield.enables_parry is True
        assert shield.halves_movement is False

        pavise = create_tower_pavise()
        assert pavise.armor_dice == 2
        assert pavise.halves_movement is True

        godstone = create_godstone_aegis()
        assert godstone.immune_to_piercing is True
        assert godstone.break_threshold == 0

    def test_consumables_and_explosives(self):
        spark = create_spark_bomb()
        assert spark.is_explosive is True
        assert spark.threat.difficulty == Difficulty.EASY
        assert spark.threat.damage == 1

        molotov = create_molotov()
        assert Tag.FIRE in molotov.tags
        assert molotov.damage == 2
        assert molotov.impact_size == 2

        smoke = create_smoke_pot()
        assert Tag.GASEOUS in smoke.tags
        assert Tag.DARK in smoke.tags
        assert smoke.damage == 0

        keg = create_powder_keg()
        assert keg.threat.threat_tn == 2
        assert keg.damage == 3
        assert keg.impact_size == 3

        mortar = create_mortar_shell()
        assert mortar.damage == 4
        assert mortar.blast_range == 2

        sol = create_sol_quartz()
        assert sol.damage == 5
        assert sol.threat.difficulty == Difficulty.HARD


class TestQuirksAndTwists:
    """Verify Quirk triggers, costs, effects, and modular twist modifiers."""

    def test_meat_shield_quirk(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", grunt=2)
        mob = PlayerMob(id="m1", name="Runts", zone_id="z1", size=3)
        mob_other_zone = PlayerMob(id="m2", name="Far Mob", zone_id="z2", size=3)

        meat_shield = MeatShield()

        # Cannot trigger if no mob or mob in other zone
        assert meat_shield.can_trigger(boss, {"allied_mob": None}) is False
        assert meat_shield.can_trigger(boss, {"allied_mob": mob_other_zone}) is False

        # Can trigger with mob in same zone
        assert meat_shield.can_trigger(boss, {"allied_mob": mob}) is True

        res = meat_shield.apply(boss, {"allied_mob": mob, "use_grunt": True})
        assert res["success"] is True
        assert res["resource_spent"] == "grunt"
        assert boss.grunt == 1

    def test_ankle_bite_quirk(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1")
        footpad = StandardEnemy(id="e1", name="Footpad", zone_id="z1")
        archer = StandardEnemy(id="e2", name="Archer", zone_id="z2")

        ankle_bite = AnkleBite()

        # Requires clean dodge vs melee enemy in same zone
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": False, "is_melee": True, "attacker": footpad}) is False
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": True, "is_melee": False, "attacker": footpad}) is False
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": True, "is_melee": True, "attacker": archer}) is False
        assert ankle_bite.can_trigger(boss, {"is_clean_dodge": True, "is_melee": True, "attacker": footpad}) is True

        res = ankle_bite.apply(boss, {"attacker": footpad})
        assert res["free_counter_attack"] is True
        assert res["bonus_successes"] == 1
        assert res["target"] == footpad

    def test_push_luck_quirk(self):
        boss = GoblinBoss(id="b1", name="Boss", zone_id="z1", grunt=2)
        push_luck = PushLuck()

        # Roll: [1, 3, 4] -> non-1s are index 1 (3) and index 2 (4)
        assert push_luck.can_trigger(boss, {"faces": [1, 3, 4]}) is True
        res = push_luck.apply(boss, {"faces": [1, 3, 4]})
        assert res["reroll_indices"] == [1, 2]
        assert res["locked_indices"] == [0]
        assert boss.grunt == 1

    def test_modular_twists(self):
        meat_shield = MeatShield()
        assert meat_shield.get_effective_grunt_cost() == 1

        efficient = TwistModifier.efficient()
        meat_shield.add_twist(efficient)
        assert meat_shield.get_effective_grunt_cost() == 0

        spiteful = TwistModifier.spiteful()
        loud = TwistModifier.loud()
        reflexive = TwistModifier.reflexive()

        assert spiteful.name == "Spiteful"
        assert loud.name == "Loud"
        assert reflexive.name == "Reflexive"

    def test_other_quirks(self):
        swallow = SwallowLoot()
        assert swallow.internal_bulk_capacity == 2

        boss = GoblinBoss(id="b1", name="Big Boss", zone_id="z1", size=2, quirks=[swallow])
        rat = StandardEnemy(id="e1", name="Rat", zone_id="z1", size=0)
        bear = EliteEnemy(id="e2", name="Bear", zone_id="z1", size=2)

        butcher = Butcher()
        assert butcher.can_trigger(boss, {"target": rat}) is True
        assert butcher.can_trigger(boss, {"target": bear}) is False


class TestEnemyTraitsAndAncestries:
    """Verify Parrying Buckler, Thick Blubber, Bastion, Steam Vent, Regrowth, Dry Bones."""

    def test_parrying_buckler(self):
        buckler = ParryingBuckler()
        enemy = EliteEnemy(id="e1", name="Highwayman", zone_id="z1", traits=[buckler])
        sword = create_notched_sword()

        # 1st melee attack in round is Hard (6)
        diff1 = buckler.on_incoming_attack_modify_difficulty(enemy, None, sword, Difficulty.NORMAL)
        assert diff1 == Difficulty.HARD
        assert buckler.buckler_active is False

        # 2nd melee attack in same round is Normal (5+)
        diff2 = buckler.on_incoming_attack_modify_difficulty(enemy, None, sword, Difficulty.NORMAL)
        assert diff2 == Difficulty.NORMAL

        # Reset at round start
        buckler.on_round_start(enemy)
        assert buckler.buckler_active is True
        diff3 = buckler.on_incoming_attack_modify_difficulty(enemy, None, sword, Difficulty.NORMAL)
        assert diff3 == Difficulty.HARD

    def test_thick_blubber(self):
        blubber = ThickBlubber()
        enemy = EliteEnemy(id="e1", name="Bear", zone_id="z1", traits=[blubber])

        normal_sword = create_notched_sword()
        fire_sword = Weapon(name="Flaming Blade", tags={Tag.FIRE})

        # Normal attack loses 1 die (Bane 1)
        assert blubber.on_incoming_attack_modify_pool(enemy, None, normal_sword, 3) == 2
        # Fire attack does not suffer Bane
        assert blubber.on_incoming_attack_modify_pool(enemy, None, fire_sword, 3) == 3

    def test_bastion_damage_reduction(self):
        bastion = Bastion()
        enemy = EliteEnemy(id="e1", name="Knight", zone_id="z1", traits=[bastion])

        # Normal attack of 3 damage reduced to 2
        assert bastion.on_incoming_damage_modify(enemy, None, 3, tags=set(), traits=set()) == 2
        # Piercing attack ignores Bastion
        assert bastion.on_incoming_damage_modify(enemy, None, 3, tags=set(), traits={WeaponTrait.PIERCING}) == 3
        # Fire attack ignores Bastion
        assert bastion.on_incoming_damage_modify(enemy, None, 3, tags={Tag.FIRE}, traits=set()) == 3

    def test_pressurized_steam_vent(self):
        vent = PressurizedSteamVent()
        enemy = EliteEnemy(id="e1", name="Solar Praetor", zone_id="z1", traits=[vent])

        burst = vent.on_wound_taken(enemy, wounds_taken=1, source=None)
        assert burst is not None
        assert burst["steam_vent_burst"] is True
        assert burst["damage"] == 2

    def test_voracious_regrowth(self):
        regrowth = VoraciousRegrowth()
        troll = EliteEnemy(id="e1", name="Troll", zone_id="z1", wounds=2, max_wounds=4, traits=[regrowth])

        # Normal round start: heals 1 wound
        troll.last_round_fire_or_acid_damage = False
        regrowth.on_round_start(troll)
        assert troll.wounds == 3

        # Disabled if burned in previous round
        troll.last_round_fire_or_acid_damage = True
        regrowth.on_round_start(troll)
        assert troll.wounds == 3  # Did not heal

    def test_dry_bones(self):
        dry_bones = DryBones()
        skeleton = StandardEnemy(id="s1", name="Skeleton", zone_id="z1", traits=[dry_bones])

        sword = create_notched_sword()  # Cutting
        mace = create_spiked_mace()     # Bashing
        bow = create_shortbow()         # Ranged bow + Piercing

        # Cutting -> Bane 1 (-1d)
        assert dry_bones.on_incoming_attack_modify_pool(skeleton, None, sword, 3) == 2
        # Bashing -> Boon 1 (+1d)
        assert dry_bones.on_incoming_attack_modify_pool(skeleton, None, mace, 3) == 4
        # Bow -> Bane 1 (-1d)
        assert dry_bones.on_incoming_attack_modify_pool(skeleton, None, bow, 3) == 2

    def test_ancestry_traits(self):
        beast_trait = BeastAncestryTrait()
        assert beast_trait.on_morale_check_trigger(None, "fire") is True
        assert beast_trait.on_morale_check_trigger(None, "casualty") is False

        undead_trait = UndeadAncestryTrait()
        assert undead_trait.on_morale_check_trigger(None, "50_percent_loss") is False


class TestEntitiesStateAndBehavior:
    """Verify GoblinBoss, PlayerMob, StandardEnemy, EliteEnemy, EnemyMob."""

    def test_goblin_boss_full_lifecycle(self):
        boss = GoblinBoss(
            id="b1",
            name="Garg",
            zone_id="z1",
            tough=2,
            slink=3,
            mouth=2,
            brains=1,
            grunt=2,
            main_hand=create_notched_sword(),
            off_hand=create_shield(),
            armor=create_medium_armor(),
        )

        assert boss.max_grit == 8  # 4 + 2 * 2 Tough
        assert boss.grit == 8
        assert boss.get_armor_dice() == 3  # 2 from medium armor + 1 from shield
        assert boss.get_slink_bane() == 1
        assert boss.can_parry() is True
        assert boss.get_movement_speed() == 3  # Slink 3 = Move 3

        # Action management
        assert boss.actions_left == 3
        assert boss.save_reaction() is True
        assert boss.actions_left == 2
        assert boss.saved_reactions == 1
        assert boss.use_reaction() is True
        assert boss.saved_reactions == 0

        # Damage and healing
        boss.take_damage(3)
        assert boss.grit == 5
        assert boss.is_alive is True
        boss.heal_grit(2)
        assert boss.grit == 7

        # Lethal damage
        boss.take_damage(10)
        assert boss.grit == 0
        assert boss.is_alive is False

    def test_player_mob_damage_models(self):
        # Single target decrement and spillover
        mob = PlayerMob(id="m1", name="Gobbos", zone_id="z1", size=3)
        assert mob.health_dice == [6, 6, 6]

        # 4 damage hits active die: 6 becomes 2
        mob.take_single_target_damage(4)
        assert mob.health_dice == [2, 6, 6]
        assert mob.size == 3

        # 3 damage hits active die: 2 exhausted, 1 spills into next die (6 becomes 5)
        mob.take_single_target_damage(3)
        assert mob.health_dice == [5, 6]
        assert mob.size == 2

        # AoE damage simultaneously hits all dice
        mob2 = PlayerMob(id="m2", name="Swarm", zone_id="z1", size=4)
        mob2.take_aoe_damage(2)
        assert mob2.health_dice == [4, 4, 4, 4]
        assert mob2.size == 4

        mob2.take_aoe_damage(5)
        assert mob2.health_dice == []
        assert mob2.size == 0
        assert mob2.is_alive is False

    def test_standard_enemy(self):
        guard = StandardEnemy(id="g1", name="City Guard", zone_id="z1", defence_tn=2, size=1)

        # 1 success: misses Defence 2, but Impact Size 1 >= Size 1 -> Staggers!
        res1 = guard.take_hit(successes=1, impact_size=1)
        assert res1["killed"] is False
        assert res1["staggered"] is True
        assert guard.is_staggered is True
        assert guard.get_effective_defence_tn() == 1  # 2 - 1 because staggered

        # 1 success against staggered guard (effective Defence 1) kills!
        res2 = guard.take_hit(successes=1, impact_size=1)
        assert res2["killed"] is True
        assert guard.is_alive is False

    def test_elite_enemy_overkill(self):
        boss_foe = EliteEnemy(
            id="e1", name="Solar Praetor", zone_id="z1", defence_tn=2, size=2, wounds=4, max_wounds=4
        )

        # 4 successes vs Defence 2 = floor(4 / 2) = 2 Wounds dealt (Overkill!)
        res = boss_foe.take_hit(successes=4, impact_size=2)
        assert res["wounds_dealt"] == 2
        assert boss_foe.wounds == 2
        assert boss_foe.is_alive is True

        # 1 success vs Defence 2, Impact Size 1 < Size 2: mass resistance ignores stagger
        res2 = boss_foe.take_hit(successes=1, impact_size=1)
        assert res2["wounds_dealt"] == 0
        assert res2["staggered"] is False
        assert boss_foe.is_staggered is False

    def test_enemy_mob_damage_scaling(self):
        mob_enemy = EnemyMob(id="em1", name="Robber Gang", zone_id="z1", size=3, base_damage=1)
        # Mob damage = base (1) + size (3) - 1 = 3
        assert mob_enemy.get_mob_damage() == 3

        mob_enemy.take_single_target_damage(7)
        # Active die (6) exhausted, 1 spilled into next die (6 becomes 5) -> Size 2
        assert mob_enemy.size == 2
        # Mob damage at Size 2 = 1 + 2 - 1 = 2
        assert mob_enemy.get_mob_damage() == 2


if __name__ == "__main__":
    import inspect
    print("Running Milestone 1 Domain & Models Test Suite...")
    test_classes = [
        TestCoreEnumsAndTypes,
        TestTopologyAndRouting,
        TestEquipmentCatalogue,
        TestQuirksAndTwists,
        TestEnemyTraitsAndAncestries,
        TestEntitiesStateAndBehavior,
    ]
    passed = 0
    failed = 0
    for cls in test_classes:
        instance = cls()
        for attr_name in dir(instance):
            if attr_name.startswith("test_"):
                method = getattr(instance, attr_name)
                if callable(method):
                    try:
                        method()
                        print(f"  [PASS] {cls.__name__}.{attr_name}")
                        passed += 1
                    except Exception as e:
                        print(f"  [FAIL] {cls.__name__}.{attr_name}: {e}")
                        failed += 1
    print(f"\nResults: {passed} passed, {failed} failed.")
    if failed > 0:
        raise SystemExit(1)

