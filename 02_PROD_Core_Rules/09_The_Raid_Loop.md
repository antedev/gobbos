# The Raid Loop & Economy

*A goblin without a plan gets squashed. A goblin with a plan gets squashed while carrying something shiny. The raid is the lifeblood of the Warren—a high-stakes smash-and-grab where Bosses lead their Mobs into hostile territory to plunder riches, smash infrastructure, and haul back enough scrap to keep the Lair growing.*

---

## 1. The Four Raid Phases

Every raid operates within a continuous four-phase loop that structures the transition from the **Lair** to the target site and back again:

```mermaid
flowchart TD
    P1["Phase 1: Planning & Approach (The Journey)<br>- Select scouted target & review Danger Ratings<br>- Mobilize Raider Mobs & assign Travel Roles<br>- Traverse travel Stages to reach raid site"] --> P2["Phase 2: Infiltration & Assault (Entry & Breach)<br>- Establish starting Alert equal to Danger Rating (1–5)<br>- Infiltrate initial Zones & bypass sentries"]
    P2 --> P3["Phase 3: Objective & Plunder (Tactical Execution)<br>- Complete Main Objective (3–5 Raid Points)<br>- Pursue Opportunity Targets (+2 Raid Points each)<br>- Dismantle infrastructure for Scrap & Plunder Loot"]
    P3 --> P4["Phase 4: Extraction & Escape (The Return)<br>- Declare extraction & retreat through Zones to exit<br>- Haul physical Loot/Scrap through Return Journey<br>- Manage encumbrance & pursuing forces"]
```

