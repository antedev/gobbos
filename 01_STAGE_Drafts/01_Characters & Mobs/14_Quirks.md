# 14. Quirks & Twists

> **THIS SECTION IS TO BE CONSIDERED A BIT OUTDATED. ALL THE RULES AROUND STILL CHANGE THAT WILL AFFECT THIS. THIS IS THEREFORE NOT TO SEEN AS A BLOCKER TO OTHER RULE CHANGES, BUT RATHER WE WILL COME BACK AND FINISH THIS ONCE ALL THE OTHER RULES ARE SOLIDIFIED.**

*Goblins don't fight fair. They fight weird. When a tall-man swings a shiny sword, a goblin Boss doesn't block it—they duck, bite their ankle, and shove a friend in the way.*

**Quirks** are unique personal abilities that allow a Boss to manipulate dice outcomes, bypass combat restrictions, or alter the action economy. A **Quirk** is a modular base action. The true chaos happens when you attach a **Twist**—a modifier that alters how the **Quirk** works, creating a customized, volatile combination.

All **Quirks** and **Twists** are governed by the modular structure detailed in [16. Unified Modular Powers System](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md).

---

## 1. Acquiring Quirks & The Limit

To prevent Bosses from forgetting their own chaotic repertoire mid-raid, a Boss is strictly limited in how many personal **Quirks** they can maintain.

*   **The Personal Limit:** A Boss can hold a maximum of **3 Personal Quirks**.
*   **Twist Limits:** Each **Quirk** can hold exactly **1 Twist**. 

### Progression
New **Quirks** and **Twists** are acquired and upgraded during downtime:
1.  **Character Creation:** A newly rolled Boss starts with **1 Basic Quirk** of their choice, and **0 Twists**.
2.  **Leveling Up:** Every time a Boss permanently upgrades *any* stat by 1 point, they may choose to:
    *   Learn 1 new **Quirk** (if under the cap of 3).
    *   Learn 1 new **Twist** and attach it to an existing **Quirk**.
    *   Upgrade an existing **Quirk** or **Twist** to a higher **Tier**.

### Stat Gating (Tier Requirements)
**Quirks** and **Twists** are rated by **Tier (T1–T5)**. To learn or upgrade to a **Tier** X **Quirk** or **Twist**, the Boss's underlying relevant Stat (**Tough**, **Slink**, **Mouth**, or **Brains**) must be equal to or greater than X.
> **Example:** To learn the **T3** **Tough** **Quirk** **Head Chopper**, you must have **Tough** 3 or higher.

---

## 2. Gang Quirks & Infamy

**Gang Quirks** are powerful, legendary abilities that belong to the **Gang** as a whole. They are acquired when a Boss reaches Level 6 in any stat and retires as an **Elder**, or dies gloriously and joins the **Pile of Bones** (see [12. Gangs](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/12_Gang.md)).

*   **The Infamy Limit:** **Gang Quirks** **do not** count toward a Boss's personal limit of 3. Instead, the maximum number of **Gang Quirks** a starting Boss can bring on a raid is determined by the **Gang**'s **Infamy** score. 

---

## 3. Activation Costs

To use a **Quirk**, the Boss must pay its associated cost (detailed in [16. Unified Modular Powers System](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md)):
*   **[Cost: Passive]** - The **Quirk** is always active or triggers automatically based on a stated condition. It costs zero actions or **Grunt**.
*   **[Cost: Grunt]** - The Boss must spend the stated number of **Grunt** points to activate the **Quirk**.
*   **[Cost: 1 Action]** - The Boss must spend one of their Standard Actions (Move, Attack, Order) to activate the **Quirk**. 

---

## 4. Example Quirks (Base Atoms)

The following **Quirks** are assembled using the successes and condition standards of the modular powers toolkit.

### Tough Quirks
*   **Meat Shield (T1) | [Cost: 1 Grunt]**
    *   *Trigger:* When you take a **Wound** from an incoming attack.
    *   *Effect:* Instantly shove an allied **Mob** in your **Zone** into the way. The **Mob** takes the hit instead (losing **1d3** **Mob** **Size**), and you take **0 Wounds**.
*   **Butcher (T2) | [Cost: Passive]**
    *   *Effect:* Gain **+1 Boon Die** when making an Attack test against an enemy whose Size is strictly smaller than yours.

### Slink Quirks
*   **Ankle-Biter (T1) | [Cost: Passive]**
    *   *Trigger:* Whenever you successfully Dodge an incoming attack.
    *   *Effect:* You may immediately make a free melee attack against the attacker's legs (if they are in your **Zone**) adding **+1 Success** to the attack roll.
*   **Slippery (T2) | [Cost: Passive]**
    *   *Effect:* Enemies do not get free reactionary Opportunity Attacks against you when you leave their **Zone**.

### General Quirks
*   **Coward's Luck (T1) | [Cost: 1 Grunt]**
    *   *Trigger:* After you roll the dice pool for any test.
    *   *Effect:* Spend 1 **Grunt** to completely reroll all dice that did not land on a 1 (You cannot reroll **Fumbles**).
*   **Iron Stomach (T1) | [Cost: Passive]**
    *   *Effect:* You can carry up to **2 Bulk** worth of items by swallowing them. Swallowed items do not count toward your Carry Capacity. *It requires 1 Action to regurgitate them.*

---

## 5. Example Twists (Modifiers)

**Twists** modify the behaviors of **Quirks** to add utility, change delivery, or adjust action costs.

*   **Spiteful (T1)**
    *   *Effect:* Whenever the attached **Quirk** is activated, deal **1** **Grit** damage (on hit) or add **+1 Success** (on attack) to the nearest enemy.
*   **Loud (T1)**
    *   *Effect:* Activating this **Quirk** automatically rallies 1 Fleeing **Mob** in your **Zone**, but imposes a **Bane** on all stealth-related **Slink** tests for the rest of the round.
*   **Efficient (T2)**
    *   *Effect:* Reduces the **Grunt** cost of the attached **Quirk** by 1 (minimum 0). Cannot be attached to Passive **Quirks**.
*   **Reflexive (T3)**
    *   *Effect:* If the attached **Quirk** normally costs 1 Action, it now costs a Free Action.
