"""Reference Scenario 1: Street Skirmish.

Armored Boss (Garg: Sword + Shield + Ankle Bite, Medium Armor) + Size 3 Mob
vs Robber Gang (Enemy Mob Size 3) and 2 Footpads (Footpad A with Rusty Shiv,
Footpad B with Thrown Cobblestone) across a 3-zone street topology
(Street West, Street Center with Partial Cover, Alley East with Narrow).
"""

from __future__ import annotations

from combat_sim.core.types import (
    CoverType,
    Difficulty,
    ZoneTraitType,
)
from combat_sim.domain.entities import (
    EnemyMob,
    GoblinBoss,
    PlayerMob,
    StandardEnemy,
    ThreatAttack,
)
from combat_sim.domain.equipment import (
    create_medium_armor,
    create_notched_sword,
    create_pot_lid_shield,
)
from combat_sim.domain.quirks import AnkleBite
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.scenarios.registry import Scenario


def build_street_skirmish() -> Scenario:
    """Construct a fresh instance of the Street Skirmish reference scenario."""
    # 1. Topology (3 connected zones)
    topo = TopologyGraph()
    z_west = Zone(
        id="street_west",
        name="Street West",
        profile=ZoneProfile(Difficulty.NORMAL, 1, "Cobblestone street opening"),
    )
    z_center = Zone(
        id="street_center",
        name="Street Center",
        profile=ZoneProfile(Difficulty.NORMAL, 1, "Market stalls and barricades"),
        cover=CoverType.PARTIAL,
    )
    z_east = Zone(
        id="alley_east",
        name="Alley East",
        profile=ZoneProfile(Difficulty.NORMAL, 1, "Cramped alleyway"),
        traits=[ZoneTrait(ZoneTraitType.NARROW, "Narrow passage limits large mobs")],
    )
    topo.add_zone(z_west)
    topo.add_zone(z_center)
    topo.add_zone(z_east)
    topo.connect("street_west", "street_center")
    topo.connect("street_center", "alley_east")

    # 2. Allies (Armored Boss Garg + Size 3 Mob)
    boss = GoblinBoss(
        id="garg",
        name="Boss Garg",
        zone_id="street_west",
        tough=2,
        slink=2,
        mouth=2,
        brains=1,
        grunt=2,
        grit=4,
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

    # 3. Enemies (Robber Gang + 2 Footpads)
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
        attacks=[
            ThreatAttack(
                name="Rusty Shiv",
                threat_stat="Slink",
                difficulty=Difficulty.NORMAL,
                threat_tn=1,
                damage=1,
            )
        ],
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
                difficulty=Difficulty.NORMAL,
                threat_tn=1,
                damage=1,
                range_zones=1,
            )
        ],
    )

    return Scenario(
        name="Street Skirmish",
        description=(
            "Armored Boss (Garg: Sword + Shield + Ankle Bite, Medium Armor) + Size 3 Mob "
            "vs Robber Gang (Enemy Mob Size 3) and 2 Footpads (Footpad A with Rusty Shiv, "
            "Footpad B with Thrown Cobblestone) across a 3-zone street topology "
            "(Street West, Street Center with Partial Cover, Alley East with Narrow)."
        ),
        topology=topo,
        allies=[boss, mob],
        enemies=[robber_gang, footpad_a, footpad_b],
    )


create_street_skirmish = build_street_skirmish
