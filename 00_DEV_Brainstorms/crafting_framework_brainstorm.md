# Crafting Framework & Oddities Brainstorm

## The Core Concept
The idea is to take a **Base Item** (like those found in `33_Equipment.md`), gather **Scrap** (just a generic, stackable resource), and tape **Oddities** (unique bits of junk that provide specific traits) onto it.

### Your Brain Limits Your Chaos
*   **Brains Stat & Utility Slots:** As noted in `10_Stats.md`, your Brains score gives you "Utility Slots." These slots represent your capacity to manage, maintain, and wield dangerously complex contraptions.
*   **Rule Suggestion:** An item can have a number of attached Oddities up to a maximum equal to the wielder's **Brains**. If a Goblin with Brains 1 tries to pick up a weapon that has 3 attached Oddities, they can't figure out how to pull the triggering mechanisms and it acts as a clumsy paperweight.

### The True Cost: Quality Degradation
To balance the chaos of taping a "Fiery" oddity to a "Bouncy" oddity to a Heavy Hammer, we weaponize the **Quality** mechanic (`33_Equipment.md`).
*   **The Baseline:** A "Goblin Made" item breaks on a roll of 1 on the gear dice.
*   **The Oddity Tax:** Each Oddity attached to a weapon increases the "Break Chance" threshold by 1 on the die.
    *   *0 Oddities:* Breaks on a 1.
    *   *1 Oddity:* Breaks on 1-2.
    *   *2 Oddities:* Breaks on 1-3.
    *   *3 Oddities:* Breaks on 1-4.
*   *Why this works:* It creates an incredible burst of temporary power. The player gets a super-weapon, but it is statistically guaranteed to blow up in their hands soon. It balances itself through imminent destruction, forcing the player to scavenge again.

---

## GM Scaffolding Framework
Players *will* combine things you didn't anticipate. Here is a 3-step scaffold for the GM (the "Rules Lawyer") to adjudicate any combination on the fly.

**Step 1: Determine the Base Skeleton**
Always start with the underlying item. This provides the fundamental stats (Bulk, Handedness, base Damage output). 
*e.g., A "Medium Weapon" (Bulk 2, One-Handed, +3d Damage).*

**Step 2: Apply the Tags (The Oddities)**
Read the Oddities tags sequentially. Do *not* overthink the physics. If the Oddity says "Bouncy," the weapon now bounces. If it says "Fiery," it sets things on fire. Let the narrative form naturally from the tags.
*e.g., Medium Weapon + Bouncy + Fiery = A fiery hunk of metal that bounces between targets.*

**Step 3: Define "The Exploit" and "The Rebound"**
The final step is to determine the immediate mechanical effect on a **Hit** vs. a **Fumble/Break**.
*   **Hit (The Exploit):** What cool thing happens? (e.g., The Bouncy Fire-Hammer hits two targets in the same zone).
*   **Fumble/Break (The Rebound):** What awful thing happens when it shatters? (e.g., It explodes in a fiery blast, hitting the Goblin and anyone nearby).

---

## d66 List of Oddities
Here is a starting list of 36 distinct Oddities that players can find out in the world, categorized by their dominant feature.

