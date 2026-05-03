# 007 — Search Tier 1 Agent Startups (YC W26 Cohort)

## Type
RESEARCH

## Description
Deep search for founding/early engineer roles at YC W26 agent-infrastructure startups.

## Requirements
- Use WebSearch to find hiring pages and job listings for:
  - Rubric AI, Salus, Sentrial, Moda, OpenSpec, Cofia, Emdash
  - Other W26 batch companies in agent/AI infrastructure space
- Check each company's website, LinkedIn, and Lever/Greenhouse/Ashby boards
- Write results to `projects/career-role-matching/raw/tier1-agent-startups.json`
- Each entry: `{ url, company, title, location, remote, tier, equity_range, yc_batch, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/tier1-agent-startups.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
