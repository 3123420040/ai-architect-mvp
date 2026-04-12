# 03 - Architecture Blueprint

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*

---

## 0. Module-Pipeline Mapping Matrix

9 business modules KHONG map 1:1 vao 6 pipelines. Chung xuyen suot nhieu pipelines:

```
                    P1      P2      P3      P4      P5      P6
                   Client  Query   Tool   Multi    Ctx    Perm &
                    UI     Loop   Orch.   Agent   Mgmt    Sec
                   ------  ------  ------  ------  ------  ------
M1 Experience       [X]                                     [X]
M2 Intake           [X]     [X]     [X]     [X]
M3 Style                    [X]     [X]     [X]     [X]
M4 Canonical                        [X]             [X]     [X]
M5 2D Generation            [X]     [X]     [X]     [X]
M6 Review           [X]     [X]     [X]                     [X]
M7 3D Derivation    [X]     [X]     [X]     [X]     [X]
M8 Export                   [X]     [X]                     [X]
M9 Delivery         [X]                                     [X]
```

**Doc matrix nay de hieu:** Module M5 (2D Generation) su dung 4 pipelines: Query Loop (P2) de dieu phoi, Tool Orchestration (P3) de goi GPU, Multi-Agent (P4) cho Design Agent, va Context Management (P5) de quan ly context khi session dai.

**Cross-team implication:** Khi FE team lam M1, ho chi can quan tam P1 (UI) va P6 (permission UI). Khi BE team lam M5, ho can hieu P2+P3+P4+P5 dong thoi.

---

## 1. System Overview

```
                                 INTERNET
                                    |
                            +-------+-------+
                            |   Vercel CDN  |
                            |  (Frontend)   |
                            +-------+-------+
                                    |
                    +---------------+---------------+
                    |                               |
            REST API (HTTPS)              WebSocket (WSS)
                    |                               |
            +-------+-------+               +------+------+
            |   Railway     |               |  Socket.io  |
            |   (Backend)   +---------------+  Server     |
            |   FastAPI     |               +-------------+
            +---+---+---+---+
                |   |   |
        +-------+   |   +-------+
        |           |           |
   +----+----+ +---+---+ +----+----+
   |PostgreSQL| | Redis | |  S3     |
   | (Neon)   | |(Upstash)|(AWS)   |
   +----------+ +---+---+ +--------+
                    |
              +-----+-----+
              |   Celery   |
              |  Workers   |
              +-----+------+
                    |
              +-----+------+
              |   RunPod    |
              | GPU Service |
              | (ComfyUI)  |
              +-------------+
```

---

## 2. Module Architecture

### 2.1 Nine Business Modules

```
+------------------------------------------------------------------+
|                    EXPERIENCE LAYER (M1)                           |
|  [End-User Workspace] [KTS Review] [Admin] [Delivery]            |
+--------+---------+--------+--------+--------+--------+-----------+
         |         |        |        |        |        |
    +----+---+ +---+----+ +-+------+ +---+---+ +-----+----+ +-----+
    |M2      | |M3      | |M4      | |M5     | |M6        | |M7   |
    |Intake &| |Style   | |Canon.  | |2D Gen | |Review &  | |3D   |
    |Brief   | |Intel.  | |Design  | |Engine | |Annotate  | |Deriv.|
    +--------+ +--------+ |State   | +-------+ +----------+ +-----+
                           |(CORE) |
    +--------+ +---------+ +---+---+
    |M8      | |M9       |     |
    |Export  | |Delivery |     |
    |PDF/SVG | |Handoff  |     |
    +--------+ +---------+ TRUTH
```

### 2.2 Module Responsibilities (FINAL)

