# 14. Feats & Twists

> **THIS SECTION IS TO BE CONSIDERED A BIT OUTDATED. ALL THE RULES AROUND STILL CHANGE THAT WILL AFFECT THIS. THIS IS THEREFORE NOT TO SEEN AS A BLOCKER TO OTHER RULE CHANGES, BUT RATHER WE WILL COME BACK AND FINISH THIS ONCE ALL THE OTHER RULES ARE SOLIDIFIED.**

*Goblins don't fight fair. They fight weird. When a tall-man swings a shiny sword, a goblin Boss doesn't block it—they duck, bite their ankle, and shove a friend in the way.*

[[Feat|Feats]] are unique personal abilities that allow a Boss to manipulate dice outcomes, bypass combat restrictions, or alter the action economy. A [[Feat]] is a modular base action. The true chaos happens when you attach a [[Twist]]—a modifier that alters how the [[Feat]] works, creating a customized, volatile combination.

All [[Feat|Feats]] and [[Twist|Twists]] are governed by the modular structure detailed in [16. Unified Modular Powers System](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md).

---

## 1. Acquiring Feats & The Limit

To prevent Bosses from forgetting their own chaotic repertoire mid-raid, a Boss is strictly limited in how many personal [[Feat|Feats]] they can maintain.

*   **The Personal Limit:** A Boss can hold a maximum of 3 [[Personal Feats]].
*   **Twist Limits:** Each [[Feat]] can hold exactly 1 [[Twist]]. 

### Progression
New [[Feat|Feats]] and [[Twist|Twists]] are acquired and upgraded during downtime:
1.  **Character Creation:** A newly rolled Boss starts with 1 **Basic Feat** of their choice, and 0 [[Twist|Twists]].
2.  **Leveling Up:** Every time a Boss permanently upgrades *any* stat by 1 point, they may choose to:
    *   Learn 1 new [[Feat]] (if under the cap of 3).
    *   Learn 1 new [[Twist]] and attach it to an existing [[Feat]].
    *   Upgrade an existing [[Feat]] or [[Twist]] to a higher [[Tier]].

### Stat Gating (Tier Requirements)
[[Feat|Feats]] and [[Twist|Twists]] are rated by **Tier (T1–T5)**. To learn or upgrade to a [[Tier]] X [[Feat]] or [[Twist]], the Boss's underlying relevant Stat ([[Tough]], [[Slink]], [[Mouth]], or [[Brains]]) must be equal to or greater than X.
> **Example:** To learn the **T3** [[Tough]] [[Feat]] **Head Chopper**, you must have [[Tough]] 3 or higher.

---

## 2. Gang Feats & Infamy

[[Gang Feats]] are powerful, legendary abilities that belong to the [[Gang]] as a whole. They are acquired when a Boss reaches Level 6 in any stat and retires as an [[Elder]], or dies gloriously and joins the [[Pile of Bones]] (see [12. Gangs](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/12_Gang.md)).

*   **The [[Infamy]] Limit:** [[Gang Feats]] **do not** count toward a Boss's personal limit of 3. Instead, the maximum number of [[Gang Feats]] a starting Boss can bring on a raid is determined by the [[Gang]]'s [[Infamy]] score. 

---

## 3. Activation Costs

To use a [[Feat]], the Boss must pay its associated cost (detailed in [16. Unified Modular Powers System](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md)):
*   **[Cost: Passive]** - The [[Feat]] is always active or triggers automatically based on a stated condition. It costs zero actions or [[Grunt]].
*   **[Cost: Grunt]** - The Boss must spend the stated number of [[Grunt]] points to activate the [[Feat]].
*   **[Cost: 1 Action]** - The Boss must spend one of their Standard Actions (Move, Attack, Order) to activate the [[Feat]]. 

---

## 4. Example Feats (Base Atoms)

The following [[Feat|Feats]] are assembled using the successes and condition standards of the modular powers toolkit.

### Tough Feats
*   **[Cost: 1 Grunt**]
    *   *Trigger:* When you take a [[Wound]] from an incoming attack.
    *   *Effect:* Instantly shove an allied [[Mob]] in your [[Zone]] into the way. The [[Mob]] takes the hit instead (losing **1d3** [[Mob]] [[Size]]), and you take 0 [[Wound|Wounds]].
*   **[Cost: Passive**]
    *   *Effect:* Gain **+1 Boon Die** when making an Attack test against an enemy whose Size is strictly smaller than yours.

### Slink Feats
*   **[Cost: Passive**]
    *   *Trigger:* Whenever you successfully Dodge an incoming attack.
    *   *Effect:* You may immediately make a free [[melee attack]] against the attacker's legs (if they are in your [[Zone]]) adding **+1 Success** to the attack roll.
*   **[Cost: Passive**]
    *   *Effect:* Enemies do not get free reactionary Opportunity Attacks against you when you leave their [[Zone]].

### General Feats
*   **[Cost: 1 Grunt**]
    *   *Trigger:* After you roll the [[dice pool]] for any test.
    *   *Effect:* Spend 1 [[Grunt]] to completely reroll all dice that did not land on a 1 (You cannot reroll [[Fumbles]]).
*   **[Cost: Passive**]
    *   *Effect:* You can carry up to 2 [[Bulk]] worth of items by swallowing them. Swallowed items do not count toward your [[Carry Capacity]]. *It requires 1 Action to regurgitate them.*

---

## 5. Example Twists (Modifiers)

[[Twist|Twists]] modify the behaviors of [[Feat|Feats]] to add utility, change delivery, or adjust action costs.

*   **Spiteful (T1)**
    *   *Effect:* Whenever the attached [[Feat]] is activated, deal **1** [[Grit]] damage (on hit) or add **+1 Success** (on attack) to the nearest enemy.
*   **Loud (T1)**
    *   *Effect:* Activating this [[Feat]] automatically rallies 1 Fleeing [[Mob]] in your [[Zone]], but imposes a [[Bane]] on all stealth-related [[Slink]] tests for the rest of the round.
*   **Efficient (T2)**
    *   *Effect:* Reduces the [[Grunt]] cost of the attached [[Feat]] by 1 (minimum 0). Cannot be attached to Passive [[Feat|Feats]].
*   **Reflexive (T3)**
    *   *Effect:* If the attached [[Feat]] normally costs 1 Action, it now costs a [[Free Action]].
