# Fraud Detector — Traditional App Architecture Analysis

## Overview

The government fraud detector (`D:\my_ai_projects\fraud-detection-app`) is a Python application built by the kernel via task-builder. It's a 7-layer investigation pipeline that scans public government spending data (USASpending.gov, IRS 990, SAM.gov, OFAC) to detect fraud patterns and generate evidence packages for qui tam whistleblower filings.

Built across 39 tasks in 10 phases. Runs as a scheduled pipeline via `run-task.sh` / cron.

## Code Structure

```
fraud-detection-app/
├── src/
│   ├── apis/           # 4 API clients (USASpending, ProPublica 990, SAM.gov, OFAC SDN)
│   │   └── base_client.py   # Shared: rate limiting, retries, caching, error handling
│   ├── patterns/       # Pattern library (22+ fraud patterns) + scanner + check functions
│   ├── scoring/        # Risk scorer (composite scoring) + materiality filter (3-tier: LOW/MEDIUM/HIGH)
│   ├── entity/         # Entity profiler + network analyzer (cross-entity relationship mapping)
│   ├── evidence/       # Evidence archiver, package builder, FinCEN tip generator, channel router
│   └── pipeline/       # 7 layers (L0-L6) + pipeline_runner.py orchestrator
├── config/settings.py  # API URLs, keys (env vars), rate limits, focus sectors (NTEE codes)
├── tests/              # conftest.py + test_usaspending.py + test_risk_scorer.py
├── data/cache/         # API response cache (24hr TTL)
├── evidence-packages/  # Generated evidence packages
├── research/           # Attorney research (qui tam firms)
├── tasks/daily-scan/   # Kernel task files for daily cron execution
├── run-task.sh         # Kernel execution script
└── requirements.txt    # pydantic, requests, etc.
```

**34 Python source files** across 6 packages. Traditional layered architecture with clear separation of concerns.

## Runtime Independence

The fraud detector is fully runtime-independent:

- **Runs without the agent:** `python -m src.pipeline.pipeline_runner` executes the full pipeline. No LLM needed at runtime.
- **Scheduled execution:** Designed for `cron → run-task.sh → pipeline_runner.py`. The agent built it, but the agent doesn't run it.
- **Standard dependencies:** `requests`, `pydantic`, Python stdlib. No MCP tools, no agent context window, no skill files.
- **Persistent state:** Uses filesystem (`data/cache/`, `evidence-packages/`, `data/reports/`) for state between runs. Not dependent on agent memory.
- **Configuration:** Environment variables for API keys, `config/settings.py` for constants. Standard 12-factor app pattern.

## Testing Model

- **Level 2:** Unit tests via pytest — `test_usaspending.py`, `test_risk_scorer.py` with mock fixtures in `conftest.py`
- **Level 3:** `039-test-l3-mini-pipeline-run.md` — end-to-end pipeline execution with real (or mock) API responses
- Tests are deterministic, repeatable, CI-ready — no agent judgment required to verify correctness

## Architectural Characteristics

| Characteristic | Fraud Detector | Website Cloner (for comparison) |
|---------------|---------------|--------------------------------|
| **Runtime** | Python process (`pipeline_runner.py`) | Agent context window |
| **State** | Filesystem (cache, reports, evidence) | Agent working memory |
| **Dependencies** | `pip install -r requirements.txt` | Playwright MCP tools |
| **Testing** | pytest (deterministic) | Agent visual comparison |
| **Error handling** | try/except, logging, APIError class | Prose-described fallback strategies |
| **Scheduling** | cron + run-task.sh | Manual `/clone` invocation |
| **Code volume** | ~34 Python files, ~3000+ lines | 0 lines of code (markdown only) |
| **Composability** | High — import any module independently | Low — monolithic 6-stage pipeline |
| **Modification** | Code change → test → deploy | Edit markdown instruction |

## Could This Have Been a Skill Instead?

**Partially, but with significant losses.**

What a skill version would look like:
- Agent reads USASpending API docs, calls `WebFetch` to pull awards
- Agent reasons about fraud patterns against each entity
- Agent generates evidence package as markdown/JSON
- No Python code, no tests, no cron — agent IS the pipeline

What would be lost:
1. **Deterministic execution:** The fraud detector runs identically every time. A skill-based version would produce variable results based on agent reasoning variance.
2. **Scheduling:** Can't cron-schedule an agent skill. The whole point is daily unattended scanning.
3. **Scale:** Processing thousands of awards per day requires rate-limited batch API calls with caching. Agent tool calls are ~100x slower than `requests.get()` with connection pooling.
4. **Testability:** pytest tests verify the scorer, pattern matcher, and API clients work correctly. A skill has no equivalent — you'd need the agent to self-verify, which is the QA model the website-cloner uses (and which is less reliable).
5. **Composability:** Other code can `from src.scoring.risk_scorer import RiskScorer`. A skill's logic lives in prose instructions — not importable.
6. **Evidence integrity:** Evidence packages need SHA-256 hashes, timestamps, and archival. These are deterministic operations that belong in code, not agent judgment.

What a skill version would GAIN:
1. **Judgment on novel patterns:** An agent could identify fraud patterns that aren't in the pattern library. The code can only match patterns it was programmed to detect.
2. **Natural language evidence narratives:** The case builder could write more compelling narratives than template-filled Markdown.
3. **Adaptive investigation:** An agent could decide to dig deeper on a suspicious entity, following leads that weren't pre-programmed as pipeline layers.

## Key Insight for Architecture Research

The fraud detector represents the **opposite end of the spectrum from the website-cloner**: maximum traditional code, minimum agent involvement at runtime. The agent's role is purely generative (build the code) not operational (run the pipeline).

This is the correct architecture for this problem because:
- **High volume:** Thousands of awards/day can't go through agent tool calls
- **Deterministic correctness:** Fraud scoring must be reproducible for legal proceedings
- **Unattended operation:** Daily cron requires no human or agent in the loop
- **Auditability:** Python code can be reviewed by attorneys; agent reasoning traces cannot

The hybrid opportunity: Layer 0 (pattern discovery) and Layer 6 (case builder) are where agent judgment would add the most value — discovering new fraud patterns from news/PACER, and writing compelling evidence narratives. These could be skill-augmented layers while keeping L1-L5 as deterministic code.
