# Step 3: Copy Artifact or Repo

Copy the target into the test repo. In **artifact mode**, copy the target artifact + dependencies. In **harness mode**, copy the entire source repo (it IS the artifact).

## Input

| Field | Source | Example |
|-------|--------|---------|
| `mode` | Output of Step 0 | `artifact` or `harness` |
| `target` | Output of Step 0 | `check-data` or `null` |
| `source_path` | Output of Step 0 | `D:\my_ai_projects\project_test_repos\kernel-minimal` |
| `test-repo` | Output of Step 1 | `D:\my_ai_projects\project_test_repos\eval-kernel-minimal-test` |

## Pre-Copy Checkpoint

Read the dependency resolution strategy:
-> `references/step-03/dependency-resolution.md`

### Artifact Mode — Identify artifact type

Search the source repo to classify the target:

| Artifact Type | Detection | What Gets Copied |
|---------------|-----------|-------------------|
| **Command** | `.claude/commands/kernel/<target>.md` exists | command entry, backing skill/, design docs, referenced data |
| **Skill** | `.claude/skills/<target>/SKILL.md` exists | full skill/ tree (SKILL.md, workflow, steps, references, contracts) |
| **Harness** | `.claude/skills/<target>/` + `framework/` | skill/ tree + framework/ interfaces, references, resources |
| **Agent workflow** | `.claude/skills/<target>/workflow.md` only | skill/ tree + state schemas, referenced protocols |

If target matches multiple types (e.g., command backed by skill), copy ALL matched components.
If target matches NONE: **ABORT** with classification failure message.

### Harness Mode — No classification needed

The entire source repo is the artifact. Skip classification.

## Procedure

### Harness Mode

Copy the entire source repo into the test repo, excluding disposable files:

```bash
# Copy everything except .git/, .claude/state/, and prior eval results
rsync -a --exclude='.git/' --exclude='.claude/state/' --exclude='eval/' \
  "<source_path>/" "<test-repo>/harness-under-test/"
```

The source repo is placed under `harness-under-test/` to keep it separate from the test repo's own compiled harness (kernel + platform-deepeval from Step 2). This isolation is critical — the compiled harness governs the eval; the `harness-under-test/` directory is the subject.

**What gets copied in harness mode:**
- `CLAUDE.md` — the harness's agent instructions
- `.claude/commands/` — all commands
- `.claude/skills/` — all skills
- `.claude/hooks/` — all hooks
- `.claude/lessons/` — lessons cheat sheet
- `.claude/settings.local.json` — hook wiring
- `run-task.sh`, `lib/`, `framework/` — scripts and libraries
- `kernel-manifest.json` — if present
- `docs/`, `projects/` — referenced documentation

**What gets excluded:**
- `.git/` — not needed for eval
- `.claude/state/` — runtime state from prior runs
- `eval/` — prior eval results

### Artifact Mode (unchanged)

#### Phase 1: Copy Primary Artifact

Copy the artifact's entire directory tree, preserving structure:

```bash
# Skill tree (if exists):
cp -r "<source_path>/.claude/skills/<target>/" "<test-repo>/.claude/skills/<target>/"

# Command entry point (if exists):
cp "<source_path>/.claude/commands/kernel/<target>.md" "<test-repo>/.claude/commands/kernel/<target>.md"

# Framework components (if harness type):
cp -r "<source_path>/framework/" "<test-repo>/framework/"
```

#### Phase 2: Resolve Dependencies

Scan the copied artifact's files for external references and copy them too:

1. **Scan SKILL.md file index** — every file listed in the File Index table must exist in test repo
2. **Scan step files** — any reference paths (e.g., `projects/...`, `docs/...`) get copied
3. **Scan contracts** — any referenced schemas or data files get copied
4. **Scan for design docs** — if `.claude/docs/design/<target>/` exists in source, copy it

#### Phase 3: Copy Referenced Data

If step files reference data directories, copy those directories.

## What NOT to Copy

- Source repo's `.git/` directory
- Source repo's `.claude/state/` (runtime state)
- Source repo's `eval/` directory (prior eval results)
- **Artifact mode only:** source repo's kernel (test repo has its own from Step 2)
- **Artifact mode only:** other artifacts not referenced by the target

## Verification

### Artifact Mode

| ID | Check | Method | Pass |
|----|-------|--------|------|
| G3.1 | SKILL.md file index | Every file in SKILL.md File Index table exists in test repo | All present |
| G3.2 | Step file references | Every reference path in step files resolves in test repo | All resolve |
| G3.3 | Contract integrity | Every JSON in `contracts/` parses as valid JSON | All parse |
| G3.4 | No broken wikilinks | Scan copied markdown for `→` references, verify targets exist | All resolve |

### Harness Mode

| ID | Check | Method | Pass |
|----|-------|--------|------|
| G3.1h | Harness directory exists | `test -d <test-repo>/harness-under-test/` | Present |
| G3.2h | CLAUDE.md copied | `test -f <test-repo>/harness-under-test/CLAUDE.md` | Present |
| G3.3h | Commands copied | `ls <test-repo>/harness-under-test/.claude/commands/` | Non-empty |
| G3.4h | No .git leaked | `test ! -d <test-repo>/harness-under-test/.git` | Absent |

All checks for the active mode must pass before transitioning to Step 4.

## Error Handling

| Failure | Action |
|---------|--------|
| Target artifact not found in source repo | Abort with classification failure message (see Pre-Copy Checkpoint) |
| Referenced file doesn't exist in source | Log warning and continue — some references may be optional (e.g., future step files) |
| Directory copy fails (permission/disk) | Check permissions, disk space. Retry once. |
| SKILL.md file index has entries that don't exist | Log each missing file. If >50% missing, abort — artifact may be incomplete |
| Contract JSON fails to parse | Log the malformed file. Copy it anyway (test will catch it). |
| Still failing after retry | Set `failed` state with `resume_step: 3`. Invoke `/kernel/learn`. |

## Output

- Self-contained artifact in test repo — every file the LLM would read during execution exists
- State transition: `compiling_harness` → `copying_artifact` → ready for Step 4
- Contract: → `contracts/step-03-contract.json`
