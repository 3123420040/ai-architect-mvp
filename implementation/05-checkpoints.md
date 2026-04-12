# 05 - Development Checkpoints

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*
*Tong: 6 Checkpoints, ~20 weeks*

---

## Team Structure

| Team | Members | Lead | Repo |
|------|---------|------|------|
| **FE** (Frontend) | 2-3 devs | Tech Lead Frontend | ai-architect-web |
| **BE** (Backend) | 2-3 devs | Tech Lead Backend | ai-architect-api |
| **AI** (GPU/AI) | 1-2 devs | Tech Lead AI | ai-architect-gpu |
| **DevOps** | 1 dev (shared) | - | All repos |

---

## Checkpoint Overview

```
CP1 (3w)     CP2 (3w)     CP3 (4w)     CP4 (3w)     CP5 (4w)     CP6 (3w)
Foundation   Intake       Generation   Review       3D+Export    Polish
   |            |            |            |            |            |
   v            v            v            v            v            v
Auth+Shell   Chat+Form    2D Options   Annotate     3D Render    Bug fix
DB+API       Brief JSON   GPU Pipeline Approve      PDF Export   Performance
DevOps       Query Loop   Gallery UI   Revision     Handoff      Launch
```

---

## CP1: Foundation (Week 1-3)

### Muc tieu
Tat ca 3 repos co the chay, auth hoat dong, app shell render duoc, database migrations done.

### Tasks

#### BE Team (ai-architect-api)
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-1.1 | Setup FastAPI project structure (theo 03-architecture-blueprint) | P0 | Server start, /health returns 200 |
| BE-1.2 | PostgreSQL + SQLAlchemy + Alembic setup | P0 | Migration tao duoc tables, rollback ok |
| BE-1.3 | Database models: User, Organization, Project, DesignVersion, AuditLog | P0 | All tables created, relations correct |
| BE-1.4 | Auth endpoints: register, login, refresh token | P0 | JWT flow works, tests pass |
| BE-1.5 | Project CRUD endpoints | P0 | Create, list, get, update project |
| BE-1.6 | Role-based permission middleware | P0 | user/architect/admin roles enforced |
| BE-1.7 | Redis + Celery setup | P0 | Celery worker starts, test task runs |
| BE-1.8 | S3/MinIO file upload service | P0 | Upload file, get presigned URL |
| BE-1.9 | Socket.io server setup | P0 | Client connects, receives events |
| BE-1.10 | Version state machine (core logic) | P0 | All transitions tested, invalid transitions rejected |
| BE-1.11 | Audit trail service | P0 | Every state change logged |
| BE-1.12 | OpenAPI spec exported | P0 | /api/v1/openapi.json accessible |

#### FE Team (ai-architect-web)
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-1.1 | Setup Next.js 14 + TypeScript + Tailwind + shadcn/ui | P0 | Dev server runs, builds successfully |
| FE-1.2 | Design tokens CSS (globals.css) theo 09-design-tokens.md | P0 | All tokens defined, Tailwind config maps them |
| FE-1.3 | Geist font setup | P0 | Geist Sans + Mono loaded, fallbacks set |
| FE-1.4 | AppShell component (TopNav + Sidebar + Main content area) | P0 | Responsive: desktop/tablet/mobile |
| FE-1.5 | shadcn/ui base components: Button, Input, Dialog, Tabs, Toast | P0 | Customized theo Vercel tokens |
| FE-1.6 | Login + Register pages | P0 | Forms validate, call API, store JWT |
| FE-1.7 | API client + TanStack Query setup | P0 | Typed client, auth headers auto |
| FE-1.8 | Socket.io client setup | P0 | Connects to backend, receives events |
| FE-1.9 | Dashboard page (empty state + project list shell) | P0 | ProjectCard component, responsive grid |
| FE-1.10 | StatusBadge component (all 8 statuses) | P0 | Colors correct, all variants render |
| FE-1.11 | Generate TypeScript types from OpenAPI | P0 | Script runs, types match API |

