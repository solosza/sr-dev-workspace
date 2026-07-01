# DeepEval File List — Step 2 Reference

Exact files and directories to copy from platform-deepeval into the test repo during harness compilation. Step 2 reads this after copying kernel files — do not guess, follow this list.

## Source

Platform-DeepEval at `D:\my_ai_projects\project_test_repos\platform-deepeval`. All paths are relative to the platform-deepeval root.

## Directories (recursive copy)

### `.claude/skills/deepeval-management-layer/`

Full DeepEval management skill. Copy the entire directory:

- `SKILL.md` — skill identity and step table
- `workflow.md` — eval workflow behavior
- `gate-contract.md` — quality gates for eval runs
- `steps/` — step files:
  - `step-01.md`
  - `step-02.md`
  - `step-03.md`
  - `step-04.md`
  - `step-05.md`
  - `pre-eval.md`
  - `on-failure.md`
- `references/` — supporting references:
  - `architecture.md`
  - `metric-catalog.md`

### `framework/interfaces/`

DeepEval interface module:

- `__init__.py`
- `deepeval_interface.py` — main DeepEval interface (test creation, metric config, execution)

### `framework/_reference/`

All reference implementations. Copy the entire directory:

- `__init__.py`
- `metrics/` — reference metric implementations
- `tests/` — reference test implementations
- `tasks/` — reference task definitions
- `roles/` — reference role definitions
- `fixtures/` — reference test fixtures

### `framework/resources/`

Shared resources for eval operations:

- `eval_config.py` — evaluation configuration
- `metric_defaults.py` — default metric parameters

### `framework/__init__.py`

Root framework init file.

## Root Files

### `FRAMEWORK.md`

Framework documentation — describes the DeepEval framework structure and usage.

## Copy Rules

1. Preserve directory structure exactly
2. Create parent directories before copying (`mkdir -p`)
3. Overwrite any existing files in the test repo
4. Copy into matching paths in the test repo (e.g., `framework/` → `<test-repo>/framework/`)
5. The skill goes into `.claude/skills/deepeval-management-layer/` (same path)

## Verification

After copying, verify key files exist in the test repo:

```bash
test -f "<test-repo>/.claude/skills/deepeval-management-layer/SKILL.md"
test -f "<test-repo>/.claude/skills/deepeval-management-layer/gate-contract.md"
test -f "<test-repo>/framework/interfaces/deepeval_interface.py"
test -f "<test-repo>/framework/_reference/__init__.py"
test -f "<test-repo>/framework/resources/eval_config.py"
test -f "<test-repo>/FRAMEWORK.md"
```

All must pass before proceeding to Phase 3 (domain-setup compilation).
