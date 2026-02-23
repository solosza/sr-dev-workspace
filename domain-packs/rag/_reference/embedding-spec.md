# Embedding Spec

## Interface Contract

```
EmbeddingInterface:
  method: embed(text: str) → list[float]
  method: embed_batch(texts: list[str]) → list[list[float]]
  property: dimensions → int
  property: model_name → str
```

## Provider Abstraction

The interface MUST be provider-agnostic. Concrete implementations wrap specific providers:

```
EmbeddingInterface (abstract)
├── OpenAIEmbedding        # text-embedding-3-small, text-embedding-3-large
├── CohereEmbedding        # embed-english-v3.0
├── LocalEmbedding         # sentence-transformers (runs locally)
└── MockEmbedding          # For testing (returns deterministic vectors)
```

Selection is via config — no provider-specific code in the pipeline.

## Batching

- `embed_batch` MUST handle lists larger than API batch limits
- Auto-split into sub-batches of configurable size (default: 100)
- Rate limit handling: exponential backoff with configurable max retries
- Progress reporting for large batch jobs (optional)

## Output Format

```
EmbeddingResult:
  vector: list[float]     # Dense vector of `dimensions` length
  model: str              # Model used for this embedding
  token_count: int        # Tokens consumed by this embedding call
```

## Configuration

```yaml
embedding:
  provider: "openai"               # "openai", "cohere", "local", "mock"
  model: "text-embedding-3-small"  # Provider-specific model name
  dimensions: 1536                  # Expected output dimensions
  batch_size: 100                   # Max items per API call
  max_retries: 3                    # Retry count for transient failures
  retry_delay_seconds: 1            # Initial backoff delay
```

## Rules

1. `embed` and `embed_batch` MUST return vectors of exactly `dimensions` length
2. Empty string input MUST raise an error (not return zero vector)
3. `MockEmbedding` MUST be deterministic — same input = same output
4. Provider switch MUST NOT require any pipeline code changes
5. Token counting MUST be available before embedding (to check limits)
