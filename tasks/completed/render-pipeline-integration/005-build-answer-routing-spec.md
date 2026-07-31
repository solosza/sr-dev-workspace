# 005 — Build the answer-routing spec

Type: BUILD

## Deliverable
`.claude/skills/render/steps/step-route-annotations.md`

## What it does
Session-side routing logic: when the watcher wakes the session with new annotations, decide what each means and act. Answer inline, or route "go deeper" into /deep-dive. UI stays a capture surface; only the session changes state via kernel commands.

## Acceptance Criteria
- [ ] File exists at the deliverable path.
- [ ] Documents the annotation shape `{target, action, raw_words, ref, at}`.
- [ ] Rule: plain `ask` → session writes `session-reply.json` `{status, answers:[{ref, answer}]}` (accumulate prior answers).
- [ ] Rule: "go deeper" ask → re-confirm in chat, then route `/deep-dive <target wedge>`; raw_words pass verbatim.
- [ ] Rule: destructive / next-loop actions re-confirm in chat before routing.
- [ ] Rule: after answering/routing, re-arm the watcher with the new answered-count.
- [ ] Is a spec (pointers + rules), not code.

## Verify
`test -f .claude/skills/render/steps/step-route-annotations.md` and `grep -q 'session-reply.json' .claude/skills/render/steps/step-route-annotations.md`.
