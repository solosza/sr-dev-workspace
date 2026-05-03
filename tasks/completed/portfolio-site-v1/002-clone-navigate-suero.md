# Navigate to Suero Studio Homepage

## Context
Suero Studio (ethansuero.com) is the structure source for the portfolio site clone. This task loads the page and confirms it renders before any extraction begins.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-output-dir.md

## Requirements
- Use `browser_navigate` with URL `https://ethansuero.com`
- Use `browser_wait_for` with selector `main` (or `body`), state `visible`, timeout `10000`
- Use `browser_snapshot` to confirm page content is present
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 1

## Acceptance Criteria
- [ ] Page loaded successfully — `browser_snapshot` returns content with visible headings/sections

## Gates Satisfied
CLONE-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
