"""Core dice rolling engine for the Gobbos tactical combat simulation.

Implements:
- D6 dice pool tests against difficulty thresholds (Easy 4+, Normal 5+, Hard 6).
- Recursive exploding 6s (every natural 6 adds 1 success and rolls an extra regular d6).
- Critical Double Explosions (consecutive 6s on bonus dice).
- Salvage rolls (1d6 when pool <= 0d6: 6=1 success, 1=fumble, 2-5=fail).
- Gobbo Gamble (rerolling 1s on failed tests, with continuing failure causing Fumble).
- Bangaranga communal dice pool mechanics (seeding, tax, double explosions, failure drain).
- Clatter roll defense (active evasion vs passive armor mitigation).
"""

from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import List, Optional

from combat_sim.core.types import Difficulty


def roll_d6(rng: Optional[random.Random] = None) -> int:
    """Roll a single discrete six-sided die."""
    if rng is not None:
        return rng.randint(1, 6)
    return random.randint(1, 6)


@dataclass
class DiceResult:
    """Encapsulates the complete outcome of a Gobbos dice pool roll."""
    successes: int = 0
    faces: List[int] = field(default_factory=list)
    bonus_faces: List[int] = field(default_factory=list)
    is_critical: bool = False
    fumble: bool = False
    salvage: bool = False
    gambled: bool = False
    tn: int = 1

    @property
    def is_success(self) -> bool:
        """True if total successes meet or exceed the Target Number (TN)."""
        return self.successes >= self.tn


@dataclass
class BangarangaOutcome:
    """Outcome of resolving a Bangaranga-assisted test."""
    grunt_loss: int = 0
    pool_drained: int = 0


@dataclass
class BangarangaPool:
    """Communal pool of Bangaranga dice shared across the goblin party."""
    initial_dice: int = 0
    available_dice: int = field(init=False)

    def __post_init__(self):
        self.available_dice = max(0, self.initial_dice)

    def seed(self, count: int) -> None:
        """Add dice to the communal Bangaranga pool."""
        self.available_dice += max(0, count)

    def draw(self, count: int, tn: int = 1) -> int:
        """Draw Bangaranga dice up to available limit with tax if drawn > tn."""
        if count <= 0 or self.available_dice <= 0:
            return 0

        # Tax: if drawn count > TN, costs 1 extra discarded die
        tax = 1 if count > tn else 0
        total_required = count + tax

        if self.available_dice >= total_required:
            self.available_dice -= total_required
            return count
        elif self.available_dice > tax:
            # Draw as many as possible after paying tax if applicable
            drawn = self.available_dice - tax if self.available_dice > tax else self.available_dice
            self.available_dice = 0
            return drawn
        else:
            return 0

    def roll_bangaranga_test(
        self,
        drawn_dice: int,
        difficulty: Difficulty = Difficulty.NORMAL,
        tn: int = 1,
        rng: Optional[random.Random] = None,
    ) -> DiceResult:
        """Roll Bangaranga dice where every natural 6 explodes TWICE into 2 bonus dice."""
        if drawn_dice <= 0:
            return DiceResult(successes=0, faces=[], bonus_faces=[], tn=tn)

        faces: List[int] = [roll_d6(rng) for _ in range(drawn_dice)]
        bonus_faces: List[int] = []
        successes = sum(1 for f in faces if difficulty.meets_threshold(f))
        is_critical = False

        for f in faces:
            if f == 6:
                # Double explosion: 2 regular bonus dice
                for _ in range(2):
                    bonus_die = roll_d6(rng)
                    bonus_faces.append(bonus_die)
                    if difficulty.meets_threshold(bonus_die):
                        successes += 1
                    if bonus_die == 6:
                        is_critical = True
                        # Bonus die explodes recursively as normal
                        curr_bonus = bonus_die
                        while curr_bonus == 6:
                            next_bonus = roll_d6(rng)
                            bonus_faces.append(next_bonus)
                            if difficulty.meets_threshold(next_bonus):
                                successes += 1
                            curr_bonus = next_bonus

        return DiceResult(
            successes=successes,
            faces=faces,
            bonus_faces=bonus_faces,
            is_critical=is_critical,
            fumble=False,
            salvage=False,
            gambled=False,
            tn=tn,
        )

    def resolve_test_outcome(
        self,
        drawn_dice: int,
        faces: List[int],
        successes: int,
        tn: int = 1,
    ) -> BangarangaOutcome:
        """Evaluate penalty consequences if a Bangaranga-assisted test failed."""
        grunt_loss = 0
        pool_drained = 0

        if successes < tn:
            grunt_loss = 1
            if 1 in faces:
                pool_drained = drawn_dice

        return BangarangaOutcome(grunt_loss=grunt_loss, pool_drained=pool_drained)


