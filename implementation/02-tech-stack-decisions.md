# 02 - Tech Stack Decisions (Final)

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*
*Quyet dinh boi: System Architect*

---

## 1. Tong quan 3 Repos

```
ai-architect-web    (Frontend)     ── REST/WS ──>  ai-architect-api   (Backend)
                                                          |
                                                     HTTP/Queue
                                                          |
                                                   ai-architect-gpu  (GPU Service)
```

---

## 2. Repo 1: `ai-architect-web` — Frontend

### Core Stack

| Component | Technology | Version | Ly do chon |
|-----------|-----------|---------|------------|
| **Framework** | Next.js (App Router) | 14.x | SSR, routing, image optimization, Vercel deploy |
| **Language** | TypeScript | 5.x | Type safety, DX tot |
| **UI Library** | React | 18.x | Ecosystem lon nhat, shadcn/ui support |
| **Styling** | Tailwind CSS | 3.x | Utility-first, design token mapping tot |
| **Component Base** | shadcn/ui | latest | Unstyled primitives, customize duoc hoan toan |
| **State (Client)** | Zustand | 4.x | Lightweight, khong boilerplate nhu Redux |
| **State (Server)** | TanStack Query | 5.x | Cache, revalidation, optimistic updates |
| **Realtime** | Socket.io Client | 4.x | WebSocket voi fallback, reconnect tu dong |
| **Forms** | React Hook Form + Zod | 7.x + 3.x | Validation schema reuse voi backend |
| **Font** | Geist Sans + Geist Mono | latest | Vercel design system identity |

### Specialized Libraries

| Component | Technology | Version | Dung cho |
|-----------|-----------|---------|----------|
| **3D Viewer** | Three.js + @react-three/fiber + @react-three/drei | r160+ / 8.x | 3D model viewer (P1) |
| **2D Canvas** | Fabric.js | 6.x | Annotation overlay tren floor plan |
| **PDF Preview** | react-pdf | 7.x | Xem PDF truoc khi download |
| **Charts** | Recharts | 2.x | Dashboard metrics (P1) |
| **Date** | date-fns | 3.x | Date formatting (Vietnamese locale) |
| **Icons** | Lucide React | latest | Consistent icon set |

### Build & Dev Tools

| Tool | Version | Muc dich |
|------|---------|----------|
| pnpm | 8.x | Package manager (nhanh, disk efficient) |
| ESLint | 8.x | Linting |
| Prettier | 3.x | Code formatting |
| Vitest | 1.x | Unit tests |
| Playwright | 1.x | E2E tests |
| Storybook | 7.x | Component development (optional) |

### Quyet dinh dac biet - Frontend

1. **Fabric.js cho annotation** - KHONG dung canvas API truc tiep. Fabric.js quan ly object model, selection, serialization.
2. **Three.js chi load khi can** - Lazy import Three.js bundle. Chi load khi user mo 3D viewer tab.
3. **shadcn/ui customize theo Vercel tokens** - Khong dung default shadcn theme. Map tat ca sang CSS custom properties.
4. **Zustand cho UI state only** - Project data, versions, reviews deu qua TanStack Query (server state).
5. **Socket.io cho realtime** - Generation progress, notifications, live annotation updates.

---

## 3. Repo 2: `ai-architect-api` — Backend

### Core Stack

| Component | Technology | Version | Ly do chon |
|-----------|-----------|---------|------------|
| **Framework** | FastAPI | 0.110+ | Async native, auto OpenAPI docs, Python ecosystem |
| **Language** | Python | 3.11+ | AI/ML ecosystem, LangGraph support |
| **ORM** | SQLAlchemy | 2.0+ | Mature, async support, migration tool (Alembic) |
| **Migrations** | Alembic | 1.13+ | Schema migrations |
| **Database** | PostgreSQL | 16 | JSONB, full-text search, reliability |
| **Cache/Queue** | Redis | 7.x | Cache, Celery broker, PubSub |
| **Task Queue** | Celery | 5.3+ | Background tasks (generation, export) |
| **File Storage** | MinIO (dev) / AWS S3 (prod) | latest | S3-compatible object storage |
| **Auth** | JWT (PyJWT) + bcrypt | latest | Stateless auth |
| **Realtime** | python-socketio | 5.x | WebSocket server |

