# Task 009: Create step-ab-2-build-prompt.md

## Action
Create `.claude/skills/eval/steps/step-ab-2-build-prompt.md`.

## Content
Step file for A/B mode — builds the task prompt that will be run against both variants.

Include:
- Input table (artifact content, config with optional task_prompt)
- Two modes: provided prompt (use directly) or auto-generated (LLM analyzes artifact)
- Auto-generation template: read artifact, produce realistic task exercising 3+ steps
- Output: task_prompt string + optional golden expected output description
- Verification: prompt is non-empty, exercises the artifact's workflow

## Acceptance Criteria
- File exists at `.claude/skills/eval/steps/step-ab-2-build-prompt.md`
- Documents both provided and auto-generated prompt modes
- Under 100 lines
