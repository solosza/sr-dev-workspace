# Build AI QA Resume

## Context
Write the new AI QA resume optimized for quality engineering, test automation, and AI-powered QA roles. Uses the positioning strategy and resume review as inputs.

## Type
BUILD

## Execution
inline

## Dependencies
- 004 (resume review)

## Phase Gate
- [ ] `projects/targeted-resume-pair/03-resume-review.md` exists
- [ ] `projects/targeted-resume-pair/00-positioning-research.md` exists

## Requirements
- Create `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-qa-engineer.md`
- Follow positioning strategy from 00-positioning-research.md
- Apply section-by-section changes from 03-resume-review.md
- **PROSE-ONLY format** — no bullet points, no asterisk lists. Use flowing paragraphs.
- Must reflect actual work: QA platforms (Playwright, Selenium, API, DB), compliance, healthcare/telecom/gov experience
- Lead with enterprise QA leadership, frame Isagawa as QA innovation
- Must include: contact info, summary, professional experience, Isagawa QA section, technical skills
- Optimize for ATS parsing: use standard section headers
- Target role titles identified in positioning strategy

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-qa-engineer.md` exists
- [ ] Has SUMMARY section
- [ ] No bullet points (no lines starting with `*`)
- [ ] Contains QA-specific keywords (Playwright, Selenium, pytest)

## Gates Satisfied
- BUILD-03, BUILD-05, BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
