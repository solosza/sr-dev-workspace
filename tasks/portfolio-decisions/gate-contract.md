# Gate Contract - 258 Decisions & Trade-offs

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PD-01 | Section per guide 10: the 5-row decision/reason/operational-trade-off table (persist state outside chat; bound work into units; separate mechanical vs semantic checks; controlled integration; adapt by domain) - each row with Decision + Reason + Trade-off/Invariant; responsive table styling | grep | 001 | 5 rows, 3 columns each |
| PD-02 | Avoid clean: no internal enforcement implementation, no universal-optimality claims, no absolute language | run_test | 001 | 0 hits |
| PD-03 | Pushed; Pages rebuilt | run_code | 002 | push clean |
| PD-04 | L3 GATE (cache-busted): live page shows the decisions table; IP-safety + absolute-claims greps clean (check match context - ignore CSS max-width:100%, lessons 255/256) | run_test | 003 | live green |

## Rules
- READ guide section 10 + current index.html FIRST (RULE ZERO); use the guide's exact 5-row table
- Any red: fix then /kernel/learn
