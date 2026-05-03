# L2: Visual QA — Mobile

## Context
Level 2 functional test. Open the site in Playwright at mobile resolution, verify responsive layout works, hamburger menu is visible, and cards stack vertically.

## Type
TEST

## Execution
agent

## Dependencies
- 022-test-l2-visual-qa-desktop

## Phase Gate
- [ ] Desktop visual QA passed

## Requirements
- Use Playwright MCP to:
  1. Navigate to `file:///D:/my_ai_projects/isagawa-portfolio-site/index.html`
  2. Set viewport to 375x812 (iPhone viewport)
  3. Take a full-page screenshot
  4. Verify:
     - Hamburger menu button is visible
     - Nav links are hidden (or in mobile menu)
     - Hero text is readable (not overflowing)
     - Evidence cards are single-column
     - Attestation cards are stacked vertically
  5. Click hamburger button, verify nav links appear
  6. Take screenshot with menu open

## Acceptance Criteria
- [ ] Screenshot captured at 375x812
- [ ] Hamburger button visible in mobile view
- [ ] Cards display in single column
- [ ] Menu toggle works (nav links appear on click)

## Gates Satisfied
- TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
