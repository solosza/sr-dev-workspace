# CSS Typography Hierarchy + Anchor Numbers

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
styles.css

## Acceptance Criteria
1. Hero h1: `font-size: clamp(4rem, 9vw, 8rem)`, `font-weight: 700`, `letter-spacing: -0.04em`, `line-height: 0.95`, linear gradient text from `#fcf9f3` to `#dcdce8` using `background: linear-gradient(...)`, `background-clip: text`, `-webkit-background-clip: text`, `color: transparent`
2. Hero h2: `font-size: clamp(1.25rem, 2vw, 1.5rem)`, `font-weight: 400`, `color: var(--text-secondary)`, `max-width: 50ch`
3. Hero p: add `max-width: 55ch`
4. Section h2 (.anchor-section__title): `font-size: clamp(2.75rem, 5.5vw, 5rem)`, `font-weight: 600`, `letter-spacing: -0.025em`, `line-height: 1.0`
5. Card h3 (.evidence-card h3): `font-size: clamp(1.125rem, 2vw, 1.5rem)`, `font-weight: 600`, `letter-spacing: -0.01em`
6. Body: `line-height: 1.7` (was 1.6)
7. .reveal-text: bump to `font-size: clamp(2.75rem, 5.5vw, 5rem)`, `font-weight: 600`
8. Anchor numbers (.anchor-section__number): `font-size: clamp(5rem, 12vw, 11rem)`, `font-weight: 700`, `font-family: var(--font-mono)`, `color: var(--text-primary)`, `opacity: 0.08`, `line-height: 0.85`, `margin-bottom: 0.5rem`
9. Remove `@media (max-width: 1400px)` hero h1 override (2.5rem)
10. Remove `@media (max-width: 767px)` hero h1 override (2rem)
11. Remove `@media (max-width: 479px)` anchor-section__title override

## Gates
CSS-01, CSS-02, CSS-03, CSS-04, CSS-05, CSS-15

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/typography-hierarchy.md
docs/backlog/053-market-refactor-portfolio-site-visual-layer/anchor-numbers.md
