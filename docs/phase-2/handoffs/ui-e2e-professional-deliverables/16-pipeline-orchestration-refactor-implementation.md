---
title: Professional Deliverables Pipeline Orchestration Refactor Implementation
phase: 2
status: ready-for-implementation
date: 2026-04-28
owner: Codex Coordinator
related_files:
  - 10-remediation-implementation-contract.md
  - 11-remediation-execution-playbook.md
  - 15-current-artifact-generation-order-and-inputs.md
---

# Professional Deliverables Pipeline Orchestration Refactor Implementation

This document gives the detailed implementation plan to fix the current orchestration defect before starting artifact quality optimization.

Problem to fix:

```text
Current code has removed Sprint 4 from the product path, but Sprint 3 still regenerates Sprint 2 internally.
That means GLB/FBX/textures can be produced twice.
The task also marks export_usdz before USDZ is actually generated, because USDZ generation currently happens inside Sprint 3 after the task has already moved to render_video.
```

This is an orchestration correctness fix, not a visual quality uplift. Do this before improving PDF/DXF/GLB/video quality.

## 1. Objective

Refactor the professional deliverables product path so the generation order is true, single-pass, and stage-aligned:

```text
adapter
-> export_2d
-> export_3d
-> export_usdz
-> render_video
-> validate
-> ready
```

Expected properties:

- Sprint 2 3D outputs are generated exactly once in the product task.
- USDZ generation consumes the existing Sprint 2 GLB/textures/scene.
- Video generation consumes the existing Sprint 2 GLB/scene.
- `export_usdz` stage means USDZ is actually being generated.
- `render_video` stage means camera path and MP4 are actually being generated.
- Golden public functions still work.
- Sprint 1-3 golden parity remains intact.
- No Sprint 4 product outputs are reintroduced.

Implementation invariants:

- Product orchestration owns stage transitions. Generator helpers must not silently advance product job stages.
- Product orchestration owns asset registration. Generator helpers may write files and reports, but DB asset readiness must remain in the task/orchestrator layer.
- A file must not be registered as ready before the stage that creates and validates it has completed.
- Stage names must describe active work, not future work already completed elsewhere.
- The product path must use the selected `DesignVersion.geometry_json` through `DrawingProject`; it must not fall back to golden data.
- Golden fixture functions must stay backward-compatible because they protect Sprint 1-3 parity.

Core contracts:

- `DrawingProject`: canonical 2D/3D semantic input for professional deliverables.
- `SceneContract`: canonical 3D scene representation derived from `DrawingProject`.
- `Sprint2BundleResult`: owns existing GLB, FBX, and texture outputs.
- `USDZStageResult`: owns USDZ outputs and USDZ-specific gate reports.
- `VideoStageResult`: owns camera path, MP4, and video-specific gate reports.
- `Sprint3BundleResult`: remains the compatibility summary for Sprint 3/golden callers.

Execution model:

- Build `DrawingProject` once from the selected version.
- Build `SceneContract` once from that `DrawingProject`.
- Generate 2D, 3D, USDZ, and video in a single forward pass.
- Validate and register artifacts after their owning stage finishes.
- Preserve partial artifact evidence if a later stage fails.

## 2. Current Code Problem

Current top-level task:

`app/tasks/professional_deliverables.py::run_professional_deliverable_bundle_task`

Current simplified flow:

```text
drawing_project = geometry_to_drawing_project(...)

sprint1 = generate_project_2d_bundle(...)

sprint2 = generate_project_3d_bundle(...)
register GLB/FBX

mark export_usdz
mark render_video

sprint3 = generate_project_ar_video_bundle(...)
```

But current `generate_project_ar_video_bundle(...)` in:

`app/services/professional_deliverables/sprint3_demo.py`

does this internally:

```text
sprint2 = generate_project_3d_bundle(...)
scene = build_scene_from_project(project)
export USDZ
render MP4
write sprint3 gates
```

So the task calls Sprint 2 once directly, then Sprint 3 calls Sprint 2 again.

