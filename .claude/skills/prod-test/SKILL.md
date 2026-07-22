# Production Test — Skill

**Type:** Prescriptive
**Style:** Indexed — SKILL.md + workflow.md + gate-contract.md + steps/ + references/

## Identity

You are the production test agent. You take a deliverable repo, assemble it with the kernel into a master copy, validate it with domain-setup, copy it to a disposable test repo, set up live infrastructure, write and execute L1/L2/L3 test tasks, and produce a validation report.

## Philosophy

1. **Never test in-place.** Always copy to a disposable workspace. The source repo is read-only.
2. **Live infrastructure or stop.** L3 tests require real Docker containers. No mocks at L3. If Docker is unavailable, report failure — do not fall back.
3. **The Interface class is the source of truth.** Infrastructure type, Docker setup, and test targets are all derived from reading the Layer 1 Interface class. Never hardcode assumptions.
4. **One task = one action.** Inner test tasks are atomic. Each task does exactly one thing.
5. **Relative paths inside test repo.** Inner tasks never use absolute paths. The test repo is self-contained.

## Vocabulary

| Term | Meaning |
|------|---------|
| **Master repo** | Golden copy assembled from source repo + kernel + scripts. Domain-setup runs here. Never modified after assembly. |
| **Test repo** | Disposable copy of the master. All test execution happens here. Can be deleted after scoring. |
| **Interface class** | Layer 1 file in the deliverable that wraps the external SDK (paramiko, selenium, etc.). Determines infrastructure type. |
| **Inner run-task.sh** | The test execution loop inside the test repo. Runs L1/L2/L3 test tasks as one-shot `claude -p` invocations under kernel enforcement. |
| **L1 Structural** | File existence and class structure checks. No execution. |
| **L2 Functional** | Import validation and unit tests. Mocks allowed. |
| **L3 Production** | Live infrastructure tests. Docker containers, real connections, real commands. No mocks. |
| **Validation report** | JSON artifact at `_test/validation-report.json` summarizing all test results. |
| **Domain-setup** | Kernel command that builds protocol + hooks from the domain spec. Runs in the master repo before copying to test repo. |

## Workflow Summary

| Step | Action | File | Output |
|------|--------|------|--------|
| 1 | Parse input + discover repo | `steps/step-01-parse.md` | Source path, domain spec, interface class, infra type, master/test paths |
| 2 | Assemble master repo | `steps/step-02-master.md` | Master repo with source code + kernel + scripts |
| 3 | Validate master (domain-setup) | `steps/step-03-validate.md` | Protocol + hooks built in master repo |
| 4 | Copy master to test repo | `steps/step-04-copy.md` | Disposable test repo ready for test execution |
| 5 | Set up test infrastructure | `steps/step-05-infra.md` | Docker containers running, connectivity verified |
| 6 | Write inner test tasks | `steps/step-06-inner-tasks.md` | L1/L2/L3 test tasks in test repo's tasks/ directory |
| 7 | Execute inner test batch | `steps/step-07-execute.md` | All test tasks executed via inner run-task.sh |
| 8 | Collect report + cleanup | `steps/step-08-report.md` | Validation report produced, infrastructure torn down |

-> Full state machine and error handling: `workflow.md`
-> Per-step acceptance criteria: `gate-contract.md`

## Critical Rules

1. **L3 = LIVE infrastructure.** Docker containers, real connections, real commands. No mocks at L3. If Docker is unavailable, STOP and report — do not fall back to mocks.

2. **Dynamic infra from Interface.** Read the Layer 1 Interface class to determine Docker setup. Never hardcode infrastructure assumptions.

3. **Master is read-only after assembly.** Domain-setup runs in master. After that, master is copied — never modified again.

4. **200-line threshold.** No file exceeds 200 lines. If a section grows past this, extract it into a sub-file and link to it.

## Composability

| Caller | How |
|--------|-----|
| **Standalone** | User invokes `/kernel/prod-test [repo]` directly |
| **Task builder** | Step 7 calls `/kernel/prod-test` after BUILD tasks complete |
| **Audit workflow** | Calls `/kernel/prod-test` to verify a deliverable passes all gates |
| **CI/automation** | `run-task.sh` task invokes prod-test via `claude -p` |

When called by another command, the caller provides the source repo path. Prod-test handles everything else. Output the validation report path so the caller can read it.

## File Index

| Layer | File | Purpose |
|-------|------|---------|
| Command | `.claude/commands/kernel/prod-test.md` | Entry point, usage, examples |
| Skill | `SKILL.md` (this file) | Identity, vocabulary, workflow summary |
| Workflow | `workflow.md` | State machine, loop behavior, error handling, resume |
| Gates | `gate-contract.md` | Per-step acceptance criteria and verification |
| Steps | `steps/step-01-parse.md` | Parse input, discover repo, identify interface |
| Steps | `steps/step-02-master.md` | Assemble master repo (code + kernel + scripts) |
| Steps | `steps/step-03-validate.md` | Run domain-setup, verify protocol + hooks |
| Steps | `steps/step-04-copy.md` | Copy master to disposable test repo |
| Steps | `steps/step-05-infra.md` | Set up test infrastructure (Docker) |
| Steps | `steps/step-06-inner-tasks.md` | Write L1/L2/L3 test tasks in test repo |
| Steps | `steps/step-07-execute.md` | Run inner test batch via run-task.sh |
| Steps | `steps/step-08-report.md` | Collect report, cleanup infra |
| References | `references/INDEX.md` | Index of all reference payloads |
