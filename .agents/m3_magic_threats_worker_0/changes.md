# Changes Summary: Milestone 3 (Health, Magic & Threats)

**Worker:** Worker 3 (`m3_magic_threats_worker_0`)  
**Scope:** Core Rules Synthesis for Chapters 07, 08, and 12 in `02_PROD_Core_Rules/`.

---

## 1. Files Created and Synthesized

### 1. `02_PROD_Core_Rules/07_Damage_Grit_and_Wounds.md`
*   **Systemic Purpose:** Establishes the core rules for damage decrement, player survival, dying states, multi-wound adversary tracking, and status conditions.
*   **Key Mechanics Implemented:**
    *   **Boss Grit Pool:** Maximum Grit derived from Tough (3 to 5); strict unmitigated damage decrement via Clatter Rolls (active Dodge/Parry + passive Armor Dice).
    *   **The Final Act & Death:** 0 Grit immediately triggers 1 Standard Action (Easy 4+) + 1 Free Order Action (guaranteed hit in LOS) under Rule of Cool before permanent death.
    *   **Temporary Boss & Successors:** Runt steps up during raid (stats -1, min 1, no quirks); true successor created in Lair with $\text{Gang Infamy} \times 4$ XP.
    *   **Adversary Scales:** Standard enemies are One-Hit Kill (`Successes >= Defence TN`); Elites/Bosses track Wounds (2 to 8) via the Overkill Rule ($\lfloor \text{Successes} / \text{Defence TN} \rfloor$).
    *   **Impact Size & Stagger:** Partial hits inflict Staggered only if $\text{Impact Size} \ge \text{Target Physical Size}$; natural mass resistance ignores Stagger.
    *   **9 In-Game Status Conditions Matrix:** Standardized effects across Goblin Bosses (PCs), Goblin Mobs, and Enemies/NPCs for Weakened, Restrained, Dumb, Silenced, Blinded, Terrified, Stunned, Prone, and Staggered.
    *   **Durations & Recovery:** Staggered auto-clears at Round Closure; hazard conditions clear with 1 Standard Action in clean zone or combat end; resting restores 1 Grit/hour.
    *   **Content Extension Hook & Schema:** Formal template with `[CONTENT EXTENSION POINT: Environmental Hazards & Conditions]`.
    *   **Gap Flags:** `[MISSING RULE / GAP]` markers for forbidden mid-combat Mob health dice redistribution and PC Wounds vs Grit keyword constancy.

### 2. `02_PROD_Core_Rules/08_Magic_and_Bangaranga.md`
*   **Systemic Purpose:** Establishes the pure Farkle-style push-your-luck spellcasting engine without living spell catalogs.
*   **Key Mechanics Implemented:**
    *   **Casting Engine:** 1 Standard Action; Brains dice pool rolled vs GM Difficulty (Easy 4+, Normal 5+, Hard 6); lock successes and push remaining non-success dice; Farkle Mishap on 0 new successes.
    *   **Power Word Slots:** Brains 1–2 = 0 slots (cannot cast); Level 3 = 2 slots; Level 4 = 4 slots; Level 5 = 6 slots; conduit required.
    *   **Spell Tiers:** Largest matching set of successes determines Tier (T1 Single, T2 Pair, T3 Triple, T4 Quadruple, T5 Quintuple); Singleton successes provide Potency (+1 target or +1 damage).
    *   **Chaotic Leakage:** Non-success matching sets trigger elemental/physical, mental/social, or movement/spatial side effects; Hard casts feature natural volatility.
    *   **Bangaranga Integration:** Drawing dice up to Grunt; 1-die tax if draw > TN; double explosions on 6s; overreaching penalties and pool drain.
    *   **Extended Rituals:** Cooperative casting (Lead Caster + Assistants + Bangaranga) accumulating successes toward Ritual TN (TN 5 for T3, TN 8 for T4, TN 12 for T5); resource loss on 1s rather than instant Farkle.
    *   **Content Extension Hook & Schema:** Formal template with `[CONTENT EXTENSION POINT: Magic Spells & Tag Effects]`.
    *   **Gap Flags:** `[MISSING RULE / GAP]` markers for Power Word slot progression and Ritual casting mechanics specification.

### 3. `02_PROD_Core_Rules/12_Adversaries_and_Threats.md`
*   **Systemic Purpose:** Establishes the deterministic threat engine, adversary classifications, trait hierarchy, and morale rules without living monster bestiaries.
*   **Key Mechanics Implemented:**
    *   **Deterministic Threats:** GM never rolls dice; all enemy attacks are static Threat Profiles (`Difficulty+/TN`) + flat Damage defended by player Clatter Rolls.
    *   **Three Enemy Scales:** Standard (One-Hit Kill), Elites/Bosses (Wounds track + Overkill rule), Enemy Mobs (shared d6 dice-HP pool).
    *   **Enemy Mob Damage Scaling:** $\text{Damage} = \text{Base Damage} + (\text{Size} - 1)$ delivered via Frontline Rule or single combined strike.
    *   **No Elite Mobs Rule:** Mobs are strictly composed of standard units.
    *   **3-Layer Trait Hierarchy:**
        *   Layer 1: Universal Ancestries (Beast, Humanoid, Undead, Monstrosity, Fiend) with global psychological and biological rules.
        *   Layer 2: Standardized Tags (`[Hardened]`, `[Heavy]`, `[Fast]`, `[Regenerating]`, etc.).
        *   Layer 3: Unique Statblock Traits (Max 1 for Standard, Max 2 for Elites/Bosses).
    *   **Enemy Reactions & Group Attacks:** 2 actions per round default; reactions deduct 1 action (max 1 reaction per round); group attacks combine up to 3 enemies (+1 damage per extra enemy).
    *   **Morale & Swarm Terror:** 50% casualties / leader death triggers Swarm Terror check at Round Closure ($\sum \text{Mob Sizes} + \sum \text{Bosses}$ vs Morale TN); breaking forces 2 Move actions fleeing; Commander Rally opposed check.
    *   **Content Extension Hook & Schema:** Formal statblock template with `[CONTENT EXTENSION POINT: Bestiary & Adversary Statblocks]`.
    *   **Gap Flags:** `[MISSING RULE / GAP]` markers for Enemy reaction economy cap and Swarm Terror pool formula.

---

## 2. Style Guide & GEMINI.md Compliance Verification
*   **Language Tiers:** Tier A mechanical rules in active present-tense; Tier B flavor separated at section starts in *Italics*; Tier C examples formatted using `> **Example:**`.
*   **De-Gendering:** Exclusively second-person ("You/Your") or explicit role nouns ("Goblin Boss", "The Mob", "The GM", "The Player").
*   **Slash Notation:** Strict `[Stat] [Target Face]+/[Successes]` for 4+ and 5+; `[Stat] 6/[Successes]` for 6 (no `+` on 6).
*   **Hierarchy:** Strict `# H1` -> `## H2` -> `### H3` -> `#### H4` without skipping levels.
*   **Keyword Constancy:** Perfect adherence to Grit (Bosses), Wounds (Elites/Bosses), Health Dice (Mobs), Loot (treasure), Mob (player units).
