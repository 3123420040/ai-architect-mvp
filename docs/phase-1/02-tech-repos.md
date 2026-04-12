# Phase 1 – Git Repos & Tech Stack Map

*Ngày chốt: Apr 11, 2026*

---

## Tổng quan kiến trúc repos

Phase 1 sẽ tạo **3 git repos chính** (monorepo approach cho mỗi layer) + sử dụng **8 open-source repos** bên ngoài.

---

## A. Repos dự án (Tự tạo)

### Repo 1: `ai-architect-web` — Frontend Application

| Thuộc tính | Giá trị |
|------------|---------|
| **Tech** | Next.js 14 (App Router) + React 18 + TypeScript |
| **3D Engine** | Three.js + @react-three/fiber + @react-three/drei |
| **BIM Components** | @thatopen/components (measurement, floor plan navigation) |
| **UI Library** | Tailwind CSS + shadcn/ui |
| **State** | Zustand (client state) + TanStack Query (server state) |
| **Realtime** | Socket.io client (notifications, generation progress) |

**Phục vụ Epic/User Stories:**
- Epic 1 (Auth): Login/Register UI
- Epic 2 (Intake): Chat interface, Multi-step form
- Epic 3 (Generation): Floor plan gallery, variation selector
- Epic 4 (3D): 3D Viewer, measurement tool, render gallery
- Epic 5 (Review): Review dashboard, annotation overlay
- Epic 6 (Feedback): Share link page, client feedback UI
- Epic 7 (Versioning): Version timeline, side-by-side compare
- Epic 8 (Export): Export buttons, PDF preview
- Epic 9 (Dashboard): Dashboard, notification bell

**Cấu trúc thư mục dự kiến:**
```
ai-architect-web/
├── src/
│   ├── app/                    # Next.js App Router pages
│   │   ├── (auth)/             # Login, Register
│   │   ├── dashboard/          # Dashboard overview
│   │   ├── projects/[id]/      # Project workspace
│   │   │   ├── intake/         # Chat + Form intake
│   │   │   ├── designs/        # Floor plan gallery
│   │   │   ├── viewer/         # 3D viewer
│   │   │   ├── review/         # KTS review workspace
│   │   │   └── versions/       # Version history
│   │   └── share/[token]/      # Client share link (public)
│   ├── components/
│   │   ├── chat/               # Chat UI components
│   │   ├── viewer-3d/          # Three.js viewer wrapper
│   │   ├── floor-plan/         # Floor plan display + annotate
│   │   ├── forms/              # Intake form steps
│   │   └── ui/                 # shadcn/ui base components
│   ├── lib/                    # API client, utils
│   └── stores/                 # Zustand stores
├── public/
├── package.json
└── next.config.ts
```

---

### Repo 2: `ai-architect-api` — Backend API & Agent Orchestration

| Thuộc tính | Giá trị |
|------------|---------|
| **Framework** | FastAPI (Python 3.11+) |
| **Agent** | LangGraph + LangChain |
| **LLM** | Claude API (Anthropic) / GPT-4o (OpenAI) — configurable |
| **Database** | PostgreSQL 16 + SQLAlchemy + Alembic (migrations) |
| **File Storage** | MinIO (S3-compatible, self-hosted) hoặc AWS S3 |
| **Queue** | Celery + Redis (async generation tasks) |
| **Realtime** | Socket.io server (progress updates, notifications) |
| **Auth** | JWT tokens + bcrypt password hashing |
| **PDF** | WeasyPrint hoặc ReportLab |

**Phục vụ Epic/User Stories:**
- Epic 1: Auth endpoints (register, login, invite, roles)
- Epic 2: Project CRUD, Design Brief processing, Chat agent (LangGraph)
- Epic 3: Generation orchestration (queue to GPU service)
- Epic 5: Review workflow (status transitions, annotations storage)
- Epic 6: Share link generation, feedback storage, AI revision trigger
- Epic 7: Version management
- Epic 8: PDF generation, DXF conversion
- Epic 9: Dashboard queries, notification dispatch

