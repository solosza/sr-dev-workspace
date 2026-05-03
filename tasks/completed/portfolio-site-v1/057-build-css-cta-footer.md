# Build CSS CTA and Footer

## Context
Adds CTA section and footer styles to styles.css.

## Type
BUILD

## Execution
inline

## Dependencies
- 056

## Requirements
- Add CTA section CSS rules to styles.css:
  - Full-width section
  - Content centered
  - Prominent button/link styling for the email CTA
  - Social links styled inline
- Add footer CSS rules to styles.css:
  - Subtle background color (darker than main bg)
  - Small text size
  - Link columns or inline links
  - Attribution line styled subtly
- All values use design token variables

## Acceptance Criteria
- [ ] CTA section is full-width with centered content
- [ ] Email link/button has prominent styling
- [ ] Footer has subtle background distinct from main content
- [ ] Footer text is smaller than body text
- [ ] All colors and sizes reference CSS custom properties

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
