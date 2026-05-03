# 014 — Score and Rank Listings

## Type
BUILD

## Description
Score each job listing against the portfolio profile and produce ranked output.

## Requirements
- Read `projects/career-role-matching/profile.json` for matching criteria
- Read `projects/career-role-matching/compiled-listings.json` for all listings
- For each listing, compute a `match_score` (0-100) based on:
  - Skill alignment (weight: 40%)
  - Domain overlap (weight: 25%)
  - Compensation fit (weight: 15%)
  - Growth potential (weight: 10%)
  - Remote/location match (weight: 10%)
- Sort by match_score descending
- Write to `projects/career-role-matching/scored-rankings.json`

## Acceptance Criteria
- [ ] `projects/career-role-matching/scored-rankings.json` exists with scored entries

## Gates
BUILD-05, FUNC-03, FUNC-04