**Cấu trúc thư mục dự kiến (Agentic OS Architecture):**
```
ai-architect-api/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth.py           # Auth endpoints
│   │   │   ├── projects.py       # Project CRUD
│   │   │   ├── designs.py        # Design generation, versions
│   │   │   ├── reviews.py        # Review workflow
│   │   │   ├── feedback.py       # Client feedback
│   │   │   ├── exports.py        # PDF, DXF export
│   │   │   ├── share.py          # Share link management
│   │   │   └── tasks.py          # Background task status/output
│   │   └── deps.py               # Dependencies (auth, db)
│   │
│   ├── engine/                    # === AGENTIC OS ENGINE ===
│   │   ├── query_loop.py          # Pipeline 2: async generator while(true)
│   │   ├── state_machine.py       # needsFollowUp + 8 transition types
│   │   └── recovery.py            # Escalating recovery (5 levels)
│   │
│   ├── agents/                    # === Pipeline 4: Multi-Agent ===
│   │   ├── coordinator.py         # Design Coordinator (restricted tools!)
│   │   ├── requirements_agent.py  # Extract & clarify requirements
│   │   ├── design_agent.py        # Generate floor plans + renders
│   │   ├── review_agent.py        # Check feasibility (READ-ONLY)
│   │   ├── revision_agent.py      # Process feedback → regenerate
│   │   └── run_agent.py           # Unified agent runner (like runAgent.ts)
│   │
│   ├── tools/                     # === Pipeline 3: Tool Orchestration ===
│   │   ├── base.py                # Tool interface + isConcurrencySafe
│   │   ├── orchestrator.py        # partitionToolCalls + batch execution
│   │   ├── streaming_executor.py  # Streaming tool execution
│   │   ├── design_brief_tools.py  # DesignBriefGet, DesignBriefUpdate
│   │   ├── generation_tools.py    # FloorPlanGenerate, Render3D
│   │   ├── search_tools.py        # StyleSearch, BuildingCodeLookup
│   │   ├── export_tools.py        # ExportPDF, ExportDXF
│   │   ├── check_tools.py         # FeasibilityCheck, DimensionCalc
│   │   └── material_tools.py      # MaterialSearch
│   │
│   ├── context/                   # === Pipeline 5: Context Management ===
│   │   ├── compact.py             # Auto-compact (LLM summarize)
│   │   ├── microcompact.py        # Microcompact (no LLM needed)
│   │   ├── truncation.py          # Tool result truncation
│   │   ├── reactive_compact.py    # Emergency compact on 413
│   │   └── memory/                # Design Memory system
│   │       ├── extract.py         # Extract memories end-of-session
│   │       ├── scan.py            # Scan + find relevant memories
│   │       └── inject.py          # Inject memories into prompt
│   │
│   ├── permissions/               # === Pipeline 6: Permission & Security ===
│   │   ├── classifier.py          # Action classification (6 layers)
│   │   ├── roles.py               # Role-based access (viewer/architect/admin)
│   │   ├── review_gate.py         # KTS approval state machine
│   │   ├── budget.py              # Generation budget tracking
│   │   └── audit.py               # Immutable audit trail
│   │
│   ├── skills/                    # === Skill System ===
│   │   ├── loader.py              # Load skills from 3 sources
│   │   ├── activation.py          # Conditional activation by project context
│   │   └── builtin/               # Bundled skills
│   │       ├── vietnamese_code/   # QCVN building code
│   │       ├── tropical_arch/     # Tropical architecture patterns
│   │       └── narrow_lot/        # Narrow lot design (< 5m width)
│   │
│   ├── tasks/                     # === Background Tasks ===
│   │   ├── base.py                # Task lifecycle (5 states)
│   │   ├── generation_task.py     # GPU generation task
│   │   ├── export_task.py         # PDF/DXF export task
│   │   └── notifications.py      # Task notifications via WebSocket
│   │
│   ├── models/                    # SQLAlchemy models
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── design.py
│   │   ├── feedback.py
│   │   └── annotation.py
│   ├── services/
│   │   ├── gpu_client.py          # Call GPU service (ComfyUI API)
│   │   ├── pdf_export.py          # PDF generation
│   │   ├── notification.py        # Email + in-app notifications
│   │   └── file_storage.py        # S3/MinIO wrapper
│   ├── core/
│   │   ├── config.py              # Settings, env vars
│   │   ├── security.py            # JWT, password hashing
│   │   └── database.py            # DB session management
│   └── main.py                    # FastAPI app entry
├── migrations/                    # Alembic
├── tests/
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

### Repo 3: `ai-architect-gpu` — GPU Generation Service

| Thuộc tính | Giá trị |
|------------|---------|
| **Runtime** | ComfyUI (node-based workflow engine) |
| **Models** | Stable Diffusion XL/1.5 + ControlNet models |
| **Diffusion Lib** | huggingface/diffusers (backup/custom pipelines) |
| **3D Pipeline** | FloorPlanToBlender3D + Blender headless |
| **API Wrapper** | FastAPI thin wrapper hoặc ComfyUI native API |
| **Infra** | Docker + NVIDIA GPU (RunPod / vast.ai / on-premise) |

**Phục vụ Epic/User Stories:**
- Epic 3: Floor plan image generation (text → ControlNet → floor plan)
- Epic 4: 3D model generation (floor plan → Blender 3D → GLTF) + render images (ControlNet → exterior/interior)

**Cấu trúc thư mục dự kiến:**
```
ai-architect-gpu/
├── comfyui/
│   ├── workflows/
│   │   ├── floor_plan_gen.json       # Text → floor plan workflow
│   │   ├── exterior_render.json      # Floor plan → exterior 3D render
│   │   ├── interior_render.json      # Room layout → interior render
│   │   └── revision_gen.json         # Feedback-conditioned regeneration
│   ├── models/                       # SD checkpoints, ControlNet models
│   └── custom_nodes/                 # Custom ComfyUI nodes if needed
├── pipelines/
│   ├── floor_plan_pipeline.py        # Diffusers-based alternative pipeline
│   ├── blender_3d_pipeline.py        # FloorPlan → Blender → GLTF export
│   └── post_processing.py           # Label overlay, dimension annotation
├── api/
│   ├── server.py                     # FastAPI wrapper for ComfyUI
│   └── schemas.py                    # Request/Response models
├── scripts/
│   ├── download_models.sh            # Download SD + ControlNet weights
│   └── setup_blender.sh              # Install Blender headless
├── Dockerfile.gpu                    # NVIDIA CUDA base image
└── docker-compose.gpu.yml
```

---

## B. Open-source Repos (Dependencies)

### Layer 1: AI Agent Orchestration

#### 1. langchain-ai/langchain + langchain-ai/langgraph
| | |
|---|---|
| **URL** | https://github.com/langchain-ai/langchain |
| | https://github.com/langchain-ai/langgraph |
| **Stars** | ~133k (langchain), ~8k (langgraph) |
| **License** | MIT |
| **Dùng cho** | Agent orchestration: intake chatbot, design agent, review agent, revision agent |
| **Cách integrate** | `pip install langchain langgraph` trong `ai-architect-api` |
| **Map to Stories** | US-2.2 (Chat AI), US-3.1 (Generate), US-3.3 (Regenerate), US-6.3 (AI Revise) |

**Lý do chọn:**
- LangGraph cho phép define multi-step workflow dạng graph (state machine), phù hợp cho flow: intake → clarify → generate → review → revise
- Human-in-the-loop support tốt (KTS approve/reject nằm trong graph)
- Tool calling mạnh: agent gọi generation service, query database, export PDF
- Dễ debug: visualize graph execution, replay states

---

### Layer 2: AI Image Generation

#### 2. Comfy-Org/ComfyUI
| | |
|---|---|
| **URL** | https://github.com/comfy-org/ComfyUI |
| **Stars** | ~108k |
| **License** | GPL-3.0 |
| **Dùng cho** | Node-based workflow engine cho Stable Diffusion generation |
| **Cách integrate** | Standalone service trong `ai-architect-gpu`, gọi qua ComfyUI API |
| **Map to Stories** | US-3.1 (Floor Plan Gen), US-4.1 (3D Render), US-3.3 & US-6.3 (Regeneration) |

**Lý do chọn:**
- Visual workflow editor: nhanh chóng prototype pipeline generation
- API mode: chạy headless, nhận workflow JSON → trả kết quả
- Ecosystem plugin lớn: ControlNet, IP-Adapter, upscaler nodes có sẵn
- Dễ reproduce: save workflow JSON, version control được

**Lưu ý licensing:** GPL-3.0 — chạy ComfyUI như service riêng biệt (network boundary), không embed vào proprietary code. Cần legal review trước khi commercialize.

---

#### 3. huggingface/diffusers
| | |
|---|---|
| **URL** | https://github.com/huggingface/diffusers |
| **Stars** | ~33.3k |
| **License** | Apache-2.0 |
| **Dùng cho** | Programmable diffusion pipeline, ControlNet integration |
| **Cách integrate** | `pip install diffusers` trong `ai-architect-gpu` |
| **Map to Stories** | US-3.1, US-4.1 (backup/custom generation pipelines) |

**Lý do chọn:**
- API-first: dễ build custom pipeline hơn ComfyUI khi cần fine-grained control
- ControlNet pipeline tích hợp sẵn (`StableDiffusionControlNetPipeline`)
- Apache-2.0 license: không có GPL concern
- Dùng song song với ComfyUI: ComfyUI cho prototyping nhanh, diffusers cho production pipeline

---

### Layer 3: 3D Visualization (Frontend)

#### 4. mrdoob/three.js
| | |
|---|---|
| **URL** | https://github.com/mrdoob/three.js |
| **Stars** | ~112k |
| **License** | MIT |
| **Dùng cho** | 3D rendering engine trên browser |
| **Cách integrate** | `npm install three @react-three/fiber @react-three/drei` trong `ai-architect-web` |
| **Map to Stories** | US-4.2 (3D Viewer), US-4.3 (Measurement) |

**Lý do chọn:**
- Standard de facto cho WebGL/WebGPU 3D trên browser
- React wrapper (r3f) tốt cho Next.js integration
- MIT license: hoàn toàn free cho commercial
- Ecosystem lớn: loaders (GLTF, OBJ), controls (orbit, first-person), post-processing

---

#### 5. ThatOpen/engine_components
| | |
|---|---|
| **URL** | https://github.com/ThatOpen/engine_components |
| **Stars** | ~622 |
| **License** | MIT |
| **Dùng cho** | BIM-oriented web components: measurement, floor plan navigation, DXF export |
| **Cách integrate** | `npm install @thatopen/components` trong `ai-architect-web` |
| **Map to Stories** | US-4.2 (Floor Plan View mode), US-4.3 (Measurement), US-8.3 (DXF Export) |

**Lý do chọn:**
- AEC-native: measurement tools, 2D plan navigation, DXF export có sẵn — không cần build from scratch
- Built on Three.js: tương thích với 3D viewer stack
- MIT license
- Active maintenance (latest release Apr 9, 2026)

---

#### 6. ThatOpen/engine_web-ifc
| | |
|---|---|
| **URL** | https://github.com/ThatOpen/engine_web-ifc |
| **Stars** | ~931 |
| **License** | MPL-2.0 |
| **Dùng cho** | WebAssembly IFC parser — đọc/ghi IFC files trực tiếp trên browser |
| **Cách integrate** | `npm install web-ifc` trong `ai-architect-web` (Phase 1 optional, Phase 2 critical) |
| **Map to Stories** | US-8.3 (DXF/IFC export — P2, nếu kịp) |

**Lý do chọn:**
- Client-side IFC parsing: không cần server roundtrip
- Tiền đề cho Phase 2 (full BIM integration)
- Dùng cùng engine_components cho viewer tích hợp

---

### Layer 4: 2D → 3D Conversion

#### 7. grebtsew/FloorPlanToBlender3D
| | |
|---|---|
| **URL** | https://github.com/grebtsew/FloorPlanToBlender3D |
| **Stars** | ~1.5k |
| **License** | MIT |
| **Dùng cho** | Convert 2D floor plan image → Blender 3D scene → export GLTF/GLB |
| **Cách integrate** | Python module trong `ai-architect-gpu`, chạy Blender headless |
| **Map to Stories** | US-4.1 (3D model generation), US-4.2 (3D model cho viewer) |

**Lý do chọn:**
- Direct pipeline: PNG floor plan → 3D model tự động
- Export nhiều format: .blend, .gltf, .glb, .obj
- MIT license
- Blender headless chạy được trên server (Docker + GPU)

**Lưu ý:** Output quality phụ thuộc vào chất lượng floor plan input. Cần post-processing để thêm textures, lighting.

---

### Layer 5: BIM/Engineering Data (Backend)

#### 8. IfcOpenShell/IfcOpenShell
| | |
|---|---|
| **URL** | https://github.com/IfcOpenShell/IfcOpenShell |
| **Stars** | ~2.4k |
| **License** | LGPL-3.0 |
| **Dùng cho** | Read/write/convert IFC files (BIM standard) |
| **Cách integrate** | `pip install ifcopenshell` trong `ai-architect-api` (Phase 1: basic, Phase 2: full) |
| **Map to Stories** | US-8.3 (DXF export — P2) |

**Lý do chọn:**
- IFC là standard quốc tế cho BIM data exchange
- Python API mạnh: tạo IFC programmatically
- Chuẩn bị foundation cho Phase 2 BIM integration
- LGPL-3.0: cho phép commercial use miễn là dynamic linking

**Phase 1 scope:** Chỉ dùng basic export nếu kịp. Focus chính ở Phase 2.

---

## C. Tổng hợp: Repo → Epic Map

```
┌──────────────────────┬──────────────────────────────────────────┐
│        REPO          │              EPICS SERVED                │
├──────────────────────┼──────────────────────────────────────────┤
│ ai-architect-web     │ E1 E2 E3 E4 E5 E6 E7 E8 E9  (all)     │
│ ai-architect-api     │ E1 E2 E3 E5 E6 E7 E8 E9               │
│ ai-architect-gpu     │ E3 E4                                    │
├──────────────────────┼──────────────────────────────────────────┤
│ langchain/langgraph  │ E2(chat) E3(gen) E6(revise)             │
│ ComfyUI              │ E3(floor plan) E4(3D render)            │
│ diffusers            │ E3(floor plan) E4(3D render)            │
│ three.js             │ E4(viewer)                               │
│ engine_components    │ E4(measure, nav) E8(DXF)                │
│ engine_web-ifc       │ E8(IFC - P2)                             │
│ FloorPlanToBlender3D │ E4(2D→3D)                                │
│ IfcOpenShell         │ E8(IFC - P2)                             │
└──────────────────────┴──────────────────────────────────────────┘
```

---

## D. License Summary

| Repo | License | Commercial OK? | Lưu ý |
|------|---------|----------------|-------|
| langchain/langgraph | MIT | Yes | Không hạn chế |
| ComfyUI | GPL-3.0 | Conditional | Chạy như service riêng, không embed. Cần legal review |
| diffusers | Apache-2.0 | Yes | Không hạn chế |
| three.js | MIT | Yes | Không hạn chế |
| engine_components | MIT | Yes | Không hạn chế |
| engine_web-ifc | MPL-2.0 | Yes | File-level copyleft, modified files phải open-source |
| FloorPlanToBlender3D | MIT | Yes | Không hạn chế |
| IfcOpenShell | LGPL-3.0 | Yes | Dynamic linking OK, static linking cần open-source |

**Kết luận license:** Stack nhìn chung an toàn cho commercial. Chỉ cần chú ý ComfyUI (GPL) — giải pháp: chạy isolated service, communicate qua API.

---

## E. Infrastructure Overview (Phase 1)

```
┌─────────────────────────────────────────────────────┐
│                   DEVELOPMENT                        │
│  Local: Docker Compose (api + web + db + redis)      │
│  GPU: RunPod serverless (ComfyUI + models)           │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                   STAGING / PROD                     │
│                                                      │
│  ┌─────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ Vercel  │  │ Railway / │  │ RunPod /         │   │
│  │ (web)   │  │ Fly.io   │  │ vast.ai          │   │
│  │ Next.js │  │ (api)    │  │ (gpu service)    │   │
│  └────┬────┘  └────┬─────┘  └────┬─────────────┘   │
│       │            │              │                   │
│       └──────┬─────┘              │                   │
│              │                    │                   │
│  ┌───────────▼────────┐  ┌───────▼──────────────┐   │
│  │ Supabase /         │  │ MinIO / S3           │   │
│  │ Neon (PostgreSQL)  │  │ (file storage)       │   │
│  └────────────────────┘  └──────────────────────┘   │
│                                                      │
│  Redis: Upstash (serverless Redis)                   │
└─────────────────────────────────────────────────────┘
```

---

## F. Model Weights cần download (Phase 1)

| Model | Size | Source | Dùng cho |
|-------|------|--------|----------|
| Stable Diffusion XL Base | ~6.5 GB | HuggingFace | Base image generation |
| ControlNet SDXL (canny/mlsd) | ~2.5 GB | HuggingFace | Floor plan conditioning |
| ControlNet SDXL (depth) | ~2.5 GB | HuggingFace | 3D render conditioning |
| IP-Adapter (style transfer) | ~1 GB | HuggingFace | Reference image style matching |

**Tổng GPU VRAM cần:** Tối thiểu 12GB (RTX 3060) cho inference, recommend 24GB (RTX 4090 / A5000) cho SDXL + ControlNet combo.
