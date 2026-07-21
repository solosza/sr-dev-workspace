# Build: Deliverable Barrier Gates in run-task.sh

## Status
Open

## Priority
Medium — 242 verdict is YAH strictly as defense-in-depth under the wave engine; catches the edge cases waves can't model (upstream done but file missing, partial outputs from skipped tasks).

## Summary
Implement the 242 YAH-conditional verdict: gate contracts gain a `## Prerequisites` section (`PRE-*` entries reusing existing gate types `file_exists`/`grep`), and run-task.sh gains a bash `check_prerequisites()` that polls before spawning the one-shot agent — 15-second interval, 120-second timeout (short by design: the wave engine should have ensured availability). Per-agent state exposes WAITING vs RUNNING vs BLOCKED so the swarm monitor never false-positives a waiting agent as stalled. Standalone adoption was explicitly disqualified by the research — this ships only after 247.

## Requirements
- Prerequisite declaration + bash parse rules per `projects/kernel-barrier-gate-research/01-prereq-format.md` (read it — format already chosen)
- `check_prerequisites()` in run-task.sh per `02-wait-loop-design.md`: 15s poll, 120s timeout, timeout → mark BLOCKED in per-agent state and skip per the 3-attempt cycling contract (never abort the whole run)
- WAIT happens in run-task.sh BEFORE agent spawn — the one-shot agent contract is unchanged
- Per-agent state `status` field: WAITING | RUNNING | BLOCKED | COMPLETE; swarm monitor rules updated to treat WAITING as healthy
- Static cycle detection at dispatch complements 247's sort-time detection per `03-deadlock-and-staleness.md`
- L3 test: dispatch a task whose prerequisite appears 30s later (asserts WAITING → RUNNING → COMPLETE), and one whose prerequisite never appears (asserts BLOCKED at 120s, no hang)

## References
- Backlogs done: 242, 243 (combined recommendation: build order 241 → 242, defer 243)
- **Depends on: 247** (wave engine) — the research disqualified standalone adoption
- `run-task.sh`, `.claude/skills/spawn-agent-swarm/references/step-04-monitor.md`

## Task Builder Input
- **Deliverable:** Prerequisites section in gate-contract template + check_prerequisites() in run-task.sh + WAITING state in per-agent files + both L3 tests green
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** BLOCKED until 247 accepted via /kernel/review-queue. Bash-parseable only (grep/sed level, no new tooling). Timeout behavior must never hang the runner.
