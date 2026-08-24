# 21. Bestiary: Classic & Tough Threats

*The world above the warrens is full of terrible things: greedy tall-men with sharp iron, feral beasts that view a goblin as a crunchy mid-day snack, ancient blood-drinking counts, and colossal fire-breathing horrors that can incinerate an entire gang in a single breath. A smart Goblin Boss knows every enemy's tricks—and more importantly, knows exactly how many goblins it takes to drag them down.*

---

## 1. Using the Bestiary

This chapter contains standardized stat blocks for adversaries encountered during [[Raid|Raids]]. All creatures operate on the deterministic rules detailed in [Enemies](20_Enemies.md) and [Combat](02%20Combat.md).

### Quick Reference Rules
*   **Zero GM Rolls:** The **GM** never rolls to hit or damage. All enemy attacks present a static **Threat** (difficulty and successes required to avoid) and flat **Damage**.
*   **Player Reactions:** When targeted by an enemy attack, you can spend a saved [[Standard Action]] to make a [[Clatter Roll]], rolling [[Slink]] to [[Dodge]] or [[Tough]] to [[Parry]] against the attack's **Threat**. 
*   **Passive Mitigation:** Successes on your equipped [[Armor]] dice reduce incoming damage by 1 per success (**5+**).
*   **One-Hit Kills:** Standard enemies die instantly when you roll successes equal to or greater than their [[Defence]] [[Target Number (TN)]].
*   **Wounds & Overkill:** [[Elite]] and [[Boss]] enemies track damage using a **Wounds** track. You deal **1 [[Wound]] for every full multiple of the target's [[Defence]] TN** scored on a single attack roll (e.g., against Defence 2, scoring 2 successes deals 1 Wound, 4 successes deals 2 Wounds, and 6 successes deals 3 Wounds).
*   **Mob Health (Dice-HP):** An Enemy [[Mob]] of **Size X** is tracked using **X physical D6s** on the table. Each point of damage reduces a die's face; losing a die removes 1 unit of [[Size]].

---

## 2. Universal Ancestries

Every creature belongs to an **Ancestry** that establishes its universal behavior, psychological limits, and condition vulnerabilities. You resolve these rules automatically without needing them printed on individual stat blocks.

### Beast
*Feral predators, vermin, and wild animals.*
*   **Instinctive Morale:** Beasts trigger an immediate [[Morale Check]] if targeted by `[Fire]`, loud explosions (`[Loud]`), or if their group size is halved.
*   **Lure Vulnerability:** Beasts prioritize targets possessing the `[Tasty]` tag above all other tactical targets and gain a **Boon (+1d)** on attacks against them.
*   **Mindless Immunity:** Beasts are immune to verbal [[Mouth]] persuasion and complex magical trickery.

### Humanoid
*Men, elves, dwarves, High Aurelians, and civilized outlaws.*
*   **Tactical Discipline:** Humanoids utilize cover, focus fire on goblin commanders, and obey allied [[Order]] actions.
*   **Standard Morale:** Subject to normal group [[Morale Check|Morale Checks]] when suffering 50% casualties or when their Commander is killed.
*   **Gear Salvage:** Defeated humanoids drop salvageable [[Scrap]], weapons, and [[Loot]].

### Undead
*Mindless skeletons, rotting corpses, vampires, and vengeful spirits.*
*   **Cold & Mindless:** Immune to [[Morale Check|Morale Checks]] (they fight until destroyed) and immune to the [[Terrified]] condition.
*   **Dead Flesh:** Immune to [[Weakened]] from poison (`[Toxic]`) and bleeding (`[Bleeding]`).
*   **Holy Vulnerability:** Attacks carrying the `[Angelic]` or `[Light]` tags deal **+1 Success** against Undead.

### Monstrosity
*Ogres, trolls, hydras, and colossal dragons.*
*   **Hulking Mass:** Monstrosities cannot be knocked [[Prone]], shoved, or [[Staggered]] unless the attack's **Impact Size** meets or exceeds the creature's physical **[[Size]]** ($\text{Impact Size} \ge \text{Target Size}$).
*   **Sweeping Blows:** Melee attacks made by a Monstrosity naturally Cleave, damaging all Goblins and [[Mob]] dice in the target [[Zone]].

