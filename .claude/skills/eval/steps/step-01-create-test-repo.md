# Step 1: Create Test Repo

Create the disposable test repo for this eval run. The repo is recreated each run — if it already exists, delete it first.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `mode` | Output of Step 0 | `artifact` or `harness` |
| `target` | Output of Step 0 | `check-data` (artifact mode) or `null` (harness mode) |
| `source_path` | Output of Step 0 | `D:\my_ai_projects\project_test_repos\kernel-minimal` |
| `test_repo_name` | Output of Step 0 | `eval-check-data-test` or `eval-kernel-minimal-test` |

## Pre-Creation Checkpoint

Step 0 already verified source exists. Additional checks per mode:

1. **Artifact mode — verify target exists in source:**
   - Search for the artifact by name in `.claude/skills/`, `.claude/commands/`, or project root
   - The artifact must have at least one file (SKILL.md, command .md, or source file)
   - If not found: **ABORT** with message:
     ```
     EVAL ABORT: Target artifact "<target>" not found in <source_path>.
     Available artifacts:
     - [list skills from .claude/skills/]
     - [list commands from .claude/commands/]
     ```

2. **Harness mode — verify source has harness structure:**
   - Check for at least one of: `CLAUDE.md`, `.claude/commands/`, `.claude/skills/`, `.claude/hooks/`
   - If none found: **ABORT** with message:
     ```
     EVAL ABORT: No harness structure detected in <source_path>.
     Expected at least: CLAUDE.md, .claude/commands/, .claude/skills/, or .claude/hooks/
     ```

## Procedure

1. **Resolve test repo path:**
   ```
   D:\my_ai_projects\project_test_repos\<test_repo_name>\
   ```
   Uses the `test_repo_name` resolved in Step 0 (`eval-[target]-test` or `eval-[repo-name]-test`).

2. **Cleanup prior run (if exists):**
   ```bash
   if test -d "D:\my_ai_projects\project_test_repos\eval-<target>-test"; then
     rm -rf "D:\my_ai_projects\project_test_repos\eval-<target>-test"
   fi
   ```

3. **Create directory:**
   ```bash
   mkdir -p "D:\my_ai_projects\project_test_repos\eval-<target>-test"
   ```

4. **Initialize git:**
   ```bash
   git init "D:\my_ai_projects\project_test_repos\eval-<target>-test"
   ```

## Verification

| ID | Check | Command | Pass |
|----|-------|---------|------|
| G1.1 | Directory exists | `test -d eval-<target>-test/` | Present |
| G1.2 | Git initialized | `test -d eval-<target>-test/.git` | `.git/` exists |

Both checks must pass before transitioning to Step 2.

## Error Handling

| Failure | Action |
|---------|--------|
| Source repo doesn't exist | Abort with clear message, do not create test repo |
| Target not found in source repo | Abort with available artifacts list |
| Test repo path already exists | Delete it first (it's disposable), then create fresh |
| `git init` fails | Check disk space, permissions. Retry once. If still fails, set `failed` with `resume_step: 1` |

## Output

- Empty git-initialized directory at `D:\my_ai_projects\project_test_repos\eval-<target>-test\`
- State transition: `init` → `creating_repo` → ready for Step 2
