---
title: Sprint 2 Plan — 3D Core Formats
phase: 2
status: pending-pm-architect-acceptance
date: 2026-04-27
owner: Dev/Test Agent
track: Professional Deliverables
depends_on:
  - docs/phase-2/sprint-reports/sprint-1.md
---

# Sprint 2 Plan — 3D Core Formats

No production implementation starts until the PO relays PM/Architect acceptance of this plan.

## Context Ingestion

Sprint 1 is formally accepted. The sign-off block in `docs/phase-2/sprint-reports/sprint-1.md` confirms all Sprint 1 DoD items passed, including the GitHub Actions `DWG clean-open` gate: `ODA audit round-tripped 5 DWG files`.

Locked constraints carried into Sprint 2:

- ADR-001 selects glTF 2.0 Metal-Roughness PBR as the web/client 3D spine, FBX with Twinmotion preset for engineer handoff, and BIMForum LOD 100/200/300 metadata.
- PRD-05 requires `model.glb`, `model.fbx`, LOD tagging, Metal-Roughness only materials, KTX2 textures, and zero `KHR_materials_pbrSpecularGlossiness`.
- Deferred roadmap exclusions remain active: no IFC, no Pascal Editor, no full ISO 19650 process compliance, no TCVN/QCVN compliance, no procedural material generation, and no Spec-Glossiness.

## Safety Invariants

- No Sprint 2 output may use or import `KHR_materials_pbrSpecularGlossiness`.
- Final `/textures/` output contains KTX2 only. Temporary PNG files may exist inside a build temp directory for Blender/KTX authoring but must not be copied into the bundle.
- USDZ, video, derivatives, and final `manifest.json` assembly are not implemented in Sprint 2.
- Bundle delivery remains gate-driven: if glTF validation, material inspection, texture policy, or FBX import fails, the Sprint 2 bundle is not considered releasable.
- Reuse Sprint 1 `GateResult` + JSON/MD summary style so PR comments remain consistent.

## Core Contracts

### Scene Contract

Add a Sprint 2 scene layer beside the Sprint 1 drawing contract:

- `SceneElement`: `id`, `name`, `kind`, `floor`, `lod`, `mesh_role`, `material_id`, `dimensions_m`, `transform`.
- `kind` enum: `wall`, `slab`, `roof`, `opening`, `column`, `fixed_fixture`, `furniture`, `site_context`.
- `lod` enum: `100`, `200`, `300`.
- LOD policy:
  - Walls, slabs, roof, columns, doors/windows/openings, fixed kitchen/bath fixtures: LOD 300.
  - Furniture and movable props: LOD 200.
  - Site ground/planting/neighbor massing placeholders: LOD 100-200.

### Material Contract

- `MaterialSpec`: `id`, `asset_name`, `part_name`, `fbx_name`, `workflow`, `resolution`, `texture_set`.
- `workflow` is always `metallic-roughness`.
- FBX material names use `MAT_<asset>_<part>`.
- Texture slots:
  - `baseColor`: sRGB.
  - `metallicRoughness`: linear KTX2, green = roughness, blue = metallic, red unused/0.
  - `normal`: linear, OpenGL +Y.
  - `ao`: linear, red channel.
  - `emissive`: sRGB.

### Sprint-2 Metadata Stub

Do not write final `manifest.json`. Write a Sprint 2-only metadata stub under `/3d/model_metadata.json` or `/3d/sprint2_model_metadata.json` with fields shaped to match PRD-05 Appendix B later:

```json
{
  "lod_summary": { "lod_100": 0, "lod_200": 0, "lod_300": 0 },
  "material_list": [
    {
      "name": "MAT_wall_plaster",
      "workflow": "metallic-roughness",
      "textures": {
        "baseColor": "../textures/wall_plaster_baseColor.ktx2",
        "metallicRoughness": "../textures/wall_plaster_metallicRoughness.ktx2",
        "normal": "../textures/wall_plaster_normal.ktx2",
        "ao": "../textures/wall_plaster_ao.ktx2",
        "emissive": "../textures/wall_plaster_emissive.ktx2"
      },
      "resolution": "2K"
    }
  ],
  "scene_elements": [
    { "id": "wall-f1-front", "lod": 300, "material": "MAT_wall_plaster" }
  ]
}
```

