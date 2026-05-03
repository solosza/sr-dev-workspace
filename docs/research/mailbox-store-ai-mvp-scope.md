# Mailbox Store AI — MVP Scope Definition

**Date:** 2026-04-23
**Source Task:** `tasks/mailbox-store-ai/004-build-write-mvp-scope.md`
**Depends On:** `docs/research/mailbox-store-ai-operations.md`, `docs/research/mailbox-store-ai-opportunities.md`

---

## 1. First Agent: Package Intake Agent

### Why This Agent First

The Package Intake Agent scores highest ROI across all five candidates:

| Factor | Score | Rationale |
|--------|-------|-----------|
| **Time Savings** | 2-4 hrs/day | 35-45% of daily labor is package intake — largest single time sink |
| **Implementation Complexity** | EASY | Linear pipeline (scan → log → photo → notify), all APIs mature |
| **Revenue Impact** | HIGH | Reduces peak-season staffing needs, eliminates lost-package disputes |
| **Time to Value** | 1-2 weeks | MVP notification trigger can ship in days |
| **Competitive Gap** | WIDE | Zero AI-powered solutions exist in the CMRA market (7 competitors analyzed, none offer AI) |

The Package Intake Agent is a **straight pipeline with no branching logic** — each step feeds the next. This makes it ideal for proving the concept to store owners before tackling the more complex Shipping Advisor (4 carrier APIs, rate normalization) or Customer Communication Agent (multi-channel orchestration, chatbot guardrails).

---

## 2. Core Features (MVP)

### Must-Have (Ship in MVP)

1. **Barcode Scan Trigger** — Listen for USB HID barcode scanner input, extract carrier tracking number, match to mailbox holder in POS database
2. **Auto-Log Package** — Create package record in local database with tracking number, mailbox number, timestamp, carrier name (parsed from tracking format)
3. **SMS Notification** — Send templated SMS to mailbox holder via Twilio: "Your package from [carrier] has arrived at [store]. Tracking: [number]"
4. **Email Notification** — Send templated email as fallback/supplement (customer preference)
5. **Package Photo Capture** — Trigger webcam/tablet camera on scan, store photo linked to package record
6. **Customer Preference Management** — Simple settings per customer: SMS, email, or both; phone number and email address
7. **Pickup Confirmation** — Staff scans package out on pickup, closes tracking loop, sends "picked up" confirmation
8. **Dashboard** — Web UI showing today's packages: pending pickup, picked up, aging (>3 days)
9. **Daily Summary** — End-of-day report: packages received, picked up, still pending, average dwell time

### Nice-to-Have (Post-MVP)

10. **Carrier Auto-Detection** — Parse tracking number format to identify carrier without manual selection
11. **Shelf Assignment** — Suggest shelf/bin location based on mailbox zone mapping
12. **Photo-Based Dimension Estimation** — Use CV to estimate package size from intake photo

---

## 3. Tech Stack

### Backend

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Runtime** | Python 3.12+ | Fastest development cycle, rich ecosystem for APIs/automation |
| **Framework** | FastAPI | Async support for concurrent API calls, auto-generated OpenAPI docs, lightweight |
| **Database** | SQLite (MVP) → PostgreSQL (scale) | SQLite for single-store simplicity, zero-config; PostgreSQL when multi-location needed |
| **ORM** | SQLAlchemy 2.0 | Type-safe queries, easy migration path SQLite → PostgreSQL |
| **Migrations** | Alembic | Schema versioning, rollback support |
| **Task Queue** | None (MVP) → Celery (scale) | Synchronous processing sufficient for MVP volumes; add queue for multi-store |

### Notifications

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **SMS** | Twilio | $0.0079/SMS, 99.95% delivery rate, best Python SDK, phone number verification built-in |
| **Email** | SendGrid (free tier) | 100 emails/day free, scales to 100K+, same parent company as Twilio |

### Frontend

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Dashboard** | HTMX + Jinja2 templates | Server-rendered, no JS build step, instant updates via SSE, minimal frontend complexity |
| **Styling** | Tailwind CSS | Utility-first, responsive, no custom CSS maintenance |

### Hardware Integration

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Barcode Scanner** | USB HID (keyboard wedge mode) | All common scanners (Zebra DS2208, Honeywell Voyager) support this — no driver/SDK needed |
| **Camera** | OpenCV (local capture) | Webcam triggered on scan event, photo saved to local storage |

