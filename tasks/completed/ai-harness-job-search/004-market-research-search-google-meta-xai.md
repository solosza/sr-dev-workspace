# 004 — Search Google DeepMind, Meta AI, and xAI for Matching Roles

**Type:** RESEARCH
**Depends on:** 002

## Goal

Search Google DeepMind, Meta AI, and xAI career pages for roles matching the AI agent/harness/infrastructure profile. These are priority targets — relocation considered for Google DeepMind.

## Requirements

- Search Google DeepMind / Google AI careers for: agent infrastructure, developer tools, AI platform, evaluation, safety infrastructure, research engineering roles
- Search Meta AI careers (metacareers.com) for the same role categories
- Search xAI careers for agent/infra/platform roles
- For each matching role found:
  - Record: company, title, location, remote status, URL, brief description
  - Assign preliminary match score (1-10) based on profile from task 002
  - Note strong vs partial match criteria
- Target: NOT QA, NOT data annotation — agent platform, harness, infra, DX, evals only
- Write findings to `projects/ai-harness-job-search/runs/[date]-google-meta-xai.md`

## Acceptance Criteria

- [ ] Google DeepMind / Google AI careers searched and results recorded
- [ ] Meta AI careers searched and results recorded
- [ ] xAI careers searched and results recorded
- [ ] Output file `projects/ai-harness-job-search/runs/[date]-google-meta-xai.md` exists
- [ ] Each job entry has: company, title, location, remote status, URL, match score (1-10), match notes
- [ ] No QA or annotation roles included
