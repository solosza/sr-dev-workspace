# Review Existing Resumes Against Strategy

## Context
Read the existing resumes and cross-reference against the positioning strategy. Produce a detailed review noting what to keep, change, remove, and add for each new resume variant.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 003 (positioning strategy)

## Phase Gate
- [ ] `projects/targeted-resume-pair/00-positioning-research.md` exists

## Requirements
- Read `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md`
- Read `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-qa-architect.md`
- Read `projects/targeted-resume-pair/00-positioning-research.md`
- For each new resume, produce a section-by-section review:
  - Summary: what to rewrite
  - Isagawa section: what to emphasize/de-emphasize
  - Professional experience: what to highlight for this track
  - Technical skills: what to add/remove
  - Format: confirm prose-only (no bullet points)
- Output to `projects/targeted-resume-pair/03-resume-review.md`

## Acceptance Criteria
- [ ] `projects/targeted-resume-pair/03-resume-review.md` exists
- [ ] Contains section-by-section review for both resume variants

## Gates Satisfied
- (none — feeds into BUILD-02, BUILD-03)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
