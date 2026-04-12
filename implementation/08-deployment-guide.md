# 08 - Deployment & Production Guide

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*

> Note: tai lieu nay giu lai huong host theo CP6 goc (`Vercel + Railway + RunPod`).
> Production standard hien tai cua Blackbird da chuyen sang `GHCR -> linuxvm -> Cloudflare Tunnel`.
> Xem quyet dinh moi nhat tai [12-production-direction-decision.md](/Users/nguyenquocthong/project/ai-architect-mvp/docs/phase-1/12-production-direction-decision.md:1).

---

## 1. Environment Overview

```
LOCAL DEV          STAGING                    PRODUCTION
-----------        -------------------        -------------------
localhost:3000     staging.aiarchitect.vn     app.aiarchitect.vn
localhost:8000     api-staging.aiarc...       api.aiarchitect.vn
localhost:8001     (shared RunPod)            gpu.aiarchitect.vn
Docker Compose     Vercel+Railway+RunPod      Vercel+Railway+RunPod
```

---

## 2. Local Development Setup

### 2.1 Prerequisites

```bash
# Required
node >= 20.x        # Frontend
python >= 3.11      # Backend
pnpm >= 8.x         # Package manager
docker >= 24.x      # PostgreSQL, Redis, MinIO
```

### 2.2 Backend (ai-architect-api)

```bash
# Clone
git clone git@github.com:org/ai-architect-api.git
cd ai-architect-api

# Start dependencies
docker-compose up -d  # PostgreSQL + Redis + MinIO

# Python env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Environment
cp .env.example .env.local
# Edit .env.local with your keys

# Database
alembic upgrade head

# Run
uvicorn app.main:app --reload --port 8000

# Celery worker (separate terminal)
celery -A app.tasks worker --loglevel=info
```

### 2.3 Frontend (ai-architect-web)

```bash
# Clone
git clone git@github.com:org/ai-architect-web.git
cd ai-architect-web

# Install
pnpm install

# Environment
cp .env.example .env.local
# NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXT_PUBLIC_WS_URL=http://localhost:8000

# Run
pnpm dev  # localhost:3000
```

### 2.4 GPU Service (ai-architect-gpu)

```bash
# CHI CAN khi test generation locally
# Yeu cau: NVIDIA GPU 12GB+ VRAM

git clone git@github.com:org/ai-architect-gpu.git
cd ai-architect-gpu

# Setup
./scripts/download_models.sh
./scripts/setup_blender.sh

# Python env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-gpu.txt

# Run ComfyUI
python -m comfyui --listen 0.0.0.0 --port 8188

# Run API wrapper
uvicorn api.server:app --port 8001
```

### 2.5 docker-compose.yml (Dev Dependencies)

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:16-alpine
    ports: ["5432:5432"]
    environment:
      POSTGRES_DB: ai_architect
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: devpass
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]

  minio:
    image: minio/minio
    ports: ["9000:9000", "9001:9001"]
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    command: server /data --console-address ":9001"
    volumes:
      - miniodata:/data

volumes:
  pgdata:
  miniodata:
```

---

## 3. Environment Variables

### 3.1 Backend (.env.example)

```bash
# App
APP_ENV=development                    # development | staging | production
APP_SECRET_KEY=change-me-in-production
APP_CORS_ORIGINS=http://localhost:3000

# Database
DATABASE_URL=postgresql+asyncpg://dev:devpass@localhost:5432/ai_architect

# Redis
REDIS_URL=redis://localhost:6379/0

# S3 / MinIO
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=ai-architect
S3_REGION=us-east-1
S3_PUBLIC_URL=http://localhost:9000/ai-architect  # For presigned URLs

# Auth
JWT_SECRET=change-me-in-production
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=15
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7

# LLM
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
DEFAULT_LLM=anthropic                  # anthropic | openai

# GPU Service
GPU_SERVICE_URL=http://localhost:8001
GPU_API_KEY=internal-dev-key

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# Monitoring
SENTRY_DSN=                            # Empty for dev
LOG_LEVEL=DEBUG
```

### 3.2 Frontend (.env.example)

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_WS_URL=http://localhost:8000
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Feature flags
NEXT_PUBLIC_FF_VIEWER_3D=false
NEXT_PUBLIC_FF_NOTIFICATIONS=false
NEXT_PUBLIC_FF_STYLE_INTELLIGENCE=false
```

### 3.3 GPU Service (.env.example)

```bash
GPU_API_KEY=internal-dev-key
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
S3_BUCKET=ai-architect
COMFYUI_URL=http://localhost:8188
MODEL_DIR=/models
BLENDER_PATH=/usr/bin/blender
```

---

## 4. Staging Deployment

### 4.1 Frontend -> Vercel

```bash
# Connect GitHub repo to Vercel
# Branch: develop -> Preview deployments
# Environment variables set in Vercel dashboard

# vercel.json
{
  "framework": "nextjs",
  "buildCommand": "pnpm build",
  "installCommand": "pnpm install"
}
```

### 4.2 Backend -> Railway

```bash
# Connect GitHub repo to Railway
# Branch: develop -> auto deploy

# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Railway services:
# 1. Web service (FastAPI)
# 2. Worker service (Celery)
# 3. PostgreSQL addon
# 4. Redis addon
```

### 4.3 GPU -> RunPod

```bash
# RunPod Serverless endpoint
# Docker image: custom GPU image with ComfyUI + models
# Template: RunPod GPU Pod (RTX 4090 / A5000)
# Scaling: 0 min, 2 max workers

# Dockerfile.gpu
FROM nvidia/cuda:12.1-runtime-ubuntu22.04
# ... install Python, ComfyUI, models, Blender
COPY . /app
CMD ["python", "-m", "uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "8001"]
```

