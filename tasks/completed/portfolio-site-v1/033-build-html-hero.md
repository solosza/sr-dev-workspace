# Build HTML Hero Section

## Context
Adds the hero section to index.html. This is the first thing visitors see — the main value proposition of Isagawa.

## Type
BUILD

## Execution
inline

## Dependencies
- 032

## Requirements
- Add a `<section id="hero">` to index.html after the nav header
- Headline (h1): "The AI Management Layer"
- Subheadline (p or h2): "Manages AI agents across any domain — mechanically enforced, not advisory."
- Supporting line (p): "One kernel governs. One factory compiles. 27+ managed agents ship."
- CTA button: text "See the architecture", href="#architecture"
- Section should be structured for full viewport height (CSS will handle the sizing)

## Acceptance Criteria
- [ ] Section element exists with id="hero"
- [ ] H1 contains "The AI Management Layer"
- [ ] Subheadline text matches exactly: "Manages AI agents across any domain — mechanically enforced, not advisory."
- [ ] Supporting line text matches: "One kernel governs. One factory compiles. 27+ managed agents ship."
- [ ] CTA link/button present with text "See the architecture" and href="#architecture"

## Gates Satisfied
BUILD-06, BUILD-19

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
