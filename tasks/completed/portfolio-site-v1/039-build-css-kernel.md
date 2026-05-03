# Build CSS Kernel Section

## Context
Adds kernel section styles to styles.css for the four governance mechanism cards.

## Type
BUILD

## Execution
inline

## Dependencies
- 038

## Requirements
- Add kernel section CSS rules to styles.css
- Card grid: 2x2 layout on desktop
- Card styling: use `var(--card-bg)` for background, `var(--card-border)` for borders
- Cards stack vertically on mobile (single column)
- Card heading and description have clear visual hierarchy
- Consistent padding and spacing using design tokens

## Acceptance Criteria
- [ ] Cards display in 2x2 grid on desktop
- [ ] Cards stack to single column on mobile
- [ ] Card background uses var(--card-bg)
- [ ] Card border uses var(--card-border)
- [ ] Spacing and padding reference design token variables

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
