# Build CSS Typography Variables

## Context
Reads the extracted typography data and appends font family and type scale tokens to the existing `:root` block in `styles.css`. These tokens control all text rendering across the site.

## Type
BUILD

## Execution
inline

## Dependencies
- 022 (color variables written to styles.css)

## Requirements
- Read `D:\my_ai_projects\isagawa-portfolio-site\extraction\shader-typography.json`
- Append typography tokens inside the existing `:root` block in `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Font family tokens:
  - `--font-heading` — heading font stack
  - `--font-body` — body text font stack
  - `--font-mono` — monospace/code font stack
- Type scale tokens:
  - `--text-xs` — smallest text size
  - `--text-sm` — small text size
  - `--text-base` — base/body text size
  - `--text-lg` — large text size
  - `--text-xl` — extra large text size
  - `--text-2xl` — section heading size
  - `--text-3xl` — page heading size
  - `--text-hero` — hero/display text size
- Values must be derived from the extraction JSON

## Acceptance Criteria
- [ ] `:root` block contains all 3 font family tokens
- [ ] `:root` block contains all 8 type scale tokens
- [ ] Token values are sourced from the extraction data
- [ ] Existing color tokens in `:root` are preserved

## Gates Satisfied
BUILD-16

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