### Fiend (Demon)
*Brimstone horrors, nether-beasts, and corrupt planar fiends.*
*   **Infernal Body:** Immune to damage and zone hazards carrying the `[Fire]` tag; immune to the [[Confusing]] and [[Terrified]] conditions.
*   **Purification Weakness:** Attacks carrying the `[Purified]` or `[Angelic]` tags ignore the Fiend's passive armor and reduce its [[Defence]] TN by 1.
*   **Chaos Opportunism:** Whenever a Goblin within 1 [[Zone]] rolls a [[Fumble]] (two or more 1s), the Fiend immediately triggers its listed retaliation reaction.

---

## 3. Vermin & Wild Beasts

*Dungeon floors and deep forests crawl with biting critters. While a single rat is a tasty snack, a swarm of them will strip the flesh from a goblin's bones in seconds.*

### Giant Sewer Rat
*Standard Beast (Size 0)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **2** | **5+/1** | `[Teeny]` |

**Special — Filth Fever:** If you fail your [[Dodge]] reaction against this creature's bite, you contract filthy sewer fleas, gaining the [[Weakened]] condition until treated in the Lair.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Gnawing Bite** | `Slink 4+/1` | 1 | Melee | Inflicts [[Weakened]] on failed evasion. |

**Plunder:** Matted rat pelt, sharp incisor (1 Scrap T1).

---

### Sewer Rat Swarm
*Enemy Mob (Size 3)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **2** | **5+/2** | `[Teeny]` |

**Special — Swarm Overwhelm:** If the Rat Swarm shares a [[Zone]] with a [[Prone]] Goblin or Mob, the **Threat TN** of its *Chittering Tide* increases by **+1**.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Chittering Tide** | `Slink 5+/2` | 3 | Melee | Damage scales with Mob Size: $1 + (\text{Size} - 1)$. |

**Plunder:** Piles of mangled rat bones, 1d6 Shiny Pennies (Loot Value 1, 1 Scrap T1).

---

### Cave Bat Swarm
*Enemy Mob (Size 3)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **3** | **5+/1** | `[Teeny]`, `[Fast]` |

**Special — Screeching Flap:** At the start of the Enemy Active turn, all Goblins sharing a [[Zone]] with the Bat Swarm must succeed on a **Brains 5+/1** test or gain the [[Blinded]] condition for 1 round as leathery wings buffet their faces.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Fluttering Claws** | `Slink 5+/1` | 3 | Melee | Damage scales with Mob Size: $1 + (\text{Size} - 1)$. |

**Plunder:** Leathery bat wings, guano dust (1 Scrap T1).

---

### Dire Wolf (Hunting Hound)
*Standard Beast (Size 1)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **3** | **5+/2** | `[Fast]` |

**Special — Takedown:** If you fail your [[Dodge]] reaction against the wolf's bite, you are knocked [[Prone]] and dragged down.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Snapping Jaws** | `Slink 5+/2` | 2 | Melee | Target is knocked [[Prone]] on failed evasion. |

**Plunder:** Thick canine pelt, spiked iron collar (1 Scrap T2).

---

### Forest Mauler (Cave Bear)
*Elite Beast (Size 2)*  
**Wounds:** 3

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **2** | **5+/3** | `[Heavy]`, `[Spiky]` |

**Special — Thick Blubber:** Attacks against the bear suffer a [[Bane]] (-1d) due to its dense layers of fat and matted fur. Attacks carrying the `[Fire]` tag bypass this blubber and roll normally without a Bane.  
**Special — Enraged Roar:** The first time the bear takes a [[Wound]], it lets loose an ear-splitting roar. All Goblins in its [[Zone]] must succeed on a **Brains 5+/1** test or suffer the [[Terrified]] condition.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Crushing Claws** | `Tough 5+/2` | 3 | Melee | `Cleave 2` (damages up to 2 Mob dice). |
| **Bear Hug** | `Slink 4+/2` | 2 | Melee | Target gains the [[Restrained]] condition. |

**Plunder:** Massive Bear Hide, Bear Skull Helm (Loot Value 2, 2 Scrap T2).

---

## 4. Outlaws & Tall-Men

*Tall-men are loud, arrogant, and carry shiny metal toys. They believe their heavy boots make them masters of the forest—until twenty goblins drop from the trees on top of them.*

### Desperate Robber (Footpad)
*Standard Humanoid (Size 1)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **2** | **5+/1** | None |

