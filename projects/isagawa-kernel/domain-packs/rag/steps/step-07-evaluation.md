# Step 7: Build Evaluation Harness

## Goal

Implement quality measurement across faithfulness, relevance, and completeness.

## Spec Reference

→ `_reference/evaluation-spec.md`

## Actions

1. **Read the evaluation spec** — metrics definitions, test harness structure, output format
2. **Implement faithfulness metric** — is the answer grounded in the retrieved context? (no hallucination)
3. **Implement relevance metric** — are the retrieved chunks relevant to the query?
4. **Implement completeness metric** — does the answer address all aspects of the query?
5. **Build test harness** — predefined Q&A pairs with expected answers and source documents
6. **Structured output** — metrics in JSON format for programmatic consumption
7. **Write tests** — verify metric calculations against known good/bad examples

## Key Decisions (Agent Makes During Build)

- Metric implementation: LLM-as-judge, heuristic-based, embedding similarity
- Test dataset: manually curated, synthetic, existing benchmark (e.g., RAGAS)
- Threshold definitions: what score = pass for each metric
- Regression tracking: compare across runs

## Gate

→ See `gate-contract.md` Step 7 criteria
