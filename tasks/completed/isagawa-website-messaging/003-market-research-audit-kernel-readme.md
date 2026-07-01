# Audit Kernel README Messaging

## Context
Fetch and document the isagawa-kernel GitHub README positioning. This captures how the framework presents itself to developers and provides alignment context for homepage messaging.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/isagawa-website-messaging/` exists

## Requirements
- Fetch isagawa-kernel README from GitHub via WebFetch
- Document key positioning elements:
  - Main headline and tagline
  - Problem statement
  - Solution framing (SDD)
  - Core components description
  - Use cases and audiences
- Save raw audit to `projects/isagawa-website-messaging/_research/kernel-readme-audit-raw.md`

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/_research/kernel-readme-audit-raw.md` exists
- [ ] File contains key positioning elements from README
- [ ] File captures headline, problem, solution, components, and audiences

## Gates Satisfied
None (intermediate artifact — feeds into BUILD-02)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