| Module | Build | Borrow | Ly do |
|--------|-------|--------|-------|
| M1 Experience Layer | Custom UI | shadcn/ui + Fabric.js + Three.js | UI la product identity, primitives borrow |
| M2 Intake & Brief | Custom logic | LangGraph (orchestration) | Brief schema la domain-specific |
| M3 Style Intelligence | Custom pipeline | - (Phase 2: Qdrant) | Phase 1 chi log data hooks |
| M4 Canonical Design State | **100% Custom** | - | DAY LA CORE. Khong outsource. |
| M5 2D Generation | Custom orchestration | ComfyUI + ControlNet + Diffusers | Generation backend borrow, orchestration custom |
| M6 Review & Annotation | Custom workflow | Fabric.js (canvas) | Approval logic la business core |
| M7 3D Derivation | Custom pipeline | Blender headless + Three.js | Pipeline custom, tools borrow |
| M8 Export & Package | Custom sheet system | WeasyPrint + Jinja2 + svgwrite + cairo | Sheet templates, title blocks, package manifest custom |
| M9 Delivery | Custom | S3 (storage) | Business logic custom |

---

## 3. Agentic OS - 6 Pipelines

### P1: Client UI Pipeline
```
Browser -> Next.js App Router -> REST API / WebSocket -> Backend
```
- Server Components cho static pages (dashboard, project list)
- Client Components cho interactive (chat, viewer, annotation)
- WebSocket cho realtime (generation progress, notifications)

### P2: Query Loop Pipeline
```python
async def query_loop(session_id, user_message):
    while True:
        # Phase 1: Context Assembly
        context = assemble_context(
            brief=get_brief(project_id),
            style=get_style_profile(kts_id),  # None in Phase 1
            canonical=get_canonical_state(version_id),
            memory=get_project_memory(project_id)
        )
        
        # Phase 2: LLM API Call (streaming)
        response = await llm.stream(context + user_message)
        yield response.chunks  # -> WebSocket -> Frontend
        
        # Phase 3: Tool Execution
        if response.tool_calls:
            results = await tool_orchestrator.execute(response.tool_calls)
            context.append(results)
        
        # Phase 4: Stop or Continue
        if not response.needs_follow_up:
            break
```

### P3: Tool Orchestration Pipeline

**12 Tools, 2 Categories:**

| Tool | Category | Concurrency | Module |
|------|----------|-------------|--------|
| DesignBriefGet | READ | Safe | M2 |
| DesignBriefUpdate | WRITE | Exclusive | M2 |
| StyleResolve | READ | Safe | M3 |
| StyleSearch | READ | Safe | M3 |
| BuildingCodeLookup | READ | Safe | M2 |
| FloorPlanGenerate | GPU | Exclusive | M5 |
| Render3D | GPU | Exclusive | M7 |
| ModelDerive | GPU | Exclusive | M7 |
| ExportPackage | WRITE | Exclusive | M8 |
| ExportSVG | WRITE | Exclusive | M8 |
| FeasibilityCheck | READ | Safe | M6 |
| DimensionCalc | READ | Safe | M4 |

**Execution Rule:**
- READ tools: run concurrently (batch)
- WRITE/GPU tools: run exclusively (one at a time)

### P4: Multi-Agent Coordination

```
                    Coordinator
                   (restricted tools)
                   /    |    \     \
                  /     |     \     \
    Requirements   Design   Review   Revision
    Agent (M2)    Agent    Agent    Agent
                  (M3+M5)  (M6)    (M5+M6)
                           READ-ONLY
```

**Coordinator restrictions:** Chi co AssignTask va SendFeedback. KHONG goi truc tiep GPU tools.

### P5: Context Management (5 Layers)

| Layer | Trigger | Action |
|-------|---------|--------|
| L1: Truncation | Tool result > 3000 chars | Persist to S3, keep pointer |
| L2: Microcompact | Token > 60% window | Remove stale tool_results (>5 turns old) |
| L3: Auto-compact | Token > 85% window | LLM summarize -> compact boundary |
| L4: Reactive | API 413 error | Emergency summarize + retry |
| L5: Memory Extract | End of session | Extract key decisions to project memory |

### P6: Permission & Security

