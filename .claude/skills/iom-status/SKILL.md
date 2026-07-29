# IOM Status — Skill

## Identity

You report the IOM factory state: which capabilities exist, their command-skill-pattern conformance, and
the overall build status. Read-only — you survey and report, you change nothing.

## Usage

```
/iom-status
```

## What It Does

Surveys the factory capabilities (the `discover` primitive, the compile capabilities `evaluate` / `design`
/ `build` / `validate`, and the `coordinator`) and reports, for each: which command-skill-pattern layers
exist (L1 command · L2 SKILL · L3 steps · L4 references · L5 contracts · L6 hook), whether it is
individually callable as `/kernel/<name>`, and its status. Then a factory rollup and the open gaps.

## Method

1. Glob `.claude/skills/*/SKILL.md` and `.claude/commands/kernel/*.md` to locate the factory capabilities.
   The factory set: `discover`, `evaluate`, `design`, `build`, `validate`, `coordinator` (+ `iom-status`).
2. For each, check which layers are present (L1 file exists? steps/ dir? contracts/ dir? a hook?).
3. Report a table (capability · layers · callable · status), a rollup (n of 5 compile capabilities built,
   gate present), and open gaps drawn from `design-decisions.md` §12 to §14.

## Output

A concise status report: the per-capability table + the factory rollup + open gaps. Read-only.

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — the read-only factory status reporter (lean; no payloads yet, extract when it grows) |
