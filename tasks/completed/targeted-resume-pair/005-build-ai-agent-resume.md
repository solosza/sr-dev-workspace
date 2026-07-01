# Build AI Agent Resume

## Context
Write the new AI Agent resume optimized for agent infrastructure, agent engineering, and agentic systems roles. Uses the positioning strategy and resume review as inputs.

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
- Create `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-engineer.md`
- Follow positioning strategy from 00-positioning-research.md
- Apply section-by-section changes from 03-resume-review.md
- **PROSE-ONLY format** — no bullet points, no asterisk lists. Use flowing paragraphs.
- Must reflect actual work: Isagawa Kernel, multi-agent orchestration, evaluation platform, autonomous workflows
- Must include: contact info, summary, Isagawa section, professional experience, technical skills
- Optimize for ATS parsing: use standard section headers (SUMMARY, EXPERIENCE, SKILLS)
- Target role titles identified in positioning strategy

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-engineer.md` exists
- [ ] Has SUMMARY section
- [ ] No bullet points (no lines starting with `*`)
- [ ] Contains "Isagawa Kernel" reference

## Gates Satisfied
- BUILD-02, BUILD-04, BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
