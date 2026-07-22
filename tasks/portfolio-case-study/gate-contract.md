# Gate Contract - 256 Flagship Case Study

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| CS-01 | Platform state verified at BUILD TIME (not from backlog memory): which of Browser(202-208)/REST(209-213)/SQL-Server(214-219)/SOAP(220-223) backlogs exist in docs/backlog/done/ vs docs/backlog/ (open) in the sr_dev_workspace | run_code | 001 | verified state recorded with evidence |
| CS-02 | Section per guide 8: problem, personal role, solution scope, result, per-interface coverage phrased per VERIFIED state (done/in-progress/planned - no aspirational claims), unified governance high-level, technologies, trade-off box (state checkpointed outside model context window, de-absolutized per v1.2 changelog) | grep | 002 | includes present |
| CS-03 | Avoid clean: no 5-layer contract details, fixture wiring, constructor rules, method-by-method spec; no absolute/guarantee language | run_test | 002 | 0 hits |
| CS-04 | Pushed; Pages rebuilt | run_code | 003 | push clean |
| CS-05 | L3 GATE (cache-busted): live page shows the case study with coverage language matching the task-001 verified state; IP-safety + absolute-claims greps clean | run_test | 004 | live green |

## Rules
- READ guide section 8 + section 13 + current index.html FIRST (RULE ZERO)
- Task 001's verified state is the SOURCE OF TRUTH for task 002's coverage wording - do not phrase from the original backlog text if state has moved on
- Any red: fix then /kernel/learn
