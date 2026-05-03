# Screenshot Shader Development Studio — Mobile

## Context
Capture a mobile-width reference screenshot of Shader Development Studio for responsive aesthetic QA.

## Type
BUILD

## Execution
inline

## Dependencies
- 012-clone-screenshot-shader-desktop.md

## Requirements
- Use `browser_resize` with `{ "width": 375, "height": 812 }`
- Use `browser_take_screenshot` to capture the mobile viewport
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 2

## Acceptance Criteria
- [ ] Mobile screenshot captured at 375x812 viewport

## Gates Satisfied
CLONE-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
