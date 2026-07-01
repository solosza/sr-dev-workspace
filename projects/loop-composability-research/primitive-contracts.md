# Primitive Loop Entry/Exit Contracts

Research for backlog 155 — Loop Composability.

---

## 1. Execute Pipeline

**Identity:** Outer orchestrator. Takes a goal or backlog number and runs the full autonomous pipeline.

### Entry Contract
| Requirement | Source |
|-------------|--------|
| Natural language goal OR backlog file path OR backlog number | User input (argument) |
| `session_state.json` readable | Kernel state |
| Kernel loop active (session-start + anchor done) | Kernel governance |
| No existing `pipeline_state.resume_step` (or resume from it) | `session_state.json` |

### Exit Contract
| Artifact | Location |
|----------|----------|
| Backlog item (created or pre-existing) | `docs/backlog/NNN-*.md` |
| Task folder with numbered tasks + gate contract | `tasks/[project-name]/` |
| All tasks executed via run-task.sh | One-shot `claude -p` per task |
| Validation report | `tasks/[project-name]/_test/validation-report.json` |
| `pipeline_state` cleared from session_state.json | `session_state.json` |

### State Isolation
| File | Access | Notes |
|------|--------|-------|
| `session_state.json` | Read/Write | Stores `pipeline_state`, `pipeline_mode` flags |
| `[domain]_workflow.json` | Read/Write | Anchor counter, cycling state |
| `tasks/[project-name]/` | Write | Creates task folder and all task files |
| `docs/backlog/NNN-*.md` | Write (optional) | Creates backlog if natural language input |

### Error Modes
| Failure | State Left |
|---------|-----------|
| Backlog creation fails | `pipeline_state.input_mode` set, no task folder |
| Task-builder fails mid-decomposition | Partial task files in `tasks/[project-name]/` |
| run-task.sh fails on a task | `completed_tasks` partially populated, task marked failed |
| Validation fails | Report exists with failures noted |

### Composability Notes
- Already acts as an outer loop (calls task-builder internally, spawns run-task.sh)
- Primary candidate for orchestrating inner loops
- State coupling: writes `pipeline_state` and `pipeline_mode` into shared `session_state.json`

---

## 2. Task Builder

**Identity:** Decomposition engine. Takes a goal and produces atomic task files + gate contract.

### Entry Contract
| Requirement | Source |
|-------------|--------|
| Goal text (natural language or backlog content) | Caller (execute-pipeline or user) |
| `session_state.json` readable | Kernel state |
| Optional: `pipeline_mode` flags (`skip_plan_review`, `no_execute`) | Set by execute-pipeline |
| Optional: existing task folder with files (resume cycling) | Filesystem |

### Exit Contract
| Artifact | Location |
|----------|----------|
| `000-index.md` with task index | `tasks/[project-name]/` |
| `gate-contract.md` with 5-column verification spec | `tasks/[project-name]/` |
| Numbered task files (`001-*.md` through `NNN-*.md`) | `tasks/[project-name]/` |
| `_context/` with template resolution (if platform build) | `tasks/[project-name]/_context/` |
| `_test/` with fixtures + validation report | `tasks/[project-name]/_test/` |
| All BUILD tasks implemented, TEST tasks verified | In-session or via run-task.sh |

### State Isolation
| File | Access | Notes |
|------|--------|-------|
| `session_state.json` | Read | Reads `pipeline_mode`, `resume_step` |
| `tasks/[project-name]/` | Write | Creates all task artifacts |
| Domain protocol | Read | Convention check references protocol |

### Error Modes
| Failure | State Left |
|---------|-----------|
| Parse fails | No task folder created |
| Research/convention check fails | Partial analysis, no tasks written |
| Template resolution fails | `_context/` may be partial |
| Task execution fails | `completed_tasks` partial, validation report shows failures |

### Composability Notes
- Currently called by execute-pipeline (step 3)
- Pure decomposition + execution — no state pollution beyond task folder
- Could be called by any outer loop that needs task decomposition
- The `pipeline_mode` flags are its only coupling to execute-pipeline

---

## 3. Production Test (prod-test)

**Identity:** Validation engine. Takes a deliverable repo and runs L1/L2/L3 tests in an isolated copy.

### Entry Contract
| Requirement | Source |
|-------------|--------|
| `source_repo_path` — path to deliverable repo | User input (argument) |
| Repo must contain code + domain spec (or be buildable) | Filesystem |
| Kernel must be available for copy into master | `D:\my_ai_projects\isagawa-kernel` |

