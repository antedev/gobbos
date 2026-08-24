"""Reference Scenario 3: Tomb of the Highwayman.

Boss (Wizgog: Spiked Mace Bashing + Push Luck, Light Armor) + Size 3 Mob
vs Armored Highwayman (Elite, 2 Wounds, Defence 2, Parrying Buckler, Heavy Cleave)
and 2 Rattlebone Skeletons (Dry Bones) across a 2-zone crypt topology
(Crypt Antechamber with Slippery, Burial Vault with Shoring).
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
    StandardEnemy,
    ThreatAttack,
)
from combat_sim.domain.equipment import (
    create_light_armor,
    create_spiked_mace,
)
from combat_sim.domain.quirks import PushLuck
from combat_sim.domain.topology import TopologyGraph, Zone, ZoneProfile, ZoneTrait
from combat_sim.domain.traits import (
    DryBones,
    HumanoidAncestryTrait,
    ParryingBuckler,
    UndeadAncestryTrait,
)
from combat_sim.scenarios.registry import Scenario


def build_tomb_highwayman() -> Scenario:
    """Construct a fresh instance of the Tomb of the Highwayman reference scenario."""
    # 1. Topology (2 connected crypt zones)
    topo = TopologyGraph()
    z_ante = Zone(
        id="crypt_antechamber",
        name="Crypt Antechamber",
        profile=ZoneProfile(Difficulty.NORMAL, 1, "Slick stone flagstones"),
        traits=[ZoneTrait(ZoneTraitType.SLIPPERY, "Wet moss and slime on stones")],
    )
    z_vault = Zone(
        id="burial_vault",
        name="Burial Vault",
        profile=ZoneProfile(
            Difficulty.NORMAL, 2, "Decaying crypt supported by rotted timber"
        ),
        traits=[
            ZoneTrait(
                ZoneTraitType.SHORING, "Weak wooden beams can be collapsed"
            )
        ],
    )
    topo.add_zone(z_ante)
    topo.add_zone(z_vault)
    topo.connect("crypt_antechamber", "burial_vault")

    # 2. Allies (Boss Wizgog + Size 3 Mob with Light Armor)
    boss = GoblinBoss(
        id="wizgog",
        name="Boss Wizgog",
        zone_id="crypt_antechamber",
        tough=2,
        slink=3,
        mouth=2,
        brains=2,
        grunt=2,
        grit=4,
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

    # 3. Enemies (Armored Highwayman + 2 Rattlebone Skeletons)
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
            ThreatAttack(
                name="Broadsword",
                threat_stat="Tough",
                difficulty=Difficulty.NORMAL,
                threat_tn=2,
                damage=2,
            )
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
        attacks=[
            ThreatAttack(
                name="Notched Scimitar",
                threat_stat="Tough",
                difficulty=Difficulty.NORMAL,
                threat_tn=1,
                damage=1,
            )
        ],
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
        attacks=[
            ThreatAttack(
                name="Notched Scimitar",
                threat_stat="Tough",
                difficulty=Difficulty.NORMAL,
                threat_tn=1,
                damage=1,
            )
        ],
    )

    return Scenario(
        name="Tomb of the Highwayman",
        description=(
            "Boss (Wizgog: Spiked Mace Bashing + Push Luck, Light Armor) + Size 3 Mob "
            "vs Armored Highwayman (Elite, 2 Wounds, Defence 2, Parrying Buckler, Heavy Cleave) "
            "and 2 Rattlebone Skeletons (Dry Bones) across a 2-zone crypt topology "
            "(Crypt Antechamber with Slippery, Burial Vault with Shoring)."
        ),
        topology=topo,
        allies=[boss, mob],
        enemies=[highwayman, skel_a, skel_b],
    )


create_tomb_highwayman = build_tomb_highwayman
