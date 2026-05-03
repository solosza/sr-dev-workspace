# Mailbox Store AI — System Architecture

**Date:** 2026-04-23
**Source Task:** `tasks/mailbox-store-ai/006-build-write-system-architecture.md`
**Depends On:** `docs/research/mailbox-store-ai-opportunities.md`, `docs/research/mailbox-store-ai-mvp-scope.md`

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MAILBOX STORE AI                            │
│                                                                     │
│  ┌──────────┐   ┌──────────────┐   ┌──────────────┐               │
│  │ Hardware  │   │   FastAPI     │   │  Dashboard   │               │
│  │ Layer     │──▶│   Backend     │──▶│  (HTMX)      │               │
│  │           │   │               │   │              │               │
│  │ • Scanner │   │ • REST API    │   │ • Today view │               │
│  │ • Camera  │   │ • WebSocket   │   │ • Analytics  │               │
│  └──────────┘   │ • Event Bus   │   │ • Customer   │               │
│                  └───────┬───────┘   │   mgmt       │               │
│                          │           └──────────────┘               │
│                          │                                          │
│              ┌───────────┼───────────┐                              │
│              │           │           │                              │
│        ┌─────▼──┐  ┌─────▼──┐  ┌────▼───┐                         │
│        │ Notif  │  │  Data  │  │ Photo  │                          │
│        │ Engine │  │  Layer │  │ Store  │                          │
│        │        │  │        │  │        │                          │
│        │• Twilio│  │• SQLite│  │• Local │                          │
│        │• Send- │  │  (MVP) │  │  disk  │                          │
│        │  Grid  │  │• Pg    │  │• S3    │                          │
│        └────────┘  │  (v2)  │  │  (v2)  │                          │
│                    └────────┘  └────────┘                          │
└─────────────────────────────────────────────────────────────────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
        ┌─────▼──┐  ┌─────▼──┐  ┌────▼───┐
        │  USPS  │  │  UPS   │  │ FedEx  │
        │  Track │  │  Track │  │ Track  │
        │  API   │  │  API   │  │ API    │
        └────────┘  └────────┘  └────────┘
              (Post-MVP carrier enrichment)
```

### Component Summary

| Component | Purpose | MVP? |
|-----------|---------|------|
| **Hardware Layer** | USB barcode scanner + webcam input | Yes |
| **FastAPI Backend** | Core application server, REST API, event processing | Yes |
| **Dashboard (HTMX)** | Web UI for staff — package status, customer management | Yes |
| **Notification Engine** | SMS (Twilio) + email (SendGrid) delivery | Yes |
| **Data Layer** | SQLite database for all application state | Yes |
| **Photo Store** | Local filesystem for package photos | Yes |
| **Carrier APIs** | Tracking enrichment from USPS/UPS/FedEx | No (Phase 2) |

### Data Flow: Package Intake

```
USB Scanner ──▶ pynput listener ──▶ /api/packages/intake
                                         │
                    ┌────────────────────┤
                    │                    │
                    ▼                    ▼
             Create package       Trigger camera
             record in DB         (OpenCV capture)
                    │                    │
                    │                    ▼
                    │              Save photo to
                    │              disk, link to
                    │              package record
                    │                    │
                    ├────────────────────┘
                    │
                    ▼
             Lookup customer by
             mailbox number
                    │
                    ▼
             Check notification
             preferences
                    │
              ┌─────┴─────┐
              │           │
              ▼           ▼
          Send SMS    Send Email
          (Twilio)    (SendGrid)
              │           │
              ▼           ▼
         Log delivery  Log delivery
         status        status
                    │
                    ▼
             Push update to
             dashboard (SSE)
