# Gate Contract — 275 Owner-Facing Business Plan

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| OB-01 | business-plan-format-notes.md: the standard healthcare/medical business-plan structure researched live and cited (section list + source URL + date); notes which sections apply here | file_exists + content | 001 | format cited, sections listed |
| OB-02 | The 274 technical draft preserved as business-plan-strategy-brief-internal.md (not lost); new business-plan.md scaffolded with the researched section headings | file_exists (both) | 002 | old preserved + new skeleton |
| OB-03 | business-plan.md: Executive Summary + Business/Company Description + Market Analysis (industry, target market, competition) written in plain owner-facing language | file_exists + content | 003 | 3 sections, non-technical |
| OB-04 | business-plan.md: Products & Services (the application in plain language) + Marketing & Sales + Operations + Organization/Management | file_exists + content | 004 | sections present, plain |
| OB-05 | business-plan.md: Financial Plan/Projections + Pricing + Funding + the phased Roadmap (plain) + Appendix; unverified numbers flagged owner-to-confirm (not fabricated); never-auto-submit + human-review guarantees stated in plain English | file_exists + content | 005 | sections + guarantees + honest gaps |
| OB-06 | JARGON + FORMAT GATE: business-plan.md contains ZERO occurrences (case-insensitive) of: isagawa, kernel, 3-layer, config layer, validator layer, judgment layer, LLM, rubric, AST, harness, playwright, deterministic gate. All standard business-plan sections present. Product referred to as "the application"/"the solution". HITL ("a person reviews/approves before billing") + never-auto-submit present in plain language. | grep + read | 006 | zero jargon hits, all sections, guarantees |

## Rules
- READ the 274 draft + 269 research FIRST (RULE ZERO) — reuse the substance; do NOT re-derive the domain or invent new facts
- HARD BRANDING RULE: the reader is a non-technical owner. Translate every mechanism to plain language. Banned terms (case-insensitive): isagawa, kernel, 3-layer, config/validator/judgment layer, LLM, rubric, AST, harness, playwright, deterministic gate, model-assisted. Say "the application" / "the solution" / "the system".
- Follow the RESEARCHED business-plan format (task 001) — real structure, not an ad-hoc essay
- Keep the guarantees in plain English: "a person always reviews and approves before any claim is billed"; "the application never submits a claim on its own"
- Keep honesty: unverified numbers = owner/expert-to-confirm, never fabricated; the four preconditions stated plainly
- Any RED (jargon hit, missing section, fabricated number, branding leak) -> fix -> /kernel/learn
