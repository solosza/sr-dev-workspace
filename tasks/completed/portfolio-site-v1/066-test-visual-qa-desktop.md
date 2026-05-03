# Test Visual QA — Desktop

## Context
First visual QA checkpoint. Verifies the full site renders correctly at desktop resolution before testing responsive breakpoints.

## Type
TEST

## Execution
inline

## Dependencies
- 065-build-responsive-typography

## Requirements
- Use Playwright MCP: `browser_navigate` to `file:///D:/my_ai_projects/isagawa-portfolio-site/index.html`
- Use `browser_resize` to set viewport to 1440x900
- Use `browser_take_screenshot` to capture full page
- Visually verify all 9 sections are present and rendered: Hero, Architecture, Kernel, Factory, Catalog, Platforms, Loop, CTA, Footer
- Verify no layout breakage, overflow, or missing content

## Acceptance Criteria
- [ ] Playwright successfully navigates to the local HTML file
- [ ] Screenshot captured at 1440x900 resolution
- [ ] All 9 sections visible in screenshot
- [ ] No visual breakage or overflow detected
- [ ] Nav bar is visible and styled

## Gates Satisfied
TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
