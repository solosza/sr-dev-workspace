# Build CSS Factory Section

## Context
Adds factory section styles to styles.css covering the pipeline visual and throughput proof badges.

## Type
BUILD

## Execution
inline

## Dependencies
- 041

## Requirements
- Add factory section CSS rules to styles.css
- Pipeline layout: horizontal flexbox with stages in a row
- Stage boxes with consistent sizing and design token colors
- Arrows/connectors between stages (CSS borders, pseudo-elements, or arrow characters)
- Badge/pill styling for output types:
  - Rounded, inline elements
  - Distinct background colors for BUILD, WORKSPACE, OPERATE
- Pipeline wraps or scrolls horizontally on mobile
- Throughput line styled prominently

## Acceptance Criteria
- [ ] Pipeline stages display horizontally on desktop
- [ ] Visual connectors/arrows exist between stages
- [ ] Badges have rounded pill styling with distinct colors per type
- [ ] Layout is responsive — pipeline adapts on mobile
- [ ] All colors reference CSS custom properties

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
