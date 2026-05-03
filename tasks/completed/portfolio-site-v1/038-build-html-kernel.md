# Build HTML Kernel Section

## Context
Adds the kernel governance section to index.html. This section explains the four mechanical enforcement mechanisms that make Isagawa governance non-optional.

## Type
BUILD

## Execution
inline

## Dependencies
- 037

## Requirements
- Add a `<section id="kernel">` to index.html after the architecture section
- Heading (h2): "The Kernel — Governance That Cannot Be Bypassed"
- Subheading (p): "Four mechanisms that make AI agent governance mechanical, not advisory."
- Four mechanism cards:
  1. **Anchor Token** — "Every 10 actions, the kernel forces re-centering on protocol. A UUID token proves the agent actually re-read its rules."
  2. **Gate Enforcer** — "Python hooks intercept every Write, Edit, and Bash command. Five gates checked before any action proceeds."
  3. **Learn Loop** — "Every failure becomes a permanent lesson. Lessons promote into hard enforcement (hooks, not just docs)."
  4. **Self-Audit** — "The kernel audits its own infrastructure for gaps. Auto-generates fix tasks when drift is detected."
- Read full content from content-spec.md Section 3 for any additional detail
- Each card should have a heading element for the mechanism name and a paragraph for the description

## Acceptance Criteria
- [ ] Section element exists with id="kernel"
- [ ] H2 heading matches: "The Kernel — Governance That Cannot Be Bypassed"
- [ ] Subheading matches: "Four mechanisms that make AI agent governance mechanical, not advisory."
- [ ] Four mechanism cards present with correct names and descriptions
- [ ] Each card has a heading and description paragraph

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
