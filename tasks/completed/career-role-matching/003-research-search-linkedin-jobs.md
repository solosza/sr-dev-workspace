# 003 — Search LinkedIn Jobs

## Type
RESEARCH

## Description
Search LinkedIn for job listings across all role tiers defined in backlog 036.

## Requirements
- Use WebSearch to find LinkedIn job listings matching:
  - "AI Platform Engineer"
  - "AI Agent Infrastructure Engineer"
  - "Forward Deployed Engineer AI"
  - "AI Solutions Architect"
  - "Senior QA Automation Engineer"
  - "Staff Engineer"
- Filter for remote-friendly or major tech hubs
- Write results to `projects/career-role-matching/raw/linkedin.json`
- Each entry: `{ url, company, title, location, remote, tier, salary_range, posted_date, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/linkedin.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
