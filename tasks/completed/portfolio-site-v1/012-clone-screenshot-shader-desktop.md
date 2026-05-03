# Screenshot Shader Development Studio — Desktop

## Context
Capture a desktop-width reference screenshot of Shader Development Studio for visual QA comparison of the skin/aesthetic.

## Type
BUILD

## Execution
inline

## Dependencies
- 011-clone-navigate-shader.md

## Requirements
- Use `browser_resize` with `{ "width": 1440, "height": 900 }`
- Use `browser_take_screenshot` to capture the viewport
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 2

## Acceptance Criteria
- [ ] Desktop screenshot captured at 1440x900 viewport

## Gates Satisfied
CLONE-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
