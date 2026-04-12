# 06 - API Contracts

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*
*Base URL: `/api/v1`*

---

## 1. Common Patterns

### Authentication Header
```
Authorization: Bearer <access_token>
```

### Pagination
```
GET /resource?page=1&per_page=20

Response:
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 45,
    "total_pages": 3
  }
}
```

### Error Format
```json
{
  "code": "VALIDATION_ERROR",
  "message": "Human-readable message in Vietnamese",
  "details": [
    {"field": "lot.width_m", "error": "Phai la so duong"}
  ]
}
```

### Error Codes
| HTTP | Code | Meaning |
|------|------|---------|
| 400 | VALIDATION_ERROR | Request body invalid |
| 401 | UNAUTHORIZED | Missing or invalid token |
| 403 | FORBIDDEN | Insufficient permissions |
| 404 | NOT_FOUND | Resource does not exist |
| 409 | CONFLICT | Invalid state transition |
| 413 | PAYLOAD_TOO_LARGE | File too large |
| 429 | RATE_LIMITED | Too many requests |
| 500 | INTERNAL_ERROR | Server error |
| 503 | GPU_UNAVAILABLE | GPU service down |

---

## 2. Auth Endpoints

### POST /auth/register
```
Request:
{
  "email": "kts@company.vn",
  "password": "securepass123",
  "full_name": "Nguyen Van A",
  "organization_name": "Studio A"    // Tao org moi
}

Response 201:
{
  "user": {
    "id": "uuid",
    "email": "kts@company.vn",
    "full_name": "Nguyen Van A",
    "role": "architect",
    "organization_id": "uuid"
  },
  "access_token": "jwt...",
  "refresh_token": "jwt..."         // Also set as HttpOnly cookie
}
```

### POST /auth/login
```
Request:
{
  "email": "kts@company.vn",
  "password": "securepass123"
}

Response 200:
{
  "user": { ... },
  "access_token": "jwt...",
  "refresh_token": "jwt..."
}
```

### POST /auth/refresh
```
Request:
{
  "refresh_token": "jwt..."        // Or from HttpOnly cookie
}

Response 200:
{
  "access_token": "jwt..."
}
```

---

## 3. Project Endpoints

### GET /projects
```
Query: ?page=1&per_page=20&status=draft&search=keyword

Response 200:
{
  "data": [
    {
      "id": "uuid",
      "name": "Nha pho Tan Binh",
      "client_name": "Anh Minh",
      "status": "in_progress",
      "current_version_number": 2,
      "current_version_status": "under_review",
      "kts_user_id": "uuid",
      "kts_name": "KTS Nguyen",
      "thumbnail_url": "https://s3.../thumb.jpg",
      "created_at": "2026-04-11T10:00:00Z",
      "updated_at": "2026-04-11T14:30:00Z"
    }
  ],
  "pagination": { ... }
}
```

### POST /projects
```
Request:
{
  "name": "Nha pho Tan Binh",
  "client_name": "Anh Minh",
  "client_phone": "0901234567",
  "kts_user_id": "uuid"           // Optional, assign later
}

Response 201:
{
  "id": "uuid",
  "name": "Nha pho Tan Binh",
  ...
}
```

### GET /projects/{project_id}
```
Response 200:
{
  "id": "uuid",
  "name": "Nha pho Tan Binh",
  "client_name": "Anh Minh",
  "status": "in_progress",
  "brief": { ... },                // DesignBrief JSON or null
  "versions": [
    {
      "id": "uuid",
      "version_number": 1,
      "status": "superseded",
      "thumbnail_url": "...",
      "created_at": "..."
    },
    {
      "id": "uuid",
      "version_number": 2,
      "status": "under_review",
      "thumbnail_url": "...",
      "created_at": "..."
    }
  ],
  "kts": { "id": "uuid", "name": "KTS Nguyen", "avatar_url": "..." },
  "created_at": "...",
  "updated_at": "..."
}
```

