# Build Recommendation Report

## Context
Synthesize all research into a concrete recommendation with implementation sketch.

## Type
BUILD

## Execution
agent

## Dependencies
- 001-research-map-workflow-state-consumers
- 002-research-classify-fields-by-scope
- 003-research-evaluate-isolation-strategies

## Phase Gate
- [ ] All 3 research files exist in `projects/workflow-state-isolation-research/`

## Requirements
- Read all 3 research deliverables
- Pick the recommended strategy (or hybrid)
- Write implementation sketch:
  - Which files change
  - What each change does (pseudocode or description)
  - Migration path (how to go from current to new without breaking sequential)
  - How execute-pipeline parallel dispatch integrates
  - How parent aggregates results from N agent workflow files
- Include a "rejected alternatives" section with one-line reason each
- Include the test plan: how to verify the fix works (re-run 150/151/152 parallel test)

## Deliverable
Write to `projects/workflow-state-isolation-research/recommendation.md`

## Acceptance Criteria
- [ ] File exists with concrete recommendation
- [ ] Implementation sketch lists every file to modify
- [ ] Migration path documented
- [ ] Test plan included
- [ ] Rejected alternatives listed

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
