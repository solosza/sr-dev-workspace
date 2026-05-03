# Build HTML Mobile Nav Toggle Script

## Context
Adds an inline JavaScript snippet for the mobile hamburger menu toggle behavior.

## Type
BUILD

## Execution
inline

## Dependencies
- 058

## Requirements
- Add mobile nav toggle logic to the existing inline script (or a second script tag) in index.html
- Script targets the hamburger button element (by class or data attribute)
- On click, toggles a `.nav-open` class on the nav element
- When `.nav-open` is active, mobile menu links become visible (CSS handles the display)
- Clicking a nav link also closes the menu (removes `.nav-open`)

## Acceptance Criteria
- [ ] Hamburger button click toggles `.nav-open` class on nav element
- [ ] Nav link clicks remove `.nav-open` class (close menu after navigation)
- [ ] No external JS libraries used

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
