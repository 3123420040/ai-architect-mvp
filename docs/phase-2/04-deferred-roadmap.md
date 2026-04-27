---
title: Deferred Roadmap — Future Phase Items
phase: post-MVP (Phase 2+)
status: tracking
date: 2026-04-26
owners:
  - Product Owner (evo-pm-vn@trustingsocial.com)
related:
  - docs/phase-2/03-adr-001-standards-combo.md
---

# Deferred Roadmap — Items to Pick Up Post-MVP

> **Mục đích file này:** track formally những item đã nghiên cứu kỹ ở Phase 1 nhưng quyết định defer sang phase tiếp theo. Mỗi item có **trigger condition** (khi nào nên pickup) + **acceptance signal** (signal nào nói "ready to start") + **estimated effort**.
>
> Khi Phase 2 kickoff, file này là input chính cho prioritization session.

---

## DEF-001 — Pascal Editor (pascalorg/editor) Integration

### Summary
Browser-native parametric 3D building editor (React 19 + Next 16 + WebGPU + R3F). MIT license, 14.4k stars, very modern stack. Khả năng cao trở thành **in-app editor** cho user/PM tweak AI-generated layout trước khi render.

### Why deferred
- v0.6.0 (April 2026) — **pre-1.0**, schema breaking changes risk
- 2-contributor bus factor cao
- Không thay được SketchUp/Twinmotion cho engineer handoff (no path-tracing, no NURBS, no 2D extraction)
- MVP có thể dùng plain three.js viewer + glTF — đủ cho web preview

### What we'd use it for (Phase 2)
- **In-app editing feature**: cho user drag walls, tweak openings, di chuyển nội thất AI-generated trước khi commit render
- **Output pipeline tương thích**: editor's three.js scene → glTF export (đã native) → fit thẳng vào pipeline ADR-001

### Trigger conditions (pickup khi 1 trong các điều kiện sau)
- [ ] pascalorg/editor đạt v1.0 stable release
- [ ] Schema (Zod nodes trong `packages/core`) có guarantee backwards-compat
- [ ] Có ≥3 core contributors (giảm bus factor)
- [ ] User feedback từ MVP cho thấy "tôi muốn chỉnh sửa kết quả AI trước khi render" là top-3 request

### Acceptance signals
- [ ] Repo có CHANGELOG ghi rõ semver discipline
- [ ] `packages/core` + `packages/viewer` được publish độc lập trên npm với pin version
- [ ] Demo integration POC tốn < 1 sprint dev effort

### Estimated effort (rough)
- POC integration (embed `packages/viewer` vào AI Architect web): **1-2 sprints**
- Feature complete (full editing flow + state sync với AI generation): **3-4 sprints**

### Re-evaluate date
**Q3 2026** — kiểm tra repo health, version, contributor count.

### Reference
- Repo: https://github.com/pascalorg/editor
- Live demo: editor.pascal.app
- Initial eval: [02-market-standards-research.md § B](02-market-standards-research.md)

---

## DEF-002 — IFC 4.3 Export (Full BIM Workflow)

### Summary
buildingSMART openBIM schema, ISO 16739-1:2024. Cho phép AI Architect output xuất sang Revit / ArchiCAD / Tekla pipeline với semantic preservation (IfcWall, IfcSpace, IfcDoor, etc.).

### Why deferred
- IFC mạnh ở Detailed Design / Construction Documentation (RIBA Stage 4-5) — không phải concept/schematic của ta
- Mapping geometry → IFC entities phức tạp (wall axes, space boundaries, type definitions)
- MVP scope chỉ concept→SD → FBX + glTF + USDZ đã đủ

### What we'd use it for (Phase 2+)
- Khi khách hàng B2B (large architectural firm, developer enterprise) yêu cầu **Revit/ArchiCAD pipeline**
- Khi product mở rộng từ concept → SD sang Detailed Design (Stage 4)
- Khi cần code compliance check (auto-validate floor plan against QCVN 03/2012)

### Trigger conditions
- [ ] Pipeline đối tác B2B yêu cầu Revit/ArchiCAD nguyên bản (không chấp nhận FBX import)
- [ ] Mở rộng scope sang Detailed Design (RIBA Stage 4+)
- [ ] Khách hàng yêu cầu xin giấy phép xây dựng VN (bắt đầu cần TCVN/QCVN compliance)

### Acceptance signals
- [ ] ≥3 deal request / quarter mention "Revit/IFC required"
- [ ] Average deal size B2B > X (justify dev cost ~2-3 sprints)

### Estimated effort
- IFC 2x3 (older, simpler) basic export: **2 sprints**
- IFC 4.3 với property sets, type definitions: **3-4 sprints**
- Validation gate (IfcOpenShell test): **0.5 sprint**

