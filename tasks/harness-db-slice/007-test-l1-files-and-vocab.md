# Task 007: L1 — Files Exist + Vocab Lexicon Clean

**Type:** TEST (L1) | **Gates:** DB-07

## Action
Run ONE Python verification script (absolute paths, no cd):
1. On branch `build/214-qa-build-harness-db-slice`: all 5 artifacts exist (compose, schema.sql, sp.sql, db.py changed, init_sqlserver.py)
2. Extended lexicon grep over `git diff main --name-only` files: hmsa, healthcare, claim, patient, member, subscriber, eligib, EOB, remittance, diagnosis, autopend, DRG, PCN, 837 — 0 case-insensitive hits (skip binary)
3. DB-01 branch check

## Acceptance
Script exit 0, per-check PASS lines. Red → fix → /kernel/learn.
