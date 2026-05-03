# Extract Resume Matching Profile

## Context
Read the AI agent architect resume and extract a structured matching profile — skills, keywords, target roles, and experience highlights. This profile is used by all subsequent search tasks to formulate queries and by the scoring task to rate job matches.

## Type
RESEARCH

## Execution
inline

## Dependencies
None

## Requirements
- Read the master resume at `D:\my_python_projects\resume-ai-pipeline\resumes\ai-agent-architect-resume.md`
- If the resume file does not exist, read backlog 029 `What I Built` section as fallback profile source
- Extract: skills (technical keywords), target roles, experience highlights, key projects
- Write structured JSON to `tasks/ai-job-search/output/resume-profile.json`

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/resume-profile.json` exists
- [ ] JSON contains `skills` array with at least 10 technical keywords
- [ ] JSON contains `target_roles` array with at least 4 role types
- [ ] JSON contains `experience_highlights` array
- [ ] JSON contains `key_projects` array

## Gates Satisfied
- BUILD-01, BUILD-02, BUILD-03

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
