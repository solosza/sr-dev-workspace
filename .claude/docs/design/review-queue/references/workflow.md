# Review Queue — Workflow

## Step 1: Discover

**Purpose:** Find all completed backlogs that haven't been reviewed yet.

**Procedure:**
1. Glob `docs/backlog/done/*.md` to get all completed backlogs
2. Read `.claude/state/review-status.json` (create empty if missing)
3. Extract backlog numbers from filenames (NNN prefix)
4. Diff: completed set minus reviewed set = unreviewed items
5. Output: list of unreviewed backlog paths

**Pre-generation checkpoint:**
- Read: `docs/backlog/done/` (glob)
- Read: `.claude/state/review-status.json`

## Step 2: Present

**Purpose:** Sort unreviewed items by priority and show the next one.

**Procedure:**
1. Apply priority ordering (→ [[priority-ordering]])
2. Format the top item as a review card:
   - Backlog number, title, scope, priority
   - Summary (first paragraph)
   - Deliverable location
   - Completion date (from file modification or done/ move date)
3. Show available actions: accept, iterate, reject, skip, defer

**Pre-generation checkpoint:**
- Read: each unreviewed backlog file (for title, summary, scope)

## Step 3: Act

**Purpose:** Process the user's selected quick action.

**Procedure:**
1. Parse user action:
   - `accept` — mark as accepted
   - `iterate [notes]` — create follow-up backlog via `/kernel/backlog`, mark as needs-iteration
   - `reject [reason]` — mark as rejected with reason
   - `skip` — move to next item without state change
   - `defer` — mark as deferred, push to end of queue
2. For `iterate`: invoke `/kernel/backlog` with parent_backlog link and iteration notes
3. Record action with timestamp

## Step 4: Update State

**Purpose:** Write the state transition to review-status.json.

**Procedure:**
1. Read current review-status.json
2. Add/update entry for the reviewed backlog number:
   ```json
   {
     "NNN": {
       "status": "accepted | needs-iteration | rejected | deferred",
       "reviewed_at": "ISO timestamp",
       "notes": "user notes if any",
       "followup_backlog": "NNN (if iterate action)"
     }
   }
   ```
3. Update aggregate stats
4. Write back to review-status.json

**Pre-generation checkpoint:**
- Read: `.claude/state/review-status.json` (current state)

## Step 5: Report

**Purpose:** Show summary statistics and present next item if available.

**Procedure:**
1. Compute stats from review-status.json:
   - Total completed, reviewed, unreviewed
   - Accepted, needs-iteration, rejected, deferred
2. If more unreviewed items: show next item (loop to Step 2)
3. If all reviewed: show final summary

**Output format:**
```
REVIEW QUEUE — [N] unreviewed

[Review card for next item]

Stats: [total] completed | [reviewed] reviewed | [unreviewed] remaining
       [accepted] accepted | [iteration] iterating | [rejected] rejected

Actions: accept | iterate [notes] | reject [reason] | skip | defer
```
