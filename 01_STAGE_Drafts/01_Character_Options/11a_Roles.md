# Roles

*Goblins do not have careers. They have jobs they took by force and roles they fill to avoid being eaten. A Boss is only as strong as their gang's fear of them, and that fear changes depending on how the Boss leads.*

A [[Role]] represents the tactical archetype and leadership style of your **Goblin Boss** based on your current [[Main Stats]] configuration. Your [[Role]] defines how you fight, how you command your [[Mob]], and what innate talents you bring to a raid.

Because you increase your [[Main Stats]] by spending [[XP]] during downtime, your [[Role]] is dynamic. As your stats change, your [[Role]] and **Role Level** naturally evolve.

---

## 1. Determining Your Role

Your [[Role]] is determined by comparing your **Primary Stat** (your highest [[Main Stat]]) with your **Secondary Stat** (your second-highest [[Main Stat]], which also determines your [[Grunt]]):

*   **Specialist Roles (Gap $\ge$ 2):** If your highest stat is **2 or more levels higher** than your second-highest stat, you are a **Specialist** dedicated to running ahead in that single discipline.
*   **Hybrid Roles (Gap $\le$ 1):** If the difference between your highest and second-highest stat is **1 or 0**, you are a **Hybrid** combining both stats into a coordinated leadership style.

>> **Tied Stats:** If you have multiple stats tied for highest or second-highest, you choose which of those stats acts as your Primary and Secondary for the purpose of your active [[Role]].

---

## 2. Role Levels & Innate Role Skills

Each of the 16 Roles grants **1 unique Role Skill** that defines that archetype. 

*   **No XP Cost:** You do not spend [[XP]] to acquire or upgrade your Role Skill. It is an innate feature granted automatically by your active [[Role]].
*   **Zero XP Waste on Shifting:** If your stats shift during the [[Lair Phase]] and your [[Role]] changes, you immediately replace your old Role Skill with your new Role's skill at your new **Role Level** for free.

### How Role Level is Calculated

Your **Role Level** determines which tier of your Role Skill is currently active:

*   **Specialist Role Level = Primary Stat (Levels 3–5):** Because Specialists hyper-focus on a single discipline, your **Role Level** is equal to your **Primary Stat**. Because starting Specialists begin at `3, 1, 1, 1`, Specialist progression spans **Level 3, Level 4, and Level 5**. Your [[Grunt]] remains low (1 to 3), meaning you command smaller [[Mob|Mobs]] (Size 1–3) but wield devastating personal power.
*   **Hybrid Role Level = Secondary Stat / Grunt (Levels 2–5):** Because Hybrids rely on the synergy between two stats, your **Role Level** is equal to your **Secondary Stat** (which is also your maximum [[Grunt]]). Because starting Generalists begin at `2, 2, 1, 1`, Hybrid progression spans **Level 2, Level 3, Level 4, and Level 5**. Your high [[Grunt]] allows you to command larger [[Mob|Mobs]] (Size 2–5) while scaling your hybrid synergy.

---

## 3. The 16 Roles & Progression Tracks

### Tough Roles (Primary: Tough)

#### 1. The Meat-Wall (Tough Specialist)
*A towering brute of pure muscle and scarred hide who absorbs punishment that would flatten ordinary goblins.*
*   **Skill: Iron Hide (Passive)**
    *   **Level 3:** Your maximum [[Grit]] increases by **+2**. Gain **+1d [[Passive Defence]]** against physical melee and ranged attacks.
    *   **Level 4:** Your maximum [[Grit]] increases by **+2** and **+1d [[Passive Defence]]**. Once per raid, when damage would reduce you to 0 [[Grit]], you drop to 1 [[Grit]] instead.
    *   **Level 5:** Your maximum [[Grit]] increases by **+3** and **+2d [[Passive Defence]]**. Once per raid, when damage would reduce you to 0 [[Grit]], you drop to 1 [[Grit]] instead and gain an immediate bonus [[Standard Action]].

