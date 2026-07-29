# /coordinator

The factory — compile a need into a governed command/skill (or, at larger scope, a harness) by routing
it through the capabilities.

## Usage

```
/coordinator [need] [--scope <scope>]
```

| Argument | Purpose |
|----------|---------|
| `need` | What to compile |
| `--scope` | The output scope (command, doc, domain, ...) |

## What It Does

A thin router (an index-node): invokes `evaluate` (reuse / adapt / build), routes to `design` + `build`
when needed, `validate`s the output, and closes the evidence loop (operational vs architectural). Owns no
artifact. Copy-tailored from `execute-pipeline`; the workspace loop is left untouched.

## Design Reference

> `projects/isagawa-v2.0/architecture.md` · `design-decisions.md` §13

## Skill Reference

> `.claude/skills/coordinator/`
