# 02 — Market Standards Research & OSS Eval (pascalorg/editor)

**Project:** AI Architect — VN market, modern minimalist + tropical VN house
**Scope:** Concept → Schematic Design (RIBA Stage 2-3 / AIA SD). Output 2D drawings + 3D models + cinematic videos for (1) client concept signoff, (2) BĐS marketing, (3) handoff cho kỹ sư (SketchUp+V-Ray/Enscape, 3ds Max+Twinmotion/Lumion).
**Out of scope:** Permit drawings, shop/construction drawings.
**Date:** 2026-04-26

---

## A. Market Standards Research

### 2D Standards

#### 1. NCS — US National CAD Standard (V7, current)
NCS V7 (2024) is the authoritative US CAD standard, packaging AIA CAD Layer Guidelines + CSI Uniform Drawing System (UDS) + NIBS BIM Implementation + Plotting Guidelines. **Layer naming format**: `Discipline-Major Group-Minor Group-Status` (e.g., `A-WALL-FULL-N`). Defines line weight pen tables, sheet identification, title block requirements, drawing set organization. **License: paid.** Single license ~$400-700, Site $1,428, Enterprise $3,808 (NCS V6 retired for new buyers; existing V6 license holders still have access).
**Fit:** Phù hợp cho concept/schematic 2D plans, sections, elevations. Quá nặng nếu chỉ làm marketing — nhưng layer naming subset là tài sản handoff giá trị cho engineer.
**How to apply:** Adopt **AIA layer naming subset** (free reference PDFs widely available) + NCS title block convention. Dev agent: define layer dictionary trong DXF/DWG export module với prefix `A-` (Architecture), `S-` (Structure), `E-` (Electrical), kèm color/lineweight map.
- Spec: https://www.nationalcadstandard.org/ncs7/
- AIA Layer Guidelines reference (V6 PDF): https://www.nationalcadstandard.org/ncs6/pdfs/ncs6_clg_lnf.pdf

#### 2. ISO 13567 (Parts 1-3, 2017) — CAD Layer Organization
International alternative cho NCS. Layer names = chuỗi alpha-numeric với mandatory + optional fixed-length fields (Agent, Element, Presentation, Status…). **Paid** (~CHF 158/part qua ISO).
**Fit:** Tốt cho hand-off quốc tế, nhưng VN thị trường chủ yếu dùng AIA-style trong các văn phòng dùng AutoCAD/Revit. Less common ở studio VN.
**How to apply:** Dùng ISO 13567 nếu khách hàng/đối tác EU. Otherwise prioritize AIA. Dev agent: optional ISO-mode layer mapper cho export.
- Spec: https://www.iso.org/standard/70181.html

#### 3. AIA CAD Layer Guidelines
Embedded trong NCS, nhưng PDF V5/V6 free copies lưu hành rộng rãi (CUNY, Duke). Thực chất là **de-facto standard** cho US/VN AutoCAD-driven offices. Format `[Discipline]-[Major]-[Minor]-[Status]`.
**Fit:** Best fit cho MVP — pragmatic, widely understood by VN engineers using SketchUp/AutoCAD/Revit.
**How to apply:** Hardcode AIA layer dictionary trong export module. Cover ~20-30 most-used layers (A-WALL, A-DOOR, A-GLAZ, A-FURN, A-AREA, A-ROOF, S-COLS, etc.) đủ cho schematic.
- Reference: https://facilities.duke.edu/sites/default/files/AIA%20CAD%20Layer%20Guidelines.pdf

#### 4. TCVN (Vietnam National Standards) — CAD?
**Finding: KHÔNG có TCVN equivalent dedicated cho CAD layer naming/architectural drafting.** TCVN ~14,000 standards cover construction materials, fire safety, structural, environment — không có CAD layer org spec. Studios VN thực tế xài AIA/NCS hoặc internal office standards. QCVN (mandatory regulations) chỉ apply ở giai đoạn permit/construction (out-of-scope).
**How to apply:** Skip TCVN cho 2D layer convention. Document trong README: "AI Architect uses AIA-derived layer naming, compatible with VN office norms."
- VSQI tra cứu: https://vsqi.gov.vn/en/tieu-chuan

### 3D Standards

#### 5. glTF 2.0 (Khronos) — ISO/IEC 12113:2022
"JPEG of 3D." JSON + binary (.glb), royalty-free, native PBR Metal-Rough, animations, KTX2 textures, Draco mesh compression. Universal support: web (three.js, Babylon), Blender, 3ds Max, Unity, Unreal, AR Quick Look (via conversion).
**Fit:** **CHỌN — primary web 3D format** cho web preview & client review.
**How to apply:** All 3D artifacts emit `.glb` (binary, single file) + optional `.gltf` (text, debug). Use Draco compression cho mesh, KTX2/BasisU cho textures. Validate bằng Khronos glTF Validator.
- Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
- Validator: https://github.khronos.org/glTF-Validator/