#### 2. The Raider (Tough + Slink Hybrid)
*A violent shock-trooper who charges across the battlefield to smash enemy lines on the run.*
*   **Skill: Shock Charge (Active)**
    *   **Level 2:** When you spend a [[Move Action]] to enter a [[Zone]] containing enemies, your next melee [[Attack]] in the same round gains **+1d**, and you ignore movement penalties from Difficult Terrain when moving into combat.
    *   **Level 3:** Melee attacks after a [[Move Action]] gain **+2d**. If your attack scores 2+ successes, the target is knocked [[Prone]].
    *   **Level 4:** Melee attacks after a [[Move Action]] gain **+2d** and knock targets [[Prone]]. You may immediately Disengage 1 [[Zone]] for free after resolving the attack.
    *   **Level 5:** Melee attacks after a [[Move Action]] gain **+3d** and knock targets [[Prone]]. Your attack cleaves, dealing 1 [[Wound]] (or 1 [[Size]] loss) to all other enemies in the [[Zone]].

#### 3. The Enforcer (Tough + Mouth Hybrid)
*A ruthless gang leader who uses fists, heavy clubs, and vicious threats to keep runts and enemies obedient.*
*   **Skill: Skull-Cracker Command (Active)**
    *   **Level 2:** Once per round when you issue an [[Order Action]], you can intimidate an allied [[Mob]] in your [[Zone]] to grant them **+1d** on their next test. When an enemy enters your [[Zone]], you can make an immediate melee attack as a [[Reaction]].
    *   **Level 3:** Allied [[Mob|Mobs]] you intimidate gain **+2d**. When you hit an enemy in melee, allied [[Mob|Mobs]] in your [[Zone]] gain **+1d** on their next attack against that enemy.
    *   **Level 4:** Allied [[Mob|Mobs]] you intimidate gain **+2d**. When you deal melee damage to an enemy, that enemy gains the [[Weakened]] condition.
    *   **Level 5:** Allied [[Mob|Mobs]] you intimidate gain **+3d**. Whenever you defeat an enemy in melee, all allied [[Mob|Mobs]] in your [[Zone]] immediately resolve a free [[Attack Action]].

#### 4. The Iron-Tinker (Tough + Brains Hybrid)
*A heavy crafter who straps jagged scrap-metal plates to their chest and swings massive, customized bludgeons.*
*   **Skill: Scrap Juggernaut (Passive/Active)**
    *   **Level 2:** Weapons and armor you wield ignore their first [[Break Roll]] per raid ([[Junk]] gear does not shatter on its first fumble). Heavy weapons you wield have their encumbrance reduced by **1 [[Bulk]]** (minimum 1 Bulk).
    *   **Level 3:** Gain **+1d [[Passive Defence]]** while equipped with armor or a shield. When you hit an enemy with a Heavy weapon, destroy any minor cover in their [[Zone]].
    *   **Level 4:** Gain **+1d [[Passive Defence]]**. When your weapon triggers a [[Break Roll]], you can choose to intentionally shatter it to add **+2 automatic successes** to your attack.
    *   **Level 5:** Gain **+2d [[Passive Defence]]**. You can attach 1 additional [[Component]] to any Heavy weapon or armor beyond normal workshop limits.

---

### Slink Roles (Primary: Slink)

#### 5. The Scuttler (Slink Specialist)
*A shadow-dwelling ghost who darts between cover, slips through cracks, and cannot be pinned down.*
*   **Skill: Ghost Slink (Passive)**
    *   **Level 3:** You move freely through enemy [[Zone|Zones]] without triggering Opportunity Attacks, and gain **+1d** on all [[Slink]] tests made to hide or maintain stealth. While in Cover, ranged attacks cannot target you unless the attacker enters your [[Zone]].
    *   **Level 4:** You move freely through enemy [[Zone|Zones]] and gain **+2d** on [[Slink]] tests. When targeted by an attack, you may spend a [[Reaction]] to pass a `Slink 4+/1` test to slip into an adjacent cover [[Zone]] and cancel the attack.
    *   **Level 5:** You move freely through enemy [[Zone|Zones]] and gain **+2d** on [[Slink]] tests. You automatically succeed on stealth tests against standard guards, and attacks against you while in cover suffer **-2d (2 Bane Dice)**.