## Chosen Libraries and Versions

Versions are pinned for reproducible `ubuntu-latest` CI. Version checks were made on 2026-04-27 via official project/package sources and npm metadata.

| Purpose | Tool | Version / pin | Notes |
|---|---|---|---|
| Scene authoring, GLB/FBX export/import | Blender LTS | `4.5.1` Linux x64 tarball | Use official Blender LTS portable download, not distro `apt` Blender, to avoid version drift. |
| KTX2/BasisU encoding | KTX-Software / `toktx` | `4.4.2` | Use official Khronos release. Use `--threads 1` for deterministic CI outputs where practical. |
| glTF post-processing | `@gltf-transform/cli` | `4.3.0` | Apply Draco and KTX2 transforms, inspect output. |
| glTF extensions helpers | `@gltf-transform/extensions` | `4.3.0` | Use only in Node validation scripts if needed. |
| glTF validation | `gltf-validator` | `2.0.0-dev.3.10` | Official Khronos validator npm package. |
| Draco fallback | `gltf-pipeline` | `4.3.1` | Keep as fallback if glTF Transform Draco path proves incompatible with the Blender export. |
| Python image generation/inspection | Pillow | existing transitive via ReportLab, or pin if needed | Temporary source texture creation and pixel policy tests. |
| Existing backend/test stack | pytest, Celery, FastAPI | existing Sprint 1 pins | No synchronous product-facing render/export path. |

References for version decisions:

- Blender LTS: https://www.blender.org/download/lts/
- KTX-Software releases: https://github.com/KhronosGroup/KTX-Software/releases
- glTF Validator npm package: https://www.npmjs.com/package/gltf-validator
- glTF Pipeline npm package: https://www.npmjs.com/package/gltf-pipeline

## Proposed Module Structure

Extend `ai-architect-api/app/services/professional_deliverables/`:

```text
app/services/professional_deliverables/
  scene_contract.py          # SceneElement, MaterialSpec, TextureSpec, LOD policy
  scene_builder.py           # Golden townhouse 3D scene from Sprint 1 DrawingProject
  material_registry.py       # deterministic material specs and MAT_* naming
  texture_authoring.py       # temporary source maps, KTX2 output path plan
  ktx2_encoder.py            # toktx wrapper; UASTC hero, ETC1S mobile reserved
  blender_runner.py          # Blender binary discovery/install contract
  blender_scripts/
    export_scene.py          # build meshes/materials, export GLB + FBX
    import_fbx_check.py      # headless FBX import gate
  gltf_exporter.py           # Blender export + glTF Transform post-process
  fbx_exporter.py            # Twinmotion preset export wrapper
  model_validators.py        # GLB/FBX/material/texture gates, reusing GateResult
  sprint2_demo.py            # golden GLB/FBX/textures generation entry point
```

Tests:

```text
tests/professional_deliverables/
  test_sprint2_scene_contract.py
  test_sprint2_materials.py
  test_sprint2_gltf_gates.py
  test_sprint2_fbx_gates.py
  test_sprint2_bundle_layout.py
```

CI:

```text
.github/workflows/sprint2-deliverables.yml
tools/sprint2/package.json
tools/sprint2/package-lock.json
```

Make targets:

```text
make sprint2-demo-local     # local DXF/PDF + GLB/FBX if Blender/toktx available
make sprint2-ci             # hard CI gates on ubuntu-latest
```

## Golden Fixture Extension Strategy

Use the same golden `DrawingProject` from Sprint 1: 5 m x 15 m, 2 storeys, Tropical VN.

3D scene generation:

- Walls: extrude Sprint 1 wall segments to 3.2 m height per storey, LOD 300.
- Slabs/floors: one slab per floor, LOD 300.
- Roof: simple tropical flat/parapet roof mass from `roof_outline`, LOD 300.
- Doors/windows/openings: simple framed boxes/planes aligned to Sprint 1 openings, LOD 300.
- Columns/fixed fixtures: use Sprint 1 fixture types where stable, LOD 300 for plumbing/fixed, LOD 200 for furniture.
- Site context: ground plane and planting placeholders, LOD 100/200.
- Pivot/origin: floor center of the building footprint; one unit = one meter in Blender/glTF, with FBX exported using cm unit scale.

