"""
Tier 3 Test Suite: Scenario Definitions, Encounters, and Integration Playouts.
Validates the three reference scenarios:
1. Street Skirmish (Armored Boss + Mob vs Robber Gang & Footpads across 3 zones with Partial Cover).
2. The Mauler's Den (2 Heavy Weapon Bosses + 2 Mobs vs Forest Mauler with Thick Blubber and Cleave).
3. Tomb of the Highwayman (Boss + Mob vs Armored Highwayman with Parrying Buckler & Dry Bones Skeletons).
"""

from __future__ import annotations

import pytest

from combat_sim.core.types import (
    Ancestry,
    Condition,
    CoverType,
    Difficulty,
    EnemyScale,
    Tag,
    WeaponHandedness,
    WeaponTrait,
    ZoneTraitType,
)
from combat_sim.domain.topology import Zone, ZoneProfile, ZoneTrait, TopologyGraph
from combat_sim.domain.equipment import (
    create_notched_sword,
    create_heavy_greataxe,
    create_spiked_mace,
    create_light_armor,
    create_medium_armor,
    create_pot_lid_shield,
)
from combat_sim.domain.quirks import MeatShield, AnkleBite, PushLuck
from combat_sim.domain.traits import (
    ParryingBuckler,
    ThickBlubber,
    DryBones,
    BeastAncestryTrait,
    UndeadAncestryTrait,
    HumanoidAncestryTrait,
)
from combat_sim.domain.entities import (
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
    EliteEnemy,
    EnemyMob,
    ThreatAttack,
)


class TestStreetSkirmishScenario:
    """Validate Setup and Components of Scenario 1: Street Skirmish."""

    def build_street_skirmish(self):
        """Construct Street Skirmish scenario graph and units."""
        topo = TopologyGraph()
        z_west = Zone(id="street_west", name="Street West", profile=ZoneProfile(Difficulty.NORMAL, 1))
        z_center = Zone(
            id="street_center",
            name="Street Center",
            profile=ZoneProfile(Difficulty.NORMAL, 1),
            cover=CoverType.PARTIAL,
        )
        z_east = Zone(
            id="alley_east",
            name="Alley East",
            profile=ZoneProfile(Difficulty.NORMAL, 1),
            traits=[ZoneTrait(ZoneTraitType.NARROW)],
        )
        topo.add_zone(z_west)
        topo.add_zone(z_center)
        topo.add_zone(z_east)
        topo.connect("street_west", "street_center")
        topo.connect("street_center", "alley_east")

        boss = GoblinBoss(
            id="garg",
            name="Boss Garg",
            zone_id="street_west",
            tough=2,
            slink=2,
            mouth=2,
            brains=1,
            grunt=2,
            main_hand=create_notched_sword(),
            off_hand=create_pot_lid_shield(),
            armor=create_medium_armor(),
            quirks=[AnkleBite()],
        )

        mob = PlayerMob(
            id="runts",
            name="Garg's Runts",
            zone_id="street_west",
            size=3,
            boss_id="garg",
        )

        robber_gang = EnemyMob(
            id="robbers",
            name="Robber Gang",
            zone_id="street_center",
            size=3,
            defence_tn=1,
            movement=2,
            morale_tn=2,
            base_damage=1,
            attacks=[
                ThreatAttack(
                    name="Shiv Swarm",
                    threat_stat="Slink",
                    difficulty=Difficulty.NORMAL,
                    threat_tn=1,
                    damage=3,
                )
            ],
        )

        footpad_a = StandardEnemy(
            id="footpad_a",
            name="Footpad Shiv",
            zone_id="street_center",
            defence_tn=1,
            movement=2,
            morale_tn=1,
            attacks=[ThreatAttack(name="Rusty Shiv", threat_stat="Slink", threat_tn=1, damage=1)],
        )

        footpad_b = StandardEnemy(
            id="footpad_b",
            name="Footpad Slinger",
            zone_id="alley_east",
            defence_tn=1,
            movement=2,
            morale_tn=1,
            attacks=[
                ThreatAttack(
                    name="Thrown Cobblestone",
                    threat_stat="Slink",
                    threat_tn=1,
                    damage=1,
                    range_zones=1,
                )
            ],
        )

        return {
            "topology": topo,
            "allies": [boss, mob],
            "enemies": [robber_gang, footpad_a, footpad_b],
        }

    def test_scenario_street_skirmish_structure(self):
        """Verify Street Skirmish setup and zone distances."""
        scen = self.build_street_skirmish()
        topo = scen["topology"]
        assert topo.get_distance("street_west", "street_center") == 1
        assert topo.get_distance("street_west", "alley_east") == 2

        boss = scen["allies"][0]
        assert boss.can_parry() is True
        assert boss.get_armor_dice() == 3  # Medium Armor (2d) + Shield (1d)
        assert boss.get_slink_bane() == 1  # Medium Armor Slink Bane 1
        assert boss.has_quirk("Ankle Bite") is True

    def test_street_skirmish_combat_interactions(self):
        """Verify footpad one-hit kill and robber gang damage scaling."""
        scen = self.build_street_skirmish()
        footpad_a: StandardEnemy = scen["enemies"][1]
        robber_gang: EnemyMob = scen["enemies"][0]

        # Footpad killed on 1 success vs Defence 1
        hit_res = footpad_a.take_hit(successes=1)
        assert hit_res["killed"] is True
        assert footpad_a.is_alive is False

        # Robber gang damage at Size 3 is 3
        assert robber_gang.get_mob_damage() == 3
        # After taking 6 damage, size becomes 2 and damage becomes 2
        robber_gang.take_single_target_damage(6)
        assert robber_gang.size == 2
        assert robber_gang.get_mob_damage() == 2


