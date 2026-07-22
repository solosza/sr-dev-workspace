# Write Compliance Report

## Context
Synthesize all layer audits and import direction audit into a final compliance report.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 through 008 (all audit tasks)

## Phase Gate
- [ ] `tasks/ssh-5-layer-audit/l1-violations.md` exists
- [ ] `tasks/ssh-5-layer-audit/l2-violations.md` exists
- [ ] `tasks/ssh-5-layer-audit/l3-violations.md` exists
- [ ] `tasks/ssh-5-layer-audit/l4-violations.md` exists
- [ ] `tasks/ssh-5-layer-audit/l5-violations.md` exists
- [ ] `tasks/ssh-5-layer-audit/import-direction-violations.md` exists

## Requirements
- Read all violation files
- Write final compliance report to `projects/ssh-5-layer-audit/compliance-report.md`
- Report must include:
  - Executive summary (compliant vs non-compliant file counts)
  - Per-layer violation tables (file:line, violation type, current code, required pattern)
  - Import direction violations
  - Remediation steps grouped by violation type
  - Priority ordering (critical violations first: direct SDK imports > wrong import direction > missing methods > style)
  - Recommendation: whether a remediation backlog item is needed

## Acceptance Criteria
- [ ] Compliance report exists at `projects/ssh-5-layer-audit/compliance-report.md`
- [ ] Contains per-file violation list with file:line references
- [ ] Contains summary counts
- [ ] Contains remediation steps
- [ ] Contains priority ordering

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
