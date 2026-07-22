# Task 003: L1 — Structure + Clean-Room + Lexicon

**Type:** TEST (L1) | **Gates:** SI3-02, SI3-03, SI3-04

## Action

Run ONE Python verification script (absolute paths, no cd):

1. File exists on the 215 branch; py_compile
2. AST: every method from the design doc's Method Surface section present with matching signatures; no `pyodbc`/`sqlalchemy` imports
3. AST: no f-string/`%`/.format-constructed SQL passed to execute calls (docstring-excluded, body-scoped — lessons #39/#44)
4. Extended vocab lexicon over the branch diff: 0 hits
5. Design-doc cross-check: parse the doc's method table and diff against the AST surface — report any missing/extra public method

## Acceptance

Exit 0, per-check PASS lines. Red → fix → /kernel/learn.
