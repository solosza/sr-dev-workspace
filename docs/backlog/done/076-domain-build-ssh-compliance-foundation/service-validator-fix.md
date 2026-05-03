# ServiceValidator Systemd Fallback

## Status
EXISTS — needs enhancement

## Location
`framework/_reference/validators/service_validator.py`

## Problem
Current implementation only uses `systemctl is-active`. Fails in Docker containers where systemd isn't running (proven in prod-test: service_sshd XFAIL).

## Fix
Add fallback detection: try `systemctl` first, fall back to `pgrep` or `/proc` check.

```python
def _check_service(self, service):
    # Try systemctl first
    result = self.ssh.execute(f"systemctl is-active {service}")
    if result["stdout"].strip() == "active":
        return True, result["stdout"]
    # Fallback: check if process is running
    result = self.ssh.execute(f"pgrep -x {service}")
    if result["passed"]:
        return True, f"running (pid: {result['stdout'].strip()})"
    return False, "not running"
```

## Dependencies
None — standalone fix.
