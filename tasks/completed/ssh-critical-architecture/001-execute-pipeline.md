# Execute Pipeline: Backlog 178

## Task
Run `/kernel/execute-pipeline 178` to completion.

This will:
1. Read backlog 178 (Fix SSH Platform 5-Layer Critical Architecture)
2. Run task-builder to decompose into atomic tasks
3. Execute all tasks against the SSH platform repo

## Deliverable
SSH platform at `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/` with:
- L2 metrics layer created
- L3 refactored to compose L2 metrics
- L4 refactored to import L3 tasks
- L5 imports fixed
- All tests passing

## Acceptance Criteria
- [ ] L2 `framework/_reference/metrics/` directory exists with metric wrapper classes
- [ ] L3 `run_ssh_command.py` imports from metrics, not L1 directly
- [ ] L4 `ssh_batch_executor.py` imports L3 task functions
- [ ] L5 test files import from L4/L2, not validators
- [ ] Import direction: L5→L4→L3→L2→L1→SDK
- [ ] All existing tests pass
