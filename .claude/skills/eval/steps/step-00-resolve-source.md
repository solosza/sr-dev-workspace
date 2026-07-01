# Step 0: Resolve Source + Detect Mode

Parse the input arguments, resolve the source to a local directory, and detect whether this is artifact mode or harness mode.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `args` | Raw arguments from `/kernel/eval` invocation | `D:\path\to\repo` or `domain-setup https://github.com/org/repo` |

## Procedure

### Phase 1: Parse Arguments

Count the arguments:

| Arg Count | Interpretation | Mode |
|-----------|---------------|------|
| 1 arg | Arg is the source (path or URL) | **Harness mode** — `target = null` |
| 2 args | First arg = target name, second arg = source | **Artifact mode** — `target = first arg` |
| 0 args | Missing input | **ABORT** with: `EVAL ABORT: No source provided. Usage: /kernel/eval <source> or /kernel/eval <target> <source>` |

### Phase 2: Resolve Source

Read the source resolution reference for detection rules:
-> `references/step-00/source-resolution.md`

**Detection logic:**

```
if source starts with "http://" or "https://" or contains "github.com":
    → GitHub URL → clone to local path
else:
    → Local path → verify it exists
```

**For GitHub URLs:**

1. Extract repo name from URL (last path segment, strip `.git` suffix)
2. Clone to: `D:\my_ai_projects\project_test_repos\eval-[repo-name]-clone\`
3. If clone dir already exists, delete and re-clone (disposable)
4. Clone with `--depth 1` for speed (shallow clone is sufficient for eval)

```bash
# Example:
git clone --depth 1 "https://github.com/isagawa-co/isagawa-kernel" "D:\my_ai_projects\project_test_repos\eval-isagawa-kernel-clone"
```

**For local paths:**

1. Verify path exists: `test -d "<source>"`
2. If missing: **ABORT** with: `EVAL ABORT: Source path not found: <source>`

### Phase 3: Resolve Test Repo Name

| Mode | Test Repo Name |
|------|---------------|
| **Artifact** | `eval-[target]-test` |
| **Harness** | `eval-[repo-name]-test` |

Where `[repo-name]` is the directory name of the resolved source path (e.g., `kernel-minimal` from `D:\...\kernel-minimal`).

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| G0.1 | Mode detected | `mode` is `artifact` or `harness` | Set |
| G0.2 | Source resolved | Local directory exists at resolved path | `test -d` passes |
| G0.3 | Test repo name resolved | Non-empty string | Set |

All checks must pass before transitioning to Step 1.

## Error Handling

| Failure | Action |
|---------|--------|
| No arguments | Abort with usage message |
| GitHub clone fails (network, auth, repo not found) | Abort with clone error. Do not retry — user should check URL. |
| Local path doesn't exist | Abort with path not found message |
| Ambiguous input (can't determine mode) | Default to harness mode if single arg looks like a path |

## Output

- `mode`: `artifact` or `harness`
- `target`: artifact name or `null`
- `source_path`: resolved local directory path
- `original_source`: original input (URL or path — preserved for reporting)
- `test_repo_name`: name for the test repo directory
- State transition: `init` -> `resolving_source` -> ready for Step 1
