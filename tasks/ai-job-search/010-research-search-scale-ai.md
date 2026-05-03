# Search Scale AI Jobs

## Context
Search for AI agent platform, harness engineering, infrastructure, evaluation, and developer tools roles at Scale AI.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-research-extract-resume-profile

## Phase Gate
- [ ] `tasks/ai-job-search/output/resume-profile.json` exists

## Requirements
- Use WebSearch to find current job openings at Scale AI matching target roles
- Search queries should include: "Scale AI careers agent platform engineer", "Scale AI jobs AI infrastructure engineer", "Scale AI developer tools engineer"
- Capture: job title, URL, location, remote status, key requirements
- Write results to `tasks/ai-job-search/output/raw-results/scale-ai.json`
- Do NOT filter at this stage — capture all potentially relevant listings

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/raw-results/scale-ai.json` exists
- [ ] JSON is valid and contains a `jobs` array
- [ ] Each job entry has: title, url, location, remote (boolean), requirements (array)

## Gates Satisfied
- BUILD-12

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
