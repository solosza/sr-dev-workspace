# Retrieval Spec

## Interface Contract

```
RetrievalInterface:
  method: retrieve(query: str, top_k: int, filters: dict | None) → RetrievalResult
  method: retrieve_with_scores(query: str, top_k: int, threshold: float) → RetrievalResult
```

## Data Types

### RetrievalResult (output)
```
RetrievalResult:
  query: str                      # Original query
  chunks: list[RetrievedChunk]    # Ranked results
  total_candidates: int           # Total vectors searched
  retrieval_time_ms: float        # Time taken for retrieval
```

### RetrievedChunk
```
RetrievedChunk:
  id: str                 # Chunk ID
  content: str            # Chunk text
  score: float            # Similarity score
  rank: int               # Position in results (1-based)
  metadata: dict          # Full chunk metadata (source, position, etc.)
```

## Pipeline Flow

```
Query (str)
  → EmbeddingInterface.embed(query)     # Convert to vector
  → VectorStoreInterface.search(...)     # Find similar vectors
  → rank and filter                       # Apply threshold, re-rank
  → RetrievalResult                       # Structured output
```

## Configuration

```yaml
retrieval:
  default_top_k: 5                 # Default number of results
  similarity_threshold: 0.7        # Minimum score to include
  reranking: "none"                # "none", "cross_encoder", "mmr"
  mmr_lambda: 0.5                  # Diversity vs relevance (0=diverse, 1=relevant)
  hybrid_search: false             # Enable BM25 + vector hybrid
  hybrid_alpha: 0.5                # Weight: 0=keyword only, 1=vector only
```

## Rules

1. Results MUST be sorted by score descending (highest first)
2. `threshold` filtering happens AFTER retrieval (don't limit search, filter results)
3. Empty results MUST return valid `RetrievalResult` with empty `chunks` list
4. `retrieve_with_scores` MUST exclude chunks below `threshold`
5. Retrieval MUST use the same embedding model/provider as ingestion
6. `retrieval_time_ms` MUST be measured (for performance monitoring)
