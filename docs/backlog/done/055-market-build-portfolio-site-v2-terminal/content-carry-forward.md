# Content Carry-Forward from V1

## Status
NEW

## Location
`isagawa-portfolio-site-v2/` — all files

## What Carries Over (Pipeline 053 Visual Refactor)
Everything from v1 content and styling carries forward. V2 is a presentation layer upgrade, not a content rewrite.

### Typography (from styles.css)
- Hero h1: clamp(4rem, 9vw, 8rem), weight 700, gradient text
- Section h2: clamp(2.75rem, 5.5vw, 5rem), weight 600
- Card h3: clamp(1.125rem, 2vw, 1.5rem), weight 600
- Anchor numbers: clamp(5rem, 12vw, 11rem), 0.08 opacity
- Body line-height: 1.7

### Content (from index.html)
- All em dash replacements (14 instances, natural punctuation)
- Bold emphasis tags (strong) in all narratives
- Card tags (GOVERNANCE / PROTOCOL / TOKEN etc.)
- Stat numbers: GOVERNED, 122, 5
- Chain list with closing line
- Three attestation cards with embedded bundles (#050, #052, #047)
- Footer 4-column layout with Rekor links
- Nav with "This Page" link
- Hero CTA with arrow span + scroll caption

### Styles (from styles.css)
- All CSS custom properties (:root block)
- Card hover effects (translateY, border glow, box-shadow)
- Badge pulse animation
- Nav underline hover
- Radial gradient background + grain overlay
- Compositional whitespace (clamp padding)
- Provenance subtitle, 3-column grid
- Footer grid, responsive breakpoints

### What Changes in V2
- Hero section gets terminal component added
- All sections get `.reveal` class for scroll animations
- Section numbers get parallax behavior
- New JS modules: terminal typing, scroll observer, parallax
- CSS extended with animation keyframes and reveal states