## 3. Target Architecture

Split Sprint 3 into reusable stage helpers:

```text
Sprint 2:
  generate_project_3d_bundle(...)
    -> Sprint2BundleResult
    -> scene
    -> glb_path
    -> fbx_path
    -> textures_dir

Sprint 3 split helpers:
  export_project_usdz_stage(...)
    -> USDZStageResult

  render_project_video_stage(...)
    -> VideoStageResult

  write_project_sprint3_gate_summary(...)
    -> Sprint3SummaryResult
```

Then the product task calls:

```text
scene = build_scene_from_project(drawing_project)

sprint2 = generate_project_3d_bundle(..., scene=scene)

mark export_usdz
usdz = export_project_usdz_stage(scene=scene, glb_path=sprint2.glb_path, textures_dir=sprint2.textures_dir, ...)

mark render_video
video = render_project_video_stage(scene=scene, glb_path=sprint2.glb_path, ...)

sprint3 = write_project_sprint3_gate_summary(usdz.gates + video.gates, ...)
```

The old `generate_project_ar_video_bundle(...)` should remain as a compatibility wrapper for golden commands/tests, but product code must not use the wrapper if the wrapper regenerates Sprint 2.

## 4. Files To Change

API:

- `app/services/professional_deliverables/sprint2_demo.py`
- `app/services/professional_deliverables/sprint3_demo.py`
- `app/tasks/professional_deliverables.py`
- `tests/professional_deliverables/test_product_e2e_bridge.py`
- `tests/professional_deliverables/test_sprint3_camera_and_video.py`
- possibly `tests/professional_deliverables/test_sprint3_usdz.py`

Do not change for this refactor unless necessary:

- `pdf_generator.py`
- `dxf_exporter.py`
- `scene_builder.py` quality logic
- `video_renderer.py` visual quality logic
- Web UI files

This refactor is about orchestration and test coverage only.

## 5. Step-by-step Implementation

## Step 1 - Make Sprint 2 accept a prebuilt scene

File:

`app/services/professional_deliverables/sprint2_demo.py`

Current function:

```python
def generate_project_3d_bundle(
    project: DrawingProject,
    output_root: Path,
    *,
    require_external_tools: bool | None = None,
    project_dir: Path | None = None,
) -> Sprint2BundleResult:
    ...
    scene = build_scene_from_project(project)
```

Change to:

```python
def generate_project_3d_bundle(
    project: DrawingProject,
    output_root: Path,
    *,
    require_external_tools: bool | None = None,
    project_dir: Path | None = None,
    scene: SceneContract | None = None,
) -> Sprint2BundleResult:
    ...
    scene = scene or build_scene_from_project(project)
```

Requirements:

- Preserve the existing positional arguments.
- Add `scene` as keyword-only optional arg.
- Do not change `generate_golden_3d_bundle(...)` behavior.
- Do not change returned `Sprint2BundleResult` shape unless necessary.

Reason:

The product task can build the scene once and pass it forward.

## Step 2 - Add split result dataclasses in sprint3_demo.py

File:

`app/services/professional_deliverables/sprint3_demo.py`

Add dataclasses:

```python
@dataclass(frozen=True)
class USDZStageResult:
    project_dir: Path
    three_d_dir: Path
    usdz_path: Path
    gate_results: tuple[GateResult, ...]
    inventory_paths: tuple[Path, ...]

@dataclass(frozen=True)
class VideoStageResult:
    project_dir: Path
    video_dir: Path
    master_video_path: Path
    camera_path_json: Path
    gate_results: tuple[GateResult, ...]
    inventory_paths: tuple[Path, ...]

@dataclass(frozen=True)
class Sprint3SummaryResult:
    project_dir: Path
    three_d_dir: Path
    video_dir: Path
    usdz_path: Path
    master_video_path: Path
    gate_results: tuple[GateResult, ...]
    gate_summary_json: Path
    gate_summary_md: Path
```

Keep existing `Sprint3BundleResult` if tests/public API depend on it. Either:

