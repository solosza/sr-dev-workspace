# Build CSS Hero Section

## Context
Adds hero section styles to styles.css. The hero must feel like a terminal/code aesthetic with full viewport presence.

## Type
BUILD

## Execution
inline

## Dependencies
- 033

## Requirements
- Add hero section CSS rules to styles.css
- Full viewport height: `min-height: 100vh`
- Content centered both vertically and horizontally (flexbox)
- Headline styled with `var(--text-hero)` font size or equivalent design token
- Subheadline and supporting line styled with appropriate hierarchy
- CTA button styling: visible, clickable, uses design token variables for colors
- Terminal/code feel through typography and spacing choices
- All values must use CSS custom property variables (design tokens) — no hardcoded colors or sizes

## Acceptance Criteria
- [ ] Hero section has min-height: 100vh
- [ ] Content is centered vertically and horizontally
- [ ] Headline, subheadline, supporting line have distinct visual hierarchy
- [ ] CTA button is styled as a prominent interactive element
- [ ] All color and size values reference CSS custom properties

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