def roll_dice(
    pool_size: int,
    difficulty: Difficulty = Difficulty.NORMAL,
    tn: int = 1,
    allow_gamble: bool = False,
    is_salvage: bool = False,
    exploding: bool = True,
    rng: Optional[random.Random] = None,
) -> DiceResult:
    """Execute a Gobbos d6 dice pool roll according to core system rules."""
    # Salvage Roll: pool <= 0 or explicit salvage flag
    if pool_size <= 0 or is_salvage:
        face = roll_d6(rng)
        if face == 6:
            # 6 grants exactly 1 success and does NOT explode
            return DiceResult(
                successes=1,
                faces=[face],
                bonus_faces=[],
                is_critical=False,
                fumble=False,
                salvage=True,
                gambled=False,
                tn=tn,
            )
        elif face == 1:
            # 1 causes a Fumble
            return DiceResult(
                successes=0,
                faces=[face],
                bonus_faces=[],
                is_critical=False,
                fumble=True,
                salvage=True,
                gambled=False,
                tn=tn,
            )
        else:
            # 2-5 is normal failure
            return DiceResult(
                successes=0,
                faces=[face],
                bonus_faces=[],
                is_critical=False,
                fumble=False,
                salvage=True,
                gambled=False,
                tn=tn,
            )

    # Standard Pool Roll: roll all initial dice first
    faces: List[int] = [roll_d6(rng) for _ in range(pool_size)]
    bonus_faces: List[int] = []
    successes = sum(1 for f in faces if difficulty.meets_threshold(f))
    is_critical = False

    if exploding:
        for f in faces:
            if f == 6:
                # Exploding 6 recursion
                bonus_die = roll_d6(rng)
                bonus_faces.append(bonus_die)
                if difficulty.meets_threshold(bonus_die):
                    successes += 1
                if bonus_die == 6:
                    is_critical = True

                curr = bonus_die
                while curr == 6:
                    next_die = roll_d6(rng)
                    bonus_faces.append(next_die)
                    if difficulty.meets_threshold(next_die):
                        successes += 1
                    curr = next_die

    # Check for Gobbo Gamble (pushing 1s on failed tests)
    gambled = False
    fumble = False

    if allow_gamble and successes < tn and 1 in faces:
        gambled = True
        # Keep non-1 dice
        kept_faces = [f for f in faces if f != 1]
        reroll_count = faces.count(1)

        # Roll new faces for the rerolled 1s
        rerolled_faces = [roll_d6(rng) for _ in range(reroll_count)]
        new_faces: List[int] = list(kept_faces) + rerolled_faces
        new_bonus_faces: List[int] = list(bonus_faces)
        new_successes = successes  # successes came from kept faces/bonus faces

        for rf in rerolled_faces:
            if difficulty.meets_threshold(rf):
                new_successes += 1
            if exploding and rf == 6:
                bonus_die = roll_d6(rng)
                new_bonus_faces.append(bonus_die)
                if difficulty.meets_threshold(bonus_die):
                    new_successes += 1
                if bonus_die == 6:
                    is_critical = True

                curr = bonus_die
                while curr == 6:
                    next_die = roll_d6(rng)
                    new_bonus_faces.append(next_die)
                    if difficulty.meets_threshold(next_die):
                        new_successes += 1
                    curr = next_die

        faces = new_faces
        bonus_faces = new_bonus_faces
        successes = new_successes

        # If still failing TN after gamble -> Fumble
        if successes < tn:
            fumble = True

    return DiceResult(
        successes=successes,
        faces=faces,
        bonus_faces=bonus_faces,
        is_critical=is_critical,
        fumble=fumble,
        salvage=False,
        gambled=gambled,
        tn=tn,
    )


@dataclass
class ClatterResult:
    """Detailed resolution breakdown of an incoming Clatter defense roll."""
    evaded: bool = False
    stat_successes: int = 0
    armor_successes: int = 0
    mitigated_damage: int = 0
    damage_taken: int = 0
    stat_faces: List[int] = field(default_factory=list)
    armor_faces: List[int] = field(default_factory=list)


def resolve_clatter(
    threat_tn: int,
    stat_dice: int,
    difficulty: Difficulty,
    armor_dice: int,
    incoming_damage: int = 1,
    can_dodge_or_parry: bool = True,
    rng: Optional[random.Random] = None,
) -> ClatterResult:
    """Resolve a unified Clatter Roll defense against an incoming deterministic threat.

    1. Active Evasion (Slink Dodge / Tough Parry):
       If saved action available and stat_dice > 0:
       Roll stat_dice vs threat_tn at difficulty.
       If successes >= threat_tn: Clean Dodge/Parry -> 0 damage taken.
    2. Passive Mitigation:
       If evasion fails or no active defense:
       Roll armor_dice vs Normal 5+ (each 5+ mitigates 1 damage; armor dice do not explode).
       Remaining damage reduces Grit/Health.
    """
    incoming_damage = max(0, incoming_damage)
    stat_faces: List[int] = []
    stat_successes = 0

    # Step 1: Active Evasion
    if can_dodge_or_parry and stat_dice > 0:
        stat_res = roll_dice(
            pool_size=stat_dice,
            difficulty=difficulty,
            tn=threat_tn,
            allow_gamble=False,
            rng=rng,
        )
        stat_successes = stat_res.successes
        stat_faces = stat_res.faces + stat_res.bonus_faces

        if stat_successes >= threat_tn:
            # Clean Dodge / Parry: Completely evades attack
            return ClatterResult(
                evaded=True,
                stat_successes=stat_successes,
                armor_successes=0,
                mitigated_damage=incoming_damage,
                damage_taken=0,
                stat_faces=stat_faces,
                armor_faces=[],
            )

    # Step 2: Passive Armor Mitigation (Armor dice do not explode)
    armor_faces: List[int] = []
    armor_successes = 0

    if armor_dice > 0:
        armor_faces = [roll_d6(rng) for _ in range(armor_dice)]
        armor_successes = sum(1 for f in armor_faces if f >= 5)

    mitigated = min(incoming_damage, armor_successes)
    damage_taken = max(0, incoming_damage - armor_successes)

    return ClatterResult(
        evaded=False,
        stat_successes=stat_successes,
        armor_successes=armor_successes,
        mitigated_damage=mitigated,
        damage_taken=damage_taken,
        stat_faces=stat_faces,
        armor_faces=armor_faces,
    )
