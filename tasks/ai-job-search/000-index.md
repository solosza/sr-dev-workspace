# AI Job Search — Task Index

## Goal
Research and compile AI agent infrastructure / harness engineering jobs at top companies, producing structured data with match scores ready for job-application-spec pipeline.

## Source
Backlog 029: `docs/backlog/029-market-research-ai-harness-engineering-jobs.md`

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-research-extract-resume-profile]] | RESEARCH | none | pending |
| 002 | [[002-research-search-anthropic]] | RESEARCH | 001 | pending |
| 003 | [[003-research-search-openai]] | RESEARCH | 001 | pending |
| 004 | [[004-research-search-google-deepmind]] | RESEARCH | 001 | pending |
| 005 | [[005-research-search-meta-ai]] | RESEARCH | 001 | pending |
| 006 | [[006-research-search-xai]] | RESEARCH | 001 | pending |
| 007 | [[007-research-search-cohere]] | RESEARCH | 001 | pending |
| 008 | [[008-research-search-mistral]] | RESEARCH | 001 | pending |
| 009 | [[009-research-search-databricks]] | RESEARCH | 001 | pending |
| 010 | [[010-research-search-scale-ai]] | RESEARCH | 001 | pending |
| 011 | [[011-research-search-hugging-face]] | RESEARCH | 001 | pending |
| 012 | [[012-build-compile-raw-results]] | BUILD | 002-011 | pending |
| 013 | [[013-build-score-jobs-against-profile]] | BUILD | 001, 012 | pending |
| 014 | [[014-build-write-final-output]] | BUILD | 013 | pending |

## Gate Contract
-> [[gate-contract.md]]

## Deliverables
- `output/job-search-results.json` — structured job listings with URLs, match scores, company, title, location, remote status
- `output/resume-profile.json` — extracted matching profile from resume
- `output/raw-results/` — per-company raw search results
