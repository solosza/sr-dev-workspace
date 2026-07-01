# Positioning Strategy

## Context
Synthesize the agent and QA market research with the user's actual skillset to determine the optimal positioning for each resume. Produce a positioning strategy document that defines what to emphasize, de-emphasize, and add for each resume variant.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001, 002 (both market research reports)

## Phase Gate
- [ ] `projects/targeted-resume-pair/01-agent-market-research.md` exists
- [ ] `projects/targeted-resume-pair/02-qa-market-research.md` exists

## Requirements
- Read both market research reports
- Read existing resumes at `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/`
- Read profile.json for context
- Map user's strengths to market demand for each track
- Identify gaps: skills the market wants that the user has but doesn't highlight
- Define positioning strategy for each resume:
  - **AI Agent resume:** What to lead with, what to emphasize from Isagawa work, what professional experience to highlight
  - **AI QA resume:** What to lead with, what QA achievements to elevate, how to frame Isagawa as QA innovation
- Determine best target role titles for each
- Output to `projects/targeted-resume-pair/00-positioning-research.md`

## Acceptance Criteria
- [ ] `projects/targeted-resume-pair/00-positioning-research.md` exists
- [ ] Contains positioning strategy for both resume variants
- [ ] Identifies specific sections to change in each resume

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