```python
def check_permission(user, action, resource):
    # Layer 1: Role check
    if user.role not in ALLOWED_ROLES[action]:
        raise Forbidden()
    
    # Layer 2: Resource ownership
    if resource.org_id != user.org_id:
        raise Forbidden()
    
    # Layer 3: Version state check
    if action == "export" and resource.version.status not in ["approved", "locked"]:
        raise Forbidden("Version must be approved to export")
    
    # Layer 4: Budget check
    if action == "generate" and user.org.generation_budget_remaining <= 0:
        raise BudgetExceeded()
```

---

## 4. Data Flow - Key Use Cases

### UC-01: Intake -> First 2D Options

```
User types message
    -> WebSocket -> Backend
    -> Query Loop starts
    -> LLM extracts requirements
    -> Tool: BriefParse() -> partial brief
    -> LLM asks follow-up questions
    -> User answers
    -> Tool: BriefUpdate() -> complete brief
    -> User confirms
    -> Tool: FloorPlanGenerate(brief)
        -> Celery task -> GPU Service
        -> ComfyUI workflow executes
        -> 3 floor plan images -> S3
        -> Progress updates -> WebSocket -> Frontend
    -> 3 options returned
    -> Frontend renders OptionGallery
```

### UC-02: KTS Review -> Approve -> Lock

```
KTS opens review queue
    -> GET /api/v1/reviews -> list pending versions
KTS opens version
    -> GET /api/v1/versions/{id} -> brief + floor plans + renders
KTS adds annotation
    -> POST /api/v1/annotations -> save pin (x,y,comment) on version
KTS clicks Approve
    -> POST /api/v1/reviews/{version_id}/approve
    -> Permission check: role=architect, version.status=under_review
    -> State transition: under_review -> approved -> locked
    -> Create CanonicalPlanVersion snapshot
    -> Log to AuditTrail
    -> Feed approval signal to Style Intelligence data hooks
    -> Notification to project owner
```

### UC-03: Client Feedback -> AI Revision

```
Client opens share link
    -> GET /api/v1/share/{token} -> read-only project view
Client submits feedback
    -> POST /api/v1/feedback -> save feedback text
    -> Notification to KTS
KTS clicks "AI Revise"
    -> POST /api/v1/versions/{id}/revise
    -> Load: canonical version + client feedback + style profile
    -> Revision Agent:
        1. Map feedback to structured changes
        2. Update brief
        3. FloorPlanGenerate() with modified brief
        4. Save as new version (V3, parent=V2)
    -> New version created with lineage
```

---

## 5. Service Communication

### 5.1 Frontend <-> Backend

| Protocol | Use Case |
|----------|----------|
| REST (HTTPS) | CRUD operations, auth, export downloads |
| WebSocket (Socket.io) | Generation progress, notifications, live updates |

### 5.2 Backend <-> GPU Service

| Protocol | Use Case |
|----------|----------|
| HTTP POST | Submit generation job |
| HTTP GET | Poll job status |
| Webhook (callback) | Job completion notification |

### 5.3 Backend Internal

| Protocol | Use Case |
|----------|----------|
| Celery + Redis | Async task queue (generation, export) |
| Redis PubSub | Realtime event broadcast |
| S3 API | File upload/download |

---

## 6. Canonical Design State - Core Schema

```
CanonicalPlanVersion {
    id: UUID
    project_id: UUID
    version_number: int
    parent_version_id: UUID | null     // lineage
    status: VersionStatus              // state machine
    
    // M2 Output
    brief_json: JSONB                  // DesignBrief
    
    // M5 Output  
    geometry_json: JSONB               // Phase 1: basic metadata
    floor_plan_urls: string[]          // S3 URLs
    
    // M3 Output
    style_profile_id: UUID | null
    resolved_style_params: JSONB | null
    
    // M6 Output
    reviewed_by: UUID | null
    reviewed_at: timestamp | null
    approval_status: string | null
    
    // M7 Output (derived)
    render_urls: string[]
    model_url: string | null           // GLTF
    
    // M8 Output (derived) - Professional sheet package
    export_urls: JSONB                 // {pdf: url, svg: url} (legacy single-file)
    // Also see export_packages table for full sheet packages
    
    // M9 Output
    bundle_id: UUID | null
    
    // Reproducibility
    generation_metadata: JSONB         // model_id, workflow_version, prompt, seed
    
    // Timestamps
    created_at: timestamp
    updated_at: timestamp
    locked_at: timestamp | null
}
```

