# Generic Trick Mechanics Framework

This document takes the mechanical concepts of Tricks and distills them into their raw, generic mathematical and rule-bending templates. These can be used as "formulas" to quickly construct specific Tricks by plugging in different Stats, Conditions, or Equipment.

## 1. Boons & Dice Manipulation
Formulas that alter the raw dice probabilities.
*   **Static Bonus:** Gain `+X d6` on `[Specific Action / Stat / Skill]`.
*   **Contextual Bonus:** Gain `+X d6` on `[Action / Stat]` when `[Specific Condition is met]`.
*   **Enemy Penalty:** Enemies suffer `-X d6` when `[Specific Trigger happens]`.
*   **Target Adjustment:** Treat a roll of `[Number/Face]` as `[Better Number/Success]` on `[Specific Action]`.
*   **Exploding Dice:** If you roll `[Specific Number]` on `[Action]`, roll 1 additional die.
*   **Reroll Allocation:** Reroll up to `[X]` failed dice on `[Specific Test / Condition]`.
*   **Die Discard:** Discard the lowest die result from your pool instead of counting it, when `[Condition]`.
*   **Success Multiplier:** On `[Action]`, a roll of `[Specific Number]` counts as `[X]` successes instead of 1.
*   **Critical Shift:** Rolls of `[Number]`, in addition to being a success, also inflict `[Status Effect]`.
*   **Fail Forward:** On a roll with zero successes for `[Action]`, automatically gain `[Resource or Temporary Bonus]`.
*   **Success Share:** If you generate `[X]` more successes than required for `[Test]`, grant `[Bonus]` to `[Ally / Mob]`.

## 2. Economy Bending (Actions & Time)
Formulas that bend the rules of turn phases, action economy, and initiative.
*   **Conditional Extra Action:** Gain 1 additional `[Action Type]` when `[Extremely Specific Condition]`.
*   **Action Chaining:** Perform `[Action A]` as a Free Action immediately after succeeding at `[Action B]`.
*   **Reaction Action:** When `[Enemy Action / Trigger]` occurs, you may immediately perform `[Specific Action]` as a Reaction.
*   **Action Downgrade:** Perform `[Standard Action]` as a `[Free Action / Cheaper Action]` under `[Condition]`.
*   **Initiative Shift:** You may choose to take your turn immediately before `[Enemy Type / Event]` acts.
*   **Action Investment:** If you forgo `[Action Type]` this turn, gain `[Bonus / Action]` on your next turn.
*   **Speed Override:** Performing `[Action]` takes `[Less Time / Fewer Actions]` than the standard rules dictate.

## 3. Rule Breaking & Bypassing
Formulas that let a Boss safely ignore the negative constraints that govern normal characters.
*   **Auto-Pass / Exemption:** You automatically succeed at `[Specific Test / Hazard]` without needing to roll.
*   **Stat Swapping:** You may roll `[Stat A]` instead of `[Stat B]` when performing `[Specific Action]`.
*   **Trait Ignorance:** Ignore the `[Negative Trait]` rule on `[Equipment / Weapon / Armor]`.
*   **Constraint Breaking:** Bypass `[Specific Usage Rule]` for `[Equipment]` (e.g., wielding a 2-handed item in 1 hand).
*   **Environmental Bypass:** Ignore `[Specific Hazard / Terrain Penalty / Cover]` when resolving `[Action / Move]`.
*   **Condition Immunity:** You can never be afflicted by `[Specific Status Effect / Condition]`.
*   **Scale / Size Adjustment:** You count as `[Larger / Smaller]` for the specific purpose of `[Grappling / Carrying / Line of Sight]`.

## 4. Resource Manipulation (Grit, Grunt, Costs)
Formulas that alter the economy of health, command points, or other meta-currencies.
*   **Capacity Increase:** Gain `+X` to Max `[Resource Type]`.
*   **Cost Reduction:** Reduce the activation cost of `[Specific Action / Order]` by `[X] Resource` (minimum 1).
*   **Resource for Bonus:** Spend `[X] Resource` to instantly gain `+Y d6` on `[Specific Action]`.
*   **Resource for Mitigation:** Spend `[X] Resource` to reduce incoming `[Damage / Consequence]` by `[Y]`.
*   **Resource Refund:** Regain `[X] Resource` whenever `[Trigger / Success Condition]` occurs.
*   **Desperation Buff:** While at exactly `[Number] Resource`, gain `[Specific Bonus]`.
*   **Auto-Success via Resource:** Spend `[X] Resource` to automatically pass `[Specific Test / Morale]`.
*   **Resource Conversion:** Take `[X] Damage to Resource A` to instantly gain `[Y] of Resource B`.
*   **Rest Enhancement:** Regain `+[X] additional Resource` whenever you `[Rest / Recover]`.

## 5. Mob & Leadership
Formulas relating exclusively to the interaction with and command of Mobs.
*   **Damage Reassignment:** Redirect `[X]` damage you take to a Grunt in your Mob under `[Condition]`.
*   **Mob Stat Boost:** Mobs you lead gain `+[X]` to their base `[Stat / Speed / Damage]` under `[Condition]`.
*   **Mob Boon:** Mobs you lead gain `+[X] d6` when performing `[Specific Action]`.
*   **Mob Penalty Negation:** Mobs you lead ignore `[Specific Penalty]` (e.g., half-size penalties).
*   **Free Command:** Issue `[Specific Order]` without spending an Action or Grunt under `[Condition]`.
*   **Casualty Mitigation:** Mobs you lead ignore the first casualty they suffer from `[Specific Source]`.
*   **Mob Recovery Shortcut:** `[Action / Resource]` automatically rallies or reforms Mobs in `[Area]`.
*   **Mob Utility Boost:** Mobs you lead gain `[Utility Rule]` (e.g., extra carry slots, providing better cover).
*   **Sacrificial Boost:** Command a Mob to gain `+[X] Bonus`, but they automatically suffer `[Y] Casualty / Penalty` afterwards.

## 6. Survivability & Defense
Formulas that prevent a Boss from dying to stray arrows or unlucky rolls.
*   **Damage Ceiling:** You cannot take more than `[X]` damage from a single `[Source / Attack]`.
*   **Damage Type Mitigation:** Reduce or ignore `[Damage / Effects]` from `[Specific Damage Type]`.
*   **Death Defy:** When reduced to 0 `[Health Resource]`, roll `[X] d6`. On a `[Target Number]+`, stay at 1.
*   **Vampirism:** Regain `[X] Health Resource` whenever you `[Defeat Enemy / Trigger Condition]`.
*   **Last Stand:** When reduced to 0 `[Health Resource]`, you may immediately perform `[Specific Action]` before dying.
*   **Fast Healing:** Automatically regain `[X] Health Resource` when `[Trigger, e.g., combat starts]`.

## 7. Loot & Gear Interaction
Formulas based on manipulating items in the world.
*   **Guaranteed Loot:** When rolling for Loot after `[Condition]`, automatically find at least `[X]` of `[Item Type]`.
*   **Field Repair:** You can repair `[Item Type]` using `[Alternative Resource / Action]`.
*   **Carry Capacity:** You can hold `+[X]` items of `[Bulk / Specific Type]` without suffering encumbrance.
*   **Equipment Juggler:** Swap or equip `[Item Type]` as a `[Free Action / Cheaper Action]`.
*   **Effect Area Increase:** `[Item Type, e.g., grenades]` have their Area of Effect increased by `[X] zones`.
