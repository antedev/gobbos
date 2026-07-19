# 08. Master Tag Index

*Goblins don't write dictionaries, but they do have a lot of words for things that burn, melt, smell, or go squish. A [Fire] blade sets a peasant alight; a [Sticky] Net keeps him from running; an [Angelic] word makes a knight's heavy plate feel like tissue paper. This is the master ledger of the active forces in the world.*

---

## 1. The Core Architecture: What is a Tag?

A [[Tag]] (always written in brackets, e.g., `[Fire]`, `[Sticky]`) is the dynamic systemic vocabulary of Gobbos. It represents a transient physical force, element, substance, or magical state that can be slung as a spell, crafted into an item, or applied to a zone. 

Unlike a creature's [[Ancestry]] (what it *is*) or an item's [[Trait]] (how it is *constructed*), a Tag represents a temporary state that can be dynamically attached or stripped away during play.

---

## 2. Pre-Roll Profile Calculations

>> **GOLDEN RULE: No Post-Roll Math**
>> To keep combat fast and chaotic, all tag interactions, vulnerabilities, and environmental modifiers must be resolved **before** the dice are thrown. Once the dice land, the result must be instantly clear.

When a player makes a test involving tags (e.g., attacking a monster with an elemental weapon), they calculate the [[Roll Profile]] in three quick steps:

1.  **Check Base Stats:** Look up the attacker's pool ([[Tough]] or [[Slink]]) and the target's base [[Defence]] TN and [[Difficulty]] 
2.  **Check Monster Hooks (Local Overrides):** Compare the attacker's weapon tags with the target's printed [[Flaw Hooks]] or [[Resistance Hooks]]:
    *   *Flaws:* If a tag matches a Flaw, it typically reduces [[Defence TN]] or makes the test [[Easy (4+)]].
    *   *Resistances:* If a tag matches a Resistance, it typically increases [[Defence TN]] or makes the test [[Hard (6)]].
3.  **Apply the Boon/Bane Cap:** Apply any environmental zone tags (e.g., a `[Slick]` floor or `[Strong Wind]` battlefield).
    *   *The Cap:* Multiple environmental Boons or Banes do not stack. You either have one Boon (**+1d**), one Bane (**-1d**), or they cancel to **0** bonus dice.

---

## 3. Element Synthesis

When two dynamic elements meet (either combined in custom gear crafting or overlapping in a zone), they synthesize into a new state. Element synthesis is resolved at creation or downtime to avoid combat speed-bumps.

*   `[Fire]` + `[Sticky]` $\rightarrow$ [[Burning Glue]]: Inflicts the *Restrained* condition and deals **+1 success** on the attack.
*   `[Toxic]` + `[Chilled]` $\rightarrow$ [[Numbing Venom]]: Inflicts the *Restrained* condition (movement becomes 0).
*   `[Wet]` + `[Shock]` $\rightarrow$ [[Conduction]]: Shakes the target's defenses, making all attack tests against them [[Easy (4+)]] for 1 round.
*   `[Wet]` + `[Fire]` $\rightarrow$ [[Steam Cloud]]: Immediately strips the `[Fire]` tag and creates a `[Dark]` zone hazard.
*   `[Fire]` + `[Volatile]` $\rightarrow$ [[Detonation]]: Immediately triggers a `[Explosive]` payload, clearing the source items.

---

## 4. The Master Tag Catalog

---

### Group 1: Elemental & Material States (Alchemical Hazards)

#### `[Acidic]`
*   *Flavor:* Sizzling green slime, corrosive bile, or rusted metal-eating juice.
*   *Universal Baseline:* Corrosion. Destroys 1 Passive Defense die granted by the target's armor on a hit.
*   *Fictional Interaction:* Eats through wood, leather, and metal, but is inert against glass or stone.

#### `[Chilled]`
*   *Flavor:* Frost-covered metal, frozen wind, or magical numbing cold.
*   *Universal Baseline:* Reduces the target's [[Movement]] by 1 Zone (minimum 0) for 1 round.
*   *Fictional Interaction:* Freezes standing water, cracks brittle stone, and extinguishes fires.

#### `[Fire]`
*   *Flavor:* Crackling embers, liquid pitch, or sudden alchemical heat.
*   *Universal Baseline:* Deals **+1 Success** on attack tests and places the `[Burning]` tag on the target's Zone.
*   *Fictional Interaction:* Ignites dry wood, melts ice, burns away ropes, and strips `[Wet]` tags.

