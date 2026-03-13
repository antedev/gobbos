# Markdown Formatting Guide

This document defines the strict formatting rules for all text written for the Gobbos TTRPG. It ensures that output can easily be converted into printed PDFs and website pages, maintaining visual hierarchy, scanning ease, and logical flow.

If you are an AI Agent or a Human contributor, **you must read and follow these formatting principles.**

## 1. Hierarchy and Headers (Semantic Structure)
Strict semantic hierarchy is required for automatic Table of Contents (ToC) generation.
*   `#` **H1:** Reserved strictly for Chapters (e.g., `# Combat`, `# Character Creation`).
*   `##` **H2:** Used for Sections within a Chapter (e.g., `## Melee`, `## Turn Order`).
*   `###` **H3:** Used for specific Sub-rules (e.g., `### Hitting a Gobbo`, `### Fumbles`).
*   **Rule:** Never skip a heading level. Do not jump from H1 directly to H3. You must use H2 between them.

## 2. Highlighting Mechanics and Dice
To make the text instantly scannable for the reader at the table:
*   **Core Stats & Mechanics:** Must be **Bold**. (e.g., **Grit**, **Boon**, **Bane**, **Vigor**, **Slink**, **Brain**, **Renown**).
*   **Dice Expressions:** Must be **Bold**. (e.g., **1d6**, **3 successes**, **2d6**).

## 3. Flavor Text vs. Rules
Gobbos relies on clear, punchy rules mixed with chaotic, funny lore. These must be kept visually distinct.
*   **Evocative Flavor:** Write flavor text, lore, or in-world quotes in *Italics*. Usually placed at the beginning of a Chapter or Section.
*   **Rules Language:** Must be clear, precise, and literal. Do not mix flavor adjectives into the actual mechanical instructions.

## 4. Examples of Play
Examples clarify the rules but must not be confused for the rules themselves.
*   **Format:** Always use the standard markdown blockquote tag (`>`) and begin with **Example:**.
> **Example:** Grub tries to stab the tall-man. Because the tall-man has a shield, Grub suffers a **Bane**. He rolls **3d6** and needs **2 successes**...

## 5. Break-out Boxes / Golden Rules
For critical rules, important warnings, overarching principles, or sidebars that must stand out from the rest of the text.
*   **Format:** Use a special blockquote with a bolded header. To ensure layout programs and CSS can identify these differently than standard examples, we will use a double blockquote `>>`.
>> **IMPORTANT:** Goblins never leave a shiny object behind...

## 6. Lists and Procedures
*   **Numbered Lists (1., 2., 3.):** Use ONLY for strict procedures where the sequence of operations matters (e.g., The Sequence of Combat, Steps for Character Creation).
*   **Bullet Points (- or *):** Use for non-sequential options, lists of gear, or traits.

## 7. Internal Linking
Because the rulebook will become a website/digital PDF, cross-referencing is essential.
*   **Format:** Use standard markdown internal linking syntax when referencing a rule defined in a different file.
*   **Example:** `For details on mob attacks, see [Mob Combat](06_Mob_Combat.md).`

## 8. Tables
Use standard Markdown tables for content like Loot, Weapons, Fumble results, or quick-reference stats. Ensure the columns align logically.

## 9. Statblocks
All NPCs and Mobs must be formatted identically to allow for easy reading and predictable layout transition. *(Note: The precise template for Statblocks is to be established)*.
