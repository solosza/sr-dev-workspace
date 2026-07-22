# Task 002: Isagawa Feasibility
**Type:** RESEARCH | **Gates:** RC-02
## Action
Write projects/therapy-compliance-automation/isagawa-feasibility.md.
## Spec
READ projects/rt-automation/ (design baseline, 3-layer pattern: Config JSON rules + Python validators + Kernel enforcement) FIRST - reference it, do not re-derive. Map task-001's compliance rules to the 3 layers; classify which checks are DETERMINISTIC (coverage status, order present, CPT-vs-charting match, refused-flag) vs MODEL-ASSISTED (charting supports medical necessity; diagnosis supports intervention) - the latter need an LLM judge + a mandatory human-review gate (never auto-bill a probabilistic eligible). Address data access (EMR integration vs Playwright UI automation vs export), PHI handling, and the audit-trail requirement (Isagawa attestation/state as a fit - no internals exposed). Honest effort estimate + hard parts. State the technical GO/NO-GO criteria.
## Acceptance
Feasibility verdict with the deterministic-vs-judgment split, data/PHI/audit treatment, honest effort. Cited where external.
