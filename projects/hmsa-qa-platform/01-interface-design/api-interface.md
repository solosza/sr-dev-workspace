# ApiInterface (REST) — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 1 rules apply:
- Wraps the SDK — no business logic, no domain vocabulary
- Constructor takes SDK instance + config + logger
- Config-driven defaults (timeouts, headers)
- Returns SDK primitives only — never domain objects
- No knowledge of layers above
- Catches SDK exceptions, logs, re-raises — never swallows
- One SDK call per method
- Module-level docstring states file purpose and layer
- Class docstring lists structural rules as bullet points
- Docstring on every method
- Inline comments only where explanation is needed
- Methods organized by category with section headers (`# === CATEGORY ===`)
- Type hints on all parameters and return types
- Logging on every operation
- Constants as class-level attributes, config-driven defaults via constructor
- Composition over inheritance — no subclassing
- PEP 8 + SOLID (by reference)

## Decision

Translate from `platform-playwright/framework/interfaces/api-client.ts` (336 lines TypeScript) to Python. The TypeScript version is already 5-layer contract compliant. Python SDK: `requests` (industry standard, synchronous, simple).

## SDK

`requests` 2.x (Python) — not `httpx`, not `aiohttp`. Synchronous is fine for test automation. If async needed later, swap to `httpx` (same API surface).

## Translation from TypeScript

| TypeScript (Playwright) | Python (requests) | Notes |
|------------------------|-------------------|-------|
| `APIRequestContext` | `requests.Session` | Session gives connection pooling, cookie persistence, base headers |
| `ApiConfig` interface | `config: dict` | Same as BrowserInterface — dict from conftest fixture |
| `ApiResponseData<T>` | `ApiResponse` dataclass or dict | Structured response with status, headers, body, response_time |
| `async/await` | Synchronous calls | No async needed for test automation |
| `request.get(url, {...})` | `self.session.get(url, **kwargs)` | requests Session API |
| Generic `<T>` return type | `dict` / `str` body | Python — JSON auto-parsed to dict, else raw text |
| `Logger` class | `logging.Logger` | Same as BrowserInterface |

## Method Surface

### Authentication
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `set_auth_token` | `(token: str) -> None` | Sets Bearer token for subsequent requests |
| `clear_auth_token` | `() -> None` | Removes auth token |
| `set_basic_auth` | `(username: str, password: str) -> None` | Sets Basic auth on session |

### HTTP Methods
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `get` | `(endpoint, headers?, params?, timeout?) -> ApiResponse` | GET request |
| `post` | `(endpoint, data?, json?, headers?, timeout?) -> ApiResponse` | POST request |
| `put` | `(endpoint, data?, json?, headers?, timeout?) -> ApiResponse` | PUT request |
| `patch` | `(endpoint, data?, json?, headers?, timeout?) -> ApiResponse` | PATCH request |
| `delete` | `(endpoint, data?, json?, headers?, timeout?) -> ApiResponse` | DELETE request |

### Response Helpers
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `assert_status` | `(response, expected: int) -> None` | Raises if status != expected |
| `assert_status_in` | `(response, expected: list[int]) -> None` | Raises if status not in set |

### Utility
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `get_last_response_time` | `() -> float` | Returns timing of last request (seconds) |

## Constructor

```python
def __init__(self, session: requests.Session, config: dict, logger: logging.Logger):
```

- `session` — `requests.Session` instance (created by Driver & Client Factory, 3.5)
- `config` — dict with `base_url`, `default_timeout`, `default_headers`
- `logger` — standard logging.Logger

Same pattern as BrowserInterface: SDK instance + config + logger.

## Return Type: ApiResponse

```python
@dataclass
class ApiResponse:
    status: int
    headers: dict
    body: Any          # dict if JSON, str if text
    response_time: float  # seconds
```

This is an SDK primitive (structured data from the HTTP response) — not a domain object. Contract compliant.

## What's Different from the TypeScript Version

| Aspect | TypeScript | Python | Why |
|--------|-----------|--------|-----|
| SDK | Playwright APIRequestContext | requests.Session | Playwright is browser-centric; requests is the Python standard for HTTP |
| Async | async/await everywhere | Synchronous | Test automation doesn't need async — simpler, easier to debug |
| `data` vs `json` param | Single `data` field | Both `data` (form) and `json` (JSON body) | requests convention — `json=` auto-serializes + sets Content-Type |
| Basic auth | Not in TS version | Added `set_basic_auth()` | Common in enterprise APIs (SOAP services, legacy systems) |
| Generic types | `<T>` on methods | `Any` body in dataclass | Python typing doesn't benefit from generics here — tests assert on the body anyway |

## Contract Compliance

| Rule | Status |
|------|--------|
| Wraps SDK — no business logic | PASS — wraps requests.Session |
| Constructor takes SDK instance + config + logger | PASS |
| Config-driven defaults (timeout, headers) | PASS |
| Returns SDK primitives only | PASS — ApiResponse is structured HTTP data |
| No knowledge of upper layers | PASS |
| Catches SDK exceptions, logs, re-raises | PASS |
| One SDK call per method | PASS — each HTTP method is one `session.get/post/etc` call |
| No domain vocabulary | PASS — endpoints come from Layer 2 API Objects |

## Dependencies

- `requests` (Session, Response, exceptions)
- `logging` (stdlib)
- `dataclasses` (stdlib — ApiResponse)
- `typing` (stdlib — Any, Optional)
- `time` (stdlib — response timing)

## Security

- **SSL verification ON by default** — `verify=True` is the requests.Session default. Never disable globally. If a test environment uses self-signed certs, `verify` is toggled per-environment via config (3.1), not hardcoded to `False`.
- **Credentials never logged** — auth tokens and Basic auth headers are set on the session but never appear in log output. Logging strategy (3.8) masks Authorization headers.
- **No credential storage** — interface receives session with auth already configured (or sets via `set_auth_token`). Never reads credentials from files or env vars directly.

## What Does NOT Go Here

- No endpoint URLs (those live in Layer 2 API Objects)
- No request body schemas (Layer 2)
- No pagination logic (Layer 2 PaginationComponent)
- No retry/backoff (Layer 2 or conftest/plugin level)
- No OAuth flows (Layer 2 AuthComponent)
- No response parsing into domain models (Layer 2)
