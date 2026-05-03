# Build Responsive Diagrams

## Context
The architecture diagram, pipeline visual, and flywheel loop are horizontal layouts that break on narrow screens. They need to reflow to vertical on mobile.

## Type
BUILD

## Execution
inline

## Dependencies
- 063-build-responsive-catalog

## Requirements
- Add media queries for architecture diagram section
- Add media queries for pipeline visual
- Add media queries for flywheel/loop diagram
- Horizontal flows become vertical on mobile (`max-width: 768px`)
- Maintain readability of arrows/connectors in vertical layout

## Acceptance Criteria
- [ ] Architecture diagram reflows to vertical layout on mobile
- [ ] Pipeline visual reflows to vertical layout on mobile
- [ ] Flywheel/loop diagram reflows to vertical layout on mobile
- [ ] No horizontal scrolling required at any breakpoint
- [ ] Diagram labels and connectors remain legible

## Gates Satisfied
None (intermediate build task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
