# 04 - Implementation Directives

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*
*BAT BUOC doc truoc khi code*

---

## 1. General Rules (Tat ca teams)

### 1.1 Git Workflow

```
main (protected)
  └── develop (integration)
        ├── feature/CP1-auth-backend
        ├── feature/CP1-auth-frontend
        ├── feature/CP2-intake-chat
        └── fix/CP1-jwt-refresh
```

- **Branch naming:** `feature/CP{N}-{short-description}` hoac `fix/CP{N}-{description}`
- **Commit message:** `feat(M2): add chat intake endpoint` (Conventional Commits)
- **PR size:** Max 400 lines changed. Lon hon -> tach PR.
- **Review:** 1 approval bat buoc. Cross-team review cho API contracts.
- **Merge:** Squash merge vao develop. Develop merge vao main khi checkpoint done.
- **KHONG force push** vao develop hoac main.

### 1.2 Code Style

| Repo | Formatter | Linter | Config |
|------|-----------|--------|--------|
| web | Prettier | ESLint | Strict TypeScript |
| api | Black | Ruff | pyproject.toml |
| gpu | Black | Ruff | pyproject.toml |

- **Pre-commit hooks bat buoc:** format + lint + type check
- **Khong merge** neu CI fail

### 1.3 Environment Variables

- **KHONG hardcode** secrets trong code
- Dung `.env.local` cho dev, `.env.example` cho template
- Moi env var phai co trong `.env.example` voi comment
- Production secrets qua platform env (Vercel/Railway/RunPod)

### 1.4 Error Handling

```python
# Backend: DUNG
raise HTTPException(status_code=404, detail={"code": "PROJECT_NOT_FOUND", "message": "..."})

# Backend: SAI
raise Exception("Project not found")  # Khong co status code, khong co code
```

```typescript
// Frontend: DUNG
const { data, error } = useQuery(...)
if (error) return <ErrorState message={error.message} />

// Frontend: SAI
try { ... } catch(e) { console.log(e) }  // Nuot error
```

---

## 2. Frontend Directives (ai-architect-web)

### 2.1 Component Rules

1. **Dung shadcn/ui lam base** - Khong tu viet Button, Input, Dialog tu dau. Init shadcn/ui roi customize.
2. **Design tokens BAT BUOC** - Dung CSS custom properties. KHONG hardcode hex values.
   ```tsx
   // DUNG
   className="text-foreground bg-background shadow-border"
   
   // SAI
   className="text-[#171717] bg-white border border-gray-200"
   ```
3. **Shadow-as-border** - Dung `box-shadow` thay CSS border cho cards, inputs.
   ```css
   /* DUNG */
   box-shadow: rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
   
   /* SAI */
   border: 1px solid #ebebeb;
   ```
4. **Server Components default** - Chi dung `"use client"` khi can interactivity.
5. **Co-location** - Component file + types + hooks cung folder.

### 2.2 State Management Rules

```
Server State (TanStack Query)     Client State (Zustand)
├── Projects list                 ├── Sidebar open/close
├── Version data                  ├── Active workspace tab
├── Annotations                   ├── Annotation tool mode
├── Generation status             └── Theme (future)
└── Notifications
```

- **KHONG dung Zustand cho data tu API.** Dung TanStack Query.
- **KHONG fetch data trong useEffect.** Dung `useQuery` hook.
- **Optimistic updates** cho: annotation create, review actions.

### 2.3 API Client Pattern

```typescript
// lib/api-client.ts
const api = {
  projects: {
    list: (params) => fetchApi<Project[]>('/projects', { params }),
    get: (id) => fetchApi<Project>(`/projects/${id}`),
    create: (data) => fetchApi<Project>('/projects', { method: 'POST', body: data }),
  },
  versions: {
    get: (id) => fetchApi<DesignVersion>(`/versions/${id}`),
    approve: (id) => fetchApi<void>(`/reviews/${id}/approve`, { method: 'POST' }),
  },
}

// hooks/use-project.ts
export function useProject(id: string) {
  return useQuery({
    queryKey: ['project', id],
    queryFn: () => api.projects.get(id),
  })
}
```

### 2.4 Responsive Rules

```
Mobile (<640px):    1 column, sidebar hidden, carousel for cards
Tablet (640-1023):  2 columns, sidebar collapsed (icons only)
Desktop (>=1024):   Full layout, sidebar expanded, 3-column grids
```

- **Test o 3 breakpoints:** 375px (iPhone SE), 768px (iPad), 1280px (laptop)
- **Mobile-first CSS** - Base styles cho mobile, `md:` va `lg:` cho larger

### 2.5 Image Rules

- Floor plan thumbnails: `aspect-ratio: 4/3`
- 3D renders: `aspect-ratio: 16/9`
- Dung Next.js `<Image>` component voi `srcSet` cho responsive
- Lazy load images below fold
- Skeleton placeholder -> fade in

