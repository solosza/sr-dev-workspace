# Write References INDEX.md

## Context
Layer 4 of the 6-layer command-skill-pattern. INDEX.md is the reference index — it lists all reference files organized by step, with one-line descriptions. This is an INDEX file (points to payloads, never contains payload).

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/INDEX.md`
- Must contain a table listing all reference files:
  - `step-02/kernel-file-list.md` — exact files to copy from kernel
  - `step-02/deepeval-file-list.md` — exact files to copy from platform-deepeval
  - `step-03/dependency-resolution.md` — how to scan and resolve artifact dependencies
  - `step-04/component-decision-table.md` — use existing vs. create new decision matrix
  - `step-05/golden-translation-patterns.md` — reference pattern for golden dataset generation
  - `step-06/metric-selection.md` — which metrics for which pipeline types
  - `step-06/report-format.md` — scored report template
- Must be an index only — no inline implementation
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/INDEX.md`
- [ ] `grep -q "kernel-file-list" .claude/skills/eval/references/INDEX.md` passes
- [ ] `grep -q "report-format" .claude/skills/eval/references/INDEX.md` passes
- [ ] `grep -q "golden-translation" .claude/skills/eval/references/INDEX.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-11, INT-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