#### 6. The Gut-Cutter (Slink + Tough Hybrid)
*A vicious assassin who waits for allies to distract the enemy before slipping behind them for a lethal back-shank.*
*   **Skill: Back-Shank (Passive/Active)**
    *   **Level 2:** When making a melee [[Attack]] against an enemy in a [[Zone]] containing an allied [[Mob]] or Boss, gain **+1d**. On a Critical hit (exploding 6s), inflict the [[Weakened]] condition on the target.
    *   **Level 3:** Flanking melee attacks gain **+2d**. If the target is [[Weakened]] or [[Prone]], your attack deals **+1 [[Wound]]** (or +1 [[Grit]] damage).
    *   **Level 4:** Flanking melee attacks gain **+2d**. Flanking attacks bypass the enemy's armor and [[Passive Defence]] dice completely.
    *   **Level 5:** Flanking melee attacks gain **+3d**. Flanking attacks that score 2+ successes instantly execute standard enemies, or deal double [[Wound|Wounds]] against Monsters.

#### 7. The Ring-Leader (Slink + Mouth Hybrid)
*A slippery agitator who directs the chaos from safety, shouting orders through the shadows.*
*   **Skill: Distraction Scheme (Active)**
    *   **Level 2:** You can issue [[Order|Orders]] to [[Mob|Mobs]] up to **2 [[Zone|Zones]] away** (instead of 1 zone). Once per round, you can order a [[Mob]] to [[Scatter]] or [[Dodge]] as a [[Free Action]].
    *   **Level 3:** [[Order|Orders]] reach up to 3 [[Zone|Zones]] away. When your [[Mob]] attacks an enemy you have distracted with a [[Slink]] test, the [[Mob]] gains **+1d**.
    *   **Level 4:** [[Order|Orders]] reach up to 3 [[Zone|Zones]] away. When an enemy enters your [[Zone]], you can swap positions with an allied [[Mob]] in the same or adjacent [[Zone]] as a [[Reaction]].
    *   **Level 5:** [[Order|Orders]] reach across the entire encounter map. Allied [[Mob|Mobs]] within your line of sight gain **+2d** on all [[Dodge]] and [[Attack]] tests.

#### 8. The Saboteur (Slink + Brains Hybrid)
*An infiltration expert who bypasses complex locks, rigs deadfalls, and hurls corrosive alchemical flasks.*
*   **Skill: Trap & Toxin Mastery (Passive/Active)**
    *   **Level 2:** Gain **+1d** on all tests to pick locks, disarm mechanical traps, or rig environmental hazards. Thrown flasks, grenades, and alchemical items gain **+1 [[Zone]] range** and **+1d** on the attack test.
    *   **Level 3:** Gain **+2d** on trap/lock tests. When you deploy a trap or explosive in a [[Zone]], enemies caught in the blast gain the [[Blinded]] or [[Restrained]] condition on a hit.
    *   **Level 4:** Gain **+2d** on trap/lock tests. You can deploy traps or poisons as a [[Free Action]] during a [[Move Action]].
    *   **Level 5:** Gain **+3d** on trap/lock tests. Alchemical explosives you craft deal **+2 [[Wound|Wounds]]** (or +2 [[Size]] loss) and ignite the target [[Zone]] with persistent hazards.

---

### Mouth Roles (Primary: Mouth)

