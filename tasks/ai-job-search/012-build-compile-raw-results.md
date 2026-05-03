# Compile Raw Search Results

## Context
Merge all per-company raw result files into a single compiled results JSON. This creates a unified dataset for scoring.

## Type
BUILD

## Execution
inline

## Dependencies
- 002 through 011 (all company search tasks)

## Phase Gate
- [ ] `tasks/ai-job-search/output/raw-results/anthropic.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/openai.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/google-deepmind.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/meta-ai.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/xai.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/cohere.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/mistral.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/databricks.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/scale-ai.json` exists
- [ ] `tasks/ai-job-search/output/raw-results/hugging-face.json` exists

## Requirements
- Read all 10 raw result files from `tasks/ai-job-search/output/raw-results/`
- Merge all `jobs` arrays into a single `compiled-results.json`
- Add `company` field to each job if not already present
- Deduplicate by URL
- Write to `tasks/ai-job-search/output/compiled-results.json`

## Acceptance Criteria
- [ ] `tasks/ai-job-search/output/compiled-results.json` exists
- [ ] JSON is valid and contains a `jobs` array
- [ ] All jobs have a `company` field
- [ ] No duplicate URLs

## Gates Satisfied
- BUILD-14

## Completion Signal
When ALL acceptance criteria are met, proceed to next task.
