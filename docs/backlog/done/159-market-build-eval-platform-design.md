# Multi-Vertical AI Testing Platform: Architecture Design

## Status
Open — BLOCKED by 158

## Priority
Medium — Design depends on 158's research output and go/no-go recommendation.

## Summary

Design the architecture for a multi-vertical AI testing platform. Users submit LLM artifacts, bring their own API keys (BYOK), and get scored results. The platform uses disposable cloud containers, compiles agent harnesses per-run, and grows its intelligence library through dynamic component creation. One architecture serves multiple verticals by swapping which platform spec loads into the container.

This backlog consumes 158's research output as its primary input. A prerequisite gate validates that research is complete and recommends "go" before any design work begins.

## Dependency Chain

```
158 (RESEARCH: feasibility + competitive + tech stack)
    │
    ├── Produces: feasibility report, competitive landscape, tech stack recommendation,
    │             business model analysis, legal/IP guidance, go/no-go
    │
    └──→ 159 (BUILD: platform architecture design)  ← THIS BACKLOG
              │
              ├── Gate 0: Validate 158 output (exists, complete, go)
              │
              └── Produces: architecture docs, API design, container pipeline,
                            vertical plugin spec, BYOK design, curation pipeline
```

## Prerequisite Gate (Step 0)

Before ANY design work begins, the agent MUST:

### Check 1: Research output exists
- Read `projects/eval-web-app-research/` (158's deliverable location)
- If the directory doesn't exist or is empty → BLOCK. Report: "158 not complete."

### Check 2: Research is complete
Verify the research covers ALL of these (check for sections/files):
- [ ] Idea validation (demand, target user, first vertical recommendation)
- [ ] Competitive landscape (per-vertical competitors, differentiation)
- [ ] Tech stack recommendation (container orchestration, API, frontend/backend)
- [ ] BYOK model (key management approach, provider support)
- [ ] Component flywheel + curation (automated gates, human review, operational cost)
- [ ] Security & isolation (sandboxing, abuse prevention, data retention)
- [ ] Business model (pricing, comparable benchmarks)
- [ ] Legal/IP (component ownership, user submission boundaries)
- [ ] Go/no-go recommendation

If ANY item is missing → BLOCK. Report which items are missing.

### Check 3: Go/no-go is "go"
- Read the go/no-go recommendation from 158's output
- If "no-go" → BLOCK permanently. Report: "158 recommends no-go. Reason: [reason]."
- If "go with conditions" → proceed but carry conditions as constraints into design

### Check 4: Data correctness
- Cross-check: does the tech stack recommendation align with existing infrastructure? (kernel runs on Windows/bash, containers would be Linux — is this addressed?)
- Cross-check: does the business model account for BYOK? (users shouldn't be charged for LLM costs they're already paying)
- Cross-check: does the competitive analysis cover DeepEval's own cloud offering?
- If inconsistencies found → FLAG but don't block. Carry as open questions into design.

### Gate Output
```
GATE 0: PREREQUISITE CHECK

  158 output location: projects/eval-web-app-research/
  Research complete: YES/NO (missing: [items])
  Go/no-go: GO / NO-GO / GO WITH CONDITIONS
  Data consistency: PASS / FLAGS ([issues])

  Verdict: PROCEED / BLOCKED ([reason])
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[159-market-build-eval-platform-design/vertical-plugin-system]] | How platform specs plug into the common execution layer |
| [[159-market-build-eval-platform-design/execution-pipeline]] | Submission → container → harness compilation → eval → results → teardown |
| [[159-market-build-eval-platform-design/byok-key-management]] | Secure key injection, provider abstraction, zero-retention |
| [[159-market-build-eval-platform-design/component-curation-pipeline]] | Dynamic components → review gate → master merge (the flywheel's plumbing) |
| [[159-market-build-eval-platform-design/api-and-frontend]] | REST/GraphQL design, submission UI, results dashboard, vertical selector |
| [[159-market-build-eval-platform-design/multi-tenancy-isolation]] | Concurrent users, container sandboxing, rate limiting, abuse prevention |
| [[159-market-build-eval-platform-design/prerequisite-gate]] | Gate 0 specification — how to validate 158's output before proceeding |

## Requirements

- Prerequisite gate MUST pass before any design work begins
- All design decisions must reference 158's research findings (not assumptions)
- Architecture must support multiple verticals from day one (not bolted on later)
- BYOK is non-negotiable — platform never touches user's LLM costs
- Component curation pipeline must have automated quality gates (not just human review)
- Container isolation must prevent cross-user data leakage
- Design must account for the existing platform specs (deepeval, ssh, selenium)
- First vertical chosen based on 158's recommendation

## References

- Backlog 158: Research (prerequisite) — `docs/backlog/158-market-research-eval-web-app-feasibility.md`
- Backlog 157: `/kernel/eval` command design — `docs/backlog/157-kernel-build-deepeval-command-testing.md`
- Platform-deepeval: `D:\my_ai_projects\project_test_repos\platform-deepeval`
- Platform-ssh: `D:\my_ai_projects\project_test_repos\platform-ssh-verify`
- Platform-selenium: `D:\my_ai_projects\project_test_repos\platform-selenium`
- 158 research output: `projects/eval-web-app-research/`

## Task Builder Input
- **Deliverable:** Complete platform architecture design with API spec, container pipeline design, vertical plugin system, BYOK design, curation pipeline, and multi-tenancy model. All grounded in 158's research findings.
- **Location:** `subproject:eval-platform-design`
- **Scope:** BUILD
- **Constraints:** BLOCKED by 158. Prerequisite gate must pass before execution. Design must consume 158's research output — no assumptions where data exists. First vertical per 158's recommendation.
