# Add eval-results.jsonl logging to learn.md

## Context
Log the post-learn regression check results to eval-results.jsonl for trend analysis. Tier 2.

## Type
BUILD

## Execution
inline

## Dependencies
- 011 (regression check added)

## Phase Gate
- [ ] learn.md contains regression classification logic

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md`
- After the regression check (step 6c), add results logging:
  ```
  6d. **Log regression check results (append-only):**
      Append post-learn results to `.claude/state/eval-results.jsonl`:
      ```json
      {"timestamp":"<ISO>","event":"post_learn_check","baseline_tests":{"test_name":"PASS|FAIL"},"post_tests":{"test_name":"PASS|FAIL"},"regressions":[],"improvements":[],"pre_existing":[]}
      ```
  ```
- Logging is append-only, failure does not block

## Acceptance Criteria
- [ ] learn.md contains `eval-results.jsonl` logging step
- [ ] Logging captures both baseline and post-learn results
- [ ] Logging includes classification arrays (regressions, improvements, pre_existing)

## Gates Satisfied
- BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
