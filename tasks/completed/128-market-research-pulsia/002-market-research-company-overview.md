# Research and Document Company Overview

## Context
Pulsia is an autonomous AI company builder operating at scale (1,000-2,000 companies, nightly autonomous decisions). This task researches and documents Pulsia's business model, positioning, revenue structure, and scale metrics. Understanding their operational model is foundational for assessing harness pattern applicability.

## Type
RESEARCH

## Execution
inline

## Dependencies
None

## Phase Gate
- [ ] Project directory `projects/pulsia-research/` exists (from task 001)

## Requirements
- Research Pulsia's public information (website, blog, case studies, LinkedIn, Twitter, YouTube)
- Document business model and revenue structure (note: $50/month base + 20% revenue share)
- Identify customer segments and use cases
- Capture scale metrics (number of companies, autonomous decisions/nightly, geographic reach)
- Identify pricing model and go-to-market strategy

## Acceptance Criteria
- [ ] `projects/pulsia-research/01-company-overview.md` created
- [ ] Document covers business model and positioning (minimum 300 words)
- [ ] Document includes revenue structure ($50/month + 20% rev share)
- [ ] Document identifies 3+ customer segments or use cases
- [ ] Document states scale metrics (1,000-2,000 companies, nightly decisions)
- [ ] Document has minimum 500 words total

## Gates Satisfied
- RESEARCH-01 (company overview exists)
- SEMANTIC-01 (content quality — contributes to consolidated report)

## Completion Signal
When all acceptance criteria are met, invoke `/kernel/complete`.
