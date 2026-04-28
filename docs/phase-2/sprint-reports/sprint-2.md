---
title: Sprint 2 Report — 3D Core Formats
phase: 2
status: ACCEPTED
date: 2026-04-27
accepted: 2026-04-27
owner: Dev/Test Agent
reviewer: PM/Architect Agent
pr: https://github.com/blackbirdzzzz365-gif/ai-architect-api/pull/2
---

# Sign-off (PM/Architect Agent — 2026-04-27)

**Sprint 2 ACCEPTED.** All Sprint 2 DoD items verified directly against code + outputs:

- [x] `model.glb` passes Khronos glTF Validator (errors=0, warnings=0).
- [x] Metal-Rough only enforced — JSON scan in `model_validators.py:59-61` rejects any presence of `KHR_materials_pbrSpecularGlossiness`.
- [x] MR channel packing verified by per-material pixel sampling (`extract_ktx_rgba8_sample` + tolerance).
- [x] FBX gate: 40 meshes / 9 materials / extents in cm / Z-up / **UV0 ∈ [0, 1] enforced** (per Sprint 2 guidance #2).
- [x] `KTX_BIN` env var (not `TOKTX_BIN`) supports unified `ktx` 4.x CLI with `toktx` legacy fallback (per Sprint 2 guidance #1).
- [x] `FBX_PRESET_TWINMOTION` constant pattern adopted for future Lumion preset extension (per Sprint 2 guidance #3).
- [x] Texture policy: hero ≥2K, mobile ≤1K, max ≤4K; final `/textures/` is KTX2-only.
- [x] USDZ correctly skipped (Sprint 3 scope).
- [x] Sprint 1 companion CI passed on same PR — zero regression to 2D pipeline.

## BasisU KTX2 validator limitation — handled correctly

The npm `gltf-validator@2.0.0-dev.3.10` does not decode BasisU KTX2 supercompressed textures (Khronos validator scope is glTF JSON + buffer structure). Dev demoted only `IMAGE_UNRECOGNIZED_FORMAT` to info-level and ran KTX-Software `ktx validate` against every KTX2 file as a separate gate. This dual-validator pattern is correct.

Sprint 3 is now formally unblocked.

---


# Sprint 2 Report — 3D Core Formats

## What Was Built

Implemented in `ai-architect-api/`:

| Path | Purpose |
|---|---|
| `app/services/professional_deliverables/scene_contract.py` | Typed Sprint 2 3D scene contract, BIMForum LOD tags, material/texture slot contracts. |
| `app/services/professional_deliverables/scene_builder.py` | Golden townhouse 3D scene derived from the Sprint 1 fixture. |
| `app/services/professional_deliverables/material_registry.py` | Deterministic 9-material fixture set using `MAT_<asset>_<part>` naming. |
| `app/services/professional_deliverables/texture_authoring.py` | Deterministic temporary source maps for BaseColor, MetallicRoughness, Normal, AO, Emissive. |
| `app/services/professional_deliverables/ktx2_encoder.py` | KTX-Software wrapper using `KTX_BIN`, unified `ktx create`, KTX validation, and raw RGBA sampling. |
| `app/services/professional_deliverables/gltf_authoring.py` | glTF/GLB authoring with Metal-Roughness materials, Draco-compatible geometry, UV0, tangents, and `KHR_texture_basisu` texture references. |
| `app/services/professional_deliverables/gltf_exporter.py` | glTF Transform Draco post-processing. |
| `app/services/professional_deliverables/blender_runner.py` | Blender binary discovery and headless script runner. |
| `app/services/professional_deliverables/fbx_exporter.py` | FBX exporter with `FBX_PRESET_TWINMOTION` constant. |
| `app/services/professional_deliverables/blender_scripts/export_fbx_scene.py` | Blender scene construction and Twinmotion FBX export. |
| `app/services/professional_deliverables/blender_scripts/import_fbx_check.py` | Headless FBX import gate, including material resolution, cm units, Z-up, and UV0 range check. |
| `app/services/professional_deliverables/model_validators.py` | Sprint 2 gates using the Sprint 1 `GateResult` JSON/MD summary pattern. |
| `app/services/professional_deliverables/sprint2_demo.py` | Golden 3D bundle generator CLI. |
| `app/tasks/professional_deliverables.py` | Async task entrypoint extended for Sprint 2 generation. |
| `tools/sprint2/package.json` | Node tool pins for glTF Transform and Khronos glTF Validator. |
| `tools/sprint2/validate-gltf.mjs` | Validator wrapper with external texture resource loading. |
| `tests/professional_deliverables/test_sprint2_*.py` | Focused Sprint 2 tests for scene, texture, GLB, FBX, and gate behavior. |
| `.github/workflows/sprint2-deliverables.yml` | GitHub Actions workflow for Blender 4.5.1, KTX-Software 4.4.2, GLB/FBX gates, artifact upload, and PR comment. |
| `Makefile` | `make sprint2-demo`, `make sprint2-demo-local`, `make sprint2-ci`. |

## Golden Output

CI golden output path:

`ai-architect-api/storage/professional-deliverables/project-golden-townhouse/`

Generated in the canonical bundle layout:

- `3d/model.glb`
- `3d/model.fbx`
- `3d/sprint2_model_metadata.json`
- `3d/gltf-validator-report.json`
- `3d/fbx-import-report.json`
- `3d/sprint2_gate_summary.json`
- `3d/sprint2_gate_summary.md`
- `textures/*.ktx2` — 45 KTX2 textures: 9 materials x 5 PRD texture slots.

Sprint 1 `/2d/` output remains unchanged. USDZ, video, derivatives, and final `manifest.json` remain out of scope for Sprint 2.

## CI Gate Results

Evidence:

- PR: https://github.com/blackbirdzzzz365-gif/ai-architect-api/pull/2
- Sprint 2 workflow run: https://github.com/blackbirdzzzz365-gif/ai-architect-api/actions/runs/24969040278
- Sprint 2 job: https://github.com/blackbirdzzzz365-gif/ai-architect-api/actions/runs/24969040278/job/73108727838
- Sticky PR gate comment: https://github.com/blackbirdzzzz365-gif/ai-architect-api/pull/2#issuecomment-4323187128

| Gate | Status | Evidence |
|---|---|---|
| `model.glb` passes Khronos glTF Validator with 0 errors | Pass | CI gate summary: `errors=0, warnings=0, infos=177`. |
| Metal-Rough only; no Specular-Glossiness | Pass | CI gate summary: `9 materials use pbrMetallicRoughness only`. |
| MetallicRoughness packed correctly | Pass | CI sampled all 9 material MR textures: `R=unused, G=rough, B=metal`. |
| `model.fbx` Blender import, materials, Z-up, cm units | Pass | CI import check: `40 meshes, 9 materials, extents_cm=[620.0, 1620.0, 679.0], UV0 0-1`. |
| USDZ size budget | Skipped | Expected Sprint 2 skip. Sprint 3 owns USDZ export and size budget. |
| Texture-resolution policy | Pass | CI summary: hero/default textures satisfy policy, no texture exceeds 4K, final `/textures/` contains KTX2 only, and all KTX2 files pass KTX validation. |

Companion Sprint 1 workflow also passed on the same PR:

- Sprint 1 run: https://github.com/blackbirdzzzz365-gif/ai-architect-api/actions/runs/24969040277

## Verification Commands Run

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest
```

Result:

- Full backend suite: `38 passed, 19 warnings`

Local GLB/KTX verification with KTX-Software 4.4.2 extracted from the official Darwin arm64 package:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
KTX_BIN=/tmp/ktx-mac/expanded/KTX-Software-4.4.2-Darwin-arm64-tools.pkg/Payload/usr/local/bin/ktx \
  PYTHONPATH=. .venv/bin/python -m app.services.professional_deliverables.sprint2_demo --allow-missing-external-tools
```

Result:

- GLB/KTX gates passed locally.
- FBX export/import gates skipped locally because Blender is absent on this macOS workspace.

CI hard verification:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make sprint2-ci
```

Result on `ubuntu-latest`:

- `sprint2-3d-gates` passed in GitHub Actions run `24969040278`.

## Reproducible Demo Command

Full Sprint 2 DoD demo with hard GLB/FBX/KTX gates:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
export BLENDER_BIN=/opt/blender/blender
export KTX_BIN=/usr/bin/ktx
export GLTF_TRANSFORM_BIN=/path/to/tools/sprint2/node_modules/.bin/gltf-transform
make sprint2-demo
```

Developer/local demo when Blender or KTX is not installed:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make sprint2-demo-local
```

## Known Issues / Follow-up

- The official npm `gltf-validator@2.0.0-dev.3.10` reports BasisU KTX2 image decoding as `IMAGE_UNRECOGNIZED_FORMAT`. The wrapper demotes only that issue to info, while the pipeline validates every final KTX2 file with KTX-Software `ktx validate`. The GLB gate still fails on any validator error or non-allowed warning.
- `KHR_draco_mesh_compression`, `KHR_texture_basisu`, and `URI_GLB` appear as validator infos; they are not errors or warnings.
- GitHub Actions emits a Node.js 20 deprecation annotation for upstream actions. This is non-blocking and unrelated to Sprint 2 deliverable correctness.
- No USDZ, video, hero still, GIF, final `manifest.json`, IFC, Pascal Editor integration, Spec-Glossiness, or procedural materials were implemented.
