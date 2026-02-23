# Evaluation Spec

## Metrics

### Faithfulness
**Question:** Is the answer grounded in the retrieved context?
```
Score: 0.0 (hallucinated) to 1.0 (fully grounded)
Method: Check each claim in the answer against source chunks
Pass threshold: >= 0.8
```

### Relevance
**Question:** Are the retrieved chunks relevant to the query?
```
Score: 0.0 (irrelevant) to 1.0 (perfectly relevant)
Method: Score each retrieved chunk against the query
Pass threshold: >= 0.7
```

### Completeness
**Question:** Does the answer address all aspects of the query?
```
Score: 0.0 (misses everything) to 1.0 (fully addresses query)
Method: Decompose query into sub-questions, check coverage
Pass threshold: >= 0.7
```

## Test Harness

### Test Case Format
```
TestCase:
  id: str                          # Unique test ID
  query: str                       # Input question
  expected_answer: str             # Reference answer (for comparison)
  source_documents: list[str]      # Documents that should be retrieved
  expected_chunks: list[str]       # Specific chunks expected in context
  tags: list[str]                  # Categories (e.g., "factual", "multi-hop")
```

### Test Dataset
```
test_data/
├── cases.json             # Test cases (Q&A pairs)
├── documents/             # Source documents for ingestion
└── expected/              # Expected outputs per case
```

### Evaluation Run
```
EvaluationRun:
  timestamp: str
  model: str                       # Generation model used
  embedding_model: str             # Embedding model used
  results: list[CaseResult]
  summary:
    avg_faithfulness: float
    avg_relevance: float
    avg_completeness: float
    pass_rate: float               # Percentage of cases meeting all thresholds
```

## Metric Implementation Options

| Approach | Pros | Cons |
|----------|------|------|
| LLM-as-judge | High quality, flexible | Expensive, slow, non-deterministic |
| Embedding similarity | Fast, cheap | Less nuanced |
| Heuristic (keyword/overlap) | Fastest, deterministic | Lowest quality |

Recommendation: Start with LLM-as-judge for development, add heuristic fallback for CI.

## Configuration

```yaml
evaluation:
  metrics: ["faithfulness", "relevance", "completeness"]
  judge_model: "gpt-4o"           # LLM for judge-based metrics
  thresholds:
    faithfulness: 0.8
    relevance: 0.7
    completeness: 0.7
  output_format: "json"           # "json", "csv", "markdown"
  test_data_path: "./test_data"
```

## Rules

1. Evaluation MUST run end-to-end (ingest → retrieve → generate → score)
2. Results MUST be structured JSON (not just console output)
3. Each metric MUST have a configurable pass threshold
4. Test cases MUST be version-controlled (not generated at runtime)
5. Regression detection: compare current run to previous run's scores
6. `MockGeneration` + `InMemoryStore` enable fast evaluation without API calls
