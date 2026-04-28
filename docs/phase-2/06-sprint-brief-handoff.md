---
title: Sprint Brief — Handoff to Dev/Test Agent
phase: 2
status: ready-to-execute
date: 2026-04-27
revision: 2026-04-27 — local-first git and verification protocol added
audience: dev/test agent (executed by separate agent in different session)
bridged_via: Product Owner (evo-pm-vn@trustingsocial.com)
related:
  - docs/phase-2/01-discovery-summary.md
  - docs/phase-2/02-market-standards-research.md
  - docs/phase-2/03-adr-001-standards-combo.md
  - docs/phase-2/04-deferred-roadmap.md
  - docs/phase-2/05-prd-deliverables.md
  - docs/phase-2/07-local-git-verification-protocol.md
---

# Sprint Brief — Professional Deliverables Track

> **Đọc file này từ trên xuống. Tất cả input cần để start có ở đây hoặc link tới file canonical.**

> **Operational update — 2026-04-27:** Phase 2 now uses the local-first workflow in [`07-local-git-verification-protocol.md`](07-local-git-verification-protocol.md). GitHub Actions and PR comments are optional transport, not mandatory acceptance requirements. Required gates still must pass before a bundle is deliverable.

## 0. Mission Statement

Implement professional-grade deliverable bundle (2D drawings + 3D models + cinematic videos + manifest) cho mỗi project AI Architect tạo ra. Đầu ra phải đạt chuẩn thị trường theo ADR-001 và pass acceptance criteria trong PRD-05.

## 1. Background — Đọc trước khi bắt đầu

**Mandatory reading order:**

1. [`01-discovery-summary.md`](01-discovery-summary.md) — Hiểu vì sao và cho ai
2. [`03-adr-001-standards-combo.md`](03-adr-001-standards-combo.md) — Standards đã chốt (BLOCKING — không tự ý đổi)
3. [`05-prd-deliverables.md`](05-prd-deliverables.md) — Functional + acceptance criteria chi tiết
4. [`07-local-git-verification-protocol.md`](07-local-git-verification-protocol.md) — Local git + local-equivalent verification protocol
5. [`02-market-standards-research.md`](02-market-standards-research.md) — Spec gốc nếu cần tra cứu (link Khronos, AIA, Apple…)
6. [`04-deferred-roadmap.md`](04-deferred-roadmap.md) — KHÔNG implement những item ở đây (DEF-001 thru DEF-006)

## 2. What's Already Built (Phase 1 baseline — không build lại)

- ✅ FastAPI backend (`ai-architect-api/`) — agent orchestration, business logic
- ✅ GPU service (`ai-architect-gpu/`) — Diffusers/ControlNet/ComfyUI/Blender headless, endpoints `/generate/floor-plan`, `/derive/model`
- ✅ Next.js frontend (`ai-architect-web/`) — Three.js + ThatOpen Components viewer
- ✅ Phase 1 MVP outputs: PNG floor plan, GLB web preview, PDF concept package

**Build ON TOP của những thứ trên — không thay thế.**

## 3. Deliverables ngoài Phase 1 cần build

### Tier 1 (Sprint 1-2) — 2D Engineering-Grade

- [ ] **DWG/DXF exporter** với hardcoded AIA layer dictionary (~25 layers, see PRD Appendix A)
  - Library suggest: `ezdxf` (Python) cho DXF; convert DXF → DWG via ODA File Converter (free)
  - Tests: layer names match AIA exactly; line weights correct; opens in AutoCAD 2024 + LibreCAD
- [ ] **PDF generator** với NCS-style title block template
  - Suggest: ReportLab + matplotlib hoặc Cairo. VN font embedded (Roboto / Be Vietnam Pro)
  - Tests: VN accents render correctly (test "Phòng khách", "Kích thước", "Bản vẽ")
