# Search xAI Jobs

## Context
Search for AI agent platform, harness engineering, infrastructure, evaluation, and developer tools roles at xAI (Elon Musk's AI company).

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-research-extract-resume-profile

## Phase Gate
- [ ] `tasks/ai-job-search/output/resume-profile.json` exists

## Requirements
- Use WebSearch to find current job openings at xAI matching target roles
- Search queries should include: "xAI careers agent platform engineer", "xAI jobs infrastructure engineer", "xAI developer tools engineer"
- Capture: job title, URL, location, remote status, key requirements
- Write results to `tasks/ai-job-search/output/raw-results/xai.json`
- Do NOT filter at this stage — capture all potentially relevant listings

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/raw-results/xai.json` exists
- [ ] JSON is valid and contains a `jobs` array
- [ ] Each job entry has: title, url, location, remote (boolean), requirements (array)

## Gates Satisfied
- BUILD-08

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
