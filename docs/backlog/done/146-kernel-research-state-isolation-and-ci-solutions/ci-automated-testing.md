# CI / Automated Testing — Research

## Status
NEW

## The Problem

The kernel has no CI. All verification is either:
- Agent self-checking (git log, file counts, JSON state reads)
- Prod-test (independent but manual — invoked by the agent, not automated)
- Pytest (run by agent or run-task.sh, not triggered on push/PR)

An external reviewer's expectation: "I'd want independent validation scripts, CI, or a reproducible replay before calling it production-grade."

## What Already Exists

1. **Prod-test skill** — copies to disposable repo, runs L1/L2/L3 tests, produces validation report
2. **Validation report** — `_test/validation-report.json` with pass/fail per task
3. **Pytest suites** — exist in isagawa-kernel, test-platform-deepeval, and other repos
4. **run-task.sh** — deterministic task runner with iteration logs

## Research Questions

1. What GitHub Actions patterns work for agent-governed repos? (pytest on push, hook validation on PR)
2. Can prod-test be wrapped as a GitHub Action that runs on PR?
3. Should validation reports be committed as artifacts alongside deliverables?
4. What's the right CI scope — just isagawa-kernel, or a template that domain-setup generates per repo?
5. How do other Claude Code harness projects handle CI?
6. Can hook integrity be verified in CI (hash check on hook files, settings validation)?

## Solution Criteria

- Works with GitHub Actions free tier (2,000 minutes/month)
- No secrets required for basic test runs (no API keys for structural/import tests)
- Template-based — domain-setup should generate CI config, not hand-write per repo
- Validation report published as GitHub Actions artifact