- [ ] **Sheet set assembly:** A-100 site, A-101 floor plan (1 per floor), A-201 elevations (4 mặt), A-301 sections (1-2)

### Tier 2 (Sprint 2-3) — 3D Multi-Format

- [ ] **glTF 2.0 exporter** (Metal-Rough only, Draco mesh + KTX2 textures)
  - Pipeline: Blender headless → glTF Blender Exporter → KTX2 conversion via `toktx` (KTX-Software)
  - Verification gate: `gltf-validator` returns 0 errors
- [ ] **FBX exporter** với Twinmotion preset profile
  - Settings: cm units, Y→Z axis convert, embed media, triangulate optional, smoothing groups exported
  - Verification gate: scripted FBX import test trong Blender (validate transform matrix, material count, texture references)
- [ ] **USDZ converter** glTF → USDZ
  - Tool suggest: Apple's `usdpython` toolkit OR `usd_from_gltf` (Google) OR Reality Converter (macOS)
  - Budget enforcement: ≤8 MB, ≤200k tris, ≤2K textures (auto-decimate + downsample if exceed)
- [ ] **BIMForum LOD tagging** trong scene graph metadata → emit vào manifest.json
- [ ] **PBR material pipeline** Metal-Rough only — 2K base, 4K hero variants, 1K mobile
  - Curate ~50 starter material Modern Minimalist + Tropical VN (Plan A per OQ4)
  - Source: Quixel Megascans free tier + Polyhaven (CC0)
  - Storage: KTX2 BasisU compressed

### Tier 3 (Sprint 3-4) — Video Cinematic

- [ ] **Twinmotion render pipeline** (preferred) HOẶC Lumion render pipeline
  - Headless render via Twinmotion API (UE5 Movie Render Queue) hoặc Lumion command-line
  - Master config: 3840×2160, 30fps, H.264 MP4, ACES color
- [ ] **Master walkthrough generator** — 60s narrative arc:
  - 0:00-0:15 exterior approach (drone-style camera path)
  - 0:15-0:50 interior walkthrough (≥3 key rooms)
  - 0:50-1:00 exterior closing
- [ ] **Reel auto-derivation** từ master — 20-30s, 1080×1920, safe-area crop (NO re-render)
  - Tool: `ffmpeg` với crop filter + bitrate 10-15 Mbps target
- [ ] **Derivative extraction:**
  - Hero still 4K — frame extraction 0:08-0:12 range
  - Preview GIF — 6-10s segment, ≤5 MB

### Tier 4 (Sprint 4) — Manifest + Bundle

- [ ] **Manifest schema** (PRD Appendix B) — implement JSON Schema validator gate
- [ ] **Bundle assembler** — package toàn bộ artifacts vào folder structure đúng (xem PRD Output Structure)
- [ ] **Naming convention** ISO 19650-inspired: `<Project>-AIA-<Type>-<Number>`
- [ ] **Bundle smoke test** — zip → unzip → all paths resolve → all files open

## 4. Pipeline Mode (CRITICAL)

**Async-first.** Implement như sau:

```
User submit project
    ↓
API enqueues job (Celery/RQ/BullMQ) → returns job_id
    ↓
Worker picks up → orchestrates pipeline:
    ├─ Stage 1: Generate scene graph + LOD tagging
    ├─ Stage 2: 2D exports (DWG/PDF) — parallel
    ├─ Stage 3: 3D exports (GLB/FBX/USDZ) — sequential (FBX → USDZ depends on GLB)
    ├─ Stage 4: Video render (15-30 min on GPU)
    ├─ Stage 5: Derivatives extraction
    ├─ Stage 6: Manifest + checksum
    └─ Stage 7: Bundle assembly + S3 upload
    ↓
Notify user (email/webhook) with signed URL
```

Per-stage retry max 3. On final failure → user notified with stage + reason. **Bundle KHÔNG được deliver nếu ANY required artifact fail required verification gate.**

## 5. Verification Gates / Test Strategy

