---
adr: 001
title: Professional Deliverable Standards Combo (2D / 3D / Video)
status: ACCEPTED
date: 2026-04-26
deciders:
  - Product Owner (evo-pm-vn@trustingsocial.com)
  - PM/Architect Agent (Claude)
supersedes: none
related:
  - docs/phase-2/01-discovery-summary.md
  - docs/phase-2/02-market-standards-research.md
  - docs/phase-2/04-deferred-roadmap.md
---

# ADR-001 — Professional Deliverable Standards Combo

## Status
**ACCEPTED** — 2026-04-26

## Context

AI Architect MVP cần nâng cấp deliverable lên chuẩn thị trường để phục vụ 3 use case (theo thứ tự ưu tiên):
1. Sales — trình khách hàng chốt concept
2. Marketing — bán hàng cho developer BĐS
3. Engineering handoff — kỹ sư thiết kế (SketchUp+V-Ray/Enscape, 3ds Max+Twinmotion/Lumion) refine thành sản phẩm cuối

Scope: Concept Design → Schematic Design (RIBA Stage 2-3 / AIA SD).
Out of scope: shop drawing thi công, xin giấy phép xây dựng, TCVN/QCVN compliance, BIM workflow đầy đủ.

Đã làm market research (xem [02-market-standards-research.md](02-market-standards-research.md)) covering 16 standards: NCS V7, ISO 13567, AIA CAD, TCVN, glTF 2.0, IFC 4.3, ISO 19650, BIMForum LOD, USDZ, FBX, Twinmotion/Lumion video presets, social media specs, PBR Metal-Rough vs Spec-Gloss, texture resolutions.

## Decision

Adopt combo standards sau cho **Phase 1 MVP** (current product):

### 2D Deliverables
| Aspect | Standard | Format |
|---|---|---|
| Layer naming | **AIA CAD Layer Guidelines** (subset of NCS V7) | `.dwg` + `.dxf` |
| Drawing convention | **Architectural Graphic Standards** (Wiley) for annotation/scale/hatch | `.dwg` + `.pdf` |
| Title block | NCS-style (project info, sheet number, scale, north arrow, KTS stamp placeholder) | embedded |
| Sheet set (minimum) | A-100 Site / A-101 Floor Plan / A-201 Elevations (4 mặt) / A-301 Sections (1-2) | numbered per AIA convention |

**Layer dictionary scope:** ~20-30 most-used layers hardcoded — `A-WALL`, `A-WALL-FULL`, `A-DOOR`, `A-GLAZ` (windows), `A-FURN`, `A-FLOR`, `A-AREA`, `A-ROOF`, `A-ANNO-DIMS`, `A-ANNO-TEXT`, `S-COLS`, `S-BEAM`, `E-LITE`, `P-FIXT`, etc. Color/lineweight map theo AIA defaults.

### 3D Deliverables
| Use case | Standard | Format |
|---|---|---|
| Web preview / client review | **glTF 2.0 Metal-Roughness PBR** (ISO/IEC 12113:2022) | `.glb` (Draco mesh + KTX2 texture compression) |
| Engineer handoff — Twinmotion/Lumion/3ds Max | **FBX with Twinmotion preset** (cm units, Y-up→Z-up convert, embed media) | `.fbx` |
| Engineer handoff — SketchUp | **glTF 2.0** primary (SketchUp 2025+ imports natively) + **DAE** fallback | `.glb` / `.dae` |
| AR mobile (BĐS marketing killer demo) | **USDZ** (Apple AR Quick Look guidelines: ≤8MB, ≤200k tris, ≤2K textures, 1 unit = 1m, pivot at floor center) | `.usdz` |
| Detail level tagging | **BIMForum LOD Specification 2024** — LOD 200 (concept) → LOD 300 (schematic) | metadata in `manifest.json` |

**LOD strategy:**
- Hero render assets (walls, openings, fixed furniture, structural columns): **LOD 300**
- Decorative furniture, props: **LOD 200**
- Site context (terrain, neighboring buildings): **LOD 100-200**

### Material / Texture
| Aspect | Standard |
|---|---|
| PBR workflow | **Metal-Roughness only** — Specular-Glossiness archived by Khronos 2021, do NOT implement |
| Texture map slots | BaseColor (sRGB), MetallicRoughness packed (B=metallic, G=roughness, linear), Normal (linear, OpenGL +Y), AO (linear, R), Emissive (sRGB) |
| Default resolution | **2K (2048×2048)** |
| Hero close-up | **4K** for surfaces seen up-close (feature wood floor, marble counter, tropical materials like rattan/brick wall) |
| Mobile/AR | Auto-downsize to **1K** for USDZ pipeline |

### Video Deliverables
| Use case | Spec | Format |
|---|---|---|
| Master render — cinematic walkthrough | **3840×2160 (4K) / 30fps / H.264 MP4** | `.mp4` |
| Marketing reel social vertical | **1080×1920 (9:16) / 30fps / H.264 / 10-15 Mbps / AAC** — universal cho YouTube Shorts, Instagram Reels, TikTok | `.mp4` |
| Render engine | Twinmotion 2024.1 preset OR Lumion 5-Star quality (RT 256 samples interior, rasterization exterior) | — |
| Color grading | **ACES** preferred, **Rec.709 sRGB** acceptable | — |

### Bundle Structure & Naming
**Naming convention:** ISO 19650-inspired `<Project>-<Originator>-<Type>-<Number>` (apply to filenames inside bundle, not enforce full ISO 19650 process).

