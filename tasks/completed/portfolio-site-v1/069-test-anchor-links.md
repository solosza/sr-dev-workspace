# Test Anchor Links

## Context
Verifies that all navigation anchor links scroll to the correct section. Smooth scroll behavior should be active and each link must land on its target section.

## Type
TEST

## Execution
inline

## Dependencies
- 068-test-visual-qa-mobile

## Requirements
- Use Playwright MCP: reset viewport to desktop (1440x900)
- Click each nav link one at a time
- After each click, use `browser_snapshot` to verify the target section is visible
- Test all nav links: Architecture, Kernel, Factory, Catalog, Platforms, Loop, CTA
- Verify smooth scroll behavior is active (no jarring jumps)

## Acceptance Criteria
- [ ] Clicking "Architecture" nav link scrolls to architecture section
- [ ] Clicking "Kernel" nav link scrolls to kernel section
- [ ] Clicking "Factory" nav link scrolls to factory section
- [ ] Clicking "Catalog" nav link scrolls to catalog section
- [ ] Clicking "Platforms" nav link scrolls to platforms section
- [ ] Clicking "Loop" nav link scrolls to loop section
- [ ] Clicking "CTA" nav link scrolls to CTA section
- [ ] Each target section is confirmed visible via browser_snapshot

## Gates Satisfied
TEST-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