```

---

## 2. Agent Design

### Architecture: Standalone Modular (Not Kernel-Powered)

The MVP Package Intake Agent is a **standalone FastAPI application**, not an Isagawa kernel-powered agent. Rationale:

| Factor | Kernel-Powered | Standalone | Decision |
|--------|---------------|-----------|----------|
| **Target user** | Developer/power user | Store owner (non-technical) | Standalone |
| **Deployment** | Requires Claude Code runtime | Docker Compose, one-click | Standalone |
| **Latency** | LLM inference per action (~2-5s) | Deterministic pipeline (~100ms) | Standalone |
| **Cost** | API tokens per package scan | Zero per-scan marginal cost | Standalone |
| **Reliability** | Depends on API availability | Runs fully offline (except notifications) | Standalone |

The Package Intake Agent is a **deterministic pipeline** — scan triggers a fixed sequence of actions with no decision-making. LLM inference adds cost and latency without value for this use case.

### Future Agent Integration Points

When later agents (Shipping Advisor, Customer Communication) require natural language understanding or decision-making, they will integrate LLM capabilities via:

| Agent | LLM Use Case | Integration Point |
|-------|-------------|-------------------|
| **Shipping Advisor** | Natural language package description → dimensions/weight estimation | `/api/shipping/describe` endpoint |
| **Customer Comm** | Inbound chatbot for "is my package here?" queries | `/api/chat/message` endpoint |
| **Analytics** | Natural language queries against business data | `/api/analytics/query` endpoint |

These future agents add LLM endpoints to the same FastAPI application — the architecture is extensible without restructuring.

### Agent Module Structure

```
mailbox-store-ai/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── intake.py          # Package Intake Agent (MVP)
│   │   ├── shipping.py        # Shipping Advisor Agent (Phase 2)
│   │   └── communication.py   # Customer Comm Agent (Phase 3)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── packages.py    # /api/packages/*
│   │   │   ├── customers.py   # /api/customers/*
│   │   │   ├── notifications.py
│   │   │   └── dashboard.py
│   │   └── app.py             # FastAPI app factory
│   ├── core/
│   │   ├── config.py          # Settings (Pydantic BaseSettings)
│   │   ├── database.py        # SQLAlchemy engine + session
│   │   └── events.py          # Internal event bus (scan, notify, pickup)
│   ├── models/
│   │   ├── package.py         # Package ORM model
│   │   ├── customer.py        # Customer ORM model
│   │   └── notification.py    # Notification log ORM model
│   ├── services/
│   │   ├── scanner.py         # USB HID barcode listener
│   │   ├── camera.py          # OpenCV photo capture
│   │   ├── twilio_sms.py      # Twilio SMS sender
│   │   └── sendgrid_email.py  # SendGrid email sender
│   └── templates/             # Jinja2 + HTMX dashboard templates
├── alembic/                   # Database migrations
├── tests/
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

---

## 3. Carrier API Integrations

### MVP: No Direct Carrier API Integration

The MVP does **not** call carrier APIs. The barcode scanner captures the tracking number, and the system logs it as-is. Carrier identification is done via tracking number format parsing (regex-based, no API call needed):

| Carrier | Tracking Format | Pattern |
|---------|----------------|---------|
| **USPS** | 20-22 digits, or starts with 9400/9205/9261/9270 | `^(94|92|93)\d{18,20}$` |
| **UPS** | Starts with 1Z, 18 chars | `^1Z[A-Z0-9]{16}$` |
| **FedEx** | 12 or 15 digits | `^\d{12,15}$` |
| **DHL** | 10-digit, starts with 00-99 | `^\d{10}$` |
| **Amazon** | TBA prefix | `^TBA\d+$` |

### Post-MVP: Carrier Tracking Enrichment (Phase 2)

| Carrier | API | Auth | Rate Limit | Key Data |
|---------|-----|------|-----------|----------|
| **USPS** | USPS Web Tools REST API (v3) | OAuth 2.0 (Client Credentials) | 1,000 requests/day (free tier) | Delivery status, expected delivery date, origin |
| **UPS** | UPS Developer Kit REST API | OAuth 2.0 | 500 requests/15 min | Service type, delivery date, signature status |
| **FedEx** | FedEx REST API (Track v1) | OAuth 2.0 (Client Credentials) | 1,400 requests/hr (production) | Delivery status, proof of delivery, estimated delivery |
| **DHL** | DHL Express Tracking API | API Key | 250 requests/day (free) | Shipment status, origin country, service |

### Carrier API Integration Architecture

