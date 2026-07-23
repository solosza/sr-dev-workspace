# Gate Contract - 261 IP-Safe Review + Final Deploy Sweep

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| RS-01 | Section 13 IP-safe disclosure audit vs LIVE page + repo: sweep for anything in the keep-private column (state schemas, hook logic/names, gate rules, command protocols, meta-factory internals, full domain contracts, private paths/logs). Strip <style>; check match context (lessons 255/256/258) | run_test | 001 | 0 real leaks (context-verified) |
| RS-02 | Section 15 final checklist (v1.2) each item verified vs the live URL with evidence: name+role before Isagawa brand; first screen <10s; verified-only stack badges; Isagawa explained w/o internal architecture; NO unfilled [INSERT] shipped as final copy; DX snippet labeled illustrative; every project states personal contribution; NO absolute claims (100%/guaranteed/unbypassable/zero drift) anywhere; one flagship + <=3 secondary; limitations honest; asks for interviews; resume/GitHub/LinkedIn/email findable; skimmable in 1 min | run_test | 002 | every item PASS or flagged |
| RS-03 | Rendering: mobile + desktop viewport (Playwright MCP or HTTP + width checks) + print stylesheet check; OG metadata present + valid | run_test | 003 | renders + OG valid |
| RS-04 | Signed-off review report written to projects/portfolio-site/261-review-report.md with per-item evidence + any open HUMAN items (esp. the 255 pending-verified-figure metric slots) listed for the user | file_exists | 004 | report with evidence + open items |

## Rules
- READ guide sections 13 + 15 + fetch the full live page FIRST (RULE ZERO)
- Absolute-claims / kernel-internal greps: use `lib/gate_integrity.py`'s `strip_markup_then_grep` (RS-01) / `check_absolute_claims` (RS-02) — strips <style>/<script>/inline style="..." THEN greps THEN reports match CONTEXT, only failing on real occurrences (CSS max-width:100% is NOT a claim - lessons 255/256/258; helper added backlog 273 GI-03)
- If a checklist item genuinely fails (e.g., a visible [INSERT], a real absolute claim), that is a RED - fix on the live page then re-verify (or flag as a HUMAN item if it needs user input like verified metrics)
- Any red -> fix then /kernel/learn
