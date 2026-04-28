---
title: Pipeline Orchestration Refactor - Agent Prompt
phase: 2
status: ready-to-copy
date: 2026-04-28
owner: Codex Coordinator
related_files:
  - 10-remediation-implementation-contract.md
  - 11-remediation-execution-playbook.md
  - 15-current-artifact-generation-order-and-inputs.md
  - 16-pipeline-orchestration-refactor-implementation.md
---

# Pipeline Orchestration Refactor Agent Prompt

Copy and send the following prompt to the implementation/testing agent responsible for this narrow pipeline fix.

```text
You are the Implementation and Verification Agent for the AI Architect Phase 2 Professional Deliverables pipeline orchestration refactor.

Your job is to fix one specific backend orchestration defect before any artifact quality optimization work begins:

1. Current product path has removed Sprint 4, but Sprint 3 still regenerates Sprint 2 internally.
2. As a result, GLB, FBX, and textures can be generated twice.
3. The product task marks export_usdz before USDZ is actually generated.
4. USDZ is currently generated inside the Sprint 3 wrapper after the task has already advanced to render_video.

This is an orchestration correctness task only. Do not redesign artifact quality, PDF/DXF layout, 3D visual quality, UI/UX, or product strategy in this task.

Work from the shared project root:

cd /Users/nguyenquocthong/project/ai-architect

Repos:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Docs/compose repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Read these documents first, in this order:

1. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/03-adr-001-standards-combo.md
2. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/05-prd-deliverables.md
3. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md
4. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/10-remediation-implementation-contract.md
5. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/11-remediation-execution-playbook.md
6. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/15-current-artifact-generation-order-and-inputs.md
7. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/16-pipeline-orchestration-refactor-implementation.md

Primary objective:

Refactor the professional deliverables product path so generation is true, single-pass, and stage-aligned:

adapter
-> export_2d
-> export_3d
-> export_usdz
-> render_video
-> validate
-> ready

Success means:

- Sprint 2 3D outputs are generated exactly once in the product task.
- GLB, FBX, and textures are produced during export_3d only.
- USDZ is produced during export_usdz only.
- camera_path.json and master_4k.mp4 are produced during render_video only.
- Product task does not call generate_project_ar_video_bundle if that wrapper regenerates Sprint 2.
- Golden public functions remain backward-compatible.
- Existing Sprint 1-3 golden parity remains intact.
- No Sprint 4 product outputs are reintroduced.

Hard non-goals:

- Do not push remote.
- Do not open PRs.
- Do not commit unless explicitly asked later.
- Do not modify ADR-001 or relax PRD-05 acceptance.
- Do not work on UI/UX in this task.
- Do not optimize PDF/DXF/GLB/FBX/USDZ/MP4 visual quality in this task.
- Do not add Sprint 4 product outputs.
- Do not add IFC, Pascal Editor integration, ISO 19650, TCVN/QCVN, Specular-Glossiness, procedural materials, or external model upload/import.
- Do not weaken golden fixture pipelines.
- Do not run heavy generation synchronously inside a FastAPI request.
- Do not add heavy Blender/KTX/FFmpeg/USD tooling to the main API image.

Implementation invariants:

- Product orchestration owns stage transitions.
- Product orchestration owns DB asset registration.
- Generator helpers may write files and local reports, but they must not silently advance product job stages.
- A file must not be registered as ready before the stage that creates and validates it has completed.
- Stage names must describe active work, not work already completed inside another wrapper.
- Product generation must use the selected DesignVersion.geometry_json through DrawingProject and SceneContract.
- Do not fall back to golden fixture data in the product path.
- Preserve partial artifact evidence if a later stage fails.

Key files to inspect before editing:

API:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/tasks/professional_deliverables.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/sprint2_demo.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/sprint3_demo.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/scene_builder.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/usdz_exporter.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/video_renderer.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/camera_path.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/orchestrator.py
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/tests/professional_deliverables/

Expected implementation plan:

Step 1 - Confirm current flow
- Trace run_professional_deliverable_bundle_task in app/tasks/professional_deliverables.py.
- Trace generate_project_3d_bundle in sprint2_demo.py.
- Trace generate_project_ar_video_bundle in sprint3_demo.py.
- Confirm whether generate_project_ar_video_bundle still calls generate_project_3d_bundle internally.
- Record the current call chain in your final report.

Step 2 - Make Sprint 2 reusable with a prebuilt scene
- Update generate_project_3d_bundle in sprint2_demo.py to accept an optional keyword-only scene parameter:
  scene: SceneContract | None = None
- Preserve existing positional arguments.
- Preserve generate_golden_3d_bundle behavior.
- Preserve Sprint2BundleResult shape unless a small additive change is clearly necessary.
- Inside generate_project_3d_bundle, use:
  scene = scene or build_scene_from_project(project)

Step 3 - Split Sprint 3 into stage helpers
- In sprint3_demo.py, add explicit result dataclasses or equivalent typed structures:
  - USDZStageResult
  - VideoStageResult
  - Sprint3SummaryResult, if useful
- Keep Sprint3BundleResult for compatibility.

Add this helper:

export_project_usdz_stage(
    *,
    scene: SceneContract,
    glb_path: Path,
    textures_dir: Path,
    three_d_dir: Path,
    project_dir: Path,
    require_external_tools: bool,
) -> USDZStageResult

This helper must:
- consume the existing scene, GLB, and textures;
- export model.usdz and related USDZ files/reports;
- run existing USDZ validators;
- return USDZ paths and USDZ gate results;
- not call generate_project_3d_bundle;
- not rebuild the scene;
- not render video;
- not write the final Sprint 3 summary.

Add this helper:

render_project_video_stage(
    *,
    scene: SceneContract,
    glb_path: Path,
    project_dir: Path,
    video_dir: Path,
    require_external_tools: bool,
) -> VideoStageResult

This helper must:
- consume the existing scene and GLB;
- build or load camera_path.json;
- fail early with a structured CAMERA_PATH_UNSAFE error when collision warnings are fatal under require_external_tools=True;
- render master_4k.mp4;
- validate the MP4 using existing validators;
- return video paths and video gate results;
- not generate GLB, FBX, textures, or USDZ;
- not write the final Sprint 3 summary.

Add this helper:

write_project_sprint3_summary(
    *,
    project_dir: Path,
    three_d_dir: Path,
    video_dir: Path,
    usdz_result: USDZStageResult,
    video_result: VideoStageResult,
) -> Sprint3BundleResult

This helper must:
- combine USDZ and video gate results;
- write gate_summary.json and gate_summary.md;
- return a Sprint3BundleResult-compatible object;
- not generate files other than summary/report files;
- not call external tools.

Step 4 - Preserve generate_project_ar_video_bundle as compatibility wrapper
- Keep the public generate_project_ar_video_bundle function.
- Reimplement it by calling:
  - build_scene_from_project
  - generate_project_3d_bundle(..., scene=scene)
  - export_project_usdz_stage(...)
  - render_project_video_stage(...)
  - write_project_sprint3_summary(...)
- It is acceptable for this wrapper to generate Sprint 2 because it is a standalone Sprint 3/golden entrypoint.
- Product task must not call this wrapper.

Step 5 - Rewrite product task to use split helpers
- In app/tasks/professional_deliverables.py, remove product-path usage of generate_project_ar_video_bundle.
- Build DrawingProject once from the selected DesignVersion.geometry_json.
- Build SceneContract once from DrawingProject.
- Call generate_project_2d_bundle during export_2d.
- Call generate_project_3d_bundle during export_3d with the prebuilt scene.
- Mark export_usdz, then call export_project_usdz_stage.
- Mark render_video, then call render_project_video_stage.
- Call write_project_sprint3_summary after USDZ and video stages complete.
- Register valid artifacts only after their owning stage completes.
- Preserve skipped DWG behavior when ODA is missing.
- Preserve partial evidence if USDZ or video fails after 2D/3D succeeded.

Required product stage semantics:

- adapter 10: geometry adapter and DrawingProject creation
- export_2d 25: PDF/DXF/DWG-skipped and 2D reports
- export_3d 50: GLB/FBX/textures and Sprint 2 reports
- export_usdz 65: USDZ files and USDZ reports
- render_video 85: camera path, render reports, MP4, video reports
- validate 95: product output validation and final bundle status
- ready 100: success only after required Phase 2 artifacts are valid or explicitly skipped where allowed

Step 6 - Add regression tests

Add or update focused tests under:

/Users/nguyenquocthong/project/ai-architect/ai-architect-api/tests/professional_deliverables/

Required tests:

1. Product task generates Sprint 2 exactly once
- Monkeypatch generate_project_3d_bundle to count calls.
- Monkeypatch split USDZ/video helpers to create expected fake files.
- Run the product task or the narrow orchestration function used by the task.
- Assert generate_project_3d_bundle was called exactly once.

2. Product task stage order is correct
- Capture calls or persisted stage updates.
- Expected order:
  adapter, export_2d, export_3d, export_usdz, render_video, validate
- Expected progress:
  10, 25, 50, 65, 85, 95
- Do not require ready to be emitted by mark_job_stage if success is handled by mark_job_succeeded.

3. Product task does not overwrite GLB after export_3d
- Fake Sprint 2 writes deterministic 3d/model.glb content.
- Fake USDZ/video helpers consume the GLB but do not modify it.
- Assert the GLB checksum/content is unchanged after task completion.

4. Product task does not call generate_project_ar_video_bundle
- Monkeypatch generate_project_ar_video_bundle to raise if called.
- Run the product task happy path with split helpers.
- Assert task succeeds without calling the wrapper.

5. Golden compatibility remains intact
- Existing tests for generate_golden_bundle, generate_golden_3d_bundle, and generate_golden_ar_video_bundle must still pass.

Verification commands:

cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api

PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_product_e2e_bridge.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_sprint3_camera_and_video.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_sprint3_usdz.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
make sprint3-ci-linux

If you touch shared models, schemas, task wiring, or DB behavior, also run:

PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py

Do not run web lint/build unless you unexpectedly change the Web repo. This task should not require Web changes.

Acceptance criteria:

- Product task no longer calls generate_project_ar_video_bundle.
- Product task calls generate_project_3d_bundle exactly once.
- export_usdz stage creates USDZ outputs.
- render_video stage creates camera_path.json and master_4k.mp4.
- GLB, FBX, and textures are not regenerated, deleted, or overwritten after export_3d.
- Existing Sprint 1-3 golden commands/tests pass.
- Product path does not create Sprint 4 product outputs.
- Partial artifacts remain available as evidence if a later stage fails.
- No frontend or artifact quality optimization changes are mixed into this refactor.

Final report format:

Decision: PASS | BLOCKED | NEEDS_REVIEW

Repos:
- API repo:
- API branch:
- API dirty status:
- Web repo:
- Web branch:
- Web dirty status:
- Docs repo:
- Docs branch:
- Docs dirty status:

Summary:
- Fixed:
- Not fixed:
- Deferred:

Current flow found:
- Product task previous Sprint 2 call:
- Sprint 3 previous internal Sprint 2 regeneration:
- Previous export_usdz/render_video misalignment:

Implementation:
- Sprint 2 prebuilt scene support:
- Split USDZ helper:
- Split video helper:
- Sprint 3 summary helper:
- generate_project_ar_video_bundle compatibility wrapper:
- Product task split-helper usage:

Pipeline orchestration evidence:
- generate_project_3d_bundle product call count:
- generate_project_ar_video_bundle product call count:
- Stage order observed:
- Progress order observed:
- GLB checksum preserved after export_usdz/render_video:
- USDZ generated during export_usdz:
- MP4 generated during render_video:

Files changed:
- API:
- Web:
- Docs/compose:

Commands run:
1.
2.
3.

Test results:
- test_product_e2e_bridge:
- test_sprint3_camera_and_video:
- test_sprint3_usdz:
- full tests/professional_deliverables:
- make sprint3-ci-linux:
- foundation/flows, if run:

Scope compliance:
- No remote push:
- No PR:
- No Sprint 4 product outputs:
- No UI/UX changes:
- No artifact quality optimization mixed in:
- No main API heavy toolchain:
- No synchronous render request:
- Golden fixture pipeline preserved:

Known issues:
-

Return PASS only if all acceptance criteria above are met.

Return NEEDS_REVIEW if the refactor is mostly complete but one non-critical test expectation needs owner confirmation.

Return BLOCKED if:
- current code structure prevents splitting Sprint 3 without a broader architecture decision;
- required local tests cannot run due to missing environment;
- professional deliverables dependencies are missing in a way that prevents even mocked/focused tests from running.
```
