# Validate Prerequisite Gate (158 Research Output)

## Context
Backlog 159 has a mandatory prerequisite gate (Step 0) that validates 158's research output before any design work begins. This task performs the 4-check validation defined in the backlog and produces the gate verdict. The verdict determines whether design tasks 003-009 can proceed.

This is the critical blocking gate — if 158's research is incomplete, has a no-go recommendation, or has data inconsistencies, all design work is blocked.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (project directory exists)

## Phase Gate
- [ ] `projects/eval-platform-design/` directory exists
- [ ] `projects/eval-web-app-research/` directory exists and contains 9 research files

## Requirements
Perform all 4 checks from backlog 159's prerequisite gate specification:

**Check 1: Research output exists**
- Read `projects/eval-web-app-research/` — verify directory exists and is non-empty
- If missing or empty, verdict = BLOCKED

**Check 2: Research is complete**
Verify ALL 9 items are covered across the research files:
- Idea validation (demand, target user, first vertical recommendation) — `01-idea-validation.md`
- Competitive landscape (per-vertical competitors, differentiation) — `02-competitive-landscape.md`
- Tech stack recommendation (container orchestration, API, frontend/backend) — `03-tech-stack.md`
- BYOK model (key management approach, provider support) — `04-byok-model.md`
- Component flywheel + curation (automated gates, human review, operational cost) — `05-component-flywheel-curation.md`
- Security and isolation (sandboxing, abuse prevention, data retention) — `06-security-isolation.md`
- Business model (pricing, comparable benchmarks) — `07-business-model.md`
- Legal/IP (component ownership, user submission boundaries) — `08-legal-ip.md`
- Go/no-go recommendation — `09-go-no-go-recommendation.md`

**Check 3: Go/no-go is "go"**
- Read `09-go-no-go-recommendation.md`
- If "no-go" — BLOCKED permanently
- If "go with conditions" — proceed but carry conditions as design constraints

**Check 4: Data correctness cross-checks**
- Does the tech stack recommendation address the Windows/Linux gap? (kernel runs on Windows/bash, containers would be Linux)
- Does the business model account for BYOK? (users should not be charged for LLM costs they already pay)
- Does the competitive analysis cover DeepEval's own cloud offering?
- If inconsistencies found, FLAG but do not block

**Output:** Write the gate verdict to stdout in the format specified by the backlog. This verdict is consumed by task 003 which writes the formal document.

## Acceptance Criteria
- [ ] All 9 research files in `projects/eval-web-app-research/` have been read and verified present
- [ ] Go/no-go recommendation extracted and is "GO" or "GO (Conditional)"
- [ ] Cross-check results documented (flags or pass)
- [ ] Gate verdict produced: PROCEED or BLOCKED with reason
- [ ] If GO (Conditional), conditions extracted and listed for downstream tasks to consume

## Gates Satisfied
- BUILD-10, BUILD-03 (partial — verdict produced, formal doc written in 003)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
