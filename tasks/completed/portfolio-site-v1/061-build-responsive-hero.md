# Build Responsive Hero

## Context
The hero section needs media queries to adapt at tablet and mobile breakpoints. Without responsive rules, the hero headline and padding will overflow or look disproportionate on smaller screens.

## Type
BUILD

## Execution
inline

## Dependencies
- 060-build-css-nav

## Requirements
- Add media query at `max-width: 1024px` (tablet) for hero section
- Add media query at `max-width: 768px` (mobile) for hero section
- Reduce headline font size at each breakpoint
- Adjust hero padding to fit smaller viewports
- Maintain visual hierarchy at all sizes

## Acceptance Criteria
- [ ] `styles.css` contains `@media (max-width: 1024px)` rule targeting hero
- [ ] `styles.css` contains `@media (max-width: 768px)` rule targeting hero
- [ ] Hero headline font size decreases at tablet breakpoint
- [ ] Hero headline font size decreases further at mobile breakpoint
- [ ] Hero padding reduces at each breakpoint

## Gates Satisfied
None (intermediate build task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
