# Gate Contract

## Phase Gates

| Gate | Trigger | Check | On Fail |
|------|---------|-------|---------|
| Setup → Requirements | After Step 2 | Command name confirmed AND reference design selected | Cannot proceed without both |
| Requirements → Generation | After Step 3 | Structured requirements cover all 7 required sections | Loop back to interview gaps |
| Generation → Closeout | After Step 6 | Design doc passes completeness (7/7) AND files written | Re-validate, fix gaps, re-write |

## Step Gates

| Step | Output | Validation |
|------|--------|-----------|
| 1. Parse Intent | Confirmed command name | Kebab-case, no conflict with existing design docs |
| 2. Select Reference | Reference design path | Path resolves to existing design doc index |
| 3. Interview | Structured requirements | Covers: identity, philosophy, vocabulary, rules, workflow, steps, file structure |
| 4. Draft Design Doc | Draft content for all files | All 7 required sections present in draft |
| 5. Validate Completeness | Pass/fail report | 7/7 required sections at minimum depth |
| 6. Write Files | Files on disk | All files written, verified readable |
| 7. Report | Summary output | Includes path, completeness score, next steps |
