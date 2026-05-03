# Update Nav and Footer CSS

## Context
The nav links changed from Kernel/Factory/Catalog/Platforms to Seed/Growth/Self-Extension/Provenance. The footer needs styling. Update both in one pass since they're related layout elements.

## Type
BUILD

## Execution
inline

## Dependencies
- 015-build-html-footer

## Phase Gate
- [ ] Footer HTML written in `index.html`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Add/update nav styles:
  - `.site-header` — fixed top, bg-primary with slight opacity, z-index high
  - `.nav` — flex layout, space-between, padding
  - `.nav__logo` — ISAGAWA wordmark, font-heading, accent color, letter-spacing
  - `.nav__links` — flex list, gap, no list-style
  - `.nav__links a` — text-secondary, hover accent, transition
  - `.nav__hamburger` — hidden on desktop, visible on mobile
  - `.nav__hamburger-line` — three lines for hamburger icon
- Add footer styles:
  - `footer` — padding, border-top subtle, text-center
  - `.footer__tagline` — text-secondary, mono font, small
  - `.footer__links` — flex row, gap
  - `.footer__copyright` — text-xs, muted

## Acceptance Criteria
- [ ] `styles.css` contains `.nav__logo` styles
- [ ] `styles.css` contains `footer` styles
- [ ] `styles.css` contains `.nav__hamburger` styles

## Gates Satisfied
- BUILD-02, BUILD-17 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
