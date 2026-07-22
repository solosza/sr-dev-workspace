# Task 005: Scope-Boundary Gate
**Type:** TEST | **Gates:** BP-05
## Action
Verify business-plan.md holds the load-bearing scope boundary and contains no full-workflow-automation claims. Write pass/fail evidence.
## Spec
Confirm the doc EXPLICITLY states never-auto-bill AND never-auto-chart (and never-automate-filtering). Scan for prohibited claims: any promise to automate billing SUBMISSION, perform charting, or auto-filter patients (the product validates OVER those, it doesn't perform them). Confirm positioning is liability/audit-defensibility, not automation speed. Confirm all five required section groups (Problem, Solution, Proof, ROI/Pricing/GTM, Risk/Preconditions) exist and unverified numbers are flagged, not fabricated. This is a documentation gate — grep + read, evidence captured (which lines carry the boundary; zero prohibited-claim hits).
## Acceptance
Boundary present (never auto-bill/chart/filter), zero auto-workflow claims, all sections present, numbers flagged. Evidence recorded.
