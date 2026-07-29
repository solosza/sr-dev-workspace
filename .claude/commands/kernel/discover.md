# /discover

The discover primitive — characterize an input and locate where its target lives. Invoked by other
capabilities as their step-01, and callable standalone.

## Usage

```
/discover [input] --goal "<what to determine>"
```

| Argument | Purpose |
|----------|---------|
| `input` | The artifact / need to characterize |
| `--goal` | What to determine (e.g. a scope + contract; where capabilities live) |

## What It Does

Characterizes the input's kind, locates the target the goal asks for (reasoned from the input, not
defaulted), resolves material ambiguity with one bounded HITL question, and returns a structured
discovery. Invoked as the first step by other capabilities so none of them hardcodes "what is this and
where do I look."

## Design Reference

> `projects/isagawa-v2.0/architecture.md` · `design-decisions.md` §12

## Skill Reference

> `.claude/skills/discover/`
