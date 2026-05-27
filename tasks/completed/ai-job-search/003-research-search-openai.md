# Search OpenAI Jobs

## Context
Search for AI agent platform, harness engineering, infrastructure, evaluation, and developer tools roles at OpenAI. OpenAI is a top-priority company (relocation considered).

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-research-extract-resume-profile

## Phase Gate
- [ ] `tasks/ai-job-search/output/resume-profile.json` exists

## Requirements
- Use WebSearch to find current job openings at OpenAI matching target roles
- Search queries should include: "OpenAI careers AI agent platform engineer", "OpenAI jobs infrastructure engineer", "OpenAI developer tools engineer"
- Capture: job title, URL, location, remote status, key requirements
- Write results to `tasks/ai-job-search/output/raw-results/openai.json`
- Do NOT filter at this stage — capture all potentially relevant listings

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/raw-results/openai.json` exists
- [ ] JSON is valid and contains a `jobs` array
- [ ] Each job entry has: title, url, location, remote (boolean), requirements (array)

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
