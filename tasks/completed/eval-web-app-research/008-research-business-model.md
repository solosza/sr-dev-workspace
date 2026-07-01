# Research Business Model

## Context
Users pay their own LLM costs via BYOK. The platform charges for infrastructure compute and access to the growing component library (the moat). This section must benchmark pricing against comparable platforms and recommend a model.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Use WebSearch to research pricing of comparable platforms:
  - **LLM Eval:** DeepEval cloud pricing, Braintrust pricing, LangSmith pricing tiers
  - **Compliance SaaS:** Qualys pricing, Chef InSpec / Progress pricing, Wiz pricing
  - **QA SaaS:** Testim pricing, Mabl pricing, Katalon pricing
  - **Dev tools:** GitHub Actions pricing (compute model), Replit pricing, CodeSandbox pricing
- Research pricing models:
  - Per-run pricing (pay per container execution)
  - Subscription tiers (free/pro/enterprise with run limits)
  - Freemium (limited runs free, pay for more)
  - Open source framework + hosted platform (GitLab model)
- Analyze per-vertical vs unified pricing:
  - Different verticals have different compute costs
  - Compliance runs may be cheaper (no LLM calls by platform)
  - LLM eval runs may be more expensive (agent uses Claude API)
- Estimate unit economics:
  - Container compute cost per run (Cloud Run, ECS pricing)
  - Claude API cost per eval run (agent token usage)
  - Storage cost for results and component library
  - Break-even analysis at various run volumes
- Recommend pricing model with rationale

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/07-business-model.md` exists
- [ ] Contains pricing benchmarks from at least 5 comparable platforms
- [ ] Contains pricing model comparison (per-run vs subscription vs freemium)
- [ ] Contains per-vertical cost analysis
- [ ] Contains unit economics estimates
- [ ] Contains pricing recommendation
- [ ] Minimum 400 words

## Gates Satisfied
DOC-19, DOC-20, DOC-21

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