---

## 4. Design Brief Endpoints

### GET /projects/{project_id}/brief
```
Response 200:
{
  "id": "uuid",
  "project_id": "uuid",
  "status": "confirmed",           // draft | confirmed
  "brief_json": {
    "lot": { "width_m": 5, "depth_m": 20, "orientation": "south", "area_m2": 100 },
    "floors": 4,
    "rooms": [ ... ],
    "style": "modern_minimalist",
    "budget_vnd": 2500000000,
    "special_requests": ["gara o tang 1"]
  },
  "created_at": "...",
  "updated_at": "..."
}
```

### PUT /projects/{project_id}/brief
```
Request:
{
  "brief_json": { ... },
  "status": "confirmed"
}

Response 200:
{
  "id": "uuid",
  "brief_json": { ... },
  "status": "confirmed"
}
```

---

## 5. Chat Endpoints

### POST /projects/{project_id}/chat
```
Request:
{
  "message": "Toi muon xay nha 5x20m, 4 tang"
}

Response 200 (streaming via WebSocket, not REST):
// REST response just acknowledges
{
  "session_id": "uuid",
  "status": "processing"
}

// Actual response comes via WebSocket:
// event: "chat:chunk" -> { "content": "Xin chao!...", "done": false }
// event: "chat:chunk" -> { "content": " Cho toi biet...", "done": false }
// event: "chat:done"  -> { "brief_updated": true, "needs_follow_up": true }
```

### GET /projects/{project_id}/chat/history
```
Response 200:
{
  "messages": [
    { "role": "user", "content": "Toi muon xay nha...", "timestamp": "..." },
    { "role": "ai", "content": "Xin chao! Cho toi...", "timestamp": "..." },
    { "role": "user", "content": "Huong Nam", "timestamp": "..." },
    { "role": "ai", "content": "Brief hoan tat...", "timestamp": "...",
      "metadata": { "brief_confirmed": true } }
  ]
}
```

---

## 6. Generation Endpoints

### POST /projects/{project_id}/generate
```
Request:
{
  "num_options": 3,
  "config": {                     // Optional overrides
    "resolution": 2048,
    "seed": null                  // null = random
  }
}

Response 202:
{
  "job_id": "uuid",
  "status": "queued",
  "estimated_seconds": 120
}

// Progress via WebSocket:
// event: "generation:progress" -> { "job_id": "uuid", "progress": 30, "stage": "Dang tao mat bang tang 1..." }
// event: "generation:progress" -> { "job_id": "uuid", "progress": 70, "stage": "Dang tao mat bang tang 2..." }
// event: "generation:complete" -> { "job_id": "uuid", "version_ids": ["uuid1", "uuid2", "uuid3"] }
// event: "generation:failed"   -> { "job_id": "uuid", "error": "...", "recovery_level": 3 }
```

### GET /projects/{project_id}/generation/{job_id}
```
Response 200:
{
  "job_id": "uuid",
  "status": "completed",          // queued | processing | completed | failed
  "progress": 100,
  "versions": [
    {
      "id": "uuid",
      "option_label": "Option A",
      "option_description": "Hien dai toi gian",
      "floor_plan_urls": ["s3://...floor1.png", "s3://...floor2.png"],
      "thumbnail_url": "s3://...thumb.png"
    },
    ...
  ],
  "generation_metadata": {
    "model_id": "sdxl-base-1.0",
    "workflow_version": "v1.2",
    "seed": 42,
    "duration_seconds": 95
  }
}
```

---

## 7. Version Endpoints

