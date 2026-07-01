# Game Mechanics Report: Tag Index & Modular Powers Integration

**Prepared by:** Game Mechanics Engineer  
**Audit Target:** Integration between [08_Master_Tag_Index.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/08_Master_Tag_Index.md) and [16_Unified_Modular_Powers_System.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md).  
**Status:** SUCCESSFUL COHESION (Requires minor Stage updates to align rules text).

---

## 1. Do They Work Together? (The Verdict)

**Yes. The two documents are highly cohesive, but they require a clear "handshake" rule to define how tag baselines scale with modular Tiers (T1–T5).**

When a player builds a power using the **Unified Modular Powers System**, they combine a **Tag** (Narrative Descriptor) with a **Tier (T1–T5)**. 
*   **The Tag** provides the *flavor, delivery type, environmental interaction, and condition mapping* (defined in the Tag Index).
*   **The Tier** provides the *mathematical scale* (successes, Wounds, range, area, and activation costs).

---

## 2. Resolving the Integration Gaps

### Gap A: The Scaling Rules (Tag Baseline vs. Power Tier)
*   *The Issue:* In `08_Master_Tag_Index.md`, many tags have math attached to their baseline (e.g. `[Fire]` deals +1 success, `[Shock]` deals 1 damage to an adjacent target). How does this scale if a player builds a **T3** Fire Sword or a **T4** Shock Blast?
*   *The Handshake Rule:* A custom power uses the **Tier's successes/damage value** instead of the tag's baseline success/damage. The tag's baseline condition and area/delivery rules still apply.
    *   *Example (T1 Fire Dagger):* A T1 power deals +1 success/damage. `[Fire]` baseline deals +1 success. They match.
    *   *Example (T3 Fire Sword):* A T3 power deals +3 successes/damage. This overrides `[Fire]`'s +1 success baseline. The sword now deals +3 successes and ignites the zone (the tag's environmental effect).
    *   *Example (T4 Shock Blast):* A T4 power deals 4 damage across a Blast area. The weapon deals 4 damage to all targets in the main and adjacent zones, and triggers the `[Shock]` tag's conduction effect (+1 Boon/Easy difficulty) on wet targets.

### Gap B: Outdated Condition Mapping in Modular Powers
*   *The Issue:* Section 6 of `16_Unified_Modular_Powers_System.md` contains an outdated, flat condition mapping list (e.g. `[Chilled]` imposing full Restrained). This conflicts with the richer, more specific conditions defined in our new `08_Master_Tag_Index.md` (e.g. `[Chilled]` only saps movement speed, while `[Sticky]` restrains).
*   *The Handshake Rule:* We must update `16_Unified_Modular_Powers_System.md` to point directly to `08_Master_Tag_Index.md` as the single source of truth for tag baselines and condition mappings.

---

## 3. Required Modifications to Stage Drafts

To finalize the integration, the following updates must be made to [16_Unified_Modular_Powers_System.md](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/01_Characters & Mobs/16_Unified_Modular_Powers_System.md):
1.  Update **Section 5 (Narrative Descriptors)** to clarify how baseline tag rules scale with T1–T5 power tiers.
2.  Replace the outdated condition mapping in **Section 6 (Element Synthesis)** with a direct reference to the [Master Tag Index](file:///c:/Users/ante/Documents/github/gobbos/01_STAGE_Drafts/00_Rules/08_Master_Tag_Index.md).
