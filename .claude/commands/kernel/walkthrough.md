# /walkthrough

Walk through any artifact or concept section by section — plain-English explanations grounded in this workspace's real repos, one section per turn, recording settled decisions into a durable ledger.

## Usage

```
/walkthrough [file-or-topic]              → loop mode, plain depth
/walkthrough [file-or-topic] --terse      → loop mode, terse depth
/walkthrough [narrow question]            → one-shot (inferred)
/walkthrough [topic] --once               → one-shot (forced)
continue                                  → resume loop from cursor
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `file-or-topic` | Artifact to walk through: file, design doc, command, concept, plan, error | `conftest design`, `.claude/commands/kernel/anchor.md`, `"fixture scoping"` |
| `--terse` | Analysis + recommendation only — drops the teaching parts | `/walkthrough api-objects.md --terse` |
| `--once` | Single explanation, no loop, no state, no ledger | `/walkthrough "the intent chain" --once` |

Mid-loop verbal dials: "terse from here", "slow down on this one", "skip this section", "add a section on X".

## What It Does

Decomposes the artifact into a user-approved section map, then loops: explain one section (plain-English purpose → visual flow → why each piece → grounding in your real files → recommendation for your case → mental model → settle prompt), discuss until you settle the decision, record it, advance. Blocks on you every iteration — this is the user-paced counterpart to autonomous cycling. At exit, writes the decisions ledger to `docs/walkthroughs/` and offers to feed it to `/design`.

## Examples

```
# Loop over a design topic, grounded in the workspace's reference implementations
/walkthrough conftest design

# Loop over an existing command's mechanics
/walkthrough .claude/commands/kernel/anchor.md

# Quick single explanation
/walkthrough "what does the cursor in walkthrough state do" --once

# Terse design review of a doc you mostly know
/walkthrough projects/hmsa-qa-platform/02-reference-patterns/api-objects.md --terse
```

## Critical Behavior

- One section per message — never batched. The settle prompt ends every turn.
- Never explains ungrounded — reads the actual sources first; grounding cites them by name.
- Never runs autonomously — not invocable from run-task.sh or any pipeline.

## Design Reference

> `.claude/docs/design/walkthrough/index.md`

## Skill Reference

> `.claude/skills/walkthrough/`
