# Task 004: Research — Design Sync Workflow Integration

## Objective
Design how versioning integrates with the existing kernel workflow (domain-setup, anchor, sync).

## Instructions

1. Read the drift detection design from task 003 in the report
2. Design integration points:
   - **domain-setup** — could check kernel version on first run, warn if master is newer
   - **anchor** — could include a periodic version check (every N anchors?)
   - **New command: `/kernel/sync`** — pull latest artifacts from master, update manifest
   - **New command: `/kernel/upgrade`** — guided upgrade with changelog review
   - **Backlog 057's manual sync** — how does versioning make this automated?
3. For each integration point, assess:
   - Does it require changes to existing commands?
   - Does it need network access (to check master repo)?
   - What happens when the user is offline?
   - What's the UX? (automatic? prompted? blocking?)
4. Write findings as `## 4. Sync Workflow Integration` in the report
   - Include a workflow diagram (text-based) showing how version check flows through the kernel loop
   - Include recommendations for which integration points to implement first

## Acceptance Criteria
- At least 2 integration points described
- Workflow diagram present
- Prioritized implementation order

## Gate
RESEARCH-04
