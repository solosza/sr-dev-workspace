# L3 Test — Execute Backlog 031 via /kernel/execute-pipeline

## Context
Level 3 production test: run the full execute-pipeline against backlog 031 (hmsa-healthcare-qa workspace). This exercises the entire pipeline end-to-end: parse existing backlog → task-builder decomposes → run-task.sh executes.

## Type
TEST

## Execution
agent

## Dependencies
- 013, 014 (L1 and L2 must pass first)

## Phase Gate
- [ ] 013-test-l1-verify-files.md in completed_tasks
- [ ] 014-test-l2-verify-flags.md in completed_tasks

## Requirements
1. Invoke `/kernel/execute-pipeline docs/backlog/031-domain-build-hmsa-healthcare-qa-workspace.md`
2. Pipeline should:
   - Skip backlog creation (existing file)
   - Run task-builder with skip_plan_review and no_execute flags
   - Spawn run-task.sh against the generated task folder
3. Verify results:
   - Task folder exists under `tasks/`
   - run-task.sh completed (check exit code or workflow state)
   - Workspace created at `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`
   - Kernel files present in new workspace
   - Domain-setup completed (protocol + state files exist)

## Acceptance Criteria
- [ ] Pipeline runs without manual intervention
- [ ] Task folder created with numbered task files
- [ ] run-task.sh executed and completed
- [ ] New workspace exists at target path
- [ ] Report produced by step 5 of execute-pipeline

## Gates Satisfied
- TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
