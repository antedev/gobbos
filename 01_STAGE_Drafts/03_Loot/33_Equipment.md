# Equipment & Gear

*A goblin's life is short, violent, and cheap, but good gear makes it loud and glorious. Whether swinging a sharpened shovel, hiding behind a dented wash-tub, or hauling a stolen cannon, your gear is the difference between a dead runt and a living Boss. Take everything that is not nailed down, and bring a crowbar for the rest.*

---

## The Equipment Framework

Every physical item in the game—from a rusty shiv plucked from a mud puddle to a masterwork dwarven breastplate—is built upon a single unified foundation called the **Base Chassis**. 

Equipment in **Gobbos** serves two distinct purposes:
1. **Immediate Tactical Utility:** Mundane gear provides immediate survival tools, offensive reach, passive armor mitigation, and test difficulty adjustments during raids.
2. **The Crafting Foundation:** Every piece of mundane gear functions as an un-upgraded **Base Chassis** for the crafting system (see [Crafting & Custom Gear](34_Crafting.md)). When you attach volatile components to gear between raids, the item retains its underlying chassis stats while gaining explosive new powers.

>> **GOLDEN RULE: No Math Bloat**
>> Equipment never adds awkward `+1` or `+2` arithmetic to die faces after a roll. Equipment modifies your tests in three clean ways: adding dice to your pool (**Boon 1 (+1d)**, **Boon 2 (+2d)**), shifting the test Difficulty (**Hard (6)** -> **Normal (5+)** -> **Easy (4+)**), or increasing your **Impact Size** to stagger heavy targets.

---

## Base Item Attributes

Every item is defined by five core mechanical properties:

### 1. Classification & Category
*   **Melee Weapon:** Wielded in close combat within the same [[Zone]], rolling [[Tough]] to attack.
*   **Ranged Weapon:** Fired across 1 or more [[Zones]], rolling [[Slink]] to attack.
*   **Armor:** Worn protective clothing providing passive mitigation dice in the [[Clatter Roll]].
*   **Shield:** Held defensive barrier providing passive mitigation dice and enabling the [[Parry]] [[Reaction]].
*   **Tool & Utility:** Functional gear used to overcome obstacles, pick locks, or manipulate the environment.
*   **Consumable:** Single-use items (potions, explosives, alchemical flasks) that produce an immediate effect and are destroyed upon use.
*   **Loot & Treasure:** Plunder scavenged during raids. It has high [[Loot Value]] and heavy [[Bulk]], but no combat function.

### 2. Bulk & Handedness
[[Bulk]] measures an item's weight, awkward size, and physical encumbrance.
*   **Bulk 0 (Negligible):** Tiny objects (lockpicks, coins, rings, loose blueprints). Carried freely in pouches and pockets.
*   **Bulk 1 (Light / Compact):** One-handed weapons, daggers, bucklers, light armor, single grenades, crowbars. Easily strapped to a belt or shoulder sling.
*   **Bulk 2 (Medium / Standard):** Shortswords, maces, shortbows, crossbows, medium armor, heavy toolkits. Standard expedition gear.
*   **Bulk 3 (Heavy / Bulky):** Greataxes, two-handed polearms, heavy arbalests, heavy plate armor, treasure chests, powder kegs. Highly taxing to carry; requires **two hands** to haul or wield in combat.
*   **Bulk 4+ (Massive / Obscene):** Stolen statues, siege engine parts, giant iron cauldrons. Cannot be packed in a bag; must be dragged or carried collectively by a [[Mob]].

**Handedness & Slots:**
*   **Worn:** Fitted to the body (e.g., 1 suit of Armor). Does not occupy hands.
*   **One-Handed (1H):** Requires 1 hand to wield. Leaves your other hand free to hold a shield, torch, ladder, or piece of [[Loot]].
*   **Two-Handed (2H):** Requires both hands to wield effectively in combat. You cannot hold another item or weapon while attacking.
*   **Stowed:** Packed inside a sack, pack, or pocket. Drawing a stowed weapon or item takes a [[Free Action]] (once per turn) or a [[Manipulate]] action.

### 3. Quality & Durability
Every mundane item belongs to a **Quality Tier** (T1 to T5). This rating determines the item's physical resilience when you push it beyond its limits:

