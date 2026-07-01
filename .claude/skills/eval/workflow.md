# Eval Workflow

State machine, loop behavior, error handling, and resume support for `/kernel/eval`.

## Input Parsing

```
/kernel/eval <source>                    # harness mode
/kernel/eval <target> <source>           # artifact mode
```

### Mode Detection

| Arg Count | Rule | Mode | Target |
|-----------|------|------|--------|
| 1 arg | Arg is a path or URL | **Harness** | `null` (whole repo) |
| 2 args | First arg = target name, second = path or URL | **Artifact** | First arg |

### Source Detection

| Pattern | Type | Action |
|---------|------|--------|
| Starts with `http://` or `https://` | GitHub URL | Clone to `eval-[repo-name]-clone\`, use clone path |
| Contains `github.com` | GitHub URL | Same as above |
| Everything else | Local path | Use directly |

The resolved local path and detected mode are passed to all subsequent steps.

## State Machine

| State | Entry Condition | Exit Condition |
|-------|-----------------|----------------|
| `init` | Command invoked | Input parsed, source resolved, mode detected |
| `resolving_source` | Input parsed | Source is a local directory (cloned if URL) |
| `creating_repo` | Source resolved | Test repo created at `eval-[name]-test/`, git initialized |
| `compiling_harness` | Test repo exists | Kernel + platform-deepeval copied, domain-setup complete |
| `copying_artifact` | Harness compiled | Target artifact (or whole repo) isolated in test repo |
| `checking_components` | Artifact copied | `_reference/` scanned, missing components created |
| `generating_tests` | Components ready | DeepEval test suite generated in test repo |
| `running_scoring` | Tests generated | `deepeval test` executed, scored report produced |
| `complete` | All scores produced | Report output, score history updated |
| `failed` | Any step error | Error logged, resume_step set, agent stops |

## Loop Behavior

7-step sequential execution (Step 0 + Steps 1-6). Each step must complete before the next begins.

| Step | Action | State | Contract |
|------|--------|-------|----------|
| 0 | Resolve source + detect mode | `resolving_source` | — |
| 1 | Create test repo | `creating_repo` | — |
| 2 | Compile harness | `compiling_harness` | `contracts/step-02-contract.json` |
| 3 | Copy artifact or repo | `copying_artifact` | `contracts/step-03-contract.json` |
| 4 | Component check | `checking_components` | — |
| 5 | Generate tests | `generating_tests` | `contracts/step-05-contract.json` |
| 6 | Run and score | `running_scoring` | `contracts/step-06-contract.json` |

Steps with contracts validate their own output before transitioning to the next state.

## Error Handling

| Step | Failure Mode | Action |
|------|--------------|--------|
| 1 | Test repo path exists | Delete and recreate (disposable) |
| 2 | Harness compilation fails | Check kernel/platform-deepeval paths exist. If domain-setup fails, read error, fix, retry once. If still fails, set `failed` state with `resume_step: 2`. |
| 3 | Missing dependencies | Agent re-scans artifact for unresolved references. Copy missing files. If source file not found, log gap and set `failed` with `resume_step: 3`. |
| 4 | `_reference/` not found | Platform-deepeval may lack `_reference/`. Log warning, create components from scratch using artifact analysis only. |
| 5 | Test generation failure | Re-read artifact + components. Simplify test scope (fewer metrics). If still fails, set `failed` with `resume_step: 5`. |
| 6 | DeepEval execution failure | Check deepeval installed (`pip install deepeval`). Check API key set. Retry once. If infrastructure issue, set `failed` with `resume_step: 6`. |

On any failure: invoke `/kernel/learn` to record what went wrong before stopping.

## Resume Support

When `resume_step` is set in `session_state.json`:

1. `/kernel/session-start` detects `resume_step: N`
2. Agent skips steps 1 through N-1 (their outputs should still exist in the test repo)
3. Agent re-validates the previous step's exit condition before resuming
4. If previous step's output is missing, back up one step and re-execute

Resume state fields in `session_state.json`:

| Field | Purpose |
|-------|---------|
| `resume_step` | Step number to resume from (0-6) |
| `eval_target` | Target artifact name (null in harness mode) |
| `eval_source_repo` | Source repo path (resolved local path, not original URL) |
| `eval_test_repo` | Test repo path |
| `eval_mode` | `artifact` or `harness` |
| `eval_original_source` | Original input (URL or path — preserved for reporting) |

## Composability

The eval loop is composable — it can run standalone or be called by other loops.

| Mode | Behavior |
|------|----------|
| **Standalone** | `/kernel/eval target repo` — full 6-step loop, report to stdout |
| **Called by another loop** | Caller passes target + repo, receives scored report path as output |
| **Task builder** | After BUILD tasks complete, invoke eval against the built artifact |
| **Audit workflow** | Verify LLM artifact scores above configured thresholds |
| **CI/automation** | `run-task.sh` task invokes eval via `claude -p` one-shot |

When called by another command:
- Skip user-facing output (no progress messages)
- Return the scored report path so caller can read and act on results
- Respect caller's error handling (don't invoke `/kernel/learn` if caller handles it)

## Score Tracking

After Step 6, scores are persisted:
- Test repo: `eval/results/report.json` (full scored report)
- Source repo: `eval/results/score-history.json` (append-only score log)
- Regression detection: score drop > 0.1 between consecutive runs triggers a warning
