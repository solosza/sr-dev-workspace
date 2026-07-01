# /kernel/eval

Test any LLM artifact or harness using DeepEval. Accepts local paths or GitHub URLs. Two modes: **artifact mode** (test one command/skill) or **harness mode** (test an entire repo as a system). Creates an isolated test repo, compiles a harness, dynamically generates and runs deepeval tests, produces scored reports.

## Usage

```
/kernel/eval <source>                    # harness mode — eval entire repo
/kernel/eval <target> <source>           # artifact mode — eval one artifact
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `source` | Local path OR GitHub URL to the repo (e.g., `D:\path\to\repo` or `https://github.com/org/repo`) |
| `target` | (Optional) Command, skill, or artifact name to test. If omitted, evals the entire repo as a harness. |

### Source Resolution

| Format | Example | Behavior |
|--------|---------|----------|
| **Local path** | `D:\my_ai_projects\project_test_repos\kernel-minimal` | Use directly |
| **GitHub URL** | `https://github.com/isagawa-co/isagawa-kernel` | Clone to `eval-[repo-name]-clone\`, then use as local path |

### Examples

```
# Eval entire harness from local path (harness mode)
/kernel/eval D:\my_ai_projects\project_test_repos\kernel-minimal

# Eval entire harness from GitHub (harness mode)
/kernel/eval https://github.com/isagawa-co/isagawa-kernel

# Eval specific artifact (artifact mode)
/kernel/eval domain-setup D:\my_ai_projects\project_test_repos\kernel-minimal

# Eval specific artifact from GitHub (artifact mode)
/kernel/eval domain-setup https://github.com/isagawa-co/isagawa-kernel
```

## Instructions

This command uses a skill-based approach with 7 steps (Step 0 + Steps 1-6).

### Load Skill

Read and follow: `.claude/skills/eval/SKILL.md`

### Quick Reference

| Step | Action |
|------|--------|
| 0 | Resolve source (local path or GitHub clone) + detect mode |
| 1 | Create test repo |
| 2 | Compile harness (kernel + platform-deepeval + domain-setup) |
| 3 | Copy artifact (artifact mode) or entire repo (harness mode) |
| 4 | Dynamic component check (use existing or create new) |
| 5 | Generate deepeval tests |
| 6 | Run and score |

### Key Principles

- **Two modes** — artifact mode (one target) or harness mode (whole repo), dynamically detected from input
- **Source flexibility** — local path or GitHub URL, resolved transparently in Step 0
- **Harness = kernel + platform-deepeval + domain-setup** — fully compiled, not just file copy
- **Dynamic components** — agent checks _reference/ patterns before creating new metrics/tests
- **Composable** — standalone or callable by another loop
- **Framework grows** — new components follow _reference/ patterns, eventually merge to master
- **Auto-execute** — don't ask, just run

### Composability

This command is designed to be called standalone or by other commands:

```
# Standalone — harness mode
/kernel/eval D:\my_ai_projects\project_test_repos\kernel-minimal

# Standalone — artifact mode
/kernel/eval check-data D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa

# From task-builder (after BUILD tasks, run eval against the output)
# From audit-workflow (verify an LLM artifact scores above thresholds)
```

When called by another command, output the scored report path so the caller can read it.
