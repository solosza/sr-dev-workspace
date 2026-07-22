# SoapInterface — Design Doc

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

**Build from scratch.** No existing reference in any repo. The v2 framework made SOAP calls through the UI (browser-automated SOAP operations). This platform gives SOAP its own Layer 1 interface — direct service invocation without browser mediation.

## SDK

`zeep` 4.x (Python) — industry standard SOAP client. Handles WSDL parsing, type factories, serialization/deserialization, WS-Security. No viable alternative in Python for enterprise SOAP.

## Why zeep

| Option | Verdict | Reason |
|--------|---------|--------|
| `zeep` | CHOSEN | WSDL auto-parsing, type factories, WS-Security plugin, maintained, enterprise-grade |
| `requests` + manual XML | Rejected | No WSDL parsing — you'd rebuild half of zeep manually |
| `suds-community` | Rejected | Fork of abandoned project, limited Python 3 support |
| `xmltodict` + requests | Rejected | No schema validation, no type safety, no WSDL support |

## Constructor

```python
def __init__(self, client: zeep.Client, config: dict, logger: logging.Logger):
```

- `client` — `zeep.Client` instance (created by Driver & Client Factory, 3.5, from WSDL URL + transport settings)
- `config` — dict with `default_timeout`, `strict_mode`, `raw_response`
- `logger` — standard logging.Logger

Same pattern as all other interfaces. The zeep.Client is created externally (factory handles WSDL URL, transport, session, proxy settings). Interface just wraps its operations.

## Method Surface

### Operations
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `call_operation` | `(operation: str, **kwargs) -> Any` | Invoke a SOAP operation by name, return deserialized response |
| `call_service_operation` | `(service: str, port: str, operation: str, **kwargs) -> Any` | Invoke operation on a specific service/port (multi-service WSDLs) |

### Headers & Auth
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `set_soap_header` | `(header: Any) -> None` | Set SOAP header element for subsequent calls |
| `clear_soap_headers` | `() -> None` | Remove all custom SOAP headers |
| `set_wsse_token` | `(username: str, password: str, use_digest: bool = False) -> None` | Add WS-Security UsernameToken |

### Introspection
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `get_operations` | `() -> list[str]` | List all available operations from WSDL |
| `get_service_operations` | `(service: str) -> list[str]` | List operations for a specific service |
| `get_type` | `(type_name: str) -> Any` | Get a zeep type from the WSDL type factory |
| `create_object` | `(type_name: str, **kwargs) -> Any` | Create a typed SOAP object (for complex request params) |

### Raw Access
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `get_raw_response` | `() -> Optional[str]` | Return raw XML from last response (if `raw_response` enabled in config) |
| `get_last_request_xml` | `() -> Optional[str]` | Return raw XML of last sent request |

## Key Design Choices

### 1. Generic operation invocation

SOAP operations are defined by the WSDL — they vary per service. The interface does NOT hardcode any operation names. `call_operation("GetMemberInfo", member_id="12345")` invokes whatever the WSDL defines. Layer 2 API Objects wrap specific operations with domain vocabulary.

### 2. Type factory access

Enterprise SOAP services use complex types (nested objects, arrays of custom types). `get_type` and `create_object` let Layer 2 build typed request objects:

```python
# Layer 2 (API Object) — NOT in the interface
address_type = self.soap.get_type("AddressType")
address = self.soap.create_object("AddressType", street="123 Main", city="Honolulu")
```

The interface just delegates to `client.get_type()` — one SDK call, returns SDK primitive.

### 3. WS-Security built in

Enterprise SOAP services (healthcare, government, finance) commonly require WS-Security. `set_wsse_token` wraps zeep's `wsse.UsernameToken` plugin. No need to import zeep internals at Layer 2+.

### 4. Multi-service WSDL support

Some enterprise WSDLs expose multiple services on different ports. `call_service_operation` handles this. Single-service WSDLs use the simpler `call_operation`.

### 5. Custom transport for raw XML capture

zeep doesn't expose raw request/response XML natively. The Driver & Client Factory (3.5) will create the zeep.Client with a custom `Transport` subclass that captures raw XML on each call. The interface's `get_raw_response()` and `get_last_request_xml()` read from this transport's buffer. This is a well-documented pattern (zeep issue #603).

## Return Types

All methods return **SDK primitives**:
- `Any` — zeep's deserialized response (dicts, lists, strings, numbers — auto-mapped from XML schema)
- `list[str]` — operation names
- `str` — raw XML
- `None` — void operations

zeep auto-deserializes XML responses into Python primitives (dict, list, str, int, datetime). No domain objects needed at Layer 1.

## Naming: trace.py

Layer 1 interfaces log internally via `self.logger` on every operation (contract rule). The `@trace("Task")` decorator (at `resources/utilities/trace.py`) is NOT used at Layer 1 — it would double-log. Only Layer 3+ imports `@trace`.

## Contract Compliance

| Rule | Status |
|------|--------|
| Wraps SDK — no business logic | PASS — wraps zeep.Client |
| Constructor takes SDK instance + config + logger | PASS |
| Config-driven defaults (timeout, strict_mode) | PASS |
| Returns SDK primitives only | PASS — zeep deserialized primitives |
| No knowledge of upper layers | PASS |
| Catches SDK exceptions, logs, re-raises | PASS |
| One SDK call per method | PASS — each method is one client/service call |
| No domain vocabulary | PASS — operation names come from callers |

## Dependencies

- `zeep` (Client, Transport, wsse, exceptions)
- `logging` (stdlib)
- `typing` (stdlib — Any, Optional)

## What Does NOT Go Here

- No WSDL URLs (config via Driver & Client Factory, 3.5)
- No operation-specific wrappers (Layer 2 API Objects)
- No response parsing into domain models (Layer 2)
- No retry/backoff (Layer 2 or conftest plugin)
- No complex request body construction (Layer 2 builds typed objects, passes to interface)
- No endpoint routing logic (Layer 2)
- No multi-step SOAP workflows (Layer 3 Task)
