# Gate Contract - 255 Evidence Section

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PE-01 | Sanitized CLI trace visual captured from a REAL kernel run (existing runner output text reformatted as a styled terminal block or SVG - no fake output); scrubbed: no real paths beyond generic names, no internal hook/state filenames, no identifiers | run_test (grep the visual) | 001 | sanitization greps 0 hits |
| PE-02 | 3-4 evidence cards per guide section 7 (governed workflow, independent validation, controlled delivery, evaluation routing); each has a factual mechanism description + why-it-matters; metric slots marked 'pending verified figure' (NOT fabricated numbers); responsive two-column | grep | 002 | cards present, no invented metrics |
| PE-03 | Pushed; Pages rebuilt | run_code | 003 | push clean |
| PE-04 | L3 GATE: live page (cache-busted) shows 3-4 cards + the trace visual; NO fabricated percentages/counts (grep for suspicious patterns: \d+% success, \d+ workflows); IP-safety + absolute-claims greps clean | run_test | 004 | live green |

## Rules
- READ guide section 7 + section 13 disclosure table + current index.html FIRST (RULE ZERO)
- The trace visual comes from REAL runner output (e.g., a sanitized ALL TASKS COMPLETE banner + iteration lines) - never invented output
- Metrics: mechanism described, number omitted with a clearly-styled 'pending verified figure' marker
- Any red: fix then /kernel/learn
