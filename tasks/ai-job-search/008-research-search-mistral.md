# Search Mistral Jobs

## Context
Search for AI agent platform, harness engineering, infrastructure, evaluation, and developer tools roles at Mistral AI.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-research-extract-resume-profile

## Phase Gate
- [ ] `tasks/ai-job-search/output/resume-profile.json` exists

## Requirements
- Use WebSearch to find current job openings at Mistral AI matching target roles
- Search queries should include: "Mistral AI careers agent platform engineer", "Mistral AI jobs infrastructure engineer", "Mistral AI developer tools engineer"
- Capture: job title, URL, location, remote status, key requirements
- Write results to `tasks/ai-job-search/output/raw-results/mistral.json`
- Do NOT filter at this stage — capture all potentially relevant listings

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/raw-results/mistral.json` exists
- [ ] JSON is valid and contains a `jobs` array
- [ ] Each job entry has: title, url, location, remote (boolean), requirements (array)

## Gates Satisfied
- BUILD-10

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