### 2.6 WebSocket Integration

```typescript
// lib/socket.ts
const socket = io(API_URL, { auth: { token: getAccessToken() } })

// Generation progress
socket.on('generation:progress', ({ jobId, progress, stage }) => {
  queryClient.setQueryData(['generation', jobId], { progress, stage })
})

// Notifications
socket.on('notification', (data) => {
  queryClient.invalidateQueries({ queryKey: ['notifications'] })
  toast({ title: data.message })
})
```

---

## 3. Backend Directives (ai-architect-api)

### 3.1 API Design Rules

1. **RESTful endpoints** - `GET /projects`, `POST /projects`, `GET /projects/{id}`
2. **Version prefix** - `/api/v1/...`
3. **Pagination** - `?page=1&per_page=20` cho list endpoints
4. **Filtering** - `?status=draft&search=keyword`
5. **Error format** - Consistent across all endpoints:
   ```json
   {
     "code": "VALIDATION_ERROR",
     "message": "Human-readable message",
     "details": [{"field": "lot.width_m", "error": "Must be positive"}]
   }
   ```

### 3.2 Domain Model Rules

```python
# models/version.py
class DesignVersion(Base):
    __tablename__ = "design_versions"
    
    # KHONG dung String cho status. Dung Enum.
    status = Column(Enum(VersionStatus), nullable=False, default=VersionStatus.DRAFT)
    
    # KHONG luu file content trong DB. Luu S3 URL.
    floor_plan_urls = Column(ARRAY(String), default=[])
    
    # JSONB cho flexible data (brief, geometry, metadata)
    brief_json = Column(JSONB, nullable=True)
    generation_metadata = Column(JSONB, nullable=True)
```

### 3.3 State Machine Rules

```python
# VALID TRANSITIONS ONLY
VALID_TRANSITIONS = {
    VersionStatus.DRAFT: [VersionStatus.GENERATED],
    VersionStatus.GENERATED: [VersionStatus.UNDER_REVIEW, VersionStatus.SUPERSEDED],
    VersionStatus.UNDER_REVIEW: [VersionStatus.APPROVED, VersionStatus.REJECTED],
    VersionStatus.APPROVED: [VersionStatus.LOCKED],
    VersionStatus.REJECTED: [],  # Tao version moi thay vi transition
    VersionStatus.LOCKED: [VersionStatus.HANDOFF_READY],
    VersionStatus.HANDOFF_READY: [VersionStatus.DELIVERED],
}

def transition_version(version, new_status, actor):
    if new_status not in VALID_TRANSITIONS[version.status]:
        raise InvalidTransition(f"Cannot go from {version.status} to {new_status}")
    
    old_status = version.status
    version.status = new_status
    
    # ALWAYS log to audit trail
    create_audit_log(version, old_status, new_status, actor)
```

### 3.4 Permission Rules

```python
# permissions/roles.py
ROLE_PERMISSIONS = {
    "user": ["read_own_projects", "create_project", "send_feedback"],
    "client": ["read_shared", "send_feedback"],
    "architect": ["read_all_projects", "create_project", "review", "approve", 
                  "reject", "annotate", "export", "generate", "revise"],
    "admin": ["*"],  # All permissions
    "contractor": ["read_handoff", "download_bundle"],
}
```

### 3.5 Celery Task Rules

```python
# tasks/generation_task.py
@celery_app.task(
    bind=True,
    max_retries=3,           # Level 1 retry
    default_retry_delay=5,
    acks_late=True,          # Acknowledge after completion
)
def generate_floor_plan(self, version_id: str, brief: dict):
    try:
        result = gpu_client.generate(brief)
        # Save to S3, update version
    except GPUTimeoutError as e:
        # Retry with same config (Level 1)
        raise self.retry(exc=e)
    except GPUMaxRetriesError:
        # Escalate to Level 2 (reduce params)
        generate_floor_plan_reduced.delay(version_id, brief)
```

### 3.6 LangGraph Rules

```python
# engine/query_loop.py
# LangGraph state chi chua conversation context
# KHONG chua project data, version status, approval state

class QueryState(TypedDict):
    messages: list[BaseMessage]
    needs_follow_up: bool
    current_tool_results: list[ToolResult]

# Project data LUON doc tu database
# KHONG cache trong graph state
```

### 3.7 Audit Trail Rules

```python
# MOI state transition phai co audit log
# MOI generation job phai co metadata log
# MOI export phai co log

def create_audit_log(
    project_id: UUID,
    version_id: UUID,
    user_id: UUID,
    action: str,          # "approve", "reject", "generate", "export"
    details: dict,        # Action-specific details
):
    AuditLog.create(
        project_id=project_id,
        version_id=version_id,
        user_id=user_id,
        action=action,
        details_json=details,
        created_at=utcnow(),
    )
```

---

## 4. GPU Service Directives (ai-architect-gpu)