### Implementation hint
- Library: **IfcOpenShell** (Python, đã được nhắc trong Phase 1 research)
- Pattern: parametric IFC builder pattern (don't try to convert raw mesh — use semantic info từ AI generation step)

### Reference
- Spec: https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/
- IfcOpenShell: https://ifcopenshell.org/

---

## DEF-003 — ISO 19650 Full Process Compliance

### Summary
ISO 19650 (Parts 1-6) là information management standard cho BIM — Common Data Environment (CDE), naming convention, workflow, info containers, security. Mandatory ở UK government projects, optional elsewhere.

### Why deferred
- Process standard, **không phải data format** — không ảnh hưởng output file
- Apply ở enterprise level (project management process), không phải product feature
- MVP chỉ adopt **naming convention inspired** (`<Project>-<Originator>-<Type>-<Number>`) trong manifest.json — đủ cho future-proofing

### What we'd use it for (Phase 2+)
- Khi AI Architect bán B2B cho large firm cần ISO 19650-compliant project delivery
- Khi cần chứng nhận compliance cho UK / EU government RFP

### Trigger conditions
- [ ] B2B deal yêu cầu ISO 19650 compliance certification
- [ ] Mở rộng sang UK/EU market

### Acceptance signals
- [ ] Có deal pipeline với compliance requirement value > X

### Estimated effort
- Naming convention enforcement (đã partial trong MVP): **0** (already done)
- Full CDE integration (project info containers, audit trail, role-based access): **5-8 sprints** (enterprise-grade)
- Certification audit: external consulting

### Reference
- Spec: https://www.iso.org/standard/68078.html

---

## DEF-004 — TCVN/QCVN Code Compliance Check

### Summary
Auto-validate floor plan against Vietnam building codes (QCVN 03/2012 — National Technical Regulation on Civil Construction Classification). Required cho permit drawing workflow.

### Why deferred
- MVP scope không cần xin giấy phép xây dựng (PO confirmed)
- Implementation phức tạp (rule engine + spatial analysis)

### What we'd use it for (Phase 2+)
- Khi product mở rộng sang permit drawing service
- Khi target user shifts từ "trình khách concept" sang "submit cho cơ quan cấp phép"

### Trigger conditions
- [ ] PO chốt mở rộng product scope sang permit drawings
- [ ] Khách yêu cầu auto-check QCVN compliance trước khi nộp

### Estimated effort: **4-6 sprints** (rule engine + UI feedback)

---

## DEF-006 — AI-Generated Procedural Material Library (via Agentic Room)

### Summary
Thay thế Plan A (CC0 curated từ Quixel/Polyhaven) bằng Plan C — **AI procedural material generation orchestrated qua Agentic Room project**. Cho phép AI Architect generate material đặc thù VN không có trong library quốc tế (gạch men, ngói âm dương, mây tre đan, đá ong, gỗ teak, vải gai…) on-demand per project.

### Why deferred
- ROOM project Phase 1 (multi-agent protocol) đang implement — chưa stable
- Plan A (CC0 curated) đủ ship MVP với ~50 starter material Modern Minimalist + Tropical VN
- R&D pipeline 8-agent + diffusion model = 2-3 tháng work — sau khi MVP launch + có demand signal

### What we'd use it for
- AI generate PBR Metal-Rough material (BaseColor + MetallicRoughness + Normal + AO) on-demand
- Material đặc thù VN: gạch men hoa văn, ngói âm dương, lam chắn nắng, đá ong, mây tre đan, sàn xi măng đánh bóng…
- Output ready-to-use trong glTF/FBX pipeline của AI Architect

### Trigger conditions
- [ ] Agentic Room Phase 1 multi-agent protocol stable (production-grade)
- [ ] AI Architect MVP launched với Plan A material
- [ ] Demand signal: AI Architect users complain "thiếu material đặc thù VN"
- [ ] Compute cost diffusion-based < library subscription cost ($30-100/tháng Quixel/Poliigon)

### Acceptance signals
- [ ] ROOM has stable multi-agent orchestration API
- [ ] POC generates 1 material end-to-end < 5 phút
- [ ] 80%+ output passes QA without human intervention

### Estimated effort
- POC (single material end-to-end): **1-2 sprints** sau khi ROOM Phase 1 done
- Production pipeline (8 agents): **4-6 sprints**
- Library bootstrap (50-100 starter VN materials): **2-3 sprints additional**

### Cross-project linkage
- **Use case file (canonical):** `/Users/nguyenquocthong/project/agentic-room/docs/external-use-cases/ai-architect-procedural-materials.md`
- **Pipeline design:** 8-agent (Brief Interpreter → Reference Curator → Texture Generator → PBR Map Derivation → Tileability Validator → PBR Validator → Asset Packager → Quality Reviewer)
- **API contract sketch:** `POST /materials/generate` + `GET /materials/job/{id}` callback pattern

### Reference
- ROOM use case file: `agentic-room/docs/external-use-cases/ai-architect-procedural-materials.md`
- glTF Material spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#metallic-roughness-material

---

## DEF-007 — 50-Material Curated Starter Pack (Modern Minimalist + Tropical VN)

### Summary
Curate, license-clear, and commit a ~50-material starter pack of PBR Metal-Rough materials covering Modern Minimalist + Tropical VN house styles. Sources: Quixel Megascans (free/subscription tier, license per terms) + Polyhaven (CC0). This is the original "Plan A" material library from OQ4.

### Why deferred (out of Sprint 2)
- Sprint 2 only needs deterministic golden-fixture materials (~5–10) to prove the GLB/FBX/KTX2 pipeline end-to-end.
- Curating 50 external materials is an **asset/licensing workstream**, not engineering — different skill set, different cadence.
- Licensing has real implications: Quixel Megascans free tier requires Epic Games account + Megascans subscription terms acknowledgment; Polyhaven is CC0 (truly public domain). These need a policy owner before any binaries are committed.
- Storage: 50 materials × 5 maps × 2K KTX2 ≈ 100–200 MB committed binaries — needs a decision on Git LFS vs. external CDN vs. signed-URL fetch.

### What we'd deliver
- ~50 materials covering: wall plasters, ceiling, slab/floor (tile, hardwood, cement, terrazzo, polished concrete), roof tiles (Vietnamese ngói âm dương, ngói tây, flat concrete), wood (teak, oak, walnut), glass, metal (steel, aluminium, brass), fabric, bamboo/rattan, brick, stone (đá ong stand-in until DEF-006 generates it), vegetation/foliage atlases, site ground, water.
- Each in PBR Metal-Roughness, KTX2-encoded, matching the Sprint 2 material registry schema.
- License manifest (`docs/phase-2/material-pack-licenses.md`) with source URL, license, attribution requirements, last-checked date per material.

### Trigger conditions
- [ ] Sprint 2 ships and pipeline correctness is validated.
- [ ] Policy decision made on: (a) storage location (in-repo LFS vs. CDN), (b) attribution surface (in-app credits page).
- [ ] Asset/licensing workstream owner identified (could be PM, design lead, or a contractor — not the engineering Dev/Test Agent).

### Acceptance signals
- [ ] License manifest reviewed and approved by PO.
- [ ] All 50 materials pass the same Sprint 2 KTX2/Metal-Rough/glTF Validator gates the synthetic registry passes.
- [ ] Render test on golden fixture shows visible quality uplift vs. synthetic baseline.

### Estimated effort
- License audit + curation: ~1 sprint of asset/PM time (not engineering).
- Engineering integration (drop into existing material registry): < 0.5 sprint.

### Reference
- OQ4 decision: `docs/phase-2/01-discovery-summary.md` § 8
- Material registry schema (Sprint 2 will define the canonical shape): `docs/phase-2/sprint-plans/sprint-2.md`
- Polyhaven: https://polyhaven.com/ (CC0)
- Quixel Megascans: https://quixel.com/megascans (license terms apply)

---

## DEF-005 — Spec-Glossiness PBR Workflow Support

### Summary
Alternative PBR workflow (Specular-Glossiness) for legacy DCC pipelines.

### Decision: **DO NOT IMPLEMENT.**
Khronos archived `KHR_materials_pbrSpecularGlossiness` extension in 2021. Metal-Roughness only is industry consensus going forward. **Remove this from consideration permanently** — not a "deferred" item, a "rejected" item kept for documentation.

---

## Tracking Notes

| ID | Item | Status | Re-evaluate |
|---|---|---|---|
| DEF-001 | Pascal Editor integration | Deferred | Q3 2026 |
| DEF-002 | IFC 4.3 export | Deferred | When B2B trigger hits |
| DEF-003 | ISO 19650 process compliance | Deferred | When enterprise B2B trigger hits |
| DEF-004 | TCVN/QCVN compliance check | Deferred | If permit-drawing scope added |
| DEF-005 | Spec-Glossiness PBR | **Rejected (do not implement)** | — |
| DEF-006 | AI Procedural Material Library (via ROOM) | Deferred | When ROOM Phase 1 stable + demand signal |
| DEF-007 | 50-Material Curated Starter Pack | Deferred | After Sprint 2 ships + policy/storage owner assigned |

---

## Update Log

- **2026-04-26** — File created. ADR-001 ratified; DEF-001 thru DEF-005 logged.