| d66 | Oddity Name | The Tag / Effect |
| :--- | :--- | :--- |
| **11** | **Bouncy Gland** | **Bouncy:** Can be thrown into an adjacent zone and returns to hand. On a miss, it hits a random target in the zone. |
| **12** | **Sticky Sap** | **Sticky:** Target hit cannot willingly move to a new zone next round. |
| **13** | **Heavy Core** | **Heavy:** +1d Damage, but increases the item's Bulk by +1. |
| **14** | **Screeching Whistle** | **Loud:** Forces a morale/rout test on Mobs it hits, but breaks stealth instantly for the whole group. |
| **15** | **Rusty Spring** | **Propelled:** Extends melee reach to an adjacent zone, or adds +1d to movement actions. |
| **16** | **Floaty Bladder** | **Light:** Reduces the item's Bulk by -1 (minimum 0). |
| **21** | **Spark Battery** | **Shocking:** Ignores any armor based on metal. Target drops whatever they are holding. |
| **22** | **Volatile Ooze** | **Acidic:** Destroys enemy armor on a critical hit, but destroys your armor if it breaks. |
| **23** | **Spicy Pepper Box** | **Blinding:** Characters hit lose their passive defense dice for the round. |
| **24** | **Magnetic Shard** | **Pulling:** Pulls metallic items from an adjacent zone towards you. |
| **25** | **Glow Worm Jar** | **Blazing:** Illuminates the darkness. Dazzles targets in melee (+1d to hit them). |
| **26** | **Chilling Frost-Stone** | **Freezing:** Extinguishes fires. Target hit loses 1 action next turn due to shivering. |
| **31** | **Spiked Carapace** | **Jagged:** Rolls of 6 deal 1 bleeding wound to the target. |
| **32** | **Twitchy Muscle** | **Alive:** +1d to hit, but requires a Slink test to put the item down safely without it biting you. |
| **33** | **Venom Gland** | **Toxic:** Deals damage over time, ignoring Grit entirely (requires an antidote). |
| **34** | **Stretchy Sinew** | **Whip-like:** Can hit two targets in your current zone with a single strike. |
| **35** | **Bone-Crushing Vise** | **Crushing:** +2d Damage against targets with passive defense dice (armor), -1d against unarmored. |
| **36** | **Puffball Spore** | **Choking:** Creates a cloud in the zone; all actions inside lose -1d next round. |
| **41** | **Clockwork Gyro** | **Whirling:** Allows an attack against all enemies in the zone, but also hits all allies. |
| **42** | **Telescoping Tube** | **Extending:** Can strike enemies anywhere in line-of-sight, but takes 1 action to retract. |
| **43** | **Mirror Shard** | **Reflective:** Can bounce ranged attacks back at the attacker on a critical defense. |
| **44** | **Pressure Valve** | **Steaming:** Pushes targets out of your zone into an adjacent zone on a hit. |
| **45** | **Alchemical Primer** | **Explosive:** Converts single-target damage to an area-of-effect blast (entire zone), but always breaks on a 1-3. |
| **46** | **Fragile Glass Hull** | **Shattering:** Does massive +3d damage, but breaks automatically after 1 successful hit. |
| **51** | **Goblin-Bite Clamp** | **Latching:** Clamps onto the target. You gain +2d to all subsequent attacks against them, but you are attached to them. |
| **52** | **Rat-Skull Rattle** | **Spooky:** Targets must pass a Brains test to willingly attack you in melee. |
| **53** | **Thick Sludge** | **Gooey:** Absorbs impacts. If attached to armor, halves incoming damage but restricts Movement. |
| **54** | **Screaming Crystal** | **Shatter-Sonic:** Deals damage directly to Mobs instead of Bosses, bypassing their human shields. |
| **55** | **Hollowed Horn** | **Amplifying:** Any order given through this item gives a built-in +1d boon to your Mobs. |
| **56** | **Void-Touched Rock** | **Teleporting:** Swap places with the target upon a successful hit. |
| **61** | **Troll-Blood Vial** | **Regenerating:** Weapon repairs itself at the end of combat (negates one break). |
| **62** | **Shiny Coin Slot** | **Greedy:** Deals +1d damage for every piece of treasure/loot you shove into it before attacking. |
| **63** | **Boomerang Fin** | **Curving:** Ignores any cover the target might be hiding behind. |
| **64** | **Stolen Magic Wand** | **Erratic:** Roll a d6 after every attack. On a 1, you turn pink. On a 6, the target turns into a sheep. |
| **65** | **Giant's Toenail** | **Massive Force:** Any target hit is immediately knocked prone. |
| **66** | **The Red Button** | **Panic:** Does something spectacular and devastating (GM's discretion), but breaks the item permanently and irreparably. |
