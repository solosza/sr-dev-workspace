# Build HTML CTA Section

## Context
Adds the call-to-action section to index.html — the conversion point where visitors are invited to reach out.

## Type
BUILD

## Execution
inline

## Dependencies
- 054

## Requirements
- Add a `<section id="cta">` to index.html after the loop section
- Heading (h2): "What domain do you need managed?"
- Subheading (p): "Whether it's compliance, QA, healthcare, DevOps, or something we haven't built yet — the factory can compile it."
- Contact email: `<a href="mailto:alain@isagawa.co">alain@isagawa.co</a>`
- Links:
  - GitHub: link to isagawa-co GitHub org
  - LinkedIn: link to LinkedIn profile

## Acceptance Criteria
- [ ] Section element exists with id="cta"
- [ ] H2 heading matches: "What domain do you need managed?"
- [ ] Subheading matches: "Whether it's compliance, QA, healthcare, DevOps, or something we haven't built yet — the factory can compile it."
- [ ] mailto link present for alain@isagawa.co
- [ ] GitHub and LinkedIn links present

## Gates Satisfied
BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
