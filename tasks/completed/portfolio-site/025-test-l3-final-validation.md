# L3: Final Validation

## Context
Level 3 production test. Full end-to-end validation of the portfolio site. Scroll through the entire page, verify the narrative flow matches the 4 anchor moments, check the 90-second test criteria, and produce a validation report.

## Type
TEST

## Execution
agent

## Dependencies
- 022-test-l2-visual-qa-desktop
- 023-test-l2-visual-qa-mobile
- 024-test-l3-provenance-display

## Phase Gate
- [ ] Desktop and mobile visual QA passed
- [ ] Provenance display verification passed

## Requirements
- Use Playwright MCP to:
  1. Navigate to `file:///D:/my_ai_projects/isagawa-portfolio-site/index.html` at 1440x900
  2. Verify narrative flow by scrolling through each section in order:
     - Hero: "conversational agent factory" visible
     - Seed: "The Seed" heading, 4 evidence cards (kernel mechanisms)
     - Growth: "Growth" heading, 3 evidence cards, "27+" stat visible
     - Self-Extension: "Self-Extension" heading, 3 evidence cards
     - This Page: "This Page" heading, 8-step chain list, punchline visible
     - Provenance: 2 attestation cards with intent text
     - Footer: "Built by the system it describes"
  3. Click each nav link, verify it scrolls to the correct section
  4. Check console for any errors throughout the scroll
  5. Verify dark terminal aesthetic (background is black/near-black, text is warm off-white)
- Produce validation report at `tasks/portfolio-site/_test/validation-report.json`

## Acceptance Criteria
- [ ] All 7 sections render in correct order
- [ ] Nav links scroll to correct sections (4 nav links, all resolve)
- [ ] No JavaScript errors in console
- [ ] Dark theme confirmed (black background)
- [ ] Validation report written to `_test/validation-report.json`

## Gates Satisfied
- FUNC-01, FUNC-02 (full sweep)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
