# Game Mechanics Audit: The Gobbo Pool Lair System

**Role:** Game Mechanics Engineer  
**Objective:** Analyze the mechanical coherence, probability models, and gameplay loops of the proposed d6 "Gobbo Pool" Lair system, identifying tuning points and edge cases.

---

## 1. Overall System Architecture

The proposal to treat the Lair's population as a communal pool of physical **d6 dice** is a major design success. It achieves three core goals:
1.  **Mechanical Coherence:** It integrates base management with the core resolution mechanic of *Gobbos* (rolling d6 pools, looking for successes, and exploding 6s).
2.  **No Bookkeeping:** Players do not track individual names, rations, or population counts. They literally slide physical dice across a table to allocate their labor force.
3.  **High-Stakes Tension:** By linking the Lair's labor force directly to the players' combat Mobs, casualties suffered on a raid have immediate, painful strategic consequences.

---

## 2. Probability & Economy Analysis

Let's analyze the mathematical engine behind the Labor Phase. A standard test in this system succeeds on a **4, 5, or 6** (50% base success rate per die), with 6s exploding.

### 2.1 — Clearing Caverns (Construction)
Assume a locked slot requires a target number of successes to clear:
*   **Low Threat Slot:** 5 successes.
*   **Medium Threat Slot:** 10 successes.
*   **High Threat Slot:** 15 successes.

An exploding d6 has an expected value (EV) of successes calculated as:
$$\text{EV} = 0.5 \text{ (base success chance)} \times \frac{6}{5} \text{ (exploding multiplier)} = 0.6 \text{ successes per die}$$

```
Labor Dice Assigned  | Expected Successes | Est. Turns to Clear Low (5) | Est. Turns to Clear High (15)
--------------------|--------------------|----------------------------|------------------------------
2d6                 | 1.2                | 4.2 Turns                  | 12.5 Turns
4d6                 | 2.4                | 2.1 Turns                  | 6.3 Turns
6d6                 | 3.6                | 1.4 Turns                  | 4.2 Turns
8d6                 | 4.8                | 1.0 Turns                  | 3.1 Turns
```

*   **Verdict:** This pacing is excellent. A small Lair with only a few spare dice will take several turns to clear a room, creating a tight bottleneck. A prosperous Lair with a large workforce can clear a basic cavern in a single week.
*   **Risk Profile:** The complication rate is $\frac{1}{6} \approx 16.7\%$ per die rolled. 
    *   If you assign 6d6 to clear a room, you expect **1 complication** on average per turn. This guarantees that larger, faster projects generate more noise, chaos, and minor setbacks, which fits the goblin theme perfectly.

### 2.2 — Recruitment Math (Tuning Required)
The current proposal states: *"Every 6 rolled (exploding!) recruits 1 new d6 to the Gobbo Pool."*
Let's analyze the expected growth rate:
*   A 6 has a $1/6$ chance of rolling. Due to explosions, the expected value of new dice recruited per die assigned is:
$$\text{EV}_{\text{recruit}} = \frac{1}{6} \times \frac{6}{5} = 0.2 \text{ new dice per Laborer die}$$

If the players assign **5d6** to recruitment:
*   Expected yield is **1.0 new die** per turn.
*   However, the probability of rolling **zero 6s** on 5d6 is:
$$P(\text{zero } 6\text{s}) = \left(\frac{5}{6}\right)^5 \approx 40.2\%$$

*   **The Issue:** A 40% chance of gaining absolutely nothing after dedicating 5 Gobbos to recruitment for a whole turn is too volatile. It will feel frustratingly slow and grindy.
*   **Engineers Recommendation:** We should increase the success chance or use a "Runt" currency to smooth out the curve.

#### Option A: Recruitment on a 5 or 6 (Exploding)
*   Expected yield per die: $2/6 \times 6/5 = 0.4$ new dice.
*   If you assign 3d6, you expect **1.2 new dice** per turn.
*   Chance of recruiting 0 dice on 3d6 drops to $\left(\frac{4}{6}\right)^3 \approx 29.6\%$. This is much more rewarding and less swingy.

#### Option B: The "Runt Token" Sub-Pool (Recommended)
*   Instead of recruiting full d6s directly, recruitment rolls generate **Runts** (successes on a 4+).
*   **3 Runts = 1 permanent d6** added to the Gobbo Pool.
*   This removes the volatility completely. Every Laborer die rolled has a 50% chance of generating a Runt, ensuring slow but guaranteed progress even with small pools.

---

## 3. Auto-Healing & The Casualty Threshold

The decision to **auto-heal returning Mobs for free** (provided they have at least 1 HP remaining) is brilliant because it sets up a high-stakes, binary gamble during raids.

### The Combat Incentive:
*   If a player has a Size 3 Mob and it takes heavy damage, bringing it down to Size 1 with only 1 HP left, they face a choice:
    *   *Option A: Push on.* If the Mob takes one more point of damage and dies, those 3d6 are lost forever from the Lair's pool.
    *   *Option B: Retreat/Cover.* Shield the Mob, or order them to flee. If they survive the fight, they will return to the Lair and heal back to Size 3 completely for free.
*   **Design Verdict:** This creates an incredibly tense push-your-luck dynamic. Players will protect their near-death Mobs with their lives, leading to heroic (and hilarious) goblin shielding maneuvers.

---

## 4. Growth and Scaling Caps

To prevent the Gobbo Pool from growing infinitely and turning the game into a massive bookkeeping chore, we must enforce a strict scaling limit.

### Recommended Capacity Math:
Let $N$ be the number of players, and $I$ be the Lair's **Infamy** level.

$$\text{Maximum Gobbo Pool} = (5 \times N) + I$$

*   **Example (3 Players, Infamy 1):** Max capacity is 16d6.
*   **Example (3 Players, Infamy 5):** Max capacity is 20d6.
*   **Upgrades:** Specific Lair upgrades (e.g., *Sewer Warrens*, *Hut Expansions*) can add a flat $+2\text{d6}$ or $+4\text{d6}$ to this capacity.

This ensures that at campaign start, players must manage a very tight pool (e.g., 9d6 to 12d6), forcing them to make hard choices between sending larger Mobs on raids or building up their Lair.

---

## 5. Summary of Recommended Adjustments

Before drafting these rules into `STAGE_Drafts/05_Base/`, I recommend implementing the following tweaks to polish the system:

1.  **Refine Recruitment:** Switch to the **Runt Token** system (successes on 4+ generate Runts; 3 Runts = 1d6 pool growth) or make recruitment succeed on a 5–6 (exploding) to reduce frustration.
2.  **Explicit Dig Progress:** Set clear Target Successes for room expansion based on Lair Site Type.
3.  **Raid vs. Labor Allocation Phase:** Make the division of the Gobbo Pool an official, phase-based decision that players must lock in at the beginning of the Lair Turn.