**Per-project bundle:**
```
/project-<id>/
  /2d/       *.dwg (AIA layers), *.pdf (sheet set A-100/101/201/301)
  /3d/       model.glb   (hero, Draco+KTX2)
             model.fbx   (Twinmotion preset, cm, embed)
             model.usdz  (AR mobile, ≤8MB)
  /video/    master_4k.mp4
             reel_9x16_1080p.mp4
             walkthrough_4k.mp4
  /textures/ *.ktx2 (2K default, 4K hero, 1K mobile derivatives)
  manifest.json  // LOD tags per element, material list, scene metadata, ISO 19650-style ID
```

## Rationale

### Why AIA over NCS V7 / ISO 13567
- AIA reference PDFs free; NCS V7 paid ($400-1.4k single license)
- VN engineers using AutoCAD/Revit recognize AIA conventions instantly
- TCVN không có equivalent → AIA fills gap pragmatically

### Why glTF 2.0 as 3D spine
- Royalty-free ISO/IEC 12113:2022
- Universal viewer: web (three.js, Babylon), Blender, 3ds Max, Unity, Unreal
- Native PBR Metal-Rough = no migration risk
- Smallest payload với Draco+KTX2

### Why FBX for engineer handoff (not OBJ/DAE)
- Lingua franca cho realtime engine (UE/Twinmotion/Lumion)
- Materials + animations + bones support
- 3ds Max native; SketchUp imports cleanly

### Why USDZ for AR
- iOS native AR Quick Look — zero install, scan QR → see house in space
- Killer marketing demo cho BĐS sales (nhà mẫu virtual)
- Apple ecosystem dominant ở khách hàng VN cao cấp

### Why defer IFC / ISO 19650 / Pascal editor (Phase 2+)
See [04-deferred-roadmap.md](04-deferred-roadmap.md) for full reasoning + trigger conditions.

### Why LOD 200-300 not higher
- Concept→Schematic stage doesn't need LOD 350-400
- Engineer downstream pushes to 350-400 in their tool
- Generating LOD 400 in AI pipeline = wasted compute

## Consequences

### Positive
- ✅ Free standards stack (no license fees) → faster MVP
- ✅ Universal compatibility (web, mobile, desktop, all DCC tools)
- ✅ Engineer handoff works out-of-the-box for SketchUp + Twinmotion + Lumion + 3ds Max
- ✅ AR demo capability từ ngày 1 → marketing differentiator
- ✅ Future-proof bundle structure (ISO 19650-inspired naming → enterprise B2B sau)

### Negative / Trade-offs
- ❌ MVP **không serve được Revit/ArchiCAD BIM workflow** (yêu cầu IFC) — flagged as Phase 2 trigger
- ❌ AIA layer dictionary cần maintain manually nếu standards update — low risk, AIA stable
- ❌ USDZ pipeline = thêm conversion step (glTF → USDZ via `usd_from_gltf` / Reality Converter)
- ❌ Twinmotion/Lumion preset profiles cần test với engineer thực tế để validate import cleanly

### Risks
| Risk | Mitigation |
|---|---|
| FBX import fail trong Twinmotion/Lumion | Test với asset thực ở Sprint 1; có Twinmotion + Lumion preset profile riêng |
| USDZ ≤200k tris budget tight cho hero models | Auto-decimation pipeline; provide both `model_full.usdz` (interior) + `model_lite.usdz` (mobile-first) nếu cần |
| AIA layer set chưa đủ cho VN office norms | Beta test với 2-3 KTS VN, expand dictionary trước GA |

## Implementation Checklist (cho dev/test agent)

- [ ] Implement DWG/DXF exporter với hardcoded AIA layer dictionary (~25 layers)
- [ ] Implement PDF generator với NCS-style title block template
- [ ] Implement glTF 2.0 exporter (Metal-Rough only) với Draco + KTX2 compression
- [ ] Validate output bằng Khronos glTF Validator (CI gate)
- [ ] Implement FBX exporter với Twinmotion preset (cm, Y→Z, embed media)
- [ ] Implement USDZ converter (glTF → USDZ pipeline) với mobile budget enforcement
- [ ] Implement BIMForum LOD tagging trong scene graph metadata
- [ ] Build manifest.json schema (LOD, materials, ISO 19650-style ID)
- [ ] Setup Twinmotion/Lumion video render preset profiles (4K/30fps H.264)
- [ ] Setup social reel auto-derivation (master 4K → 9:16 1080p crop with safe area)
- [ ] PBR material library Metal-Rough only — 2K base, 4K hero variants
- [ ] CI tests: each output format passes its validator (glTF Validator, PDF/A check, FBX import test)

## References (spec gốc đính kèm trong research doc)

- AIA CAD Layer Guidelines: https://facilities.duke.edu/sites/default/files/AIA%20CAD%20Layer%20Guidelines.pdf
- glTF 2.0 spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
- glTF Validator: https://github.khronos.org/glTF-Validator/
- BIMForum LOD 2024: https://bimforum.org/wp-content/uploads/2024/11/LOD-Spec-2024-Part-I-official-English.pdf
- Apple AR Quick Look: https://developer.apple.com/augmented-reality/quick-look/
- Twinmotion video export: https://dev.epicgames.com/documentation/en-us/twinmotion/export-settings-for-videos-in-twinmotion
- Lumion render guide: https://support.lumion.com/hc/en-us/articles/360003476493
