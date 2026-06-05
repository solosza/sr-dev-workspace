# 003 — Search Anthropic and OpenAI for Matching Roles

**Type:** RESEARCH
**Depends on:** 002

## Goal

Search Anthropic and OpenAI career pages for roles matching the AI agent/harness/infrastructure profile. These are priority targets — relocation considered.

## Requirements

- Search Anthropic careers (anthropic.com/careers) for: agent infrastructure, developer tools, AI platform, evaluation, safety infrastructure roles
- Search OpenAI careers (openai.com/careers) for the same role categories
- For each matching role found:
  - Record: company, title, location, remote status, URL, brief description
  - Assign preliminary match score (1-10) based on profile from task 002
  - Note: strong match criteria (e.g., "infrastructure", "evaluation", "developer tools") vs partial match
- Target: NOT QA, NOT data annotation — agent platform, harness, infra, DX, evals only
- Write findings to `projects/ai-harness-job-search/runs/YYYY-MM-DD-anthropic-openai.md`

## Acceptance Criteria

- [ ] Anthropic careers page searched and results recorded
- [ ] OpenAI careers page searched and results recorded
- [ ] Output file `projects/ai-harness-job-search/runs/[date]-anthropic-openai.md` exists
- [ ] Each job entry has: company, title, location, remote status, URL, match score (1-10), match notes
- [ ] No QA or annotation roles included
