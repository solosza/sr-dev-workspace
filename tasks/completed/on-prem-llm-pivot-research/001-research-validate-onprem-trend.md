# Validate the Enterprise On-Prem LLM Trend

## Context
Companies reportedly fear frontier model providers absorb their IP via API usage, driving interest in local/on-prem LLM hosting. This task validates whether that shift is real and how big it is — everything downstream (pivot analysis, skill plan) depends on this being evidence-based, not assumed. Produces `projects/on-prem-llm-pivot-research/01-trend-validation.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Web research (WebSearch/WebFetch) — every substantive claim carries a source link
- Find: enterprise surveys/spend data on on-prem vs API LLM usage; vendor moves signaling demand (NVIDIA enterprise push, open-weight releases, private-AI offerings); documented IP/data-leak incidents or policies (e.g., companies banning external LLM APIs); regulated-industry drivers (healthcare/HIPAA, defense, finance)
- Distinguish hype from spend: who is actually BUYING GPUs / deploying local models vs just talking
- Note counter-evidence too: API-side mitigations (zero-retention agreements, VPC endpoints, BAAs) that weaken the on-prem case
- Write `projects/on-prem-llm-pivot-research/01-trend-validation.md`: findings, evidence table with sources, honest assessment of trend strength (strong/moderate/weak) and trajectory

## Acceptance Criteria
- [ ] `projects/on-prem-llm-pivot-research/01-trend-validation.md` exists
- [ ] Contains ≥ 5 source URLs (grep -c "http" ≥ 5)
- [ ] States an explicit trend-strength assessment
- [ ] Includes counter-evidence section

## Gates Satisfied
- RSCH-01, RSCH-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
