# 011 — Search Tier 2 Staff Engineer Roles

## Type
RESEARCH

## Description
Search for Staff Engineer roles at non-AI companies where system design skills translate.

## Requirements
- Use WebSearch to find listings at:
  - Stripe, Figma, Datadog, Cloudflare
  - Other high-growth non-AI companies hiring Staff Engineers
- Focus on: Staff Engineer, Principal Engineer, Platform Engineer
- Write results to `projects/career-role-matching/raw/tier2-staff-eng.json`
- Each entry: `{ url, company, title, location, remote, tier, salary_range, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/tier2-staff-eng.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