**Special — Pocket Sand:** Once per encounter, when engaged in Melee, the robber throws blinding dirt; the target's [[Dodge]] reaction becomes **Hard (6)**.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Rusty Shiv** | `Slink 5+/1` | 1 | Melee | None. |
| **Thrown Cobblestone** | `Slink 5+/1` | 1 | Ranged (1 Zone) | None. |

**Plunder:** Pouch of copper pennies, greasy dice (Loot Value 1, 1 Scrap T1).

---

### Robber Gang
*Enemy Mob (Size 3)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **2** | **5+/2** | None |

**Special — Greedy Snatch:** If the Robber Gang damages a Goblin or Mob carrying [[Loot]], the target immediately drops **1 Bulk** of carried treasure onto the ground.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Club & Shiv Swarm** | `Slink 5+/1` | 3 | Melee | Damage scales with Mob Size: $1 + (\text{Size} - 1)$. |

**Plunder:** Stolen trade sack, cheap knives (Loot Value 2, 1 Scrap T1).

---

### Bandit Crossbowman
*Standard Humanoid (Size 1)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **1** | **5+/1** | None |

**Special — Sniper's Focus:** If the crossbowman takes no [[Move]] actions on their turn, the **Threat TN** of their *Heavy Crossbow* attack increases by **+1** for that turn.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Heavy Crossbow** | `Slink 5+/2` | 2 | Ranged (2 Zones) | Piercing: Ignores 1 passive Armor Die. |
| **Dagger Jab** | `Slink 5+/1` | 1 | Melee | None. |

**Plunder:** Iron quarrel bundle, wooden crossbow stock (1 Scrap T2).

---

### Armored Highwayman
*Elite Humanoid (Size 1)*  
**Wounds:** 2

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **1** | **5+/2** | `[Hardened]` |

**Special — Parrying Buckler:** The first melee attack committed against the highwayman each round (regardless of whether it hits or misses, and whether made by a Boss or a Mob) must be rolled at **Hard (6)**. Once that first attack resolves, the buckler is committed and all subsequent melee attacks in the same round are resolved at Normal difficulty (**5+**).  
**Special — Heavy Cleave:** Hits from the highwayman's broadsword inflict the [[Staggered]] condition on the target until the end of the round.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Steel Broadsword** | `Tough 5+/2` | 2 | Melee | Inflicts [[Staggered]] on a failed [[Parry]]. |

**Plunder:** Polished steel buckler, heavy broadsword (Loot Value 2, 2 Scrap T3).

---

### Bandit Chief (The Road-Baron)
*Boss Humanoid (Size 1)*  
**Wounds:** 3

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **2** | **5+/3** | None |

**Special — Rousing Command:** As a free reaction at the start of the round, the Bandit Chief clears the [[Staggered]] condition and rallies broken Morale on all allied Humanoids in the same or adjacent [[Zone]].  
**Special — Human Shield:** When targeted by a [[ranged attack]] while in Melee with a Goblin or ally, the Chief redirects the incoming attack to that adjacent target on a failed attacker roll.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Flanged Iron Mace** | `Tough 5+/2` | 3 | Melee | Target is knocked [[Prone]] on a failed [[Parry]]. |
| **Flintlock Pistol** | `Slink 4+/2` | 3 | Ranged (1 Zone) | `[Loud]`: Alerts adjacent zones. 1 use per encounter. |

**Plunder:** Feathered cavalier hat, brass flintlock pistol, lockbox of silver sovereigns (Loot Value 4, 3 Scrap T3).

---

## 5. The Restless Dead & Blood Aristocracy

*The dead are supposed to stay in the ground. When they don't, it takes a lot of bashing to make them lie back down. From lowly rattlebones to ancient blood-drinking nobles, the undead represent unyielding, hunger-driven dread.*

### Rattlebone Skeleton
*Standard Undead (Size 1)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **1** | **Immune** | `[Mindless]` |

**Special — Dry Bones:** Attacks with the `Piercing` or `Cutting` traits (and all ranged bow attacks) suffer a [[Bane]] (-1d) against the skeleton. Attacks with the `Bashing` or `Crushing` traits gain a [[Boon]] (+1d).

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Notched Scimitar** | `Tough 5+/1` | 1 | Melee | None. |

**Plunder:** Ancient burial coins, skull scrap (1 Scrap T1).

---

### Skeleton Legion
*Enemy Mob (Size 4)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **1** | **Immune** | `[Mindless]` |

