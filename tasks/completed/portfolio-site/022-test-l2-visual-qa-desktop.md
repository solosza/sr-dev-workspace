# L2: Visual QA — Desktop

## Context
Level 2 functional test. Open the site in Playwright at desktop resolution, verify it renders without errors, and take a screenshot for visual review.

## Type
TEST

## Execution
agent

## Dependencies
- 021-test-l1-verify-structure

## Phase Gate
- [ ] L1 structural tests passed

## Requirements
- Use Playwright MCP to:
  1. Navigate to `file:///D:/my_ai_projects/isagawa-portfolio-site/index.html`
  2. Set viewport to 1440x900
  3. Check console for JavaScript errors
  4. Take a full-page screenshot
  5. Verify visible elements:
     - Nav bar with ISAGAWA logo
     - Hero section with "conversational agent factory" text
     - At least one evidence-card visible
     - Dark background (black/near-black)
  6. Scroll to provenance section, verify attestation cards visible
  7. Take screenshot of provenance section

## Acceptance Criteria
- [ ] Page loads without JavaScript errors in console
- [ ] Screenshot captured at 1440x900
- [ ] Hero text visible in screenshot
- [ ] Provenance cards visible when scrolled

## Gates Satisfied
- FUNC-01, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