**Mọi local implementation branch / sprint handoff phải pass tất cả required gates dưới đây trước khi được claim complete.**

As of 2026-04-27, gate execution follows [`07-local-git-verification-protocol.md`](07-local-git-verification-protocol.md):

- Local git branch + local commits are the default workflow.
- GitHub Actions / GitLab CI may be used if free and explicitly requested, but are not mandatory.
- For Linux-specific gates previously assigned to `ubuntu-latest`, use a local Linux-equivalent runner (Docker/VM/WSL/Ubuntu host) when feasible.
- Gate evidence is the generated JSON/Markdown gate summary plus exact command logs in the sprint report.
- PR comments are optional; sprint reports are the required review artifact.

| Gate | Tool | Pass criteria |
|---|---|---|
| glTF Validator | `gltf-validator` (Khronos) | 0 errors |
| DWG opens in AutoCAD | LibreCAD or ODA Viewer headless | No "drawing recovery" prompt |
| FBX import test | Blender headless script | All meshes + materials present |
| USDZ size budget | `du` + `pixar-usd` tools | ≤8 MB, ≤200k tris |
| Video format check | `ffprobe` | Resolution + fps + codec exact match |
| Manifest schema | `ajv` (JSON Schema) | Validates clean |
| Bundle integrity | sha256 verify | All checksums match |
| VN font render | PDF text extraction + diacritic check | "ô, ư, đ, ấ" present, no `?` |

Required gates must run in the active verification environment. A skipped gate is acceptable for local smoke runs only; final sprint acceptance must show pass, blocked, or explicit out-of-scope reason per the local protocol.

## 6. Acceptance Test — End-to-End Smoke

Tạo 1 reference project (small townhouse 5×15m, 2 storey, Tropical VN style) làm **golden test fixture**. Bundle output này phải pass **ALL** Definition of Done items trong PRD § "Definition of Done".

Manual review checkpoint:
1. PO opens DWG trong AutoCAD → confirms layers + dimensions
2. PO opens FBX trong Twinmotion (or screenshot) → confirms scale + materials
3. PO views master video → confirms narrative arc (exterior → interior → exterior)
4. PO opens USDZ on iPhone → confirms AR scale 1:1
5. PO uploads reel to TikTok/Reels test account → confirms accepted

## 7. Sprint Breakdown (suggested)

| Sprint | Goal | Output |
|---|---|---|
| **Sprint 1** (2 weeks) | 2D pipeline foundation | DWG exporter w/ AIA layers + PDF generator w/ VN title block |
| **Sprint 2** (2 weeks) | 3D core formats | GLB + FBX exporters + Khronos validator CI |
| **Sprint 3** (2 weeks) | 3D AR + Video pipeline | USDZ converter + Twinmotion master render |
| **Sprint 4** (2 weeks) | Derivatives + Manifest + E2E | Reel derivation + Hero still + GIF + Manifest schema + golden fixture passing |

**Total: ~8 weeks** to production-ready bundle pipeline.

## 8. Risks + Mitigation

| Risk | Mitigation |
|---|---|
| Twinmotion headless render unstable | Fallback to Lumion CLI; OR pre-bake camera paths in Blender + render via Cycles → composite to video |
| FBX import inconsistent across DCC tools | Provide 2 FBX presets (`twinmotion`, `sketchup-import`); test matrix in CI |
| USDZ budget fails for complex models | Auto-decimation pipeline (Open3D / MeshOptimizer); deliver `model_lite.usdz` if `model_full.usdz` exceeds budget |
| AIA layer set incomplete for some VN building types | Beta with 2-3 VN KTS firms before GA; expand dictionary based on feedback |
| GPU costs spike at scale | Spot instances on RunPod; cache materials/textures aggressively; lazy-render videos only on-demand |
| VN font rendering broken trong PDF | Pre-validate font subsets; whitelist tested fonts (Be Vietnam Pro, Roboto, Inter) |

