# Score Jobs Against Profile

## Context
Score each compiled job listing against the extracted resume profile. Match score is 0-100 based on skills overlap, role alignment, and requirements match.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-research-extract-resume-profile
- 012-build-compile-raw-results

## Phase Gate
- [ ] `tasks/ai-job-search/output/resume-profile.json` exists
- [ ] `tasks/ai-job-search/output/compiled-results.json` exists

## Requirements
- Read `tasks/ai-job-search/output/resume-profile.json` for matching criteria
- Read `tasks/ai-job-search/output/compiled-results.json` for job listings
- For each job, calculate match_score (0-100) based on:
  - Skills keyword overlap with job requirements (40% weight)
  - Role title alignment with target_roles (30% weight)
  - Remote status preference match (15% weight)
  - Company tier (top-priority companies get 15% bonus: Anthropic, OpenAI, Google DeepMind)
- Add `match_score` and `score_breakdown` fields to each job
- Sort jobs by match_score descending
- Write scored results to `tasks/ai-job-search/output/scored-results.json`

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/scored-results.json` exists
- [ ] JSON is valid with `jobs` array
- [ ] Every job has `match_score` (number 0-100) and `score_breakdown` (object)
- [ ] Jobs are sorted by match_score descending

## Gates Satisfied
- FUNC-03

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