Bundle output:

```text
storage/professional-deliverables/project-golden-townhouse/
  /2d/        # unchanged Sprint 1 outputs
  /3d/
    model.glb
    model.fbx
    sprint2_model_metadata.json
    sprint2_gate_summary.json
    sprint2_gate_summary.md
  /textures/
    *_baseColor.ktx2
    *_metallicRoughness.ktx2
    *_normal.ktx2
    *_ao.ktx2
    *_emissive.ktx2
```

## Export Pipeline

1. Build typed scene contract from the golden `DrawingProject`.
2. Generate temporary source textures in a build temp directory.
3. Encode final KTX2 textures:
   - UASTC for hero/default Sprint 2 material textures.
   - ETC1S command support prepared but mobile 1K variants are not emitted until Sprint 3.
4. Run Blender headless:
   - Build mesh objects.
   - Assign Metal-Rough material node trees.
   - Export an intermediate GLB.
   - Export FBX with Twinmotion preset: `global_scale=100`, cm units, Z-up, embedded media, smoothing groups, optional triangulation.
5. Post-process GLB:
   - Apply Draco compression.
   - Ensure KTX2 textures and `KHR_texture_basisu`.
6. Run gates.
7. Write gate summary JSON/MD and metadata stub.

## Test Plan Per CI Gate

| Gate | Test implementation |
|---|---|
| glTF Validator 0 errors | Install `gltf-validator@2.0.0-dev.3.10`; run against `model.glb`; parse JSON; fail on any error. Warnings pass only if code is an unused vertex attribute class. |
| Metal-Rough only | Parse GLB JSON chunk or use glTF Transform inspect; assert every material has `pbrMetallicRoughness`; assert extensions do not include `KHR_materials_pbrSpecularGlossiness`. |
| MetallicRoughness packing | Decode/generated-source reference and/or KTX2 metadata sample after `toktx`; sample at least one deterministic pixel per material; assert R is unused/0, G roughness in expected range, B metallic in expected range. |
| FBX import | Run Blender 4.5.1 headless `import_fbx_check.py`; assert expected mesh count/categories, material names begin `MAT_`, embedded texture images resolve after import, scene up-axis is Z, unit scale corresponds to centimeters for FBX. |
| Texture resolution policy | Inspect KTX2 dimensions with `ktx info` or local parser; assert hero/default textures are >= 2048, none exceed 4096, and no Sprint 2 final mobile variants are emitted. |
| Bundle layout | Assert `/3d/model.glb`, `/3d/model.fbx`, `/textures/*.ktx2`, and `/3d/sprint2_model_metadata.json` exist; assert no raw `.png`, `.jpg`, `.jpeg` under final bundle. |
| Failure case | Inject one degenerate mesh or NaN vertex in a unit test fixture; exporter/gate must fail and not mark bundle releasable. |

## CI Plan

`sprint2-deliverables.yml` on `ubuntu-latest`:

1. Checkout.
2. Set up Python 3.12.
3. Set up Node 20 or 22 with npm cache.
4. Install backend requirements.
5. Install Blender 4.5.1 portable tarball to `${RUNNER_TEMP}/blender`.
6. Install KTX-Software 4.4.2 Linux release or build/install package exposing `toktx`/`ktx`.
7. `npm ci --prefix tools/sprint2`.
8. Run `make sprint2-ci`.
9. Upload `sprint2_gate_summary.md/json`.
10. Post sticky PR comment using the same permission pattern fixed in Sprint 1.

Docker guardrail:

- Sprint 2 CI may install tools directly on `ubuntu-latest` for validator speed, but the implementation will keep binary paths env-driven (`BLENDER_BIN`, `TOKTX_BIN`, `GLTF_VALIDATOR_BIN`) so the same path can be moved into Docker images later without code changes.

## Clarification Questions

Formal question file:

- `docs/phase-2/questions-from-dev/sprint-2-material-library-scope.md`

This is non-blocking for plan acceptance if PM/Architect agrees the golden fixture material set is enough for Sprint 2 DoD. If unanswered within 24 hours, I will implement a deterministic material registry sufficient for the golden fixture plus a schema that can scale to the later ~50-material curated pack, without committing external Quixel/Polyhaven assets in Sprint 2.

