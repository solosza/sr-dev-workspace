# Write Decision Framework

## Context
Synthesize findings from tasks 001-003 into a concrete decision framework that answers: "For a given project, should I build it as a traditional app or as a kernel skill?"

## Type
BUILD

## Execution
inline

## Dependencies
- 001, 002, 003, 004

## Phase Gate
- [ ] `projects/kernel-architecture/` exists (task 004)
- [ ] Website cloner analysis complete (task 001)
- [ ] Fraud detector analysis complete (task 002)
- [ ] Portfolio site analysis complete (task 003)

## Requirements
- Write the `## Decision Framework` section of `projects/kernel-architecture/skill-as-app-research.md`
- Include a decision tree or matrix with clear criteria:
  - Does the deliverable need to run without an agent? → traditional
  - Is the deliverable a one-time generation? → skill
  - Does it need persistent state between runs? → traditional (or hybrid)
  - Is the "app" really a workflow? → skill
  - Does it need a UI for humans? → traditional (agent builds it)
- Include trade-off analysis for each approach
- Use the two test subjects as concrete examples in the framework
- Framework must be actionable — given a new project, you can follow it to decide

## Acceptance Criteria
- [ ] `projects/kernel-architecture/skill-as-app-research.md` exists with `## Decision Framework` section
- [ ] Decision tree/matrix with at least 5 criteria
- [ ] Both test subjects referenced as examples
- [ ] Trade-offs documented

## Gates Satisfied
BUILD-02, BUILD-03, BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
