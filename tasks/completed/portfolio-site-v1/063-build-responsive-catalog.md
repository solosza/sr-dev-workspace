# Build Responsive Catalog

## Context
The catalog section contains vertical groups (IT, Healthcare, QA, DevOps, etc.) that need to stack on mobile. Badge positioning must also adapt to smaller card sizes.

## Type
BUILD

## Execution
inline

## Dependencies
- 062-build-responsive-cards

## Requirements
- Add media queries for catalog section vertical groups
- Mobile: vertical groups stack fully (no side-by-side layout)
- Reduce card size at mobile breakpoint
- Adjust badge positioning so badges remain visible and legible on smaller cards

## Acceptance Criteria
- [ ] Catalog vertical groups stack on mobile (`max-width: 768px`)
- [ ] Catalog card sizes reduce proportionally at mobile breakpoint
- [ ] Badge positioning adjusts to remain visible on smaller cards
- [ ] No horizontal overflow in catalog section at any breakpoint

## Gates Satisfied
None (intermediate build task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