### GET /versions/{version_id}
```
Response 200:
{
  "id": "uuid",
  "project_id": "uuid",
  "version_number": 2,
  "parent_version_id": "uuid",    // null if first version
  "status": "under_review",
  "option_label": "Option A",
  "option_description": "Hien dai toi gian",
  "brief_json": { ... },
  "geometry_json": { ... },       // Basic metadata
  "floor_plan_urls": ["s3://..."],
  "render_urls": ["s3://...exterior.png", "s3://...interior1.png"],
  "model_url": "s3://...model.gltf",
  "export_urls": { "pdf": "s3://...", "svg": "s3://..." },
  "reviewed_by": "uuid",
  "reviewed_at": "...",
  "generation_metadata": { ... },
  "created_at": "...",
  "locked_at": null
}
```

### POST /versions/{version_id}/select
```
// User selects this option for review
Response 200:
{
  "id": "uuid",
  "status": "under_review"        // Transition: generated -> under_review
}
```

### POST /versions/{version_id}/revise
```
// KTS triggers AI revision based on feedback
Request:
{
  "feedback_text": "Phong khach rong hon, bot 1 PN tang 2",
  "feedback_id": "uuid"           // Reference to stored feedback
}

Response 202:
{
  "job_id": "uuid",
  "new_version_id": "uuid",       // V3, parent=V2
  "status": "queued"
}
```

### GET /versions/compare?v1={id1}&v2={id2}
```
Response 200:
{
  "version_1": { ... },
  "version_2": { ... },
  "diff": {
    "rooms_changed": [
      { "room": "living", "change": "area 12m2 -> 16m2" },
      { "room": "bedroom_floor2", "change": "count 3 -> 2" }
    ],
    "brief_changes": { ... }
  }
}
```

---

## 7b. 3D Derivation Endpoints

### POST /versions/{version_id}/derive-3d
```
// Trigger 3D model + renders from a LOCKED canonical version
// Aligns with UC-03 in system design (POST /3d/{ver_id})

Request:
{
  "render_rooms": ["living", "kitchen", "master_bedroom"],  // Which rooms to render interior
  "config": {
    "exterior": true,
    "model_format": "gltf"
  }
}

Response 202:
{
  "job_id": "uuid",
  "status": "queued",
  "estimated_seconds": 180
}

Error 409 (version not locked):
{
  "code": "VERSION_NOT_LOCKED",
  "message": "3D derivation chi chay tu locked version"
}

// Progress via WebSocket:
// event: "derivation:progress" -> { "job_id": "uuid", "progress": 30, "stage": "Dang dung mo hinh 3D..." }
// event: "derivation:progress" -> { "job_id": "uuid", "progress": 60, "stage": "Dang render exterior..." }
// event: "derivation:progress" -> { "job_id": "uuid", "progress": 85, "stage": "Dang render noi that..." }
// event: "derivation:complete" -> { "job_id": "uuid", "model_url": "s3://...", "render_urls": [...] }
```

### GET /versions/{version_id}/3d
```
// Get 3D assets for a version
Response 200:
{
  "model_url": "s3://...model.gltf",
  "render_urls": {
    "exterior": "s3://...exterior.png",
    "interiors": [
      { "room": "living", "url": "s3://...living.png" },
      { "room": "kitchen", "url": "s3://...kitchen.png" },
      { "room": "master_bedroom", "url": "s3://...master.png" }
    ]
  },
  "generation_metadata": {
    "model_id": "blender-4.0",
    "render_engine": "controlnet-sdxl",
    "duration_seconds": 120
  }
}

Error 404 (no 3D assets yet):
{
  "code": "NO_3D_ASSETS",
  "message": "Version nay chua co 3D. Goi POST /derive-3d truoc."
}
```

---

## 8. Review Endpoints

### GET /reviews
```
Query: ?status=pending&page=1

Response 200:
{
  "data": [
    {
      "version_id": "uuid",
      "project_name": "Nha pho Tan Binh",
      "version_number": 2,
      "status": "under_review",
      "submitted_at": "...",
      "thumbnail_url": "..."
    }
  ]
}
```