### AI/Agent Stack

| Component | Technology | Version | Ly do chon |
|-----------|-----------|---------|------------|
| **Agent Framework** | LangGraph | 0.2+ | Stateful graph orchestration, HITL, streaming |
| **LLM SDK** | LangChain | 0.2+ | Tool calling, prompt management |
| **Primary LLM** | Claude API (Anthropic) | claude-sonnet-4-20250514 | Best reasoning, tool use |
| **Fallback LLM** | GPT-4o (OpenAI) | gpt-4o | Backup khi Claude unavailable |
| **Validation** | Pydantic | 2.x | Schema validation cho Brief, Geometry, etc. |

### Export & Document

| Component | Technology | Ly do chon |
|-----------|-----------|------------|
| **PDF Generation** | WeasyPrint | HTML/CSS to PDF, flexible layout |
| **SVG Generation** | svgwrite | Programmatic SVG tao tu geometry data |
| **Image Processing** | Pillow | Resize, watermark, format conversion |

### Quyet dinh dac biet - Backend

1. **LangGraph chi lam orchestration** - KHONG luu business truth trong graph state. Truth nam o PostgreSQL.
2. **Celery cho long-running tasks** - Generation, export, style ingestion deu chay qua Celery workers.
3. **Pydantic models lam contract** - Moi API endpoint co Pydantic request/response model. Reuse cho validation.
4. **Alembic migrations bat buoc** - Moi thay doi schema phai co migration file. KHONG dung auto-migrate.
5. **Structured logging** - JSON format, correlation_id cho moi request chain.
6. **GPU service qua HTTP** - Backend goi GPU service qua REST API. KHONG import truc tiep GPU code.

---

## 4. Repo 3: `ai-architect-gpu` — GPU Service

### Core Stack

| Component | Technology | Version | Ly do chon |
|-----------|-----------|---------|------------|
| **Workflow Engine** | ComfyUI | latest | Visual workflow, node ecosystem, API mode |
| **Diffusion Library** | Diffusers (HuggingFace) | 0.27+ | Backup pipeline, fine-grained control |
| **Base Model** | Stable Diffusion XL | sdxl-base-1.0 | High quality floor plan generation |
| **Fallback Model** | Stable Diffusion 1.5 | v1-5 | Lighter, cho recovery level 3 |
| **Conditioning** | ControlNet | sdxl-controlnet | Edge/depth conditioning cho floor plan |
| **3D Engine** | Blender headless | 4.0+ | Scene assembly, GLTF export, rendering |
| **3D Conversion** | FloorPlanToBlender3D | latest | 2D floor plan -> 3D model |
| **API Wrapper** | FastAPI | 0.110+ | Thin wrapper expose ComfyUI workflows |
| **GPU Runtime** | CUDA | 12.x | NVIDIA GPU acceleration |

### Quyet dinh dac biet - GPU

1. **ComfyUI chay isolated** - GPL-3.0 license. Chay nhu standalone service, giao tiep qua API. KHONG embed vao core.
2. **Diffusers lam fallback** - Khi ComfyUI fail, fallback sang Diffusers pipeline (Apache-2.0).
3. **Blender headless** - Khong co GUI. Script automation qua Python API.
4. **Model versioning** - Moi model co version tag. Generation job luu model_id de reproducibility.
5. **Workflow JSON versioning** - ComfyUI workflows luu trong git. Moi generation luu workflow_version.

---

## 5. Infrastructure & DevOps

