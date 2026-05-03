# CSS Chain List + Provenance + Badge Pulse

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
styles.css

## Acceptance Criteria
1. Chain list items: `line-height: 2.4`, adequate vertical padding
2. Chain list last-child already styled with --accent; confirm weight 600
3. Add `.chain-climax` class: `font-size: clamp(1.75rem, 3.5vw, 2.75rem)`, `font-weight: 600`, `color: var(--text-primary)`, `margin-top: clamp(4rem, 8vh, 7rem)`, `text-align: center`
4. Provenance subtitle: `font-size: clamp(1.125rem, 2vw, 1.375rem)`, `max-width: 60ch`
5. Attestation grid: `grid-template-columns: repeat(3, 1fr)` on desktop (was 2)
6. Badge pulse: `@keyframes badge-pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }` and apply to `.verification-badge--verified`

## Gates
CSS-11, CSS-12, CSS-17

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/chain-list.md
docs/backlog/053-market-refactor-portfolio-site-visual-layer/provenance-upgrade.md
