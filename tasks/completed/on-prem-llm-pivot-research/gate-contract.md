# Gate Contract — On-Prem LLM Pivot Research

## Verification Methods
→ [[../../.claude/skills/task-builder/references/verification-methods.md]]

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| RSCH-01 | Trend validation doc exists | file_exists | `projects/on-prem-llm-pivot-research/01-trend-validation.md` | Re-run task 001 |
| RSCH-02 | Trend claims are sourced | grep | `grep -c "http" 01-trend-validation.md` ≥ 5 | Task 001: add sources — claims must not be assumed |
| RSCH-03 | Solution landscape doc exists | file_exists | `projects/on-prem-llm-pivot-research/02-solution-landscape.md` | Re-run task 002 |
| RSCH-04 | Landscape covers inference stacks | grep | `grep -ciE "vllm\|ollama\|llama.cpp\|tgi\|nim" 02-solution-landscape.md` ≥ 3 | Task 002: cover the major serving stacks |
| RSCH-05 | Isagawa pivot doc exists | file_exists | `projects/on-prem-llm-pivot-research/03-isagawa-pivot-analysis.md` | Re-run task 003 |
| RSCH-06 | Pivot ties to existing assets | grep | `grep -ci "kernel" 03-isagawa-pivot-analysis.md` ≥ 2 | Task 003: analysis must build on Isagawa's assets, not generic ideas |
| RSCH-07 | Skill path doc exists | file_exists | `projects/on-prem-llm-pivot-research/04-personal-skill-path.md` | Re-run task 004 |
| RSCH-08 | Skill path has 30-60-90 plan | grep | `grep -c "30-60-90\|30/60/90\|Day 30\|Days 1-30" 04-personal-skill-path.md` ≥ 1 | Task 004: plan must be time-phased |
| RSCH-09 | Synthesis report exists | file_exists | `projects/on-prem-llm-pivot-research/research-report.md` | Re-run task 005 |
| RSCH-10 | Report has recommendation | grep | `grep -ciE "go / no-go\|go/no-go\|recommendation" research-report.md` ≥ 1 | Task 005: report must state go / no-go / watch |

## Requirements Coverage
Each backlog requirement maps to gates: trend validation → RSCH-01/02, solution landscape → RSCH-03/04, Isagawa pivot → RSCH-05/06, personal skill path → RSCH-07/08, final report + recommendation → RSCH-09/10.