#### 9. The Over-Lord (Mouth Specialist)
*A loud, self-important tyrant who wears the biggest hat, screaming commands while hiding behind a wall of goblins.*
*   **Skill: Tyrant's Roar (Passive/Active)**
    *   **Level 3:** Your [[Max Mobs]] capacity is treated as **1 higher** than your current [[Mouth]] stat, and you roll **+1d** on tests to command or rally a [[Mob]]. When an allied [[Mob]] is in your [[Zone]], you can redirect any attack targeting you onto that [[Mob]] without spending an action.
    *   **Level 4:** Gain **+2 [[Max Mobs]]** and **+2d** on command tests. [[Mob|Mobs]] under your direct command never suffer Morale failures while you remain conscious.
    *   **Level 5:** Gain **+2 [[Max Mobs]]** and **+2d** on command tests. Once per raid, issue a **Grand Command**: all allied [[Mob|Mobs]] on the map immediately resolve a free [[Standard Action]].

#### 10. The Taskmaster (Mouth + Tough Hybrid)
*A cruel driver who cracks whips and drives runts into a howling, self-destructive frenzy.*
*   **Skill: Blood Frenzy (Active)**
    *   **Level 2:** When you order an allied [[Mob]] to [[Attack]], you can choose to sacrifice **1 [[Mob]] [[Size]]** to grant the [[Mob]] **+2d** on their attack roll. When an allied [[Mob]] in your [[Zone]] suffers casualties, you immediately regain **1 [[Grunt]]** (up to your maximum).
    *   **Level 3:** Sacrificing 1 [[Mob]] [[Size]] grants **+3d**. [[Mob|Mobs]] under your command gain **+1 [[Zone]] [[Movement]]**.
    *   **Level 4:** Sacrificing 1 [[Mob]] [[Size]] grants **+3d**. When your [[Mob]] charges an enemy [[Zone]], enemies must pass `Tough 4+/2` or become [[Terrified]].
    *   **Level 5:** Sacrificing 1 [[Mob]] [[Size]] grants **+4d**. If a [[Mob]] under your command is wiped out, you gain an immediate bonus turn with **+3d** on all attacks.

#### 11. The Swindler (Mouth + Slink Hybrid)
*A fast-talking con artist and coward who weaves lies, creates chaos, and tricks enemies into attacking each other.*
*   **Skill: Fast Talk & Misdirection (Passive/Active)**
    *   **Level 2:** Gain **+1d** on [[Mouth]] tests to deceive, bluff, or distract guards and NPCs. When an enemy in your [[Zone]] attacks you, make a `Mouth 4+/1` test as a [[Reaction]]: if successful, the enemy misses completely.
    *   **Level 3:** Gain **+2d** on bluff tests. When you succeed on your misdirection test (`Mouth 4+/1`), redirect the incoming attack onto an adjacent enemy in the same [[Zone]].
    *   **Level 4:** Gain **+2d** on bluff tests. You can [[Plunder]] guarded containers or enemy pockets during combat as a [[Free Action]].
    *   **Level 5:** Gain **+3d** on bluff tests. Once per combat, make a `Mouth 5+/2` test against an enemy minion: on a success, that unit fights for you for 1 round before fleeing.

#### 12. The Chant-Monger (Mouth + Brains Hybrid)
*A loud war-chanter who turns magical formulas into rhythmic goblin songs that empower the entire swarm.*
*   **Skill: War-Chant Cadence (Active)**
    *   **Level 2:** You can begin a Chant as a [[Free Action]]. While chanting, all allied spellcasters in your [[Zone]] reduce Side Effects from non-success dice by 1, and allied [[Mob|Mobs]] in your [[Zone]] gain **+1d** on all test pools.
    *   **Level 3:** Side Effects reduced by 2. Allied [[Mob|Mobs]] gain **+1d**. You can activate [[Power Words]] through chants without needing an item focus.
    *   **Level 4:** Side Effects reduced by 2. Allied [[Mob|Mobs]] gain **+2d**. Your Chant reaches your [[Zone]] and all adjacent [[Zone|Zones]].
    *   **Level 5:** Side Effects are completely neutralized. All allies in range gain **+2d** on all tests and regain **1 [[Grit]]** whenever an enemy is defeated.

---

### Brains Roles (Primary: Brains)

