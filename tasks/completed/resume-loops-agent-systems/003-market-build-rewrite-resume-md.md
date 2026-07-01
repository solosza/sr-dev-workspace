# Rewrite Resume Markdown — Loops and Agent Systems Framing

## Context
Full rewrite of the resume to lead with loops and agent systems. Must be factual, grounded, prose-only, no em dashes. Match isagawa.co tone.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-research-target-role-language
- 002-market-research-read-current-resume

## Phase Gate
- [ ] `projects/resume-loops-agent-systems/target-role-language.md` exists
- [ ] `projects/resume-loops-agent-systems/current-resume-analysis.md` exists

## Requirements
- Rewrite `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md`
- Lead with loops and agent systems language from the target role research
- Prose-only format (no bullet lists in body)
- No em dashes anywhere
- No inflated or debunkable claims
- Match isagawa.co tone: factual, technical, describes what was built
- Keep all factual content accurate (dates, companies, what was actually built)
- Incorporate target keywords naturally (not keyword stuffing)
- Contact: alain@isagawa.co, isagawa.co, GitHub orgs

## Acceptance Criteria
- [ ] File updated: `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md`
- [ ] No em dash characters in file
- [ ] Contains "loop" in context of agent systems
- [ ] Contains "agent system" or "agent infrastructure"
- [ ] Prose-only (no `- ` list items in body sections)
- [ ] isagawa.co tone maintained

## Gates Satisfied
- BUILD-01, TEST-01, TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
