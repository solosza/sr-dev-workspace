# Build CSS Catalog Section

## Context
Adds catalog section styles to styles.css covering vertical group headings, spec card grid, and type badges.

## Type
BUILD

## Execution
inline

## Dependencies
- 048

## Requirements
- Add catalog section CSS rules to styles.css
- Vertical group headings: distinct styling, spacing between groups
- Spec card grid:
  - 3-column on desktop
  - 2-column on tablet
  - 1-column on mobile
- Card styling consistent with kernel section cards (var(--card-bg), var(--card-border))
- Badge styling using design tokens:
  - BUILD badge: `var(--badge-build-bg)`
  - WORKSPACE badge: `var(--badge-workspace-bg)`
  - OPERATE badge: `var(--badge-operate-bg)`
- Badges should be small, inline, rounded pill elements

## Acceptance Criteria
- [ ] Spec cards display in 3-column grid on desktop
- [ ] Spec cards display in 2-column grid on tablet
- [ ] Spec cards stack to 1 column on mobile
- [ ] Badge backgrounds use var(--badge-build-bg), var(--badge-workspace-bg), var(--badge-operate-bg)
- [ ] Group headings have distinct styling and vertical spacing

## Gates Satisfied
BUILD-20

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
