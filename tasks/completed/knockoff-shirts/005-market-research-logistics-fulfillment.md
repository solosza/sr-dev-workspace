# Research: Logistics & Fulfillment — Import Duties and Freight

## Context
Produce a logistics cost model covering import duties (US HTS codes for apparel), freight options, and small-batch fulfillment. This data feeds directly into the pricing strategy task. Output: `projects/hoi-an-knockoff-shirts/logistics-fulfillment.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-knockoff-shirts/` directory exists

## Requirements
- Identify US HTS codes for: knit T-shirts (Chapter 61), woven shirts (Chapter 62), hoodies (Chapter 61) — include specific 10-digit HTS codes and duty rates from China and Vietnam
- Assess de minimis threshold ($800/shipment) — is it viable for commercial replica imports, or does Customs flag it?
- Research air freight costs from Guangzhou and Da Nang for 12-unit and 36-unit apparel batches (use freight forwarder rate cards or Freightos benchmarks)
- Identify 2-3 freight forwarders or shipping agents that handle small-batch China/Vietnam apparel (e.g., Flexport, Freightos, or agent networks)
- Research Customs seizure risk for apparel with visible branded logos (replica risk at small quantities)
- Identify fulfillment options: self-fulfill, 3PL (ShipBob/Shipmonk minimum order requirements for apparel), or direct dropship from supplier

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/logistics-fulfillment.md` exists
- [ ] File contains HTS code table with duty rates from China and Vietnam
- [ ] File contains freight cost estimates for at least two batch sizes
- [ ] File contains de minimis strategy assessment
- [ ] File contains at least 2 fulfillment options with pros/cons
- [ ] `grep -qi "HTS\|duty\|chapter 61\|chapter 62" projects/hoi-an-knockoff-shirts/logistics-fulfillment.md` passes

## Gates Satisfied
- DOC-09, DOC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