class TestMaulersDenScenario:
    """Validate Setup and Components of Scenario 2: The Mauler's Den."""

    def build_maulers_den(self):
        """Construct The Mauler's Den scenario."""
        topo = TopologyGraph()
        z_entrance = Zone(
            id="den_entrance",
            name="Den Entrance",
            profile=ZoneProfile(Difficulty.NORMAL, 2),
            traits=[ZoneTrait(ZoneTraitType.NARROW)],
        )
        z_main = Zone(
            id="main_den",
            name="Main Den",
            profile=ZoneProfile(Difficulty.NORMAL, 2),
            traits=[
                ZoneTrait(ZoneTraitType.RUBBLE),
                ZoneTrait(ZoneTraitType.PILLARS),
            ],
        )
        topo.add_zone(z_entrance)
        topo.add_zone(z_main)
        topo.connect("den_entrance", "main_den")

        boss1 = GoblinBoss(
            id="skag",
            name="Boss Skag",
            zone_id="den_entrance",
            tough=3,
            slink=1,
            mouth=2,
            brains=1,
            grunt=2,
            main_hand=create_heavy_greataxe(),
            armor=create_light_armor(),
            quirks=[MeatShield()],
        )

        boss2 = GoblinBoss(
            id="grub",
            name="Boss Grub",
            zone_id="den_entrance",
            tough=3,
            slink=2,
            mouth=1,
            brains=1,
            grunt=2,
            main_hand=create_heavy_greataxe(),
            armor=create_light_armor(),
            quirks=[MeatShield()],
        )

        mob1 = PlayerMob(id="mob_skag", name="Skag's Boyz", zone_id="den_entrance", size=2, boss_id="skag")
        mob2 = PlayerMob(id="mob_grub", name="Grub's Crew", zone_id="den_entrance", size=3, boss_id="grub")

        bear = EliteEnemy(
            id="forest_mauler",
            name="Forest Mauler",
            zone_id="main_den",
            size=2,
            wounds=3,
            max_wounds=3,
            defence_tn=2,
            movement=2,
            morale_tn=3,
            ancestry=Ancestry.BEAST,
            traits=[ThickBlubber(), BeastAncestryTrait()],
            attacks=[
                ThreatAttack(
                    name="Crushing Claws",
                    threat_stat="Tough",
                    difficulty=Difficulty.NORMAL,
                    threat_tn=2,
                    damage=3,
                    cleave=True,
                )
            ],
        )

        return {
            "topology": topo,
            "allies": [boss1, boss2, mob1, mob2],
            "enemies": [bear],
        }

    def test_scenario_maulers_den_structure(self):
        """Verify Mauler's Den stats and Stagger interactions."""
        scen = self.build_maulers_den()
        boss1: GoblinBoss = scen["allies"][0]
        bear: EliteEnemy = scen["enemies"][0]

        # Boss wielding Heavy Greataxe (+1 Impact Size) has Impact Size 2 vs Size 2 Bear
        axe = boss1.main_hand
        assert axe.get_effective_impact_size(boss1.size) == 2
        assert axe.get_effective_impact_size(boss1.size) >= bear.size  # Able to stagger!

        # Bear Thick Blubber imposes -1d Bane on non-fire
        blubber = bear.get_trait("Thick Blubber")
        assert blubber is not None
        assert blubber.on_incoming_attack_modify_pool(bear, boss1, axe, 4) == 3

    def test_maulers_den_meat_shield_and_cleave(self):
        """Verify Meat Shield redirection and Bear Cleave on Mobs."""
        scen = self.build_maulers_den()
        boss1: GoblinBoss = scen["allies"][0]
        mob1: PlayerMob = scen["allies"][2]
        bear: EliteEnemy = scen["enemies"][0]

        # Meat shield redirects hit to mob
        quirk: MeatShield = boss1.get_quirk(MeatShield)
        assert quirk.can_trigger(boss1, {"allied_mob": mob1}) is True
        res = quirk.apply(boss1, {"allied_mob": mob1})
        assert res["success"] is True

        # Bear Overkill calculation: 4 successes vs Defence 2 = 2 Wounds
        hit_res = bear.take_hit(successes=4)
        assert hit_res["wounds_dealt"] == 2
        assert bear.wounds == 1
        assert bear.is_alive is True


