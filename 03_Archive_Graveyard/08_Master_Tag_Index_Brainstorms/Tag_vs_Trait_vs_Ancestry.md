# Brainstorm: Tags vs. Traits vs. Ancestries

*Goblins don't know the difference between an attribute and an adjective, but they know that putting fire on a sticky thing makes a bigger boom. If we use the same word for a creature's biological nature, a sword's weight, and a magical fire blast, we confuse the players. Let's separate the terms so that the rules write themselves.*

This brainstorm addresses the semantic confusion of the catch-all "Tag" label. To keep the rules clear, intuitive, and simple, we should avoid "tagging tags with tags" and instead align our terminology with the natural language already used in the rulebook.

We can define three distinct categories: **Ancestries**, **Traits**, and **Tags**.

---

## The Simplified Terminology Matrix

| Category | What it applies to | Examples | Can it Synthesize? | Can it float dynamically? |
|---|---|---|:---:|:---:|
| **Ancestry** | Creatures (Bosses, Mobs, NPCs) | `Undead`, `Beast`, `Construct`, `Human` | **No** | **No** (Static classification) |
| **Trait** | Equipment & Structures | `Bashing`, `Cutting`, `Heavy`, `Loud`, `Bonded` | **No** | **No** (Built into the item) |
| **Tag** | Elements, Spells, Hazards, Zones | `[Fire]`, `[Sticky]`, `[Chilled]`, `[Toxic]` | **Yes** | **Yes** (SLAPPED onto anything) |

---

## 1. Ancestry (The Identity)
*   **What it is:** A creature's biological or existential categorization (e.g., `Undead`, `Construct`, `Beast`).
*   **Why it's not a tag:** A skeleton doesn't have the "Undead tag"—it *is* an **Undead** creature. It is an intrinsic part of its nature that dictates core immunities (e.g., not needing to breathe, immune to fear).
*   **Rule:** Rules references filter by Ancestry (e.g., "The spell targets only Beasts" or "Holy weapons deal +Xd against Undead").

## 2. Trait (The Attribute)
*   **What it is:** A structural, physical property built into equipment (e.g., `Bashing`, `Cutting`, `Heavy`, `Loud`, `Fragile`).
*   **Why it's not a tag:** These are static design attributes. You don't dynamically "tag" a sword with `Heavy` in the middle of combat; it is heavy because of how it was forged. They modify core rules math (like Passive Defense penalties or carrying limits).
*   **Rule:** Traits are static. They do not interact with elemental rules or participate in synthesis.

## 3. Tag (The Dynamic Element)
*   **What it is:** A transient physical or magical element (written in brackets like `[Fire]`, `[Sticky]`, `[Chilled]`, `[Toxic]`).
*   **Why it is a tag:** It can be dynamically slapped onto or stripped away from anything:
    *   Slap it on a zone: The zone is now `[Fire]` (a hazard).
    *   Slap it on a sword: The sword now deals `[Fire]` damage.
    *   Shout it as a spell: You cast a `[Fire]` Power Word.
    *   Grow it as a mutation: Your skin secretes `[Toxic]` slime.
*   **Rule:** Only **Tags** participate in **Element Synthesis** (combining `[Fire]` + `[Sticky]`) and map directly to temporary status conditions (like *Restrained* or *Weakened*).

---

## Resolving the Overcomplication: The "Self-Sufficient" Rule

By restricting the word **Tag** strictly to the dynamic Layer 1 (Elements/Substances), we keep the system extremely simple and self-sufficient:

*   **A Tag is a physical substance or state.** It is self-sufficient because it has a singular, clear rule: " স্ল্যাপিং (Slapping) this onto an object/zone gives it this elemental property and its mapped status condition."
*   **We don't need "tags for tags."** You don't tag `[Fire]` with `[Heavy]`. Instead, a sword has the structural **Trait** `Heavy`, and is dynamically **Tagged** with `[Fire]` (by crafting a fire crystal into it). The sword has both a Trait and a Tag, which is logically clear.
*   **We avoid lazy design:** The grammar of the rules remains logical. A player cannot claim they can cast an "Undead" spell to make their sword undead because `Undead` is an **Ancestry** (a classification of life/unlife), not a dynamic **Tag** (elemental substance).

## Summary: A Clear Rulebook Grammar

We can formalize this terminology in the draft index to ensure consistency across the files:
1.  **Ancestries** define what a creature *is*.
2.  **Traits** define how gear is *constructed*.
3.  **Tags** define what elemental forces are *active*.
