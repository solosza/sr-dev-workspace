# Production Test Baseline — General Purpose

**Version:** 1.0
**Created:** 2026-03-24
**Status:** Baseline — adapt per project

---

## Overview

General-purpose workflow for production-testing any deliverable built with the Isagawa kernel. Uses a master repo → test repo copy pattern. All tests run inside a disposable test repo via spawned agents.

Works for: QA platforms, CLI tools, APIs, libraries, domain specs, scripts — anything with testable output.

## Architecture

```
MASTER REPO (golden copy)
  ├── src/                ← deliverable code (any structure)
  ├── .claude/            ← domain spec + kernel
  ├── run-task.sh         ← task runner
  └── CLAUDE.md           ← kernel bootstrap
         │
         │  copy
         ▼
TEST REPO (disposable)
  ├── src/                ← same code
  ├── .claude/            ← same kernel (protocol + hooks pre-built)
  ├── run-task.sh         ← same runner
  ├── tasks/prod-test/    ← test task files
  └── _test/              ← test infra + fixtures + reports
```

The master is the **golden copy** — kernel fully configured (domain-setup already run, protocol + hooks in place). Copying gives the test repo a ready-to-go environment.

## Execution Model

```
orchestrator-repo/run-task.sh (outer)
  └── spawned agent per task (linear, one at a time)
        ├── MASTER phase: assemble master repo
        ├── VALIDATE phase: verify kernel setup
        ├── COPY phase: master → test repo
        ├── INFRA phase: set up test target (Docker, mock server, etc.)
        └── TEST phase: run test-repo/run-task.sh (inner)
              └── inner agents run L1/L2/L3 tests inside test repo
```

- **Linear execution** — one agent at a time, no parallelism
- **Two levels** — outer orchestrates setup, inner runs tests
- **No manual intervention** — fully automated end to end

### Commands

```bash
# Outer: orchestrate from your workspace
./run-task.sh [orchestrator_repo] [max_iterations] [task_folder]

# Inner: tests inside test repo (invoked by an outer task)
./run-task.sh [test_repo_path] [max_iterations] prod-test
```

### Personas

| Persona | Role | Where |
|---------|------|-------|
| **Outer spawned agent** | Builds master, copies, sets up infra, kicks off inner tests | orchestrator repo |
| **Inner spawned agent** | Executes test tasks under kernel enforcement | test repo |
| **run-task.sh** | Spawns agents sequentially, handles retries | both levels |
| **User** | Kicks off outer script, reviews report | orchestrator repo |

## Phases

```
MASTER → VALIDATE → COPY → INFRA → TEST → REPORT → CLEANUP
```

| Phase | Purpose | Where | Required? |
|-------|---------|-------|-----------|
| MASTER | Assemble golden master: code + kernel + domain spec + scripts | master repo | Yes |
| VALIDATE | Run domain-setup, verify protocol + hooks + commands | master repo | Yes |
| COPY | Copy master → fresh test repo | filesystem | Yes |
| INFRA | Set up test target (Docker, mock server, test data, etc.) | test repo | If needed |
| TEST | Run L1/L2/L3 via inner run-task.sh | test repo | Yes |
| REPORT | Aggregate results into validation-report.json | test repo | Yes |
| CLEANUP | Tear down test infra | test repo | If INFRA used |

### Phase Details

**MASTER** — What goes in:
- Deliverable code (any directory structure)
- Kernel files: CLAUDE.md, `.claude/commands/kernel/`, `.claude/hooks/`
- Domain spec: `.claude/skills/[domain]/`
- Shell scripts: `run-task.sh`, `run-task-batch.sh`

**VALIDATE** — What to check:
- Protocol file exists in `.claude/protocols/`
- Hooks registered in `.claude/settings.local.json`
- Kernel commands present (session-start, anchor, complete)

**INFRA** — Depends on deliverable type:

| Deliverable | Test Target |
|-------------|-------------|
| SSH/network tool | Docker container with service exposed |
| Web UI | Docker + Playwright/Selenium |
| CLI tool | No infra needed (runs locally) |
| API | Mock server or Docker service |
| Library | No infra needed (import directly) |
| Data pipeline | Test data files in `_test/fixtures/` |

