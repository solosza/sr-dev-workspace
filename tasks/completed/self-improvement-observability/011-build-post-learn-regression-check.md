# Add post-learn regression check to learn.md

## Context
After /kernel/learn modifies files, run structural tests again and compare to baseline. Classify results as regression, pre-existing, or improvement. Tier 2.

## Type
BUILD

## Execution
inline

## Dependencies
- 010 (baseline snapshot added)

## Phase Gate
- [ ] learn.md contains `pre_learn_baseline` step

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md`
- Add regression check step AFTER step 6 (skill extraction) and the metrics emission (6b):
  ```
  6c. **Post-learn regression check (if baseline was captured):**
      If pre_learn_baseline was captured in step 0:
      Run structural tests again:
      ```bash
      python -m pytest "[platform-deepeval]/tests/" --harness-root "[workspace-root]" --rootdir "[platform-deepeval]" -k "structural" --tb=short -q 2>/dev/null
      ```
      Compare to baseline and classify:
      - Was PASS, now FAIL → REGRESSION (report, must fix before proceeding)
      - Was FAIL, still FAIL → PRE-EXISTING (warn, don't block)
      - Was FAIL, now PASS → IMPROVEMENT (report as positive)
      - Was PASS, still PASS → STABLE (no action)

      If any REGRESSION found: STOP. Fix the regression before continuing.
  ```
- Classification logic must be clear and mechanical

## Acceptance Criteria
- [ ] learn.md contains regression classification logic
- [ ] Classification covers all 4 cases (REGRESSION, PRE-EXISTING, IMPROVEMENT, STABLE)
- [ ] REGRESSION case blocks further progress until fixed

## Gates Satisfied
- BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
