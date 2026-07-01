# Research AI QA Job Market

## Context
Analyze the current AI-powered QA and quality engineering job market to understand what companies want, which skills are in highest demand, what role titles to target, and which companies are actively hiring. This informs the AI QA resume positioning.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Web search for current AI QA / AI-powered quality engineering roles (June/July 2026 market)
- Identify top role titles: AI QA Engineer, QA Automation Architect, AI Test Engineer, Quality Engineering Lead, etc.
- Identify most-demanded skills: AI-assisted testing, LLM evaluation, Playwright, Selenium, pytest, CI/CD, compliance testing
- Identify top hiring companies and industries (healthcare, fintech, enterprise SaaS)
- Identify what differentiates QA candidates (frameworks built, automation at scale, AI integration)
- Note salary ranges and remote availability
- Output findings to `projects/targeted-resume-pair/02-qa-market-research.md`

## Acceptance Criteria
- [ ] `projects/targeted-resume-pair/02-qa-market-research.md` exists
- [ ] Contains role titles, skills demand, top companies, differentiators

## Gates Satisfied
- (none — research feeds into BUILD-01)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
