# Task 003: Build runner.py

## Action
Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/runner.py`.

## Requirements

Implements the `ABRunner` class:

1. `__init__(self, config: ExperimentConfig)` — takes experiment configuration
2. `setup_workspace(self, variant_path: Path, workspace_dir: Path)` — creates an isolated workspace with the variant's artifact files and a minimal CLAUDE.md (no hooks/enforcement)
3. `run_single(self, workspace_dir: Path, prompt: str, run_id: int, variant_label: str) -> dict` — executes one `claude -p` run, captures output
4. `run_experiment(self, flat_path: Path, tiered_path: Path, prompt: str, output_dir: Path) -> list[dict]` — runs N iterations of both variants, returns results

### Execution
- Each run: `env -u CLAUDECODE claude -p "<prompt>" --cwd <workspace_dir>`
- Capture stdout to `results/run-{run_id}/variant-{a|b}-output.md`
- Write `metadata.json` per run: timestamps, model, exit code
- Sequential execution (parallel as future enhancement)

### Isolation
- Separate temp directory per variant per run
- No kernel governance (no hooks, no settings.local.json)
- Minimal CLAUDE.md: just "You are an agent. Follow the instructions in the skill/command provided."
- Identical prompt text for both variants

### Task Prompt Generation
- If `config.task_prompt` is provided, use it directly
- If null, generate via `generate_prompt(artifact_content: str) -> str` — reads the artifact and produces a realistic task prompt using an LLM call

## Acceptance Criteria
- File exists at the specified path
- `ABRunner` class with `run_experiment()` method
- Output structure: `results/run-N/variant-{a,b}-output.md` + `metadata.json`
- Uses `subprocess.run` with `env -u CLAUDECODE` for isolation
