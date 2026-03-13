# Rules Lawyer Audit: Gang Mechanics Brainstorm

**Role:** Rules Lawyer
**Objective:** Audit the `Gang_Mechanics_Brainstorm.md` to identify mechanical conflicts, terminology mismatches, and potential loopholes regarding the current PROD and STAGE rules (`13_Goblin_mob.md`, `15_Death.md`, Tricks, etc.).

## Findings & Conflicts

### 1. "Infamy" vs "Renown"
*   **Conflict:** `15_Death.md` originally used the term **"Renown Level"** to determine stat advances for respawning PCs. The Brainstorm suggested changing this to **"Infamy"**. 
*   **Resolution:** Executed a find-and-replace across all STAGE and PROD documents to change "Renown" to "Infamy" to maintain keyword consistency.

### 2. The "Hoard" & Outfitting Mobs
*   **Observation:** The Brainstorm suggests outfitting a Mob from "The Hoard" before a raid. `13_Goblin_mob.md` (Stage) has a strict **Mob Equipment & Loot Tradeoff** rule where equipping a Mob with armor/weapons directly reduces their **Loot Capacity** by an equal amount of Bulk.
*   **Resolution:** The game designer confirmed this is a **Feature, not a bug**. Players *can* outfit their Mob with heavy armor and weapons to make them harder to kill, but they actively sacrifice their ability to carry raid loot back. It forces a strategic choice between survival and greed.

### 3. The "Inspiration" & "Relic" System (The Bone Pile)
*   **Conflict:** Allowing a new Boss to keep an old Trick ("Inspiration") circumvents the strict Trick limits established in `14_Tricks.md` (if they bring a Trick over, does it count against their new Boss's maximum?). 
*   **Conflict:** The Brainstorm mentions attaching a Bone to an item to create a Relic. We currently do not have a robust "Item Slots" or "Attunement" system in standard gear. If Relics stack, a player could theoretically wield 5 Relics and break the game.
*   **Resolution:** The game designer confirmed a **1 Relic limit** is a good starting point. We also need to define that "Inspiration Tricks count toward your maximum Trick limit." when drafting the final rules.

### 4. Gang "Quirks" & The "Frenzy/Go-go-go" Pool
*   **Conflict:** The brainstorm suggests rewarding players with "Grit or Tricks" for leaning into Quirks. Granting permanent Tricks mid-raid breaks the progression economy. Granting "Grit" is acceptable, but Grit is currently tied to personal Boss stamina, not Mob chaos. 
*   **Action Required:** As noted by the user, we need a distinct **"Frenzy Pool"** keyword. This pool should be mechanically separate from Grit (Boss stamina). We must define what Frenzy can be spent on (e.g., extra Mob actions, automatic successes on 'For Fuck Sake' mob behavior) before implementing Quirks.

### 5. Inter-Gang Rivalries (PvP Mechanics)
*   **Conflict:** The core rules assume the Bosses are generally cooperating on a Raid to get Loot back to the Lair. If Gangs can place "Wagers" or sabotage each other, we need strict PvP resolution mechanics. Currently, we use opposed tests, but Mob vs Mob PvP is lethal. In `13_Goblin_mob.md`, "Cross-Gang Merging" results in 1 Damage per rolled '1' due to in-fighting.
*   **Resolution:** The game designer agreed. Rivalries will be kept strictly to the *Lair phase* (e.g., competing for Upgrades or Hoard items) to prevent raids from deteriorating into total player kills.

### 6. The Mob Mutiny Gauge
*   **Conflict:** We already have an "Uncontrolled Mob" mechanic in `13_Goblin_mob.md` (Survival > Loot > Violence > Trash). If a Mob Mutinies, do they become Uncontrolled, or do they instantly execute the Boss?
*   **Action Required:** Tie "Mutiny" directly to the existing "Inherent Nature" priority list. A Mutiny should simply trigger the Uncontrolled state with a permanent "-1d" to Re-commanding them until they are bribed with Loot.

## Conclusion
The brainstorm introduces excellent flavor, but it stretches across Boss Economy (Tricks/Grit), Base Building (Hoards/Turf), and Mob Mechanics (Mutiny/Quirks). We must isolate these into distinct STAGE documents to prevent overlapping rules. The most urgent technical debt is defining the "Frenzy" pool to support the Quirk/Chaos loop.
