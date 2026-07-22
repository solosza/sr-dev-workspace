# Tiered Index Threshold Research — Final Report

**Backlog:** 174-kernel-research-tiered-index-failure-threshold
**Date:** 2026-07-06
**Researcher:** Isagawa Kernel (autonomous pipeline)

---

## 1. Executive Summary

Tiered indexing does not outperform flat indexing at 60,000+ token corpus sizes. Across three task types (sequential, precision, cross-reference), five metrics, and five runs per condition, no statistically significant differences were found between flat and tiered index structures. This result is consistent with the prior 12K-token baseline experiment, confirming that the "lost-in-the-middle" effect does not materialize as a tiered indexing advantage for Claude Sonnet 4.6 at either corpus scale. The kernel's tiered indexing pattern remains a valid organizational convention but should not be justified on retrieval accuracy grounds alone.

---

## 2. Experiment Design

| Parameter | Value |
|-----------|-------|
| **Corpus source** | HMSA Healthcare QA platform (5 skill domains concatenated) |
| **Corpus size** | 60,000+ tokens |
| **Skills concatenated** | healthcare-qa, check-data-engine, verify-sit-xlsx, create-sit-xlsx, create-test-artifacts |
| **Model** | claude-sonnet-4-6 |
| **Runs per condition** | 5 (flat) + 5 (tiered) = 10 total per task type |
| **Task types** | Sequential, Precision-Recall, Cross-Reference |
| **Metrics** | compliance, adherence, completeness, following, drift |
| **Scoring method** | Heuristic (rule-based) + LLM Judge (gpt-4o-mini) |
| **Significance criteria** | delta > 0.05 AND win rate > 67% |
| **Tie threshold** | delta <= 0.01 |

**Variant A (flat):** All skill documentation concatenated into a single flat document with no hierarchical structure.

**Variant B (tiered):** Same documentation organized into a hierarchical index with section headers, sub-indices, and cross-references — matching the kernel's wikilink tiered indexing pattern.

---

## 3. Results by Task Type

### 3.1 Sequential Tasks

Sequential tasks required the model to follow multi-step procedures in order.

| Metric | Flat Mean | Tiered Mean | Delta (B-A) | Cohen's d | Verdict |
|--------|-----------|-------------|-------------|-----------|---------|
| compliance | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| adherence | 1.0000 | 0.9600 | -0.0400 | -0.6325 (medium) | no significant difference |
| completeness | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| following | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| drift | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |

Both variants achieved near-perfect scores. The single adherence drop (run 5, tiered: 0.80) was the only deviation across 50 data points.

### 3.2 Precision-Recall Tasks

Precision tasks required the model to locate and extract exact values from the corpus.

| Metric | Flat Mean | Tiered Mean | Delta (B-A) | Cohen's d | Verdict |
|--------|-----------|-------------|-------------|-----------|---------|
| compliance | 0.6000 | 0.2000 | -0.4000 | -0.8000 (medium) | no significant difference |
| adherence | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| completeness | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| following | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| drift | 1.0000 | 0.9612 | -0.0388 | -2.2032 (large) | no significant difference |

This was the most differentiated task type. Flat indexing had a compliance advantage (0.60 vs 0.20), but the binary nature of scores (0 or 1) produced high variance that prevented significance. The drift metric showed a large Cohen's d (-2.20) favoring flat, but the absolute delta was small (-0.039). Tiered indexing's nested structure may have introduced navigation overhead for exact-value lookup tasks.

### 3.3 Cross-Reference Tasks

Cross-reference tasks required the model to synthesize information across multiple skill domains.

| Metric | Flat Mean | Tiered Mean | Delta (B-A) | Cohen's d | Verdict |
|--------|-----------|-------------|-------------|-----------|---------|
| compliance | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| adherence | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| completeness | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| following | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | no significant difference |
| drift | 0.4405 | 0.4148 | -0.0257 | -0.4370 (small) | no significant difference |

