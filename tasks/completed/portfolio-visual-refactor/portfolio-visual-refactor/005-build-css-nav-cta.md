# CSS Nav + Hero CTA Styles

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
styles.css

## Acceptance Criteria
1. Nav logo: `letter-spacing: 0.2em` (was 0.15em)
2. Nav link underline hover: `.nav__links a` gets `position: relative`, `.nav__links a::after` pseudo-element with `content: ''`, `position: absolute`, `bottom: -2px`, `left: 50%`, `width: 0`, `height: 1px`, `background: var(--accent)`, `transition: width 250ms ease, left 250ms ease`. On hover: `width: 100%`, `left: 0`
3. Hero CTA: `padding: 0.875rem 1.75rem`
4. Hero arrow rotation: `.hero__arrow` gets `display: inline-block`, `transition: transform 200ms ease`. On `.hero__cta:hover .hero__arrow`: `transform: rotate(-45deg)`
5. Scroll caption: `.hero__scroll-hint` with `display: block`, `font-family: var(--font-mono)`, `font-size: var(--text-xs)`, `color: var(--text-secondary)`, `letter-spacing: 0.1em`, `margin-top: var(--space-md)`

## Gates
CSS-13

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/navigation.md
docs/backlog/053-market-refactor-portfolio-site-visual-layer/hero-cta.md
