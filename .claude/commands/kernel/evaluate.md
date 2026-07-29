# /evaluate

The reuse gate — decide reuse / adapt / build for a needed capability, against the capability library.

## Usage

```
/evaluate [need]
```

| Argument | Purpose |
|----------|---------|
| `need` | The capability / harness required (purpose, scope, behaviours) |

## What It Does

Discovers the need + where candidate capabilities live, surveys that library, matches each candidate's
fit (`exact` / `adaptable` / `none`), and decides **reuse > adapt > build** (with `adapt_mode`: by-copy
for load-bearing targets). Emits a decision conforming to the contract. Keeps the library a graph, not a tree.

## Design Reference

> `projects/isagawa-v2.0/architecture.md` · `design-decisions.md`

## Skill Reference

> `.claude/skills/evaluate/`
