# Production Readiness Solutions — Summary Report

**Backlog:** 146-kernel-research-state-isolation-and-ci-solutions
**Date:** 2026-06-22
**Origin:** External review critique analysis (backlog 145)

---

## Executive Summary

Two production readiness gaps were identified in backlog 145 as the highest-impact fixes: (1) state isolation for concurrent agents, and (2) CI/automated testing. Research across LangGraph, CrewAI, AutoGen, and GitHub Actions best practices confirms both gaps are real but bounded in scope. Solutions leverage existing kernel mechanisms — no new architecture or external dependencies required.

| Critique | Verdict | Solution | Effort |
|----------|---------|----------|--------|
| State contention during parallel agents | PARTIALLY TRUE — designed but not wired | Per-agent state files + agent_id routing | Small (4-6 hours) |
| No CI / independent verification | TRUE — zero GitHub Actions in any repo | Two-tier CI (push + PR) + template generation | Medium (2-3 days) |

---

## State Isolation — Summary

**Full proposal:** [state-isolation-proposal.md](state-isolation-proposal.md)

### Problem
When multiple agents run concurrently, they all write to `session_state.json` and `{domain}_workflow.json`. Later agents overwrite earlier agents' state.

### Industry Research
- **LangGraph**: Reducer-driven state with thread isolation — each thread gets independent state/checkpoints
- **CrewAI**: Namespace separation — shared read-only layer + per-agent private layer
- **AutoGen**: No shared mutable state — pure message passing between agent instances

### Proposed Solution
**Per-agent state files + protected parent context.** Each spawned agent writes to `agent-{N}-state.json` and `agent-{N}-actions.jsonl`. Parent session_state.json is orchestrator-only. Monitor aggregates by reading per-agent files.

### Key Changes
1. Hook: route actions log by `agent_id`
2. run-task.sh: pass `agent_id` in `pre_init_state`
3. execute-pipeline: spawn agents with identity
4. Prompt: instruct agents to write only to their state file

### Why This Works
- Extends existing `spawn-agent-swarm` per-agent file pattern (already designed)
- Compatible with `one_shot` guard (no gate changes)
- No external runtime (file-based, cross-platform)
- Backward compatible (agents without `agent_id` use shared state)

---

## CI / Automated Testing — Summary

**Full proposal:** [ci-automated-testing-proposal.md](ci-automated-testing-proposal.md)

### Problem
Zero GitHub Actions workflows in any repo. All verification is manual (agent-invoked or human-invoked). No automated tests on push/PR.

### Industry Research
- Standard Python CI: checkout → setup-python → pip install → pytest → upload-artifact
- Artifact publishing: JUnit XML + `publish-unit-test-result-action` for PR annotations
- Template CI: shell scripts or Copier templates generate per-repo workflows
- Free tier: 2,000 min/month — sufficient for 400-1,000 CI runs

### Proposed Solution
**Two-tier CI: fast push checks + thorough PR checks.** Plus template generation in domain-setup.

| Tier | Trigger | Duration | What |
|------|---------|----------|------|
| Push CI | Every push | ~2-3 min | Import checks, pytest (structural + unit) |
| PR CI | Pull requests | ~5-10 min | Full pytest, hook integrity, validation report |

### Key Changes
1. Add `.github/workflows/ci.yml` to isagawa-kernel (reference implementation)
2. Add hook integrity check (SHA-256 audit trail in CI logs)
3. Add CI generation function to domain-setup
4. Publish validation reports as GitHub Actions artifacts

### Why This Works
- Fits within free tier constraints
- No secrets needed for structural/unit tests
- Template-based — domain-setup generates CI for new repos
- Hook integrity creates audit trail without preventing legitimate modifications

---

## Implementation Roadmap

### Phase 1: State Isolation (Week 1)
**Priority: First** — prevents bugs at scale, required before any multi-agent workflow expansion

| Step | Change | File | Hours |
|------|--------|------|-------|
| 1a | Add `agent_id` to pre_init_state | `run-task.sh` | 1 |
| 1b | Route actions log by agent_id | `universal-gate-enforcer.py` or actions-log-appender | 2 |
| 1c | Update execute-pipeline to pass agent identity | `step-04-execute-tasks.md` | 1 |
| 1d | Test: spawn 2 concurrent agents, verify no state overwrites | Manual test | 2 |

**Total: ~6 hours**

### Phase 2: CI — Reference Implementation (Week 1-2)
**Priority: Second** — standard engineering credibility, visible to external reviewers

| Step | Change | File | Hours |
|------|--------|------|-------|
| 2a | Write CI workflow YAML | `isagawa-kernel/.github/workflows/ci.yml` | 2 |
| 2b | Add hook integrity check | Same workflow, PR-only job | 1 |
| 2c | Test CI workflow against actual repo | Push to branch, verify Actions run | 2 |
| 2d | Document CI pattern | `isagawa-kernel/docs/ci.md` | 1 |

**Total: ~6 hours**

### Phase 3: CI — Template Generation (Week 2-3)
**Priority: Third** — scales CI to all domain repos

| Step | Change | File | Hours |
|------|--------|------|-------|
| 3a | Write CI generation function | `lib/ci_generator.py` or inline in domain-setup | 4 |
| 3b | Integrate into domain-setup step 9 | `step-09-commands.md` | 2 |
| 3c | Test: run domain-setup on fresh repo, verify CI generated | Manual test | 2 |

**Total: ~8 hours**

### Phase 4: Integration (Week 3+)
| Step | Change | Hours |
|------|--------|-------|
| 4a | Monitor aggregation in execute-pipeline step 5 | 2 |
| 4b | Validation report as GitHub Actions artifact | 2 |
| 4c | Gate contract verification in CI | 4 |

**Total: ~8 hours**

---

## Dependencies Between Solutions

```
State Isolation (Phase 1)
    └── Enables safe multi-agent execution
         └── Which is tested by CI (Phase 2)

CI Reference (Phase 2)
    └── Proves testing infrastructure works
         └── Template generation (Phase 3) scales it

Template Generation (Phase 3)
    └── Every new domain-setup repo gets CI
         └── Integration (Phase 4) connects gate contracts to CI
```

State isolation should come first because:
1. It's smaller scope (one sprint vs multi-sprint)
2. It prevents bugs that would confuse CI results
3. CI tests will exercise multi-agent workflows — isolation must work first

---

## Critique Traceability

| Original Critique (Backlog 145) | Verdict | Solution Proposal | Phase |
|--------------------------------|---------|-------------------|-------|
| State contention — shared mutable state | PARTIALLY TRUE | [state-isolation-proposal.md](state-isolation-proposal.md) | 1 |
| Independent verification — no CI | TRUE | [ci-automated-testing-proposal.md](ci-automated-testing-proposal.md) | 2-3 |
| External reproducibility | TRUE (separate concern) | Not in scope — see backlog 145 findings | Future |

---

## Total Effort

| Phase | Effort | Timeline |
|-------|--------|----------|
| Phase 1: State Isolation | ~6 hours | Week 1 |
| Phase 2: CI Reference | ~6 hours | Week 1-2 |
| Phase 3: CI Template | ~8 hours | Week 2-3 |
| Phase 4: Integration | ~8 hours | Week 3+ |
| **Total** | **~28 hours** | **~3 weeks** |

All solutions are implementable without external dependencies, work on Windows and Unix, and are compatible with the existing kernel architecture.