---

## 5. Production Deployment

### 5.1 Infrastructure Map

```
Vercel (Frontend)
  - Custom domain: app.aiarchitect.vn
  - Edge functions for API proxy (optional)
  - Image optimization enabled
  - Branch: main only

Railway (Backend)
  - Custom domain: api.aiarchitect.vn
  - Web service: 2 replicas, 1GB RAM each
  - Worker service: 1 replica, 512MB RAM
  - PostgreSQL: Neon (external, for better scaling)
  - Redis: Upstash (external, serverless)

RunPod (GPU)
  - Serverless endpoint
  - Min 0, Max 3 workers
  - RTX 4090 (24GB VRAM)
  - Auto-scale on queue depth

Neon (PostgreSQL)
  - Production branch
  - Read replicas (if needed)
  - Auto-suspend after 5 min idle

Upstash (Redis)
  - Serverless, pay-per-request
  - Global replication (optional)

AWS S3
  - Bucket: ai-architect-prod
  - Region: ap-southeast-1 (Singapore)
  - CloudFront CDN for public assets
  - Lifecycle: move old exports to Glacier after 90 days
```

### 5.2 Domain & SSL

```
app.aiarchitect.vn      -> Vercel (automatic SSL)
api.aiarchitect.vn      -> Railway (automatic SSL)
gpu.aiarchitect.vn      -> RunPod (if needed, or internal only)
cdn.aiarchitect.vn      -> CloudFront -> S3
```

### 5.3 CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/deploy.yml (Backend)
name: Deploy
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
        ports: ["5432:5432"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/ -v --cov=app
      - run: ruff check app/
      - run: mypy app/

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: railwayapp/deploy@v1
        with:
          token: ${{ secrets.RAILWAY_TOKEN }}
```

```yaml
# .github/workflows/ci.yml (runs on PRs)
name: CI
on:
  pull_request:
    branches: [develop, main]

jobs:
  lint-and-test:
    # Same as test job above
    # MUST pass before merge allowed
```

---

## 6. Monitoring & Observability

### 6.1 Sentry (Error Tracking)

```python
# Backend
import sentry_sdk
sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    environment=settings.APP_ENV,
    traces_sample_rate=0.1,  # 10% of transactions
)
```

```typescript
// Frontend
Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 0.1,
})
```

### 6.2 Structured Logging

```python
# Backend - JSON logs
import structlog

logger = structlog.get_logger()

logger.info("generation_started",
    project_id=project.id,
    version_id=version.id,
    model="sdxl",
    correlation_id=request.state.correlation_id
)
```

### 6.3 Health Checks

```
GET /health              -> { "status": "ok", "db": "ok", "redis": "ok" }
GET /health/gpu          -> { "status": "ok", "gpu_available": true, "queue_depth": 2 }
```

### 6.4 Alerts

| Alert | Condition | Channel |
|-------|-----------|---------|
| API 5xx spike | > 10 errors in 5 min | Slack + Email |
| GPU unavailable | Health check fails 3x | Slack |
| Generation failure rate | > 30% in 1 hour | Slack |
| Database connection pool exhausted | Active connections > 90% | Slack |
| Disk usage (S3) | > 80% bucket quota | Email |

---

## 7. Backup & Recovery

### 7.1 Database Backup

```
Neon: Automatic point-in-time recovery (7 days)
Additional: pg_dump daily -> S3 (retention: 30 days)
```

### 7.2 S3 Backup

```
S3 versioning: enabled
Cross-region replication: ap-southeast-1 -> ap-northeast-1 (optional Phase 2)
Lifecycle: old exports -> Glacier after 90 days
```

### 7.3 Recovery Procedures

| Scenario | Recovery |
|----------|----------|
| Backend crash | Railway auto-restart (health check) |
| Database corruption | Neon point-in-time restore |
| S3 file deleted | S3 versioning restore |
| GPU service down | Generation queued, retry when available |
| Full outage | Deploy from main branch, restore DB from backup |

---

## 8. Security Hardening (Production)

| Item | Implementation |
|------|---------------|
| HTTPS everywhere | Automatic via Vercel/Railway |
| CORS | Restrict to app.aiarchitect.vn |
| Rate limiting | 100 req/min per user (API level) |
| SQL injection | SQLAlchemy parameterized queries |
| XSS | React auto-escape + CSP headers |
| CSRF | SameSite cookies |
| File upload | Type whitelist + size limit (50MB) |
| Secrets | Platform env vars, NEVER in code |
| Dependencies | Dependabot alerts enabled |
| Access logs | All API requests logged with user_id |

---

## 9. Production Launch Checklist

```
[ ] All P0 features working on staging
[ ] Load test passed (50 concurrent users)
[ ] Security audit completed (OWASP top 10)
[ ] SSL certificates active
[ ] Custom domains configured
[ ] Sentry monitoring active
[ ] Database backups verified
[ ] S3 bucket permissions correct
[ ] Environment variables set (all 3 services)
[ ] CI/CD pipelines green
[ ] Error alerting configured
[ ] Rollback procedure documented and tested
[ ] PM sign-off
[ ] Legal: ComfyUI GPL compliance verified (isolated service)
[ ] Performance: LCP < 2.5s, API p95 < 500ms
```

---

## 10. Scaling Plan (Post-Launch)

| Trigger | Action |
|---------|--------|
| > 50 concurrent users | Add Railway replica |
| > 5 concurrent generations | Add RunPod workers |
| > 100GB S3 storage | Enable lifecycle policies |
| > 1000 DB queries/min | Add Neon read replica |
| Response time degradation | Enable Redis caching for read endpoints |