- keep it and map `Sprint3SummaryResult` into it, or
- replace only if all tests are updated safely.

Recommended: keep `Sprint3BundleResult` for compatibility.

## Step 3 - Extract USDZ generation helper

File:

`app/services/professional_deliverables/sprint3_demo.py`

Add:

```python
def export_project_usdz_stage(
    *,
    scene: SceneContract,
    glb_path: Path,
    textures_dir: Path,
    three_d_dir: Path,
    project_dir: Path,
    require_external_tools: bool,
) -> USDZStageResult:
    ...
```

Move this logic out of `generate_project_ar_video_bundle(...)`:

- discover KTX tool
- call `export_usdz_from_glb(...)`
- run USDZ validators:
  - `validate_usdz_size_budget`
  - `validate_usdz_structural_integrity`
  - `validate_usdz_material_parity`
  - `validate_usdz_texture_payload`

Input:

- existing `scene`
- existing `glb_path`
- existing `textures_dir`
- existing `three_d_dir`
- `project_dir`
- `require_external_tools`

Output:

- `USDZStageResult`

Do not:

- call `generate_project_3d_bundle(...)`
- rebuild scene
- render video
- write Sprint 3 summary yet

Expected inventory paths:

- `3d/model.glb`
- `3d/model.fbx`
- `3d/model.usdz`
- `3d/model_lite.usdz`
- `3d/model_lite.usd`
- `3d/usdz-budget-report.json`
- `3d/usdz-structural-report.json`
- `3d/usdz-material-parity-report.json`
- `3d/usdz-texture-report.json`

## Step 4 - Extract video generation helper

File:

`app/services/professional_deliverables/sprint3_demo.py`

Add:

```python
def render_project_video_stage(
    *,
    scene: SceneContract,
    glb_path: Path,
    project_dir: Path,
    video_dir: Path,
    require_external_tools: bool,
) -> VideoStageResult:
    ...
```

Move this logic out of `generate_project_ar_video_bundle(...)`:

- build camera path
- check collision warnings
- call `render_master_video(...)`
- render second video for determinism
- run video validators:
  - `validate_master_video_format`
  - `validate_master_video_integrity`
  - `validate_camera_path_determinism`

Input:

- existing `scene`
- existing `glb_path`
- `project_dir`
- `video_dir`
- `require_external_tools`

Output:

- `VideoStageResult`

Do not:

- generate GLB/FBX/textures
- generate USDZ
- write Sprint 3 summary yet

Expected inventory paths:

- `video/master_4k.mp4`
- `video/camera_path.json`
- `video/render_stills_report.json`
- `video/ffprobe-master-report.json`
- `video/video-integrity-report.json`
- `video/video-determinism-report.json`

Camera behavior:

- If `camera_path.collision_warnings` and `require_external_tools=True`, raise `VideoRenderError("CAMERA_PATH_UNSAFE: ...")` before expensive render.
- If tools are optional, keep current skipped/fail gate behavior.

## Step 5 - Add Sprint 3 summary writer helper

File:

`app/services/professional_deliverables/sprint3_demo.py`

Add:

```python
def write_project_sprint3_summary(
    *,
    project_dir: Path,
    three_d_dir: Path,
    video_dir: Path,
    usdz_result: USDZStageResult,
    video_result: VideoStageResult,
) -> Sprint3BundleResult:
    ...
```

Responsibilities:

- combine `usdz_result.gate_results + video_result.gate_results`
- combine inventory paths from both stages
- call `build_file_inventory(...)`
- call `write_gate_outputs(...)`
- return a `Sprint3BundleResult` compatible object:
  - `project_dir`
  - `three_d_dir`
  - `video_dir`
  - `usdz_path`
  - `master_video_path`
  - `gate_results`
  - `gate_summary_json`
  - `gate_summary_md`

Do not:

- generate files
- call external tools

## Step 6 - Rewrite generate_project_ar_video_bundle as wrapper

File:

`app/services/professional_deliverables/sprint3_demo.py`

