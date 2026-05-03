# 002 — Extract Portfolio Matching Profile

## Type
RESEARCH

## Description
Extract the user's matching profile from backlogs 036 and 029 into a structured JSON file. This profile is used by task 014 to score job listings.

## Requirements
- Read `docs/backlog/036-market-research-career-role-matching.md` section "What I Built (Matching Profile)"
- Read `docs/backlog/029-market-research-ai-harness-engineering-jobs.md` for additional portfolio evidence
- Write `projects/career-role-matching/profile.json` with fields:
  - `skills`: array of skill objects with name and strength (1-5)
  - `domains`: array of domain expertise areas
  - `differentiators`: array of unique selling points
  - `tier_definitions`: the 3 tiers with salary ranges and role descriptions
  - `preferences`: remote, relocation, location constraints

## Acceptance Criteria
- [ ] `projects/career-role-matching/profile.json` exists and is valid JSON

## Gates
BUILD-02, FUNC-01