#### `[Gaseous]`
*   *Flavor:* Choking green fumes, heavy mist, or toxic sulfur.
*   *Universal Baseline:* Suffocating screen. The Zone becomes `[Dark]` (ranged attacks suffer a [[Bane]]).
*   *Fictional Interaction:* Dispersed instantly by wind tags (`[Gale]`).

#### `[Shock]`
*   *Flavor:* Blue static sparks, crackling lightning, or sudden nerve spasms.
*   *Universal Baseline:* Arc damage. If the attack hits, it deals [[1 automatic success]] (against standard enemies) or [[1 automatic Grit/Size damage]] (against PCs/Bosses/Mobs) to one additional target in the same [[Zone]].
*   *Fictional Interaction:* Conducts instantly through metal armor (`Corporeal:Metal`) or water (`[Wet]`), making tests against them [[Easy (4+)]].

#### `[Slick]`
*   *Flavor:* Buttered grease, wet ice, or slimy oil.
*   *Universal Baseline:* Slippery footing. Any creature attempting to Move into or out of the Zone must succeed on a [[Slink]] test or fall [[Prone]] (wasting their movement).
*   *Fictional Interaction:* Can be ignited by `[Fire]`, turning the zone into a raging greasefire.

#### `[Sticky]`
*   *Flavor:* Spider webs, boiling sap, or thick industrial glue.
*   *Universal Baseline:* Inflicts the [[Restrained]] condition (target cannot Move; suffers **-1d** to Dodge).
*   *Fictional Interaction:* Can be burned away by `[Fire]`, clearing the restraint but dealing 1 Grit damage.

#### `[Toxic]`
*   *Flavor:* Serpent venom, bubbling sewer gas, or glowing fungal spores.
*   *Universal Baseline:* Inflicts the [[Weakened]] condition (**-1d** to all action tests).
*   *Fictional Interaction:* Can be washed away with clean water. Ignored by constructs (`Construct`) and undead (`Undead`).

#### `[Wet]`
*   *Flavor:* Splashing water, damp swamp moss, or heavy rain.
*   *Universal Baseline:* Extinguishes the `[Burning]` tag on a creature or zone.
*   *Fictional Interaction:* Conducts electricity (triggers conduction with `[Shock]`), washes away poisons, and increases the difficulty of climbing.

---

### Group 2: Kinetic & Spatial Forces (Movement & Positioning)

#### `[Anchored]`
*   *Flavor:* Heavy gravity, roots wrapping feet, or electromagnetic clamps.
*   *Universal Baseline:* Target cannot move vertically, leap over hazards, fly, or use the `[Teleport]` tag.
*   *Fictional Interaction:* Forces flying beasts to land; keeps incorporeal spirits from phasing through floors.

#### `[Bouncy]`
*   *Flavor:* Rubbery alloys, compressed springs, or gelatinous membranes.
*   *Universal Baseline:* Kinetic ricochet. If a ranged attack using this tag misses, the projectile bounces, making an immediate attack check against a random adjacent target in the [[Zone]]. A projectile can only bounce once per attack.
*   *Fictional Interaction:* Allows gobbos to bounce off walls, adding **+1 Zone** of movement on a jump.

#### `[Crushing]`
*   *Flavor:* High-gravity fields, massive atmospheric pressure, or giant weights.
*   *Universal Baseline:* Compression. Target is slowed to a maximum of 1 Zone of movement. Attacks against the compressed target are [[Easy (4+)]] due to their restricted mobility.
*   *Fictional Interaction:* Collapses wooden structures, triggers cave-ins, and snaps tree branches.

#### `[Elastic]`
*   *Flavor:* Rubbery limbs, stretchy skin, or weirdly double-jointed bones.
*   *Universal Baseline:* Stretch. Increases melee range to Adjacent Zone (1 zone away) and grants a [[Boon (+1d)]] to escape physical restraints.
*   *Fictional Interaction:* Allows reaching high ledges, squeezing through narrow pipes, and bouncing back blunt physical impacts.

#### `[Fast]`
*   *Flavor:* Twitchy legs, high-velocity reflexes, or caffeinated energy.
*   *Universal Baseline:* High speed. Allows moving 1 [[Zone]] as a Free Action once per round.
*   *Fictional Interaction:* Harder to pin down; grants a [[Boon (+1d)]] to Dodge reactions.

