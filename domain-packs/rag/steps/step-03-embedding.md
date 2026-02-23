# Step 3: Build Embedding Pipeline

## Goal

Implement embedding generation that converts text chunks into vector representations.

## Spec Reference

→ `_reference/embedding-spec.md`

## Actions

1. **Read the embedding spec** — interface contract, batching requirements, provider abstraction
2. **Implement `EmbeddingInterface`** — concrete class following the spec
3. **Provider-agnostic design** — interface allows swapping embedding models without changing pipeline code
4. **Implement batching** — large document sets must batch API calls (configurable batch size)
5. **Handle rate limits** — retry with backoff for API-based providers
6. **Write unit tests** — mock embeddings, batch logic, dimension validation

## Key Decisions (Agent Makes During Build)

- Default provider: OpenAI, Cohere, local model (sentence-transformers)
- Embedding dimensions: model-dependent, must match vector store config
- Batching strategy: fixed-size batches vs adaptive

## Gate

→ See `gate-contract.md` Step 3 criteria
