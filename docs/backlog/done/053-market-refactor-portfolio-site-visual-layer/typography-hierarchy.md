# Typography Hierarchy

## Status
NEW

## Location
`D:\my_ai_projects\isagawa-portfolio-site\styles.css`

## Changes

### Hero h1
- `font-size: clamp(4rem, 9vw, 8rem)`
- `font-weight: 700`
- `letter-spacing: -0.04em`
- `line-height: 0.95`
- Linear gradient text: `#fcf9f3` to `#dcdce8` via `background: linear-gradient(...)`, `background-clip: text`, `color: transparent`

### Hero h2
- `font-size: clamp(1.25rem, 2vw, 1.5rem)`
- `font-weight: 400`
- `color: var(--text-secondary)`
- `max-width: 50ch`

### Hero p
- Add `max-width: 55ch`

### Section h2 titles (.anchor-section__title)
- `font-size: clamp(2.75rem, 5.5vw, 5rem)`
- `font-weight: 600`
- `letter-spacing: -0.025em`
- `line-height: 1.0`

### Card h3 titles (.evidence-card h3)
- `font-size: clamp(1.125rem, 2vw, 1.5rem)`
- `font-weight: 600`
- `letter-spacing: -0.01em`

### Body
- `line-height: 1.6` to `1.7`

### .reveal-text
- Bump to at least section h2 size: `clamp(2.75rem, 5.5vw, 5rem)`, weight 600

### Media query cleanup
- Remove `@media (max-width: 1400px) { #hero h1 { font-size: 2.5rem; } }`
- Remove `@media (max-width: 767px) { #hero h1 { font-size: 2rem; } }`
- Remove `@media (max-width: 479px) { .anchor-section__title { font-size: var(--text-2xl); } }`
- clamp() handles all responsive sizing