### Phase 1: Planning & Approach
Before leaving the **Lair**, you select a scouted target, inspect the known **Base Danger Rating** and **Objectives**, allocate **Raider Mobs** from the communal **Gobbo Pool** (up to your Boss's **Grunt** limit), and assign the four **Travel Roles**. The party then traverses wilderness or subterranean **Stages** as detailed in [Journeys & Hazards](11_Journeys_and_Hazards.md).

### Phase 2: Infiltration & Assault
The party breaches the target perimeter. The **GM** sets the location's starting **Alert** track equal to its **Base Danger Rating** (1 to 5). You navigate connected **Zones**, defeat sentries, bypass obstacles, and work to keep **Alert** low before sounding alarms.

### Phase 3: Objective & Plunder
The party executes tactical combat and exploration actions in the target **Zones**. You secure the **Main Objective** (worth 3–5 **Raid Points**), seek optional **Targets of Opportunity** (worth +2 **Raid Points** each), dismantle heavy machinery or architecture for **Scrap**, and spend **Plunder** **Standard Actions** to gather loose **Loot** and **Oddities**.

### Phase 4: Extraction & Escape
Once objectives are secured, or when **Alert** escalates to lethal levels, the party declares **Extraction**. You must haul all gathered physical **Loot**, **Scrap**, and **Oddities** back through the perimeter to the exit, managing encumbrance penalties and fighting off pursuers before resolving the return journey.

---

## 2. The Raid Economy

The **Gobbos** economy operates without fractional coinage or coin-counting math. Wealth and progress are measured across five standardized systemic resources:

| Resource | Scope | Acquisition Method | Primary Mechanical Function |
| :--- | :--- | :--- | :--- |
| **Loot Value (LV)** | Liquid Wealth | Plundered as physical items during raids | Smelted via Rule of Five; buys equipment, hires specialists, expands Lair facilities. |
| **Scrap** | Building Matter | Harvested from broken infrastructure and salvage | Constructs facility chassis, expands rooms, and provides base weapon materials. |
| **Infamy Marks** | Gang Level | Contributed Loot (10 LV = 1 Mark) or Agendas | Determines Gang Infamy (1–5), Successor starting XP, and equipped Gang Quirks. |
| **Raid Points (Glory)** | Shared Renown | Completing Main and Opportunity Objectives | Pooled at raid end; converts into shared **Boss XP** during Homecoming. |
| **Boss XP** | Personal Power | Pooled Raid Points, Personal Glory, Successor pools | Spent during downtime to advance **Main Stats** (**Tough**, **Slink**, **Brains**, **Mouth**). |

---

## 3. Loot Value & The Exponential Scale

All treasure plundered from a raid belongs to a **Quality Tier (T1–T5)** and possesses a **Loot Value (LV)** representing its concentrated material worth.

### The 5-to-1 Tier Ladder
Each tier represents an exponential **5-to-1 step** in value. Lower-tier items cannot bypass higher-tier economy gates without combining them in groups of five:

| Tier | Category & Quality | Single Unit Value | Typical Raid Plunder |
| :---: | :--- | :--- | :--- |
| **T1** | **Junk & Pocket Scrap** | 1x T1 | Brass buttons, bent iron nails, tin mugs, loose teeth. |
| **T2** | **Scrappy Plunder** | 5x T1 (1x T2) | Silver cutlery, iron shivs, copper kettles, crude pewter rings. |
| **T3** | **Standard Fine Treasure** | 25x T1 (5x T2 / 1x T3) | Gold banquet chalices, guard broadswords, bolts of fine silk. |
| **T4** | **Superior Masterwork** | 125x T1 (5x T3 / 1x T4) | Dwarven rune-hammers, jeweled altar idols, black pearl necklaces. |
| **T5** | **Legendary Mythic Relic** | 625x T1 (5x T4 / 1x T5) | Dragon skull trophies, intact godstone shards, astral astrolabes. |

### Multi-Unit Treasures & Hoards
Massive treasures possess a **Loot Value** greater than 1 of their Tier:
* A stolen **Alabaster Sarcophagus** might be valued at **4x T4**.
* Under the exponential scale, that single sarcophagus is worth:
  **4x T4** = **20x T3** = **100x T2** = **500x T1**
* This scale prevents hoarding loose Junk (T1) from trivializing high-tier economic purchases without physical smelting.

---

## 4. The Rule of Five: Smelting & Barter

During the **Lair Phase** (downtime between raids), you can combine, melt down, or break apart plunder using the **Rule of Five**:

1. **Trading Up (Smelting / Combining):** You combine **5 tokens of Tier X** into **1 token of Tier X+1**.
   * *Example:* 5x T2 silver goblets melt down into 1x T3 gold ingot.
2. **Trading Down (Breaking Down / Pawning):** You break down **1 token of Tier X+1** into **5 tokens of Tier X**.
   * *Example:* 1x T4 masterwork brooch trades down into 5x T3 trade bars.

>> **THE RULE OF FIVE RESTRICTION:**
>> Smelting upward requires exact multiples of five. Non-multiples of five cannot be traded up to the next tier until additional matching tokens are acquired.

---

## 5. Scrap Generation & Conversion

**Scrap** is abstract structural building matter (reclaimed iron plates, oak beams, lead pipes, chains, and masonry) required to construct Lair facilities, build defenses, and form custom weapon chassis.

### Generating Scrap
1. **Dismantling Infrastructure:** During a raid, a **Goblin Boss** or **Mob** can spend a **Standard Action** (**Manipulate** or **Attack**) to dismantle environmental objects (iron doors, portcullises, chandeliers, ballistas). A successful **Tough 5+/1** or **Brains 5+/1** test extracts **1d6 Scrap** (or the object's listed yield) into the party's carry load.
2. **Salvage Yields:** Plundered items with high structural bulk can be smelted down in the Lair. Dismantling a plundered item yields its listed **Scrap Yield** into the **Communal Hoard**.
3. **Passive Lair Yields:** Dedicated Lair facilities (such as the Junkyard Sifter or Scrap Forge) generate passive **Scrap** each **Lair Turn**.

---

## 6. Carry Capacity & Tactical Encumbrance

Greed has physical weight. All weapons, armor, tools, and plunder possess a **Bulk** rating (0 to 4+). 

### Goblin Boss Carry Capacity
Your unburdened **Carry** capacity is derived from your **Tough** stat:

**Carry Capacity** = **4 + (2 x Tough) Bulk**

| Tough Stat | Unburdened Carry | Over-Laden Threshold | Dragging Limit (2x Carry) |
| :---: | :---: | :---: | :---: |
| **Level 1** | **6 Bulk** | 7–7 Bulk | 12 Bulk |
| **Level 2** | **8 Bulk** | 9–10 Bulk | 16 Bulk |
| **Level 3** | **10 Bulk** | 11–13 Bulk | 20 Bulk |
| **Level 4** | **12 Bulk** | 13–16 Bulk | 24 Bulk |
| **Level 5** | **14 Bulk** | 15–19 Bulk | 28 Bulk |

### Load States & Penalties
Total the **Bulk** of all carried weapons, armor, gear, and plunder to determine your current **Load State**:

* **Unburdened (<= Carry):** Standard **Movement** speed (in Zones per **Move** action); zero test penalties; full access to all standard actions and reactions.
* **Over-Laden (Carry + 1 to Carry + Tough):** **-1 Zone** per **Move** action (minimum 1 Zone); **Bane 1 (-1d)** on all physical **Slink** and **Tough** tests; you cannot perform two **Move** actions in the same round.
* **Dragging (Carry + Tough + 1 to 2x Carry):** Fixed at **1 Zone** per **Move** action; auto-fails all stealth and jumping tests; requires **two hands**; you cannot attack with weapons and cannot perform **Dodge** or **Parry** **Reactions** (0 active defense).
* **Immobilized (> 2x Carry):** **0 Zones** movement speed; you cannot move and must drop carried items as a **Free Action** to regain mobility.

### The Bulk 3+ Item Rule
Items of **Bulk 3 or higher** (iron safes, great cauldrons, stone statues, heavy kegs) represent awkward, heavy loads:
* **Two Hands Required:** Hauling a loose Bulk 3+ item occupies two hands. You cannot wield a weapon, hold a shield, or cast somatic spells while carrying it.
* **No Disengage:** You cannot perform a **Disengage** action while holding a Bulk 3+ item. You must drop the item as a **Free Action** to disengage, defeat adjacent enemies, or take Opportunity Attacks.
* **Boss Hauling Limit:** A **Goblin Boss** can haul at most Tough / 2 (rounded down, minimum 1) loose Bulk 3+ items at one time.

### Mob Carry Limits & Casualties
* **Unburdened Mob Limit:** A **Mob** carries up to **Size x 4 Bulk** with normal movement and no penalties.
* **Dragging Mob Limit:** A **Mob** can drag up to **Size x 5 Bulk** (movement fixed at 1 Zone per **Move** action; cannot execute the reactive **Scatter!** order).
* **Mob Combat Penalty:** Every loose object of **Bulk 3+** carried by a **Mob** imposes **Bane 1 (-1d)** on that **Mob's** attack rolls. A **Mob** can carry a maximum number of Bulk 3+ items equal to its current **Size**.
* **Casualty Drops:** When a **Mob** takes damage that reduces its **Size**, its carry capacity shrinks immediately. The controlling **Goblin Boss** must **immediately declare which Loot items are dropped** in the current **Zone** to meet the new capacity ceiling. Picking dropped items back up requires spending a **Plunder** **Standard Action** per item.

---

## 7. Danger Scaling, Scouting & Alert

Raids scale dynamically based on site danger and the party's operational profile.

### Base Danger Rating (1 to 5)
Every raid target has a **Base Danger Rating** (T1 to T5) that sets its starting **Alert** level, baseline environmental hazard profiles, and enemy strength.

### Scouting the Target
During the Labor step of the **Lair Phase**, players allocate **Laborer Dice** to survey a target site. Roll the allocated pool against **4+**:

* **0 Successes (Blind Entry):** The location exists, but the party knows nothing. The party suffers a **Bane 1 (-1d)** on their first Zone entry test during the raid.
* **1 Success:** Reveals the **Base Danger Rating** and the **Main Objective** (worth 3–5 **Raid Points**).
* **2 Successes:** In addition to the above, reveals 1 **Target of Opportunity** (worth +2 **Raid Points**).
* **3+ Successes:** In addition to the above, reveals 2 **Targets of Opportunity** (+4 **Raid Points** total) and a **Secret Bypass** (grants the party a **Boon 1 (+1d)** on their first Zone entry test).

### The Alert Track
The **GM** tracks the raid location's active **Alert** (starting equal to the **Base Danger Rating**):
* **Alert Check Triggers:** The **GM** rolls **1d6** whenever the party enters a new **Zone**, completes a **Target of Opportunity**, or takes a rest round.
* **Resolution:**
  * If the roll is **strictly greater** than current **Alert**: The party remains undetected.
  * If the roll is **less than or equal to** current **Alert**: A complication triggers (reinforcements arrive, alarms sound, or traps arm), and **Alert** permanently increases by **+1**.

---

## 8. Post-Raid Reckoning & Payout

When the party extracts safely back to the **Lair**, rewards are tallied across three separate tracks:

### 1. Communal Glory to Shared Boss XP
All **Raid Points** earned by the party from completing objectives are pooled and converted into shared **Boss XP**:

| Pooled Raid Points | Shared Boss XP Awarded | Raid Reputation |
| :---: | :---: | :--- |
| **1–4 Points** | **0 XP** | Failure. The horde throws mud at the returning raiders. |
| **5–9 Points** | **1 XP** | Decent raid. The horde acknowledges the plunder. |
| **10+ Points** | **2 XP** | Legendary triumph! A feast is held in your honor. |

### 2. Personal Glory (+1 XP)
A **Goblin Boss** earns **+1 Personal Glory** (maximum 1 per raid, converting to **+1 XP** during Homecoming) by fulfilling at least one of these chaotic acts:
* **The Compulsion:** Voluntarily trigger your Gang's **Shenanigan** compulsion in an disadvantageous tactical situation, causing a complication and adding a die to the communal **Bangaranga Pool**.
* **The Sacrifice:** Completely destroy a custom gear item by declaring an **Overclock**.
* **The Tyrant:** Use the **Assert Dominance** action (attacking a **Mob** under your command) to regain **Grunt** in combat.
* **The Martyr:** Roll a **Fumble** or trigger **Overreaching** when rolling dice, yet survive the raid.

### 3. Communal Hoard Deposit vs. Private Gang Hoard
* **Communal Hoard:** All standard **Loot Value** and **Scrap** gathered by the party is deposited into the **Communal Hoard**. Contributing 10 **Loot Value** to the Communal Hoard earns your Gang **1 Infamy Mark**.
* **Oddity Drafting:** Rare **Oddities** extracted from the raid are placed on the table and distributed by **Player Consensus**. If an **Oddity** was physically carried out by a specific **Mob**, that **Mob's** controlling Gang holds **First Pick** rights.

---

## 9. Loot & Salvage Structural Schema

Every plundered treasure, scrap cache, or harvested monster oddity is defined by the following structural template:

```markdown
### [Item Name]
- **Category:** [Pocket Scrap | Scrappy Plunder | Fine Treasure | Masterwork | Mythic Relic | Oddity | Chassis | Consumable]
- **Quality Tier:** [T1 Junk | T2 Scrappy | T3 Standard | T4 Superior | T5 Legendary]
- **Bulk:** [0 | 1 | 2 | 3 | 4+]
- **Loot Value (LV):** [Quantity of Tier units, e.g. 1x T1, 1x T2, 3x T3, 1x T5]
- **Scrap Yield:** [Quantity of Scrap recovered if dismantled in Lair]
- **Divisibility:** [Divisible | Indivisible]
- **Special Utility / Crafting Tag:** [Attached Oddity (Tier/Bite), Weapon/Armor Tag, or Blueprint schematic]
- **Description:** [Brief physical Tier B/C description]
```

### Reference Plunder Instances

#### Bent Brass Nails
- **Category:** Pocket Scrap
- **Quality Tier:** T1 Junk
- **Bulk:** 0
- **Loot Value (LV):** 1x T1
- **Scrap Yield:** 1 Scrap
- **Divisibility:** Divisible
- **Special Utility / Crafting Tag:** None
- **Description:** *A pocketful of bent, tarnished brass nails pried from floorboards.*

#### Gilded Silver Chalice
- **Category:** Fine Treasure
- **Quality Tier:** T3 Standard
- **Bulk:** 1
- **Loot Value (LV):** 1x T3
- **Scrap Yield:** 2 Scrap
- **Divisibility:** Indivisible
- **Special Utility / Crafting Tag:** None
- **Description:** *A heavy silver banquet cup lined with gold filigree and small garnet beads.*

#### Flame Drake Bile Gland
- **Category:** Oddity
- **Quality Tier:** T4 Superior
- **Bulk:** 2
- **Loot Value (LV):** 1x T4
- **Scrap Yield:** 0 Scrap
- **Divisibility:** Indivisible
- **Special Utility / Crafting Tag:** [Fire] (Tier 4, Bite 3, [Searing] Tag)
- **Description:** *A pulsating, smoking organ harvested from a drake carcass. Warm to the touch.*

---

## Content Extension Point

[CONTENT EXTENSION POINT: Loot & Salvage Items]

All future compendiums of treasures, trade goods, monster harvest oddities, relics, and scrap caches must implement the Loot & Salvage Structural Schema defined above, respecting Quality Tiers (T1–T5), Bulk encumbrance rules, and Scrap yields.

---

## Mechanical Gaps & Unresolved Systems

[MISSING RULE / GAP: Economy Currency Normalization & Tiered Conversion]
*   **Description:** Stage drafts define Loot Value on a 5-to-1 exponential scale (T1–T5), but Lair construction rules list flat costs like "10 Loot, 15 Scrap" and Gang progression awards 1 Infamy Mark per "10 Loot Value" contributed. If a single T5 Relic equals 6,250 T1 units, depositing one T5 item would grant 625 Infamy Marks, instantly maxing Gang Infamy 40 times over.
*   **Why it is needed:** The macro progression and Lair construction loops collapse into hyper-inflation or complete ambiguity if currency tiers are not strictly normalized.
*   **Suggested Resolution:**
    1. Define all flat Lair construction costs in matching Tier tokens (e.g., Tier 2 rooms cost T2 tokens, Tier 3 rooms cost T3 tokens).
    2. Normalize Infamy Mark generation to require 10x T1 for Infamy 1, 10x T2 for Infamy 2, 10x T3 for Infamy 3, 10x T4 for Infamy 4, and 10x T5 for Infamy 5.

[MISSING RULE / GAP: Codified Extraction Phase & Chase Mechanics]
*   **Description:** While Journey rules handle travel to and from the site, there is no formal mechanical procedure for the transition between dungeon combat/plunder and extraction. If Alert reaches 4 or 5, there are no rules for whether enemies chase the party into the return journey, or how players disengage from the dungeon node to start return stages.
*   **Why it is needed:** The "Extraction & Escape" phase is one of the four core raid pillars, but currently lacks dedicated evasion mechanics.
*   **Suggested Resolution:** Define the Extraction Trigger: Once the party declares Extraction, each Zone between their current location and the entrance must be traversed. If Alert is 4+, each exit transition triggers an immediate Slink 5+/1 evasion test; failure inflicts 1 Attrition damage on all Mobs and carries +1 Alert into the Return Journey.

[MISSING RULE / GAP: Private Gang Hoard vs. Communal Hoard Economy]
*   **Description:** The Skim Downtime Action allows a Boss to secretly divert Loot into the Gang's Private Hoard. However, the rules never define what a Gang's Private Hoard can be spent on versus the Communal Hoard, or whether Private Hoard wealth counts toward Infamy Marks.
*   **Why it is needed:** Without distinct mechanical uses (e.g. purchasing personal gear without table consensus, bribing Elders for personal perks, or buying unshared Mob upgrades), the Skim action has no tactical purpose.
*   **Suggested Resolution:** Clarify that the Communal Hoard is spent strictly by group consensus for Lair upgrades and shared outfitting, while a Gang's Private Hoard is spent exclusively by that player to purchase personal gear, bribe Elders, or buy personal Mob equipment. Wealth in the Private Hoard only grants Infamy Marks when deposited into the Communal Hoard.
