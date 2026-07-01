# Research Domain Setup and Lessons System

## Context
Analyze domain-setup bootstrapping quality and lessons system compounding for depth improvements.

## Type
RESEARCH

## Execution
agent

## Dependencies
- None

## Requirements
- Domain-setup: is scan-repo → extract-patterns → write-protocol the best bootstrap approach?
- How can protocol quality improve without adding steps?
- Should domain-setup produce tighter initial gates by default?
- Lessons: is the current format (issue, root cause, fix, anti-pattern, quality gate) capturing enough signal?
- How should lessons compound over time? Decay old lessons? Promote to hard rules?
- Should lessons auto-generate enforcement (lesson → hook rule)?

## Deliverable
Write findings to `projects/kernel-governance-depth/domain-setup-and-lessons.md`

## Acceptance Criteria
- [ ] File exists with analysis of both domain-setup and lessons
- [ ] Concrete recommendations for lessons compounding strategy
- [ ] Assessment of auto-enforcement feasibility
- [ ] No new commands or hooks proposed

## Gates Satisfied
- RESEARCH-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
