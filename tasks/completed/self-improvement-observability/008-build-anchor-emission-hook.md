# Add emission hook to anchor.md

## Context
Adds a metric emission statement to /kernel/anchor so it appends an anchor event to .claude/state/metrics.jsonl after every anchor ceremony. Tier 1.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/anchor.md`
- Add emission instruction in Part C after step 11 (archive actions log) and before step 12 (state current task):
  ```
  11b. **Emit anchor metric (append-only, failure does not block):**
       Append to `.claude/state/metrics.jsonl`:
       ```json
       {"schema_version":1,"timestamp":"<ISO>","event":"anchor","actions_count":<N>,"violations_found":<N>}
       ```
  ```
- Emission is append-only — failure to emit must NOT block the anchor command
- No new dependencies added

## Acceptance Criteria
- [ ] `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/anchor.md` contains `metrics.jsonl`
- [ ] Emission instruction is placed after actions log archive, before state update
- [ ] Instruction specifies append-only and non-blocking

## Gates Satisfied
- BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
