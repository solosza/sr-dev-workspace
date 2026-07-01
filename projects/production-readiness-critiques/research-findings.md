# Production Readiness Critiques — Research Findings

**Backlog:** 145-kernel-research-production-readiness-critiques
**Date:** 2026-06-22
**Source:** External review of backlog sweep 003-140 execute-pipeline run

---

## Critique 1: State Contention

### VERDICT: PARTIALLY TRUE — designed solution exists, not yet wired into execute-pipeline

### Evidence

**The problem is real and documented.** During the backlog sweep, background agent 128 overwrote the main session's `context` field in `session_state.json`. The `state-contention.md` lesson (2026-04-23) and `multi-agent orchestration` lesson (2026-06-14) both document this exact issue.

**Existing mitigations (already in code):**

1. **`one_shot` guard in universal-gate-enforcer.py** (lines 196-252): When `one_shot: true`, the hook skips Gates 3 (anchor), 4 (counter increment), and 5 (token). This prevents sub-agents spawned by `run-task.sh` from invalidating the parent's anchor state. This works well for sequential `run-task.sh` execution.

2. **`pre_init_state` in run-task.sh** (line 289): Sets `session_started=True,one_shot=True` before each claude -p invocation. This tags sub-agents as one-shot, activating the guard above.

3. **Lock file in run-task.sh** (lines 47-64): Prevents concurrent `run-task.sh` invocations on the same task folder.

4. **`spawn-agent-swarm` skill** (step-02-create-manifest.md): Has per-agent state isolation designed — each agent gets `agent-{N}-state.json` instead of writing to shared state. Monitor aggregates from per-agent files.

**The gap:** The `spawn-agent-swarm` per-agent isolation pattern exists in the skill spec but was NOT used during the backlog sweep. The sweep used direct `Agent` tool calls (not spawn-agent-swarm), so background agents wrote to the shared `session_state.json`. The isolation pattern is designed but not integrated into the general parallel-agent workflow.

**Actual impact in the sweep:** Cosmetic only. Agent 128 overwrote the `context` field, but:
- No work was lost (agents were building in separate repos/branches)
- No agent missed a task or duplicated work
- The overwrite was detected and noted (not silently ignored)
- The `one_shot` guard on hooks prevented the more severe contention (anchor/counter corruption)

### Fix Required: YES (small scope)

The per-agent state pattern in `spawn-agent-swarm` should be the default when spawning parallel Agent tool calls from execute-pipeline. Specifically:
- When execute-pipeline spawns parallel agents, each should write to `agent-{backlog-N}-state.json`
- The parent session's `session_state.json` context should be protected (only the parent writes to it)
- This is a wiring fix (connect existing pattern to existing workflow), not a design problem

**Effort:** Small. The pattern exists. It needs to be applied.

---

## Critique 2: Independent Verification (Self-Reported)

### VERDICT: PARTIALLY TRUE — prod-test IS independent verification, but no CI exists

### Evidence

**The reviewer underestimated what already exists:**

1. **Prod-test IS independent verification.** The prod-test skill:
   - Copies the source repo to a disposable test repo (separate directory)
   - Resets workflow state (clean slate)
   - Runs tests via inner `run-task.sh` — which spawns separate `claude -p` sessions
   - Each test task is a fresh agent with no memory of the build
   - Produces a validation report (`_test/validation-report.json`)
   - This is NOT self-reported — it's a separate agent evaluating the deliverable

2. **Git verification is external.** The sweep checked `git log --oneline`, `git show --stat`, file counts — these are external tools confirming artifacts exist and match expectations. Git doesn't lie about commit contents.

3. **pytest runs are external.** Backlog 007's tests (18 pytest tests) ran independently of the build agent.

**What's genuinely missing:**

1. **No CI/CD.** Zero GitHub Actions workflows in any repo. No automated test runs on push/PR. The kernel repo has no `.github/workflows/` directory.

2. **No reproducible replay.** There's no "run this command and get the same result" script. The sweep was orchestrated by the agent in real-time, not by a deterministic script.

3. **Validation reports are task-scoped, not repo-scoped.** Each prod-test run produces a report, but there's no aggregate "repo health" dashboard or persistent test history.

### Fix Required: YES (medium scope)

- Add GitHub Actions CI to `isagawa-kernel` (pytest on push, lint on PR)
- The validation report from prod-test should be committed alongside deliverables as proof-of-test
- Consider: a `/kernel/ci-setup` command that auto-generates GitHub Actions from the domain's test structure

**Effort:** Medium. CI is standard infrastructure, not novel engineering.

---

## Critique 3: External Reproducibility

### VERDICT: TRUE — the kernel itself is portable, but the workspace is not

### Evidence

**The kernel IS portable by design:**
- All commands, skills, hooks, and references use relative paths (`.claude/commands/...`, `.claude/skills/...`)
- Hooks reference `STATE_DIR = Path('.claude/state/')` — relative to repo root
- `run-task.sh` uses `$(cd "$(dirname "$0")" && pwd)` to resolve script dir, then relative paths
- `IS_WINDOWS` detection exists in `common.sh` (line 8-10) — cross-platform awareness built in
- The `universal-gate-enforcer.py` uses `Path('.claude/state/')` — relative
- Domain-setup generates everything from scratch — new user runs `/kernel/domain-setup` and gets protocol, hooks, state

**Hardcoded paths in the kernel repo (4 instances):**
- All in `cross-repo-delegation.md` — a reference file with example paths, not executable code
- These are documentation examples, not functional dependencies

**Where reproducibility breaks:**
1. **The sr_dev_workspace** has hardcoded paths everywhere — but that's the AUTHOR'S workspace, not the kernel itself. The workspace protocol (`sr_dev-protocol.md`) references `D:\my_ai_projects\...` because it was generated by domain-setup for this specific machine.

2. **Backlogs reference local repos** (e.g., backlog 010 needs `platform-deepeval-spec` at a specific path). This is inherent to multi-repo development, not a kernel design flaw.

3. **No "getting started" test.** There's no script that validates: clone kernel → drop in repo → run domain-setup → verify hooks work. The README explains the concept but doesn't provide a one-command verification.

4. **No integration test repo.** There's no public "example repo" where someone can see the kernel in action, clone it, and try it themselves.

### Fix Required: YES (medium scope)

The kernel itself needs:
- A "getting started" example repo (e.g., `isagawa-co/kernel-example`) pre-configured with a simple domain
- A verification script: `./verify-kernel.sh` that confirms hooks, state, and commands are functional
- The README could add a "Quick Start" section: clone, drop kernel, run domain-setup, verify

The workspace hardcoded paths are correct behavior — they're generated per-machine by domain-setup. That's the design working as intended.

**Effort:** Medium. Example repo + verification script + README update.

---

## Summary

| Critique | Verdict | Fix Required | Effort |
|----------|---------|--------------|--------|
| State contention | PARTIALLY TRUE | Wire existing per-agent isolation into execute-pipeline | Small |
| Independent verification | PARTIALLY TRUE | Add CI (GitHub Actions), commit validation reports | Medium |
| External reproducibility | TRUE | Example repo, verification script, README quickstart | Medium |

**Key insight:** Two of three critiques have partial solutions already designed or implemented — they're integration/wiring problems, not fundamental architecture gaps. The third (reproducibility) is the most impactful for public credibility and the easiest to validate externally.

**Recommended priority order:**
1. External reproducibility (highest visibility, proves the system works for others)
2. CI setup (standard engineering practice, builds trust)
3. State isolation wiring (lowest external visibility, but prevents future bugs at scale)
