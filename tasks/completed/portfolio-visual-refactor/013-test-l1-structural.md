# L1 Structural Verification

## Type
TEST

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## Acceptance Criteria
Grep-verify all CSS and HTML gates from gate-contract.md:

### CSS checks (styles.css)
1. `clamp(4rem, 9vw, 8rem)` present (hero h1)
2. `background-clip: text` present (hero gradient)
3. `clamp(2.75rem, 5.5vw, 5rem)` present (section h2)
4. `line-height: 1.7` in body
5. `clamp(5rem, 12vw, 11rem)` present (anchor numbers)
6. `clamp(8rem, 18vh, 18rem)` present (section padding)
7. `radial-gradient` in body
8. `feTurbulence` in body::before
9. `translateY(-2px)` present (card hover)
10. `.card-tags` rule present
11. `line-height: 2.4` in chain list
12. `badge-pulse` keyframes present
13. `.nav__links a::after` present
14. `.footer__grid` present
15. No `2.5rem` in 1400px media query (conflicting override removed)
16. `.anchor-section__narrative strong` present
17. `.chain-climax` present

### HTML checks (index.html)
1. No `—` in copy outside script tags
2. `<strong>natural language</strong>` present
3. `GOVERNANCE / PROTOCOL / TOKEN` present
4. `GOVERNED` in evidence-stat
5. `122` in evidence-stat
6. `href="#this-page"` in nav
7. `hero__arrow` present
8. `OR SCROLL` present
9. `footer__grid` present
10. `attestation-bundle-3` present

## Gates
CSS-01 through CSS-17, HTML-01 through HTML-12
