# Task 003 — Verify Injection Mechanics

## Type
RESEARCH

## Description
Verify in the INSTALLED Claude Code version whether PreToolUse hooks can return advisory, non-blocking context (e.g. additionalContext / system-message output) visible to the agent, or whether hook output is only surfaced on a block. Live-test with a scratch hook; document exact JSON output schema and what the agent sees in each case.

## Acceptance Criteria
- [ ] File `projects/kernel-jit-rule-injection-research/02-injection-capability.md` exists
- [ ] Covers: live test results of non-blocking PreToolUse output
- [ ] Covers: exact output schema and agent-visible rendering
- [ ] Covers: fallback design if advisory injection is unsupported (block-with-FIX as the only channel)
- [ ] Minimum 300 words

## Gate
DOC-03, DOC-04

## Dependencies
001
