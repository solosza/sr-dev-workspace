# Step AB-3: Run Iterations

Run N iterations of both variants (flat and tiered) using `ABRunner` from `platform-deepeval/framework/ab_testing/runner.py`.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `flat_path` | Output of Step AB-1 | `evals/eval-domain-setup/variants/flat/domain-setup-flat.md` |
| `tiered_path` | Output of Step AB-1 | `evals/eval-domain-setup/variants/tiered/` |
| `prompt` | Output of Step AB-2 | `"Set up a domain for this repo..."` |
| `config.runs` | Experiment config | `5` |
| `output_dir` | Experiment config | `evals/eval-domain-setup/results/` |

## Procedure

1. **Instantiate ABRunner:**
   ```python
   from framework.ab_testing.runner import ABRunner

   runner = ABRunner(config)
   ```

2. **Run experiment:**
   ```python
   results = runner.run_experiment(
       flat_path=flat_path,
       tiered_path=tiered_path,
       prompt=prompt,
       output_dir=output_dir
   )
   ```

3. **Execution order (sequential):**
   For each iteration `i` in `1..config.runs`:
   - Set up isolated workspace for variant A (flat) via `runner.setup_workspace()`
   - Run variant A: `env -u CLAUDECODE claude -p "<prompt>" --cwd <workspace_a>`
   - Capture output to `results/run-{i}/variant-a-output.md`
   - Set up isolated workspace for variant B (tiered) via `runner.setup_workspace()`
   - Run variant B: `env -u CLAUDECODE claude -p "<prompt>" --cwd <workspace_b>`
   - Capture output to `results/run-{i}/variant-b-output.md`
   - Write `results/run-{i}/metadata.json` (timestamps, model, exit codes)

4. **Workspace isolation:**
   - Each run uses a separate temp directory per variant
   - No kernel governance (no hooks, no `settings.local.json`)
   - Minimal `CLAUDE.md`: "You are an agent. Follow the instructions in the skill/command provided."
   - Identical prompt text for both variants

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| GAB3.1 | All output files exist | `N * 2` output .md files in `results/` | All present |
| GAB3.2 | No empty outputs | Each output file `size > 0` | All non-empty |
| GAB3.3 | Metadata per run | `results/run-{i}/metadata.json` exists for each `i` | All present |
| GAB3.4 | Results list complete | `len(results) == config.runs * 2` | True |

All checks must pass before transitioning to Step AB-4.

## Error Handling

| Failure | Action |
|---------|--------|
| `claude -p` non-zero exit | Record exit code in metadata. Mark run as failed. Continue remaining runs. |
| Timeout (> 5 min per run) | Kill process, record timeout in metadata. Continue remaining runs. |
| Rate limit (429) | Wait 60s, retry once. If second failure, record and continue. |
| Workspace setup fails | Abort experiment — cannot proceed without isolation. |

## Output

- `results`: list of dicts with `run_id`, `variant`, `output_path`, `exit_code`, `duration_s`
- All output files written to `output_dir/run-{i}/`
- State transition: `prompt_built` -> `iterations_complete` -> ready for Step AB-4
