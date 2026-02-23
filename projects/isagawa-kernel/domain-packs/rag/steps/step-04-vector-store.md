# Step 4: Set Up Vector Store

## Goal

Implement vector storage and indexing with CRUD operations and similarity search.

## Spec Reference

→ `_reference/vector-store-spec.md`

## Actions

1. **Read the vector store spec** — interface contract, operations, metadata filtering
2. **Implement `VectorStoreInterface`** — concrete class following the spec
3. **CRUD operations** — create collection, insert vectors, read by ID, update, delete
4. **Similarity search** — top-k nearest neighbors with configurable distance metric
5. **Metadata filtering** — filter results by chunk metadata (source, date, category)
6. **Write integration tests** — use in-memory or local store for testing

## Key Decisions (Agent Makes During Build)

- Store choice: ChromaDB (local), Pinecone (cloud), Qdrant, Weaviate
- Distance metric: cosine, euclidean, dot product
- Index type: flat, IVF, HNSW (depends on store)

## Gate

→ See `gate-contract.md` Step 4 criteria
