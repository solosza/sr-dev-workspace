# Build Evidently LLM Monitoring & Eval Domain Spec

## Status
Deprioritized

## Priority
Low — revisit after eval business is established; monitoring is a different buyer and pitch than evaluation

## Summary
Build a domain spec for Evidently — LLM production monitoring, testing, and evaluation. Third in the eval spec trilogy alongside DeepEval (general LLM eval) and RAGA (RAG-specific eval). Evidently fills the "operate" gap — what happens after deployment. Uses the DeepEval spec as the template.

## Why Evidently
- **Production monitoring** — tracks model quality, data drift, and output degradation over time
- **Complements DeepEval/RAGA** — they handle pre-deployment eval; Evidently handles post-deployment
- **Open source** — Python library, no platform lock-in
- **LLM-as-judge support** — custom judge prompts and models for automated quality scoring
- **Dashboards** — visual reporting for eval results and quality trends
- **Test suites** — define pass/fail conditions for CI/CD integration
- **Active maintenance** — v0.4.25+, regular releases through 2026

## Why Not Promptfoo
Promptfoo was acquired by OpenAI (March 9, 2026) and folded into their Frontier platform. Open source future uncertain — bad bet for a long-lived spec.

## What Makes It Different From DeepEval/RAGA
| Concern | DeepEval | RAGA | Evidently |
|---------|----------|------|-----------|
| Focus | Pre-deploy eval | RAG pipeline eval | Production monitoring + eval |
| When | During development | During development | After deployment |
| Drift detection | No | No | Core feature |
| Dashboards | Confident AI (SaaS) | No | Built-in HTML reports |
| Test suites | pytest | pytest | Own test suite format + pytest |
| Data profiling | No | No | Yes — input/output distributions |
| LLM-as-judge | Via metrics | Via metrics | Custom judge prompts |

## Template
**Source:** `C:\Users\solos\my_ai_projects\platform-deepeval-spec`

| Component | Reuse | Adapt |
|-----------|-------|-------|
| SKILL.md | Structure, philosophy | Evidently identity, monitoring vocabulary |
| workflow.md | Step pipeline pattern | Report generation + test suite workflow |
| gate-contract.md | Gate structure | Drift thresholds, quality degradation gates |
| steps/ | Step file pattern | Adapted for: configure → baseline → monitor → alert → triage |
| references/ | Catalog format | Evidently metric catalog, report types, test conditions |
| framework/_reference/ | Layer pattern | Report templates, test suites, dashboard configs |

## Evidently-Specific Workflow
1. **User Input** — target LLM application, quality dimensions to monitor, alert thresholds
2. **Pre-flight** — verify evidently installed, data access, baseline dataset available
3. **Baseline Generation** — run eval on reference dataset, establish quality baseline
4. **Monitor Configuration** — set up reports, test suites, drift detection
5. **Execution** — generate reports, run test suites, detect regressions
6. **Triage** — human reviews quality degradation, agent recommends fixes

## Key Monitoring Dimensions
| Category | Metrics |
|----------|---------|
| Text quality | Length, sentiment, toxicity, readability |
| Retrieval quality | Context relevance, retrieval precision |
| LLM output quality | LLM-as-judge scores, custom rubrics |
| Data drift | Input distribution shift, output distribution shift |
| Regression | Quality score trends, failure rate changes |

## Implementation Steps
- [ ] Research Evidently API, report types, test suite format
- [ ] Clone DeepEval spec structure into new repo
- [ ] Replace pytest-centric workflow with report + test suite workflow
- [ ] Build monitoring-specific gates (drift thresholds, quality baselines)
- [ ] Build reference report templates and test suites
- [ ] Test with a real LLM application in production
- [ ] Package for marketplace

## Output
- Repo: `isagawa-qa/platform-evidently-spec`
- Drop-in domain spec for LLM production monitoring and quality testing

## Eval Spec Trilogy
| Spec | Focus | Phase | Status |
|------|-------|-------|--------|
| DeepEval | General LLM eval | Build/Test | Done |
| RAGA | RAG-specific eval | Build/Test | Backlog 010 |
| Evidently | Production monitoring + eval | Operate | This item |

## References
- Evidently docs: https://docs.evidentlyai.com
- Evidently GitHub: https://github.com/evidentlyai/evidently
- DeepEval spec (template): `C:\Users\solos\my_ai_projects\platform-deepeval-spec`

## Task Builder Input
- **Deliverable:** Evidently domain spec repo (`isagawa-qa/platform-evidently-spec`) with monitoring workflow, drift detection, report generation
- **Scope:** BUILD
- **Constraints:** Deprioritized — revisit after eval business established. Template: DeepEval spec. Different buyer/pitch than eval specs.
