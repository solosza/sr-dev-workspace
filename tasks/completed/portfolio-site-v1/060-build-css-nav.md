# Build CSS Navigation

## Context
Adds navigation styles to styles.css covering sticky header, desktop horizontal links, and mobile hamburger menu.

## Type
BUILD

## Execution
inline

## Dependencies
- 059

## Requirements
- Add navigation CSS rules to styles.css
- Sticky header:
  - `position: sticky`
  - `top: 0`
  - `z-index: 100`
  - Background color using design token (should not be transparent — content scrolls behind)
- Desktop layout:
  - Logo and links in horizontal row (flexbox)
  - Links styled inline with spacing
  - Hamburger button hidden (`display: none`)
- Mobile layout (media query):
  - Nav links hidden by default
  - Hamburger button visible
  - When `.nav-open` class is present on nav:
    - Links container becomes visible (e.g., `display: flex; flex-direction: column`)
    - Full-width dropdown or slide-in menu

## Acceptance Criteria
- [ ] Header is sticky with position: sticky, top: 0, z-index: 100
- [ ] Header has opaque background color
- [ ] Desktop: links display horizontally, hamburger hidden
- [ ] Mobile: links hidden by default, hamburger visible
- [ ] Mobile: `.nav-open` class reveals nav links in vertical layout

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
