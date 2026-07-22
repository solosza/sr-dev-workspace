# Test: Contract Semantics (AST)

## Type
TEST
## Execution
inline
## Dependencies
- 002

## Requirements
- AST-based semantics script per lessons #38/#39/#43: parse the exemplar; EXCLUDE docstrings from all string checks; body-scoped rules iterate `fn.body` per-statement (NEVER `ast.walk(fn)` — decorators false-positive); dynamic locator/testid checks normalize `{placeholder}` ↔ Jinja before comparing
- Checks: (a) no try/except in tests outside doc-sanctioned `pytest.raises`; (b) one AAA block per test method; (c) asserts carry failure messages; (d) acts only through Task/Role layer (no page-object action calls, no Interface calls, no locators in test bodies); (e) no screenshot calls in test bodies; (f) same-instance assertion rule (page object used to assert is the instance the Task consumed — fixture identity)
- Extended lexicon grep per lesson #45 over the shipped files: hmsa, healthcare, claim, patient, member, subscriber, eligib*, EOB, remittance, diagnosis, provider(-as-insurer), autopend, DRG, PCN, 837 — zero hits
- Script failure = fix the CODE or the SCRIPT per the false-positive decision pattern (lessons #39/#43) — verify against the actual AST nodes before declaring the code non-compliant

## Acceptance Criteria
- [ ] AST semantics script runs exit 0 against the exemplar
- [ ] Extended lexicon grep clean

## Gates Satisfied
- UT-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
