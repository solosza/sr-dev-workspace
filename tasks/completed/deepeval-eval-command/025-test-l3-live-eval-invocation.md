# L3 Test: Live Eval Invocation Against check-data

## Context
Level 3 verification — actually invoke `/kernel/eval check-data D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` and verify it produces a scored report. This is an end-to-end test of the complete eval loop (create repo, compile harness, copy artifact, check components, generate tests, run and score).

## Type
TEST

## Execution
agent

## Dependencies
- 024-test-l2-reference-integrity

## Phase Gate
- [ ] L2 test passed (all references intact, all contracts valid)
- [ ] `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` exists and contains check-data skill
- [ ] `D:\my_ai_projects\project_test_repos\platform-deepeval` exists and contains _reference/ components

## Requirements
- Invoke `/kernel/eval check-data D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`
- The eval loop must:
  1. Create `D:\my_ai_projects\project_test_repos\eval-check-data-test\`
  2. Compile harness (kernel + deepeval spec + domain-setup)
  3. Copy check-data artifact with all dependencies
  4. Check _reference/ components, create missing ones
  5. Generate deepeval test suite
  6. Run tests and produce scored report
- Verify output contains:
  - Score table (Metric, Score, Threshold, Status)
  - Overall PASS/FAIL
  - Score history entry written to source repo
- If any step fails, capture the error and report which step failed and why

## Acceptance Criteria
- [ ] Eval loop completes all 6 steps without fatal error
- [ ] Scored report produced with at least one metric scored
- [ ] Score-history.json exists in hmsa-healthcare-qa's `eval/results/` directory
- [ ] Test repo `eval-check-data-test` was created and contains compiled harness

## Gates Satisfied
FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
