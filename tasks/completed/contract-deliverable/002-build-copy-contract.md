# Copy the Contract into the Target Repo

## Context
Backlog 201 (V-BASE): the contract is a deliverable — the platform ships its own law at framework/docs/.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Current branch is build/201-qa-build-contract-deliverable (CON-01)

## Requirements
- Copy `D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md` → `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/docs/5-layer-contract.md` (create framework/docs/)
- VERBATIM copy — no edits, no reformatting; the workspace stays source of truth

## Acceptance Criteria
- [ ] File exists at target path (CON-02)

## Gates Satisfied
- CON-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