class TestTombOfTheHighwaymanScenario:
    """Validate Setup and Components of Scenario 3: Tomb of the Highwayman."""

    def build_tomb_highwayman(self):
        """Construct Tomb of the Highwayman scenario."""
        topo = TopologyGraph()
        z_ante = Zone(
            id="crypt_antechamber",
            name="Crypt Antechamber",
            profile=ZoneProfile(Difficulty.NORMAL, 1),
            traits=[ZoneTrait(ZoneTraitType.SLIPPERY)],
        )
        z_vault = Zone(
            id="burial_vault",
            name="Burial Vault",
            profile=ZoneProfile(Difficulty.NORMAL, 2),
            traits=[ZoneTrait(ZoneTraitType.SHORING)],
        )
        topo.add_zone(z_ante)
        topo.add_zone(z_vault)
        topo.connect("crypt_antechamber", "burial_vault")

        boss = GoblinBoss(
            id="wizgog",
            name="Boss Wizgog",
            zone_id="crypt_antechamber",
            tough=2,
            slink=3,
            mouth=2,
            brains=2,
            grunt=2,
            main_hand=create_spiked_mace(),
            armor=create_light_armor(),
            quirks=[PushLuck()],
        )

        mob = PlayerMob(
            id="tomb_diggers",
            name="Tomb Diggers",
            zone_id="crypt_antechamber",
            size=3,
            armor_rating=1,
            boss_id="wizgog",
        )

        highwayman = EliteEnemy(
            id="highwayman",
            name="Armored Highwayman",
            zone_id="burial_vault",
            size=1,
            wounds=2,
            max_wounds=2,
            defence_tn=2,
            movement=1,
            morale_tn=2,
            traits=[ParryingBuckler(), HumanoidAncestryTrait()],
            attacks=[
                ThreatAttack(name="Broadsword", threat_stat="Tough", threat_tn=2, damage=2)
            ],
        )

        skel_a = StandardEnemy(
            id="skel_a",
            name="Skeleton Sentry A",
            zone_id="burial_vault",
            defence_tn=2,
            movement=1,
            morale_tn=1,
            ancestry=Ancestry.UNDEAD,
            traits=[DryBones(), UndeadAncestryTrait()],
            attacks=[ThreatAttack(name="Notched Scimitar", threat_stat="Tough", threat_tn=1, damage=1)],
        )

        skel_b = StandardEnemy(
            id="skel_b",
            name="Skeleton Sentry B",
            zone_id="crypt_antechamber",
            defence_tn=2,
            movement=1,
            morale_tn=1,
            ancestry=Ancestry.UNDEAD,
            traits=[DryBones(), UndeadAncestryTrait()],
            attacks=[ThreatAttack(name="Notched Scimitar", threat_stat="Tough", threat_tn=1, damage=1)],
        )

        return {
            "topology": topo,
            "allies": [boss, mob],
            "enemies": [highwayman, skel_a, skel_b],
        }

    def test_scenario_tomb_highwayman_structure(self):
        """Verify Tomb of Highwayman traits and Bashing interactions."""
        scen = self.build_tomb_highwayman()
        boss: GoblinBoss = scen["allies"][0]
        skel: StandardEnemy = scen["enemies"][1]
        highwayman: EliteEnemy = scen["enemies"][0]

        # Boss spiked mace (Bashing) gains +1d Boon vs Skeleton Dry Bones
        dry_bones: DryBones = skel.get_trait("Dry Bones")
        assert dry_bones is not None
        assert dry_bones.on_incoming_attack_modify_pool(skel, boss, boss.main_hand, 3) == 4

        # Highwayman Parrying Buckler: 1st melee attack is Hard 6
        buckler: ParryingBuckler = highwayman.get_trait("Parrying Buckler")
        assert buckler is not None
        diff1 = buckler.on_incoming_attack_modify_difficulty(highwayman, boss, boss.main_hand, Difficulty.NORMAL)
        assert diff1 == Difficulty.HARD
        diff2 = buckler.on_incoming_attack_modify_difficulty(highwayman, boss, boss.main_hand, Difficulty.NORMAL)
        assert diff2 == Difficulty.NORMAL


