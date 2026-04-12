# 01 - Software Requirements Specification (Final)

*Version: 1.0 FINAL*
*Ngay chot: Apr 11, 2026*

---

## 1. Product Summary

**AI Architect** la nen tang AI-native giup cong ty thiet ke kien truc tao concept design nha o nhanh gap 3x so voi workflow truyen thong.

**Core Loop:**
```
User Input -> AI Generate 2D -> KTS Review -> Client Present -> Feedback -> AI Revise
```

**Target:** B2B (cong ty thiet ke nho 5-10 nguoi) tai Viet Nam.

---

## 2. Actors & Roles

| Actor | Role ID | Quyen |
|-------|---------|-------|
| End-User (Chu nha) | `user` | Tao project, chat intake, xem gallery, feedback |
| Kien Truc Su (KTS) | `architect` | Tat ca cua user + review, annotate, approve/reject, export |
| Admin | `admin` | Tat ca cua architect + quan ly team, style profiles, dashboard |
| Client (Share link) | `client` | Read-only xem design + gui feedback |
| Contractor | `contractor` | Download handoff bundle |

---

## 3. Functional Requirements

### FR-01: Authentication & Authorization

| ID | Requirement | Priority |
|----|------------|----------|
| FR-01.1 | User dang ky bang email + password | P0 |
| FR-01.2 | Login tra ve JWT token (access + refresh) | P0 |
| FR-01.3 | Role-based access control (user/architect/admin) | P0 |
| FR-01.4 | Invite member vao organization | P1 |
| FR-01.5 | Share link tao temporary client access (read-only + feedback) | P0 |

### FR-02: Project Management

| ID | Requirement | Priority |
|----|------------|----------|
| FR-02.1 | Tao project moi voi ten, client info | P0 |
| FR-02.2 | List projects theo organization, filter by status | P0 |
| FR-02.3 | Assign KTS cho project | P0 |
| FR-02.4 | Project dashboard voi stats (total, pending, approved) | P1 |

### FR-03: Intake & Design Brief (M2)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-03.1 | Chat AI thu thap thong tin: kich thuoc dat, budget, style, so phong, lifestyle | P0 |
| FR-03.2 | AI phai hoi lai khi thieu thong tin bat buoc (lot size, so tang, huong) | P0 |
| FR-03.3 | Structured form lam backup cho chat (multi-step wizard) | P0 |
| FR-03.4 | Output: Design Brief JSON co cau truc | P0 |
| FR-03.5 | KTS co the edit Design Brief truoc khi generate | P0 |
| FR-03.6 | Luu conversation history cho reference | P1 |

**Design Brief JSON Schema (bat buoc):**
```json
{
  "lot": { "width_m": 5, "depth_m": 20, "orientation": "south", "area_m2": 100 },
  "floors": 4,
  "rooms": [
    { "type": "living", "floor": 1, "min_area_m2": 20 },
    { "type": "kitchen", "floor": 1, "min_area_m2": 12 },
    { "type": "bedroom", "floor": 2, "count": 2, "min_area_m2": 12 },
    { "type": "bedroom_master", "floor": 3, "min_area_m2": 16 },
    { "type": "bathroom", "count": 3 }
  ],
  "style": "modern_minimalist",
  "budget_vnd": 2500000000,
  "special_requests": ["gara o tang 1", "san thuong co vuon"]
}
```

### FR-04: 2D Floor Plan Generation (M5)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-04.1 | Tu Design Brief, tao 2-3 floor plan options (images) | P0 |
| FR-04.2 | Moi option co ten, mo ta ngan (vd: "Option A - Hien dai toi gian") | P0 |
| FR-04.3 | Floor plan image resolution toi thieu 2048x2048px | P0 |
| FR-04.4 | Hien thi progress realtime qua WebSocket (0-100%) | P0 |
| FR-04.5 | User chon 1 option de tiep tuc | P0 |
| FR-04.6 | Regenerate voi cung brief tao ket qua khac (seed control) | P1 |
| FR-04.7 | Time-to-first-concept < 10 phut | P0 |

### FR-05: Canonical Design State (M4)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-05.1 | Moi design option duoc luu nhu DesignVersion voi unique ID | P0 |
| FR-05.2 | Version state machine: draft -> generated -> under_review -> approved/rejected -> locked -> handoff_ready -> delivered | P0 |
| FR-05.3 | Locked version la immutable (canonical truth) | P0 |
| FR-05.4 | Moi version luu: brief_json, geometry metadata, floor_plan_urls, review_state, lineage (parent_version_id) | P0 |
| FR-05.5 | 3D, export, bundle chi doc tu locked versions | P0 |
| FR-05.6 | Rejected version tao new draft (lineage preserved) | P0 |
| FR-05.7 | Superseded = version cu bi thay the boi version moi | P0 |

