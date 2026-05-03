# 013 — Compile Raw Results

## Type
BUILD

## Description
Merge all raw search results from `projects/career-role-matching/raw/*.json` into a single compiled listings file.

## Requirements
- Read all JSON files in `projects/career-role-matching/raw/`
- Merge into a single array, adding a `source` field to each entry (linkedin, wellfound, yc, etc.)
- Deduplicate by URL
- Normalize fields: ensure every entry has url, company, title, location, remote, tier
- Write to `projects/career-role-matching/compiled-listings.json`

## Acceptance Criteria
- [ ] `projects/career-role-matching/compiled-listings.json` exists and is valid JSON

## Gates
BUILD-04, FUNC-02, FUNC-05
