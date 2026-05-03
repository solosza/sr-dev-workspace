# 006 — Search Tier 1 Company Career Pages

## Type
RESEARCH

## Description
Search career pages of top AI infrastructure companies directly for matching roles.

## Requirements
- Use WebSearch to check career pages of:
  - Anthropic
  - OpenAI
  - Scale AI
  - Sierra
  - Glean
  - Google DeepMind
- Look for: Forward Deployed Engineer, AI Platform Engineer, Solutions Engineer, Infrastructure Engineer
- Write results to `projects/career-role-matching/raw/tier1-career-pages.json`
- Each entry: `{ url, company, title, location, remote, tier, salary_range, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/tier1-career-pages.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
