# Research Tiered Index Architecture Failure Threshold via A/B Experiment

## Status
Open

## Priority
High — validates the core design pattern (tiered indexing) that all kernel skills are built on

## Summary
Design and run a large-corpus A/B test (60K+ tokens, 3 precision-recall task types, N=5 runs) to find the actual failure point where flat document structure degrades vs tiered indexing. Prior N=3 test at 12K tokens showed no significant difference — both variants scored 0.88-0.99. Research indicates lost-in-the-middle kicks in >8K tokens with >30% degradation (Liu et al. 2024), instruction budget caps at ~150-200 distinct instructions, and RULER benchmarks show 15-30 point drops at 128K. This experiment tests whether tiered indexing produces measurably better scores at scale.

## Requirements
- Concatenate multiple hmsa-healthcare-qa skills (check-data-engine + rule-engine + explain-sql + others) into a single 60K+ token flat corpus
- Tiered variant preserves the natural indexed file structure with wikilinks
- 3 task types exercising different failure modes:
  1. Sequential walkthrough (baseline — should show no difference, same as prior test)
  2. Mid-document precision recall ("which rule applies when X AND Y?" — answer buried mid-document)
  3. Cross-reference retrieval (Step 3 depends on contract defined after Step 7)
- N=5 runs per task per variant (30 Claude calls total, 150 GEval calls)
- Score with gpt-4o as judge (not gpt-4o-mini) for higher accuracy (~$3.26 OpenAI cost)
- Use refactored 5-layer ABMetrics framework from pipeline 172
- Statistical analysis: Cohen's d effect sizes, win rates, per-task-type breakdowns
- Compare results against prior N=3 baseline (12K tokens, no significant difference)

## References
- Prior A/B results: `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/results/ab-report.md`
- Liu et al. 2024 "Lost in the Middle": https://aclanthology.org/2024.tacl-1.9/
- RULER benchmark (NVIDIA): https://github.com/NVIDIA/RULER
- Tiered index design: `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/`
- Refactored AB framework: `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/ab_metrics.py`
- Claude Code best practices (<200 lines, 40K char warning): https://code.claude.com/docs/en/best-practices

## Task Builder Input
- **Deliverable:** Scored A/B report with statistical analysis showing where (if anywhere) tiered indexing outperforms flat at 60K+ token scale, plus per-task-type breakdown
- **Location:** `subproject:tiered-index-threshold-research`
- **Scope:** RESEARCH
- **Constraints:** Requires OPENAI_API_KEY for gpt-4o GEval judging. Uses existing eval-ab-check-data-engine repo. hmsa-healthcare-qa skills must have enough content to reach 60K+ tokens when concatenated. Claude calls via subscription (claude -p).
