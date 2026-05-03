# Add Anchor Section Base Styles

## Context
With old section CSS removed, add base styles for the 4 anchor moment sections (seed, growth, self-extension, this-page). These are the narrative sections that tell the loop story. Each section needs consistent spacing, a section number label, and a content container.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-css-strip-old-sections

## Phase Gate
- [ ] `styles.css` has no `.kernel-card` classes (001 complete)

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Add CSS for `.anchor-section` — base styles shared by all 4 sections: padding, max-width container
- Add `.anchor-section__number` — monospace section number label (01, 02, 03, 04)
- Add `.anchor-section__title` — section heading
- Add `.anchor-section__content` — content area
- Add `.evidence-grid` — grid layout for evidence cards within sections (2-column on desktop, 1-column mobile)
- Add `.evidence-card` — card component for evidence items (reuse `--card-bg`, `--card-border`, `--card-radius` tokens)
- Use existing CSS custom properties from `:root` — do not add new variables unless absolutely necessary

## Acceptance Criteria
- [ ] `styles.css` contains `.anchor-section` class
- [ ] `styles.css` contains `.evidence-grid` class
- [ ] `styles.css` contains `.evidence-card` class
- [ ] All new styles use existing CSS custom properties (no hardcoded colors)

## Gates Satisfied
- (supports BUILD-04 through BUILD-07)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
