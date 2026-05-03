# 008 — Search Tier 1 Vertical AI Agent Companies

## Type
RESEARCH

## Description
Search for AI engineer roles at vertical AI agent companies that need governance scaffolding for domain-specific agents.

## Requirements
- Use WebSearch to find roles at:
  - Paratus Health (healthcare AI)
  - Moby Analytics
  - Bravi
  - Throxy
  - Ovlo
  - Other vertical AI agent companies with governance needs
- Write results to `projects/career-role-matching/raw/tier1-vertical-ai.json`
- Each entry: `{ url, company, title, location, remote, tier, domain_vertical, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/tier1-vertical-ai.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
