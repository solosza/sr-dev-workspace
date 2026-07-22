# Test: Contract Semantics — AST

## Type
TEST
## Execution
inline
## Dependencies
- 002

## Requirements
- AST-only over the new test file(s): no ast.Try outside pytest.raises contexts; test functions drive Task-layer calls (no interface method calls unless the doc's canonical shows one — cite the doc line if allowing); dual-assertion presence structurally (≥2 assert statements per test path per the doc's definition — read the doc for what "dual" means and check THAT, not a naive count); extended lexicon clean
- Lessons #39/#43 methods; exit non-zero on real violations → fix → /kernel/learn

## Acceptance Criteria
- [ ] Exit 0, checks genuinely executed

## Gates Satisfied
- AT-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
