---
title: Sprint 3 Plan — AR + Cinematic Master Video
phase: 2
status: pending-pm-architect-acceptance
date: 2026-04-27
owner: Dev/Test Agent
track: Professional Deliverables
depends_on:
  - docs/phase-2/sprint-reports/sprint-2.md
---

# Sprint 3 Plan — AR + Cinematic Master Video

No production implementation starts until the PO relays PM/Architect acceptance of this plan.

## Context Ingestion

Sprint 2 is formally accepted. The sign-off block in `docs/phase-2/sprint-reports/sprint-2.md` confirms the GLB/FBX/KTX2 foundation is green, including:

- `model.glb` passes Khronos glTF Validator with `errors=0, warnings=0`.
- Materials are Metal-Rough only; `KHR_materials_pbrSpecularGlossiness` is rejected.
- Final `/textures/` is KTX2-only and KTX-validated.
- USDZ was intentionally skipped and is now Sprint 3 scope.

Locked constraints carried into Sprint 3:

- USDZ is derived from Sprint 2 `model.glb`; do not re-author 3D from scratch.
- AR delivery follows ADR-001 Apple AR Quick Look constraints: `model.usdz` <= 8 MB, <= 200,000 triangles, textures <= 2K, 1 unit = 1 meter, pivot at floor center.
- Master video is exactly the Sprint 3 video deliverable: `master_4k.mp4`, 3840x2160, 30 fps, H.264, 60s +/- 2s.
- Reel, hero still, GIF, final `manifest.json`, IFC, Pascal Editor, procedural materials, and Spec-Glossiness remain out of scope.

## Safety Invariants

- No Sprint 3 code may introduce Specular-Glossiness or procedural material generation.
- USDZ material names must match GLB material names exactly.
- USDZ `model.usdz` must be the mobile-safe delivery artifact. If a richer full file is emitted, it is additive as `model_full.usdz`; default `model.usdz` is a copy of the budget-compliant lite variant.
- CI must fail if USDZ or video gates fail; no partial Sprint 3 bundle is marked releasable.
- Heavy production video rendering remains async-first through Celery. Demo CLI may run synchronously for developer convenience.
- Audio is omitted in Sprint 3.

## Chosen USDZ Converter

Chosen path: **USD-from-Blender via Blender 4.5.1 USD export, with OpenUSD Python packaging/validation**.

Rationale:

- Blender 4.5.1 is already installed and proven in Sprint 2 CI for FBX export/import on `ubuntu-latest`.
- The source remains Sprint 2 `model.glb`: Sprint 3 imports GLB, preserves object/material names, and exports USD geometry from that imported asset.
- Apple's Reality Converter is macOS-only and cannot satisfy Linux CI.
- Google's `usd_from_gltf` adds a second conversion toolchain and build surface; Blender + OpenUSD keeps the path under tools already needed for Sprint 2/3.
- OpenUSD provides the ARKit-oriented USDZ packaging and compliance APIs directly through `usd-core`.

Planned flow:

1. Ensure Sprint 2 golden outputs exist by invoking the Sprint 2 generator when needed.
2. Validate `3d/model.glb` before deriving USDZ.
3. Use Blender 4.5.1 headless to import `model.glb` and export an intermediate geometry USD/USDC stage.
4. Decode Sprint 2 KTX2 textures with KTX-Software:
   - `baseColor`, `normal`, `ao`, and `emissive` become PNG payload textures.
   - `metallicRoughness` is split into two linear grayscale PNGs: B -> metallic, G -> roughness.
   - Lite payload is capped at 1K; full payload, if emitted, is capped at 2K.
5. Post-process the USD stage with `usd-core==26.5`:
   - create one `UsdShade.Material` per GLB material name;
   - use `UsdPreviewSurface`;
   - bind diffuseColor, metallic, roughness, normal, occlusion, and emissiveColor inputs;
   - anchor texture asset paths inside the package.
6. Package via `UsdUtils.CreateNewARKitUsdzPackage`, then run `UsdUtils.ComplianceChecker(arkit=True)`.
7. Copy `model_lite.usdz` to `model.usdz`. Emit `model_full.usdz` only when the full conversion is requested or when fallback reporting needs it.

OpenUSD references used for planning:

- USDZ packages are uncompressed zip archives with USD/image payload constraints and a default layer first.
- `usdzip`/OpenUSD packaging can localize referenced assets for ARKit-oriented USDZ packages.
- `usdchecker --arkit` has stricter ARKit/web-compliance rules; the Python `ComplianceChecker(arkit=True)` mirrors that validation class.

## Chosen Video Render Path

Chosen path: **Blender 4.5.1 render pipeline, with fast CI profile and production GPU profile**.

Rejected for Sprint 3:

