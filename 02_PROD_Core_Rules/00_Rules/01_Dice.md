# Dice

Rolling **dice** is fun, and in Gobbos you roll a lot of **dice** if you are a player. The GM, on the other hand, never rolls **dice**—unless to possibly determine the outcome of a random event.

## Tests

A **Test** in Gobbos is carried out by the player rolling a number of **d6s** (their **Dice Pool**). They then try to score as many **Successes** as the GM has decided is the target for the **Test**.

### Difficulty and Target Number

For any **Test**, the GM sets a **Difficulty** and a **Target Number (TN)**. **Difficulty** depends on the circumstances, such as having the high ground when attacking or using quality lockpicks to pick a lock. **Difficulty** determines what counts as a **Success**. For an **Easy** roll, a **4, 5, or 6** is a **Success**. For a **Normal** roll, a **5 or 6** is a **Success**. For a **Hard** roll, only **6s** are a **Success**.

**Target Number (TN)** is typically fixed, such as how good armor an enemy has or the quality of the lock that is about to be picked. **TN** then denotes how many **Successes** you need to make whatever you are trying to do.

Most of the time, you will roll a **Normal** test with a **TN** of 1, denoted as **Normal:1**. Which means that whatever number of dice you have in your **Dice Pool**, you succeed if there is at least one **5** or **6**.

| Difficulty | Success on |
| :--- | :--- |
| **Easy** | 4, 5, 6 |
| **Normal** | 5, 6 |
| **Hard** | 6 |

> **Example:** Picking a lock is typically a [Slink](../01_Characters & Mobs/10_Stats.md#slink) **Normal:1** test. But if the lock is of extra good quality, it could be a **Normal:2**. And if the lockpicker has brought quality lockpicks, it could turn into an **Easy:2** test.

### Dice Pool

The player is responsible for assembling their **Dice Pool**. If they carry out the task with their **Boss**, it is almost always equal to their main stat, modified by equipment, **Quirks**, or other circumstances. So, if you have a **Tough** stat of 2, you roll 2 dice, or **2d6**.

If rolling for a **Mob** instead, the base number of dice in your **Dice Pool** is equal to the **Size** of the **Mob**. A **Size** 2 **Mob** rolls **2d6**, a **Size** 5 **Mob** rolls **5d6**, etc.

### Exploding Dice

Every time you roll a **6**, it is not only a **Success** but it allows you to roll an additional die. If that roll is a **6** again, you keep rolling until you no longer roll **6s**. This makes it possible, but still perhaps unlikely, to get a lot of **Successes** on a single roll.

### Criticals

Whenever you roll a **6** that explodes, and the new die you roll also turns into a **6**, you have achieved a **Critical Success**! This impressive feat allows you to regain **1 Grunt** (up to your maximum) and also grants you a surge of adrenaline, allowing you to immediately perform an additional non-offensive action (a **Move**, **Plunder**, or **Manipulate** action).

*(Note: Grunt is fully explained in the [Character Stats rules](../01_Characters & Mobs/10_Stats.md#grunt)).*

### 1s and Fumbles

If your final result has zero **Successes** and at least two dice show **1s**, you have **Fumbled**! You have embarrassed yourself and lost **1 Grunt**.

## The Bangaranga Pool

Goblins are easily carried away by their own rowdy excitement. When the crowd gets hyped by awesome stunts, hilarious disasters, or massive payouts, their collective noise and rowdiness builds up. This is represented by a shared pool of dice called the **Bangaranga Pool**. These should be of a distinct color from the other dice, e.g. bright red.

### Seeding the Pool (Start of Raid)

At the start of a **Raid**, the **Bangaranga Pool** is seeded with a baseline level of chaotic energy based on the size and composition of the raiding party:

| Number of Gobbos | Dice to Add |
| :--- | :--- |
| Number of **Bosses** | **1d6** / **Boss** |
| Number of **Mobs** (**Size** 3 or 4) | **1d6** / **Mob** |
| Number of **Mobs** (**Size** 5) | **2d6** / **Mob** |

> **Example:** A 3-player raid party has one **Size** 3 **Mob**, one **Size** 4 **Mob**, and one **Size** 2 **Mob**. The starting **Bangaranga Pool** is **5 dice** (3 baseline + 1 + 1 + 0).

### Loading the Pool (Hype Triggers)

Dice are added to the physical **Bangaranga Pool** during a **Raid** when notable events hype up the horde:

| Event | Description | Dice to Add |
| :--- | :--- | :--- |
| **Critical Successes** | Any player rolls a **Critical Success** | **+1d6** |
| **Fumbles** | Any player **Fumbles** a test | **+1d6** |
| Defeating a Notable Enemy | Defeating an enemy with the `[Notable]` or `[Big Threat]` tag | **+1d6** |
| Claiming a Big Loot Cache | Looting a chest, room, or zone with the `[Big Loot]` or `[Hoard]` tag | **+1d6** |

### Tapping the Pool & The Bangaranga Tax

Before rolling any test, a player can choose to take a number of dice from the **Bangaranga Pool** (up to a maximum equal to their Boss's **Grunt** stat) and add them to their current test's **Dice Pool**.

However, using the crowd's energy for mundane tasks is considered "cheating" and costs a premium:

| Condition | Consequence |
| :--- | :--- |
| If the number of Bangaranga dice taken is **less than or equal to the Target Number (TN)** of the test | It costs nothing extra. |
| If the number of Bangaranga dice taken is **greater than the test's TN** | It costs **1 extra die** from the pool as a tax. This tax die is simply removed from the pool and discarded back to the box (not rolled). |
| If the pool does not contain enough dice to cover both the dice rolled and the tax die | The player cannot take that many dice. |

> **Example (Normal:2 Test):**
> *   If you take **1 or 2 Bangaranga dice**, it costs no tax. You simply take them from the pool and roll them.
> *   If you want to take **3 Bangaranga dice**, 3 is greater than the TN of 2. You must pay a **1 die tax**. This requires a total of **4 dice** to be present in the pool. 3 dice are rolled, 1 die is discarded.

### Rolling Bangaranga Dice - Double Explosion!

Every **6** rolled on a Bangaranga Die counts as **1 Success**, but it **explodes twice**, meaning you immediately roll *two* additional regular dice instead of one, which can themselves succeed or explode normally!

### Overreaching

If the test **fails** when you use Bangaranga dice, you lose **1 Grunt**, as with a **Fumble**. If the test **fails** and you have any **1s** on the dice that you rolled, you also drain the **Bangaranga Pool** with the same amount of Bangaranga Dice you used for the test.
