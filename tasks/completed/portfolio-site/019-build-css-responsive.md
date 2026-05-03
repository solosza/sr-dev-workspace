# Add Responsive CSS

## Context
All new sections need responsive rules. The existing breakpoint skeleton (1400px, 991px, 767px, 479px) is already in styles.css. Fill in the responsive rules for anchor sections, evidence grids, provenance cards, and the chain list.

## Type
BUILD

## Execution
inline

## Dependencies
- 018-build-js-mobile-nav

## Phase Gate
- [ ] All HTML sections and CSS written

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Fill in existing `@media` breakpoints:
  - **1400px:** reduce hero text size, constrain section max-width
  - **991px (tablet):** evidence-grid to single column, attestation cards stack vertically, reduce section padding
  - **767px (mobile):** evidence-grid single column, hero text smaller, chain-list compact, attestation cards full width, show hamburger menu, hide nav links (toggled by JS), nav links as vertical column when open
  - **479px (small mobile):** further reduce font sizes, tighter padding

## Acceptance Criteria
- [ ] `styles.css` has responsive rules at 991px breakpoint
- [ ] `styles.css` has responsive rules at 767px for `.evidence-grid`
- [ ] `styles.css` has responsive rules at 767px for `.attestation-cards`
- [ ] `styles.css` has responsive rules showing `.nav__hamburger` on mobile

## Gates Satisfied
- BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