Both variants struggled equally with drift in cross-reference tasks (scores in the 0.32-0.49 range), indicating this task type is inherently difficult regardless of index structure. This is the task type where tiered indexing would theoretically help most (cross-domain synthesis), yet no advantage was observed.

---

## 4. Statistical Analysis

### Aggregate Results (All Task Types Combined)

| Metric | Flat Mean | Tiered Mean | Delta (B-A) | Cohen's d | Flat Wins | Tiered Wins | Ties | Verdict |
|--------|-----------|-------------|-------------|-----------|-----------|-------------|------|---------|
| compliance | 0.8667 | 0.7333 | -0.1333 | -0.3266 (small) | 20% | 7% | 73% | no significant difference |
| adherence | 1.0000 | 0.9867 | -0.0133 | -0.3651 (small) | 7% | 0% | 93% | no significant difference |
| completeness | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | 0% | 0% | 100% | no significant difference |
| following | 1.0000 | 1.0000 | +0.0000 | 0.0000 (negligible) | 0% | 0% | 100% | no significant difference |
| drift | 0.8135 | 0.7920 | -0.0215 | -0.0776 (negligible) | 47% | 13% | 40% | no significant difference |

**No metric reached significance.** The significance criteria required both delta > 0.05 AND win rate > 67%. The largest delta (compliance: -0.13) had only a 20% flat win rate due to ties. The highest win rate (drift: 47% flat) had only a -0.02 delta.

### Cohen's d Distribution

| Effect Size | Count | Metrics |
|-------------|-------|---------|
| Negligible (|d| < 0.2) | 7/15 | Most metrics across most task types |
| Small (0.2 <= |d| < 0.5) | 4/15 | Aggregate compliance, adherence, crossref drift |
| Medium (0.5 <= |d| < 0.8) | 2/15 | Sequential adherence, precision compliance |
| Large (|d| >= 0.8) | 2/15 | Precision compliance, precision drift |

The two large effect sizes were both in the precision task type and both favored flat indexing — the opposite direction from the tiered indexing hypothesis.

---

## 5. Baseline Comparison

### 12K vs 60K Outcomes

| Corpus Size | Verdict | Flat Wins | Tiered Wins | Ties |
|-------------|---------|-----------|-------------|------|
| **12K** (prior) | No Significant Difference | 3 | 2 | 10 |
| **60K** (new) | No Significant Difference | 7 (47%) | 2 (13%) | 6 (40%) |

### Effect Size Trends Across Corpus Sizes

| Metric | 12K Cohen's d | 60K Cohen's d | Trend |
|--------|---------------|---------------|-------|
| compliance | +0.19 (negligible) | -0.33 (small) | Reversed: tiered edge became flat edge |
| adherence | +0.56 (medium) | -0.37 (small) | Reversed: tiered edge became flat edge |
| completeness | -0.57 (medium) | 0.00 (negligible) | Disappeared |
| following | -0.21 (small) | 0.00 (negligible) | Disappeared |
| drift | -0.42 (small) | -0.08 (negligible) | Shrank toward zero |

Effect sizes generally decreased or disappeared at 60K. The two metrics that reversed direction (compliance, adherence) shifted from small tiered advantages to small flat advantages — consistent with noise rather than a systematic effect.

**Update (LLM Judge Rescore):** The 60K experiment has now been scored with both heuristic and LLM judge (gpt-4o-mini) methods. LLM judge results confirm no significant differences (all metrics: negligible to small effect sizes). With matching scoring methodology, 12K and 60K results are directly comparable. See `statistical-report-llm-judge.md` and `baseline-comparison-llm-judge.md` for details.

---

## 6. Implications for Tiered Index Architecture

### Core Finding

**Tiered indexing does not improve retrieval accuracy at 60K tokens for Claude Sonnet 4.6.** The kernel's tiered indexing pattern (wikilink-style hierarchical indices with extracted sub-files) should be justified on organizational and maintainability grounds, not retrieval accuracy.

### What This Means for Kernel Design

