# Step 5: Report

## Purpose

Show summary statistics and present next unreviewed item if available.

## Pre-generation Checkpoint

- Read: `.claude/state/review-status.json` (updated state from Step 4)

## Procedure

1. Read review-status.json stats
2. Format summary:
   ```
   REVIEW QUEUE — [N] unreviewed

   Stats: [total] completed | [reviewed] reviewed | [unreviewed] remaining
          [accepted] accepted | [iteration] iterating | [rejected] rejected
   ```
3. If more unreviewed items remain:
   - Show "Next item available. Run `/kernel/review-queue` to continue."
4. If all reviewed:
   - Show "All completed backlogs reviewed."
5. If `--stats` mode was requested:
   - Show only the stats summary, no review card

## Acceptance Criteria

- [ ] Stats computed from review-status.json
- [ ] Stats displayed in standard format
- [ ] Next item hint shown if unreviewed items remain
- [ ] All-reviewed message shown if queue is empty