#### AI Team (ai-architect-gpu)
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-1.1 | Setup GPU service project (FastAPI wrapper) | P0 | Server starts, /health returns GPU info |
| AI-1.2 | ComfyUI installation + API mode | P0 | ComfyUI accepts workflow JSON via API |
| AI-1.3 | Download SD XL + ControlNet models | P0 | Models loaded, test inference works |
| AI-1.4 | Basic floor plan generation workflow (ComfyUI) | P0 | Text prompt -> floor plan image |
| AI-1.5 | Dockerfile.gpu working | P0 | Docker build + run with GPU access |

#### DevOps
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| DO-1.1 | docker-compose.yml cho local dev (postgres + redis + minio) | P0 | One command starts all deps |
| DO-1.2 | GitHub repos created (3 repos) | P0 | Branch protection on main |
| DO-1.3 | CI pipeline: lint + type check + test | P0 | Runs on every PR |
| DO-1.4 | .env.example cho moi repo | P0 | All vars documented |

### Merge Strategy CP1
```
FE: feature/CP1-* -> develop (FE lead reviews)
BE: feature/CP1-* -> develop (BE lead reviews)
AI: feature/CP1-* -> develop (AI lead reviews)
End of CP1: develop -> main (Tech Lead + PM sign-off)
```

### Demo CP1
- Login, see empty dashboard
- Create project, see in list
- Backend API Swagger docs
- GPU service generates test floor plan image

---

## CP2: Intake & Brief (Week 4-6)

### Muc tieu
User co the chat voi AI de tao Design Brief, hoac dung form. Brief JSON duoc luu va editable.

### Tasks

#### BE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-2.1 | LangGraph setup + Query Loop engine | P0 | Async generator works, streaming ok |
| BE-2.2 | Requirements Agent (M2) | P0 | Extract requirements from chat, detect missing info |
| BE-2.3 | BriefParse tool | P0 | User text -> partial DesignBrief JSON |
| BE-2.4 | BriefUpdate tool | P0 | Merge new info into existing brief |
| BE-2.5 | Design Brief CRUD endpoints | P0 | Save, get, update brief for project |
| BE-2.6 | Chat history storage | P0 | Messages saved, retrievable |
| BE-2.7 | WebSocket: chat message streaming | P0 | LLM response streams to frontend chunk by chunk |
| BE-2.8 | Structured form validation endpoint | P0 | Validate form data against brief schema |
| BE-2.9 | Context Management L1 (truncation) | P1 | Large tool results truncated + persisted |

#### FE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-2.1 | ChatInterface component | P0 | Send/receive messages, auto-scroll, typing indicator |
| FE-2.2 | Chat page (/projects/[id]/intake) | P0 | Full chat flow with AI |
| FE-2.3 | IntakeForm component (multi-step wizard) | P0 | 5 steps, validation, navigation |
| FE-2.4 | Form page (alternative to chat) | P0 | Form submits brief data |
| FE-2.5 | BriefEditor component | P0 | KTS can view and edit brief inline |
| FE-2.6 | BriefSummaryCard | P0 | Compact brief display after confirmation |
| FE-2.7 | Mode switcher (Chat / Form) | P0 | Toggle between intake modes |
| FE-2.8 | Sidebar navigation items for project | P0 | Links to intake, designs, review, etc. |

#### AI Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-2.1 | Refine floor plan generation workflow | P0 | Better quality with ControlNet conditioning |
| AI-2.2 | Multi-option generation (3 variations) | P0 | 3 different floor plans from same brief |
| AI-2.3 | Generation API endpoint with job queue | P0 | POST /generate -> queued -> callback |
| AI-2.4 | Progress reporting | P0 | GPU service reports 0-100% progress |

### Merge Strategy CP2
- Same as CP1. Cross-team review cho WebSocket integration (FE+BE).

### Demo CP2
- User chats with AI, AI asks questions, brief is created
- User uses form as alternative, brief is created
- KTS edits brief
- Brief JSON displayed correctly

---

## CP3: 2D Generation & Gallery (Week 7-10)

