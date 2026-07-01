# Research Target Role Language for Loops and Agent Systems

## Context
Understand what language job postings use for the roles we're targeting. The resume must match ATS filters and recruiter expectations.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Read docs/backlog/029-market-research-ai-harness-engineering-jobs.md for target roles and companies
- Read docs/backlog/done/036-market-research-career-role-matching.md for tier 1-3 role categories
- Extract the specific keywords, phrases, and framing job postings use around: agent infrastructure, loop orchestration, agent systems, agent governance, enforcement
- Identify which terms appear most frequently in job titles vs job descriptions
- Note the gap between current resume language and target role language
- Output: keyword/phrase mapping document

## Acceptance Criteria
- [ ] File exists: `projects/resume-loops-agent-systems/target-role-language.md`
- [ ] At least 10 target keywords/phrases extracted from job postings
- [ ] Gap analysis between current resume and target language included

## Gates Satisfied
- RESEARCH-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
