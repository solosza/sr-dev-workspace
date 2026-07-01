# Gate Contract — Eval Platform Design

## Verification Methods
-> `.claude/skills/task-builder/references/verification-methods.md`

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project directory exists | file_exists | `test -d projects/eval-platform-design/` | Create directory |
| BUILD-02 | Prerequisite gate doc exists | file_exists | `test -f projects/eval-platform-design/prerequisite-gate.md` | Write document |
| BUILD-03 | Prerequisite gate contains verdict | grep | `grep -q 'Verdict:' projects/eval-platform-design/prerequisite-gate.md` | Add verdict section |
| BUILD-04 | Vertical plugin system doc exists | file_exists | `test -f projects/eval-platform-design/vertical-plugin-system.md` | Write document |
| BUILD-05 | Execution pipeline doc exists | file_exists | `test -f projects/eval-platform-design/execution-pipeline.md` | Write document |
| BUILD-06 | BYOK key management doc exists | file_exists | `test -f projects/eval-platform-design/byok-key-management.md` | Write document |
| BUILD-07 | Component curation pipeline doc exists | file_exists | `test -f projects/eval-platform-design/component-curation-pipeline.md` | Write document |
| BUILD-08 | API and frontend doc exists | file_exists | `test -f projects/eval-platform-design/api-and-frontend.md` | Write document |
| BUILD-09 | Multi-tenancy isolation doc exists | file_exists | `test -f projects/eval-platform-design/multi-tenancy-isolation.md` | Write document |
| BUILD-10 | Prerequisite gate references 158 research | grep | `grep -q 'eval-web-app-research' projects/eval-platform-design/prerequisite-gate.md` | Add research references |
| BUILD-11 | Vertical plugin doc references platform-deepeval | grep | `grep -q 'platform-deepeval' projects/eval-platform-design/vertical-plugin-system.md` | Add platform-deepeval references |
| BUILD-12 | Execution pipeline references Cloud Run | grep | `grep -q 'Cloud Run' projects/eval-platform-design/execution-pipeline.md` | Add tech stack references from 158 |
| BUILD-13 | BYOK doc references session-scoped in-memory | grep | `grep -q 'session-scoped' projects/eval-platform-design/byok-key-management.md` | Add key management approach from 158 |
| BUILD-14 | API doc references FastAPI | grep | `grep -q 'FastAPI' projects/eval-platform-design/api-and-frontend.md` | Add tech stack references from 158 |
| BUILD-15 | Multi-tenancy doc references gVisor | grep | `grep -q 'gVisor' projects/eval-platform-design/multi-tenancy-isolation.md` | Add sandboxing references from 158 |
| DOC-01 | All 7 design docs exist | run_code | `ls projects/eval-platform-design/*.md \| wc -l` returns 7 | Write missing documents |
| DOC-02 | Each doc has ## References section | run_code | `for f in projects/eval-platform-design/*.md; do grep -q '## References' "$f" \|\| echo "MISSING: $f"; done` returns empty | Add References sections |
| DOC-03 | Each design doc references at least one 158 research file | run_code | `for f in projects/eval-platform-design/*.md; do grep -q 'eval-web-app-research' "$f" \|\| echo "MISSING: $f"; done` returns empty | Add 158 research references |
| TEST-01 | Cross-doc tech stack consistency | manual | All docs reference the same tech stack decisions (Cloud Run, FastAPI, Next.js, Claude Agent SDK, gVisor) without contradictions | Fix inconsistencies |
| TEST-02 | Cross-doc BYOK model consistency | manual | BYOK approach (session-scoped in-memory) described identically across byok-key-management, execution-pipeline, and multi-tenancy-isolation | Fix inconsistencies |
| TEST-03 | Prerequisite gate conditions carried forward | manual | GO (Conditional) conditions from 158 are explicitly addressed as constraints in relevant design docs | Add missing condition references |

## Requirements Coverage
Each gate maps to a task acceptance criterion. All acceptance criteria have corresponding gates.
- Tasks 001: BUILD-01
- Task 002: BUILD-10, BUILD-03
- Task 003: BUILD-02, BUILD-03, BUILD-10
- Task 004: BUILD-04, BUILD-11
- Task 005: BUILD-05, BUILD-12
- Task 006: BUILD-06, BUILD-13
- Task 007: BUILD-07
- Task 008: BUILD-08, BUILD-14
- Task 009: BUILD-09, BUILD-15
- Task 010: DOC-01, BUILD-02 through BUILD-09
- Task 011: DOC-02, DOC-03
- Task 012: TEST-01, TEST-02, TEST-03