**Version State Machine:**
```
[draft] --gen--> [generated] --submit--> [under_review]
                      |                       |
                 [superseded]            +----+--------+
                                         |             |
                                    [approved]    [rejected]
                                         |             |
                                    [locked] <--revise--+
                                         |
                                  [handoff_ready]
                                         |
                                   [delivered]
```

### FR-06: Review & Annotation (M6)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-06.1 | KTS xem floor plan voi pan/zoom | P0 |
| FR-06.2 | KTS dat annotation pin tren floor plan (vi tri x,y + comment) | P0 |
| FR-06.3 | KTS approve, reject (voi ly do bat buoc), hoac request revision | P0 |
| FR-06.4 | Review panel hien brief summary + annotation list | P0 |
| FR-06.5 | Annotation list click -> scroll den vi tri tren floor plan | P1 |
| FR-06.6 | Split layout: floor plan (left) + review panel (right, 360px) | P0 |
| FR-06.7 | Mobile: tab switch giua viewer va panel | P0 |

### FR-07: Client Feedback & Revision (M5+M6)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-07.1 | Tao share link cho client (read-only + feedback) | P0 |
| FR-07.2 | Client xem gallery, 3D renders | P0 |
| FR-07.3 | Client gui feedback bang text | P0 |
| FR-07.4 | KTS nhan notification khi co feedback moi | P0 |
| FR-07.5 | KTS click "AI Revise" -> AI map feedback thanh structured changes -> generate version moi | P0 |
| FR-07.6 | Version moi co lineage tro ve version cu (parent_version_id) | P0 |
| FR-07.7 | Side-by-side compare giua 2 versions (synced zoom) | P1 |
| FR-07.8 | Target: < 3 vong revision de dat client approval | P0 |

### FR-08: 3D Derivation & Visualization (M7)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-08.1 | Tu locked 2D version, tao 3D renders: 1 exterior + 3 interior rooms | P0 |
| FR-08.2 | Render resolution toi thieu 1920x1080 | P0 |
| FR-08.3 | 3D chi derive tu locked version (khong tu draft) | P0 |
| FR-08.4 | Three.js interactive viewer voi GLTF model | P1 |
| FR-08.5 | Viewer controls: orbit, zoom, floor plan view, section view | P1 |
| FR-08.6 | Room info popup khi click vao phong (ten, dien tich) | P1 |

### FR-09: Export & Professional Package (M8)

**Target standard:** Schematic Design Package (see 10-p1-2d-deliverable-integration.md)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-09.1 | Export multi-page PDF package voi sheet structure (khong phai image dump) | P0 |
| FR-09.2 | Moi sheet co title block: project name, sheet title, number, date, revision, scale, preparer | P0 |
| FR-09.3 | Cover sheet (A0): project name, sheet index, date, revision, branding, disclaimer | P0 |
| FR-09.4 | Floor plan sheet(s): floor plan image framed voi room labels overlay tu geometry_json | P0 |
| FR-09.5 | Render sheet: 3D renders voi title block | P0 |
| FR-09.6 | Disclaimer "THIET KE SO BO - KHONG DUNG CHO XIN PHEP XAY DUNG" tren cover | P0 |
| FR-09.7 | Watermark "CONCEPT DESIGN" neu version status != approved | P0 |
| FR-09.8 | Package manifest JSON (package_id, sheets, revision, files) | P0 |
| FR-09.9 | Per-sheet SVG export (floor plan image embedded in sheet frame) | P0 |
| FR-09.10 | Export render images (PNG high-res) | P0 |
| FR-09.11 | Revision labeling nhat quan giua manifest, title block, metadata | P0 |
| FR-09.12 | Site plan sheet (A1): site boundary, building footprint, north arrow, scale | P1 (MVP+) |
| FR-09.13 | Floor plan TRUE VECTOR SVG tu geometry Layer 1.5 | P1 (MVP+) |
| FR-09.14 | Elevation sheet (A4): 2 principal elevations tu structured geometry | P1 (MVP+) |
| FR-09.15 | Section sheet (A5): 1 key section tu structured geometry | P1 (MVP+) |
| FR-09.16 | Wall hierarchy visible: exterior nang hon interior | P1 (MVP+) |
| FR-09.17 | Dimensions: overall building + key room dimensions | P1 (MVP+) |
| FR-09.18 | 4 exterior elevations | P2 (Phase 2) |
| FR-09.19 | DXF export | P2 (Phase 2) |
| FR-09.20 | Door/window schedules | P2 (Phase 2) |

### FR-10: Delivery & Handoff (M9)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-10.1 | Tao handoff bundle (zip) gom: PDF + renders + SVG + brief JSON + approval log | P1 |
| FR-10.2 | Handoff chi tao duoc khi version = locked + KTS approved + exports co du | P1 |
| FR-10.3 | Mark bundle la "current official" (cac bundle cu -> superseded) | P1 |
| FR-10.4 | Contractor workspace de download bundle | P2 |

