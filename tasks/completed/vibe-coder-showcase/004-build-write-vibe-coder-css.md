# 004 — Write vibe-coder.css

## Type
BUILD

## Description
Write the CSS file for the Vibe Coder Pack showcase page. Must use the same design system as attestation.css (CSS custom properties, dark theme, STIX Two Text headings, SF Mono for code/labels).

## Requirements
- Copy the `:root` variables from `attestation.css` verbatim (colors, fonts, spacing, card styles)
- Include `html { background-color: rgb(0, 0, 0); }` to prevent white canvas on long pages
- Include all component classes used by vibe-coder.html (`.site-header`, `.nav`, `.hero`, `.page-section`, `.flow-grid`, `.flow-card`, `.evidence-grid`, `.evidence-card`, `.badges`, `.results-grid`, `.cta`, `footer`, etc.)
- Add comparison table styles (`.comparison-table` or similar) — dark cells, subtle borders, readable on dark background
- Mobile responsive (`@media max-width: 768px`)
- Terminal animation styles (`.demo-terminal`, `.terminal__bar`, `.terminal__body`, `.terminal__line`)

## Acceptance Criteria
- [ ] File exists at `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.css`
- [ ] `:root` block with CSS custom properties
- [ ] `html { background-color: rgb(0, 0, 0); }` present
- [ ] All component classes from HTML are styled
- [ ] Comparison table readable on dark background
- [ ] Mobile responsive breakpoint
