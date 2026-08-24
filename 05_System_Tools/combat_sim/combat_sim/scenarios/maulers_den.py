"""Reference Scenario 2: The Mauler's Den.

2 Bosses (Skag: 2H Greataxe + Meat Shield, Grub: 2H Greatclub + Meat Shield, Light Armor)
+ 2 Mobs (Size 2 & Size 3) vs Forest Mauler (Elite Bear, 3 Wounds, Defence 2,
Thick Blubber, Crushing Claws Cleave) across a 2-zone cave topology
(Den Entrance Narrow, Main Den with Rubble and Pillars).
"""

from __future__ import annotations

from combat_sim.core.types import (
    Ancestry,
    Difficulty,
    ZoneTraitType,
)
from combat_sim.domain.entities import (
    EliteEnemy,
    GoblinBoss,
    PlayerMob,
    ThreatAttack,
)
from combat_sim.domain.equipment import (
    create_heavy_greataxe,
    create_light_armor,
)
from combat_sim.domain.quirks import MeatShield
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import BeastAncestryTrait, ThickBlubber
from combat_sim.scenarios.registry import Scenario


def build_maulers_den() -> Scenario:
    """Construct a fresh instance of The Mauler's Den reference scenario."""
    # 1. Topology (2 connected cave zones)
    topo = TopologyGraph()
    z_entrance = Zone(
        id="den_entrance",
        name="Den Entrance",
        profile=ZoneProfile(Difficulty.NORMAL, 2, "Narrow cave opening"),
        traits=[ZoneTrait(ZoneTraitType.NARROW, "Cramped tunnel limits large mobs")],
    )
    z_main = Zone(
        id="main_den",
        name="Main Den",
        profile=ZoneProfile(Difficulty.NORMAL, 2, "Cavern with massive stalagmites"),
        traits=[
            ZoneTrait(ZoneTraitType.RUBBLE, "Shattered stone slows movement"),
            ZoneTrait(ZoneTraitType.PILLARS, "Natural stone columns provide cover"),
        ],
    )
    topo.add_zone(z_entrance)
    topo.add_zone(z_main)
    topo.connect("den_entrance", "main_den")

    # 2. Allies (2 Heavy Weapon Bosses with Meat Shield + 2 Mobs)
    boss1 = GoblinBoss(
        id="skag",
        name="Boss Skag",
        zone_id="den_entrance",
        tough=3,
        slink=1,
        mouth=2,
        brains=1,
        grunt=2,
        grit=4,
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
        grit=4,
        main_hand=create_heavy_greataxe(),
        armor=create_light_armor(),
        quirks=[MeatShield()],
    )

    mob1 = PlayerMob(
        id="mob_skag",
        name="Skag's Boyz",
        zone_id="den_entrance",
        size=2,
        boss_id="skag",
    )

    mob2 = PlayerMob(
        id="mob_grub",
        name="Grub's Crew",
        zone_id="den_entrance",
        size=3,
        boss_id="grub",
    )

    # 3. Enemies (Forest Mauler: Elite Cave Bear)
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

    return Scenario(
        name="The Mauler's Den",
        description=(
            "2 Bosses (Skag: 2H Greataxe + Meat Shield, Grub: 2H Greatclub + Meat Shield, Light Armor) "
            "+ 2 Mobs (Size 2 & Size 3) vs Forest Mauler (Elite Bear, 3 Wounds, Defence 2, "
            "Thick Blubber, Crushing Claws Cleave) across a 2-zone cave topology "
            "(Den Entrance Narrow, Main Den with Rubble and Pillars)."
        ),
        topology=topo,
        allies=[boss1, boss2, mob1, mob2],
        enemies=[bear],
    )


create_maulers_den = build_maulers_den
