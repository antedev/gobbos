# Gobbos GitHub Issue Creator
# Run this script to create all backlog issues in GitHub for antedev/gobbos
# Usage: .\scripts\create_github_issues.ps1 -Token "ghp_your_github_token"

param(
    [string]$Token = $env:GITHUB_TOKEN,
    [string]$Repo = "antedev/gobbos"
)

if (-not $Token) {
    Write-Host "Please provide a GitHub Personal Access Token via -Token or `$env:GITHUB_TOKEN" -ForegroundColor Yellow
    Write-Host "Example: .\scripts\create_github_issues.ps1 -Token 'ghp_xxx'"
    Write-Host "You can generate a token at https://github.com/settings/tokens (needs 'repo' scope)"
    exit 1
}

$headers = @{
    "Authorization" = "Bearer $Token"
    "Accept"        = "application/vnd.github+json"
    "User-Agent"    = "Gobbos-Project-Tool"
}

$issues = @(
    @{
        title = "[Combat/Environment] Zone Profiles & Modular Battlefield Traits"
        labels = @("rules", "combat", "loop-1")
        body = @"
## Summary
Standardize ICRPG-style Zone Profiles (Difficulty + Target Number, e.g. Normal:1, Hard:1) for room traversal, search, and environmental interactions.
Add standardized modular Zone Traits:
- **Problems (Hazards/Obstacles):** Burning, Narrow (Mob Size 2 cap), Slippery (causes Prone), Smoky (Cover), Toxic, Deep Water.
- **Opportunities (Tactical Features):** High Ground (+1d Ranged), Junk Pile (throwable scrap), Shadowy (+1d Stealth), Shoring (trigger cave-in to block exits).

### Source Documents
- `00_DEV_Brainstorms/GDRs/GDR-006_Environmental_Hazards_and_Zone_Statblocks.md`
- `00_DEV_Brainstorms/Researcher_Findings_Environmental_Hazards.md`
"@
    },
    @{
        title = "[Combat/System] Static Resistances & Opposed Tests Framework"
        labels = @("rules", "combat", "loop-1")
        body = @"
## Summary
Standardize player-facing opposed rolls against static enemy stats (e.g., wrestling vs Toughness, sneaking past sentries vs Notice) without requiring the GM to roll dice.

### Source Documents
- `00_DEV_Brainstorms/Static_Resistances_Opposed_Tests.md`
"@
    },
    @{
        title = "[Lair/Economy] Mob Raid Pitch Mechanic (Mouth vs. Wallet)"
        labels = @("rules", "lair", "loop-2")
        body = @"
## Summary
Before a raid, the Boss pitches the mission to Grunts:
- **Pay Upfront:** Spend Loot/Scrap from the Hoard to hire calm, equipped Grunts.
- **The Mouth Pitch:** Make a Mouth test promising absurd riches for free. If the raid fails, immediate Mob Mutiny triggers or Grunts steal from the Gang stash.

### Source Documents
- `00_DEV_Brainstorms/Lair_Brainstorm.md`
"@
    },
    @{
        title = "[Lair/Economy] The Loot 'Skim' (Lair Tax Evasion)"
        labels = @("rules", "lair", "loop-2")
        body = @"
## Summary
When returning from a raid, the Lair Boss/Elder collects a tax for the Communal Hoard.
Players can declare they are **Skimming**: make a Slink test to hide choice loot for their private Gang Hoard. On failure, enforcers rough them up, seize the item, and the Gang loses Infamy.

### Source Documents
- `00_DEV_Brainstorms/Lair_Brainstorm.md`
"@
    },
    @{
        title = "[Lair/Downtime] Lair Downtime Activities Menu (Bar Fights, Rumors, Beast Taming)"
        labels = @("rules", "lair", "loop-2")
        body = @"
## Summary
Give each Boss 1-2 Downtime Actions in the Lair Phase:
1. **Goblin Bar Fight (Tough test):** Win = +1 Infamy and steal 1d6 Loot from a rival gang; lose = take 1 damage before the next raid.
2. **Listen for Rumors (Pay 2 Loot):** Learn dungeon layouts or monster vulnerabilities for the upcoming raid.
3. **Tame Wild Beasts (Tough/Brains test):** Domesticate captured wolves/spiders to unlock animal Mob archetypes (`[Wolf Rider]`).

### Source Documents
- `00_DEV_Brainstorms/Lair_Brainstorm.md`
- `00_DEV_Brainstorms/Researcher_Findings_Base_Building.md`
"@
    },
    @{
        title = "[Crafting] Scrap Cascade & Scarred Oddities System"
        labels = @("rules", "crafting", "loop-2")
        body = @"
## Summary
When Custom Gear shatters:
- Chassis disintegrates into raw Scrap.
- Each attached Oddity rolls a 1d6 survival check.
- Survived Oddities become **Scarred Oddities** (+1 permanent Bite/Defect). They can be recycled into new builds but become progressively more volatile.

### Source Documents
- `00_DEV_Brainstorms/creative_genius_crafting_analysis.md`
- `00_DEV_Brainstorms/crafting_mechanics_audit.md`
"@
    },
    @{
        title = "[Crafting] Tradeable Blueprints & Mob-Scale Consumable Crafting"
        labels = @("rules", "crafting", "loop-2")
        body = @"
## Summary
- **Blueprints:** Reverse Engineering creates physical, tradeable Blueprints that Gangs can hoard, steal, or archive with Elders.
- **Mob-Scale Crafting:** Crafters with a Workshop spend downtime and Scrap to mass-produce 1-raid consumable gear for an entire Mob (e.g., burning arrows, spiked shields).

### Source Documents
- `00_DEV_Brainstorms/creative_genius_crafting_analysis.md`
"@
    },
    @{
        title = "[Crafting/Loot] Master d66 Oddities Table"
        labels = @("content", "crafting", "loot")
        body = @"
## Summary
Implement the master catalog of 36 distinct Oddities with Tiers, Bites, and Rebound effects ready for loot distribution.

### Source Documents
- `00_DEV_Brainstorms/crafting_framework_brainstorm.md`
"@
    },
    @{
        title = "[Roguelite/Legacy] Generational Grudges & Phobias"
        labels = @("rules", "gang", "loop-3")
        body = @"
## Summary
When a Boss dies, the manner of their death creates a persistent cultural mark on the Gang:
- Boss successor gains a **Grudge** (+1d attack against that enemy/hazard type).
- The Mob gains a **Phobia** (-1d morale/scatter against that enemy/hazard type).

### Source Documents
- `00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md`
"@
    },
    @{
        title = "[Roguelite/Progression] Deeds & Scars Advancement Framework"
        labels = @("rules", "character", "loop-3")
        body = @"
## Summary
- **Deeds (Beat Model):** Require specific in-raid chaotic deeds to unlock high-tier Quirks (e.g. Pyromaniac's Joy requires surviving being on fire).
- **Scars (0 Grit Survival):** Roll on a Scar Table when reduced to 0 Grit to gain permanent mutations, weird bodily traits, or stat shifts.

### Source Documents
- `00_DEV_Brainstorms/Research_Deeds_Award_Mechanics.md`
"@
    },
    @{
        title = "[Roguelite/Crafting] Ancestral Relics & Bone Oddities"
        labels = @("rules", "crafting", "loop-3")
        body = @"
## Summary
Harvest bones from dead Bosses in the Bone Pile to craft custom **Bone Oddities / Relics**. Inherits tags based on how the Boss died or their highest stat.

### Source Documents
- `00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md`
- `00_DEV_Brainstorms/creative_genius_crafting_analysis.md`
"@
    },
    @{
        title = "[Gang/Mobs] Mob Mutiny Gauge & Pre-Raid Inter-Gang Wagers"
        labels = @("rules", "gang", "loop-3")
        body = @"
## Summary
- **Mob Mutiny Gauge:** Tracks Grunt ego and failed orders; triggers workplace mutinies if pushed too far.
- **Inter-Gang Pre-Raid Wagers:** Gangs place wagers before raids for bonus Infamy and bragging rights.

### Source Documents
- `00_DEV_Brainstorms/Gang_Mechanics_Brainstorm.md`
"@
    },
    @{
        title = "[Gang/Mobs] Mob Veterans & Demand Escalation"
        labels = @("rules", "gang", "mobs")
        body = @"
## Summary
Mobs surviving multiple raids gain **Veteran Traits** (e.g., fire resistance), but demand double pay/loot share to participate in future raids.

### Source Documents
- `00_DEV_Brainstorms/Lair_Brainstorm.md`
"@
    },
    @{
        title = "[Travel/Logistics] 4 Travel Roles & Laden/Over-Laden Encumbrance"
        labels = @("rules", "travel", "campaign")
        body = @"
## Summary
- **Travel Roles:** Formalize Map-Scrawler (Brains), Sniffer (Notice/Slink), Scavver (Tough), and Loud-Mouth (Mouth).
- **Laden & Over-Laden Encumbrance:** Return trip penalties (>50% and 100% capacity) with emergency loot jettisoning rules during ambushes.

### Source Documents
- `00_DEV_Brainstorms/TargetMechanic.csv`
- `01_STAGE_Drafts/07_Travel/00_Journey_Rules.md`
"@
    },
    @{
        title = "[Enemies/GM] Enemy Automata (Tick-Tock Action Clocks & Priority AI)"
        labels = @("rules", "enemies", "gm-tools")
        body = @"
## Summary
Standardize Boss/Elite monster execution without GM dice rolling:
- **Tick-Tock Action Clocks:** Predictable round countdown sequences (Sweep -> Inhale -> Blast -> Reset).
- **Priority Checklist AI:** 3-step deterministic If/Then priority queues.

### Source Documents
- `00_DEV_Brainstorms/Enemy_Modular_Threat_Framework_Brainstorm.md`
"@
    }
)

Write-Host "Creating $($issues.Count) issues in $Repo..." -ForegroundColor Cyan

foreach ($issue in $issues) {
    $payload = @{
        title  = $issue.title
        body   = $issue.body
        labels = $issue.labels
    } | ConvertTo-Json

    try {
        $uri = "https://api.github.com/repos/$Repo/issues"
        $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $payload -ContentType "application/json"
        Write-Host "Created issue #$($response.number): $($issue.title)" -ForegroundColor Green
    }
    catch {
        Write-Host "Failed to create issue '$($issue.title)': $_" -ForegroundColor Red
    }
}
