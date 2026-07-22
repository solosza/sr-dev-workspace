# Gate Contract — Orchestrator/Subagent Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| OSR-01 | Current-state map exists | file_exists | `projects/orchestrator-subagent-research/01-current-state.md` | Re-run 001 |
| OSR-02 | Map engages the lessons | grep | `grep -c "2026-04-04\|2026-06-14" 01-current-state.md` ≥ 2 | Task 001 must cite the recorded history |
| OSR-03 | Survey exists + sourced | grep | `grep -c "http" 02-industry-survey.md` ≥ 6 | Re-run 002 — claims must be sourced |
| OSR-04 | Matrix exists | file_exists | `projects/orchestrator-subagent-research/03-recommendation-matrix.md` | Re-run 003 |
| OSR-05 | Matrix covers named commands | grep | `grep -ciE "gap-check|eval|audit-workflow|task-builder|project-run" 03-recommendation-matrix.md` ≥ 4 | Task 003: cover the named candidates |
| OSR-06 | Report exists with lesson verdict | grep | `grep -ciE "amend|keep|revise" research-report.md` ≥ 1 AND contains a decision-criterion section | Re-run 004 — must take a position |

## Requirements Coverage
Backlog 230: current-state honesty → OSR-01/02; industry survey → OSR-03; per-command matrix → OSR-04/05; explicit verdict + generic criterion → OSR-06.