#### 6. IFC 4.3 / ISO 16739-1:2024
buildingSMART openBIM schema. IFC 4.3.2.0 ADD2 (April 2024). CC BY-ND 4.0. Heavyweight, semantic-rich (IfcWall, IfcSpace, IfcDoor…), used cho Revit/ArchiCAD/Tekla exchange.
**Fit:** **OVER-SPEC cho concept/schematic stage.** IFC mạnh ở DD/CD (RIBA 4-5). Cho MVP scope (concept-SD) có lợi nhỏ vs cost cao (mapping geometry → IFC entities phức tạp).
**How to apply:** **Phase 2+ feature.** Khi handoff cho team dùng Revit/ArchiCAD muốn semantic walls/spaces, generate IFC2x3 hoặc IFC4 simplified. Cho MVP, dùng FBX + glTF.
- Spec: https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/

#### 7. ISO 19650 (Parts 1-6) — BIM Information Management
Process standard, không phải data format. CDE (Common Data Environment), naming, workflow, info containers, security. Mandatory ở UK gov projects.
**Fit:** **Out-of-scope cho MVP product.** Đây là enterprise process layer — chỉ apply nếu AI Architect bán B2B cho large firms làm projects ISO 19650-compliant.
**How to apply:** Document compatibility (file naming `Project-Originator-Volume-Level-Type-Role-Number`) khi xuất bundle. Optional manifest.json theo info container concept.
- Spec: https://www.iso.org/standard/68078.html

#### 8. BIMForum LOD Specification 2024
Industry de-facto for "how detailed?" definition. **LOD 100**: symbolic/2D placeholder, no geometry. **LOD 200**: generic geometry, approximate size/shape/location. **LOD 300**: specific geometry, accurate quantities/dimensions — **design intent finalized**. **LOD 350**: + interfaces with adjacent systems (coordination). **LOD 400**: fabrication-level. Free PDF.
**Fit:** **LOD 200 → LOD 300** = sweet spot cho AI Architect output. Concept = LOD 100-200, Schematic = LOD 200-300. Engineer downstream pushes to LOD 350-400 in SketchUp/Revit.
**How to apply:** Tag every model element với LOD. Hero render assets at LOD 300 (walls, openings, fixed furniture); decorative furniture LOD 200; site context LOD 100. Document in deliverable spec.
- Spec PDF: https://bimforum.org/wp-content/uploads/2024/11/LOD-Spec-2024-Part-I-official-English.pdf

#### 9. USDZ + Apple AR Quick Look
USDZ = zipped USD package, native iOS/iPadOS/visionOS AR. PBR via UsdPreviewSurface (~ metal/rough). Apple guidelines: ≤200k tris, file ≤4-8 MB, 1 unit = 1 meter, pivot ở floor center, embed all textures, max 2K textures.
**Fit:** **CHỌN — secondary delivery format** cho client view AR trên iPhone (nhà mẫu BĐS marketing rất tropical-VN-friendly use case).
**How to apply:** Convert glTF → USDZ via `usd_from_gltf` (Google) hoặc Reality Converter. Auto-budget: simplify mesh + texture downsize cho mobile AR pipeline.
- Apple guidelines: https://developer.apple.com/augmented-reality/quick-look/
- ARKit doc: https://developer.apple.com/documentation/arkit/previewing-a-model-with-ar-quick-look

#### 10. FBX Best Practices for Twinmotion/Lumion
FBX = lingua franca cho DCC ↔ realtime engine. Critical settings: **units = cm** (UE/Twinmotion), **Y-up vs Z-up axis convert**, embed textures, UV0 inside 0-1, separate materials per shader, naming convention `MAT_<asset>_<part>`, merge by material on export, no overlapping UVs cho lightmap (UV1).
**Fit:** **CHỌN — primary handoff format** cho engineer using Twinmotion/Lumion. SketchUp users prefer DAE/SKP nhưng FBX universally importable.
**How to apply:** Dev agent: FBX exporter với preset profiles `twinmotion`, `lumion`, `sketchup-import`. Auto-bake transform, triangulate optional, smoothing groups exported.

### Video Standards

#### 11. Twinmotion Render Presets (2024.1, UE5.4)
Defaults: H.264 MP4 / Apple ProRes (cinematic). **Resolution**: 1920×1080 (preview), 3840×2160 (4K hero). Frame rate: 30fps default, 60fps for fast moves. Filmback presets (real camera sensor sizes) trong 2024.1. Render layers (up to 5) cho compositing. Path tracer + Lumen GI. Bloom + DoF + motion blur cho cinematic.
**How to apply:** Standardize 4K/30fps H.264 MP4 cho master, derive social cuts.
- Doc: https://dev.epicgames.com/documentation/en-us/twinmotion/export-settings-for-videos-in-twinmotion

