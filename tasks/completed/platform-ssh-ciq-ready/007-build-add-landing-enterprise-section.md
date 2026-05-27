# Add Enterprise Section to Landing Page

## Context
CIQ is an enterprise Linux company. The landing page needs messaging that speaks to enterprise teams — why Isagawa, what makes this different from scripts.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Edit `D:\my_ai_projects\isagawa-co.github.io\ssh-compliance.html`
- Add a "Why Isagawa" section between the "Who This Is For" section and the CTA
- 3-4 bullet points: auditable compliance (evidence captured), self-improving (learns from failures), 8 frameworks (one platform), kernel-enforced (can't skip checks)
- Match existing page styling

## Acceptance Criteria
- [ ] ssh-compliance.html contains "Why Isagawa" or "enterprise" section
- [ ] Section has at least 3 value proposition items

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