### Exit Contract
| Artifact | Location |
|----------|----------|
| Master repo (golden copy with kernel) | `[source]-master/` |
| Test repo (disposable copy with results) | `[source]-test/` |
| Validation report | `[source]-test/_test/validation-report.json` |
| Test infrastructure torn down | Docker/mock cleanup |

### State Isolation
| File | Access | Notes |
|------|--------|-------|
| `session_state.json` | Minimal read | Checks kernel state but operates mostly independently |
| `[source]-master/` | Write | Creates master repo externally |
| `[source]-test/` | Write | Creates disposable test repo externally |
| Inner `run-task.sh` state | Write | State files inside test repo (isolated from parent) |

### Error Modes
| Failure | State Left |
|---------|-----------|
| Master assembly fails | Partial `[source]-master/`, no test repo |
| Domain-setup fails in master | Master exists but no protocol/hooks |
| Copy fails | Master exists, no test repo |
| Inner test fails | Test repo has partial results, validation report shows failures |
| Infra setup fails | No test target running |

### Composability Notes
- **Already composable** — documented composability matrix (standalone, task-builder step 7, audit, CI)
- Operates on external repos — state isolation is inherent (master/test repos are separate filesystem trees)
- Does not write to parent's `session_state.json` or `workflow.json`
- Best example of a composable primitive in the current kernel

---

## 4. Domain Setup

**Identity:** Bootstrap engine. Discovers a repo and builds protocol + hooks + commands.

### Entry Contract
| Requirement | Source |
|-------------|--------|
| Target repo with code to analyze | Filesystem |
| No existing domain (one project = one domain) | Domain persistence rule |
| Optional: `resume_step` for mid-skill resume | `session_state.json` |

### Exit Contract
| Artifact | Location |
|----------|----------|
| Protocol file | `.claude/protocols/[domain]-protocol.md` |
| Lessons folder | `.claude/lessons/` |
| Commands wrapped for kernel loop | `.claude/commands/kernel/` |
| Hook files | `.claude/hooks/` |
| State files initialized | `.claude/state/` |
| `needs_restart: true` | `session_state.json` |

### State Isolation
| File | Access | Notes |
|------|--------|-------|
| `session_state.json` | Read/Write | Sets `needs_restart`, `resume_step`, domain |
| `[domain]_workflow.json` | Write | Creates initial workflow state |
| `.claude/protocols/` | Write | Creates protocol |
| `.claude/hooks/` | Write | Creates enforcement hooks |
| `.claude/settings.local.json` | Write | Registers hooks |

### Error Modes
| Failure | State Left |
|---------|-----------|
| Prerequisites missing | No artifacts created |
| Mid-discovery failure | Partial protocol, `resume_step` saved |
| Hook creation fails | Protocol exists but hooks not registered |
| Restart not performed | `needs_restart: true`, hooks inactive |

### Composability Notes
- **Tightly coupled to bootstrap** — designed to run once per repo
- Currently called by prod-test (step 3: validate master)
- Not composable in the loop sense — it's a one-shot setup, not a repeatable loop
- Could theoretically be called as an inner loop for "set up a new workspace" tasks

---

## 5. Autonomous Cycling

**Identity:** Execution engine. Loops through numbered tasks in a folder.

### Entry Contract
| Requirement | Source |
|-------------|--------|
| `cycling: true` in `[domain]_workflow.json` | Set by `/kernel/autonomous-cycle` or session-start |
| Task folder with numbered task files | `tasks/[folder]/` |
| `task_folder` set in workflow state | `[domain]_workflow.json` |
| Kernel loop active (anchored) | Kernel governance |

### Exit Contract
| Artifact | Location |
|----------|----------|
| All tasks completed or skipped (after 3 attempts) | Task files implemented |
| `completed_tasks` populated | `[domain]_workflow.json` |
| `cycling_complete: true` | `[domain]_workflow.json` |
| Lessons recorded for any failures | `.claude/lessons/` |

### State Isolation
| File | Access | Notes |
|------|--------|-------|
| `[domain]_workflow.json` | Read/Write | `cycling`, `completed_tasks`, `skipped_tasks`, `current_task`, `attempts_on_current` |
| `session_state.json` | Read/Write | Context, actions_log |
| Task files | Read | Reads task instructions |
| Deliverable files | Write | Implements task deliverables |

