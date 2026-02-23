# RAG Reference Architecture

## Overview

This directory contains markdown specifications for building a RAG system. These are **build specs**, not reference code — the agent reads them and builds implementations from scratch.

## Architecture

```
┌──────────────────────────────────────────────────────┐
│                    RAG Pipeline                       │
│                                                       │
│  Ingestion (offline):                                │
│    Documents → Chunking → Embedding → Vector Store    │
│                                                       │
│  Query (online):                                      │
│    Query → Retrieval → Generation → Response          │
│                                                       │
│  Quality:                                             │
│    Evaluation Harness (faithfulness, relevance,       │
│    completeness)                                      │
└──────────────────────────────────────────────────────┘
```

## Spec Index

| Spec | What It Defines |
|------|----------------|
| [`chunking-spec.md`](chunking-spec.md) | Document splitting strategies, metadata format, token limits |
| [`embedding-spec.md`](embedding-spec.md) | Vector encoding interface, batching, provider abstraction |
| [`vector-store-spec.md`](vector-store-spec.md) | Storage interface, CRUD, similarity search, metadata filtering |
| [`retrieval-spec.md`](retrieval-spec.md) | Query pipeline, ranking, configurable parameters |
| [`generation-spec.md`](generation-spec.md) | LLM interface, prompt templates, citation format |
| [`evaluation-spec.md`](evaluation-spec.md) | Quality metrics, test harness, structured output |
| [`config-spec.md`](config-spec.md) | Environment config, tuning parameters, provider selection |

## Design Principles

- **Interface-first** — Define the contract, then build the implementation
- **Provider-agnostic** — Swap embedding models, LLMs, vector stores without code changes
- **Spec-driven** — Markdown specs, not reference code. Agent builds from description.
- **Composable** — Each component is independent, connected through interfaces

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Hardcoded provider (e.g., `openai.embed()` everywhere) | Can't swap models, vendor lock-in |
| Chunking without metadata | Can't trace answers back to sources |
| No evaluation harness | No way to measure quality or catch regressions |
| Monolithic pipeline class | Can't test, swap, or improve individual components |
| Magic numbers in code (chunk size, top-k, threshold) | Must externalize all tuning parameters to config |
