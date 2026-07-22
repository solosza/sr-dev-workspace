# Gate Contract - 254 Architecture

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PA-01 | Section per guide 6: four public concepts (structured intent, domain-aware workflow, governed execution, independent validation/review), conceptual flow diagram (Intent -> Structured specification -> Domain-aware execution -> Validation evidence -> Reviewable artifact), principles (externalized state, bounded work, tool-aware controls, explicit gates), key-principle line (model is not the only source of state or judge of completion) | grep | 001 | includes present |
| PA-02 | Avoid clean: no raw state diagrams, enforcement paths, internal command/hook names, orchestration sequences | run_test | 001 | 0 hits |
| PA-03 | Pushed; Pages rebuilt | run_code | 002 | push clean |
| PA-04 | L3 GATE: live page shows the section (cache-bust: request with a ?v= query param or verify content-length grew); IP-safety + absolute-claims greps clean on live HTML | run_test | 003 | live green |

## Rules
- READ guide section 6 + current index.html first (RULE ZERO); base copy on guide sample
- Conceptual flow as inline SVG or styled divs, matching the existing Isagawa diagram's visual style
- Any red: fix then /kernel/learn
