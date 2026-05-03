# Write Hero Section Content

## Context
The hero is the first thing visitors see. It must communicate the loop in one sentence. Old hero said "The AI Management Layer." New hero says "Isagawa is a conversational agent factory." The hero must pass the 90-second test: after reading, a stranger should say "He builds systems that build themselves from what he tells them."

## Type
BUILD

## Execution
inline

## Dependencies
- 003-build-html-rewrite-skeleton

## Phase Gate
- [ ] `index.html` contains `id="hero"` section stub

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Replace hero stub content with:
  - h1: "Isagawa" (the name, not a description)
  - h2: "A conversational agent factory."
  - p: "You describe intent in natural language. The factory produces structured artifacts — including new capabilities — under mechanical governance. Those capabilities become part of the factory. The loop closes."
  - CTA link: "See the loop →" pointing to `#seed`
- No jargon — stranger must understand without context
- Reference: `docs/backlog/047-market-build-portfolio-site-loop-theme/positioning.md`

## Acceptance Criteria
- [ ] `index.html` hero section contains "conversational agent factory"
- [ ] `index.html` hero section contains a CTA link to `#seed`
- [ ] `index.html` hero section does NOT contain "AI Management Layer"

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
