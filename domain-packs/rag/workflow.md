# RAG Workflow

## Data Flow

```
Raw Documents
     │
     ▼
┌─────────────┐
│  Chunking   │  Split documents into semantic units
│  Pipeline   │  → chunks with metadata
└─────┬───────┘
      │
      ▼
┌─────────────┐
│  Embedding  │  Convert chunks to vector representations
│  Pipeline   │  → vectors + chunk metadata
└─────┬───────┘
      │
      ▼
┌─────────────┐
│  Vector     │  Store and index embeddings
│  Store      │  → searchable vector database
└─────┬───────┘
      │
      ▼ (at query time)
┌─────────────┐
│  Retrieval  │  Query → embed → similarity search → ranked results
│  Pipeline   │  → relevant chunks with scores
└─────┬───────┘
      │
      ▼
┌─────────────┐
│  Generation │  Context + query → LLM → answer
│  Pipeline   │  → grounded response with citations
└─────┬───────┘
      │
      ▼
┌─────────────┐
│  Evaluation │  Measure quality across dimensions
│  Harness    │  → metrics (faithfulness, relevance, completeness)
└─────────────┘
```

## Step Execution Order

Steps are sequential — each depends on the previous:

```
step-01-setup → step-02-chunking → step-03-embedding → step-04-vector-store
                                                              │
step-07-evaluation ← step-06-generation ← step-05-retrieval ←┘
```

## Interface Boundaries

Each pipeline component communicates through defined interfaces:

| Interface | Producer | Consumer | Contract |
|-----------|----------|----------|----------|
| `ChunkInterface` | Chunking | Embedding | `_reference/chunking-spec.md` |
| `EmbeddingInterface` | Embedding | Vector Store | `_reference/embedding-spec.md` |
| `VectorStoreInterface` | Vector Store | Retrieval | `_reference/vector-store-spec.md` |
| `RetrievalInterface` | Retrieval | Generation | `_reference/retrieval-spec.md` |
| `GenerationInterface` | Generation | Evaluation | `_reference/generation-spec.md` |

The interface-first pattern ensures components can be swapped without breaking the pipeline (e.g., swap OpenAI embeddings for local model, swap Pinecone for ChromaDB).

## Two Phases

**Ingestion phase** (offline): Documents → Chunks → Embeddings → Store
**Query phase** (online): Query → Retrieve → Generate → Evaluate
