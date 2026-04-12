# 07 - Database Schema

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*
*Database: PostgreSQL 16*
*ORM: SQLAlchemy 2.0 + Alembic*

---

## 1. ER Diagram

```
organizations 1──* users
organizations 1──* projects
organizations 1──* style_profiles

users 1──* projects (as kts)
users 1──* projects (as client owner)
users 1──* annotations
users 1──* feedback
users 1──* audit_logs
users 1──* notifications

projects 1──* design_versions
projects 1──* share_links
projects 1──* handoff_bundles
projects 1──* chat_messages

design_versions 1──* annotations
design_versions 1──* feedback
design_versions *──1 design_versions (parent lineage)
design_versions *──1 style_profiles

style_profiles 1──* style_data_logs
```

---

## 2. Tables

### 2.1 organizations

```sql
CREATE TABLE organizations (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name            VARCHAR(255) NOT NULL,
    plan            VARCHAR(50) NOT NULL DEFAULT 'free',  -- free | pro | enterprise
    generation_budget_total    INT NOT NULL DEFAULT 100,
    generation_budget_used     INT NOT NULL DEFAULT 0,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);
```

### 2.2 users

```sql
CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id),
    email           VARCHAR(255) NOT NULL UNIQUE,
    password_hash   VARCHAR(255) NOT NULL,
    full_name       VARCHAR(255) NOT NULL,
    role            VARCHAR(50) NOT NULL DEFAULT 'user',
                    -- user | architect | admin | contractor
    avatar_url      VARCHAR(500),
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_org ON users(organization_id);
CREATE INDEX idx_users_email ON users(email);
```

### 2.3 projects

```sql
CREATE TABLE projects (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id),
    name            VARCHAR(255) NOT NULL,
    client_name     VARCHAR(255),
    client_phone    VARCHAR(50),
    client_user_id  UUID REFERENCES users(id),      -- If client has account
    kts_user_id     UUID REFERENCES users(id),       -- Assigned architect
    status          VARCHAR(50) NOT NULL DEFAULT 'new',
                    -- new | intake | generating | in_review | completed | archived
    brief_json      JSONB,                           -- DesignBrief
    brief_status    VARCHAR(50) DEFAULT 'draft',     -- draft | confirmed
    style_profile_id UUID REFERENCES style_profiles(id),
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_projects_org ON projects(organization_id);
CREATE INDEX idx_projects_kts ON projects(kts_user_id);
CREATE INDEX idx_projects_status ON projects(status);
```

### 2.4 design_versions

```sql
CREATE TABLE design_versions (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id          UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    parent_version_id   UUID REFERENCES design_versions(id),  -- Lineage
    version_number      INT NOT NULL,
    
    -- Status (state machine)
    status              VARCHAR(50) NOT NULL DEFAULT 'draft',
                        -- draft | generated | under_review | approved | rejected
                        -- | locked | handoff_ready | delivered | superseded
    
    -- Option info
    option_label        VARCHAR(100),               -- "Option A"
    option_description  VARCHAR(500),               -- "Hien dai toi gian"
    
    -- M2: Brief snapshot
    brief_json          JSONB,
    
    -- M5: Geometry + floor plans
    geometry_json       JSONB,                      -- Basic metadata Phase 1
    floor_plan_urls     TEXT[] DEFAULT '{}',         -- S3 URLs
    
    -- M3: Style
    style_profile_id    UUID REFERENCES style_profiles(id),
    resolved_style_params JSONB,
    
    -- M6: Review
    reviewed_by         UUID REFERENCES users(id),
    reviewed_at         TIMESTAMP WITH TIME ZONE,
    approval_status     VARCHAR(50),                -- approved | rejected
    rejection_reason    TEXT,
    
    -- M7: Derived assets
    render_urls         TEXT[] DEFAULT '{}',         -- S3 URLs (exterior + interiors)
    model_url           VARCHAR(500),               -- GLTF model S3 URL
    
    -- M8: Exports
    export_urls         JSONB DEFAULT '{}',         -- {"pdf": "url", "svg": "url"}
    
    -- M9: Bundle
    bundle_id           UUID REFERENCES handoff_bundles(id),
    
    -- Reproducibility
    generation_metadata JSONB,                      -- model_id, seed, prompt, workflow_version, duration
    
    -- Timestamps
    created_at          TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    locked_at           TIMESTAMP WITH TIME ZONE,
    
    UNIQUE(project_id, version_number)
);

CREATE INDEX idx_versions_project ON design_versions(project_id);
CREATE INDEX idx_versions_status ON design_versions(status);
CREATE INDEX idx_versions_parent ON design_versions(parent_version_id);
```

### 2.5 annotations

```sql
CREATE TABLE annotations (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    version_id      UUID NOT NULL REFERENCES design_versions(id) ON DELETE CASCADE,
    user_id         UUID NOT NULL REFERENCES users(id),
    x               FLOAT NOT NULL,                 -- Normalized 0-1
    y               FLOAT NOT NULL,                 -- Normalized 0-1
    floor_index     INT DEFAULT 0,                  -- Which floor plan
    comment         TEXT NOT NULL,
    is_resolved     BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_annotations_version ON annotations(version_id);
```