#### 13. The Sage-Tinker (Brains Specialist)
*A mad goblin inventor who locks themselves in the workshop to concoct acids, clockwork contraptions, and volatile machines.*
*   **Skill: Experimental Innovation (Passive/Active)**
    *   **Level 3:** Your [[Crafting Capacity]] is treated as **2 higher** than your current [[Brains]] stat. You can dismantle scrap or [[Junk]] gear during a raid to assemble single-use tools or makeshift bombs in 1 [[Manipulate Action]]. When an item with an [[Component]] triggers an effect, you can double its potency by risking an immediate durability test (`Brains 4+/1`).
    *   **Level 4:** Gain **+2 [[Crafting Capacity]]**. You can repair broken items during a raid with 1 [[Manipulate Action]]. Weapons you customize gain **+1d damage**.
    *   **Level 5:** Gain **+3 [[Crafting Capacity]]**. You can invent 1 Masterwork [[Relic]] with up to 4 [[Component]] sockets that never suffers [[Break Roll|Break Rolls]].

#### 14. The Runecaster (Brains + Tough Hybrid)
*A heavily built runic warrior who chisels glowing arcane glyphs onto iron blades and armor, smashing foes with elemental force.*
*   **Skill: Spell-Forged Strike (Active)**
    *   **Level 2:** When you hit with a melee attack, you can expend 1 [[Power Words|Power Word]] slot to deal **+1d [Fire]**, **[Shock]**, or **[Corrosive]** damage. Gain **+1d** on all tests to resist hostile magic, curses, and environmental hazards.
    *   **Level 3:** Elemental strikes deal **+2d**. Your armor is etched with runic wards, granting **+1d [[Passive Defence]]** against magical and elemental attacks.
    *   **Level 4:** Elemental strikes deal **+2d**. When you strike an enemy with an etched weapon, the elemental tag cleaves across all targets in the [[Zone]].
    *   **Level 5:** Elemental strikes deal **+3d**. You can infuse your body with rune magic, gaining **+2 [[Grit]]** and **+2d** on all [[Tough]] and melee attack tests for 3 rounds.

#### 15. The Hex-Weaver (Brains + Slink Hybrid)
*A sneaky spell-sniper who hurls curses and elemental bolts from complete darkness, never giving away their position.*
*   **Skill: Shadow Hexing (Passive/Active)**
    *   **Level 2:** Casting a spell from Cover does not reveal your position or break stealth unless the spell causes an explosion in your own [[Zone]]. When targeting an enemy in an adjacent [[Zone]] with a spell from stealth, gain **+1d** on the casting test.
    *   **Level 3:** Stealth casting and **+1d** casting. You can curve spell trajectories around full cover and obstacles without line-of-sight penalties.
    *   **Level 4:** Stealth casting and **+2d** casting. Enemies damaged by your hexes gain the [[Silenced]] or [[Dumb]] condition.
    *   **Level 5:** Stealth casting and **+3d** casting. When you cast a spell from the shadows, you can duplicate the spell to hit a second target in range for free.

#### 16. The Shaman (Brains + Mouth Hybrid)
*A tribal mystic who speaks with the spirits, channeling elemental tags through the swarm to guide the war party.*
*   **Skill: Spirit Conduit (Passive/Active)**
    *   **Level 2:** You can cast spells through an allied [[Mob]] in your line of sight, using the [[Mob|Mob's]] [[Zone]] as the spell's origin point. When you cast a beneficial buff spell, the effect applies to both you and 1 allied [[Mob]] simultaneously.
    *   **Level 3:** Mob conduit casting and dual buffs. Allied [[Mob|Mobs]] in your [[Zone]] gain magical attacks that bypass physical armor.
    *   **Level 4:** Mob conduit casting. You can summon spirit wisps in any [[Zone]] in line of sight, providing Light and imposing **-1d (1 Bane Die)** on enemy attacks.
    *   **Level 5:** Mob conduit casting. Once per raid, channel the Great Ancestor Spirit: all allied [[Mob|Mobs]] on the map become immune to Morale tests and deal **+2d** damage on attacks for 3 rounds.