---

## 6b. M8 Export Pipeline - Professional Sheet Package

### Architecture (2 bac)

```
BAC 1 (MVP Sprint 5-6): Image-based sheet package
=====================================================

  floor_plan_urls (PNG)  +  geometry_json (basic metadata)  +  render_urls (PNG)
          |                           |                              |
          v                           v                              v
  +------------------+     +--------------------+     +------------------+
  | Floor Plan Sheet |     | Room Label Overlay |     |  Render Sheet    |
  | (image framed    |<----| (from geometry_json|     | (images framed   |
  |  in sheet layout)|     |  rooms + areas)    |     |  in sheet layout)|
  +--------+---------+     +--------------------+     +--------+---------+
           |                                                    |
           v                                                    v
  +---------------------------------------------------------------------+
  |                    Sheet Template System                              |
  |  Jinja2 templates + WeasyPrint                                       |
  |  - base_sheet.html (title block, margins, @page CSS)                 |
  |  - cover_sheet.html (A0: project info, sheet index, disclaimer)      |
  |  - floor_plan_sheet.html (A2: image + room labels + title block)     |
  |  - render_sheet.html (renders + title block)                         |
  +------+--------------------------------------------------------------+
         |
         v
  +------------------+     +------------------+     +------------------+
  | Combined PDF     |     | Per-sheet SVG    |     | Package Manifest |
  | (multi-page)     |     | (image in frame) |     | JSON             |
  +------------------+     +------------------+     +------------------+


BAC 2 (MVP+ Sprint 21-24): Geometry-based vector package
=========================================================

  geometry_json (Layer 1.5: walls, openings, rooms, levels, site, roof)
          |
          v
  +---------------------------------------------------------------------+
  |                  Sheet Composition Engine                             |
  |  - FloorPlanRenderer: geometry -> SVG (walls, openings, fixtures)    |
  |  - ElevationRenderer: geometry -> SVG (2 principal elevations)       |
  |  - SectionRenderer: geometry -> SVG (1 key section)                  |
  |  - SitePlanRenderer: site boundary + footprint -> SVG                |
  |  - DimensionEngine: auto-place overall + room dimensions             |
  |  - RoomTagEngine: auto-place name + area tags                        |
  |  Tech: svgwrite + cairo for vector rendering                         |
  +------+--------------------------------------------------------------+
         |
         v
  Full P1 Schematic Design Package:
    A0: Cover/Issue sheet
    A1: Site/Plot sheet
    A2+: Floor Plan per level (TRUE VECTOR)
    A4: 2 Principal Elevations
    A5: 1 Key Section
  + Combined PDF + Per-sheet SVG + PNG previews + Manifest JSON
```

### Title Block Contract

Moi sheet phai co title block voi:
- Project name
- Sheet title + sheet number
- Issue date + revision label
- Scale (per sheet)
- Preparer/company name
- Disclaimer reference

### Package Positioning

- UI wording: "Xuat ho so thiet ke so bo" (Issue schematic package)
- Disclaimer: "THIET KE SO BO - KHONG DUNG CHO XIN PHEP XAY DUNG"
- KHONG dung: "Ho so thi cong", "Ho so xin phep", "San sang nop"

---

## 7. Escalating Recovery (Generation Failures)

```
Level 1: Retry same config (max 3 times)
    |-- fail -->
Level 2: Reduce params (resolution 2048->1024, remove ControlNet)
    |-- fail -->
Level 3: Switch model (SDXL -> SD 1.5)
    |-- fail -->
Level 4: Switch pipeline (ComfyUI -> Diffusers)
    |-- fail -->
Level 5: Surface error to user with options:
    - "Thu lai sau"
    - "Don gian hoa yeu cau"
    - "Lien he support"
```

