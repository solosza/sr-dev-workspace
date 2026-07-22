# Gate Contract — _reference Pages

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` on branch build/204-qa-build-reference-pages

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PAG-01 | Feature branch current | run_code | branch --show-current → build/204-qa-build-reference-pages | Re-run 001 |
| PAG-02 | Four page files exist | file_exists | login_page.py, customers_page.py, orders_page.py, order_detail_page.py under framework/_reference/pages/ | Re-run 002-005 |
| PAG-03 | Locators bind to real DOM | run_code | every data-testid referenced in page constants exists in harness/orderly/templates/*.html — zero invented selectors | Fix locators |
| PAG-04 (semantics) | No exception handling above L1 | grep | `grep -c "except\|try:" pages/*.py` == 0 (L2 never catches — contract rule 2) | Strip handlers |
| PAG-05 (semantics) | No decorators; no screenshots; no waits-in-actions | grep | `@` decorator count == 0 (excluding nothing); `screenshot` count == 0; action methods contain no WebDriverWait/wait calls (waits are separate methods) | Fix violations |
| PAG-06 (semantics) | Return-self chaining + state-check returns | run_code | python inspection: every atomic method's return annotation/behavior is self; state-checks (is_/has_/get_) return bool/primitive | Fix signatures |
| PAG-07 | Live against Orderly (L3) | run_code | headless Chrome + live Orderly: LoginPage.navigate→enter→click→ CustomersPage/OrdersPage state-checks return True on real pages — exit 0; L3-BLOCKED honestly if env broken | Fix or stop |
| PAG-08 | Committed, clean, main untouched | run_code | commit on branch; porcelain empty; main unchanged | Re-run 008 |

## Requirements Coverage
2.1.1 design doc structure → PAG-02/06; real-DOM binding (no invented selectors) → PAG-03; **lesson 2026-07-15 contract-semantics gates → PAG-04/05/06**; L3 completeness → PAG-07.
