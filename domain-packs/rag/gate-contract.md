# RAG Gate Contract

Validation rules checked at each step boundary. A step is not complete until its gate passes.

## Gate Rules

### Step 1: Project Setup
- [ ] Project scaffold created (src/, tests/, config/)
- [ ] Dependencies declared (not necessarily installed)
- [ ] Config spec implemented (environment variables, model selection)
- [ ] Base interfaces defined (abstract classes/protocols for each pipeline component)

### Step 2: Chunking Pipeline
- [ ] Implements `ChunkInterface` from spec
- [ ] Handles at least 2 document formats (e.g., plain text, markdown)
- [ ] Chunks include metadata (source, position, token count)
- [ ] Unit tests pass for chunking logic
- [ ] No chunks exceed configured max token limit

### Step 3: Embedding Pipeline
- [ ] Implements `EmbeddingInterface` from spec
- [ ] Provider-agnostic (interface allows swapping models)
- [ ] Handles batching for large document sets
- [ ] Unit tests pass with mock embeddings
- [ ] Embedding dimensions match configured model

### Step 4: Vector Store
- [ ] Implements `VectorStoreInterface` from spec
- [ ] CRUD operations work (create, read, update, delete)
- [ ] Similarity search returns ranked results with scores
- [ ] Metadata filtering supported
- [ ] Integration test passes with real store (local or in-memory)

### Step 5: Retrieval Pipeline
- [ ] Implements `RetrievalInterface` from spec
- [ ] Query → embed → search → rank flow works end-to-end
- [ ] Configurable top-k and similarity threshold
- [ ] Returns chunks with scores and metadata
- [ ] Integration test passes against populated store

### Step 6: Generation Pipeline
- [ ] Implements `GenerationInterface` from spec
- [ ] Context injection into prompt template works
- [ ] Provider-agnostic LLM interface (swap models without code changes)
- [ ] Response includes citation references to source chunks
- [ ] Integration test passes with mock LLM

### Step 7: Evaluation Harness
- [ ] Faithfulness metric implemented (answer grounded in context?)
- [ ] Relevance metric implemented (retrieved chunks relevant to query?)
- [ ] Completeness metric implemented (answer addresses the full query?)
- [ ] Test harness runs against predefined Q&A pairs
- [ ] Results output in structured format (JSON)

## Gate Enforcement

Gates are checked by the agent during `/kernel/anchor` Part B. The domain protocol references this contract — anchor reads it and verifies recent work against the current step's gate.

If a gate fails:
1. Agent identifies which criteria are not met
2. Fixes the issue
3. Re-runs the gate check
4. Proceeds only when all criteria pass