---

## 8. Security Architecture

```
Browser                    Backend                      Services
  |                          |                             |
  |-- JWT (Bearer) -------->|                             |
  |                          |-- verify token             |
  |                          |-- check role               |
  |                          |-- check org ownership      |
  |                          |-- check version state      |
  |                          |                             |
  |                          |-- API Key (internal) ----->|
  |                          |   (GPU, S3)                |
  |                          |                             |
  |<-- Set-Cookie (refresh)--|                             |
```

- Access Token: 15 min, in Authorization header
- Refresh Token: 7 days, HttpOnly cookie
- Share Token: 30 days, UUID in URL path
- GPU API Key: Internal service, not exposed to frontend
- S3: Pre-signed URLs for uploads/downloads (15 min expiry)

---

## 9. Folder Structure - Final

### ai-architect-web
```
src/
  app/                          # Next.js App Router
    (auth)/login/page.tsx
    (auth)/register/page.tsx
    dashboard/page.tsx
    projects/[id]/
      intake/page.tsx
      designs/page.tsx
      viewer/page.tsx           # P1
      review/page.tsx
      versions/page.tsx
      export/page.tsx
    share/[token]/page.tsx
    layout.tsx
    globals.css
  components/
    ui/                         # shadcn/ui (customized)
    layout/                     # AppShell, TopNav, Sidebar
    common/                     # StatusBadge, ProjectCard, etc.
    intake/                     # ChatInterface, IntakeForm, BriefEditor
    generation/                 # OptionGallery, OptionCard, Progress
    viewer/                     # FloorPlanViewer, Viewer3D (P1)
    review/                     # ReviewWorkspace, AnnotationLayer
    export/                     # ExportDialog, PdfPreview
    dashboard/                  # ProjectList, StatsBar
  lib/
    api-client.ts               # Typed API client (fetch wrapper)
    socket.ts                   # Socket.io client setup
    utils.ts
  stores/
    ui-store.ts                 # Sidebar state, active workspace
    annotation-store.ts         # Fabric.js annotation state
  hooks/
    use-project.ts              # TanStack Query hooks
    use-generation.ts
    use-notifications.ts
  types/
    api.ts                      # API response types (from OpenAPI)
    domain.ts                   # Domain types
```

### ai-architect-api
```
app/
  api/v1/
    auth.py
    projects.py
    designs.py
    versions.py
    reviews.py
    annotations.py
    feedback.py
    exports.py
    share.py
    notifications.py
  engine/
    query_loop.py
    state_machine.py
    recovery.py
  agents/
    coordinator.py
    requirements_agent.py
    design_agent.py
    review_agent.py
    revision_agent.py
  tools/
    base.py
    orchestrator.py
    brief_tools.py
    generation_tools.py
    style_tools.py
    export_tools.py
    check_tools.py
  context/
    compact.py
    microcompact.py
    truncation.py
    memory/
  permissions/
    classifier.py
    roles.py
    review_gate.py
    budget.py
    audit.py
  models/                       # SQLAlchemy models
  schemas/                      # Pydantic schemas
  services/
    gpu_client.py
    pdf_export.py
    svg_export.py
    file_storage.py
    notification.py
  core/
    config.py
    security.py
    database.py
    dependencies.py
  main.py
migrations/                     # Alembic
tests/
Dockerfile
docker-compose.yml              # Dev only
```

### ai-architect-gpu
```
comfyui/
  workflows/
    floor_plan_gen.json
    exterior_render.json
    interior_render.json
    revision_gen.json
  models/                       # Symlink to model storage
  custom_nodes/
pipelines/
  floor_plan_pipeline.py        # Diffusers fallback
  blender_3d_pipeline.py
  post_processing.py
api/
  server.py
  schemas.py
  health.py
scripts/
  download_models.sh
  setup_blender.sh
Dockerfile.gpu
docker-compose.gpu.yml          # Dev only
```
