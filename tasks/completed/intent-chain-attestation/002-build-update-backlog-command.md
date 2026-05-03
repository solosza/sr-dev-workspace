# Update backlog command with intent capture

## Context
Add an intent recording step to `.claude/commands/kernel/backlog.md` so the agent hashes the raw argument before creating/updating the backlog.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Requirements
- Edit `.claude/commands/kernel/backlog.md`
- Add a new step between "Get next number" (step 2) and "Assess complexity" (step 3):
  - **Step 2.5: Record intent**
  - After determining the backlog number (step 2), run:
    ```bash
    python lib/attestation/intent.py record NNN "the raw argument text" docs/backlog/NNN-tag-verb-object.md
    ```
  - Note: the backlog file may not exist yet (new item) — `record_intent` should handle `backlog_path` not existing (hash empty string for `backlog_hash_after` on first call)
  - For updates to existing backlog items, run the record AFTER the file is written so `backlog_hash_after` captures the updated content
- Adjust step numbering (current steps 3-7 become 4-8)
- Add a note: "The intent log is append-only. Each invocation of /kernel/backlog adds one entry."

## Acceptance Criteria
- [ ] `backlog.md` contains intent recording step
- [ ] Step references `python lib/attestation/intent.py record`
- [ ] Instructions handle both new and updated backlog items

## Gates Satisfied
BUILD-02
