# Add emission hook to learn.md

## Context
Adds a 1-2 line metric emission statement to /kernel/learn so it appends a structured JSON event to .claude/state/metrics.jsonl after every lesson recording. This is Tier 1 — lightweight, no new dependencies.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md`
- Add emission instruction after step 6 (skill extraction) and before step 7 (update state):
  ```
  6b. **Emit learn metric (append-only, failure does not block):**
      Append to `.claude/state/metrics.jsonl`:
      ```json
      {"schema_version":1,"timestamp":"<ISO>","event":"learn","trigger":"<test_failure|anchor_violation|manual>","lesson_topic":"<issue name>","files_modified":["<list of files changed>"]}
      ```
  ```
- Emission is append-only — failure to emit must NOT block the learn command
- No new dependencies added to isagawa-kernel
- Keep the addition to 3-5 lines maximum

## Acceptance Criteria
- [ ] `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md` contains `metrics.jsonl`
- [ ] Emission instruction is placed after lesson recording, before state update
- [ ] Instruction specifies append-only and non-blocking

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
