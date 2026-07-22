# Step 6: Write + Report

## Purpose

Persist the summary and display it to the user.

## Procedure

1. **Determine output target:**
   - **Integrated mode** (called by `/kernel/complete`): write to review-status.json
   - **Standalone mode** (called by user): display in conversation

2. **Integrated mode:**
   - Read `.claude/state/review-status.json`
   - Find or create the entry for this backlog number
   - Add `summary` key with the formatted summary text
   - Write review-status.json back (merge, don't overwrite)

3. **Standalone mode:**
   - Display the summary directly in conversation output
   - If the backlog has an entry in review-status.json, also write the summary there

4. **Discussion mode:**
   - After displaying, the user may respond with direction
   - If user wants follow-up work: use `/kernel/backlog` to create follow-up with parent linking
   - If user wants to accept: they can use `/kernel/review-queue accept`

## Acceptance Criteria

- [ ] Summary displayed to user (standalone) or persisted (integrated)
- [ ] review-status.json updated correctly (if applicable)
- [ ] No data loss in review-status.json (merge pattern used)
