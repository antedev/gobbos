# Rules Lawyer Audit: Equipment Framework Brainstorm

**Subject:** `00_DEV_Brainstorms/Equipment_Framework_Brainstorm.md`
**Auditor:** The Rules Lawyer ([@/rules_lawyer](file:///c:/Users/ante/Documents/github/gobbos/.agent/workflows/rules_lawyer.md))

## 1. Terminology & Keywords Check

*   **"Reaction / Free" vs Action Economy:** The draft uses "Reaction / Free" for items usable instantly. 
    *   *Conflict:* "Free" is used in `10_Stats.md` specifically for "Free Orders" (granted by Mouth), which are still your turn actions, just not costing standard actions. "Reaction" implies an out-of-turn trigger (like being attacked). If an item can be used out of turn, "Reaction" is the correct term. If it doesn't cost an action but must be done on your turn (like drinking a potion), it needs a distinct keyword to prevent confusing it with Free Orders. 
    *   *Recommendation:* Standardize the wording. Use **Reaction** for out-of-turn triggered effects. Use **Incidental** or **Minor Action** for things on your turn that don't cost a full action.
*   **"Passive Defence":** 
    *   *Status:* Corrected. `10_Stats.md` explicitly calls it "Passive Dodge Dice". However, the brainstorm document now says "Passive Defence". 
    *   *Conflict:* `10_Stats.md` explicitly uses "Passive Dodge Dice". Changing it to "Passive Defence" in the Equipment document creates a terminology mismatch. If the rule is renaming it to "Passive Defence", then `10_Stats.md` MUST be updated from "Passive Dodge Dice" to "Passive Defence".
*   **"Value":** 
    *   *Status:* Clarified. It functions as currency. No direct conflicts with existing rules, though "Loot" in `12_Gang.md` is tied to Renown. The framework aligns well by linking Value to Lair Upgrades and Renown.

## 2. Rules Consistency & Conflicts

*   **Carry Capacity (Bulk constraint):**
    *   *Consistency:* Matches `10_Stats.md` perfectly. Carry Capacity is derived from Tough. No conflicts.
*   **Weapons modifying Dice Pools:**
    *   *Consistency:* Matches the core mechanic in `01_Dice.md` where equipment adds dice to the pool. Standardizing weapons as +1d or +2d respects the "no math interpretation" tenet.
*   **Ablative Armor:**
    *   *Complexity Check:* The user's comment notes *(Comment: this might be a bit complex for Mobs, but perhaps a good thing for PC)*. The Rules Lawyer agrees. Mobs should not have ablative armor tracking; it bogs down Mob combat. It should strictly apply to the PC Boss.
*   **Named Items & Death (`15_Death.md`):**
    *   *Integration Check:* `15_Death.md` introduces "Named Items" with minor magical traits when a Boss dies. The Equipment framework's section on "Mechanical Traits" neatly creates space for this. Named Items simply gain a Trait. No conflicts.

## 3. Structural & Fast Play Assessment

*   **Generic Structure:** By avoiding specific weapon rules and keeping "Traits" rare, the framework succeeds in the "Slim Rules" goal. 
*   **Action Usage:** Explicitly stating if an item takes an Action or is Passive/Reaction is excellent for fast play at the table. It prevents GM/Player arguments over action economy.

## 4. Verdict & Next Steps

The framework is **Solid**, but requires a few specific keyword cleanups before moving to `STAGE_Drafts` or statting items.

**Required Action Items for the User/Dev:**
1.  **Resolve "Passive Dodge" vs "Passive Defence":** Decide on ONE term. If it's Passive Defence, we must update `10_Stats.md` (lines 17-23).
2.  **Clarify "Free" Item Usage:** Decide if a zero-action item used on your turn is called an "Incidental," a "Minor Action," or if "Free" is acceptable despite "Free Orders" existing. 
3.  **Lock in Ablative Armor:** Add a rule specifically stating "Ablative Armor applies only to PCs, not Mobs" to avoid tracking headaches.