**Special — Wall of Ribs:** Attacks without the `Cleave` or `Bashing` traits can only reduce the Skeleton Legion's [[Size]] by a maximum of **1** per action, regardless of total successes rolled.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Rattling Spear Thrust** | `Tough 5+/2` | 4 | Melee | Damage scales with Mob Size: $1 + (\text{Size} - 1)$. |

**Plunder:** Rusted iron spearheads, brittle bone armor (2 Scrap T1).

---

### Plague Zombie (Rotting Shambler)
*Standard Undead (Size 1)*

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **1** | **1** | **Immune** | `[Rotting]`, `[Mindless]` |

**Special — Relentless Meat:** When reduced to 0 health by non-`[Fire]` and non-`[Acidic]` damage, the zombie remains standing (movement becomes 0) and takes its active turn normally this round, collapsing permanently during the **Round Closure Phase**.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Grasping Toxic Bite** | `Slink 5+/1` | 1 | Melee | Inflicts the `[Toxic]` tag on a failed evasion. |

**Plunder:** Rotting grave shrouds, embalming wax (1 Scrap T1).

---

### Flesh-Eating Ghoul
*Elite Undead (Size 1)*  
**Wounds:** 2

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **3** | **Immune** | `[Fast]`, `[Feral]` |

**Special — Paralytic Venom:** Any Goblin who fails their [[Dodge]] reaction against the ghoul's claws must succeed on a **Tough 5+/1** test or become [[Restrained]] for 1 round by numbing grave-slime.  
**Special — Carrion Feasting:** If the ghoul starts its turn in a [[Zone]] containing a dead corpse, it can spend 1 action feasting to heal 1 lost [[Wound]].

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Ripping Talons** | `Slink 4+/2` | 2 | Melee | Inflicts [[Restrained]] on a failed **Tough 5+/1** test. |

**Plunder:** Ghoul fangs, jar of paralytic tallow (Loot Value 1, 1 Scrap T2).

---

### Barrow Wight (Tomb Sentinel)
*Elite Undead (Size 1)*  
**Wounds:** 3

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **3** | **1** | **Immune** | `[Terrifying]`, `[Haunted]` |

**Special — Grave Chill:** Any living creature that enters or ends its turn in the Wight's [[Zone]] suffers a [[Bane]] (-1d) to all physical action tests due to freezing magical gloom.  
**Special — Life Drain:** Whenever the Wight deals damage to a Goblin Boss, the Wight instantly recovers 1 lost [[Wound]] (up to its maximum).

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Cursed Ancient Blade** | `Tough 4+/2` | 2 | Melee | Inflicts the [[Weakened]] condition. |

**Plunder:** Ancient electrum burial torque, runed bronze broadsword (Loot Value 3, 2 Scrap T3).

---

### Vampire Noble (The Blood Count)
*Boss Undead (Size 1)*  
**Wounds:** 4

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **3** | **3** | **Immune** | `[Fast]`, `[Haunted]`, `[Siphoning]` |

**Special — Hypnotic Glare (Reaction):** When targeted by a Melee attack from a Goblin Boss, the Boss must pass a **Brains 5+/2** test before rolling; on a failure, the Goblin freezes in awe and the attack action is wasted. If targeted by a [[Mob]], the Boss must pass an immediate **Mouth 5+/2** [[Order]] test to force the terrified runts to strike the vampire.  
**Special — Mist Escape & Siphon:** When dealing damage with *Crimson Fangs*, the vampire heals 1 lost [[Wound]]. If reduced to 0 Wounds by non-`[Fire]`, non-`[Light]` attacks, the vampire dissolves into mist and flees to its coffin.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Noble Rapier** | `Slink 4+/2` | 2 | Melee | Inflicts the [[Staggered]] condition. |
| **Crimson Fangs** | `Tough 5+/2` | 3 | Melee | Target is [[Restrained]]; heals 1 [[Wound]] to the vampire. |
| **Summon Bat Cloud** | — | — | Ranged (1 Zone) | Spawns 1 **Cave Bat Swarm** in target Zone (Once per encounter). |

**Plunder:** Blood-Ruby signet ring, silk velvet cape, silver-inlaid rapier (Loot Value 6, 4 Scrap T4).

---

## 6. Big Bullies & Arcane Bosses

*Some things are too large to squash with a normal hammer. Taking down a troll or an ironclad knight requires teamwork, explosives, and sacrificing a few runts to create an opening.*

