# Build Responsive Cards

## Context
All card grids (kernel, catalog, platforms, output types) need responsive media queries so they reflow correctly on smaller screens. Without these, cards will overflow or be cut off.

## Type
BUILD

## Execution
inline

## Dependencies
- 061-build-responsive-hero

## Requirements
- Add media queries for all card grid sections: kernel, catalog, platforms, output types
- Tablet (`max-width: 1024px`): cards display in 2-column grid
- Mobile (`max-width: 768px`): cards stack in single column
- Maintain consistent card spacing at each breakpoint

## Acceptance Criteria
- [ ] Card grids switch to 2-column layout at tablet breakpoint
- [ ] Card grids switch to 1-column stacked layout at mobile breakpoint
- [ ] All four card sections (kernel, catalog, platforms, output types) have responsive rules
- [ ] Card spacing and padding adjust proportionally

## Gates Satisfied
None (intermediate build task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
