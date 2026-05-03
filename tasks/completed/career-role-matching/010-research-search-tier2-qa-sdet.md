# 010 — Search Tier 2 QA/SDET Roles

## Type
RESEARCH

## Description
Search for Senior QA Automation Engineer and SDET roles as floor-tier positions.

## Requirements
- Use WebSearch to find listings on major job boards for:
  - "Senior QA Automation Engineer"
  - "Staff SDET"
  - "QA Platform Engineer"
  - "Test Infrastructure Engineer"
- Focus on remote-friendly, $140K-$190K+ range
- Write results to `projects/career-role-matching/raw/tier2-qa-sdet.json`
- Each entry: `{ url, company, title, location, remote, tier, salary_range, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/tier2-qa-sdet.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
