# Step 2: Ground

## Purpose

RULE ZERO applied to teaching — Read the real sources before explaining anything. Grounding is what separates this command from a textbook answer.

## Input

- Resolved artifact from Step 1

## Output

- `sources_read`: list of exact paths Read this session

## Acceptance Criteria

- [ ] The artifact itself was Read (if it is a file/doc/command)
- [ ] Related workspace sources enumerated and Read: sibling implementations, governing contract, relevant lessons, prior design docs
- [ ] Every path recorded in `sources_read`
- [ ] If NO workspace sources exist (pure external concept): explicitly marked external-only — explanations must say so instead of implying repo-verification

## References

- Design doc: `.claude/docs/design/walkthrough/references/workflow.md` (Step 2)

## Procedure

1. Read the artifact with the Read tool.
2. Enumerate related sources for THIS workspace (e.g., for a conftest design: every reference conftest across repos; for a command: its skill + design doc).
3. Read them — never rely on memory of what a file contains.
4. Record all paths into `sources_read`.

## Verification

`sources_read` non-empty (or external-only marked). Every grounding claim made later in Step 4 must trace to one of these paths.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| Source path unreadable/missing | Drop it from grounding; note the gap; never fabricate its contents |
| Sources too numerous | Read the canonical few, list the rest as available-on-request in the map discussion |
