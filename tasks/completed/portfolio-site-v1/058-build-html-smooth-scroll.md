# Build HTML Smooth Scroll Script

## Context
Adds an inline JavaScript snippet for smooth scrolling behavior on all anchor links.

## Type
BUILD

## Execution
inline

## Dependencies
- 057

## Requirements
- Add an inline `<script>` tag at the bottom of the body in index.html (after footer)
- Script selects all anchor links with href starting with "#": `document.querySelectorAll('a[href^="#"]')`
- Each link gets a click event listener that:
  - Prevents default behavior
  - Gets the target element by the href attribute
  - Scrolls to the target using `scrollIntoView({ behavior: 'smooth' })`
- No external dependencies — vanilla JavaScript only

## Acceptance Criteria
- [ ] Inline script tag present at bottom of body
- [ ] Script targets all `a[href^="#"]` elements
- [ ] Click handler prevents default and scrolls smoothly to target
- [ ] No external JS libraries used

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