**TEST** — Three levels, all required:

| Level | What | How |
|-------|------|-----|
| L1 Structural | Files exist, patterns present | `test -f`, `grep -q` |
| L2 Functional | Code runs, imports work, unit tests pass | `python -c "import ..."`, `pytest` |
| L3 Production | Deliverable produces correct results against real target | Run the actual code against test target, verify output |

## Task Template

Every task file follows this format:

```markdown
# [Task Name]

## Type
BUILD | TEST

## Executor
Spawned agent via `run-task.sh`

## Action
[One atomic action — what to do]

## Acceptance Criteria
- [ ] [Mechanical check 1]
- [ ] [Mechanical check 2]
```

Rules:
- One task = one action (never bundle)
- Acceptance criteria must be mechanically verifiable
- Inner test tasks use **relative paths** (they run inside the test repo)
- Outer tasks use **absolute paths** (they run in the orchestrator repo)

## L3 Test Pattern

L3 tests exercise the **deliverable directly** — not the domain spec, not mocks:

```python
# Import the actual deliverable code
import sys
sys.path.insert(0, "src/")  # or wherever the code lives

from my_module import MyClass

# Set up with real config pointing to test target
config = load_config("_test/fixtures/test_config.json")

# Run the actual deliverable
result = MyClass(config).execute()

# Assert real results
assert result.status == "success", f"Expected success, got {result.status}"
print(f"PASS: {result.summary}")
```

Key: L3 tests use the **deliverable itself**, not a wrapper or mock. The test proves the code works in a production-like scenario.

## Validation Report Schema

```json
{
  "timestamp": "ISO-8601",
  "project": "[project-name]",
  "target": "[description of test target]",
  "gates": {
    "L1_structural": { "total": N, "passed": N, "failed": N },
    "L2_functional": { "total": N, "passed": N, "failed": N },
    "L2_tests": { "total": N, "passed": N, "failed": N },
    "L3_[component_1]": "pass|fail",
    "L3_[component_2]": "pass|fail"
  },
  "summary": {
    "total_checks": N,
    "total_passed": N,
    "total_failed": N,
    "verdict": "PASS|FAIL"
  }
}
```

## Outer Task Index Template

```
tasks/[project]-prod-test/
├── 000-index.md
│
│   MASTER phase
├── 001-create-master-repo.md
├── 002-copy-code-to-master.md
├── 003-copy-domain-spec-to-master.md
├── 004-copy-kernel-to-master.md
├── 005-copy-shell-scripts-to-master.md
├── 006-write-claude-md.md
│
│   VALIDATE phase
├── 007-run-domain-setup.md
├── 008-verify-protocol.md
├── 009-verify-hooks.md
├── 010-verify-commands.md
│
│   COPY phase
├── 011-copy-master-to-test-repo.md
│
│   INFRA phase (adapt per project)
├── 012-[setup-test-target].md
├── ...
├── NNN-verify-target-reachable.md
│
│   TEST phase
├── NNN-write-inner-test-tasks.md
├── NNN-run-inner-test-batch.md
│
│   REPORT + CLEANUP
├── NNN-collect-validation-report.md
└── NNN-teardown.md
```

## Adapting for a New Project

1. **Copy the outer task structure** — MASTER through CLEANUP phases
2. **Replace the code source** — point to your deliverable's repo
3. **Replace the domain spec** — point to your project's skill directory
4. **Adapt INFRA** — Docker, mock server, test data, or nothing
5. **Write inner test tasks** — L1/L2/L3 specific to your deliverable
6. **Keep the execution model** — outer run-task.sh orchestrates, inner run-task.sh tests
7. **Keep the report schema** — same JSON structure, different gate names

## Reference Implementations

| Project | Location | Notes |
|---------|----------|-------|
| SSH Platform | `tasks/ssh-prod-test/` | Docker + SSH target, 4 validators, 23/23 gates passed |
| QA Platform baseline | `docs/research/qa-platform-prod-test-baseline.md` | QA-specific version |
