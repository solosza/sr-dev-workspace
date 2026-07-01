# Resume Quality Check

## Context
Validates both resumes meet format requirements (prose-only, ATS-friendly, complete sections) and are properly differentiated for their target markets.

## Type
TEST

## Execution
agent

## Dependencies
- 005, 006 (both resumes)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-engineer.md` exists
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-qa-engineer.md` exists

## Requirements
- Verify both resumes exist and are non-empty
- Verify neither resume contains bullet points (no lines starting with `*` or `-`)
- Verify both have required sections: SUMMARY, EXPERIENCE/PROFESSIONAL EXPERIENCE, TECHNICAL SKILLS
- Verify resumes are differentiated (different summaries, different emphasis)
- Verify agent resume leads with agent infrastructure / Isagawa work
- Verify QA resume leads with professional QA experience
- Verify both reference isagawa.co portfolio

## Acceptance Criteria
- [ ] Both resumes exist and are >100 lines each
- [ ] Neither contains bullet points
- [ ] Both have SUMMARY, EXPERIENCE, SKILLS sections
- [ ] Agent resume summary mentions "agent" or "infrastructure"
- [ ] QA resume summary mentions "quality" or "QA" or "testing"

## Gates Satisfied
- BUILD-02 through BUILD-07 (all gates)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
