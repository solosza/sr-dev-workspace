# Step 2: Present

## Purpose

Sort unreviewed items by priority and display the next review card.

## Pre-generation Checkpoint

- Read: each unreviewed backlog file (for title, summary, scope, priority)
- Read: `.claude/docs/design/review-queue/references/priority-ordering.md` (sort rules)

## Procedure

1. For each unreviewed backlog, read the file and extract:
   - Backlog number (from filename)
   - Title (first `#` heading)
   - Scope (from `## Summary` or `## Task Builder Input`)
   - Priority (from `## Priority` section)
   - Summary (first paragraph after title)
2. Apply priority ordering:
   - Tier 1: Iteration follow-ups (have `parent_backlog` field)
   - Tier 2: Recent completions (last 7 days)
   - Tier 3: High/Critical priority
   - Tier 4: Everything else
   - Tie-break: highest backlog number first
3. Format the top item as a review card:
   ```
   REVIEW: #NNN — [title]
   Scope: [scope]  Priority: [priority]

   [summary]

   Deliverable: [location from Task Builder Input]

   Actions: accept | iterate [notes] | reject [reason] | skip | defer
   ```

## Acceptance Criteria

- [ ] All unreviewed backlogs read and parsed
- [ ] Priority ordering applied correctly
- [ ] Review card formatted with all required fields