- Twinmotion 2024.1+ headless: better visual target, but licensing/headless automation is not yet proven on GitHub-hosted Linux.
- Lumion 2024 CLI: Windows/commercial workflow and not a good fit for `ubuntu-latest`.

Decision:

- Sprint 3 uses **option 1** from the render budget note: CI uses a fast deterministic profile; production uses an async GPU profile.
- CI still produces an actual `master_4k.mp4` at 3840x2160, 30 fps, H.264, 58-62 seconds. Visual quality is intentionally reduced; format/pipeline correctness is the gate.
- Production preset uses Blender Cycles GPU where available; CI preset uses Blender's fast deterministic renderer profile with simplified lighting/materials and fixed encode settings.

Profiles:

| Profile | Purpose | Renderer | Output |
|---|---|---|---|
| `CI_FAST_4K` | GitHub Actions gate | Blender fast viewport/Eevee-style render, low samples, deterministic seed, no audio | 3840x2160, 30 fps, H.264, 60s |
| `PRODUCTION_4K_CYCLES_GPU` | Async production render | Blender Cycles GPU, higher samples, tropical daylight | 3840x2160, 30 fps, H.264, 60s |

Encode path:

- Render deterministic image sequence from Blender.
- Encode with `ffmpeg`/`libx264`, fixed CRF/preset, `-pix_fmt yuv420p`, `-r 30`, `-threads 1` for deterministic sample-frame hashes.
- Verify with `ffprobe` JSON output.

## Camera Path Generation

Camera paths are generated from the Sprint 2 scene contract and metadata, not hand-authored.

Inputs:

- `SceneContract.elements`
- lot width/depth from the golden project geometry
- floor/storey extents derived from element bounding boxes
- room-like anchors inferred from element/category distribution

Golden fixture anchor strategy:

| Time | Segment | Anchor derivation |
|---|---|---|
| 0:00-0:15 | Exterior approach | Start in front of lot center, elevated drone-style; look at building center/roofline. |
| 0:15-0:28 | `Phòng khách` | Floor 1, front-third anchor, eye height 1.55 m. |
| 0:28-0:42 | `Bếp và ăn` | Floor 1, rear-half fixture/kitchen zone anchor. |
| 0:42-0:50 | `Phòng ngủ chính` | Floor 2, rear-half bedroom anchor. |
| 0:50-1:00 | Exterior closing | Pull out to front corner orbit, look at whole building mass. |

Implementation details:

- Use cubic easing between keyframes.
- Keep camera target and focal length deterministic.
- Clamp camera inside walkable interior bounds and avoid structural walls by using simple offset rules from the footprint.
- Store the resolved camera path as `video/camera_path.json` for audit/debug, but do not include it in final `manifest.json` during Sprint 3.
- No in-video text overlays.

## Module Structure

Extend `ai-architect-api/app/services/professional_deliverables/`:

```text
app/services/professional_deliverables/
  usdz_converter.py              # GLB -> USDZ orchestration, lite/full policy
  usdz_materials.py              # glTF Metal-Rough -> UsdPreviewSurface mapping
  usdz_texture_payload.py        # KTX2 extraction, 1K/2K resize, MR channel split
  usdz_budget.py                 # size, triangle, texture-resolution budgets
  usdz_validators.py             # USDZ zip/material/parity/compliance gates
  camera_path.py                 # deterministic path from SceneContract
  video_renderer.py              # Blender/ffmpeg orchestration and profiles
  video_validators.py            # ffprobe, black-frame, decoder, determinism gates
  sprint3_demo.py                # golden USDZ + master video generation
  blender_scripts/
    export_usd_from_glb.py       # import Sprint 2 GLB, decimate, export USD geometry
    render_master_video.py       # deterministic Blender render from scene + camera path
```

Extend task entrypoints:

```text
app/tasks/professional_deliverables.py
  run_sprint3_golden_ar_video_bundle_task(...)
```

Tests:

```text
tests/professional_deliverables/
  test_sprint3_usdz_converter.py
  test_sprint3_usdz_materials.py
  test_sprint3_usdz_budget.py
  test_sprint3_video_renderer.py
  test_sprint3_video_validators.py
  test_sprint3_bundle_layout.py
```

CI and tools:

```text
.github/workflows/sprint3-deliverables.yml
tools/sprint3/README.md
```

Make targets:

```text
make sprint3-demo-local
make sprint3-demo
make sprint3-ci
```

## Libraries and Versions