### 4.1 API Contract

```python
# POST /generate/floor-plan
{
    "job_id": "uuid",
    "brief": { ... },           # DesignBrief JSON
    "style_params": { ... },    # Optional style constraints
    "config": {
        "model": "sdxl",
        "resolution": 2048,
        "num_options": 3,
        "seed": 42,             # For reproducibility
        "controlnet": true
    },
    "callback_url": "https://api.../webhooks/generation"
}

# Response
{
    "job_id": "uuid",
    "status": "queued"
}

# Webhook callback
{
    "job_id": "uuid",
    "status": "completed",
    "results": [
        {"option_id": "a", "image_url": "s3://...", "metadata": {...}},
        {"option_id": "b", "image_url": "s3://...", "metadata": {...}},
        {"option_id": "c", "image_url": "s3://...", "metadata": {...}}
    ],
    "generation_metadata": {
        "model_id": "sdxl-base-1.0",
        "workflow_version": "v1.2",
        "prompt": "...",
        "seed": 42,
        "controlnet_model": "sdxl-controlnet-canny",
        "duration_seconds": 45
    }
}
```

### 4.2 Reproducibility Rules

- **Moi job luu:** model_id, workflow_version, full prompt, seed, controlnet params
- **Workflow JSON versioned** trong git
- **Model checkpoints** pinned by hash
- **Random seed** controlled: cung seed + cung config = tuong tu output

### 4.3 Resource Management

- **GPU memory:** Clear VRAM after each job
- **Timeout:** 300s per generation job
- **Queue:** Max 10 pending jobs, reject khi full
- **Health check:** `/health` endpoint, check GPU availability

---

## 5. Cross-Team Rules

### 5.1 API Contract First

1. Backend define OpenAPI schema TRUOC khi implement
2. Frontend va Backend review contract CUNG nhau
3. Frontend co the mock API tu OpenAPI schema de develop song song
4. KHONG thay doi API contract ma khong thong bao team khac

### 5.2 Type Sharing

```
Backend (Pydantic) ──> OpenAPI JSON ──> Frontend (TypeScript types)
```

- Backend export OpenAPI spec tai `/api/v1/openapi.json`
- Frontend generate types tu OpenAPI: `npx openapi-typescript`
- Run type generation trong CI

### 5.3 Feature Flags

```typescript
// Dung cho P1 features (3D viewer, notifications panel)
const FEATURES = {
  VIEWER_3D: process.env.NEXT_PUBLIC_FF_VIEWER_3D === 'true',
  NOTIFICATIONS: process.env.NEXT_PUBLIC_FF_NOTIFICATIONS === 'true',
  STYLE_INTELLIGENCE: false,  // Phase 2
}
```

### 5.4 Data Hooks cho Style Intelligence

Du M3 la Phase 2, Phase 1 PHAI log data nay:
```python
# Moi khi KTS approve/reject, log:
style_data_log.save({
    "event": "approve",  # or "reject"
    "version_id": version.id,
    "kts_id": kts.id,
    "brief_json": version.brief_json,
    "floor_plan_urls": version.floor_plan_urls,
    "annotations": annotations,
    "feedback": feedback_text,
    "timestamp": utcnow(),
})
```

---

## 6. Design System Directives

### 6.1 Colors - KHONG hardcode

```css
/* globals.css - DUNG CAC TOKEN NAY */
:root {
  --color-foreground: #171717;
  --color-background: #ffffff;
  --color-muted-foreground: #4d4d4d;
  --color-subtle-foreground: #666666;
  --color-surface: #fafafa;
  --color-divider: #ebebeb;
  --color-link: #0072f5;
  --color-primary: #171717;
  --color-primary-foreground: #ffffff;
  /* Status colors */
  --color-status-draft: #666666;
  --color-status-generating: #0a72ef;
  --color-status-review: #d97706;
  --color-status-approved: #059669;
  --color-status-rejected: #dc2626;
  --color-status-locked: #171717;
  --color-status-handoff: #7c3aed;
}
```

### 6.2 Typography - 3 Weights Only

- **400 (Normal):** Body text, descriptions
- **500 (Medium):** UI elements, nav, buttons
- **600 (Semibold):** Headings, emphasis
- **KHONG dung 700 (Bold)** ngoai tru micro badges

### 6.3 Spacing - 16-32 Jump Rule

```
Gap giua components: gap-4 (16px) HOAC gap-8 (32px)
KHONG dung: gap-5 (20px), gap-6 (24px) cho gap giua components
gap-6 (24px) CHI dung cho padding BEN TRONG component
```

### 6.4 Shadow Levels

```
L0: none                          -> Background, text
L1: shadow-border                 -> Card resting, input
L2: shadow-subtle                 -> Standard card
L3: shadow-elevated               -> Selected card, hover
L4: shadow-focus                  -> Keyboard focus ring
```