### Muc tieu
User hoan tat intake -> AI generate 3 floor plan options -> User xem gallery va chon 1 option.

### Tasks

#### BE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-3.1 | Design Agent (M5) integration with GPU | P0 | Brief -> GPU -> 3 floor plan images |
| BE-3.2 | Generation orchestration (Celery + GPU client) | P0 | Job queued, progress tracked, results saved |
| BE-3.3 | FloorPlanGenerate tool | P0 | Tool callable from Query Loop |
| BE-3.4 | DesignVersion creation after generation | P0 | 3 versions created (draft -> generated) |
| BE-3.5 | Option selection endpoint | P0 | User selects option, status -> under_review |
| BE-3.6 | WebSocket progress updates | P0 | Realtime progress from GPU to frontend |
| BE-3.7 | Escalating recovery Level 1-3 | P0 | Retry, reduce params, switch model |
| BE-3.8 | Generation metadata logging | P0 | model_id, seed, prompt, duration saved |
| BE-3.9 | Tool Orchestrator (partitioning logic) | P0 | READ concurrent, WRITE exclusive |
| BE-3.10 | Context Management L2 (microcompact) | P1 | Stale tool results removed |

#### FE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-3.1 | GenerationProgress component | P0 | Spinner, progress bar, stage text |
| FE-3.2 | OptionGallery component | P0 | 3 cards, responsive grid |
| FE-3.3 | OptionCard component | P0 | Image 4:3, title, description, select button |
| FE-3.4 | Designs page (/projects/[id]/designs) | P0 | Gallery + selection flow |
| FE-3.5 | FloorPlanImage component (zoomable) | P0 | Click to lightbox, pinch-to-zoom |
| FE-3.6 | EmptyState component | P0 | Shown when no designs yet |
| FE-3.7 | Generation error state (Recovery L5 UI) | P0 | After all retries fail: show 3 options (retry later / simplify requirements / contact support) per UC-07 |
| FE-3.8 | Version create flow (after selection) | P0 | Selected option -> under_review |

#### AI Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-3.1 | Production-quality floor plan workflow | P0 | Architectural-looking floor plans |
| AI-3.2 | ControlNet edge conditioning | P0 | Floor plans follow lot dimensions |
| AI-3.3 | Seed control for reproducibility | P0 | Same seed = similar output |
| AI-3.4 | Post-processing: label overlay, dimension annotation | P1 | Room labels on floor plan images |
| AI-3.5 | Fallback pipeline (Diffusers) | P0 | Works when ComfyUI fails |
| AI-3.6 | Escalating recovery Level 4 (pipeline switch) | P0 | ComfyUI fail -> Diffusers |

### Demo CP3
- Full flow: intake -> generate -> see 3 options -> select one
- Progress shown realtime
- Generation recovery works on failure

---

## CP4: Review & Revision (Week 11-13)

### Muc tieu
KTS review floor plan, annotate, approve/reject. Client feedback triggers revision. Version lineage works.

### Tasks

#### BE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-4.1 | Review endpoints (approve, reject, request revision) | P0 | State transitions correct |
| BE-4.2 | Annotation CRUD endpoints | P0 | Create, list, update, delete pins |
| BE-4.3 | Feedback endpoints | P0 | Client submits, KTS receives notification |
| BE-4.4 | Share link generation + token auth | P0 | Token-based read-only access |
| BE-4.5 | Revision Agent (M5+M6) | P0 | Feedback -> structured changes -> regenerate |
| BE-4.6 | Version lineage (parent_version_id) | P0 | V3.parent = V2, chain traceable |
| BE-4.7 | Notification service (in-app) | P0 | Feedback, review request, generation done |
| BE-4.8 | Style Intelligence data hooks | P0 | Log approve/reject events for future M3 |
| BE-4.9 | Compare endpoint (2 versions) | P1 | Return diff data |

