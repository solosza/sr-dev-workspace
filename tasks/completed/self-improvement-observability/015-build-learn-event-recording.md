# Add learn event recording to learn.md

## Context
After each lesson recording, append a learn event to .claude/state/learn-events.jsonl linking the lesson to the code changes made. This enables rollback tracking.

## Type
BUILD

## Execution
inline

## Dependencies
- 004 (learn-events schema exists)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/learn-events.jsonl.schema.json` exists

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md`
- Add learn event recording step after the metrics emission (step 6b):
  ```
  6e. **Record learn event (append-only, failure does not block):**
      Append to `.claude/state/learn-events.jsonl`:
      ```json
      {"learn_event_id":"<UUID or timestamp-based>","timestamp":"<ISO>","lesson_topic":"<issue name>","trigger":"<test_failure|anchor_violation|manual>","files_modified":["<list>"],"git_commit_hash":"<if available>","status":"active"}
      ```
  ```
- Recording is append-only, failure does not block
- No new dependencies

## Acceptance Criteria
- [ ] learn.md contains `learn-events.jsonl` recording step
- [ ] Step captures lesson_topic, trigger, files_modified, status
- [ ] Step specifies append-only and non-blocking

## Gates Satisfied
- BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