## 9. Out of Scope (MUST NOT BUILD — see Deferred Roadmap)

- ❌ IFC export (DEF-002)
- ❌ Pascal Editor integration (DEF-001)
- ❌ ISO 19650 full process compliance (DEF-003) — chỉ adopt naming convention inspired
- ❌ TCVN/QCVN code compliance check (DEF-004)
- ❌ Spec-Glossiness PBR (DEF-005 — REJECTED permanently)
- ❌ AI procedural material generation (DEF-006 — via ROOM project)
- ❌ Construction-grade detail drawings, schedule tables, hatching (Phase 2+)
- ❌ Multi-language EN labels (defer per OQ5)
- ❌ Mid-length 30-45s video cut (rejected per OQ3 — only 2 cuts)

## 10. Communication Protocol

PM/Architect agent (Claude) ↔ Dev/Test agent (separate session) ↔ PO (cầu nối).

**Khi dev/test agent cần clarification:**
1. Document question + context vào file mới: `docs/phase-2/questions-from-dev/<sprint-N>-<topic>.md`
2. PO chuyển file path qua PM/Architect agent
3. PM/Architect agent answer + commit vào same file
4. PO chuyển answer back

**Khi PRD/ADR cần update:**
- Update file canonical (PRD-05 hoặc ADR-001)
- Bump version + date
- Note trong commit message: `[PRD] update <section>` hoặc `[ADR-001] amend <decision>`

**Khi sprint hoàn thành:**
- Dev/test agent submit completion report: `docs/phase-2/sprint-reports/sprint-N.md`
- Report must include local branch, local commit hash, dirty status, exact verification commands, gate summary paths, and environment/tool versions per `07-local-git-verification-protocol.md`
- PM/Architect agent review against acceptance criteria
- PO chốt acceptance hoặc reject

## 11. Question Buffer (cho dev agent đọc trước)

Một số câu hỏi anticipated từ dev — đã có answer:

**Q: Làm sao convert DXF → DWG free?**
A: ODA File Converter (free, official) — https://www.opendesign.com/guestfiles/oda_file_converter

**Q: glTF Blender Exporter version nào stable?**
A: Blender 4.x bundled, hoặc latest từ Khronos `glTF-Blender-IO`. Test với cube + sphere fixtures trước khi production.

**Q: KTX2 BasisU encoder?**
A: `toktx` từ KTX-Software (Khronos repo). UASTC mode cho hero textures, ETC1S cho mobile.

**Q: Twinmotion vs Lumion — bắt buộc cái nào?**
A: Không bắt buộc — pick one based on team familiarity. ADR chấp nhận cả 2. Twinmotion preferred vì preset có sẵn trong PRD.

**Q: Async queue — Celery hay BullMQ?**
A: Existing stack (`ai-architect-api`) đang dùng FastAPI Python → suggest Celery + Redis. Nhưng dev agent có thể chọn khác miễn là async-first.

**Q: VN font ổn định cho PDF?**
A: Be Vietnam Pro (Google Fonts, free) — full diacritics support, embedable, sans-serif phù hợp drafting.

---

## 12. Sign-off

| Role | Status | Date |
|---|---|---|
| Product Owner | ✅ Approved | 2026-04-26 |
| PM/Architect Agent | ✅ Brief complete | 2026-04-26 |
| Dev/Test Agent | ⏳ Awaiting handoff | — |

**Handoff message format khi PO chuyển sang dev/test agent:**

> "Đầu bài phase 2 Professional Deliverables. Đọc theo thứ tự:
> 1. `docs/phase-2/06-sprint-brief-handoff.md` (start here)
> 2. Tất cả file linked trong section 1.
> Bắt đầu Sprint 1 (2D pipeline). Bug/blocker → ghi vào `docs/phase-2/questions-from-dev/`. PO sẽ relay câu trả lời từ PM/Architect."
