# 006 — Score, Rank, and Write Structured Job List

**Type:** BUILD
**Depends on:** 003, 004, 005

## Goal

Consolidate all job findings from tasks 003-005, finalize match scores, rank jobs, and write the structured output files for this run. Output must be compatible with the job-application-spec pipeline (backlog 005).

## Requirements

- Read all three run output files from tasks 003, 004, 005
- Finalize match scores (1-10) for each job using profile from task 002
- Rank jobs by: (1) match score descending, (2) remote-friendly preference, (3) company tier
- Write `projects/ai-harness-job-search/runs/[date]-job-list.md`:
  - Ranked table: rank, company, title, location, remote, match score, URL
  - Notes section with top 5 recommendations and why
- Write `projects/ai-harness-job-search/runs/[date]-job-list.json`:
  - Array of job objects with fields: `company`, `title`, `location`, `remote`, `url`, `match_score`, `notes`
  - Format compatible with job-application-spec pipeline input
- Update `projects/ai-harness-job-search/README.md` with a summary of this run (date, jobs found, top pick)

## Acceptance Criteria

- [ ] `projects/ai-harness-job-search/runs/[date]-job-list.md` exists with ranked table and top 5 notes
- [ ] `projects/ai-harness-job-search/runs/[date]-job-list.json` exists and is valid JSON
- [ ] JSON has at least these fields per entry: `company`, `title`, `url`, `match_score`
- [ ] Jobs ranked by match score descending
- [ ] `projects/ai-harness-job-search/README.md` updated with run summary
- [ ] Top match score job is ≥7/10 (if none found at 7+, note in README that search yielded weak results)
