# 005 — Search Other AI Companies for Matching Roles

**Type:** RESEARCH
**Depends on:** 002

## Goal

Search the remaining target companies — Cohere, Mistral, Databricks, Scale AI, Hugging Face, and any other AI infrastructure companies with agent/harness/evaluation teams — for matching roles.

## Requirements

- Search Cohere careers for agent infrastructure, developer tools, evaluation, platform engineering roles
- Search Mistral AI careers for same categories
- Search Databricks careers for AI platform / agent infrastructure / MLOps engineering roles
- Search Scale AI careers for agent evaluation, infrastructure, developer tools roles (NOT labeling/annotation)
- Search Hugging Face careers for developer tools, platform, agent infrastructure roles
- Also search: Weights & Biases, LangChain/LangSmith, Letta (MemGPT), Modal, Replicate — any company building AI agent infrastructure
- For each matching role found:
  - Record: company, title, location, remote status, URL, brief description
  - Assign preliminary match score (1-10) based on profile from task 002
  - Note strong vs partial match criteria
- Write findings to `projects/ai-harness-job-search/runs/[date]-other-companies.md`

## Acceptance Criteria

- [ ] Cohere, Mistral, Databricks, Scale AI, Hugging Face careers searched and results recorded
- [ ] At least 2 additional AI infrastructure companies searched beyond the main list
- [ ] Output file `projects/ai-harness-job-search/runs/[date]-other-companies.md` exists
- [ ] Each job entry has: company, title, location, remote status, URL, match score (1-10), match notes
- [ ] No data labeling, annotation, or generic QA roles included
