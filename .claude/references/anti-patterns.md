# Anti-Patterns

## BLOCK (Hook Enforced)

| Pattern | Detection |
|---------|-----------|
| Debug statements | `console.log`, `print(`, `fmt.Println`, `println!` |
| Hardcoded secrets | `password=`, `secret=`, `api_key=`, `token=` + string |
| Wildcard imports | `import *`, `from x import *` |
| Skipped tests | `.skip`, `@pytest.mark.skip`, `xit(`, `xdescribe(` |
| File > 300 lines | Line count check |

## WARN (Protocol Advisory)

| Pattern | Guidance |
|---------|----------|
| Catch-all exceptions | Review needed - add specific handling |
| TODO comments | Flag before merge |
| Over-engineering | Build only what's needed |
| Premature abstraction | Three similar lines > premature helper |