#### `[Gale]`
*   *Flavor:* Whirling typhoons, blast valves, or wind spells.
*   *Universal Baseline:* Air current. All ranged attacks passing through the Zone suffer a [[Bane (-1d)]]. The wielder can spend 1 action to push a target to an adjacent Zone.
*   *Fictional Interaction:* Disperses gaseous clouds (`[Gaseous]`), blows away light bulk items, and deflects arrows.

#### `[Heavy]`
*   *Flavor:* Dense lead alloys, black-stone cores, or massive bulk.
*   *Universal Baseline:* Exhausting weight. The wielder suffers a [[Bane (-1d)]] on all tests unless they spend a Standard Action to brace. Target's carrying capacity is halved.
*   *Fictional Interaction:* Sinks instantly in water, collapses thin floors, and anchors items against wind.

#### `[Magnetic]`
*   *Flavor:* Lodestone shards, copper wire windings, or lightning-charged steel.
*   *Universal Baseline:* Pull. Pulls all metal objects or metal-armored creatures (`Corporeal:Metal`) in the Zone to the center. Metal targets suffer a [[Bane (-1d)]] to Dodge.
*   *Fictional Interaction:* Disarms metal weapons, forces iron doors open, and yanks knights into melee range.

#### `[Sinking]`
*   *Flavor:* Quicksand, boiling tar pools, or loose mud.
*   *Universal Baseline:* Downward drag. Any creature entering or moving in the Zone must succeed on a [[Slink]] test or become [[Restrained]].
*   *Fictional Interaction:* Heavy items sink instantly. Can be neutralized by freezing the surface with `[Chilled]`.

#### `[Teleport]`
*   *Flavor:* Purple smoke, folding space, or sudden pops.
*   *Universal Baseline:* Warp. Instantly move 1 Zone, ignoring all intervening obstacles, zones, and enemies.
*   *Fictional Interaction:* Bypasses physical locks, walls, and opportunity attacks.

#### `[Weightless]`
*   *Flavor:* Buoyant gas, levitation runes, or gravity negation.
*   *Universal Baseline:* Levitation. Target ignores vertical terrain, mud, and ground hazards. However, the lack of leverage causes a [[Bane (-1d)]] on Melee attacks.
*   *Fictional Interaction:* Allows crossing chasms, floating to ceilings, and drifting away in heavy wind.

---

### Group 3: Sensory & Mental Distortions (Perception & Focus)

#### `[Blinding]`
*   *Flavor:* Piercing flashes, pocket sand, or burning smoke.
*   *Universal Baseline:* Blindness. Target suffers the [[Blinded]] condition (attacks are Hard [6 only]; Dodge reactions are impossible) for 1 round.
*   *Fictional Interaction:* Clears shadow-camouflage and triggers panic in cave beasts.

#### `[Confusing]`
*   *Flavor:* Swirling colors, off-key humming, or backwards speech.
*   *Universal Baseline:* Bewilderment. Inflicts the [[Dumb]] condition (target cannot cast spells or issue orders; spends actions wandering aimlessly).
*   *Fictional Interaction:* Breaks concentration, ruins coordinated guard ranks.

#### `[Dark]`
*   *Flavor:* Thick shadows, magical gloom, or heavy black smoke.
*   *Universal Baseline:* Poor visibility. All attacks and notice tests in the Zone suffer a [[Bane (-1d)]].
*   *Fictional Interaction:* Can be dispelled by `[Light]`. Enables stealth tests without cover.

#### `[Deafening]`
*   *Flavor:* Thunderstones, shrieking metal, or explosions.
*   *Universal Baseline:* Silence. Target is immune to verbal Mouth/Order actions and cannot hear incoming threats (attacks against them from behind gain a [[Boon]]). A deafened Mob cannot receive [[Orders]] from their Boss.
*   *Fictional Interaction:* Disrupts verbal spellcasting, ruins coordinated troop maneuvers.

#### `[Echoing]`
*   *Flavor:* Hollow cavern chambers, metallic halls, or soundboards.
*   *Universal Baseline:* Amplification. Any noise or sound-based tag (like `[Loud]` or `[Deafening]`) has its duration doubled in this Zone.
*   *Fictional Interaction:* Shatters fragile glass structures if sonic tags are used.

#### `[Light]`
*   *Flavor:* Glowing sun-stones, holy lanterns, or dancing sprites.
*   *Universal Baseline:* Illumination. Strips the `[Dark]` tag from the Zone.
*   *Fictional Interaction:* Blinds shadow-dwelling creatures and triggers panic checks in cave beasts.

