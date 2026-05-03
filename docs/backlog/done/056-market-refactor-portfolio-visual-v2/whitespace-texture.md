# Compositional Whitespace and Visual Texture

## Status
NEW

## Whitespace
- Anchor section vertical padding: `clamp(8rem, 18vh, 18rem)`
- Narrative paragraphs: `max-width: 65ch`
- Hero CTA margin-bottom: `clamp(4rem, 8vh, 8rem)` before section 01

## Visual Texture

### Body background
- Radial gradient from `rgb(10, 10, 14)` center-top to `rgb(0, 0, 0)` edges

### Grain overlay
- Inline SVG `feTurbulence` pseudo-element
- Opacity: `0.025`
- Position: fixed
- Pointer-events: none
