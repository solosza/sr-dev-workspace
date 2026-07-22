# References Index

## Design Doc References

> `.claude/docs/design/gap-check/index.md` — design doc index
> `.claude/docs/design/gap-check/references/workflow.md` — step procedures (Steps 1-5)
> `.claude/docs/design/gap-check/references/gap-categories.md` — gap types per corpus type with detection logic
> `.claude/docs/design/gap-check/references/corpus-detection.md` — how to detect corpus type from file content

## By Step

### Step 1: Discover
- -> design doc: [[gap-check/references/workflow.md]] — Step 1 procedure (glob, inventory)

### Step 2: Detect & Model
- -> design doc: [[gap-check/references/corpus-detection.md]] — corpus type signals and priority rules
- -> design doc: [[gap-check/references/workflow.md]] — Step 2 procedure (model building per type)

### Step 3: Check
- -> design doc: [[gap-check/references/gap-categories.md]] — all 14 gap categories with detection logic and examples
- -> design doc: [[gap-check/references/workflow.md]] — Step 3 procedure (which checks per type)

### Step 4: Report
- -> design doc: [[gap-check/references/workflow.md]] — Step 4 procedure (output format, grouping)

### Step 5: Fix
- -> design doc: [[gap-check/references/workflow.md]] — Step 5 procedure (approval flow, user options)

## By Artifact Type

### Gap Categories
- -> design doc: [[gap-check/references/gap-categories.md]] — universal, skill, test-case, design-doc, onboard-run categories

### Corpus Detection
- -> design doc: [[gap-check/references/corpus-detection.md]] — file signals, priority rules, mixed corpus handling
