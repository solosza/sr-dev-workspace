# /iom-status

Report the IOM factory state — which capabilities exist, their command-skill-pattern conformance, and the
overall build status. Read-only.

## Usage

```
/iom-status
```

No arguments.

## What It Does

Surveys the factory capabilities (`discover` + `evaluate` / `design` / `build` / `validate` + `coordinator`),
reports each one's command-skill-pattern layers and whether it is individually callable, then a factory
rollup and the open gaps from the design decisions. Changes nothing.

## Design Reference

> `projects/isagawa-v2.0/architecture.md` · `design-decisions.md`

## Skill Reference

> `.claude/skills/iom-status/`
