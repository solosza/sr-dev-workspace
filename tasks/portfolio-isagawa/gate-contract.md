# Gate Contract - 252 Isagawa Overview

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PI-01 | Section per guide 4: definition, capabilities list, conceptual diagram (inline SVG/HTML: input -> governed workflow -> validated output), ownership statement, 6-8 line YAML DX teaser labeled 'representative example, not an internal file' | grep + html parse | 001 | all includes present |
| PI-02 | Avoid-list clean: no internal layer names, folder structures, protocol/hook/state-field names, meta-factory detail; snippet is generic (qa-automation domain example per guide sample) | run_test (grep for kernel-internal terms) | 001 | 0 hits |
| PI-03 | Pushed; Pages rebuilt | run_code | 002 | push clean |
| PI-04 | L3 GATE: live page shows the section (poll <=10 min): definition text, diagram element, labeled snippet, ownership line; IP-safety greps clean on LIVE html | run_test | 003 | live green |

## Rules
- READ guide section 4 fully + current index.html before editing (RULE ZERO); use the guide's sample copy and sample YAML as the base
- Self-contained page (inline CSS/SVG)
- Any red: fix then /kernel/learn
