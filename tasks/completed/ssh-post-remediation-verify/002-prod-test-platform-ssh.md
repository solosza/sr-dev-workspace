# Task 002: Prod Test Platform SSH

## Objective
Run production test on platform-ssh to verify the 5-layer architecture works end-to-end.

## Instructions
1. Run `/kernel/prod-test D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh`
2. This will:
   - Assemble master repo with kernel
   - Run domain-setup
   - Copy to test repo
   - Execute L1/L2/L3 tests
3. Review test results
4. Write results to `projects/ssh-5-layer-audit/prod-test-results.md`

## Acceptance Criteria
- [ ] Prod test completed
- [ ] L1 tests pass (interface layer)
- [ ] L2 tests pass (metrics layer — new from backlog 178)
- [ ] L5 tests pass (existing tests still work)
- [ ] Results documented