The public function should remain:

```python
def generate_project_ar_video_bundle(
    project: DrawingProject,
    output_root: Path,
    *,
    require_external_tools: bool | None = None,
    project_dir: Path | None = None,
) -> Sprint3BundleResult:
```

But implement it using the new helpers:

```python
if require_external_tools is None:
    require_external_tools = bool(os.environ.get("CI"))

scene = build_scene_from_project(project)
sprint2 = generate_project_3d_bundle(
    project,
    output_root,
    require_external_tools=require_external_tools,
    project_dir=project_dir,
    scene=scene,
)
video_dir = sprint2.project_dir / "video"
_clean_dir(video_dir)

usdz_result = export_project_usdz_stage(
    scene=scene,
    glb_path=sprint2.glb_path,
    textures_dir=sprint2.textures_dir,
    three_d_dir=sprint2.three_d_dir,
    project_dir=sprint2.project_dir,
    require_external_tools=require_external_tools,
)

video_result = render_project_video_stage(
    scene=scene,
    glb_path=sprint2.glb_path,
    project_dir=sprint2.project_dir,
    video_dir=video_dir,
    require_external_tools=require_external_tools,
)

return write_project_sprint3_summary(...)
```

This wrapper may still generate Sprint 2 because it is a standalone Sprint 3/golden function. That is acceptable.

Important:

- The product task must not call this wrapper anymore.
- Golden commands can still call it.

## Step 7 - Rewrite product task to use split helpers

File:

`app/tasks/professional_deliverables.py`

Imports:

```python
from app.services.professional_deliverables.scene_builder import build_scene_from_project
from app.services.professional_deliverables.sprint3_demo import (
    export_project_usdz_stage,
    render_project_video_stage,
    write_project_sprint3_summary,
)
```

Remove product-path use of:

```python
generate_project_ar_video_bundle(...)
```

New product task flow:

```python
drawing_project = geometry_to_drawing_project(...)
scene = build_scene_from_project(drawing_project)

mark export_2d
sprint1 = generate_project_2d_bundle(...)
register sprint1

mark export_3d
sprint2 = generate_project_3d_bundle(
    drawing_project,
    root.parent.parent.parent,
    require_external_tools=True,
    project_dir=root,
    scene=scene,
)
register sprint2

mark export_usdz
usdz_result = export_project_usdz_stage(
    scene=scene,
    glb_path=sprint2.glb_path,
    textures_dir=sprint2.textures_dir,
    three_d_dir=sprint2.three_d_dir,
    project_dir=root,
    require_external_tools=True,
)

mark render_video
video_result = render_project_video_stage(
    scene=scene,
    glb_path=sprint2.glb_path,
    project_dir=root,
    video_dir=root / "video",
    require_external_tools=True,
)

sprint3 = write_project_sprint3_summary(
    project_dir=root,
    three_d_dir=sprint2.three_d_dir,
    video_dir=video_result.video_dir,
    usdz_result=usdz_result,
    video_result=video_result,
)

_validate_master_video_boundary(root, sprint3)
register sprint3

mark validate
quality_status, degraded_reasons = _validate_product_outputs(root, sprint1, sprint2, sprint3)
...
```

Expected behavior:

- `3d/model.glb` is generated once.
- `3d/model.fbx` is generated once.
- `textures/*.ktx2` are generated once.
- `3d/model.usdz` is generated during `export_usdz`.
- `video/master_4k.mp4` is generated during `render_video`.

## Step 8 - Prevent accidental second Sprint 2 in product tests

Add a focused test in:

`tests/professional_deliverables/test_product_e2e_bridge.py`

Test name:

```python
def test_product_task_generates_sprint2_only_once_and_uses_split_sprint3_stages(...):
```

Test intent:

- monkeypatch `generate_project_3d_bundle` to count calls.
- monkeypatch split helpers to create expected fake files.
- run product task.
- assert `generate_project_3d_bundle` call count is exactly 1.
- assert `export_project_usdz_stage` was called after Sprint 2.
- assert `render_project_video_stage` was called after USDZ.
- assert product job reaches ready with expected artifacts.