| Purpose | Tool | Version / pin | Notes |
|---|---|---|---|
| GLB import, USD export, video render | Blender LTS | `4.5.1` Linux x64 tarball | Reuse Sprint 2 install path. |
| USD authoring/package/compliance | `usd-core` | `26.5` | Python `pxr` APIs: `Usd`, `UsdShade`, `UsdGeom`, `UsdUtils`. |
| KTX2 decode/validation | KTX-Software | `4.4.2` | Reuse Sprint 2 `KTX_BIN=ktx`. |
| GLB inspection | `@gltf-transform/cli` | `4.3.0` | Reuse Sprint 2 Node tooling where useful. |
| Texture resize/split | Pillow | `12.2.0` | Existing local version; pin if not already pinned in API deps. |
| Video encode/probe | FFmpeg / ffprobe | Ubuntu package in CI, version logged | Use `ffprobe` machine-readable JSON and `ffmpeg` decoder/hash checks. |
| Test runner | pytest | existing backend pin | Focused unit + gate tests. |

## Bundle Output

Sprint 3 extends the existing canonical bundle:

```text
storage/professional-deliverables/project-golden-townhouse/
  /2d/          # unchanged Sprint 1 outputs
  /3d/
    model.glb
    model.fbx
    model.usdz
    model_lite.usdz
    sprint2_model_metadata.json
  /video/
    master_4k.mp4
    camera_path.json
  /textures/    # unchanged Sprint 2 KTX2 textures
  sprint3_gate_summary.json
  sprint3_gate_summary.md
```

`model_full.usdz` is optional and emitted only when useful. Reel, derivatives, and `manifest.json` are not emitted in Sprint 3.

## Test Plan Per CI Gate

| Gate | Test implementation |
|---|---|
| USDZ size budget | Use Python file stat for <= 8 MB; open USDZ via `Usd.Stage.Open`; count triangles from `UsdGeom.Mesh` face vertex counts; fail if > 200,000. |
| USDZ structural integrity | Verify package can be inspected/extracted with OpenUSD APIs; assert default layer opens; assert referenced texture assets resolve inside package; run `UsdUtils.ComplianceChecker(arkit=True)`. |
| USDZ material parity | Parse GLB JSON material list; parse USD materials; assert exact name set match and each has `UsdPreviewSurface` inputs for diffuseColor, metallic, roughness, normal, occlusion, emissiveColor. |
| USDZ texture budget | Inspect embedded payload textures with Pillow after extraction; assert lite textures <= 1K, no payload texture > 2K. |
| Master video format | `ffprobe` JSON: width 3840, height 2160, codec `h264`, fps 30.000 +/- 0.001, duration in [58.0, 62.0]. |
| Master video integrity | `ffmpeg -v error -i master_4k.mp4 -f null -` must return 0; size <= 200 MB; sample first and last second frames and fail if all-black/near-zero variance. |
| Camera path determinism | Render CI fast profile twice; compare duration and decoded frame hashes at t=0, t=30s, t=58s. |
| Failure case | Empty/degenerate Sprint 2 scene must fail validation before writing releasable `model.usdz` or `master_4k.mp4`; unit test asserts failed gate state. |

## CI Plan

Workflow: `.github/workflows/sprint3-deliverables.yml`

Steps:

1. Checkout PR branch.
2. Install Python dependencies plus `usd-core==26.5`.
3. Install Node Sprint 2 tools if GLB inspection is needed.
4. Install Blender 4.5.1 LTS.
5. Install KTX-Software 4.4.2.
6. Install `ffmpeg`.
7. Run focused Sprint 1/2/3 professional deliverables tests.
8. Run `make sprint3-ci`.
9. Upload `sprint3_gate_summary.{json,md}`, USDZ reports, video ffprobe report, determinism report.
10. Post sticky Sprint 3 PR comment using the existing gate summary format.

Expected CI behavior:

- CI renders the 4K master with the fast deterministic profile.
- Production async jobs use the GPU/Cycles preset.
- If CI render time threatens GitHub's limit, reduce renderer samples/material preview complexity first. Do not reduce the final CI video format below 4K@30 for the gate artifact.

## Implementation Slices

1. **USDZ derivation and budgets**
   - Contracts: `usdz_converter.py`, `usdz_budget.py`, `usdz_validators.py`.
   - Tests: budget, package open, material parity, degenerate scene failure.

2. **USD material/texture payload**
   - Contracts: `usdz_materials.py`, `usdz_texture_payload.py`.
   - Tests: MR channel split, texture caps, material slot completeness.

3. **Camera path and render profiles**
   - Contracts: `camera_path.py`, `video_renderer.py`, Blender render script.
   - Tests: camera anchor order, deterministic keyframes, profile config.

4. **Video gates and CI workflow**
   - Contracts: `video_validators.py`, `sprint3_demo.py`, Make targets, workflow.
   - Tests: ffprobe parser, black-frame detector, frame hash comparison.

## Clarification Questions

None blocking before implementation.

Assumption to be reviewed during plan acceptance:

- CI fast profile is acceptable for Sprint 3 visual-quality scope as long as the generated `master_4k.mp4` still satisfies the 4K/30fps/H.264/duration/integrity/determinism gates. Production quality remains the async GPU/Cycles preset.
