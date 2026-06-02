# Research: Sourcing & Suppliers — Vietnam vs China

## Context
Produce a sourcing guide covering the two primary origin options (Vietnam and China), quality tier breakdown, and vetted supplier leads. This feeds directly into the legal compliance research (which path makes sense depends on whether suppliers will print branded replicas). Output: `projects/hoi-an-knockoff-shirts/sourcing-suppliers.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-knockoff-shirts/` directory exists

## Requirements
- Research primary China sourcing regions for replica streetwear (Guangzhou Baiyun/Shahe, 1688.com, DHgate)
- Research Vietnam apparel sourcing (Hội An/HCMC area — whether same network as leather goods extends to apparel)
- Document quality tier nomenclature: AAA, 1:1, OG, etc. — what each means in practice
- Identify 3-5 vetted supplier leads with quality indicators (DHgate stores with 500+ orders, 4.8+ ratings, etc.)
- Document sample ordering process: MOQ, sample cost, lead time, payment methods (Alipay, USDT, WeChat Pay)
- Note red flags and scam patterns at small order volumes
- Write supplier outreach template (WeChat/WhatsApp-friendly for China suppliers)

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/sourcing-suppliers.md` exists
- [ ] File contains a China vs Vietnam comparison section
- [ ] File contains a quality tier breakdown (at minimum AAA, 1:1 definitions)
- [ ] File contains at least 3 vetted supplier leads or sourcing channels
- [ ] File contains a sample order checklist
- [ ] `grep -qi "quality\|grade\|tier" projects/hoi-an-knockoff-shirts/sourcing-suppliers.md` passes

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