#### `[Loud]`
*   *Flavor:* Clattering copper pots, screeching alarms, or whistling gears.
*   *Universal Baseline:* Noise. Automatically fails any Slink/Stealth tests while active.
*   *Fictional Interaction:* Wakes up adjacent zones, alerts sleeping guards, and interrupts quiet spellcasting.

#### `[Phantasmal]`
*   *Flavor:* Shimmering light, auditory illusions, or ghost lights.
*   *Universal Baseline:* Illusion. Target suffers a [[Bane (-1d)]] to all attacks as they swing at illusory copies.
*   *Fictional Interaction:* Has zero physical mass. Can be disbelieved with a [[Brains]] test.

#### `[Shiny]`
*   *Flavor:* Gleaming gold coins, polished brass, or cut gems.
*   *Universal Baseline:* Distraction. Greed-obsessed minds (including player Goblins, dragons, and kobolds) suffer a [[Bane (-1d)]] to attacks/dodge unless they spend their turn moving toward the shiny object.
*   *Fictional Interaction:* Lures guards, distracts monsters, and triggers infighting among mobs.

#### `[Soporific]`
*   *Flavor:* Sweet poppy vapors, rhythmic humming, or sleep dust.
*   *Universal Baseline:* Drowsiness. Target suffers a [[Bane (-1d)]] to all tests. If they roll a Fumble, they fall asleep ([[Stunned]] until damaged).
*   *Fictional Interaction:* Lulls guard beasts, quietens rowdy mobs.

#### `[Tasty]`
*   *Flavor:* Roasted meat aromas, alchemical beast-lure, or sweet blood.
*   *Universal Baseline:* Bait. All beasts (`Beast`) gain a [[Boon (+1d)]] to attack rolls against the target and will prioritize them over all others.
*   *Fictional Interaction:* Triggers ravenous feeding frenzies.

#### `[Terrifying]`
*   *Flavor:* Overwhelming majesty, horror runes, or bloodcurdling shrieks.
*   *Universal Baseline:* Dread. Inflicts the [[Terrified]] condition (target suffers **-1d** to Brains/Mouth and must move away).
*   *Fictional Interaction:* Ignored by mindless constructs and undead.

---

### Group 4: Physiological & Physical Conditions (Health & Hardiness)

#### `[Bleeding]`
*   *Flavor:* Deep gashes, severed veins, or jagged iron wounds.
*   *Universal Baseline:* Lingering harm. The target takes [[1 automatic Grit/Size damage]] at the start of their round until treated.
*   *Fictional Interaction:* Attracts beasts, leaves a clear trail, and is ignored by undead and constructs.

#### `[Exposed]`
*   *Flavor:* Broken guard, off-balance posture, or shattered shields.
*   *Universal Baseline:* Open defense. All attacks against the target are [[Easy (4+)]] and ignore passive defense.
*   *Fictional Interaction:* Represents a perfect opening to strike.

#### `[Feral]`
*   *Flavor:* Beast blood, regression spells, or wild madness.
*   *Universal Baseline:* Beast regression. The target cannot cast spells, use complex items, or speak/issue orders. However, Melee attacks gain **+1 Success**.
*   *Fictional Interaction:* Governed by basic survival instincts.

#### `[Frenzied]`
*   *Flavor:* Boiling blood, red mist, or uncontrollable rage.
*   *Universal Baseline:* Berserk state. Target must spend all standard actions to Move toward and Melee Attack the nearest creature (friend or foe) in melee range on its turn.
*   *Fictional Interaction:* Bypasses self-preservation, ignores pain, and causes the target to break tactical cover.

#### `[Hardened]`
*   *Flavor:* Spiked scales, stone hide, or thick chitin.
*   *Universal Baseline:* Reinforcement. Increases Defence TN by +1 (maximum 5) against `Cutting` and `Poking` attacks.
*   *Fictional Interaction:* Impervious to minor cuts and arrows.

#### `[Itchy]`
*   *Flavor:* Fungal rash, stinging spores, or hives.
*   *Universal Baseline:* Distraction. Frantic scratching. Target cannot use Reactions (no Dodge/Parry) as they scratch.
*   *Fictional Interaction:* Ruin concentration, breaks guard.

#### `[Mindless]`
*   *Flavor:* Lobotomized servants, hollow puppets, or simple plants.
*   *Universal Baseline:* Cognitive void. Immune to `[Spooky]` (fear) and `[Confusing]` (dumb) tags. Cannot take independent actions; must be ordered.
*   *Fictional Interaction:* Unaffected by illusions or mental manipulation.