```
┌──────────────────────────────────────────┐
│          Carrier Gateway Service         │
│                                          │
│  ┌──────────┐  ┌──────────┐             │
│  │ Carrier  │  │ Response │             │
│  │ Router   │──▶│ Normal-  │──▶ Unified │
│  │ (by      │  │ izer     │   Tracking │
│  │ tracking │  │          │   Object   │
│  │ format)  │  └──────────┘             │
│  └──────────┘                            │
│                                          │
│  ┌──────────┐  ┌──────────┐             │
│  │ Token    │  │ Rate     │             │
│  │ Manager  │  │ Limiter  │             │
│  │ (OAuth   │  │ (per-    │             │
│  │ refresh) │  │ carrier) │             │
│  └──────────┘  └──────────┘             │
└──────────────────────────────────────────┘
```

**Unified Tracking Object** (normalized across carriers):

```python
@dataclass
class TrackingInfo:
    carrier: str           # "USPS" | "UPS" | "FedEx" | "DHL"
    tracking_number: str
    status: str            # "in_transit" | "delivered" | "exception"
    estimated_delivery: date | None
    origin_city: str | None
    destination_city: str | None
    last_event: str        # Human-readable last scan event
    last_event_time: datetime | None
    raw_response: dict     # Carrier-specific full response
```

---

## 4. Notification Layer

### Architecture

```
┌──────────────┐
│ Notification │
│ Dispatcher   │
│              │
│ • Check pref │
│ • Template   │
│ • Route      │
└──────┬───────┘
       │
   ┌───┴───┐
   │       │
   ▼       ▼
┌──────┐ ┌──────┐
│Twilio│ │Send- │
│ SMS  │ │Grid  │
│      │ │Email │
└──┬───┘ └──┬───┘
   │        │
   ▼        ▼
┌──────────────┐
│ Delivery Log │
│ (status,     │
│  timestamp,  │
│  retry count)│
└──────────────┘
```

### Twilio SMS Integration

| Config | Value |
|--------|-------|
| **API** | Twilio REST API v2010 |
| **Auth** | Account SID + Auth Token (env vars) |
| **Cost** | $0.0079/outbound SMS (US) |
| **Phone** | 1 local number per store ($1/month) |
| **SDK** | `twilio` Python package |
| **Delivery tracking** | Status callback webhook → update notification log |

**Message Templates:**

| Event | Template |
|-------|----------|
| Package arrived | `[StoreName]: Your package from {carrier} has arrived. Tracking: {tracking}. Pickup at {address}.` |
| Pickup confirmed | `[StoreName]: Package {tracking} picked up. Thank you!` |
| Aging reminder (3+ days) | `[StoreName]: Reminder — you have a package waiting since {date}. Please pick up at your convenience.` |

### SendGrid Email Integration

| Config | Value |
|--------|-------|
| **API** | SendGrid Mail Send v3 |
| **Auth** | API Key (env var) |
| **Cost** | Free tier: 100 emails/day |
| **SDK** | `sendgrid` Python package |
| **Templates** | Dynamic templates with Handlebars syntax |

### Notification Preferences

```python
class NotificationPreference(str, Enum):
    SMS_ONLY = "sms"
    EMAIL_ONLY = "email"
    BOTH = "both"
    NONE = "none"  # Customer opted out
```

### Retry Logic

| Attempt | Wait | Action |
|---------|------|--------|
| 1 | Immediate | Send via primary channel |
| 2 | 5 minutes | Retry same channel |
| 3 | 15 minutes | Fallback to alternate channel (SMS→email or email→SMS) |
| 4+ | — | Log as failed, flag for manual follow-up on dashboard |

---

## 5. Data Layer

### Database: SQLite (MVP) → PostgreSQL (Scale)

**MVP uses SQLite** for zero-config simplicity — the database is a single file on the store's local machine. Migration path to PostgreSQL is handled by SQLAlchemy + Alembic (same ORM, swap connection string).

### Schema

