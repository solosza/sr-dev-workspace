# Build RAGA (RAG Assessment) Domain Spec

## Status
Open

## Priority
Medium

## Summary
Build a domain spec for RAG Assessment (RAGA) — focused evaluation of Retrieval-Augmented Generation pipelines. Uses the DeepEval spec (`isagawa-qa/platform-deepeval-spec`) as the template since the architecture is identical: 5-layer eval framework, metric selection, golden datasets, pytest runner.

## Why This Is Its Own Spec
The DeepEval spec is a general-purpose LLM evaluation platform covering RAG, Chat, Agent, and Conversational pipelines. RAGA narrows the scope to RAG-specific concerns:
- Retrieval quality (precision, recall, relevance)
- Chunking strategy evaluation
- Context window utilization
- Hallucination detection specific to retrieved context
- End-to-end RAG pipeline scoring (retrieval → generation → faithfulness)

A dedicated spec means tighter gates, RAG-specific metrics by default, and a workflow optimized for the retrieval→generation pipeline rather than generic LLM eval.

## Template
**Source:** `C:\Users\solos\my_ai_projects\platform-deepeval-spec`

Reuse from DeepEval spec:
| Component | Reuse | Adapt |
|-----------|-------|-------|
| SKILL.md | Structure, philosophy | Identity, vocabulary, RAG-specific rules |
| workflow.md | 5-step pipeline | Metric selection defaults to RAG metrics only |
| gate-contract.md | Gate structure, HITL protocol | RAG-specific quality gates |
| steps/ | All 7 step files | step-03 metric selection narrowed to RAG |
| references/metric-catalog.md | Format | RAG metrics only: Faithfulness, ContextualRelevancy, ContextualRecall, ContextualPrecision, AnswerRelevancy, Hallucination |
| references/architecture.md | 5-layer pattern | RAG-specific examples per layer |
| framework/_reference/ | Layer pattern | RAG-only implementations |

## RAG-Specific Metrics
| Metric | What It Measures |
|--------|-----------------|
| Faithfulness | Is the answer grounded in retrieved context? |
| ContextualRelevancy | Is the retrieved context relevant to the question? |
| ContextualRecall | Did retrieval find all relevant information? |
| ContextualPrecision | Is retrieved context free of noise/irrelevant chunks? |
| AnswerRelevancy | Does the generated answer address the question? |
| Hallucination | Does the answer contain claims not in the context? |

## RAG-Specific Workflow Additions
- **Chunking analysis step** — evaluate chunk size, overlap, and strategy impact on retrieval quality
- **Retrieval-only mode** — score retrieval without generation (isolate retrieval issues)
- **Golden dataset format** — requires `retrieval_context` field (not optional like in general DeepEval)
- **Threshold defaults** — stricter for faithfulness (0.8 vs 0.7) since RAG pipelines should be grounded

## Implementation Steps
- [ ] Clone DeepEval spec structure into new repo
- [ ] Strip non-RAG metrics and pipeline types
- [ ] Add RAG-specific gates (retrieval_context required, chunking analysis)
- [ ] Build RAG-only reference implementations
- [ ] Build golden dataset templates for RAG evaluation
- [ ] Test with a real RAG pipeline
- [ ] Package for marketplace

## Output
- Repo: `isagawa-qa/raga-spec` (or `platform-raga-spec`)
- Drop-in domain spec for any kernel-enabled repo with a RAG pipeline

## References
- DeepEval spec: `C:\Users\solos\my_ai_projects\platform-deepeval-spec`
- DeepEval docs: https://docs.confident-ai.com
- RAGAS framework (prior art): https://docs.ragas.io

## Task Builder Input
- **Deliverable:** RAGA domain spec repo (`isagawa-qa/platform-raga-spec`) cloned from DeepEval template, RAG-only metrics, stricter faithfulness thresholds, chunking analysis step
- **Scope:** BUILD
- **Constraints:** Template: `C:/Users/solos/my_ai_projects/platform-deepeval-spec`. Must strip non-RAG metrics. Test with a real RAG pipeline. Package for marketplace.