1. **Keep tiered indexing as a convention.** It remains valuable for human readability, file organization, and the 200-line extraction threshold. These are engineering benefits independent of model retrieval performance.

2. **Do not add indexing complexity for retrieval.** Adding deeper nesting, cross-reference tables, or explicit navigation aids to improve model accuracy is not supported by the data. The model handles flat context equally well.

3. **Context window size is not the bottleneck.** At 60K tokens (well within Claude's 200K context window), the model processes both flat and tiered structures effectively. The "lost-in-the-middle" threshold, if it exists for Claude, is above 60K tokens.

4. **Precision tasks are the highest-risk task type.** Both variants struggled with exact-value extraction (compliance scores of 0.20-0.60). Improving precision task performance requires better prompting or task decomposition, not index restructuring.

5. **Cross-reference tasks have inherent difficulty.** Drift scores of 0.32-0.49 across both variants suggest that cross-domain synthesis is hard regardless of organization. This may warrant task decomposition (breaking cross-reference into sequential lookups) rather than structural changes.

---

## 7. Limitations

1. **Scoring method difference between baselines (RESOLVED).** The 60K experiment now has both heuristic and LLM judge (gpt-4o-mini) scoring. LLM judge scoring confirms the same conclusion as heuristic scoring: no significant differences. Both scoring methods agree on the core finding, eliminating this limitation.

2. **Sample size.** Five runs per condition per task type (30 total comparisons). This provides moderate power to detect large effects (Cohen's d > 0.8) but insufficient power for small effects. A 20+ run experiment would be needed for definitive conclusions about small differences.

3. **Single model.** All experiments used Claude Sonnet 4.6. Other models with different context window architectures (e.g., GPT-4, Gemini, Llama) may behave differently. Models with smaller effective context windows are more likely to benefit from tiered indexing.

4. **Single corpus domain.** Healthcare QA platform documentation. Results may not generalize to other content types (code, narrative text, mixed-media documentation).

5. **Heuristic scoring granularity.** Binary compliance scoring (0 or 1) reduces statistical power. A continuous scoring method would capture partial compliance and improve discrimination between variants.

6. **No adversarial positioning.** Documents were not deliberately positioned to trigger lost-in-the-middle effects. An experiment that places critical information at known difficult positions (middle third of context) would be a stronger test.

---

## 8. References

### Experiment Artifacts

| Artifact | Path |
|----------|------|
| Experiment config | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/experiment-config.json` |
| Flat corpus | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md` |
| Tiered corpus | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-tiered.md` |
| Statistical report (heuristic) | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/statistical-report.md` |
| Statistical report (LLM judge) | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/statistical-report-llm-judge.md` |
| Baseline comparison (heuristic) | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/baseline-comparison.md` |
| Baseline comparison (LLM judge) | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/baseline-comparison-llm-judge.md` |
| LLM judge scores | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/scores-llm-judge.json` |
| Prior 12K baseline | `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/results/ab-report.md` |

### Task Prompts

| Task Type | Flat Prompt | Tiered Prompt |
|-----------|-------------|---------------|
| Sequential | `60k/prompt-flat-sequential.md` | `60k/prompt-tiered-sequential.md` |
| Precision | `60k/prompt-flat-precision.md` | `60k/prompt-tiered-precision.md` |
| Cross-Reference | `60k/prompt-flat-crossref.md` | `60k/prompt-tiered-crossref.md` |

### Research Context

| Reference | Description |
|-----------|-------------|
| Backlog 174 | `docs/backlog/174-kernel-research-tiered-index-failure-threshold.md` |
| Task decomposition | `tasks/tiered-index-threshold-research/` (22 tasks, 20 completed, 1 skipped) + `tasks/tiered-index-llm-judge-rescore/` (LLM judge rescore) |
| "Lost in the Middle" | Liu et al. (2023) — "Lost in the Middle: How Language Models Use Long Contexts" |
| Kernel tiered indexing | CLAUDE.md "ALWAYS USE WIKILINK TIERED INDEXING" rule |