class TestPrebuiltScenariosPackage:
    """Validate that prebuilt reference scenario builders in combat_sim.scenarios construct valid scenarios."""

    def test_build_street_skirmish_scenario_package(self):
        from combat_sim.scenarios import build_street_skirmish, Scenario

        scen = build_street_skirmish()
        assert isinstance(scen, Scenario)
        assert scen.name == "Street Skirmish"
        assert len(scen.allies) == 2
        assert len(scen.enemies) == 3
        assert scen.topology.get_distance("street_west", "alley_east") == 2

        boss = scen.allies[0]
        assert isinstance(boss, GoblinBoss)
        assert boss.has_quirk("Ankle Bite") is True
        assert boss.can_parry() is True

        mob = scen.allies[1]
        assert isinstance(mob, PlayerMob)
        assert mob.size == 3

    def test_build_maulers_den_scenario_package(self):
        from combat_sim.scenarios import build_maulers_den, Scenario

        scen = build_maulers_den()
        assert isinstance(scen, Scenario)
        assert scen.name == "The Mauler's Den"
        assert len(scen.allies) == 4  # 2 Bosses + 2 Mobs
        assert len(scen.enemies) == 1  # Forest Mauler

        boss1, boss2, mob1, mob2 = scen.allies
        assert isinstance(boss1, GoblinBoss)
        assert isinstance(boss2, GoblinBoss)
        assert boss1.has_quirk("Meat Shield") is True
        assert boss2.has_quirk("Meat Shield") is True

        bear = scen.enemies[0]
        assert isinstance(bear, EliteEnemy)
        assert bear.wounds == 3
        assert bear.has_trait("Thick Blubber") is True

    def test_build_tomb_highwayman_scenario_package(self):
        from combat_sim.scenarios import build_tomb_highwayman, Scenario

        scen = build_tomb_highwayman()
        assert isinstance(scen, Scenario)
        assert scen.name == "Tomb of the Highwayman"
        assert len(scen.allies) == 2  # Boss Wizgog + Tomb Diggers Mob
        assert len(scen.enemies) == 3  # Highwayman + 2 Skeletons

        boss, mob = scen.allies
        assert isinstance(boss, GoblinBoss)
        assert boss.has_quirk("Push Luck") is True
        assert boss.main_hand is not None
        assert boss.main_hand.has_trait(WeaponTrait.BASHING) is True

        highwayman = scen.enemies[0]
        assert isinstance(highwayman, EliteEnemy)
        assert highwayman.has_trait("Parrying Buckler") is True


