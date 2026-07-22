# Audit L2 Metrics Compliance

## Context
Check that SSH platform metrics follow L2 patterns (evaluate, is_above_threshold, get_score).

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
- Find metric files in SSH platform (framework/metrics/ or _reference/)
- Check each metric class for: `evaluate()`, `is_above_threshold()`, `get_score()` methods
- Check metrics don't import directly from deepeval SDK (should use L1 interface)
- Write violations to `tasks/ssh-5-layer-audit/l2-violations.md`

## Acceptance Criteria
- [ ] L2 violations report exists at `tasks/ssh-5-layer-audit/l2-violations.md`
- [ ] Each metric class checked for required methods
- [ ] Import direction verified (L2 → L1 only)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
