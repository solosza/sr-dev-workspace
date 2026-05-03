# 005 — Search YC Work at a Startup

## Type
RESEARCH

## Description
Search Y Combinator's Work at a Startup platform for roles at YC-backed companies, especially the W26 agent-infra cohort.

## Requirements
- Use WebSearch to find YC startup jobs:
  - Search workatastartup.com for AI agent roles
  - Look specifically for: Rubric AI, Salus, Sentrial, Moda, OpenSpec, Cofia, Emdash
- Write results to `projects/career-role-matching/raw/yc-startups.json`
- Each entry: `{ url, company, title, location, remote, tier, yc_batch, funding_stage, notes }`

## Acceptance Criteria
- [ ] `projects/career-role-matching/raw/yc-startups.json` exists and is valid JSON

## Gates
BUILD-03 (partial)
