# Step 5: Set Up Test Infrastructure (MANDATORY)

Create a live test target. This step is NEVER skipped. Every prod-test needs real infrastructure.

**If you skip this step, you are not running a prod-test. You are running unit tests in a copied folder.**

## Process

1. **Read the infra type** determined in Step 1 (from Interface class analysis).

2. **Create infra directory:**
   ```bash
   mkdir -p [test_path]/_test/docker
   ```

3. **Generate infrastructure dynamically** based on infra type.

## Infrastructure Generation by Type

### `docker-ssh` (paramiko / SSH platforms)

**What to generate:**
```
_test/docker/Dockerfile
_test/docker/docker-compose.yml
_test/docker/test_key       (private)
_test/docker/test_key.pub   (public)
_test/docker/test_config.json
```

**Dockerfile pattern:**
```dockerfile
FROM rockylinux:9
# Install SSH + standard security packages
RUN dnf install -y openssh-server openssh-clients audit aide firewalld && \
    dnf clean all
# Configure SSH
RUN ssh-keygen -A && \
    mkdir -p /run/sshd
# Create test user with key auth
RUN useradd -m testuser && \
    mkdir -p /home/testuser/.ssh && \
    chmod 700 /home/testuser/.ssh
COPY test_key.pub /home/testuser/.ssh/authorized_keys
RUN chmod 600 /home/testuser/.ssh/authorized_keys && \
    chown -R testuser:testuser /home/testuser/.ssh
# Harden sshd_config for compliance testing
RUN sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#MaxAuthTries.*/MaxAuthTries 4/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```

**Adapt the Dockerfile:**
- Read the source repo's fixture files (e.g., `stig_rules.json`) to see what config directives
  the validators check, then configure sshd_config so some pass and some fail
- Install packages the validators check for (openssh-server, audit, aide, etc.)
- Enable/disable services the validators check (sshd, auditd, etc.)

**SSH key generation:**
```bash
ssh-keygen -t ed25519 -f [test_path]/_test/docker/test_key -N "" -q
```

**docker-compose.yml:**
```yaml
services:
  ssh-target:
    build: .
    container_name: prod-test-ssh-target
    ports:
      - "2222:22"
    restart: unless-stopped
```

**test_config.json:**
```json
{
  "host": "localhost",
  "port": 2222,
  "username": "testuser",
  "key_path": "_test/docker/test_key",
  "timeout": 10,
  "retries": 3
}
```

### `docker-browser` (selenium / playwright platforms)

**What to generate:**
```
_test/docker/Dockerfile.app
_test/docker/docker-compose.yml
_test/docker/test_config.json
```

**docker-compose pattern:**
```yaml
services:
  app:
    build:
      dockerfile: Dockerfile.app
    ports:
      - "8080:80"
  browser:
    image: mcr.microsoft.com/playwright:v1.40.0-jammy
    depends_on:
      - app
```

**test_config.json:**
```json
{
  "base_url": "http://localhost:8080",
  "browser": "chromium",
  "headless": true
}
```

### `docker-api` (requests / HTTP client platforms)

**What to generate:**
```
_test/docker/Dockerfile
_test/docker/docker-compose.yml
_test/docker/mock_api.py
_test/docker/test_config.json
```

Generate a Flask/FastAPI mock server that returns realistic responses
based on reading the source code's expected API patterns.

### `docker-db` (database platforms)

Use official DB images (postgres, mysql, mongo) with seed data.

### `mock-llm` (deepeval / LLM platforms)

Generate a mock LLM server that returns deterministic responses.

## Launch and Verify

4. **Build and launch:**
   ```bash
   docker compose -f [test_path]/_test/docker/docker-compose.yml up -d --build
   ```

5. **Wait for readiness** (up to 30 seconds):
   ```bash
   # SSH: wait for port
   for i in $(seq 1 30); do
     nc -z localhost 2222 && break || sleep 1
   done

   # HTTP: wait for response
   for i in $(seq 1 30); do
     curl -s http://localhost:8080 > /dev/null && break || sleep 1
   done
   ```

6. **Verify connectivity:**

   | Infra type | Verification command |
   |------------|---------------------|
   | `docker-ssh` | `ssh -i [key] -p 2222 -o StrictHostKeyChecking=no testuser@localhost echo OK` |
   | `docker-browser` | `curl -s http://localhost:8080` returns 200 |
   | `docker-api` | `curl -s http://localhost:8000/health` returns 200 |
   | `docker-db` | DB client connects and runs `SELECT 1` |

   **If verification fails:** Check Docker logs, fix Dockerfile, rebuild. Do NOT proceed to L3 tests
   with a broken target.

## Verification Checklist

- [ ] Docker container(s) running (`docker ps` shows them)
- [ ] Target port reachable (connectivity verified)
- [ ] Authentication works (SSH key / API key / credentials)
- [ ] test_config.json written with correct connection details
- [ ] Container logs show no startup errors

## Anti-patterns

- **NEVER skip this step.** "Tests use mocks" is not a prod-test.
- **NEVER hardcode infrastructure.** Read the Interface class to determine what's needed.
- **NEVER proceed to L3 with a broken target.** Verify connectivity first.
