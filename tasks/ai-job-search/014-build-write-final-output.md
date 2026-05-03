# Write Final Job Search Output

## Context
Produce the final output file in a format compatible with the job-application-spec pipeline (backlog 005). This is the deliverable for backlog 029.

## Type
BUILD

## Execution
inline

## Dependencies
- 013-build-score-jobs-against-profile

## Phase Gate
- [ ] `tasks/ai-job-search/output/scored-results.json` exists

## Requirements
- Read `tasks/ai-job-search/output/scored-results.json`
- Write final output to `tasks/ai-job-search/output/job-search-results.json` with schema:
  ```json
  {
    "generated": "2026-04-05",
    "source_backlog": "029-market-research-ai-harness-engineering-jobs",
    "total_jobs": N,
    "companies_searched": 10,
    "jobs": [
      {
        "url": "https://...",
        "company": "Anthropic",
        "title": "AI Agent Platform Engineer",
        "location": "San Francisco, CA",
        "remote": true,
        "match_score": 85,
        "score_breakdown": { ... },
        "requirements": ["Python", "distributed systems", ...]
      }
    ]
  }
  ```
- Ensure every job has all required fields: url, company, title, location, remote, match_score
- Include only jobs with match_score >= 40 (filter out clearly irrelevant results)

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/job-search-results.json` exists
- [ ] JSON is valid
- [ ] Every job has: url, company, title, location, remote (boolean), match_score (number 0-100)
- [ ] All jobs have match_score >= 40
- [ ] Jobs are sorted by match_score descending

## Gates Satisfied
- BUILD-15, FUNC-01, FUNC-02, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, this task set is complete.
