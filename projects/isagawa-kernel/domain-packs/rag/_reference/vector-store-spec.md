# Vector Store Spec

## Interface Contract

```
VectorStoreInterface:
  method: create_collection(name: str, dimensions: int) → Collection
  method: insert(collection: str, vectors: list[VectorRecord]) → list[str]
  method: get(collection: str, ids: list[str]) → list[VectorRecord]
  method: update(collection: str, records: list[VectorRecord]) → None
  method: delete(collection: str, ids: list[str]) → None
  method: search(collection: str, query_vector: list[float], top_k: int, filters: dict | None) → list[SearchResult]
  method: count(collection: str) → int
```

## Data Types

### VectorRecord (input/output)
```
VectorRecord:
  id: str                 # Unique identifier (matches Chunk.id)
  vector: list[float]     # Embedding vector
  metadata: dict          # Chunk metadata (source, position, content preview)
  content: str            # Original chunk text (for retrieval)
```

### SearchResult (output)
```
SearchResult:
  id: str                 # Record ID
  score: float            # Similarity score (0.0 to 1.0 for cosine)
  content: str            # Original chunk text
  metadata: dict          # Full metadata
```

## Provider Abstraction

```
VectorStoreInterface (abstract)
├── ChromaDBStore          # Local, file-based or in-memory
├── PineconeStore          # Cloud-hosted
├── QdrantStore            # Self-hosted or cloud
├── InMemoryStore          # For testing (dict-based, no persistence)
└── MockStore              # For unit tests (predefined responses)
```

## Configuration

```yaml
vector_store:
  provider: "chromadb"            # "chromadb", "pinecone", "qdrant", "memory", "mock"
  collection_name: "default"       # Default collection name
  distance_metric: "cosine"        # "cosine", "euclidean", "dot_product"
  persist_directory: "./data/vectordb"  # For local stores
```

## Rules

1. `insert` MUST be idempotent — reinserting same ID updates, not duplicates
2. `search` with `top_k=0` MUST return empty list (not error)
3. `filters` use simple key-value matching on metadata fields
4. `InMemoryStore` MUST pass all the same tests as persistent stores
5. Collection dimensions MUST match embedding dimensions (validate on insert)
6. `delete` on non-existent IDs MUST be a no-op (not error)
