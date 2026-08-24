# Changes Summary — Worker 2 (Milestone 2 Synthesis)

## Files Created & Modified

1. `02_PROD_Core_Rules/04_Zones_and_Movement.md`
   - **Domain**: Zones, Movement, and Environment.
   - **Systemic Mechanics**:
     - Zone topology and abstract node graph representation (Intra-Zone vs Inter-Zone distance, Macro Minimap vs Clash Cluster).
     - Universal Zone Profile rule (`Difficulty+/Target Number`) governing unlisted physical traversal and manipulation tests.
     - Movement action economy (1 Move = Movement rating in Zones for Bosses; 2 Zones for Mobs).
     - Disengagement tests (`Slink 5+/Highest Defence TN`) and Opportunity Attack penalties (halted movement, Bulk 3+ restriction).
     - Partial Cover (Bane 1 on ranged attack / Boon 1 on Dodge) vs Full Cover (blocks line of sight).
     - Modular Zone Traits and Environmental Hazards (Static obstacles, Dynamic hazards, Hazard Severity Tiers 1–3).
     - Standardized Environmental Blueprints (Blizzard, Thunderstorm, Smog Marsh, Tornado, Acid Mire).
     - Background Node Resolution via the Chaos Tick and Gobbo Mischief Table.
     - Standardized `[MISSING RULE / GAP]` callouts for vertical fall scaling and zone capacity limits.

2. `02_PROD_Core_Rules/05_Combat_Engine.md`
   - **Domain**: Combat Engine, Weaponry, Armor & Clatter Defense.
   - **Systemic Mechanics**:
     - Complete attack resolution pipeline (Melee `Tough` vs Defence TN; Ranged `Slink` vs Defence TN across 1–3 Zones).
     - Minion One-Hit Kill and Elite/Boss Overkill rule ($\lfloor \text{Successes} / \text{Defence TN} \rfloor$ Wounds).
     - Impact Size vs Target Size Stagger calculation on partial hits (stagger resistance vs mass).
     - Weapon traits (`Heavy`, `Crushing`, `Cleave X`, `Reach`, `Concealable`, `Versatile`, `Piercing`, `Bashing`) and Break Roll durability on Fumbles.
     - Formal Weapon Structural Schema with `[CONTENT EXTENSION POINT: Weapons]`.
     - Passive Armor Dice (+1d, +2d, +3d) with Slink Bane penalties, 5d6 mitigation ceiling, and Ablative Gear Sacrifice rule.
     - Shield mechanics enabling the active `Tough` Parry reaction.
     - Formal Armor & Shield Structural Schema with `[CONTENT EXTENSION POINT: Armor & Shields]`.
     - Tools (permissions, boons, difficulty shifts) and Consumables/Explosives Area Threat Profiles.
     - Formal Gear, Tools & Consumables Schema with `[CONTENT EXTENSION POINT: Gear, Tools & Consumables]`.
     - The Clatter Defense Roll (simultaneous throw of active Stat Dice and passive Armor Dice vs Threat TN).
     - Group Attacks (Enemy Swarms combining up to 3 minions into 1 strike) and Flanking/Crossfire boons.
     - Standardized `[MISSING RULE / GAP]` callouts for dual-wielding and ammunition tracking.

3. `02_PROD_Core_Rules/06_Mob_Mechanics.md`
   - **Domain**: Mob Mechanics, Swarm Health, Command Flow & Morale.
   - **Systemic Mechanics**:
     - Mob Anatomy and Size progression (Size 1–5, Combat Dice = Size, Required Grunt, Loot Capacity = Size x 4 Bulk, Over-Laden penalties).
     - Mob Equipment Bulk scaling (Armor = Size x Armor Bulk) and casualty shedding rules.
     - Health Dice Pool (physical d6s equal to Size starting at face 6) and damage resolution modes (Single-target decrement/spillover, Frontline Rule for Mob clashes, `Cleave X`, True AoE).
     - Boss Command Flow: Line of Sight, distance difficulty scaling, Free Orders, and the Boredom Rule.
     - Unordered Mob resolution: Loitering Table (1 action spent, 1 saved) vs Out of Control Table (2 actions spent, 0 saved), and Rallying rules.
     - Mob Defense & "Scatter!" Reaction (Boss `Mouth` vs Threat TN + Size penalty) with high-stakes Scatter Gamble consequences.
     - Morale Checks (50% casualty trigger) and the Swarm Terror pool test against enemy Morale TN.
     - Tactical Mob Splitting, Merging, and Cross-Gang Super-Mob In-Fighting.
     - Five official Mob Sacrifice Maneuvers (Gobbo Pyramid, Living Bridge, Canary Runt, Meat Cushion, Gnaw the Hinges).
     - Standardized `[MISSING RULE / GAP]` callouts for Mob weapon outfitting and Swarm Terror pool caps.
