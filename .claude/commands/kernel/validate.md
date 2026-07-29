# /validate

Validate any artifact against its scope contract — the honesty gate. Verifies each unit against its
authoritative source and emits a gated verdict register.

## Usage

```
/validate [artifact] [--scope <scope>]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `artifact` | The file / corpus to validate | `projects/isagawa-v2.0/design-decisions.md` |
| `--scope` | Which validate-contract applies (else inferred) | `--scope doc` |

## What It Does

Discovers the artifact's scope + contract, decomposes it into units, verifies each against its authority
(fetch the paper, resolve the path, run the test), judges, and emits a verdict register conforming to the
contract. The register is gated for correctness (the generic gate hook). Prose orchestrates; the LLM is
the validator.

## Design Reference

> `projects/isagawa-v2.0/architecture.md` · `design-decisions.md`

## Skill Reference

> `.claude/skills/validate/`
