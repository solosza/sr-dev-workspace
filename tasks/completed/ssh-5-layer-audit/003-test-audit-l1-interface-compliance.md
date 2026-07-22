# Audit L1 Interface Compliance

## Context
Check that the SSH platform's interface layer follows L1 patterns from platform-deepeval.

## Type
TEST

## Execution
inline

## Dependencies
- 001-research-scan-ssh-platform-structure
- 002-research-read-5-layer-reference

## Phase Gate
- [ ] `tasks/ssh-5-layer-audit/ssh-platform-file-map.md` exists
- [ ] `tasks/ssh-5-layer-audit/5-layer-reference-checklist.md` exists

## Requirements
- Read the file map and reference checklist
- Find interface files in SSH platform (framework/interfaces/ or _reference/)
- Check: Does the SSH platform have a DeepEvalInterface equivalent?
- Check: Do all deepeval SDK imports go through the interface?
- Grep all Python files for `from deepeval` and `import deepeval` — these should ONLY appear in interface files
- Write violations to `tasks/ssh-5-layer-audit/l1-violations.md` with file:line, current code, required pattern

## Acceptance Criteria
- [ ] L1 violations report exists at `tasks/ssh-5-layer-audit/l1-violations.md`
- [ ] All direct SDK imports identified with file:line references
- [ ] Each violation has a remediation note

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
