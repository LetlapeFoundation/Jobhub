# JobHub: South African Employment Platform

**JobHub Master Product Constitution v2.0** — Deployable Edition  
*Build the plane while flying it.*

---

## What is JobHub?

JobHub is a sovereign South African employment, recruitment, and opportunity ecosystem. It is **not** a job board — it's an Opportunity Platform connecting job seekers, employers, recruiters, entrepreneurs, and capital.

**Core Mission:** Reduce unemployment and underemployment in South Africa by creating the most trusted, accessible, and effective employment marketplace on the continent.

**Core Principles:**
- 🌍 **Accessibility First** — Works on R1,500 Android + 2G connectivity
- 🛡️ **Trust Before Scale** — Every employer verified, every job real (CRYTONET)
- 🇿🇦 **Data Sovereignty** — All PII stored on South African servers
- ⚖️ **Fairness by Design** — Algorithms audited for bias
- 💰 **Profit with Purpose** — Revenue tied to successful placements

---

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+ (or use compose)

### Development Setup

```bash
# Clone and enter directory
git clone https://github.com/LetlapeFoundation/Jobhub.git
cd Jobhub

# Copy environment template
cp .env.example .env

# Start database, cache, and message queue
docker-compose up -d

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
alembic upgrade head  # Run migrations
python -m uvicorn app.main:app --reload

# Frontend setup (new terminal)
cd frontend
npm install
npm run dev
```

**Backend runs on:** http://localhost:8000  
**Frontend runs on:** http://localhost:3000  
**API docs:** http://localhost:8000/docs

---

## Project Structure

```
Jobhub/
├── backend/               # FastAPI application
│   ├── app/
│   │   ├── main.py       # Entry point
│   │   ├── config.py     # Settings & env vars
│   │   ├── database.py   # SQLAlchemy setup
│   │   ├── api/          # API routes (v1)
│   │   ├── models/       # SQLAlchemy ORM models
│   │   ├── schemas/      # Pydantic request/response
│   │   ├── services/     # Business logic
│   │   ├── security/     # Auth, CRYTONET integration
│   │   └── utils/        # Helpers
│   ├── migrations/       # Alembic database migrations
│   ├── tests/            # pytest suite
│   ├── requirements.txt  # Python dependencies
│   └── pyproject.toml    # Package metadata
│
├── frontend/              # React + Tailwind PWA
│   ├── src/
│   │   ├── components/   # Reusable React components
│   │   ├── pages/        # Page-level components
│   │   ├── hooks/        # Custom React hooks
│   │   ├── services/     # API client
│   │   ├── store/        # Zustand/Pinia state
│   │   ├── styles/       # Tailwind config
│   │   ├── utils/        # Helpers
│   │   └── App.tsx       # Root component
│   ├── public/           # Static assets, manifest.json
│   ├── package.json
│   └── vite.config.ts    # Vite bundler config
│
├── docs/                  # Documentation
│   ├── CONSTITUTION.md   # v2.0 (from this file)
│   ├── ARCHITECTURE.md   # Tech architecture deep-dive
│   ├── API.md            # API reference
│   └── DEPLOYMENT.md     # Production guides
│
├── docker-compose.yml    # PostgreSQL, Redis, Mailhog
├── Dockerfile            # Backend container
├── .env.example          # Environment template
├── .github/              # GitHub Actions workflows
│   └── workflows/
│       ├── test.yml      # Run tests on PR
│       ├── lint.yml      # Code quality
│       └── deploy.yml    # Deploy to staging/prod
│
└── CONTRIBUTING.md       # Development guidelines
```

---

## Current Phase: Foundation (Month 1–2)

✅ Repository scaffolding  
✅ Tech stack setup  
⏳ CRYTONET Layer 1 integration  
⏳ Database schema (KYC, employer verification)  
⏳ Auth system (email + SMS OTP)  
⏳ API scaffolding (users, jobs, applications)  
⏳ Frontend shell (PWA, mobile-first)  

---

## Technology Stack

**Frontend:**
- React 18 + TypeScript
- Tailwind CSS (mobile-first design)
- Vite (ultra-fast bundler)
- PWA (Workbox for offline support)
- TanStack Query (data fetching)
- Zustand (state management)

**Backend:**
- FastAPI (Python 3.11)
- SQLAlchemy 2.0 (ORM)
- Pydantic v2 (validation)
- Alembic (migrations)
- PostgreSQL (Supabase free tier)
- Redis (caching, sessions)
- Celery (background jobs)

**Infrastructure (Zero-Budget Phase):**
- Vercel (frontend hosting, free tier)
- Render (backend hosting, free tier)
- Supabase (PostgreSQL + Auth + Storage)
- Twilio (SMS, pay-as-you-go)
- WhatsApp Business API (notifications)
- Jitsi Meet (video interviews, self-hosted)
- Sentry (error tracking, free tier)

---

## Key Features (Phase 1)