### Error Modes
| Failure | State Left |
|---------|-----------|
| Task fails 3 times | Task added to `skipped_tasks`, lesson recorded, cycling continues |
| Anchor required mid-cycle | Hook blocks, `/kernel/anchor` invoked, cycling resumes |
| Context compaction | `context` in session_state survives, cycling resumes from `current_task` |

### Composability Notes
- Pure execution loop — no opinion on what it's cycling through
- Already used as inner execution within execute-pipeline (step 4 spawns run-task.sh which cycles)
- State coupling: writes heavily to `[domain]_workflow.json` (cycling fields)
- If used as inner loop, the `cycling` and `completed_tasks` fields would collide with outer loop state

---

## 6. Audit Workflow

**Identity:** Diagnostic engine. Scans infrastructure for gaps and auto-fixes.

### Entry Contract
| Requirement | Source |
|-------------|--------|
| Kernel infrastructure exists (protocol, hooks, commands, skills) | Filesystem |
| Kernel loop active | Kernel governance |

### Exit Contract
| Artifact | Location |
|----------|----------|
| Findings report (or "clean") | Output to user |
| Fix tasks generated (if findings) | `tasks/` |
| Fix tasks executed | Auto-cycled |

### State Isolation
| File | Access | Notes |
|------|--------|-------|
| `.claude/commands/kernel/` | Read | Scans command registration |
| `.claude/skills/` | Read | Scans skill structure |
| `.claude/hooks/` | Read | Scans hook wiring |
| `.claude/protocols/` | Read | Scans protocol completeness |
| `.claude/state/` | Read | Scans state consistency |
| `.claude/lessons/` | Read | Scans lesson index |
| `session_state.json` | Read/Write | Minimal — context updates |

### Error Modes
| Failure | State Left |
|---------|-----------|
| Scan step fails | Partial findings, later steps may still run |
| Fix task generation fails | Findings reported but not auto-fixed |
| Fix task execution fails | Standard cycling error handling (3 attempts) |

### Composability Notes
- Read-heavy, write-light — scans then generates tasks
- Could be called as inner loop for "verify infrastructure" steps in any pipeline
- Low state coupling — mostly reads, only writes fix tasks
- Currently standalone only

---

## Cross-Cutting Patterns

### Pattern 1: State Coupling Spectrum

| Primitive | State Coupling | Composability |
|-----------|---------------|---------------|
| **prod-test** | Low (external repos) | **High** — already composable |
| **audit-workflow** | Low (mostly reads) | **High** — safe as inner loop |
| **task-builder** | Medium (`pipeline_mode` flags) | **Medium** — needs flag isolation |
| **domain-setup** | High (creates infrastructure) | **Low** — one-shot bootstrap |
| **execute-pipeline** | High (orchestrator) | **Low** — IS the outer loop |
| **autonomous-cycling** | High (workflow state) | **Medium** — needs state scoping |

### Pattern 2: Already-Composable Primitives

Prod-test is the gold standard — it operates on external filesystem trees, doesn't write to parent state, and has a documented composability matrix. Any primitive aspiring to composability should follow this pattern: **operate on isolated state, return results to caller, don't mutate shared state.**

### Pattern 3: State Collision Risk

The main risk for inner loops is **workflow state collision**. If cycling runs as an inner loop inside execute-pipeline, both write to `[domain]_workflow.json`:
- `cycling`, `completed_tasks`, `current_task` — inner loop values overwrite outer loop values
- `actions_since_anchor` — inner actions count against outer anchor budget
- `anchored` — inner anchor resets outer anchor state

**Current mitigation:** Per-agent workflow state files (`agent-{id}-workflow.json`) already exist for parallel agents. This same pattern could scope inner loop state.

### Pattern 4: Entry Contract Uniformity

All primitives share a common entry pattern:
1. Check `session_state.json` for resume state
2. Verify kernel governance is active
3. Accept a primary input (goal, path, folder)

This suggests a **standard invocation interface** could be defined without changing primitive internals.

### Pattern 5: Exit Contract as Return Value

Each primitive produces artifacts at known locations. An outer loop could:
1. Invoke the inner primitive
2. Read its exit artifacts (validation report, task folder, etc.)
3. Use exit status to decide next action

This is already how execute-pipeline uses task-builder (step 3 produces tasks, step 4 consumes them).
