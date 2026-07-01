# Artifact Isolation: Copy Target + All Dependencies

## Status
NEW

## Purpose

Define how Step 3 copies the target LLM artifact into the test repo with everything it needs to be tested in isolation. The artifact must be fully self-contained — no external path references.

## What "Artifact" Means

Any LLM-driven component that can be tested:

| Artifact Type | Example | What Gets Copied |
|---------------|---------|-------------------|
| Kernel command | `check-data` | skill/, command entry point, design docs, referenced data |
| Skill/harness | `deepeval-management-layer` | skill/ (SKILL.md, workflow, steps, references, contracts) |
| Agent workflow | `autonomous-cycling` | skill/, state schemas, any referenced protocols |
| Full domain spec | `platform-deepeval` | All skills, framework/, interfaces, references |

The agent determines what to copy based on what the artifact IS.

## Example: Command (`check-data` from `hmsa-healthcare-qa`)

```
From source repo → Into test repo

.claude/skills/check-data/
├── SKILL.md                    ← orchestrator, rules, vocabulary
├── workflow.md                 ← step definitions, state schema
├── gate-contract.md            ← quality gates
├── steps/
│   ├── step-01-configure.md
│   ├── step-02-load-data.md
│   └── ... (all step files)
├── references/
│   ├── INDEX.md
│   └── step-NN/               ← all reference payloads
└── contracts/
    ├── step-01-contract.json
    ├── step-03-contract.json
    └── ... (all contract JSONs)

.claude/commands/kernel/check-data.md    ← command entry point

.claude/docs/design/check-data/          ← design docs (if they exist)
```

## Dependency Resolution

The agent must scan the artifact's files for external references:

1. **Read SKILL.md** — check File Index for all referenced files
2. **Read each step file** — check References section for external paths
3. **Read contracts** — check for referenced schemas or data files
4. **Resolve paths** — if a step references `projects/30-day-readmissions/reference/`, copy that too

The goal: after copying, every file the artifact's LLM would read during execution exists in the test repo. No broken references.

## What Does NOT Get Copied

- Source repo's domain-specific state (xlsx files, run history)
- Source repo's kernel (test repo has its own compiled kernel)
- Source repo's protocol (test repo compiles its own)
- Other artifacts from the source repo (only the target)

## Verification

After copying, verify:
- All files referenced in SKILL.md File Index exist in test repo
- All files referenced in step files exist in test repo
- All contract JSONs parse as valid JSON (if contracts exist)
- No broken wikilinks in any copied markdown

## Dependencies

- Source repo must exist and be accessible
- Target artifact must be identifiable (skill folder, command entry point, or both)
