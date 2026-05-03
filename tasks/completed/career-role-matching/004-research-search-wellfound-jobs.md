# 004 — Search Wellfound (AngelList) Jobs

## Type
RESEARCH

## Description
Search Wellfound for startup roles matching the profile, focusing on seed/Series A AI agent companies.

## Requirements
- Use WebSearch to find Wellfound listings for:
  - "Founding Engineer AI"
  - "AI Infrastructure Engineer startup"
  - "Agent platform engineer"
- Focus on seed-stage and Series A companies
- Write results to `projects/career-role-matching/raw/wellfound.json`
- Each entry: `{ url, company, title, location, remote, tier, salary_range, equity_range, posted_date, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/wellfound.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