#### FE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-4.1 | FloorPlanViewer (pan/zoom, Fabric.js) | P0 | Smooth pan/zoom on desktop + mobile |
| FE-4.2 | AnnotationLayer (pin + comment) | P0 | Click to add pin, enter comment |
| FE-4.3 | AnnotationList in review panel | P0 | Click item -> scroll to pin |
| FE-4.4 | ReviewWorkspace (split layout) | P0 | Floor plan left, panel right (360px) |
| FE-4.5 | ReviewActions (approve/reject/revise buttons) | P0 | Reject requires reason |
| FE-4.6 | Share link page (/share/[token]) | P0 | Read-only gallery + feedback form |
| FE-4.7 | VersionTimeline component | P0 | Vertical timeline, status colors |
| FE-4.8 | Version compare (side-by-side) | P1 | 2 floor plans synced zoom |
| FE-4.9 | Notification bell + dropdown | P1 | Unread count, mark read |

#### AI Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-4.1 | Revision workflow (feedback-conditioned) | P0 | Modified floor plan based on structured feedback |
| AI-4.2 | Exterior render workflow | P0 | Floor plan -> ControlNet -> exterior image |
| AI-4.3 | Interior render workflow (3 rooms) | P0 | Room layout -> interior render |

### Demo CP4
- KTS reviews floor plan, adds annotations, approves
- Client opens share link, submits feedback
- KTS triggers AI revision, V3 created from V2
- Version timeline shows lineage

---

## CP5: 3D, Export & Delivery (Week 14-17)

### Muc tieu
3D renders tu locked version, PDF export, handoff bundle. Full workflow end-to-end.

### Tasks

#### BE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-5.1 | 3D derivation endpoint (trigger from locked version) | P0 | Creates Celery task for 3D |
| BE-5.2 | Sheet template system (Jinja2 + WeasyPrint) | P0 | base_sheet, title_block, disclaimer, revision_label templates |
| BE-5.3 | Cover sheet (A0) generation | P0 | Project name, sheet index, date, revision, branding, disclaimer |
| BE-5.4 | Floor plan sheet generation | P0 | Floor plan IMAGE framed with title block + room labels overlay from geometry_json |
| BE-5.5 | Render sheet generation | P0 | 3D renders framed with title block |
| BE-5.6 | Multi-page PDF composer | P0 | Assemble sheets into single PDF package |
| BE-5.7 | Per-sheet SVG export | P0 | Floor plan image embedded in sheet frame SVG |
| BE-5.8 | Package manifest JSON generation | P0 | package_id, sheets, revision, files, export_timestamp |
| BE-5.9 | Watermark logic | P0 | "CONCEPT" watermark if not approved |
| BE-5.10 | Export endpoints | P0 | POST /export/{format}, download link |
| BE-5.11 | Handoff bundle creation | P1 | Zip: PDF + images + SVG + brief JSON + manifest + audit |
| BE-5.12 | Handoff readiness check | P1 | Version locked + approved + exports exist |
| BE-5.13 | Delivery workspace endpoints | P1 | List bundles, download |
| BE-5.14 | Context Management L3 (auto-compact) | P1 | LLM summarize for long sessions |
| BE-5.15 | Multi-Agent Coordinator | P1 | Requirements + Design + Review + Revision agents |
| BE-5.16 | Context Management L4 (reactive compact) | P1 | Handle API 413 error: emergency summarize + retry with circuit breaker |
| BE-5.17 | Context Management L5 (memory extract) | P1 | End-of-session extract key decisions to project memory |
| BE-5.18 | Recovery Level 5 (surface error to user) | P0 | After all recovery levels fail: show user-facing error with 3 options (retry/simplify/support) |

#### FE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-5.1 | ExportDialog component | P0 | Format selection, options, progress |
| FE-5.2 | Export page (/projects/[id]/export) | P0 | Export buttons, download links |
| FE-5.3 | PdfPreview component | P1 | Page-by-page preview |
| FE-5.4 | DeliveryBundleCard | P1 | Bundle info + download button |
| FE-5.5 | Viewer3D component (Three.js) | P1 | GLTF model, orbit, zoom |
| FE-5.6 | 3D Viewer page (/projects/[id]/viewer) | P1 | Full-screen viewer |
| FE-5.7 | StatsBar + MetricCard | P1 | Dashboard stats |
| FE-5.8 | NotificationPanel (full) | P1 | Dropdown, mark read, pagination |

