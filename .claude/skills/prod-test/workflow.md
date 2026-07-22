# Prod-Test Workflow

State machine, loop behavior, error handling, and resume support for `/kernel/prod-test`.

## Input Parsing

```
/kernel/prod-test <source_repo_path>
```

The source repo must contain a domain spec (`.claude/skills/*/SKILL.md`) and a Layer 1 Interface class.

## State Machine

| State | Entry Condition | Exit Condition |
|-------|-----------------|----------------|
| `init` | Command invoked | Input parsed, source validated |
| `parsing` | Input validated | Repo structure discovered, interface identified, infra type determined |
| `assembling_master` | Parse complete | Master repo created with source + kernel + scripts |
| `validating_master` | Master assembled | Domain-setup complete, protocol + hooks built |
| `copying_test` | Master validated | Test repo created as disposable copy |
| `setting_up_infra` | Test repo ready | Docker containers running, connectivity verified |
| `writing_tasks` | Infra ready | L1/L2/L3 test tasks written to test repo tasks/ |
| `executing_tasks` | Tasks written | All tasks executed via inner run-task.sh |
| `reporting` | Tasks executed | Validation report produced, infra torn down |
| `complete` | Report produced | Results presented to caller |
| `failed` | Any step error | Error logged, resume_step set, agent stops |

## Loop Behavior

8-step sequential execution. Each step must complete before the next begins.

| Step | Action | State | Gate |
|------|--------|-------|------|
| 1 | Parse input + discover repo | `parsing` | G1 |
| 2 | Assemble master repo | `assembling_master` | G2 |
| 3 | Validate master (domain-setup) | `validating_master` | G3 |
| 4 | Copy master to test repo | `copying_test` | G4 |
| 5 | Set up test infrastructure | `setting_up_infra` | G5 |
| 6 | Write inner test tasks | `writing_tasks` | G6 |
| 7 | Execute inner test batch | `executing_tasks` | G7 |
| 8 | Collect report + cleanup | `reporting` | G8 |

Steps with gates validate their own output before transitioning to the next state.
-> Gate definitions: `gate-contract.md`

## Error Handling

| Step | Failure Mode | Action |
|------|--------------|--------|
| 1 | Source repo missing | Abort with path-not-found error |
| 1 | No domain spec | Abort — prod-test requires `.claude/skills/*/SKILL.md` |
| 1 | No Interface class | Abort — cannot determine infra type without Interface |
| 2 | Kernel source missing | Check kernel path exists. If not found, abort with location error. |
| 3 | Domain-setup fails | Read error, fix, retry once. If still fails, set `failed` with `resume_step: 3`. |
| 4 | Copy fails | Check disk space. Retry once. If still fails, set `failed` with `resume_step: 4`. |
| 5 | Docker unavailable | STOP. Report Docker required. Do NOT fall back to mocks. |
| 5 | Container fails to start | Read docker logs. Fix config, retry once. If still fails, set `failed` with `resume_step: 5`. |
| 6 | Task generation fails | Re-read interface and domain spec. Simplify scope. Retry once. |
| 7 | Inner run-task.sh fails | Check logs in test repo. Some task failures are expected (L3 may legitimately fail). Record results. |
| 8 | Report generation fails | Re-read task results. Generate minimal report with available data. |

On any failure: invoke `/kernel/learn` to record what went wrong before stopping.

## Resume Support

When `resume_step` is set in `session_state.json`:

1. `/kernel/session-start` detects `resume_step: N`
2. Agent skips steps 1 through N-1 (their outputs should still exist)
3. Agent re-validates the previous step's exit condition before resuming
4. If previous step's output is missing, back up one step and re-execute

Resume state fields in `session_state.json`:

| Field | Purpose |
|-------|---------|
| `resume_step` | Step number to resume from (1-8) |
| `prod_test_source` | Source repo path |
| `prod_test_master` | Master repo path |
| `prod_test_test` | Test repo path |
| `prod_test_infra_type` | Infrastructure type (docker-ssh, docker-browser, etc.) |

## Composability

The prod-test loop is composable — it can run standalone or be called by other loops.

| Mode | Behavior |
|------|----------|
| **Standalone** | `/kernel/prod-test repo` — full 8-step loop, report to stdout |
| **Called by another loop** | Caller passes source repo path, receives validation report path as output |
| **Task builder** | After BUILD tasks complete, invoke prod-test against the built artifact |
| **Audit workflow** | Verify deliverable passes all L1/L2/L3 gates |
| **CI/automation** | `run-task.sh` task invokes prod-test via `claude -p` one-shot |

When called by another command:
- Skip user-facing progress messages
- Return the validation report path so caller can read and act on results
- Respect caller's error handling

## Outcome

After completion:
- Master repo at `[source]-master/` (reusable golden copy)
- Test repo at `[source]-test/` (disposable, contains results)
- Validation report at `[source]-test/_test/validation-report.json`
- Test infrastructure torn down (Docker containers stopped and removed)
- Results presented to caller