### POST /reviews/{version_id}/approve
```
Request:
{
  "comment": "Phuong an tot, chot."    // Optional
}

Response 200:
{
  "version_id": "uuid",
  "status": "locked",
  "approved_at": "...",
  "approved_by": "uuid"
}
```

### POST /reviews/{version_id}/reject
```
Request:
{
  "reason": "Cua so huong Tay qua nong, phong ngu nho"   // REQUIRED
}

Response 200:
{
  "version_id": "uuid",
  "status": "rejected",
  "rejected_at": "...",
  "reason": "..."
}
```

---

## 9. Annotation Endpoints

### GET /versions/{version_id}/annotations
```
Response 200:
{
  "data": [
    {
      "id": "uuid",
      "version_id": "uuid",
      "user_id": "uuid",
      "user_name": "KTS Nguyen",
      "x": 0.45,                   // Normalized 0-1
      "y": 0.32,
      "comment": "Cua so o day bi huong Tay",
      "created_at": "..."
    }
  ]
}
```

### POST /versions/{version_id}/annotations
```
Request:
{
  "x": 0.45,
  "y": 0.32,
  "comment": "Cua so o day bi huong Tay"
}

Response 201:
{
  "id": "uuid",
  ...
}
```

---

## 10. Feedback Endpoints

### POST /versions/{version_id}/feedback
```
// Client or user submits feedback
Request:
{
  "content": "Muon phong khach rong hon, bot 1 phong ngu tang 2"
}

Response 201:
{
  "id": "uuid",
  "version_id": "uuid",
  "user_id": "uuid",
  "content": "...",
  "created_at": "..."
}
```

---

## 11. Export & Package Endpoints

### POST /versions/{version_id}/export-package
```
// Generate a professional sheet package (PDF + SVG + manifest)
// Aligned with P1 2D Deliverable standard (see 10-p1-2d-deliverable-integration.md)

Request:
{
  "revision_label": "A",           // A, B, C...
  "options": {
    "include_brief": true,
    "include_renders": true,
    "quality": "high"              // high | standard
  }
}

Response 202:
{
  "package_id": "uuid",
  "job_id": "uuid",
  "status": "generating",
  "estimated_sheets": 4
}

// Progress via WebSocket:
// event: "export:progress" -> { "job_id": "uuid", "progress": 50, "stage": "Generating floor plan sheet..." }
// event: "export:complete" -> { "job_id": "uuid", "package_id": "uuid" }
```

### GET /versions/{version_id}/packages
```
// List all export packages for a version
Response 200:
{
  "packages": [
    {
      "id": "uuid",
      "revision_label": "A",
      "status": "issued",
      "total_sheets": 4,
      "sheet_types": ["cover", "floor_plan", "floor_plan", "render"],
      "combined_pdf_url": "s3://...package.pdf",
      "manifest_json": {
        "package_id": "uuid",
        "issue_date": "2026-04-12",
        "issue_type": "schematic-design-package",
        "revision_label": "A",
        "sheets": [
          {
            "number": "A0",
            "title": "Cover / Issue Sheet",
            "type": "cover",
            "scale": null,
            "files": { "pdf_page": 1, "svg": "s3://...A0.svg", "png_preview": "s3://...A0.png" }
          },
          {
            "number": "A2",
            "title": "Floor Plan - Tang 1",
            "type": "floor_plan",
            "scale": "1:100",
            "files": { "pdf_page": 2, "svg": "s3://...A2.svg", "png_preview": "s3://...A2.png" }
          }
        ],
        "total_sheets": 4
      },
      "issued_at": "2026-04-12T10:30:00Z",
      "created_at": "..."
    }
  ]
}
```

### GET /packages/{package_id}/sheet/{sheet_number}
```
// Get a specific sheet SVG for web display
Response 200 (Content-Type: image/svg+xml):
// Raw SVG content for crisp web rendering

// Or with ?format=png for fallback:
Response 200 (Content-Type: image/png):
// PNG preview of the sheet
```