#### AI Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-5.1 | Blender headless 3D pipeline | P1 | Floor plan -> 3D model -> GLTF |
| AI-5.2 | Exterior render (production quality) | P0 | High-res exterior from floor plan |
| AI-5.3 | Interior renders (3 rooms, production quality) | P0 | Living room, kitchen, master bedroom |
| AI-5.4 | Model optimization for web viewer | P1 | GLTF < 50MB, loads in < 5s |

### Demo CP5
- Full workflow: intake -> generate -> review -> approve -> lock -> 3D -> export -> handoff
- PDF downloaded as MULTI-PAGE SHEET PACKAGE (cover + floor plan sheets + render sheet), NOT image dump
- Every sheet has title block with project name, sheet number, date, revision
- Cover sheet has disclaimer "THIET KE SO BO - KHONG DUNG CHO XIN PHEP XAY DUNG"
- Package manifest JSON downloadable and matches PDF contents
- Watermark "CONCEPT" visible on unapproved versions
- 3D renders visible in gallery
- Interactive 3D viewer (if time permits)

---

## CP6: Polish & Launch (Week 18-20)

### Muc tieu
Bug fixes, performance optimization, security hardening, production deployment.

### Tasks

#### All Teams
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| ALL-6.1 | Bug fixing from CP5 demo | P0 | All P0 bugs resolved |
| ALL-6.2 | Performance audit (LCP, FID, CLS) | P0 | Meets NFR targets |
| ALL-6.3 | Security audit (OWASP top 10 check) | P0 | No critical/high vulnerabilities |
| ALL-6.4 | Error handling review | P0 | All user-facing errors have clear messages |
| ALL-6.5 | Mobile responsiveness QA | P0 | Works on 375px, 768px, 1280px |

#### DevOps
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| DO-6.1 | Production deployment (Vercel + Railway + RunPod) | P0 | All services running |
| DO-6.2 | SSL/domain setup (app.aiarchitect.vn) | P0 | HTTPS working |
| DO-6.3 | Monitoring + alerting (Sentry) | P0 | Errors captured, alerts configured |
| DO-6.4 | Database backup automation | P0 | Daily backup verified |
| DO-6.5 | Load test (50 concurrent users) | P0 | No crashes, response times ok |
| DO-6.6 | Staging environment | P0 | staging.aiarchitect.vn working |

### Demo CP6 (Launch Readiness)
- Full E2E demo on staging
- PM sign-off on all P0 features
- Security checklist completed
- Monitoring dashboard live
- Production deploy approved

---

## CP7: Full Schematic Package - MVP+ (Week 21-24)

### Muc tieu
Nang cap tu "professional PDF" (Bac 1) len "full schematic design package" (Bac 2) theo P1 2D Deliverable standard. Geometry upgrade len Layer 1.5. True vector SVG. Elevation + Section sheets.

### Dieu kien bat dau
- CP6 da launch thanh cong
- PDF sheet package (Bac 1) da hoat dong on

### Tasks

#### BE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| BE-7.1 | Geometry Layer 1.5 schema design va migration | P0 | geometry_json supports levels, walls, openings, rooms polygons, stairs, site, roof |
| BE-7.2 | Sheet Composition Engine core | P0 | SheetComposer class: geometry JSON -> Sheet objects |
| BE-7.3 | Floor Plan Vector Renderer | P0 | Geometry JSON -> SVG floor plan (walls, openings, fixtures, room tags) |
| BE-7.4 | Elevation Renderer | P0 | Geometry JSON -> SVG 2 principal elevations (facade, openings, roof, grade line) |
| BE-7.5 | Section Renderer | P0 | Geometry JSON -> SVG 1 key section (levels, heights, stair, roof) |
| BE-7.6 | Site Plan Renderer | P0 | Site boundary + building footprint + north arrow + scale bar -> SVG |
| BE-7.7 | Dimension engine | P0 | Overall + key room dimensions auto-placed on floor plan |
| BE-7.8 | Room tag engine | P0 | Room name + area tags auto-placed, no overlap with geometry |
| BE-7.9 | Line weight hierarchy system | P0 | Exterior walls heavier, interior lighter, fixtures lightest |
| BE-7.10 | Full package PDF composer (4-6 sheets) | P0 | Cover + Site + Floor Plans + Elevation + Section -> PDF |
| BE-7.11 | Style Intelligence (M3) import + extract + profile | P1 | KTS uploads portfolio -> AI extracts style -> profile CRUD |

