# Multi-Vertical AI Testing Platform: Feasibility Research

## Status
Open

## Priority
High — If feasible, this turns the kernel + platform specs into a product with a real network effect across multiple verticals. The flywheel (more users → more components → better testing for everyone) is a competitive moat that compounds.

## Summary

Research the feasibility of a web platform where anyone can submit LLM artifacts for testing across multiple verticals. The core model: **BYOK + disposable containers + growing intelligence library + usage-driven flywheel.** Users bring their own API keys — we provide the testing intelligence and infrastructure. Each submission that requires new components causes the agent to build them on the spot using `_reference/` patterns, growing the platform with real-world usage. The architecture is identical across verticals — just swap which platform spec gets loaded into the container.

## The Model

```
User submits artifact + API keys
    → Fresh container spins up (kernel + relevant platform spec)
    → Agent reads submission, checks existing components
    → Builds missing components from _reference/ patterns
    → Runs the job, returns results, container dies
    → Proven new components merge to master
    → Platform gets smarter for the next user
```

## Multi-Vertical Vision

One platform architecture, multiple verticals. The kernel is the execution engine. The web wrapper is the same — the platform spec determines the vertical.

| Vertical | Platform Spec | What Users Submit | Intelligence Library | What Grows |
|----------|--------------|-------------------|---------------------|------------|
| LLM Eval | platform-deepeval | LLM artifacts (commands, skills, harnesses) | _reference/ metrics, fixtures, test patterns | New metrics, test components |
| Compliance Testing | platform-ssh | Infrastructure configs | STIG, CIS, NIST, HIPAA, SOC2 validators | New compliance rules, framework validators |
| QA Generation | platform-selenium | App specs or URLs | POM templates, selector strategies | New test patterns, page object models |
| Domain Spec Factory | kernel + existing specs | Domain descriptions | Existing domain specs as patterns | New domain spec templates, skill patterns |
| Code Review | (new spec) | Codebases | Anti-pattern library, review criteria | New anti-patterns, review rules |

Existing building blocks: platform-deepeval, platform-ssh, platform-selenium. Three verticals already have foundations.

## Key Questions to Answer

### Idea Validation
- Is there demand for "submit your LLM artifact, get it tested" as a service?
- Who is the target user? (AI engineers, teams building with Claude/GPT, enterprises with agent workflows?)
- Which vertical has the highest demand / lowest friction to start?
- Is the multi-vertical play a day-one pitch or a growth story?

### Competitive Landscape
- Who else offers LLM artifact testing as a service?
- How does this compare to DeepEval's own cloud offering?
- Compliance testing SaaS landscape (Chef InSpec, Qualys, etc.) — where's the gap?
- AI-powered QA generation competitors (Testim, Mabl, etc.)
- What's our differentiation? (Dynamic component creation, harness compilation, kernel governance, multi-vertical from one architecture)

### Tech Stack
- What's the minimum viable web wrapper around the existing CLI eval loop?
- How does the submission → container → eval → results pipeline work?
- Container orchestration: Docker Compose, K8s, ECS, Cloud Run?
- How does the agent run inside a container? (Claude API, not CLI? Claude Code SDK?)
- How do we handle the domain-setup compilation step in a containerized environment?
- Frontend: what does the submission UI + results dashboard look like?
- Backend: API design, job queue, results storage

### BYOK (Bring Your Own Key)
- How do users securely provide their API keys? (Vault, encrypted env vars, session-scoped?)
- Which LLM providers need to be supported? (Anthropic for the eval agent, user's choice for LLM-as-judge?)
- How do we prevent key leakage between container runs?
- Do users need different keys per vertical? (Anthropic for eval, maybe not for compliance)

### Component Growth Flywheel
- How do dynamically-created components get reviewed before merging to master?
- Automated quality check? Human review queue? Both?
- How do we handle conflicting component contributions from concurrent users?
- What's the versioning strategy for the growing component library?

### Component Curation at Scale
- The flywheel only works if merged components are good
- Automated quality gates: does the new component follow _reference/ patterns? Does it pass the same tests?
- Human review queue for edge cases?
- What's the operational cost of curation as the platform scales?
- This is the bottleneck that determines if the flywheel spins or stalls

### Security & Isolation
- Container-per-run handles process isolation, but what about malicious artifact submissions?
- How do we sandbox the eval agent's file access within the container?
- Rate limiting, abuse prevention?
- Data retention policy — do we keep submitted artifacts? Scores only?

### Business Model
- Users pay their own LLM costs (BYOK) — what do we charge for?
- Infrastructure costs (container compute) + the growing component library (the moat)?
- Free tier with limits? Pay per eval run? Subscription?
- Open source the framework, monetize the hosted platform?
- What do comparable platforms charge? (DeepEval cloud, compliance SaaS, QA SaaS)
- Per-vertical pricing or unified?

### Legal / IP
- Users submit artifacts that may contain proprietary logic
- Who owns the dynamically-created components? Are they derived from user submissions?
- Need clean IP boundaries — components created by the agent using _reference/ patterns may be considered platform-generated, not user-derived
- Terms of service: submitted artifacts are processed but not retained? Or retained for improvement?
- Open source licensing implications if framework is OSS but hosted platform is commercial

## References

- Backlog 157: `/kernel/eval` command design — `docs/backlog/157-kernel-build-deepeval-command-testing.md`
- Platform-deepeval: `D:\my_ai_projects\project_test_repos\platform-deepeval`
- Platform-ssh: `D:\my_ai_projects\project_test_repos\platform-ssh-verify`
- Platform-selenium: `D:\my_ai_projects\project_test_repos\platform-selenium`
- Existing _reference/ patterns: `platform-deepeval/framework/_reference/`
- Backlog 131-132: Claude harness marketplace/distribution research (in done/)

## Dependency Chain

```
157 (BUILD: /kernel/eval command)  ← designed, not yet built
    │
158 (RESEARCH: this backlog)
    │
    └──→ 159 (BUILD: platform architecture design)  ← BLOCKED by this
              Gate 0 validates this research is complete + go before proceeding
```

**Output contract:** 159's prerequisite gate checks that this research covers ALL of the following before allowing design work to proceed:
- Idea validation (demand, target user, first vertical recommendation)
- Competitive landscape (per-vertical competitors, differentiation)
- Tech stack recommendation (container orchestration, API, frontend/backend)
- BYOK model (key management approach, provider support)
- Component flywheel + curation (automated gates, human review, operational cost)
- Security & isolation (sandboxing, abuse prevention, data retention)
- Business model (pricing, comparable benchmarks)
- Legal/IP (component ownership, user submission boundaries)
- Go/no-go recommendation

If any item is missing, 159 blocks and reports what's incomplete.

## Task Builder Input
- **Deliverable:** Feasibility research covering ALL items in the output contract above. Multi-vertical analysis. Go/no-go recommendation with estimated effort for MVP. Recommended first vertical. Must be complete enough to pass 159's prerequisite gate.
- **Location:** `subproject:eval-web-app-research`
- **Scope:** RESEARCH
- **Constraints:** Depends on backlog 157 being designed (it is). Does not require 157 to be built first — research can run in parallel. Must consider existing platform specs (deepeval, ssh, selenium) and _reference/ architecture. Output must satisfy 159's gate checklist.