```sql
-- Core tables
CREATE TABLE customers (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    mailbox_number  TEXT NOT NULL UNIQUE,
    phone           TEXT,
    email           TEXT,
    notification_pref TEXT DEFAULT 'both',  -- sms, email, both, none
    active          BOOLEAN DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE packages (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    tracking_number TEXT NOT NULL,
    carrier         TEXT,                    -- USPS, UPS, FedEx, DHL, Amazon, Unknown
    customer_id     INTEGER REFERENCES customers(id),
    mailbox_number  TEXT NOT NULL,
    status          TEXT DEFAULT 'pending',   -- pending, picked_up, returned, expired
    photo_path      TEXT,
    shelf_location  TEXT,
    received_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    picked_up_at    TIMESTAMP,
    received_by     TEXT                      -- Staff member who scanned
);

CREATE TABLE notifications (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id      INTEGER REFERENCES packages(id),
    customer_id     INTEGER REFERENCES customers(id),
    channel         TEXT NOT NULL,            -- sms, email
    template        TEXT NOT NULL,            -- arrived, pickup_confirmed, aging_reminder
    status          TEXT DEFAULT 'pending',   -- pending, sent, delivered, failed
    provider_id     TEXT,                     -- Twilio SID or SendGrid message ID
    attempt         INTEGER DEFAULT 1,
    sent_at         TIMESTAMP,
    delivered_at    TIMESTAMP,
    error_message   TEXT
);

CREATE TABLE daily_summaries (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            DATE NOT NULL UNIQUE,
    packages_received INTEGER DEFAULT 0,
    packages_picked_up INTEGER DEFAULT 0,
    packages_pending INTEGER DEFAULT 0,
    avg_dwell_hours REAL,
    sms_sent        INTEGER DEFAULT 0,
    emails_sent     INTEGER DEFAULT 0,
    generated_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_packages_status ON packages(status);
CREATE INDEX idx_packages_mailbox ON packages(mailbox_number);
CREATE INDEX idx_packages_tracking ON packages(tracking_number);
CREATE INDEX idx_packages_received ON packages(received_at);
CREATE INDEX idx_customers_mailbox ON customers(mailbox_number);
CREATE INDEX idx_notifications_package ON notifications(package_id);
CREATE INDEX idx_notifications_status ON notifications(status);
```

### Data Retention

| Data Type | Retention | Rationale |
|-----------|-----------|-----------|
| Package records | 12 months | Dispute resolution, analytics |
| Package photos | 90 days | Storage management; configurable |
| Notification logs | 6 months | Audit trail, delivery analytics |
| Daily summaries | Indefinite | Small footprint, valuable for trends |
| Customer records | While active + 12 months after deactivation | CMRA regulatory requirement |

---

## 6. Deployment Model

### MVP: Local Machine (Docker Compose)

The MVP runs on the **store's existing computer** — typically the same machine running their POS system. Docker Compose bundles the entire stack.

```yaml
# docker-compose.yml (simplified)
services:
  app:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./data/db:/app/data/db          # SQLite database
      - ./data/photos:/app/data/photos  # Package photos
    environment:
      - TWILIO_ACCOUNT_SID=${TWILIO_ACCOUNT_SID}
      - TWILIO_AUTH_TOKEN=${TWILIO_AUTH_TOKEN}
      - TWILIO_PHONE_NUMBER=${TWILIO_PHONE_NUMBER}
      - SENDGRID_API_KEY=${SENDGRID_API_KEY}
      - STORE_NAME=${STORE_NAME}
      - STORE_ADDRESS=${STORE_ADDRESS}
    devices:
      - /dev/video0:/dev/video0  # Webcam access (Linux)
    restart: unless-stopped
```

**Why local-first:**
- Store owners are wary of cloud dependencies for critical operations
- Barcode scanner is a USB device — requires local access
- Webcam for photos — requires local access
- Works during internet outages (notifications queue for retry)
- No recurring cloud hosting costs for MVP

### Scale: Cloud-Hosted SaaS (Multi-Tenant)

| Phase | Deployment | When |
|-------|-----------|------|
| **MVP** | Local Docker Compose, one container per store | Launch |
| **Growth** | Cloud VPS (DigitalOcean/Linode), SQLite per tenant | 10-50 customers |
| **Scale** | Multi-tenant PostgreSQL, shared application cluster | 50+ customers |

