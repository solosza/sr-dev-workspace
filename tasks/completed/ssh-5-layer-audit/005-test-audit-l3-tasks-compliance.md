# Audit L3 Tasks Compliance

## Context
Check that SSH platform tasks follow L3 patterns (compose metrics, return None).

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
- Find task files in SSH platform (framework/tasks/ or _reference/)
- Check each task class for: composing metrics from L2, returning None pattern
- Check import direction: tasks should import from L2 (metrics), not directly from SDK
- Write violations to `tasks/ssh-5-layer-audit/l3-violations.md`

## Acceptance Criteria
- [ ] L3 violations report exists at `tasks/ssh-5-layer-audit/l3-violations.md`
- [ ] Each task class checked for L3 pattern compliance
- [ ] Import direction verified (L3 → L2 only)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