### Module A: Core Employment Engine
- 👤 Job Seeker profile (KYC verified)
- 🏢 Employer profile (CIPC verified via CRYTONET)
- 📋 Job posting & management
- 🎯 Smart job matching (rules-based v1)
- 📱 Application system with status pipeline
- 💬 In-app messaging (fraud-monitored by CRYTONET)

### Module B: Recruitment Dashboard
- 🔍 Candidate search & filtering
- 📊 Kanban-style applicant pipeline
- 📅 Interview scheduling with calendar integration
- 📈 Basic analytics (applications, time-to-hire, source)

### Module C: AI Career Tools (v1 — Template-Based)
- 📄 AI CV Builder (5 templates, ATS-optimized)
- 💌 AI Cover Letter Generator (keyword-matched)
- 🤖 Career Coach FAQ Bot (pre-built responses)

---

## Monetization (Phase 1)

| User Type | Plan | Price | Features |
|-----------|------|-------|----------|
| **Job Seeker** | Free | R0 | Profile, search, basic apply |
| | Plus | R29/mo | AI tools, priority results, insights |
| | Pro | R79/mo | Coaching, salary guide, advisor (1x/mo) |
| **Employer** | Starter | R99/mo | 3 posts, search, messaging |
| | Growth | R299/mo | Unlimited posts, ranking, analytics |
| | Enterprise | R999/mo | Team accounts, API, SLA |

**Success Fee (Primary Revenue):**
- Permanent placement: **5% of first-year remuneration**
- Contract placement: **10% of contract value**
- Collected from employer only (candidate never pays to get hired)
- 30-day replacement guarantee

---

## CRYTONET Security Integration

CRYTONET provides three security layers:

| Layer | Function |
|-------|----------|
| **Shield (L1)** | Identity verification, KYC, document authenticity |
| **Watch (L2)** | Real-time fraud detection, scam pattern matching |
| **Vault (L3)** | Encrypted storage, access logging, breach response |

### KYC Pipeline
1. User uploads ID (smartphone photo)
2. OCR extracts ID number & photo
3. Liveness check (selfie video, blink detection)
4. Home Affairs e-Verify API match
5. Manual review queue for edge cases
6. VERIFIED badge issued

### Employer Verification
1. CIPC registration number provided
2. CRYTONET queries CIPC database
3. Company details confirmed
4. Physical address geocoded & validated
5. Contact email domain verified
6. VERIFIED EMPLOYER badge issued

---

## Regulatory Compliance

- ✅ **POPIA** (Protection of Personal Information Act) — Granular consent, right to deletion, encryption
- ✅ **EEA** (Employment Equity Act) — Optional demographic tracking, B-BBEE integration
- ✅ **LRA/BCEA** — Contract templates, UIF reminders, minimum wage alerts
- ✅ **CPA** (Consumer Protection Act) — 7-day cooling-off, pro-rata refunds

---

## Success Metrics (12-Month Target)

| Metric | Target |
|--------|--------|
| Monthly Active Job Seekers | 10,000 |
| Verified Employers | 500 |
| Active Job Listings | 2,000 |
| Application-to-Interview Rate | 15% |
| Avg Time-to-Hire | 21 days |
| **Monthly Successful Placements** | **500** |
| Candidate NPS | > 50 |
| Employer NPS | > 40 |
| Monthly Revenue | R150,000 |

---

## Roadmap

### Phase 0: Foundation (Months 1–2) ⏳
- [x] Repository setup
- [ ] CRYTONET L1 integration
- [ ] Employer verification pipeline
- [ ] 50 seed employers, 500 seed job seekers
- [ ] Beta test: Johannesburg CBD + Soweto

### Phase 1: Core Launch (Months 3–6)
- [ ] Public launch (Job Seeker + Employer modules)
- [ ] Social media campaigns (TikTok, Instagram)
- [ ] Partnership launches (NYDA, SEFA)
- [ ] Target: 1,000 active seekers, 100 employers, 50 placements

### Phase 2: Scale (Months 7–12)
- [ ] Recruiter module launch
- [ ] Expansion: Cape Town, Durban, Pretoria
- [ ] AI Career Tools v1 release
- [ ] Target: 10,000 seekers, 500 employers, 500 placements
- [ ] Revenue target: R150,000/month

### Phase 3: Funding Hub (Months 13–18)
- [ ] Funding Discovery Engine
- [ ] Investor onboarding
- [ ] AI Proposal Assistant
- [ ] Target: 100 funding apps, R5M facilitated

### Phase 4: Intelligence Upgrade (Months 19–36)
- [ ] Ndlovu AI Prime Engine integration
- [ ] Neural matching model
- [ ] Conversational Career Coach
- [ ] NEARO Foundation trust layer

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development guidelines.

**Questions?** Open an issue or reach out to the team.

---

## License

TBD — Likely open-source with commercial support.

---

**Last Updated:** 23 June 2026  
**Constitution Version:** 2.0  
**Repository Status:** 🚀 Foundation Phase
