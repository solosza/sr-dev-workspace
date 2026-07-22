# Step 1: Resolve Input

## Purpose

Determine what is being walked through, in which mode (loop / one-shot), at which depth — and check for an active walkthrough to resume first.

## Input

- Command argument: `[file-or-topic]` with optional `--terse`, `--once`
- `.claude/state/walkthrough-state.json` (may not exist)

## Output

- Resolved artifact + input type (`file` | `design-doc` | `command` | `concept` | `plan` | `error`)
- Mode (`loop` | `one-shot`) and depth (`plain` | `terse`)
- OR: resume decision (jump to Step 4 at `sections[cursor]`)

## Acceptance Criteria

- [ ] Resume check ran FIRST: if state has `status: active` and input matches (or is "continue"), position announced and control jumps to Step 4
- [ ] Flags extracted; artifact resolved to concrete file(s) or a named concept
- [ ] Mode detected: `--once` → one-shot; narrow-question phrasing → one-shot; otherwise loop
- [ ] Active state never silently overwritten — new artifact while active requires explicit user confirmation

## References

- Design doc: `.claude/docs/design/walkthrough/references/workflow.md` (Step 1)

## Procedure

1. Read `.claude/state/walkthrough-state.json` if it exists. `status: active` + matching/continue input → announce "section N of M: [name]", go to Step 4.
2. Parse flags (`--terse`, `--once`); remainder is the artifact.
3. Detect input type: existing path → `file`; path in docs/design → `design-doc`; path in commands/ or skills/ → `command`; phase/plan reference → `plan`; error text → `error`; else `concept`.
4. Detect mode and depth per flags/phrasing.
5. Ambiguous artifact (multiple matches, vague topic) → ask ONE clarifying question.

## Verification

Mode, type, depth stated in output before Step 2 begins.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| State active, user wants a new walkthrough | Offer: finish / park / abandon (explicit) — only then overwrite |
| Artifact doesn't exist as a file | Treat as concept; confirm with user if unclear |