### Swamp Troll
*Boss Monstrosity (Size 3)*  
**Wounds:** 4

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **2** | **5+/4** | `[Regenerating]`, `[Heavy]` |

**Special — Voracious Regrowth:** The troll recovers 1 lost [[Wound]] at the start of each round. If the troll suffered damage with the `[Fire]` or `[Acidic]` tag during the previous round, this regeneration is disabled for that round.  
**Special — Zone Sweep:** The troll swings massive logs with wild abandon. Its Melee attacks target every Goblin and Mob in its [[Zone]] simultaneously.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Uprooted Log Smash** | `Tough 5+/2` | 3 | Melee (Zone-Wide) | `Cleave 3`: Targets are knocked [[Prone]]. |
| **Bile Vomit** | `Slink 4+/2` | 2 | Ranged (1 Zone) | Inflicts `[Acidic]` and `[Toxic]` tags. |

**Plunder:** Troll gall bladder (alchemical catalyst), petrified stone club (Loot Value 4, 3 Scrap T3).

---

### Ironclad Knight (The Tin-Can Inquisitor)
*Elite Humanoid (Size 1)*  
**Wounds:** 3

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **3** | **1** | **5+/3** | `[Hardened]`, `[Heavy]` |

**Special — Plate Armor Bastion:** The knight ignores the first 1 point of incoming damage from every attack unless the attack possesses the `Piercing` trait or an elemental Tag (`[Fire]`, `[Acidic]`, `[Shock]`).  
**Special — Shield Rebound:** If your [[Parry]] reaction against the knight's warhammer fails with zero successes, you are knocked [[Prone]] and lose 1 saved action.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Crushing Warhammer** | `Tough 5+/2` | 3 | Melee | High impact: Knocks target [[Prone]] on a failed Parry. |
| **Tower Shield Slam** | `Tough 4+/1` | 1 | Melee | Shoves target into an adjacent [[Zone]]. |

**Plunder:** Heavy plate cuirass scrap, silver holy symbol, balanced warhammer (Loot Value 4, 3 Scrap T4).

---

### Corpse Stitcher (Wandering Necromancer)
*Boss Humanoid (Size 1)*  
**Wounds:** 3

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **2** | **5+/2** | None |

**Special — Animate Corpse (Reaction):** At the end of any round where a living creature or skeleton was killed in the Necromancer's [[Zone]] or an adjacent [[Zone]], the Necromancer instantly raises 1 **Rattlebone Skeleton** or **Plague Zombie** under their command.  
**Special — Bone Shield:** While in the same [[Zone]] as at least one allied Undead creature, attacks against the Necromancer suffer a [[Bane]] (-1d) as rotting minions leap in front of blows.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Soul-Drain Ray** | `Slink 5+/2` | 2 | Ranged (2 Zones) | `[Shock]`: Arcs 1 automatic damage to an adjacent Goblin. |
| **Bone Staff Strike** | `Tough 5+/1` | 1 | Melee | Inflicts the `[Chilled]` tag. |

**Plunder:** Grimoire of Black Ichor, soul-cage lantern, pouch of onyx gemstones (Loot Value 5, 2 Scrap T3, 1 Scrap T4).

---

## 7. Imperial Horrors (The High Aurelians)

*Seven feet tall, with burning golden eyes and brass-plated flesh, the High Aurelians viewed goblins as crude vermin born only to shovel soot. Whether sealed inside pressurized steam reliquaries or drinking toxic black ichor to cheat cellular collapse, they are lethal remnants of a fallen golden age.*

### Ichor-Gorged Tyrant (The Black-Vein Noble)
*Elite Humanoid (Size 2)*  
**Wounds:** 3

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **2** | **3** | **5+/3** | `[Fast]`, `[Toxic]`, `[Frenzied]` |

**Special — Black Ichor Blood:** When the Tyrant takes a [[Wound]] in Melee, acidic black ichor sprays onto the attacker; the attacker must pass a **Slink 5+/1** test or suffer 1 [[Grit]] damage (or lose 1 unit of Mob [[Size]]).  
**Special — Solar Frenzy:** While at 1 [[Wound]], the Tyrant becomes [[Frenzied]]; its Melee attacks deal **+1 Damage** and gain the Cleave trait.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Ichor-Tipped Greatsword** | `Tough 5+/2` | 3 | Melee | Inflicts the `[Toxic]` tag. |
| **Black Bile Spit** | `Slink 4+/2` | 2 | Ranged (1 Zone) | Inflicts `[Acidic]` and corrodes 1 Armor Die. |

