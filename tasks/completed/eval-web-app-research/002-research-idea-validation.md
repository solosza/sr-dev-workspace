# Research Idea Validation

## Context
Before investing in architecture or competitive analysis, we need to validate that demand exists for "submit your LLM artifact / infrastructure config / app spec, get it tested" as a service. This section feeds directly into 159's prerequisite gate.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Research demand signals for AI artifact testing as a service (forums, Twitter/X, HN, Reddit, job postings)
- Identify the target user persona per vertical (AI engineers, DevOps/compliance teams, QA teams, enterprises)
- Analyze which vertical has highest demand and lowest friction to launch first
- Assess whether the multi-vertical pitch is a day-one value prop or a growth narrative
- Use WebSearch to find demand signals, community discussions, and market sizing data
- Consider existing platform specs (platform-deepeval, platform-ssh, platform-selenium) as readiness indicators
- Recommend a first vertical with rationale

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/01-idea-validation.md` exists
- [ ] Contains section on demand signals with sources
- [ ] Contains target user persona analysis (per vertical)
- [ ] Contains first vertical recommendation with rationale
- [ ] Contains multi-vertical timing assessment (day-one vs growth)
- [ ] Minimum 400 words

## Gates Satisfied
DOC-01, DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
