# Task 006: Jargon + Format Gate
**Type:** TEST | **Gates:** OB-06
## Action
Verify business-plan.md is jargon-free, in the researched format, and keeps the guarantees. Write pass/fail evidence.
## Spec
Grep business-plan.md (case-insensitive) for BANNED terms: isagawa, kernel, 3-layer, config layer, validator layer, judgment layer, LLM, rubric, AST, harness, playwright, deterministic gate, model-assisted. ANY hit = RED (fix the text, then /kernel/learn). Confirm all standard business-plan sections from business-plan-format-notes.md are present. Confirm the product is referred to as "the application"/"the solution"/"the system" (no internal platform name). Confirm the plain-language guarantees are present: a person reviews/approves before any claim is billed, AND the application never submits a claim on its own. Confirm unverified numbers are flagged owner-to-confirm, not fabricated. Capture evidence (zero banned-term hits; section checklist).
## Acceptance
Zero banned-term hits; all sections present; product named neutrally; guarantees present; numbers honest. Evidence recorded.