Simpler if direct order assertions are hard:

- Use a `calls: list[str]`.
- Each monkeypatched function appends:
  - `2d`
  - `3d`
  - `usdz`
  - `video`
  - `summary`
- Assert:

```python
assert calls == ["2d", "3d", "usdz", "video", "summary"]
```

## Step 9 - Add stage alignment test

Add or update a test that verifies stage/progress order.

Recommended helper:

- monkeypatch `mark_job_stage` or inspect persisted job after each fake step if possible.

Expected stage order:

```python
["adapter", "export_2d", "export_3d", "export_usdz", "render_video", "validate"]
```

Expected progress:

```python
[10, 25, 50, 65, 85, 95]
```

Do not expect `ready` through `mark_job_stage`; success is set by `mark_job_succeeded`.

## Step 10 - Add no-overwrite/checksum test

Test:

```python
def test_product_task_does_not_overwrite_glb_after_export_3d(...):
```

Intent:

- fake Sprint 2 writes `3d/model.glb` with deterministic contents.
- fake USDZ/video helpers read GLB but do not rewrite it.
- after task, assert GLB checksum is unchanged.

This catches regressions where Sprint 3 regenerates Sprint 2 or cleans `3d/`.

## Step 11 - Preserve golden compatibility

Run existing focused tests:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_sprint3_camera_and_video.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_sprint3_usdz.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_product_e2e_bridge.py
```

Then:

```bash
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
make sprint3-ci-linux
```

Golden behavior must remain:

- `generate_golden_bundle`
- `generate_golden_3d_bundle`
- `generate_golden_ar_video_bundle`

## 6. Expected Final Product Flow After Refactor

After implementation, product task should behave like:

```text
adapter 10
  input: Project.brief_json + DesignVersion.geometry_json
  output: DrawingProject + SceneContract

export_2d 25
  input: DrawingProject
  output: PDF, DXF, DWG/skipped, Sprint 1 summaries

export_3d 50
  input: DrawingProject + SceneContract
  output: GLB, FBX, textures, Sprint 2 summaries

export_usdz 65
  input: SceneContract + existing GLB + existing textures
  output: USDZ, USDZ reports

render_video 85
  input: SceneContract + existing GLB
  output: camera_path.json, render_stills_report.json, master_4k.mp4, video reports

validate 95
  input: Sprint 1 + Sprint 2 + USDZ + Video gate results
  output: final bundle status and asset readiness

ready 100
```

## 7. What Not To Do

Do not solve this by:

- only moving `mark_job_stage(...)` calls around while Sprint 3 still regenerates Sprint 2.
- letting `generate_project_ar_video_bundle(...)` stay in the product task.
- registering GLB/FBX assets before a later step can delete/overwrite them.
- making `export_usdz` stage include video rendering.
- making `render_video` stage include USDZ generation.
- weakening tests or validators to hide duplicated generation.
- removing `generate_golden_ar_video_bundle(...)`.

## 8. Pass Criteria

This refactor is complete only when:

- Product task uses split Sprint 3 helpers.
- Product task does not call `generate_project_ar_video_bundle(...)`.
- Product task generates Sprint 2 exactly once.
- Stage `export_usdz` corresponds to USDZ generation.
- Stage `render_video` corresponds to MP4 generation.
- GLB/FBX/textures are not deleted or overwritten after `export_3d`.
- Existing Sprint 1-3 golden commands/tests still pass.
- No Sprint 4 product outputs are created.

## 9. Report Section To Add

When reporting this refactor, include:

```text
Pipeline orchestration refactor:
- Product task calls generate_project_3d_bundle exactly once:
- Product task uses split USDZ helper:
- Product task uses split video helper:
- export_usdz stage verified:
- render_video stage verified:
- GLB checksum preserved after video step:
- Golden generate_golden_ar_video_bundle preserved:
- Tests added:
- Tests run:
```