#### FE Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| FE-7.1 | Sheet viewer component (per-sheet SVG display) | P0 | Zoom, pan, crisp vector rendering |
| FE-7.2 | Package viewer (multi-sheet browsing) | P0 | Sheet navigation, thumbnail sidebar |
| FE-7.3 | Style Intelligence UI (portfolio upload + profile review) | P1 | Upload, preview patterns, edit profile |

#### AI Team
| # | Task | Priority | Definition of Done |
|---|------|----------|-------------------|
| AI-7.1 | Canonicalization pipeline: floor plan image -> geometry Layer 1.5 | P0 | AI extracts walls, rooms, openings from generated floor plan image |
| AI-7.2 | Style Intelligence: portfolio ingestion + pattern extraction | P1 | Classify images, extract facade/material/spatial patterns |
| AI-7.3 | Style-conditioned generation | P1 | FloorPlanGenerate uses resolved style params |

### Acceptance Criteria CP7
- [ ] Package has 4-6 sheets (Cover, Site, Floor Plans, Elevation, Section)
- [ ] Floor plan is TRUE VECTOR SVG from geometry (not bitmap)
- [ ] 2 principal elevations derived from structured geometry
- [ ] 1 key section with floor-to-floor and roof relationship
- [ ] Site plan with boundary, footprint, north arrow, scale
- [ ] Wall hierarchy visible: exterior heavier than interior
- [ ] Dimensions: overall + key room dimensions
- [ ] Room tags: name + area, no overlap with walls
- [ ] Consistent title block across all sheets
- [ ] Package manifest JSON matches all sheet contents

---

## Checkpoint Sign-off Process

```
1. Dev completes all tasks in checkpoint
2. Tech Lead reviews: code quality, tests passing, DoD met
3. Cross-team integration test
4. Demo to PM + Stakeholders
5. PM sign-off
6. develop -> main merge
7. Deploy to staging (auto)
8. Smoke test on staging
9. Next checkpoint begins
```

---

## Risk Mitigation per Checkpoint

| Checkpoint | Biggest Risk | Mitigation |
|-----------|-------------|------------|
| CP1 | DevOps setup delays | Docker Compose cho local dev, khong doi infrastructure |
| CP2 | LangGraph learning curve | BE lead spike 2 days truoc CP2 |
| CP3 | Floor plan quality low | AI team iterate workflow tu CP1, co buffer 1 week |
| CP4 | Fabric.js annotation complexity | FE spike 2 days, fallback to simple HTML overlay |
| CP5 | Blender headless unstable | 3D viewer la P1, co the defer. Static renders la P0. |
| CP6 | Production deployment issues | Staging env san tu CP4 |

---

## Parallel Work Map

```
Week:  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
       |---CP1---|   |---CP2---|   |------CP3------|   |---CP4---|   |------CP5------|  |--CP6--|
FE:    [Shell+Auth]  [Chat+Form]  [Gallery+Progress]   [Review+Annot] [Export+Viewer]   [Polish]
BE:    [DB+API+Auth] [LangGraph]  [Generation+Tools]   [Review+Share] [Export+Handoff]  [Polish]
AI:    [GPU Setup  ] [Workflows]  [Prod Quality Gen]   [Render Flows] [Blender 3D    ]  [Polish]
DevOps:[Infra      ] [CI       ]  [Monitoring      ]   [Staging     ] [Prod Deploy   ]  [Launch]
```
