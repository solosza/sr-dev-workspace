# Screenshot Suero Studio — Desktop

## Context
Capture a desktop-width reference screenshot of Suero Studio for later QA comparison against the rebuilt site.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-clone-navigate-suero.md

## Requirements
- Use `browser_resize` with `{ "width": 1440, "height": 900 }`
- Use `browser_take_screenshot` to capture the viewport
- The screenshot serves as the desktop reference for Suero's structure
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 2

## Acceptance Criteria
- [ ] Desktop screenshot captured at 1440x900 viewport

## Gates Satisfied
CLONE-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
