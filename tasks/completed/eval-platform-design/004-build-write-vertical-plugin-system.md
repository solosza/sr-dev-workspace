# Write Vertical Plugin System Design Document

## Context
This document defines how platform specs plug into the common execution layer. The multi-vertical architecture is the platform's core structural decision — one infrastructure serves LLM Eval, Compliance Testing, QA Generation, and future verticals by swapping which platform spec loads into the container.

This design must consume 158's research findings, specifically:
- First vertical = LLM Eval (platform-deepeval) per `01-idea-validation.md`
- Existing platform specs: platform-deepeval, platform-ssh-verify, platform-selenium per `02-competitive-landscape.md`
- Pre-baked container images per vertical per `03-tech-stack.md`
- Multi-vertical timing: LLM Eval first, Compliance 6-12mo, QA 12-18mo per `01-idea-validation.md`

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (prerequisite gate passed)

## Phase Gate
- [ ] Task 002 verdict = PROCEED
- [ ] `projects/eval-platform-design/` directory exists

## Requirements
Write `projects/eval-platform-design/vertical-plugin-system.md` covering:

1. **Plugin architecture** — how a platform spec (e.g., platform-deepeval) registers with the execution layer
   - Platform spec interface contract (what a spec must provide: `_reference/` patterns, metric definitions, test fixtures, FRAMEWORK.md)
   - Spec discovery and loading mechanism
   - Spec versioning (how container images pin to spec versions)

2. **Vertical registry** — how verticals are cataloged
   - Vertical metadata schema (name, description, platform spec repo, container image tag, supported artifact types)
   - First vertical: LLM Eval with platform-deepeval
   - Future verticals: Compliance (platform-ssh-verify), QA (platform-selenium)

3. **Container image build pipeline** — how pre-baked images are produced per vertical
   - Base image composition (Node.js + Python + Claude Agent SDK)
   - Vertical layer (kernel + platform spec + pre-compiled protocol + hooks)
   - Image tagging and versioning strategy
   - Rebuild triggers (platform spec update, kernel update, base image security patch)

4. **Vertical isolation** — how verticals stay independent
   - Each vertical has its own component library namespace
   - Each vertical has its own curation quality gates
   - Verticals share infrastructure (Cloud Run, PostgreSQL, job queue) but not domain state

5. **Expansion protocol** — steps to add a new vertical
   - Reference 158's estimate: 3-4 weeks per new vertical after MVP infrastructure

6. **References** — cite specific 158 research files that informed each design decision

## Acceptance Criteria
- [ ] `projects/eval-platform-design/vertical-plugin-system.md` exists
- [ ] Document references platform-deepeval as the first vertical (`grep -q 'platform-deepeval' projects/eval-platform-design/vertical-plugin-system.md`)
- [ ] Document contains `## References` section referencing `eval-web-app-research`
- [ ] Document defines the plugin interface contract
- [ ] Document covers container image build pipeline

## Gates Satisfied
- BUILD-04, BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