### POST /exports/{version_id} (Legacy - individual exports)
```
// For individual file exports (images, single SVG)
Request:
{
  "format": "images",             // images | svg_single
  "options": {
    "quality": "high"
  }
}

Response 202:
{
  "job_id": "uuid",
  "status": "processing"
}
```

---

## 12. Share Link Endpoints

### POST /projects/{project_id}/share
```
Request:
{
  "expires_days": 30
}

Response 201:
{
  "token": "abc123def456",
  "url": "https://app.aiarchitect.vn/share/abc123def456",
  "expires_at": "2026-05-11T10:00:00Z"
}
```

### GET /share/{token}
```
// Public endpoint, no auth required
Response 200:
{
  "project_name": "Nha pho Tan Binh",
  "versions": [
    {
      "id": "uuid",
      "version_number": 2,
      "status": "under_review",
      "floor_plan_urls": ["..."],
      "render_urls": ["..."]
    }
  ],
  "can_feedback": true
}
```

---

## 13. Notification Endpoints

### GET /notifications
```
Query: ?unread_only=true&page=1

Response 200:
{
  "data": [
    {
      "id": "uuid",
      "type": "feedback_received",
      "message": "Anh Minh da gui feedback cho Project Tan Binh",
      "project_id": "uuid",
      "read": false,
      "created_at": "..."
    }
  ],
  "unread_count": 3
}
```

### POST /notifications/{id}/read
```
Response 200: { "id": "uuid", "read": true }
```

---

## 14. Handoff Endpoints

### POST /handoff/{version_id}
```
// Aligned with 05-system-design.md UC-06: POST /handoff/{ver}
// Version-centric: handoff is tied to a specific locked version, not project-level

Request:
{
  // No body needed - version_id in path is sufficient
  // Readiness checked server-side
}

Response 201:
{
  "bundle_id": "uuid",
  "version_id": "uuid",
  "files": [
    { "name": "concept-package.pdf", "url": "s3://...", "size_bytes": 4200000 },
    { "name": "renders.zip", "url": "s3://...", "size_bytes": 28000000 },
    { "name": "floor-plans-svg.zip", "url": "s3://...", "size_bytes": 1100000 },
    { "name": "brief.json", "url": "s3://...", "size_bytes": 2000 }
  ],
  "is_current": true,
  "created_at": "..."
}

Error 409 (if readiness check fails):
{
  "code": "HANDOFF_NOT_READY",
  "message": "Version chua du dieu kien handoff",
  "details": [
    { "check": "version_locked", "passed": true },
    { "check": "kts_approved", "passed": true },
    { "check": "pdf_exported", "passed": false },
    { "check": "renders_exist", "passed": true }
  ]
}
```

---

## 15. WebSocket Events

### Client -> Server
| Event | Payload | Description |
|-------|---------|-------------|
| `chat:message` | `{ project_id, message }` | User sends chat message |
| `join:project` | `{ project_id }` | Join project room for updates |
| `leave:project` | `{ project_id }` | Leave project room |

### Server -> Client
| Event | Payload | Description |
|-------|---------|-------------|
| `chat:chunk` | `{ content, done }` | LLM streaming response chunk |
| `chat:done` | `{ brief_updated, needs_follow_up }` | Chat turn complete |
| `generation:progress` | `{ job_id, progress, stage }` | Generation progress 0-100% |
| `generation:complete` | `{ job_id, version_ids }` | Generation done |
| `generation:failed` | `{ job_id, error, recovery_level }` | Generation failed |
| `export:complete` | `{ job_id, download_url }` | Export ready |
| `derivation:progress` | `{ job_id, progress, stage }` | 3D derivation progress 0-100% |
| `derivation:complete` | `{ job_id, model_url, render_urls }` | 3D derivation done |
| `notification` | `{ id, type, message, project_id }` | New notification |
| `annotation:added` | `{ annotation }` | Live annotation update |
