# Build CSS Architecture Section

## Context
Adds architecture section styles to styles.css covering the flow diagram and output type cards.

## Type
BUILD

## Execution
inline

## Dependencies
- 036

## Requirements
- Add architecture section CSS rules to styles.css
- Diagram layout: vertical flexbox flow for main nodes (KERNEL → FACTORY → AGENTS)
- Node styling: bordered boxes with design token colors
- Connecting lines/arrows between nodes (CSS borders or pseudo-elements)
- Branch layout: horizontal flexbox for the 6 vertical branches
- Card grid: 3-column layout for output type cards
- Output type badge colors using design tokens (distinct color for BUILD, WORKSPACE, OPERATE)
- Responsive: cards stack on mobile

## Acceptance Criteria
- [ ] Diagram nodes styled with borders and spacing
- [ ] Visual connectors exist between diagram levels
- [ ] Six branches display in a horizontal row on desktop
- [ ] Output type cards in 3-column grid on desktop
- [ ] Cards stack to single column on mobile
- [ ] All colors reference CSS custom properties

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
