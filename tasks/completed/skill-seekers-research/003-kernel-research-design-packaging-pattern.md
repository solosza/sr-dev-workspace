# Research: Design the Packaging Pattern

## Context
With existing projects surveyed, design what a "research skill" looks like — how it's packaged, indexed, and invoked by future pipelines.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-survey-existing-projects.md

## Phase Gate
- [ ] `projects/skill-seekers-research/projects-survey.md` exists

## Requirements
- Design what a research skill's SKILL.md looks like — what does it contain? (key facts, structured data, invocation pattern)
- Assess auto-packaging feasibility: can a Python script scan projects/*/ and generate skill stubs? What's the minimum structure a project directory needs to be auto-packageable?
- Define the invocation model: how would a future pipeline reference "use findings from hoi-an-knockoff-shirts research"? (context injection into task file? Explicit skill invocation? Read tool?)
- Compare to RAG/vector search approaches — is a skill-based index better than embedding search for this?
- Identify the minimum viable pattern (MVP): what's the smallest implementation that makes research reusable without external dependencies?
- Write to `projects/skill-seekers-research/packaging-pattern-design.md`

## Acceptance Criteria
- [ ] `projects/skill-seekers-research/packaging-pattern-design.md` exists
- [ ] File defines what a research SKILL.md contains
- [ ] File assesses auto-packaging feasibility
- [ ] File covers the invocation model
- [ ] File defines an MVP pattern

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