**Plunder:** Distilled Black Ichor Phial, Spun-Brass Regalia, Heavy Greatsword (Loot Value 4, 3 Scrap T3).

---

### Solar Praetor (The Brass Reliquary)
*Boss Humanoid / Construct (Size 2)*  
**Wounds:** 5

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **4** | **2** | **5+/4** | `[Hardened]`, `[Heavy]`, `[Angelic]` |

**Special — Pressurized Steam Vent (Hazard Reaction):** Whenever the Praetor takes a [[Wound]], boiling steam erupts across its [[Zone]]; all Goblins in the [[Zone]] must succeed on a **Slink 5+/2** test or take 2 damage from scalding vapor (`[Fire]`).  
**Special — Sol-Quartz Power Core (Flaw Hook):** If struck by an attack carrying the `[Shock]` or `[Acidic]` tags, the crystal core short-circuits: the Praetor's [[Defence]] TN drops to **2** until the end of the round.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Sun-Forged Lance** | `Tough 5+/3` | 4 | Melee | Ignores passive armor; target knocked [[Prone]]. |
| **Solar Purge Beam** | `Slink 4+/3` | 4 | Ranged (2 Zones, Line) | Blasts a line with `[Light]` & `[Fire]`, destroying cover. |
| **Crushing Brass Gauntlet** | `Tough 5+/2` | 3 | Melee | Cleave (Zone-Wide). |

**Plunder:** Intact Sol-Quartz Fuel Core, Ornate Brass Chassis Plating, Sun-Forged Lance (Loot Value 8, 5 Scrap T4, 1 Scrap T5).

---

## 8. Legendary Threats & Apex Monsters

*These are the apex predators of the world—ancient horrors whose mere presence shakes the earth. Fighting an apex monster is a lethal puzzle requiring planning, explosive oddities, and throwing dozens of screaming goblins into the grinder to create a single killing blow.*

### Brimstone Fiend (The Horned Ravager)
*Boss Fiend (Size 2)*  
**Wounds:** 5

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **3** | **3** | **Immune** | `[Terrifying]`, `[Spiky]`, `[Vile]` |

**Special — Hellfire Aura:** At the end of every round, the Fiend's [[Zone]] bursts into cursed flames; all creatures in the [[Zone]] take 1 damage and gain the `[Burning]` tag.  
**Special — Chaos Retaliation (Fumble Punisher):** Whenever a Goblin within 1 [[Zone]] rolls a [[Fumble]] (two or more 1s), the Fiend immediately makes a free *Barbed Shadow-Whip* attack against that Goblin without spending an action.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Brimstone Cleaver** | `Tough 4+/3` | 4 | Melee | `Cleave 3`; inflicts `[Vile]`. |
| **Barbed Shadow-Whip** | `Slink 5+/2` | 2 | Range (1 Zone) | Drags target into the Fiend's [[Zone]] and inflicts [[Restrained]]. |

**Plunder:** Demon Horn Scrap, Smoldering Infernal Core, Jagged Hell-Steel Blade (Loot Value 7, 4 Scrap T4).

---

### Ancient Cinder Dragon (The Great Ash-Wyrm)
*Apex Boss Monstrosity (Size 4)*  
**Wounds:** 8

| Defence | Movement | Morale | Tags |
| :---: | :---: | :---: | :--- |
| **4** | **3** | **5+/5** | `[Heavy]`, `[Hardened]`, `[Terrifying]` |

**Special — Colossal Action Clock (Automata):** The Dragon acts according to a predictable 3-round destructive cycle:
*   **Round 1 (Wing Buffet & Roar):** Massive hurricane gale pushes all Goblins in adjacent zones back 1 [[Zone]]; all Goblins must test **Brains 5+/2** or gain the [[Terrified]] condition.
*   **Round 2 (Incandescent Inhale):** The Dragon's throat ignites with white heat; the front 2 [[Zones]] are showered in embers (`[Burning]`). Goblins have 1 round to dive behind solid cover or scatter!
*   **Round 3 (Hellfire Breath):** Unleashes *Hellfire Breath* across 2 consecutive [[Zones]]. Resets Clock to Round 1.

