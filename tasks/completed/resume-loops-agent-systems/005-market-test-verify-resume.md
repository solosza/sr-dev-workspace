# Verify Resume — Gates Check

## Context
Final verification that the resume meets all constraints: no em dashes, prose-only, loops/agent systems language present, PDF generated.

## Type
TEST

## Execution
agent

## Dependencies
- 004-market-build-generate-pdf

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md` updated
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.pdf` exists

## Requirements
- Read the resume markdown
- Verify no em dash characters (grep for unicode \u2014)
- Verify "loop" appears in agent systems context
- Verify "agent system" or "agent infrastructure" appears
- Verify prose-only format (no `- ` list items in body)
- Verify PDF exists and is under 60KB
- Report pass/fail for each check

## Acceptance Criteria
- [ ] No em dashes found in resume
- [ ] "loop" keyword present
- [ ] "agent system" or "agent infrastructure" present
- [ ] PDF exists and under 60KB

## Gates Satisfied
- TEST-01, TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
