# Compositional Whitespace

## Status
EXISTS (needs enhancement)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\styles.css`

## Changes

### Anchor section vertical padding
- Current: `var(--space-xl)` (4rem)
- Target: `clamp(8rem, 18vh, 18rem)` top/bottom

### Narrative paragraphs
- Current: `max-width: 60ch`
- Target: `max-width: 65ch`

### Hero CTA spacing
- Add `margin-bottom: clamp(4rem, 8vh, 8rem)` to `.hero__cta` so there is deliberate space between the CTA and the start of section 01