**Special — Greed Distraction (Flaw Hook):** If a Goblin Boss spends a [[Standard Action]] ([[Manipulate]]) to throw a shiny treasure with [[Loot Value]] **3+** into an adjacent [[Zone]], the Dragon's pride and greed forces it to target that zone with its next melee attack instead of targeting the players.

#### [[Attack|Attacks]]
| Attack | Threat | Damage | Range | Special |
| :--- | :---: | :---: | :---: | :--- |
| **Colossal Tail Sweep** | `Slink 5+/3` | 4 | Melee (Zone-Wide) | `Cleave 5`: All targets in [[Zone]] thrown 1 Zone and knocked [[Prone]]. |
| **Crushing Dragon Jaws** | `Tough 6/2` (Hard!) | 6 | Melee | Shatters shields; inflicts 2 Wounds on Bosses if undefended. |
| **Hellfire Breath (Clock)** | `Slink 4+/3` | 5 | Ranged (2 Zones, AoE) | Vaporizes wooden cover; ignites both zones with `[Fire]`. |

**Plunder:** Hoard of the Drake-Lords (Loot Value 15, 6 Scrap T4, 2 Scrap T5, Dragon Heart Oddity T5/B0).

---

## 9. Example Combat Encounters

> **Example 1: Smashing Dry Bones**
> 
> *Skag and his Size 3 Mob of spears confront two Rattlebone Skeletons (Defence 2).* 
> 
> Skag swings his trusty Heavy Club (a `Bashing` weapon). Because skeletons have the *Dry Bones* trait, Skag gains a **Boon (+1d)** to his attack roll. Skag rolls 4d6 (Tough 3 + 1d Boon) and scores three successes (**5, 5, 6**). 
> 
> Because Skag rolled **3 successes**, which exceeds the Skeleton's **Defence TN of 2**, the first skeleton shatters instantly! The excess 1 success does not cleave because Skag is using a standard single-target weapon.
> 
> Skag's Mob then attacks the second skeleton. The Mob scores 2 successes, perfectly meeting the **Defence TN of 2**, crushing the second skeleton into dust.

> **Example 2: Surviving the Bear's Claws**
> 
> *The Forest Mauler (Elite Beast) attacks Boss Fizzle with its Crushing Claws (Threat `Tough 5+/2`, Damage 3).*
> 
> Fizzle has saved 1 [[Standard Action]] from his turn and holds a scrap iron shield. He declares a **Parry** and rolls his **Clatter Roll**:
> *   **Stat Dice:** 2d6 for [[Tough]] (Fizzle's Tough is 2).
> *   **Armor Dice:** 2 gray d6s for his Tin Plate armor.
> 
> Fizzle rolls his dice. On his Tough dice, he rolls a **3** and a **5** (1 success). Because the bear's Threat requires **2 successes on 5+** (`5+/2`), Fizzle fails to parry cleanly!
> 
> He now checks his Armor Dice for damage mitigation. The gray dice land on **5** and **6** (2 successes). Each armor success reduces the incoming 3 Damage by 1:
> $$\text{Damage Taken} = 3 - 2 = 1 \text{ Grit}$$
> 
> Fizzle takes **1 Grit** damage instead of 3, absorbing the savage swipe on his trusty armor!

> **Example 3: Overclocking Against the High Aurelian Praetor**
> 
> *Boss Grib and his Gang face the towering Solar Praetor (Defence 4, Wounds 5).*
> 
> Grib knows attacking the Praetor's thick brass armor head-on is suicide. Grib's alchemist throws an alchemical *Shock Flask* (`[Shock]`) at the Praetor. 
> 
> Because the Praetor has the *Sol-Quartz Power Core* flaw hook, the electrical arc shorts out its crystal regulator: the Praetor's [[Defence]] TN instantly drops from **4** to **2** for the rest of the round!
> 
> Grib steps up with his custom Overclocked Scrap-Cleaver. Grib rolls 5d6 on [[Tough]] and spends 2 [[Grunt]] to boost his dice pool, achieving an incredible **6 successes**!
> 
> By the **Overkill Rule**, every multiple of the Praetor's modified Defence TN (2) inflicts a [[Wound]]:
> $$\text{Wounds Dealt} = \frac{6 \text{ Successes}}{\text{Defence } 2} = 3 \text{ Wounds!}$$
> 
> Grib deals **3 Wounds** in a single massive blow, buckling the Praetor's brass chassis before its steam vents can retaliate!