### Infrastructure

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Hosting** | Local machine (MVP) → Cloud VPS (scale) | Store owners run on existing POS computer; cloud option for multi-location |
| **Deployment** | Docker Compose | Single-command install, includes all dependencies |

---

## 4. Integration Requirements

### Required Integrations (MVP)

| System | Integration Method | Purpose |
|--------|-------------------|---------|
| **Barcode Scanner** | USB HID keyboard input → Python `evdev`/`pynput` listener | Capture tracking numbers on scan |
| **Twilio SMS API** | REST API (Python SDK) | Send package arrival/pickup notifications |
| **SendGrid Email API** | REST API (Python SDK) | Send email notifications |
| **Webcam** | OpenCV `VideoCapture` | Package photo on intake |

### Required Integrations (Post-MVP)

| System | Integration Method | Purpose |
|--------|-------------------|---------|
| **POS System (ShipRite/PostalPoint)** | Database-level read (ODBC/direct) or API if available | Sync customer data, mailbox assignments |
| **USPS Tracking API** | REST API (OAuth 2.0) | Delivery status updates, carrier auto-detect |
| **UPS/FedEx Tracking APIs** | REST API (OAuth 2.0) | Multi-carrier tracking enrichment |

### MVP Standalone Approach

For MVP, the system operates **standalone** — not integrated with existing POS. Customer data is entered directly into the Package Intake Agent's database. This avoids the POS integration complexity (ShipRite's legacy system has no documented API) while proving value immediately. POS sync becomes a Phase 2 priority.

---

## 5. Timeline

### Phase 1: Core Engine (Weeks 1-2)

- Database schema (customers, packages, notifications)
- Barcode scanner listener (USB HID input capture)
- Package record creation on scan
- Customer lookup by tracking → mailbox mapping
- Basic CLI interface for testing

### Phase 2: Notifications (Week 3)

- Twilio SMS integration (send on scan)
- SendGrid email integration
- Customer notification preferences (SMS/email/both)
- Pickup scan-out with confirmation notification
- Notification delivery tracking (sent/delivered/failed)

### Phase 3: Dashboard & Photo (Week 4)

- Web dashboard (HTMX + FastAPI)
- Today's packages view (pending/picked up/aging)
- Package photo capture on intake (OpenCV)
- Daily summary report generation
- Customer management UI (add/edit preferences)

### Phase 4: Polish & Deploy (Weeks 5-6)

- Docker Compose packaging
- Installation guide for store owners
- Error handling and retry logic for notifications
- Logging and monitoring
- Beta testing with 1-2 store owners

**Total MVP: 6 weeks to deployable beta**

---

## 6. Deferred Features (NOT in MVP)

| Feature | Why Deferred | Target Phase |
|---------|-------------|--------------|
| **POS Integration** | ShipRite has no documented API; requires reverse-engineering or database-direct access | Phase 2 |
| **Multi-Carrier Rate Comparison** | Requires 4 separate carrier API integrations + rate normalization — separate agent | Phase 3 (Shipping Advisor Agent) |
| **AI Chatbot (inbound)** | Needs POS data to answer real questions; chatbot without data is just FAQ | Phase 3 (Customer Comm Agent) |
| **CMRA Compliance Tracking** | Regulatory workflow needs customer database maturity first | Phase 4 (Compliance Agent) |
| **Business Analytics Dashboard** | Requires 6+ months of historical data to be useful | Phase 5 (Analytics Agent) |
| **Multi-Location Support** | Adds database complexity (tenant isolation), auth, consolidated reporting | Phase 3+ |
| **Carrier Auto-Detection** | Nice-to-have; manual carrier selection works for MVP | Phase 2 |
| **CV Dimension Estimation** | Requires ML model training/tuning; manual entry works | Phase 3+ |
| **IVR Phone System** | Voice platform setup is complex; SMS handles 80% of notification needs | Phase 3 |
| **Predictive Shelf Assignment** | Needs volume data to train; manual shelving works | Phase 4+ |
| **White-Label / Multi-Tenant SaaS** | Premature — validate with single-store first | Phase 5+ |

---

## Summary

The MVP is a **standalone Package Intake Agent** — barcode scan triggers automatic SMS/email notification to the mailbox holder, with photo capture and a simple web dashboard. No POS integration required. Built with Python/FastAPI/SQLite/Twilio, deployable via Docker Compose in 6 weeks. This proves the core value proposition (automated intake → instant notification) in a market with zero AI competitors, before expanding to shipping, communication, compliance, and analytics agents.
