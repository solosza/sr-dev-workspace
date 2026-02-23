# Step 1: Project Setup

## Goal

Scaffold the RAG project with config, base interfaces, and dependency declarations.

## Actions

1. **Create project structure:**
   ```
   src/
   ├── chunking/
   ├── embedding/
   ├── vector_store/
   ├── retrieval/
   ├── generation/
   ├── evaluation/
   ├── config/
   └── interfaces/        ← Base interface definitions
   tests/
   ├── unit/
   └── integration/
   config/
   └── default.yaml       ← Default configuration
   ```

2. **Implement config spec:**
   - Read `_reference/config-spec.md`
   - Build configuration loader (environment variables + config file)
   - All tunable parameters externalized — no magic numbers in code

3. **Define base interfaces:**
   - Read each `_reference/*-spec.md` for interface contracts
   - Create abstract base classes / protocol definitions for:
     - `ChunkInterface`
     - `EmbeddingInterface`
     - `VectorStoreInterface`
     - `RetrievalInterface`
     - `GenerationInterface`
   - These are the contracts — implementations come in later steps

4. **Declare dependencies:**
   - Core: config loader, logging
   - Embedding: provider SDK (e.g., openai, sentence-transformers)
   - Vector store: client library (e.g., chromadb, pinecone-client)
   - Generation: LLM SDK
   - Testing: pytest + fixtures

## Gate

→ See `gate-contract.md` Step 1 criteria