### 2.6 feedback

```sql
CREATE TABLE feedback (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    version_id      UUID NOT NULL REFERENCES design_versions(id) ON DELETE CASCADE,
    user_id         UUID NOT NULL REFERENCES users(id),
    type            VARCHAR(20) NOT NULL DEFAULT 'text',
                    -- text | annotation (per 05-system-design.md ER diagram)
    content         TEXT NOT NULL,
    structured_json JSONB,                          -- AI-parsed structured changes
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_feedback_version ON feedback(version_id);
```

### 2.7 chat_messages

```sql
CREATE TABLE chat_messages (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    role            VARCHAR(20) NOT NULL,            -- user | ai | system
    content         TEXT NOT NULL,
    metadata        JSONB,                          -- brief_updated, tool_calls, etc.
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_chat_project ON chat_messages(project_id);
CREATE INDEX idx_chat_created ON chat_messages(project_id, created_at);
```

### 2.8 share_links

```sql
CREATE TABLE share_links (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    token           VARCHAR(100) NOT NULL UNIQUE,
    created_by      UUID NOT NULL REFERENCES users(id),
    expires_at      TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active       BOOLEAN NOT NULL DEFAULT TRUE,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE UNIQUE INDEX idx_share_token ON share_links(token);
```

### 2.9 handoff_bundles

```sql
CREATE TABLE handoff_bundles (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id),
    version_id      UUID NOT NULL REFERENCES design_versions(id),
    is_current      BOOLEAN NOT NULL DEFAULT TRUE,
    files_manifest  JSONB NOT NULL,                 -- [{name, url, size_bytes, type}]
    readiness_label VARCHAR(50) NOT NULL,            -- handoff_ready | delivered
    created_by      UUID NOT NULL REFERENCES users(id),
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_bundles_project ON handoff_bundles(project_id);
```

### 2.10 notifications

```sql
CREATE TABLE notifications (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID NOT NULL REFERENCES users(id),
    type            VARCHAR(50) NOT NULL,
                    -- generation_complete | feedback_received | review_requested
                    -- | version_approved | version_rejected | handoff_ready
    message         TEXT NOT NULL,
    project_id      UUID REFERENCES projects(id),
    version_id      UUID REFERENCES design_versions(id),
    is_read         BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_notifications_user ON notifications(user_id, is_read);
CREATE INDEX idx_notifications_created ON notifications(user_id, created_at DESC);
```

### 2.11 audit_logs

```sql
CREATE TABLE audit_logs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID REFERENCES projects(id),
    version_id      UUID REFERENCES design_versions(id),
    user_id         UUID NOT NULL REFERENCES users(id),
    action          VARCHAR(100) NOT NULL,
                    -- create_project | update_brief | generate | approve | reject
                    -- | lock | export | create_handoff | revise | add_annotation
    details_json    JSONB,                          -- Action-specific details
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Audit logs are append-only, never updated or deleted
CREATE INDEX idx_audit_project ON audit_logs(project_id);
CREATE INDEX idx_audit_version ON audit_logs(version_id);
CREATE INDEX idx_audit_created ON audit_logs(created_at);
```

### 2.12 style_profiles

```sql
CREATE TABLE style_profiles (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id),
    kts_user_id     UUID NOT NULL REFERENCES users(id),
    version         INT NOT NULL DEFAULT 1,
    name            VARCHAR(255),
    patterns_json   JSONB,                          -- Extracted style patterns
    status          VARCHAR(50) NOT NULL DEFAULT 'draft',
                    -- draft | processing | ready | archived
    approved_at     TIMESTAMP WITH TIME ZONE,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_styles_kts ON style_profiles(kts_user_id);
```

### 2.13 style_data_logs (Data hooks cho Phase 2 M3)

```sql
CREATE TABLE style_data_logs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    kts_user_id     UUID NOT NULL REFERENCES users(id),
    event_type      VARCHAR(50) NOT NULL,            -- approve | reject | annotate | feedback
    version_id      UUID REFERENCES design_versions(id),
    brief_json      JSONB,
    floor_plan_urls TEXT[],
    annotations     JSONB,
    feedback_text   TEXT,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- This table is append-only. Data will feed Style Intelligence in Phase 2.
CREATE INDEX idx_style_logs_kts ON style_data_logs(kts_user_id);
CREATE INDEX idx_style_logs_created ON style_data_logs(created_at);
```

### 2.14 generation_jobs

```sql
CREATE TABLE generation_jobs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id),
    version_id      UUID REFERENCES design_versions(id),
    job_type        VARCHAR(50) NOT NULL,            -- floor_plan | render_3d | model_3d | export
    status          VARCHAR(50) NOT NULL DEFAULT 'queued',
                    -- queued | processing | completed | failed
    progress        INT DEFAULT 0,                   -- 0-100
    stage           VARCHAR(255),                    -- "Dang tao mat bang tang 1..."
    config_json     JSONB,                          -- Generation config
    result_json     JSONB,                          -- Result data (urls, metadata)
    error_message   TEXT,
    recovery_level  INT DEFAULT 0,                   -- 0-5
    started_at      TIMESTAMP WITH TIME ZONE,
    completed_at    TIMESTAMP WITH TIME ZONE,
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_jobs_project ON generation_jobs(project_id);
CREATE INDEX idx_jobs_status ON generation_jobs(status);
```

