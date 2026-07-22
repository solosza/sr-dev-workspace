# Task 015: Update gate-contract.md — AB-Mode Gates

## Action
Edit `.claude/skills/eval/gate-contract.md` to add A/B mode quality gates.

## Changes
Add sections for each AB step:

### Step AB-1: Generate Variants
| ID | Check | Method | Pass | Fail Action |
|----|-------|--------|------|-------------|
| GAB1.1 | Flat variant exists | `test -f flat/artifact-flat.md` | File present | Re-run generator |
| GAB1.2 | Tiered variant exists | `test -d tiered/` | Dir present | Re-copy |

### Step AB-3: Run Iterations
| ID | Check | Method | Pass | Fail Action |
|----|-------|--------|------|-------------|
| GAB3.1 | All output files exist | Check N*2 files | All present | Re-run failed |
| GAB3.2 | No empty outputs | `wc -l` > 0 | Non-empty | Re-run |

### Step AB-5: Report
| ID | Check | Method | Pass | Fail Action |
|----|-------|--------|------|-------------|
| GAB5.1 | Report exists | `test -f ab-report.md` | Present | Re-generate |
| GAB5.2 | Verdict valid | One of 3 values | Valid | Re-compute |

## Acceptance Criteria
- gate-contract.md has AB gate sections
- Gates are mechanical (file checks, not subjective)