#### `[Puppet]`
*   *Flavor:* Soul-strings, blood magic, or master-runes.
*   *Universal Baseline:* Domination. The caster can spend 1 [[Standard Action]] on their turn to force the target to perform a Move or basic Attack action on the target's turn.
*   *Fictional Interaction:* Forces enemies to attack their own allies.

#### `[Regenerating]`
*   *Flavor:* Troll blood, rapid cell division, or life-magic.
*   *Universal Baseline:* Rapid healing. Target heals 1 [[Wound]] or 1 [[Grit]] at the start of their turn.
*   *Fictional Interaction:* Cannot regenerate if damaged by `[Fire]` or `[Acidic]` tags this round.

#### `[Rotting]`
*   *Flavor:* Putrid flesh, necrosis, or gangrenous moss.
*   *Universal Baseline:* Decay. The target cannot recover [[Grit]] or heal wounds while this tag is active.
*   *Fictional Interaction:* Smells terrible, spoils food, and ruins non-metal gear over time.

#### `[Spiky]`
*   *Flavor:* Covered in sharp barbs, glass shards, or rusted nails.
*   *Universal Baseline:* Thorns. Any creature attacking the target in Melee takes [[1 automatic success]] (against standard enemies) or [[1 automatic Grit/Size damage]] (against PCs/Bosses/Mobs) on a hit.
*   *Fictional Interaction:* Ruin grappling attempts, damages ropes and nets.

#### `[Swollen]`
*   *Flavor:* Giant mass, muscle bloat, or alchemical growth.
*   *Universal Baseline:* Gigantism. The target's [[Size]] increases by 1. Melee attacks gain a [[Boon (+1d)]], but Slink/Stealth tests suffer a [[Bane (-1d)]].
*   *Fictional Interaction:* Cannot fit through narrow bottlenecks.

#### `[Teeny]`
*   *Flavor:* Pixie dust, shrinking potions, or magic runes.
*   *Universal Baseline:* Shrinking. The target's [[Size]] decreases to 0. Slink/Stealth tests and Dodge tests gain a [[Boon (+1d)]], but carrying capacity is 0.
*   *Fictional Interaction:* Can slip through keyholes and under doors.

---

### Group 5: Metaphysical & Cosmic Anomalies (Reality-Bending Laws)

#### `[Angelic]`
*   *Flavor:* Blinding gold radiance, choral echoes, or pure law.
*   *Universal Baseline:* Holy aura. Attacks against standard foes are [[Easy (4+)]].
*   *Fictional Interaction:* Highly destructive to undead (`Undead`) and demons, reducing their Defence TN by 1.

#### `[Blessed]`
*   *Flavor:* Fortunate whispers, gleaming luck, or a patron's favor.
*   *Universal Baseline:* Good fortune. The target ignores their first Fumble during an encounter.
*   *Fictional Interaction:* Clears minor curses and dark tags on contact.

#### `[Cursed]`
*   *Flavor:* Dark runes, weeping blood, or terrible luck.
*   *Universal Baseline:* Bad fortune. The target fumbles on *any* rolled 1s (rather than needing two 1s).
*   *Fictional Interaction:* Can only be cleared by a Lair ritual or a specialized quest.

#### `[Haunted]`
*   *Flavor:* Lingering ghosts, cold drafts, or phantom hands.
*   *Universal Baseline:* Spectral curse. The target suffers a [[Bane (-1d)]] to Slink and Mouth tests. Any fumbled roll summons a minor ghost (`Undead:Spirit`) that attacks the target.
*   *Fictional Interaction:* Can be cleansed with holy tags (`[Angelic]`) or exorcisms.

#### `[Laggy]`
*   *Flavor:* Temporal distortion, slow-motion fields, or stuttering movements.
*   *Universal Baseline:* Time lag. The target's declared action does not resolve until the End of Round phase.
*   *Fictional Interaction:* Allows allies to interrupt, flee, or block the attack before it hits.

#### `[Linked]`
*   *Flavor:* Sympathetic soul-tethering, silver threads, or blood pacts.
*   *Universal Baseline:* Soul-tether. When two targets are `[Linked]`, any damage or conditions suffered by one are instantly mirrored onto the other. Damage or conditions mirrored by `[Linked]` cannot trigger further `[Linked]` mirrors.
*   *Fictional Interaction:* Allows clever players to harm bosses by attacking linked minions.

