# Step 2: Compile Harness

Transform the empty test repo into a live, governed agent harness. This is compilation — kernel + platform-deepeval + domain-setup — not just file copy. The repo must have protocol, hooks, and enforcement active.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `test-repo` | Output of Step 1 | `D:\my_ai_projects\project_test_repos\eval-check-data-test` |
| `source_path` | Output of Step 0 | `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` |
| `mode` | Output of Step 0 | `artifact` or `harness` |

## Pre-Compilation Checkpoint

Before copying anything, read the reference file lists:

1. **Read kernel file list:**
   → `references/step-02/kernel-file-list.md`
   This defines exactly which kernel files to copy. Do not guess — read the list.

2. **Read deepeval file list:**
   → `references/step-02/deepeval-file-list.md`
   This defines exactly which platform-deepeval files to copy. Do not guess — read the list.

3. **Verify source paths exist:**
   ```bash
   test -d "<kernel-source-path>"
   test -d "<platform-deepeval-source-path>"
   ```
   If either is missing: **ABORT** with message:
   ```
   EVAL ABORT: Required source not found: <path>
   Check kernel and platform-deepeval paths.
   ```

## Procedure

### Phase 1: Copy Kernel Files

Copy every file listed in `references/step-02/kernel-file-list.md` from the kernel source into the test repo. Preserve directory structure.

```bash
# For each file in kernel-file-list.md:
mkdir -p "<test-repo>/<parent-dir>"
cp "<kernel-source>/<file>" "<test-repo>/<file>"
```

Key kernel components:
- `.claude/commands/kernel/` — all kernel commands
- `.claude/hooks/` — gate enforcers, actions log appender, test failure detector
- `.claude/skills/kernel-domain-setup/` — domain-setup skill (required for compilation)
- `.claude/skills/autonomous-cycling/` — task execution
- `.claude/lessons/` — lessons template
- `.claude/state/` — fresh state files
- `run-task.sh` — task execution script
- `CLAUDE.md` — kernel CLAUDE.md

### Phase 2: Copy Platform-DeepEval Files

Copy every file listed in `references/step-02/deepeval-file-list.md` from platform-deepeval into the test repo. Preserve directory structure.

```bash
# For each file in deepeval-file-list.md:
mkdir -p "<test-repo>/<parent-dir>"
cp "<platform-deepeval-source>/<file>" "<test-repo>/<file>"
```

Key platform-deepeval components:
- `.claude/skills/deepeval-management-layer/` — skill, workflow, gate-contract, steps, references
- `framework/interfaces/deepeval_interface.py` — DeepEval adapter
- `framework/_reference/` — metrics, tests, tasks, roles, fixtures
- `framework/resources/` — shared resources

### Phase 3: Run Domain Setup

Domain-setup reads the repo, discovers platform-deepeval as the domain spec, and initializes the harness.

```bash
# Inside the test repo, invoke domain-setup via claude -p
claude -p "Read .claude/skills/kernel-domain-setup/SKILL.md and execute domain-setup for this repo" --cwd "<test-repo>"
```

Domain-setup will:
1. Discover repo structure
2. Recognize platform-deepeval as the domain spec
3. Create protocol for the test repo
4. Wire hooks in `settings.local.json`
5. Initialize state files (`session_state.json`, workflow JSON)

### Phase 4: Post-Compilation Verification

After domain-setup completes, verify the harness is live:

| ID | Check | Command | Pass |
|----|-------|---------|------|
| G2.1 | Protocol exists | `test -f "<test-repo>/.claude/protocols/"*.md` | File present |
| G2.2 | Hooks wired | `grep -q "hook" "<test-repo>/.claude/settings.local.json"` | Hook entries found |
| G2.3 | State initialized | `test -f "<test-repo>/.claude/state/session_state.json"` | File present |
| G2.4 | Domain-setup complete | `grep -q "setup_complete" "<test-repo>/.claude/state/"*workflow*.json` | `true` |

All 4 checks must pass. If any fail, see Error Handling.

## Error Handling

| Failure | Action |
|---------|--------|
| Kernel source path missing | Abort — kernel must exist at known path |
| Platform-deepeval source missing | Abort — platform-deepeval must exist at known path |
| File copy fails (permission/disk) | Check permissions, disk space. Retry once. |
| Domain-setup fails | Capture error output. Check: missing files in copy (re-read file lists, copy missing). Retry domain-setup once. |
| Domain-setup succeeds but verification fails | Read what domain-setup produced. If protocol missing, check if domain spec was detected. If hooks missing, check settings.local.json format. Fix and retry once. |
| Still failing after retry | Set `failed` state with `resume_step: 2`. Invoke `/kernel/learn`. |

## Critical Distinction

This step produces a **compiled harness**, not a file collection. The difference:

| File collection | Compiled harness |
|-----------------|------------------|
| Files exist in directories | Protocol governs agent behavior |
| No enforcement | Hooks block violations |
| No state tracking | State machine tracks progress |
| No learn loop | Failures captured and learned from |

If verification passes but the agent inside can't run with governance, the compilation failed.

## Output

- Fully compiled agent harness at `<test-repo>/`
- Protocol, hooks, state all initialized and active
- State transition: `creating_repo` → `compiling_harness` → ready for Step 3
- Contract: → `contracts/step-02-contract.json`
