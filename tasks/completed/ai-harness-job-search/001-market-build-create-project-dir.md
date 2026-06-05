# 001 — Create Project Directory

**Type:** BUILD
**Depends on:** —

## Goal

Create the `projects/ai-harness-job-search/` directory if it doesn't already exist. This is the accumulation point for all job search runs — multiple pipeline executions append results here.

## Requirements

- Create `projects/ai-harness-job-search/` if it doesn't exist
- Create a `runs/` subfolder inside it for dated run outputs
- Do NOT delete or overwrite existing files if the directory already exists (ongoing search)

## Acceptance Criteria

- [ ] `projects/ai-harness-job-search/` directory exists
- [ ] `projects/ai-harness-job-search/runs/` directory exists
