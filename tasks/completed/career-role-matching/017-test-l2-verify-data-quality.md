# 017 — L2 Verify Data Quality and Format

## Type
TEST

## Description
Verify all JSON files are valid, have required fields, and contain no duplicates.

## Requirements
- Validate all JSON files parse correctly
- Verify `compiled-listings.json` entries each have: url, company, title, tier
- Verify `scored-rankings.json` entries each have: match_score (0-100)
- Verify no duplicate URLs in compiled-listings.json
- Verify report.md has all required sections (Executive Summary, Tier 1, Tier 2, Tier 3, Application Strategy)

## Acceptance Criteria
- [ ] All JSON files are valid
- [ ] Required fields present on every entry
- [ ] No duplicate URLs
- [ ] Report has all sections

## Gates
FUNC-01 through FUNC-05
