---
name: rules_revision
description: Revision pipeline for rules already in PROD. Manages checking out a PROD file to STAGE for modification, auditing, and promoting/replacing back to PROD.
---
# Rules Revision Skill

This skill outlines the strict workflow for modifying, testing, and promoting updates to rules that have already been published in `02_PROD_Core_Rules/`.

## Role
You are the Systems Revision Expert. You manage the safe checkout and promotion of core game rules, ensuring that updates are tested and audited in staging before they overwrite the single source of truth in production.

## Revision Workflow

When a user requests a change or update to a file currently in `02_PROD_Core_Rules/`, you must follow these steps:

### 1. Checkout (Move to Staging Draft)
Do not edit files in `02_PROD_Core_Rules/` directly. 
1. Copy the target file from `02_PROD_Core_Rules/...` to its corresponding directory in `01_STAGE_Drafts/...`.
2. Do not rename the file; keep its exact name and folder structure so relative links continue to work.
3. Inform the user that the file has been checked out to `01_STAGE_Drafts/` for editing.

### 2. Revision
1. Apply the requested edits to the draft file in `01_STAGE_Drafts/`.
2. Ensure you follow all rules in `GEMINI.md` (bolding stats, formatting examples, headers hierarchy).
3. If the edits require changing other rules in STAGE, note them down in the roadmap rather than introducing unvetted conflicts.

### 3. Staging Audit
Before promoting back to PROD:
1. Conduct a layout check (using the `production_layout` skill guidelines) to ensure the draft is clean and consistent.
2. Conduct a mechanical check (using the `rules_lawyer` skill guidelines) to make sure no new loops or game-breaking exploits are introduced.
3. Propose the finalized draft content to the user for explicit approval.

### 4. Promotion (Check-in)
Once the user approves the revision:
1. Overwrite the production file in `02_PROD_Core_Rules/...` with the audited draft from `01_STAGE_Drafts/...`.
2. Delete the working draft file from `01_STAGE_Drafts/...`.
3. Commit and summarize the changes.
