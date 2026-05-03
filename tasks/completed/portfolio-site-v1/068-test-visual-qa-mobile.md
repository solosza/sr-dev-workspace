# Test Visual QA — Mobile

## Context
Verifies the site renders correctly at mobile resolution. Single-column stacked layout and hamburger navigation must be present.

## Type
TEST

## Execution
inline

## Dependencies
- 067-test-visual-qa-tablet

## Requirements
- Use Playwright MCP: `browser_resize` to set viewport to 375x812
- Use `browser_take_screenshot` to capture full page
- Verify single-column stacked layout for all card sections
- Verify hamburger nav icon is visible (desktop nav hidden)
- Verify text remains readable and no overflow

## Acceptance Criteria
- [ ] Screenshot captured at 375x812 resolution
- [ ] All card sections display in single-column layout
- [ ] Hamburger navigation icon is visible
- [ ] Desktop nav links are hidden
- [ ] No horizontal overflow or text clipping

## Gates Satisfied
TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
