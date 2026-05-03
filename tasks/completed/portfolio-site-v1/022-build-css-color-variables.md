# Build CSS Color Variables

## Context
Reads the extracted color and surface data from Phase 1 and produces the foundational CSS custom properties for the design system. This is the first write to `styles.css` and establishes the `:root` block that all subsequent token tasks will append to.

## Type
BUILD

## Execution
inline

## Dependencies
- 021 (Phase 2 boundary verified)

## Requirements
- Read `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-colors.json`
- Read `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-surfaces.json`
- Reference `docs/backlog/041-market-build-portfolio-site/design-tokens.md` for token naming structure
- Write `D:\my_ai_projects\isagawa-portfolio-site\styles.css` with a `:root { }` block containing:
  - `--bg-primary` — main background color
  - `--bg-surface` — card/panel surface color
  - `--bg-elevated` — elevated surface (modals, dropdowns)
  - `--text-primary` — primary text color
  - `--text-secondary` — secondary/muted text color
  - `--text-accent` — accent-colored text
  - `--accent` — primary accent color
  - `--accent-hover` — accent hover state
  - `--accent-glow` — accent glow/shadow color
  - `--border-subtle` — subtle border color
  - `--border-strong` — strong/visible border color
- Values must be derived from the extraction JSON, not hardcoded

## Acceptance Criteria
- [ ] `styles.css` exists at `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- [ ] File contains a `:root` block
- [ ] All 11 color tokens are present as CSS custom properties
- [ ] Token values are sourced from the extraction data

## Gates Satisfied
BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
