# Write Final Research Report

## Context
Synthesizes audit surface analysis and static analysis design into final recommendation.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-kernel-research-static-analysis-design.md

## Phase Gate
- [ ] `projects/skill-security-research/static-analysis-design.md` exists

## Requirements
Write `projects/skill-security-research/research-report.md` covering:
1. The risk landscape — why third-party skills need auditing
2. Audit surface map — what's attackable and how
3. Static analysis design — the check categories and patterns
4. Output format — PASS/WARN/FAIL report spec
5. Pre-install hook feasibility
6. MVP scope — what the minimum viable auditor checks
7. Effort estimate — how much Python, how long to build
8. Recommendation: BUILD (with MVP scope) / SKIP

## Acceptance Criteria
- [ ] `projects/skill-security-research/research-report.md` exists
- [ ] File has BUILD/SKIP recommendation
- [ ] File is > 60 lines

## Gates Satisfied
- DOC-06, DOC-07, DOC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
