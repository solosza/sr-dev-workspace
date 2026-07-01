# Add baseline snapshot step to learn.md

## Context
Before /kernel/learn modifies files, capture current structural test state as a baseline. This enables regression detection by comparing pre-learn and post-learn test results. Tier 2.

## Type
BUILD

## Execution
inline

## Dependencies
- 009 (Tier 1 verified)

## Phase Gate
- [ ] Tier 1 emission hooks verified (task 009 complete)

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md`
- Add baseline capture step BEFORE step 1 (identify what failed):
  ```
  0. **Capture pre-learn baseline (if platform-deepeval available):**
     If `D:/my_ai_projects/project_test_repos/platform-deepeval` exists:
     Run structural tests and capture results:
     ```bash
     python -m pytest "[platform-deepeval]/tests/" --harness-root "[workspace-root]" --rootdir "[platform-deepeval]" -k "structural" --tb=short -q 2>/dev/null
     ```
     Record result as pre_learn_baseline in `.claude/state/eval-results.jsonl`:
     ```json
     {"timestamp":"<ISO>","event":"pre_learn_baseline","tests":{"test_name":"PASS|FAIL",...}}
     ```
     If platform-deepeval is not available, skip silently (graceful degradation).
  ```
- Must handle missing platform-deepeval gracefully (skip, don't error)
- Must not add >10 seconds to learn event

## Acceptance Criteria
- [ ] learn.md contains `pre_learn_baseline` step
- [ ] Step includes graceful skip when platform-deepeval is unavailable
- [ ] Step is positioned BEFORE file modifications begin

## Gates Satisfied
- BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
