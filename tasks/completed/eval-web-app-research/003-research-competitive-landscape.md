# Research Competitive Landscape

## Context
Understanding existing competitors per vertical is critical for positioning. The platform spans LLM eval, compliance testing, and QA generation — each has its own competitive set. This section must cover per-vertical competitors and our differentiation.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Use WebSearch to research competitors in each vertical:
  - **LLM Eval:** DeepEval cloud offering, Arize Phoenix, Braintrust, LangSmith, Weights & Biases
  - **Compliance Testing:** Chef InSpec, Qualys, Rapid7, Wiz, Tenable, OpenSCAP
  - **QA Generation:** Testim, Mabl, Functionize, Katalon, Applitools
  - **Code Review:** CodeClimate, SonarQube, Codacy, Snyk Code
- For each competitor: what they offer, pricing model, target market, limitations
- Identify gaps in each vertical that the platform could fill
- Analyze differentiation: dynamic component creation, harness compilation from _reference/ patterns, kernel governance, multi-vertical from one architecture
- Assess defensibility of the differentiation

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/02-competitive-landscape.md` exists
- [ ] Contains per-vertical competitor analysis (at least 3 competitors per vertical)
- [ ] Contains pricing/model comparison for key competitors
- [ ] Contains differentiation analysis section
- [ ] Contains gap analysis identifying unserved needs
- [ ] Minimum 500 words

## Gates Satisfied
DOC-04, DOC-05, DOC-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
