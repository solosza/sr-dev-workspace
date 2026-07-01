# Build Recommendation Report

## Context
Synthesize all research findings into a prioritized, actionable recommendation report.

## Type
BUILD

## Execution
agent

## Dependencies
- 001-research-loop-optimization
- 002-research-enforcement-depth
- 003-research-domain-setup-and-lessons
- 004-research-external-governance-models

## Phase Gate
- [ ] All 4 research files exist in `projects/kernel-governance-depth/`

## Requirements
- Read all 4 research deliverables
- Synthesize into a single recommendation report
- Prioritize recommendations by impact and feasibility
- Each recommendation must specify: what changes, where in code, expected improvement
- Flag any recommendations that would require feature freeze exception
- Include a "do not do" section (ideas considered and rejected)

## Deliverable
Write to `projects/kernel-governance-depth/recommendation-report.md`

## Acceptance Criteria
- [ ] File exists with synthesized recommendations
- [ ] Recommendations prioritized (high/medium/low)
- [ ] Each recommendation has implementation specificity (file, change, outcome)
- [ ] "Do not do" section present
- [ ] All recommendations respect feature freeze

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