#### 12. Lumion Render Best Practices
**5 Star quality** = production (16 subsamples). **Output**: 3840×2160 master. Ray tracing: 256-512 samples, 2-4 bounces (interior). Built-in denoiser. **30 fps** for static cam, 60 fps cho fast pans. Rasterization for exterior speed, RT for interior fidelity.
**How to apply:** Cho VN tropical house exteriors, default to rasterization + sun study; interior hero shots use RT 256 samples.
- Doc: https://support.lumion.com/hc/en-us/articles/360003476493

#### 13. CGarchitect / CGconnect Conventions
No formal spec — community norms: hero stills 4K, animation 1080p/4K @ 30fps, color grade ACES or Rec.709, sRGB output, 16-bit EXR for stills if compositing. Architectural Graphic Standards (Wiley, 12th ed.) = **drawing convention bible** (annotation, scale, hatch).
**Fit:** Soft conventions, follow industry-norm not standard.
- https://cgconnect.chaos.com/

#### 14. Social Media Reel Specs (master cuts)
Universal vertical preset: **1080×1920, 9:16, H.264 MP4, AAC audio, 30 fps (60 for motion-heavy), 10-15 Mbps bitrate.**
- YouTube Shorts: ≤ 3 min, supports 4K (3840×2160 vertical), ≥8 Mbps @ 1080p.
- Instagram Reels: ≤ 90s, 1080×1920, ~4 Mbps.
- TikTok: ≤ 10 min, 1080×1920.

**How to apply:** Render master at 4K 16:9 horizontal **and** 4K 9:16 vertical safe-area; derive 1080p H.264 social variants automatically.

### PBR / Texture

#### 15. PBR Workflow — Metallic-Roughness vs Specular-Glossiness
**Metal-Rough = standard.** glTF 2.0 ratified Metal-Rough as core; Spec-Gloss extension (`KHR_materials_pbrSpecularGlossiness`) **archived 2021**. Metal-Rough: 2/3 maps grayscale → memory efficient, ideal cho realtime/web. Spec-Gloss: more artistic control, legacy DCC pipelines.
**How to apply:** **All PBR material = Metal-Rough.** Map slots: BaseColor (sRGB), Metallic-Roughness packed (B=metallic, G=roughness, linear), Normal (linear, OpenGL +Y), AO (linear, R channel), Emissive (sRGB).
- Khronos: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#metallic-roughness-material

#### 16. Texture Resolution Conventions
- **512px**: small props, far-distance debris.
- **1K (1024)**: small/distant, secondary props (lamps, knobs, books).
- **2K (2048)**: **default** cho most archviz — walls, floors, generic furniture, mid-range view.
- **4K (4096)**: hero close-ups, large surfaces seen up-close (feature wood floor, marble counter), tropical materials (rattan, brick wall) where camera dwells.
- **8K**: only for cinematic close-ups, rarely needed cho concept.

**How to apply:** Default 2K. Auto-promote to 4K nếu surface area > X m² and visible trong hero shot. Auto-demote to 1K cho mobile/AR/USDZ.

---

## B. OSS Evaluation — pascalorg/editor

**URL:** https://github.com/pascalorg/editor
**Live:** editor.pascal.app

### Findings

| Aspect | Detail |
|---|---|
| What | Web-based 3D building editor (walls/floors/ceilings/roofs/zones/furniture) |
| Stack | React 19, Next.js 16, TypeScript 98.8%, three.js + React-Three-Fiber + Drei, **WebGPU**, Zustand+Zundo (undo/redo), Zod, three-bvh-csg (Boolean ops), Turborepo/Bun |
| Repo | Monorepo: `apps/editor` (Next app), `packages/core` (schemas+state+geometry), `packages/viewer` (R3F render) |
| License | **MIT** — commercial-friendly |
| Stars | 14.4k (very active) |
| Forks | 1.8k |
| Issues | 16 open |
| Latest release | v0.6.0 (April 22, 2026) — recent |
| Contributors | 2 core (Aymeric Rabot, Wassim Samad) |

### Answers

**1. Tool gì? Use case?**
Browser-native parametric 3D building editor — user drags walls, places windows/doors/furniture, navigate trong WebGPU viewer. Closest analog = **early SketchUp Web** hoặc **Spline** but specialized cho buildings. MIT + monorepo packaging means `core` + `viewer` packages are reusable as embedded library.

