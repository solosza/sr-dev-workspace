# Audit L4 Roles Compliance

## Context
Check that SSH platform roles follow L4 patterns (orchestrate tasks).

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
- Find role files in SSH platform (framework/roles/ or _reference/)
- Check each role class for: orchestrating tasks from L3
- Check import direction: roles should import from L3 (tasks), not from L2/L1/SDK directly
- Write violations to `tasks/ssh-5-layer-audit/l4-violations.md`

## Acceptance Criteria
- [ ] L4 violations report exists at `tasks/ssh-5-layer-audit/l4-violations.md`
- [ ] Each role class checked for L4 pattern compliance
- [ ] Import direction verified (L4 → L3 only)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
