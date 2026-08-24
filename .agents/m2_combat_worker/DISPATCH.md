## 2026-08-23T21:35:00Z
You are the Implementation Worker for Milestone 2: Dice & Core Combat Engine.
Your working directory is: c:\Users\ante\Documents\github\gobbos\.agents\m2_combat_worker\

Authoritative specifications and test contracts:
- c:\Users\ante\Documents\github\gobbos\.agents\ORIGINAL_REQUEST.md
- c:\Users\ante\Documents\github\gobbos\PROJECT.md
- c:\Users\ante\Documents\github\gobbos\TEST_INFRA.md
- c:\Users\ante\Documents\github\gobbos\TEST_READY.md
- c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_rules_0\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\spec_miner_gear_0\handoff.md
- c:\Users\ante\Documents\github\gobbos\.agents\explorer_scenarios_0\handoff.md

Mission:
Implement Milestone 2 in `05_System_Tools/combat_sim`:
1. `combat_sim/core/dice.py`:
   - `DiceResult` dataclass.
   - `roll_dice(pool_size: int, difficulty: Difficulty, tn: int = 1, allow_gamble: bool = False, is_salvage: bool = False, rng: Optional[random.Random] = None) -> DiceResult`:
     - D6 dice pool tests vs Easy 4+, Normal 5+, Hard 6.
     - Exploding 6s recursion (every natural 6 adds 1 success and rolls another regular die).
     - Critical double-explosions (consecutive 6s grant +1 Grunt and free non-offensive action).
     - Salvage rolls (if pool <= 0d6, roll 1d6: 6=1 success [no explosion], 1=fumble, 2-5=fail).
     - Gobbo Gamble (on failed tests with 1s, reroll all 1s; continuing failure causes Fumble & -1 Grunt).
   - `BangarangaPool` class: communal dice seeding, draw up to Grunt, tax if drawn > TN, double-exploding 6s, drainage on 1s.
   - `resolve_clatter(threat_tn: int, stat_dice: int, difficulty: Difficulty, armor_dice: int, incoming_damage: int = 1, can_dodge_or_parry: bool = True, rng: Optional[random.Random] = None) -> ClatterResult`.
2. `combat_sim/engine/__init__.py`.
3. `combat_sim/engine/resolver.py`:
   - `AttackResolver`: Melee attack, Ranged attack, Impact Size Stagger calculation (Impact Size >= Target Size), Overkill wound conversion (floor(Successes / Defence TN)), Mob health decrement with single-target spillover, and AoE / Cleave simultaneous multi-die damage.
   - `ClatterResolver`: Active Slink Dodge / Tough Parry vs Threat TN, passive Armor mitigation on 5+, Ablative gear sacrifice on lethal damage, Meat Shield redirection.
   - `MobReactionResolver`: Mob "Scatter!" reaction (Boss Mouth vs Threat TN + Size - 1, clean move vs Gamble trample disaster: 1 AoE trample damage to all dice + drop 1 loot + out of control + Boss Stagger).
   - `HazardResolver` & `MoraleResolver`: Zone hazard tests (Slippery, Burning, Toxic Spores, Rubble, Shoring collapse), End of Round fire spread (5-6 on 1d6), 50% casualty Swarm Terror Morale checks.
4. `combat_sim/engine/ai.py`:
   - Tactical AI for Bosses (action budgeting, Movement, Melee/Ranged targeting, Quirk activations, holding reactions for Clatter/Scatter).
   - Mob AI (ordered actions obeying Boredom rule, Loitering table d6, Out-of-Control table d6).
   - Enemy AI (deterministic target selection, Group Attack swarm combining up to 3 on Boss, Mob focus, trait activations).
5. `combat_sim/engine/combat.py`:
   - `CombatEngine`, `CombatState`, `RoundSummary`, `CombatSummary`.
   - Complete 5-phase combat loop (Setup, Round Start, Player Active Turn, Enemy Active Turn, Round Closure, Combat End).