### FR-11: Style Intelligence (M3)

| ID | Requirement | Priority |
|----|------------|----------|
| FR-11.1 | KTS upload portfolio (images) de tao style profile | P1 (MVP+) |
| FR-11.2 | AI extract style patterns: facade, materials, spatial, proportions | P1 (MVP+) |
| FR-11.3 | KTS review va correct style profile | P1 (MVP+) |
| FR-11.4 | Generation su dung style profile nhu soft constraint | P1 (MVP+) |
| FR-11.5 | Log approve/reject/reference data de hoc style theo thoi gian | P0 (data hooks) |

### FR-12: Notifications

| ID | Requirement | Priority |
|----|------------|----------|
| FR-12.1 | In-app notification khi: generation done, feedback moi, review request | P0 |
| FR-12.2 | WebSocket realtime push | P0 |
| FR-12.3 | Notification bell voi unread count | P1 |
| FR-12.4 | Email notification | P2 |

---

## 4. Non-Functional Requirements

### NFR-01: Performance

| ID | Requirement | Target |
|----|------------|--------|
| NFR-01.1 | Time-to-first-concept (tu intake hoan tat den 2D options) | < 10 phut |
| NFR-01.2 | API response time (non-generation) | < 500ms p95 |
| NFR-01.3 | WebSocket message delivery | < 200ms |
| NFR-01.4 | Page load (LCP) | < 2.5s |
| NFR-01.5 | First Input Delay (FID) | < 100ms |
| NFR-01.6 | Cumulative Layout Shift (CLS) | < 0.1 |
| NFR-01.7 | 3D model initial load | < 5s cho model < 50MB |
| NFR-01.8 | PDF export time | < 30s |

### NFR-02: Scalability

| ID | Requirement | Target |
|----|------------|--------|
| NFR-02.1 | Concurrent users | 50 (Phase 1) |
| NFR-02.2 | Concurrent generation jobs | 5 (theo GPU capacity) |
| NFR-02.3 | Projects per organization | 100+ |
| NFR-02.4 | Versions per project | 20+ |

### NFR-03: Security

| ID | Requirement |
|----|------------|
| NFR-03.1 | JWT authentication voi access token (15min) + refresh token (7d) |
| NFR-03.2 | Password hashing voi bcrypt |
| NFR-03.3 | Role-based access control enforced o API layer |
| NFR-03.4 | Share links co expiry (default 30 ngay) |
| NFR-03.5 | File uploads validated: type, size (max 50MB/file) |
| NFR-03.6 | SQL injection prevention (SQLAlchemy parameterized queries) |
| NFR-03.7 | XSS prevention (React auto-escape + Content-Security-Policy) |
| NFR-03.8 | CORS restricted to known origins |

### NFR-04: Reliability

| ID | Requirement |
|----|------------|
| NFR-04.1 | Generation failure: escalating recovery 5 levels (retry -> reduce params -> switch model -> switch pipeline -> surface error) |
| NFR-04.2 | API uptime target: 99.5% |
| NFR-04.3 | Data backup: daily PostgreSQL backup |
| NFR-04.4 | File storage: S3-compatible voi redundancy |

### NFR-05: Observability

| ID | Requirement |
|----|------------|
| NFR-05.1 | Structured logging (JSON) cho moi service |
| NFR-05.2 | Request tracing (correlation ID across services) |
| NFR-05.3 | Generation job logging: model, workflow, prompt, seed, version, duration |
| NFR-05.4 | Error alerting cho generation failures va API 5xx |

### NFR-06: Reproducibility

| ID | Requirement |
|----|------------|
| NFR-06.1 | Moi generation job luu: model_id, workflow_version, prompt, seed, controlnet_params |
| NFR-06.2 | Co the re-run generation voi cung params va nhan ket qua tuong tu |
| NFR-06.3 | Audit trail cho moi state transition (who, when, what, why) |

---

## 5. Constraints

| Constraint | Detail |
|-----------|--------|
| Language | Vietnamese UI, English code/API |
| License | ComfyUI (GPL-3.0) phai chay nhu isolated service |
| GPU | Minimum 12GB VRAM (RTX 3060), recommended 24GB (RTX 4090/A5000) |
| Browser | Chrome 90+, Firefox 88+, Safari 15+, Edge 90+ |
| Mobile | Responsive web (khong native app) |
| Budget | Cloud GPU: RunPod/vast.ai cho generation |

---

## 6. Out of Scope (Phase 1)

- Ban ve thi cong (construction documents)
- Tinh toan ket cau, MEP
- Quan ly thi cong
- Marketplace nha thau/vat lieu
- IFC/BIM export day du
- Mobile native app
- Tu dong kiem tra quy chuan xay dung QCVN
- Dark mode
- Multi-language (chi Vietnamese)
- Full DXF export (Phase 2)
- Full Style Intelligence stack (Phase 2, chi data hooks o Phase 1)
