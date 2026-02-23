# Config Spec

## Purpose

Centralize all tunable parameters. No magic numbers in code — everything reads from config.

## Configuration Hierarchy

```
Priority (highest to lowest):
1. Environment variables       ← Secrets, deployment-specific
2. Config file (YAML)          ← Project defaults
3. Hardcoded defaults          ← Fallback only
```

## Master Config Structure

```yaml
# config/default.yaml

project:
  name: "my-rag-system"
  version: "0.1.0"

chunking:
  strategy: "recursive"
  max_tokens: 512
  overlap_tokens: 50
  min_chunk_tokens: 50
  separators: ["\n\n", "\n", ". ", " "]

embedding:
  provider: "openai"
  model: "text-embedding-3-small"
  dimensions: 1536
  batch_size: 100
  max_retries: 3
  retry_delay_seconds: 1

vector_store:
  provider: "chromadb"
  collection_name: "default"
  distance_metric: "cosine"
  persist_directory: "./data/vectordb"

retrieval:
  default_top_k: 5
  similarity_threshold: 0.7
  reranking: "none"
  hybrid_search: false

generation:
  provider: "openai"
  model: "gpt-4o"
  template: "default"
  max_tokens: 1024
  temperature: 0.1
  include_citations: true

evaluation:
  metrics: ["faithfulness", "relevance", "completeness"]
  judge_model: "gpt-4o"
  thresholds:
    faithfulness: 0.8
    relevance: 0.7
    completeness: 0.7
  output_format: "json"
  test_data_path: "./test_data"
```

## Environment Variables

Secrets MUST NOT appear in config files. Use environment variables:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=us-east-1
```

## Config Loader Interface

```
ConfigLoader:
  method: load(path: str | None) → Config
  method: get(key: str, default: Any) → Any
  method: get_section(section: str) → dict
```

## Rules

1. Config file format MUST be YAML (human-readable, supports comments)
2. Every numeric parameter MUST have a sensible default
3. Secrets MUST come from environment variables (never in YAML)
4. Config MUST be loaded once at startup (not re-read per request)
5. Unknown config keys MUST warn (not silently ignore, not error)
6. Config validation MUST run at startup (fail fast on invalid values)
