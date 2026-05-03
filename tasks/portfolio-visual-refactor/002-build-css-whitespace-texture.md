# CSS Whitespace + Visual Texture

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
styles.css

## Acceptance Criteria
1. Anchor section padding: `padding: clamp(8rem, 18vh, 18rem) var(--space-md)`
2. Narrative paragraphs: `max-width: 65ch` (was 60ch)
3. Hero CTA: add `margin-bottom: clamp(4rem, 8vh, 8rem)`
4. Body background: `background: radial-gradient(ellipse at 50% 0%, rgb(10, 10, 14) 0%, rgb(0, 0, 0) 70%)`
5. Grain overlay: `body::before` pseudo-element with inline SVG feTurbulence, `opacity: 0.025`, `position: fixed`, `pointer-events: none`, `z-index: 9999`, covering full viewport

## Gates
CSS-06, CSS-07, CSS-08

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/whitespace.md
docs/backlog/053-market-refactor-portfolio-site-visual-layer/visual-texture.md