#### `[Nullified]`
*   *Flavor:* Anti-magic circles, lead runes, or cold iron anchors.
*   *Universal Baseline:* Dead-zone. Temporarily deactivates all active supernatural traits, magical tags, and oddities in the [[Zone]].
*   *Fictional Interaction:* Turns magic weapons back into normal scrap, shuts down spellcasting.

#### `[Petrified]`
*   *Flavor:* Medusa glare, basilisk breath, or stone-flesh curses.
*   *Universal Baseline:* Stone state. Target is [[Stunned]] (cannot act) but gains +3 Passive Defense dice.
*   *Fictional Interaction:* Target becomes incredibly heavy and brittle to blunt impacts.

#### `[Poofed]`
*   *Flavor:* Banishing smoke, planar rifts, or sudden displacement.
*   *Universal Baseline:* Planar banishment. Target is removed from the map entirely. They return at the start of the next round in the same spot. If the spot is occupied when they return, they appear in the nearest unoccupied space.
*   *Fictional Interaction:* Traps targets in a timeless pocket dimension.

#### `[Purified]`
*   *Flavor:* Healing water, clean sunlight, or restorative runes.
*   *Universal Baseline:* Exorcism. Instantly removes all poison, decay, curses, and diseases from the target.
*   *Fictional Interaction:* Cleanses corrupted objects or defiled zones.

#### `[Revealing]`
*   *Flavor:* Glowing lenses, true-sight dust, or magical lanterns.
*   *Universal Baseline:* Expose. Instantly reveals invisible entities, ignores illusions, and exposes hidden doors.
*   *Fictional Interaction:* Discredits `[Phantasmal]` tags.

#### `[Serene]`
*   *Flavor:* Calming incense, pacifism runes, or angelic presence.
*   *Universal Baseline:* Pacifism. Attacks and violence are impossible in this [[Zone]]; characters must spend 1 [[Grunt]] or 1 [[Grit]] to override the calm.
*   *Fictional Interaction:* Forces negotiations, halts raging mobs.

#### `[Siphoning]`
*   *Flavor:* Vampiric runes, soul-drain valves, or parasitic thorns.
*   *Universal Baseline:* Life drain. Successful attacks recover 1 Grit/Size for the attacker (up to their maximum limit).
*   *Fictional Interaction:* Feeds the wielder's vitality.

#### `[Spectral]`
*   *Flavor:* Intangible, ghost-like properties that allow slipping through physical walls and armor.
*   *Universal Baseline:* Intangibility. Bypasses physical walls and ignores Passive Defense dice from armor.
*   *Fictional Interaction:* Attacker cannot be physically touched or blocked.

#### `[Vile]`
*   *Flavor:* Demonic corruption, defiled blood, or dark runes.
*   *Universal Baseline:* Defilement. Corrupts holy or blessed things, converting them into cursed states.
*   *Fictional Interaction:* Spoils holy water, defiles shrines.

---

### Group 6: Mechanical & Material Flaws (Systemic Failures)

#### `[Bonded]`
*   *Flavor:* Grafted flesh, parasitic spirits, or soul-locked steel.
*   *Universal Baseline:* Soulbind. Once equipped, the item cannot be removed, discarded, or stored.
*   *Fictional Interaction:* Bypasses standard disarm attacks. Removing the item requires a Lair ritual, an amputation, or a specialized GM quest.

#### `[Fragile]`
*   *Flavor:* Brittle clay, cheap alloys, or rusty wires.
*   *Universal Baseline:* Cheap build. Item breaks permanently on a Fumble (ignoring standard durability break checks).
*   *Fictional Interaction:* Shatters under sudden impact or stress.

#### `[Jammed]`
*   *Flavor:* Clogged gears, snapped springs, or dirt in the barrel.
*   *Universal Baseline:* Gridlock. Item cannot be used until a [[Standard Action]] (and a [[Brains]] test) is spent to clear the jam.
*   *Fictional Interaction:* Disables mechanical devices.

#### `[Overcharged]`
*   *Flavor:* Humming power cells, unstable alchemical pressure, or magical feedback.
*   *Universal Baseline:* Volts. Next attack gains **+2 Successes**, then the tag is consumed.
*   *Fictional Interaction:* Risks exploding if the attack fumbles.

#### `[Unstable]`
*   *Flavor:* Nitroglycerin canisters, loose gears, or cursed runes.
*   *Universal Baseline:* Fragility. [[Fumbling]] an action triggers a T3 explosion (`[Explosive]`) in the [[Zone]].
*   *Fictional Interaction:* Detonates at the slightest bump.