### 2.15 export_packages (P1 2D Deliverable)

```sql
CREATE TABLE export_packages (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id),
    version_id      UUID NOT NULL REFERENCES design_versions(id),
    
    -- Package metadata
    issue_type      VARCHAR(50) NOT NULL DEFAULT 'schematic-design-package',
    revision_label  VARCHAR(10) NOT NULL,              -- A, B, C...
    status          VARCHAR(50) NOT NULL DEFAULT 'draft',
                    -- draft | generating | issued
    
    -- File references
    combined_pdf_url    TEXT,                           -- s3://...package.pdf
    manifest_json       JSONB NOT NULL,                 -- Full package manifest
                        -- {package_id, sheets: [{number, title, type, scale,
                        --   files: {pdf_page, svg, png_preview}}], total_sheets}
    
    -- Sheet details (denormalized for query performance)
    total_sheets    INT NOT NULL DEFAULT 0,
    sheet_types     TEXT[],                             -- ['cover','floor_plan','floor_plan','render']
    
    -- Tracking
    created_by      UUID NOT NULL REFERENCES users(id),
    issued_at       TIMESTAMP WITH TIME ZONE,          -- When status -> issued
    created_at      TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_packages_version ON export_packages(version_id);
CREATE INDEX idx_packages_project ON export_packages(project_id);
```

---

## 3. Migration Plan

### Migration Order (Alembic)

```
001_create_organizations.py
002_create_users.py
003_create_style_profiles.py
004_create_projects.py
005_create_design_versions.py
006_create_annotations.py
007_create_feedback.py
008_create_chat_messages.py
009_create_share_links.py
010_create_handoff_bundles.py
011_create_notifications.py
012_create_audit_logs.py
013_create_style_data_logs.py
014_create_generation_jobs.py
015_create_export_packages.py
```

### Rules

1. **Moi migration co up() va down()** - Rollback phai hoat dong
2. **KHONG dung auto-generate** cho production migrations
3. **Test migration tren staging truoc** khi chay tren production
4. **Data migration tach rieng** khoi schema migration
5. **KHONG drop column** trong migration. Dung soft deprecation (rename + nullable).

---

## 4. Indexes Strategy

### Read-heavy queries (need indexes)
- Projects by organization + status (dashboard)
- Versions by project + status (project detail)
- Annotations by version (review workspace)
- Notifications by user + unread (notification bell)
- Audit logs by project (audit trail)

### Write-heavy tables (minimal indexes)
- chat_messages (only project_id + created_at)
- style_data_logs (only kts_id + created_at)
- generation_jobs (only project_id + status)

---

## 5. JSONB Schemas

### brief_json
```json
{
  "lot": {
    "width_m": 5,
    "depth_m": 20,
    "orientation": "south",
    "area_m2": 100
  },
  "floors": 4,
  "rooms": [
    { "type": "living", "floor": 1, "min_area_m2": 20 },
    { "type": "kitchen", "floor": 1, "min_area_m2": 12 }
  ],
  "style": "modern_minimalist",
  "budget_vnd": 2500000000,
  "special_requests": ["gara o tang 1"],
  "lifestyle": "gia dinh 4 nguoi, lam viec tai nha"
}
```

### geometry_json (Phase 1 - basic)
```json
{
  "rooms": [
    { "name": "Phong khach", "type": "living", "area_m2": 24, "floor": 1 },
    { "name": "Bep", "type": "kitchen", "area_m2": 12, "floor": 1 }
  ],
  "total_area_m2": 320,
  "floors": 4,
  "dimensions": { "width_m": 5, "depth_m": 20 },
  "building_coverage": 0.8
}
```

### generation_metadata
```json
{
  "model_id": "sdxl-base-1.0",
  "workflow_version": "v1.2",
  "prompt": "architectural floor plan, modern style, 5m x 20m lot...",
  "negative_prompt": "blurry, low quality...",
  "seed": 42,
  "controlnet_model": "sdxl-controlnet-canny",
  "controlnet_strength": 0.7,
  "resolution": 2048,
  "steps": 30,
  "cfg_scale": 7.5,
  "duration_seconds": 45,
  "recovery_level": 0,
  "gpu_id": "runpod-abc123"
}
```

### files_manifest (handoff_bundles)
```json
[
  { "name": "concept-package.pdf", "url": "s3://...", "size_bytes": 4200000, "type": "pdf" },
  { "name": "renders.zip", "url": "s3://...", "size_bytes": 28000000, "type": "zip" },
  { "name": "floor-plans.svg", "url": "s3://...", "size_bytes": 1100000, "type": "svg" },
  { "name": "brief.json", "url": "s3://...", "size_bytes": 2000, "type": "json" },
  { "name": "audit-log.json", "url": "s3://...", "size_bytes": 5000, "type": "json" }
]
```