class TestScenarioRegistry:
    """Validate ScenarioRegistry registration, aliases, lookup, and error handling."""

    def test_registry_list_scenarios(self):
        from combat_sim.scenarios import list_scenarios, ScenarioRegistry

        scenarios = list_scenarios()
        assert "street_skirmish" in scenarios
        assert "maulers_den" in scenarios
        assert "tomb_highwayman" in scenarios
        assert ScenarioRegistry.is_registered("street_skirmish") is True

    def test_registry_get_scenario_by_key_and_alias(self):
        from combat_sim.scenarios import get_scenario

        scen1 = get_scenario("street_skirmish")
        assert scen1.name == "Street Skirmish"

        scen1_alias = get_scenario("Street Skirmish")
        assert scen1_alias.name == "Street Skirmish"

        scen2 = get_scenario("maulers_den")
        assert scen2.name == "The Mauler's Den"

        scen2_alias = get_scenario("The Mauler's Den")
        assert scen2_alias.name == "The Mauler's Den"

        scen3 = get_scenario("tomb_highwayman")
        assert scen3.name == "Tomb of the Highwayman"

        scen3_alias = get_scenario("Tomb of the Highwayman")
        assert scen3_alias.name == "Tomb of the Highwayman"

    def test_registry_fresh_instances_per_call(self):
        from combat_sim.scenarios import get_scenario

        scen_a = get_scenario("street_skirmish")
        scen_b = get_scenario("street_skirmish")
        # Ensure separate instances
        assert scen_a is not scen_b
        assert scen_a.allies[0] is not scen_b.allies[0]
        assert scen_a.topology is not scen_b.topology

    def test_registry_custom_registration(self):
        from combat_sim.scenarios import ScenarioRegistry, Scenario
        from combat_sim.domain.topology import TopologyGraph, Zone

        def custom_factory() -> Scenario:
            t = TopologyGraph()
            t.add_zone(Zone(id="z1", name="Zone 1"))
            return Scenario(
                name="Custom Test Encounter",
                description="Custom description",
                topology=t,
                allies=[],
                enemies=[],
            )

        ScenarioRegistry.register(
            name="custom_test_encounter",
            factory=custom_factory,
            description="Custom encounter description",
            aliases=["Custom Test", "custom"],
        )

        assert ScenarioRegistry.is_registered("custom_test_encounter") is True
        assert ScenarioRegistry.is_registered("Custom Test") is True

        loaded = ScenarioRegistry.get_scenario("custom")
        assert loaded.name == "Custom Test Encounter"

    def test_registry_unknown_scenario_raises_key_error(self):
        from combat_sim.scenarios import get_scenario

        with pytest.raises(KeyError, match="Unknown scenario 'non_existent_encounter'"):
            get_scenario("non_existent_encounter")

    def test_registry_list_scenario_details(self):
        from combat_sim.scenarios import ScenarioRegistry

        details = ScenarioRegistry.list_scenario_details()
        assert len(details) >= 3
        keys = [d["key"] for d in details]
        assert "street_skirmish" in keys
        assert "maulers_den" in keys
        assert "tomb_highwayman" in keys


class TestScenarioCombatSimulation:
    """Validate full end-to-end combat simulation execution for all reference scenarios."""

    def test_street_skirmish_simulation_runs_to_completion(self):
        import random
        from combat_sim.scenarios import get_scenario

        scen = get_scenario("street_skirmish")
        engine = scen.create_engine(rng=random.Random(42))
        summary = engine.run_to_completion(max_rounds=30)

        assert summary.scenario_name == "Street Skirmish"
        assert summary.total_rounds >= 1
        assert summary.victor in ("allies", "enemies", "draw")
        assert len(summary.round_summaries) == summary.total_rounds

    def test_maulers_den_simulation_runs_to_completion(self):
        import random
        from combat_sim.scenarios import get_scenario

        scen = get_scenario("maulers_den")
        engine = scen.create_engine(rng=random.Random(123))
        summary = engine.run_to_completion(max_rounds=30)

        assert summary.scenario_name == "The Mauler's Den"
        assert summary.total_rounds >= 1
        assert summary.victor in ("allies", "enemies", "draw")
        assert len(summary.round_summaries) == summary.total_rounds

    def test_tomb_highwayman_simulation_runs_to_completion(self):
        import random
        from combat_sim.scenarios import get_scenario

        scen = get_scenario("tomb_highwayman")
        engine = scen.create_engine(rng=random.Random(999))
        summary = engine.run_to_completion(max_rounds=30)

        assert summary.scenario_name == "Tomb of the Highwayman"
        assert summary.total_rounds >= 1
        assert summary.victor in ("allies", "enemies", "draw")
        assert len(summary.round_summaries) == summary.total_rounds

