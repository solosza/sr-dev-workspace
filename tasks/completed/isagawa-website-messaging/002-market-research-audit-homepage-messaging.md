# Audit Current Homepage Messaging

## Context
Fetch and document the current isagawa.co homepage copy verbatim. This provides the baseline for identifying gaps and repositioning opportunities.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/isagawa-website-messaging/` exists

## Requirements
- Fetch isagawa.co homepage via WebFetch
- Document ALL text content verbatim, organized by section:
  - Hero section (headline, subheadline, description)
  - Each numbered section (01-04)
  - CTAs
  - Provenance section
  - Footer
- Save raw audit to `projects/isagawa-website-messaging/_research/homepage-audit-raw.md`
- Note: this is raw data capture, not analysis

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/_research/homepage-audit-raw.md` exists
- [ ] File contains verbatim copy from all homepage sections
- [ ] File is organized by section (Hero, Section 01, Section 02, etc.)

## Gates Satisfied
None (intermediate artifact — feeds into BUILD-02)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
