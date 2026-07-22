# Gate Contract — _reference Shared Components

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` on branch build/205-qa-build-reference-components

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| CMP-01 | Feature branch current | run_code | branch --show-current → build/205-qa-build-reference-components | Re-run 001 |
| CMP-02 | Exactly two components | run_code | components/ contains modal_component.py + grid_component.py and NOTHING else (deferred-set rule) | Remove extras / add missing |
| CMP-03 | Mechanics-only (no identifier values) | run_code | AST: no string literal in either component contains "data-testid='<concrete-value>'" — identifiers arrive via injected config dataclasses only | Strip embedded values |
| CMP-04 (semantics) | L2 rules, AST-based per lesson #39 | run_code | AST with docstrings excluded: zero try/except, zero decorators, zero screenshot CALLS; atomic methods return self (by execution with stub); genericity scope declared (`SCOPE = 'universal'` or `'library:x'` constant) | Fix violations |
| CMP-05 | Configs wire from page constants | run_code | GridLocators/ModalLocators instantiable from orders_page.py's constants without modification | Reconcile config shapes |
| CMP-06 | Live against Orderly (L3) | run_code | headless Chrome + live Orderly: GridComponent(browser, config from orders_page).find_row_by_values on a SEEDED order id → correct row; click_row navigates to detail; ModalComponent opens delete modal + cancel closes it — exit 0; L3-BLOCKED honestly if env broken | Fix or stop |
| CMP-07 | Committed, clean, main untouched | run_code | commit on branch; porcelain empty; main unchanged | Re-run 007 |

## Test-Script Requirements (lesson #39 — MANDATORY method)
Semantics checks MUST: parse with `ast`, exclude docstrings (ast.get_docstring nodes), detect try/except via ast.Try, decorators via decorator_list, screenshot via ast.Call/Attribute names (not source grep); dynamic locator templates normalized `{placeholder}` ↔ `{{ jinja }}` before template comparison. String-grep semantics checks are BANNED.