**2. Có dùng làm 3D editor handoff cho kỹ sư thiết kế?**
**Không thay thế SketchUp/Twinmotion**. Reasons:
- No V-Ray/Lumion-grade rendering (R3F PBR ≠ path-traced).
- No advanced modeling (NURBS, complex roof, terrain).
- No engineer-side ecosystem (plugins, extensions, .skp/.max compatibility).
- No 2D drawing extraction (sections/elevations từ model).
- Material library chưa near SketchUp 3D Warehouse / Twinmotion library.

**Nhưng** rất phù hợp làm **internal AI Architect viewer/editor** — embed vào product để user/PM tweak AI-generated layout trước khi render. Output 3D scene → export glTF → engineer downstream uses anyway.

**3. Maturity?**
**Late beta / early production** (v0.6, không phải 1.0). 14.4k stars + April 2026 release = healthy. 2-contributor bus factor đáng quan ngại cho production dependency. 16 open issues = manageable.

**4. Integrate với AI Architect pipeline?**
- **Input**: AI generates building topology (walls bounding box, openings, slab outlines) → map vào schema của `packages/core` (Zod-validated nodes). Doable.
- **Output**: editor's three.js scene → standard glTF/GLB export (already three.js native). Compatible với glTF 2.0 pipeline (Section A.5).
- Embed `packages/viewer` như React component trong AI Architect web app.
- Risk: schema breaking changes pre-1.0; need version pin.

**5. Verdict: EXPERIMENT (Phase 2+).**
- **Don't use cho MVP**: tăng complexity, immature schema, không phải core differentiator. MVP nên dùng **plain three.js viewer + glTF** đủ cho web preview.
- **Phase 2 candidate** cho "in-app editing" feature (let user drag walls to refine AI output before render). Fork `packages/core` schemas as inspiration; depending on stability around v1.0, consider as embedded dep.
- Track repo, monitor v1.0 release, re-evaluate Q3 2026.

---

## Verdict — Recommended Combo cho AI Architect MVP

| Tier | Standard chọn | Format file | Lý do chọn |
|---|---|---|---|
| 2D layer naming | **AIA CAD Layer Guidelines** (subset of NCS V7) | `.dwg` / `.dxf` | De-facto VN+US, free reference, engineers recognize instantly |
| 2D drawing convention | **Architectural Graphic Standards** (annotation/scale/hatch) | `.dwg` + `.pdf` | Industry default; pair with title block tới NCS-style |
| 3D primary (web/preview/handoff) | **glTF 2.0** (Metal-Rough PBR) | `.glb` (Draco + KTX2) | Royalty-free, ISO/IEC 12113, universal viewer support, smallest payload |
| 3D handoff cho realtime engine | **FBX** (Twinmotion/Lumion preset) | `.fbx` (embed media, cm units) | Lingua franca cho UE/Twinmotion/Lumion + 3ds Max |
| 3D handoff cho SketchUp | **glTF 2.0** + **DAE** fallback | `.glb` / `.dae` | SketchUp 2025 imports glTF natively; DAE fallback |
| AR mobile | **USDZ** | `.usdz` (≤8 MB, ≤200k tris, ≤2K tex) | iOS native AR Quick Look — killer demo cho BĐS marketing |
| BIM (optional, Phase 2) | **IFC 4.3** simplified | `.ifc` | Khi khách yêu cầu Revit/ArchiCAD pipeline |
| Detail level tagging | **BIMForum LOD 200-300** | metadata JSON | Sweet spot cho concept→SD scope |
| Material/texture | **PBR Metal-Rough**, 2K default, 4K hero | PNG/KTX2 | glTF 2.0 native; perf-balanced |
| Video master | **3840×2160 / 30 fps / H.264 MP4** | `.mp4` | Twinmotion/Lumion native; client review |
| Video social vertical | **1080×1920 / 9:16 / 30 fps / H.264 / 10-15 Mbps** | `.mp4` | Universal Reels/Shorts/TikTok export |
| Bundle naming | ISO 19650-inspired `<Project>-<Origin>-<Type>-<Number>` | folder + `manifest.json` | Future-proof for enterprise B2B |
| OSS editor | **pascalorg/editor — defer to Phase 2** | — | Promising but pre-1.0; revisit Q3 2026 |

**MVP delivery bundle per project (concrete spec):**
```
/project-<id>/
  /2d/      *.dwg (AIA layers), *.pdf (set: A-100 site, A-101 plan, A-201 elev, A-301 section)
  /3d/      model.glb (hero, Draco+KTX2), model.fbx (Twinmotion preset), model.usdz (AR)
  /video/   master_4k.mp4, reel_9x16_1080p.mp4, walkthrough_4k.mp4
  /textures/ *.ktx2 (2K default, 4K for hero materials)
  manifest.json  // LOD tags, material list, scene metadata, ISO 19650-style ID
```
