# Build CSS Component Tokens

## Context
Derives button and card component tokens from the existing color and spacing primitives, then appends them to the `:root` block. These semantic tokens map primitive values to component-level concerns, enabling consistent button and card styling.

## Type
BUILD

## Execution
inline

## Dependencies
- 024 (spacing variables appended to styles.css)

## Requirements
- Derive button tokens from existing color and spacing tokens and append to `:root` in `D:\my_ai_projects\isagawa-portfolio-site\styles.css`:
  - `--btn-bg` — button background (derived from accent)
  - `--btn-text` — button text color (derived from text-primary or bg-primary for contrast)
  - `--btn-radius` — button border radius
  - `--btn-padding` — button padding (derived from spacing tokens)
- Derive card tokens from existing color and spacing tokens and append to `:root`:
  - `--card-bg` — card background (derived from bg-surface)
  - `--card-border` — card border color (derived from border-subtle)
  - `--card-radius` — card border radius
  - `--card-padding` — card padding (derived from spacing tokens)
- Values should reference the extraction data where possible, using the already-defined primitive tokens as the source of truth

## Acceptance Criteria
- [ ] `:root` block contains all 4 button tokens (--btn-bg, --btn-text, --btn-radius, --btn-padding)
- [ ] `:root` block contains all 4 card tokens (--card-bg, --card-border, --card-radius, --card-padding)
- [ ] Existing primitive tokens in `:root` are preserved

## Gates Satisfied
BUILD-19

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
