# Write the Target Repo README Stub

## Context
Backlog 198 (Wave 0): a minimal README naming the platform and pointing at the workspace design docs — real enterprise docs come in Phase 6, documenting built code.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Target repo is a git repository (GIT-01 passing)

## Requirements
- Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/README.md`: title "HMSA QA Platform", one-paragraph description (multi-interface QA test platform — Browser/REST/SQL Server/SOAP — built on the 5-layer architecture), a note that design docs and the governing contract live in the sr_dev_workspace project folder, and that `framework/docs/5-layer-contract.md` will carry the shipped contract
- Keep it under 25 lines — it is a stub, not Phase 6 documentation

## Acceptance Criteria
- [ ] `README.md` exists in target repo root
- [ ] Contains "HMSA QA Platform" (case-insensitive grep ≥ 1)
- [ ] Under 25 lines

## Gates Satisfied
- GIT-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
