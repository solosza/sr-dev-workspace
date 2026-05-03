# Navigate to Shader Development Studio Homepage

## Context
Shader Development Studio (shader.se) is the skin/aesthetic source for the portfolio site clone. This task loads the page and confirms it renders before visual extraction begins.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-output-dir.md

## Requirements
- Use `browser_navigate` with URL `https://shader.se`
- Use `browser_wait_for` with selector `main` (or `body`), state `visible`, timeout `10000`
- Use `browser_snapshot` to confirm page content is present
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 1

## Acceptance Criteria
- [ ] Page loaded successfully — `browser_snapshot` returns content with visible elements

## Gates Satisfied
CLONE-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