### Multi-Tenant Architecture (Post-MVP)

```
┌──────────────────────────────────────┐
│         Load Balancer (nginx)        │
└──────────────┬───────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│ App    │ │ App    │ │ App    │
│ Node 1 │ │ Node 2 │ │ Node 3 │
└────┬───┘ └────┬───┘ └────┬───┘
     │          │          │
     └──────────┼──────────┘
                │
         ┌──────▼──────┐
         │ PostgreSQL  │
         │ (schema-    │
         │ per-tenant) │
         └─────────────┘
```

**Tenant isolation:** Schema-per-tenant in PostgreSQL. Each store's data lives in its own schema (`store_123.packages`, `store_123.customers`). Shared `public` schema for tenant metadata, billing, and platform-level config.

---

## 7. Security

### PII Handling

The system processes several categories of PII:

| PII Type | Source | Storage | Protection |
|----------|--------|---------|------------|
| **Customer names** | Manual entry / CSV import | `customers` table | Encrypted at rest (SQLCipher for SQLite, TDE for PostgreSQL) |
| **Phone numbers** | Manual entry | `customers.phone` | Encrypted at rest; masked in logs (`***-***-1234`) |
| **Email addresses** | Manual entry | `customers.email` | Encrypted at rest |
| **Mailing addresses** | Not stored (MVP) | N/A | Not collected in MVP; post-MVP: encrypted |
| **Package photos** | Webcam capture | Local filesystem / S3 | Access-controlled directory; S3 with server-side encryption |
| **Tracking numbers** | Barcode scan | `packages.tracking_number` | Not PII per se, but linked to customer records |

### Authentication & Authorization

| Layer | Mechanism |
|-------|-----------|
| **Dashboard login** | Username + bcrypt-hashed password, session cookie (HttpOnly, Secure, SameSite=Strict) |
| **API auth** | API key in header (`X-API-Key`) for programmatic access |
| **Role-based access** | `admin` (full access), `staff` (scan, view, pickup), `readonly` (dashboard view only) |
| **Session timeout** | 8 hours (auto-logout, matches typical store shift) |

### API Credential Security

| Credential | Storage | Rotation |
|------------|---------|----------|
| Twilio SID + Auth Token | Environment variables (`.env` file, not in repo) | Quarterly rotation recommended |
| SendGrid API Key | Environment variable | Quarterly rotation recommended |
| Carrier API OAuth tokens | Token manager service; refresh tokens in encrypted config | Auto-refresh on expiry |

### Network Security

| Control | Implementation |
|---------|---------------|
| **HTTPS** | TLS termination at nginx (Let's Encrypt cert for cloud; self-signed for local) |
| **CORS** | Restricted to dashboard origin only |
| **Rate limiting** | 100 requests/minute per IP on public endpoints |
| **Input validation** | Pydantic models validate all API inputs; SQLAlchemy parameterized queries prevent SQL injection |
| **Headers** | CSP, X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security |

### Compliance Considerations

| Regulation | Applicability | Measures |
|------------|--------------|----------|
| **TCPA** | SMS notifications require prior express consent | Opt-in captured at customer registration; opt-out via "STOP" reply |
| **CAN-SPAM** | Email notifications | Unsubscribe link in every email; sender identification |
| **CCPA/state privacy** | Customer PII storage | Data deletion on request; data export capability |
| **PCI DSS** | Payment info | **Not applicable** — billing handled by Stripe (PCI-compliant processor), no card data touches our system |

---

## Summary

The Mailbox Store AI architecture is a **standalone FastAPI application** with a deterministic Package Intake Agent pipeline (scan → log → photo → notify → dashboard). It runs locally via Docker Compose on the store's existing hardware, with SQLite for zero-config data storage and Twilio/SendGrid for notifications. The architecture is designed for extensibility — future agents (Shipping Advisor, Customer Comm) add LLM-powered endpoints to the same application without restructuring. Security covers PII encryption at rest, RBAC, HTTPS, and TCPA/CAN-SPAM compliance for notifications. Multi-tenant cloud deployment is the scale path at 50+ customers.
