# 002 — Read Master Resume and Extract Matching Profile

**Type:** RESEARCH
**Depends on:** 001

## Goal

Read the master AI agent architect resume and extract the key skills, systems built, and differentiators that will be used as matching criteria for job scoring in tasks 003-006.

## Requirements

- Read `D:\my_python_projects\resume-ai-pipeline\resumes\ai-agent-architect-resume.md`
- Extract: key technical skills, systems built (Isagawa Kernel, spec factory, pipelines), unique differentiators
- Extract: preferred job titles and what makes a strong match vs weak match
- Write a concise profile summary to `projects/ai-harness-job-search/profile-summary.md` for use by later tasks

## Acceptance Criteria

- [ ] Master resume file read successfully
- [ ] `projects/ai-harness-job-search/profile-summary.md` exists
- [ ] Profile summary includes: technical skills list, top systems built, match criteria (strong/weak), preferred titles
