# Scroll Animations

## Status
NEW

## Location
`isagawa-portfolio-site-v2/` — all sections

## What It Does
IntersectionObserver-based reveal animations that trigger as sections enter the viewport. Transforms the page from static to alive without any scroll-jacking or libraries.

## Animation Types

### Section Reveals
- Each anchor section (seed, growth, self-extension, this page) fades in and slides up 30-40px on viewport entry
- Trigger at 15-20% intersection threshold
- Duration: 600-800ms ease-out
- Section numbers can have a separate, slightly earlier reveal

### Card Stagger
- Evidence cards animate in one-by-one with 100-150ms delay between each
- Same fade-up pattern but staggered via CSS transition-delay
- Cards start with opacity: 0 and transform: translateY(20px)

### Narrative Text
- Paragraphs with .anchor-section__narrative fade in after the title
- Subtle, 400ms duration

### Chain List
- List items reveal one-by-one, top to bottom, 80ms stagger
- Last item (This Page) gets a slight emphasis (longer pause before, slightly different easing)

### Provenance Cards
- Same stagger pattern as evidence cards

## Implementation
- Single JS module: `scroll-observer.js`
- CSS class `.reveal` on elements that should animate
- CSS class `.revealed` added by JS when intersection fires
- All animation defined in CSS (transforms + opacity transitions)
- Observer disconnects after all elements revealed (performance)
- `prefers-reduced-motion` media query disables all animations

## Mobile Behavior
- Same animations, possibly reduced translateY distance (20px instead of 40px)
- Stagger delays can be slightly shorter on mobile