| Component | Dev | Staging | Production |
|-----------|-----|---------|------------|
| **Frontend Host** | localhost:3000 | Vercel Preview | Vercel |
| **Backend Host** | localhost:8000 | Railway | Railway / AWS ECS |
| **GPU Host** | Local GPU | RunPod | RunPod / vast.ai |
| **Database** | Docker PostgreSQL | Neon (free tier) | Neon / Supabase / RDS |
| **Object Storage** | MinIO (Docker) | AWS S3 | AWS S3 |
| **Cache** | Docker Redis | Upstash Redis | Upstash Redis / ElastiCache |
| **CI/CD** | - | GitHub Actions | GitHub Actions |
| **Monitoring** | Console logs | Sentry | Sentry + custom dashboard |
| **Domain** | localhost | staging.aiarchitect.vn | app.aiarchitect.vn |

### Quyet dinh Infrastructure

1. **Vercel cho frontend** - Zero config deploy, edge functions, image optimization.
2. **Railway cho backend** - Docker deploy, PostgreSQL addon, auto-scaling.
3. **RunPod cho GPU** - On-demand GPU instances, serverless endpoints.
4. **Neon cho PostgreSQL** - Serverless Postgres, branching cho dev/staging.
5. **S3 cho file storage** - Floor plans, renders, exports, bundles.
6. **Upstash cho Redis** - Serverless Redis, Celery broker compatible.

---

## 6. Dependency Version Lock

### Frontend (package.json)

```json
{
  "dependencies": {
    "next": "^14.2.0",
    "react": "^18.3.0",
    "react-dom": "^18.3.0",
    "tailwindcss": "^3.4.0",
    "@radix-ui/react-dialog": "^1.0.0",
    "zustand": "^4.5.0",
    "@tanstack/react-query": "^5.50.0",
    "socket.io-client": "^4.7.0",
    "react-hook-form": "^7.52.0",
    "zod": "^3.23.0",
    "fabric": "^6.0.0",
    "three": "^0.160.0",
    "@react-three/fiber": "^8.15.0",
    "@react-three/drei": "^9.100.0",
    "lucide-react": "^0.400.0",
    "date-fns": "^3.6.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.3.0"
  }
}
```

### Backend (requirements.txt)

```
fastapi>=0.110.0
uvicorn[standard]>=0.29.0
sqlalchemy>=2.0.30
alembic>=1.13.0
asyncpg>=0.29.0
psycopg2-binary>=2.9.9
redis>=5.0.0
celery>=5.3.6
python-socketio>=5.11.0
pydantic>=2.7.0
pyjwt>=2.8.0
bcrypt>=4.1.0
boto3>=1.34.0
langchain>=0.2.0
langgraph>=0.2.0
langchain-anthropic>=0.1.0
langchain-openai>=0.1.0
weasyprint>=62.0
svgwrite>=1.4.0
pillow>=10.3.0
httpx>=0.27.0
python-multipart>=0.0.9
```

### GPU (requirements-gpu.txt)

```
fastapi>=0.110.0
uvicorn>=0.29.0
torch>=2.3.0
diffusers>=0.27.0
transformers>=4.40.0
accelerate>=0.30.0
safetensors>=0.4.0
controlnet-aux>=0.0.9
httpx>=0.27.0
pillow>=10.3.0
```

---

## 7. Nhung thu KHONG dung

| Technology | Ly do khong dung |
|-----------|-----------------|
| Redux | Qua boilerplate cho project nay. Zustand du. |
| Prisma | Python backend, khong dung Node ORM. |
| tRPC | Backend la Python, khong la TypeScript. |
| MongoDB | Can relational data (versions, lineage, reviews). PostgreSQL JSONB du cho flexible fields. |
| GraphQL | REST + WebSocket du cho use cases hien tai. GraphQL tang complexity. |
| Docker Compose (prod) | Moi service deploy rieng (Vercel/Railway/RunPod). Docker Compose chi cho dev. |
| Kubernetes | Overkill cho Phase 1 scale (50 concurrent users). |
| Kafka | Redis PubSub + Celery du cho event/queue needs. |
| IfcOpenShell | Phase 2. Khong can IFC o Phase 1. |
| Qdrant | Phase 2 (Style Intelligence full stack). Phase 1 chi log data. |
| Speckle | Pilot only. Khong dung cho Phase 1 core. |
| FreeCAD | Khong fit workflow. Blender headless du cho 3D. |