| Quality Tier | Equivalent Level | Typical Materials & Origin | Base Purchase Cost | Break Roll on Fumble |
| :---: | :---: | :--- | :---: | :---: |
| **T1** | [[Junk]] | Splintered wood, brittle bones, rusted wire, scrap metal. | Free / 1x T1 | Breaks on **1–4** |
| **T2** | [[Scrappy]] | Rough-hammered goblin forge-iron, boiled hide, cobbled tools. | **1x T2** *(or 5x T1)* | Breaks on **1–3** |
| **T3** | [[Standard]] | Proper human military steel, cured leather, dwarven surplus. | **1x T3** *(or 5x T2)* | Breaks on **1–2** |
| **T4** | [[Superior]] | Mastercrafted alloys, tempered rune-steel, hardened carapace. | **1x T4** *(or 5x T3)* | Breaks on **1** |
| **T5** | [[Legendary]] | Mythic godstone, relic forge-alloys, ancient titan bone. | **1x T5** *(or 5x T4)* | **Never breaks** |

#### Durability & The Break Roll
Mundane equipment does not wear down from regular hits. An item is only tested when you suffer a [[Fumble]] on a test using that item (rolling multiple 1s without scoring sufficient successes, as detailed in [Dice](../00_Rules/01_Dice.md#1s-and-fumbles)).

When you Fumble a test using an item:
1. Roll a single **1d6** for the **Break Roll**.
2. Compare the result to the item's Quality threshold in the table above.
3. **If the roll is higher than the threshold:** The item holds together, though it might spark, crack, or rattle alarmingly.
4. **If the roll is equal to or below the threshold:** The item snaps, shatters, or crumples into useless debris. It is permanently broken and reduced to 0 Bulk scrap.

### 4. Action Economy of Gear
*   **Passive:** Operates automatically at all times without costing actions (e.g., passive armor mitigation dice).
*   **Standard Action:** Requires spending 1 [[Standard Action]] to use, swing, shoot, or activate.
*   **Reaction:** Usable out-of-turn in response to an enemy trigger (e.g., a [[Parry]] with a shield), costing 1 saved [[Standard Action]].
*   **Free Action:** Dropping a held item, or drawing/sheathing 1 light item (Bulk 0–1) once per turn.

---

## Weapons

Weapons allow a [[Goblin Boss]] or [[Mob]] to inflict damage, defeat enemies, and throw monsters off balance.

### Melee Weapons
All melee attacks roll a [[Dice Pool]] based on your [[Tough]] stat against the target's [[Defence]] TN. 

Melee weapons have an **Impact Size**. If your attack scores at least 1 success but falls short of the target's [[Defence]] TN, the strike does not deal damage, but it can inflict the [[Staggered]] condition if the weapon's **Impact Size** is equal to or greater than the target's physical [[Size]] (Impact Size >= Target Size).

| Weapon Category | Bulk | Hands | Base Impact Size | Special Capabilities & Traits |
| :--- | :---: | :---: | :---: | :--- |
| **Unarmed / Improvised** | 0 | 1H | Size 0 | *Crude:* Breaks on any Fumble regardless of Quality. Cannot stagger targets of Size 1+. |
| **Light Melee** *(Dagger, Shiv, Handaxe, Club, Cleaver)* | 1 | 1H | Wielder Size | *Concealable:* Can be drawn as an incidental Free Action. Bulk 1 allows carrying multiple sidearms. |
| **Medium Melee** *(Shortsword, Spiked Mace, Spear, Flail)* | 2 | 1H | Wielder Size | *Versatile:* Balanced one-handed profile. Leaves an off-hand free for a Shield or Loot. |
| **Heavy Melee** *(Greataxe, Greatclub, Halberd, War-pick)* | 3 | 2H | Wielder Size + 1 | `Heavy`: Adds **+1 to Impact Size** when attacking. Requires 2 hands; cannot hold a shield. |

### Ranged Weapons
All ranged attacks roll a [[Dice Pool]] based on your [[Slink]] stat against the target's [[Defence]] TN. Ranged combat measures distance across discrete [[Zones]].

| Ranged Weapon | Bulk | Hands | Range | Requirements | Special Capabilities & Traits |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Sling / Thrown Knives** | 1 | 1H | 1 Zone | None | *Scavenged Ammo:* Ammo is assumed freely available in any zone. Compact Bulk 1. |
| **Shortbow** | 2 | 2H | 2 Zones | None | *Rapid Fire:* Standard two-handed goblin bow. Fires across 2 zones without penalty. |
| **Crossbow** | 2 | 2H | 2 Zones | [[Brains]] 2 | *Mechanical Crank:* Requires mechanical understanding to reload smoothly under pressure. |
| **Heavy Crossbow / Arbalest** | 3 | 2H | 3 Zones | [[Tough]] 2, [[Brains]] 2 | `Heavy`: Long range (3 Zones). Requires massive physical strength and winch knowledge to operate. |

---

## Armor & Shields

Armor keeps goblins alive when dodging fails. Armor operates entirely through the **[[Clatter Roll]]** (see [Combat](../00_Rules/02%20Combat.md#dodge--parry-reaction--the-clatter-roll)).

### Passive Armor Dice
When you are targeted by an attack and fail your active [[Dodge]] or [[Parry]] evasion (or have no saved actions left to react), you roll your **Passive Armor Dice** (using distinct colored dice):
*   Every success (**5+**) rolled on your Armor Dice reduces the incoming Damage by 1.
*   Any remaining unmitigated damage is deducted directly from your [[Grit]].

| Armor Type | Bulk | Passive Armor Dice | Mobility Penalties | Special Properties |
| :--- | :---: | :---: | :--- | :--- |
| **Unarmored** | 0 | +0d | None | Maximum agility. 0 Bulk footprint. |
| **Light Armor** *(Padded cloth, Cured leather, Quilted hides)* | 1 | **+1d** | None | Silent and flexible; no stealth or movement penalties. |
| **Medium Armor** *(Chain shirt, Scaled reptile hide, Scrap-plate)* | 2 | **+2d** | **Bane 1 (-1d)** on [[Slink]] tests | Heavy metal links or stiff plates impose a Bane on stealth and acrobatics. |
| **Heavy Armor** *(Full Knight Plate, Dwarven Iron Carapace)* | 3 | **+3d** | **Bane 2 (-2d)** on [[Slink]] tests; cannot swim | Massive steel protection; noisy and exhausting. Sinks like a stone in water. |
| **Shield** *(Spiked Pot Lid, Wooden Pavise, Iron Buckler)* | 1 | **+1d** | Requires 1 Hand | Adds **+1d Armor Die** to your mitigation pool AND enables the **[[Parry]] [[Reaction]]** using [[Tough]]. |

### Optional Rule: Ablative Shield & Armor Sacrifice
When an incoming strike would deal enough unmitigated damage to reduce your [[Grit]] to 0 (or inflict a lethal wound), a [[Goblin Boss]] may declare an immediate **Gear Sacrifice**:
*   **The Shatter:** Your equipped Shield or Armor suit is violently and permanently destroyed on the spot, reduced to worthless shrapnel.
*   **The Salvation:** The destroyed piece of gear absorbs the blow completely, reducing the incoming attack's damage for that strike to **0**.
*   *(Note: This desperate tactic applies strictly to PC Bosses. Mobs do not track individual ablative equipment).*

---

## Tools & Mundane Utility

Tools allow goblins to bypass deadly obstacles, breach reinforced doors, and manipulate hazardous machinery.

>> **DESIGN MANDATE: Difficulty & Permission**
>> Tools never grant "+1 flat math modifiers." Instead, they either **step test Difficulty down** (e.g. from Hard to Normal), grant **Boon 1 (+1d)**, or grant **Narrative Permission** to perform an action that would otherwise be impossible.

| Tool / Item | Bulk | Primary Function & Mechanical Rule |
| :--- | :---: | :--- |
| **Quality Lockpicks** | 0 | *Precision Tension:* Reduces lockpicking and trap-disarming tests from **Hard (6)** to **Normal (5+)**, or from **Normal (5+)** to **Easy (4+)**. |
| **Crowbar / Pry-bar** | 1 | *Mechanical Leverage:* Grants **Boon 1 (+1d)** to [[Tough]] tests made to force heavy doors, pry open treasure chests, or unseat iron portcullises. |
| **Rope & Grappling Hook** (30 ft) | 1 | *Vertical Access:* Allows climbing sheer vertical surfaces without making hazard tests. Can also be thrown 1 Zone to snag and pull unattended Bulk 1–2 items. |
| **Lantern & Oil Flask** | 1 | *Illumination:* Strips the `[Dark]` tag from your current [[Zone]] for 1 exploration phase or combat encounter. Provides the `[Light]` tag. |
| **Heavy Iron Shackles & Key** | 1 | *Restraint:* Can be locked onto an incapacitated or willing target to inflict the `[Restrained]` condition. Escaping without a key requires a `Slink 5+/2` test. |
| **Chalk & Marking Grease** | 0 | *Dungeon Mapping:* Leaves glowing or greasy symbols on stone walls, granting **Boon 1 (+1d)** on [[Route Test|Route Tests]] when navigating complex labyrinths. |
| **Scent-Masking Paste** | 0 | *Pungent Odor:* Smearing yourself with foul sludge grants **Boon 1 (+1d)** to [[Slink]] stealth tests against beasts that hunt by scent. |

---

## Consumables & Explosives

Consumables are single-use devices that trigger instantaneous effects and are consumed in the process.

### Explosives & Area Hazards
Explosives, alchemical bombs, and environmental blast traps do not roll standard single-target weapon attacks. Instead, they produce an **Area Threat Profile** that affects every target within their blast [[Zone]].

| Explosive Device | Quality | Bulk | Area Threat Profile | Blast Range | Impact Size & Environmental Effects |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **T1 Spark Bomb** | T1 | 1 | `Threat 4+/1`, 1 Damage, `[Explosive]` | Current Zone | **Impact Size 1:** Staggers Size 1 targets. Rattles windows, ignites dry leaves. |
| **T2 Fire Flask (Molotov)** | T2 | 1 | `Threat 5+/1`, 2 Damage, `[Fire]` | 1 Zone | **Impact Size 2:** Staggers up to Size 2. Fills Zone with fire (`[Burning]`). |
| **T2 Choking Smoke Pot** | T2 | 1 | `Threat 4+/1`, 0 Damage, `[Gaseous]` | 1 Zone | **Impact Size 0:** Fills Zone with dense fog (`[Dark]`), imposing **Bane 1 (-1d)** on ranged attacks. |
| **T3 Powder Keg** | T3 | 2 | `Threat 5+/2`, 3 Damage, `[Explosive]` | 1 Zone | **Impact Size 3:** Staggers up to Size 3. Shatters wooden doors and breaches stone barricades. |
| **T4 Siege Mortar Shell** | T4 | 3 | `Threat 5+/3`, 4 Damage, `[Explosive]` | 2 Adjacent Zones | **Impact Size 4:** Staggers monsters and war-wagons. Demolishes fortified stone masonry. |
| **T5 Sol-Quartz Core** | T5 | 4 | `Threat 6/3`, 5 Damage, `[Explosive]` | Full Quadrant | **Impact Size 5:** Staggers colossal titans. Obliterates all structures and incinerates cover. |

#### Using an Explosive in Combat
*   **Throwing / Placing:** Spending 1 [[Standard Action]] allows you to throw an explosive up to **1 Zone away** or place it at your feet with a lit fuse. Throwing under heavy enemy pressure or into tight cover requires a `Slink 5+/1` test; on a failure, the bomb scatters into an adjacent zone or detonates early.
*   **Enemy Usage:** If an enemy picks up or throws a bomb, it uses the exact same printed Area Threat Profile.

#### Resolving Area Blasts by Target Type:
1.  **Goblin Bosses (PCs):** Roll a standard [[Clatter Roll]] (`Slink` Dodge vs the explosion's Threat TN). If evasion fails, roll passive Armor Dice to mitigate the incoming Damage; remaining damage reduces [[Grit]].
2.  **Mobs (PC or Enemy):** May spend a Reaction to **Scatter** (Boss Mouth test vs Threat TN) or roll passive Armor Dice. Unmitigated damage reduces Mob [[Size]].
3.  **Standard Enemies (Minions):** If the explosion's Threat TN meets or exceeds their static [[Defence]] TN, they are instantly destroyed.
4.  **Boss / Elite Enemies:** If the explosion's Threat TN meets or exceeds their [[Defence]] TN, the enemy suffers **1 Wound**. If the explosion's Impact Size meets or exceeds the Boss's physical Size (Impact Size >= Target Size), the Boss also gains the [[Staggered]] condition.

---

## Loot & Treasure Items

Not everything dragged out of a dungeon is useful in a fight. **Loot items** represent pure wealth—stolen silverware, golden chalices, jeweled idols, and kegs of vintage dwarven ale.

*   **Zero Combat Function:** Loot items provide no dice, armor, or tactical utility during an encounter.
*   **The Greed Dilemma:** Loot takes up valuable [[Bulk]]. Carrying heavy plunder directly competes with carrying extra weapons, shields, and tools.
*   **End-of-Raid Value:** When brought safely back to the Lair, Loot items are cashed in for [[Loot Value]], which feeds the Gang's [[Infamy]], funds [[Lair Upgrades]], and grants shared **XP** (see [Carrying Stuff](32_Carry%20Stuff.md) and [Loot](31_loot.md)).
