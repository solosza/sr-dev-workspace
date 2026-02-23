# Step 5: Build Retrieval Pipeline

## Goal

Implement the query-time retrieval flow: query → embed → search → rank.

## Spec Reference

→ `_reference/retrieval-spec.md`

## Actions

1. **Read the retrieval spec** — interface contract, ranking strategies, configuration
2. **Implement `RetrievalInterface`** — concrete class following the spec
3. **Query pipeline** — accept natural language query, embed it, search vector store, return ranked results
4. **Configurable parameters** — top-k count, similarity threshold, metadata filters
5. **Result format** — chunks with similarity scores, source metadata, position info
6. **Write integration tests** — populate store with known data, query, verify ranking

## Key Decisions (Agent Makes During Build)

- Re-ranking strategy: none, cross-encoder, MMR (maximal marginal relevance)
- Hybrid search: pure vector vs vector + keyword (BM25)
- Query preprocessing: expansion, decomposition, none

## Gate

→ See `gate-contract.md` Step 5 criteria
