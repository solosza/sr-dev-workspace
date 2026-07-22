# Audit Import Direction

## Context
Verify strict downward import direction across all layers (L5->L4->L3->L2->L1->SDK).

## Type
TEST

## Execution
inline

## Dependencies
- 001-research-scan-ssh-platform-structure
- 003 through 007 (all layer audits)

## Phase Gate
- [ ] All layer violation files exist (l1 through l5)

## Requirements
- Read all violation files from tasks 003-007
- Build a full import graph across all Python files in the SSH platform
- Identify any upward imports (e.g., L1 importing from L2, L2 importing from L3)
- Identify any skip-layer imports (e.g., L5 importing directly from L1)
- Write violations to `tasks/ssh-5-layer-audit/import-direction-violations.md`

## Acceptance Criteria
- [ ] Import direction violations report exists at `tasks/ssh-5-layer-audit/import-direction-violations.md`
- [ ] All upward imports identified
- [ ] All skip-layer imports identified
- [ ] Each violation has file:line reference

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
