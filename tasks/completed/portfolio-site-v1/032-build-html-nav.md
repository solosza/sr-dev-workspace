# Build HTML Navigation

## Context
Adds the sticky navigation header to index.html. This is the primary site navigation with logo and section links, plus a mobile hamburger button.

## Type
BUILD

## Execution
inline

## Dependencies
- 031

## Requirements
- Add a `<header>` element with a `<nav>` inside the body of index.html
- Logo text: "ISAGAWA" (plain text or styled span, not an image)
- Navigation links:
  - Kernel → `href="#kernel"`
  - Factory → `href="#factory"`
  - Catalog → `href="#catalog"`
  - Platforms → `href="#platforms"`
  - Contact → `href="#cta"`
- Mobile hamburger button element (hidden on desktop via CSS class)
- Hamburger button should have a class or data attribute for JS targeting

## Acceptance Criteria
- [ ] Header element exists as first child of body
- [ ] Nav element contains logo text "ISAGAWA"
- [ ] Five navigation links present with correct href values
- [ ] Mobile hamburger button element present with appropriate class
- [ ] Hamburger button is semantically a button element

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
