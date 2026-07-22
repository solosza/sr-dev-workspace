# Step 1: Discover

## Purpose

Find all completed backlogs that haven't been reviewed yet by diffing `docs/backlog/done/` against `.claude/state/review-status.json`.

## Pre-generation Checkpoint

- Read: `docs/backlog/done/*.md` (glob all completed backlogs)
- Read: `.claude/state/review-status.json` (current review state)

## Procedure

1. Glob `docs/backlog/done/*.md` to get all completed backlog files
2. Extract backlog numbers from filenames (NNN prefix pattern: `NNN-*.md`)
3. Read `.claude/state/review-status.json`:
   - If file doesn't exist, create with empty `reviewed` object and zero stats
   - If file exists, parse the `reviewed` object
4. Compute diff: completed backlog numbers minus reviewed backlog numbers = unreviewed set
5. If unreviewed set is empty: skip to Step 5 (report "all reviewed")
6. Output: list of unreviewed backlog numbers and their file paths

## Acceptance Criteria

- [ ] All completed backlogs discovered via glob
- [ ] Backlog numbers extracted from filenames
- [ ] Review state loaded or initialized
- [ ] Unreviewed set computed correctly

## Verification

- Count of completed backlogs matches glob result count
- Count of reviewed + unreviewed = total completed
