# 004 — Write qa-platforms.css

**Type:** BUILD
**Depends on:** 002

## Goal
Write the CSS file for the QA platforms showcase page at `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.css`.

## Requirements

- Use the same CSS custom properties (`:root` vars) as attestation.css: colors, fonts, spacing, card styles
- Reuse existing component patterns: `.site-header`, `.nav`, `.hero`, `.page-section`, `.flow-grid`, `.flow-card`, `.evidence-grid`, `.evidence-card`, `.badges`, `.results-grid`, `.cta`, `footer`
- Add new styles for:
  - `.architecture-diagram` — 4-layer visual with connecting lines
  - `.platform-grid` — 5-column card grid for platforms (responsive: 2-col tablet, 1-col mobile)
  - `.platform-card` — card with platform name, stack badge, description, GitHub link
  - `.terminal` — animated terminal for demo section (match ssh-compliance terminal style)
  - `.layer-card` — architecture layer cards with layer number and responsibility
- Mobile responsive: match existing breakpoints (768px for mobile)
- STIX Two Text + Inter fonts (same as ssh-compliance page)

Reference: `D:\my_ai_projects\isagawa-co.github.io\attestation.css` for all shared patterns

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.css` exists with `:root` variables and all component styles
