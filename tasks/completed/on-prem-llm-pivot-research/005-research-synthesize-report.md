# Synthesize the Research Report

## Context
Final synthesis: pull 01-04 into one decision-ready report with a go/no-go/watch recommendation. This is the deliverable the user reads. Produces `projects/on-prem-llm-pivot-research/research-report.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001, 002, 003, 004

## Phase Gate
- [ ] `projects/on-prem-llm-pivot-research/01-trend-validation.md` exists
- [ ] `projects/on-prem-llm-pivot-research/02-solution-landscape.md` exists
- [ ] `projects/on-prem-llm-pivot-research/03-isagawa-pivot-analysis.md` exists
- [ ] `projects/on-prem-llm-pivot-research/04-personal-skill-path.md` exists

## Requirements
- Read all four inputs; synthesize — do not re-research, do not duplicate their content (link to them)
- Structure: Executive summary (≤ 1 page) → Recommendation (GO / NO-GO / WATCH, with the evidence chain) → Top 3 Isagawa opportunities (from 003, one paragraph each) → Personal 30-60-90 plan summary (from 004) → What would change the recommendation (trigger conditions to re-evaluate)
- The recommendation must take a position — "it depends" is not a recommendation; conditions belong under trigger conditions
- Write `projects/on-prem-llm-pivot-research/research-report.md`

## Acceptance Criteria
- [ ] `projects/on-prem-llm-pivot-research/research-report.md` exists
- [ ] Contains an explicit GO / NO-GO / WATCH recommendation
- [ ] Contains top-3 opportunities and 30-60-90 summary sections
- [ ] Contains re-evaluation trigger conditions

## Gates Satisfied
- RSCH-09, RSCH-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
