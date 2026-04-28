---
title: UI E2E Professional Deliverables Remediation - Agent Prompt
phase: 2
status: ready-to-copy
date: 2026-04-27
owner: Codex Coordinator
related_files:
  - 09-retro-action-plan.md
  - 10-remediation-implementation-contract.md
  - 11-remediation-execution-playbook.md
  - 13-output-quality-remediation-plan.md
  - 14-artifact-input-process-quality-contract.md
  - 15-current-artifact-generation-order-and-inputs.md
  - 16-pipeline-orchestration-refactor-implementation.md
---

# Remediation Agent Prompt

Copy and send the following prompt to the new implementation/testing agent.

```text
You are the Implementation and Verification Agent for AI Architect Phase 2 UI E2E Professional Deliverables Remediation.

You have access to the current source code for all three repos. You are expected to implement, test, and report back. Do not stop at analysis unless you hit a true blocker.

Do not redefine product strategy. Do not broaden scope. Do not push remote. Do not open PRs. Do not commit unless explicitly asked later.

Work from the shared project root:

cd /Users/nguyenquocthong/project/ai-architect

Repos:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Docs/compose repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Read these documents first, in this order:

Core Phase 2 context:
1. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/03-adr-001-standards-combo.md
2. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/04-deferred-roadmap.md
3. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/05-prd-deliverables.md
4. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md

Original Option B handoff:
5. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/00-context.md
6. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/01-requirements.md
7. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/02-system-analysis.md
8. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/03-implementation-contract.md
9. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/06-review-checklist.md
10. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/07-decision-log.md
11. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/08-local-e2e-signoff.md

Remediation source of truth:
12. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/09-retro-action-plan.md
13. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/10-remediation-implementation-contract.md
14. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/11-remediation-execution-playbook.md
15. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/13-output-quality-remediation-plan.md
16. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/14-artifact-input-process-quality-contract.md
17. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/15-current-artifact-generation-order-and-inputs.md
18. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/16-pipeline-orchestration-refactor-implementation.md

Report templates:
19. /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/ui-e2e-professional-deliverables/05-opencode-report-template.md
20. Use the remediation report format embedded in 10-remediation-implementation-contract.md for the final report.

Primary objective:

Fix the local product E2E flow so that a real customer journey works from natural Vietnamese intake through design review, professional deliverables generation, delivery artifact download, share link, and 3D viewer.

The regression project that exposed the failures is:

- Project: 3b00f863-3144-4223-b04d-dec825c894d8
- V2: e888ad98-597c-4d52-872f-7b5f3106499c
  - Known issue: invalid master_4k.mp4, ffprobe error "moov atom not found".
- V4: b0f39796-d4ba-43f8-92e8-058004ce64d6
  - Known issue: valid 4K MP4 but camera collision gate failure.
- Intake parser test project: dc759def-c7e7-4075-8bec-18a8a3baaa5e
- Share token: k2GgHmvg6UG2SOEXdrP_C687

PM decisions already locked:

1. Asset access:
   - Use API proxy or presigned URL helper.
   - Do not depend on raw private MinIO URLs.
   - Do not make public MinIO bucket access the product default.

2. Partial artifacts:
   - Allow users/devs to download valid generated artifacts from failed or partial bundles.
   - Label them clearly as "Partial / not final".

3. Viewer:
   - Allow Viewer to render a professional deliverables GLB from a failed or partial bundle if the GLB asset itself is valid.
   - Show a visible warning that the bundle is not final.

4. Current version:
   - Latest locked version is the source of truth for the current approved version.
   - Designs, Review, Delivery, and Viewer must use the same version-selection rule.

5. Intake:
   - Fix deterministic parser failures first.
   - Real structured LLM extraction is not required in this remediation.

Hard non-goals:

- No remote push.
- No PR.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No Sprint 4 product outputs in the Phase 2 UI E2E path.
- No IFC.
- No Pascal Editor integration.
- No ISO 19650 process compliance.
- No TCVN/QCVN implementation.
- No Specular-Glossiness.
- No procedural materials.
- No external model upload/import.
- Do not replace or weaken the golden fixture pipeline.
- Do not run heavy generation synchronously inside a FastAPI request.
- Do not remove existing legacy export, handoff, or presentation 3D UI.
- Keep Blender/KTX/FFmpeg/USD tooling in the dedicated professional-worker only. The main API image must stay slim.

Implement in batches, in this order:

Batch 1 - Product foundations:
- Fix asset access so generated images are browser-readable.
- Fix share page API path.
- Add a shared current-version selection helper.
- Apply the same current-version rule to Designs, Review, Delivery, and Viewer.
- Add stable image fallback UI for missing/broken images.

Batch 1 acceptance:
- Designs, Review, Delivery, and Share load visible images.
- Browser image elements have non-zero natural dimensions where assets exist.
- Share token page loads real shared project content.
- Review, Delivery, Viewer, and Designs select the same current version.

Batch 2 - Professional deliverables correctness:
- Remove Sprint 4 from the Phase 2 product path.
- Product jobs must not run derive_reel, build_manifest, Sprint 4 gates, or create final manifest/reel/hero still/GIF.
- Enforce the approved progress stages only:
  - queued 0
  - adapter 10
  - export_2d 25
  - export_3d 50
  - export_usdz 65
  - render_video 85
  - validate 95
  - ready 100
  - failed preserves last progress and records error_code/error_message
- Register generated artifacts by phase or as partial evidence.
- Preserve gate summaries and failed-gate evidence when a later validation step fails.
- Fix retry behavior so failed jobs can retry without destroying useful failure evidence.

Batch 2 acceptance:
- New product jobs do not produce Sprint 4 product outputs.
- Delivery can show failed, partial, running, and ready states honestly.
- Valid generated files are represented in DB assets even when final bundle validation fails.
- Invalid or missing artifacts are not shown as ready downloads.

Batch 3 - Media/render robustness:
- Validate master_4k.mp4 immediately after render using ffprobe or existing validators.
- If MP4 is invalid, stop at render_video or validate with a structured error such as VIDEO_MASTER_INVALID.
- Do not expose invalid MP4 as a ready artifact.
- Reproduce and fix the V4 camera collision regression, or fail early before expensive render with a clear CAMERA_PATH_UNSAFE error.

Batch 3 acceptance:
- The V2-style invalid MP4 failure no longer proceeds into later stages.
- The V4-style camera collision is fixed or caught early.
- Raw ffmpeg/ffprobe logs are available for debugging but are not the primary customer-facing message.

Batch 4 - Worker toolchain:
- Ensure professional-worker includes:
  - Blender 4.5.1
  - KTX 4.4.2
  - FFmpeg/ffprobe
  - Node 22
  - Python 3.12
  - usd-core==26.5
- Verify "from pxr import Usd" works inside the professional-worker.
- Do not add heavy tools to the main API image.

Batch 5 - UX cleanup:
- Redesign Review as a state-driven decision/progress page.
- Redesign Delivery as an artifact readiness/download page.
- Connect Viewer to professional deliverables GLB first, then fallback to legacy Presentation3D.
- Clean up Designs lifecycle hierarchy.

UX requirements:
- One clear primary action per state.
- Current approved version must be obvious.
- Superseded/historical versions must not look equally active.
- Delivery must not render anchors without usable href.
- Delivery must not show Sprint 4 artifact slots.
- Review/Delivery must not show raw backend logs as the main user message.
- Failed states must be clear, actionable, and include expandable technical details.

Batch 6 - Intake parser:
- Fix deterministic parser for realistic Vietnamese customer input.
- Required regression sentence:
  "Nha biet thu xay moi lo 7*25m huong Tay Nam, 3 tang, 4 phong ngu, 3 WC, gara 1 o to, phong tho, 6 nguoi o gom ong ba va 2 tre nho, phong cach hien dai am xanh gan gui tu nhien, ngan sach khoang 7 ty, muon hoan thanh trong 8 thang, bat buoc nhieu anh sang thong gio va tranh khong gian bi."
- Expected extracted fields:
  - project_type: villa
  - project_mode: new build
  - lot width: 7m
  - lot depth: 25m
  - lot area: 175m2
  - orientation: southwest
  - floors: 3
  - bedrooms: 4
  - bathrooms: 3
  - garage: true
  - prayer room: true
  - occupants: 6
  - budget: 7,000,000,000 VND
  - timeline: 8 months
  - priorities: daylight and ventilation
  - negative constraint: avoid cramped/dark spaces

Batch 7 - Pipeline orchestration refactor:
- Use 16-pipeline-orchestration-refactor-implementation.md as the exact implementation guide.
- Split Sprint 3 so the product path does not regenerate Sprint 2 internally.
- Product jobs must generate GLB, FBX, and textures exactly once during export_3d.
- export_usdz must generate USDZ from the existing Sprint 2 GLB/textures/scene.
- render_video must generate camera_path.json and master_4k.mp4 from the existing Sprint 2 GLB/scene.
- Product jobs must not call generate_project_ar_video_bundle if that wrapper regenerates Sprint 2.
- Preserve generate_golden_ar_video_bundle as a backward-compatible golden/test wrapper.
- Add tests proving stage order, single Sprint 2 generation, and no GLB overwrite after export_3d.

Batch 7 acceptance:
- Product task calls generate_project_3d_bundle exactly once.
- Product task uses split USDZ and video helpers.
- export_usdz stage corresponds to real USDZ generation.
- render_video stage corresponds to real MP4 generation.
- GLB/FBX/textures are not deleted or overwritten after export_3d.
- Existing Sprint 1-3 golden commands/tests still pass.
- No Sprint 4 product outputs are reintroduced.

Batch 8 - Output quality uplift:
- Use 13-output-quality-remediation-plan.md as the artifact quality bar.
- Use 14-artifact-input-process-quality-contract.md as the required input/process contract for each artifact.
- Improve each generated file so it is usable, not merely present or format-valid:
  - PDF drawing bundle
  - DXF sheets
  - DWG conversion/skip state
  - GLB model
  - FBX model
  - USDZ AR package
  - master_4k.mp4
  - gate summary JSON
  - gate summary MD
- Add stronger semantic and visual QA gates where practical.
- Do not weaken existing technical validators to make files pass.

Batch 8 acceptance:
- Final report includes per-artifact quality status: exists, format-valid, semantic-valid, visual-QA, customer-ready.
- PDF/DXF do not contain stale golden dimensions on project outputs.
- GLB/FBX/USDZ represent the selected project geometry clearly enough for review.
- MP4 is playable, valid, non-black, collision-free, and visually useful.
- Gate summaries explain usability, not only tool success/failure.

Key files to inspect and likely change:

API:
- app/services/storage.py
- app/api/v1/projects.py
- app/api/v1/share.py
- app/api/v1/professional_deliverables.py
- app/services/professional_deliverables/orchestrator.py
- app/tasks/professional_deliverables.py
- app/services/professional_deliverables/video_renderer.py
- app/services/professional_deliverables/sprint3_demo.py
- app/services/professional_deliverables/camera_path.py
- app/services/professional_deliverables/geometry_adapter.py
- app/models.py
- app/schemas.py
- app/services/briefing.py
- app/services/llm.py only if needed for explicit parser/LLM state, but do not require real LLM extraction.
- Dockerfile.professional-worker
- alembic/versions/ if schema changes are needed.
- tests/

Web:
- src/lib/api.ts
- src/lib/professional-deliverables.ts
- new src/lib/version-selection.ts
- optional new src/components/asset-image.tsx
- optional new src/components/professional-deliverables-status.tsx
- optional new src/components/version-badge.tsx
- src/components/designs-client.tsx
- src/components/review-client.tsx
- src/components/delivery-client.tsx
- src/components/viewer-client.tsx
- src/components/share-client.tsx

Docs/compose:
- docker-compose.local.yml only if worker/toolchain or local service wiring requires it.
- docs/phase-2/handoffs/ui-e2e-professional-deliverables/ only for local notes/report if needed.

Testing requirements:

API:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_briefing.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux

Web:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build

Docker local E2E:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build

Worker toolchain verification:
docker exec kts-blackbirdzzzz-art-professional-worker blender --version
docker exec kts-blackbirdzzzz-art-professional-worker ktx --version
docker exec kts-blackbirdzzzz-art-professional-worker ffmpeg -version
docker exec kts-blackbirdzzzz-art-professional-worker ffprobe -version
docker exec kts-blackbirdzzzz-art-professional-worker node --version
docker exec kts-blackbirdzzzz-art-professional-worker python --version
docker exec kts-blackbirdzzzz-art-professional-worker python -m pip show usd-core
docker exec kts-blackbirdzzzz-art-professional-worker python -c "from pxr import Usd; print('ok')"

Manual browser verification:
1. Open /projects/3b00f863-3144-4223-b04d-dec825c894d8/designs.
2. Confirm images load and current approved version is clear.
3. Open /projects/3b00f863-3144-4223-b04d-dec825c894d8/review.
4. Confirm the same current version is selected.
5. Trigger or retry professional deliverables.
6. Confirm progress stages match the approved contract.
7. Open /projects/3b00f863-3144-4223-b04d-dec825c894d8/delivery.
8. Confirm same current version, honest state, artifact links, partial labels, and DWG skip reason if ODA is missing.
9. Open /projects/3b00f863-3144-4223-b04d-dec825c894d8/viewer.
10. Confirm professional GLB renders if available, or a clear empty state appears.
11. Open /share/k2GgHmvg6UG2SOEXdrP_C687.
12. Confirm shared project content loads.
13. Create a fresh project and test the Vietnamese regression intake sentence.

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

Root-cause coverage:
- RC-01 asset access:
- RC-02 current version:
- RC-03 Sprint 4 removal:
- RC-04 partial/failure assets:
- RC-05 invalid MP4:
- RC-06 camera collision:
- RC-07 share link:
- RC-08 viewer GLB:
- RC-09 delivery UX:
- RC-10 review UX:
- RC-11 designs UX:
- RC-12 intake parser:
- RC-13 worker usd-core:

Pipeline orchestration coverage:
- Product task generates Sprint 2 exactly once:
- Product task uses split USDZ helper:
- Product task uses split video helper:
- export_usdz stage verified:
- render_video stage verified:
- GLB checksum preserved after video step:
- Golden generate_golden_ar_video_bundle preserved:
- Tests added:

Output quality coverage:
- PDF drawing bundle:
- DXF sheets:
- DWG conversion/skip:
- GLB model:
- FBX model:
- USDZ AR package:
- master_4k.mp4:
- Gate summary JSON:
- Gate summary MD:

Files changed:
- API:
- Web:
- Docs/compose:

Commands run:
1.
2.
3.

Test results:
- API focused:
- API foundation/flows:
- Golden parity:
- Web lint:
- Web build:
- Docker Compose E2E:
- Worker toolchain:

Manual evidence:
- Project id:
- Version id:
- Job id:
- Bundle id:
- Current version selected consistently:
- Images load:
- Share link works:
- Viewer works:
- Delivery artifacts:

Known issues:
-

Scope compliance:
- No remote push:
- No PR:
- No Sprint 4 product outputs:
- No deferred roadmap items:
- No main API heavy toolchain:
- No synchronous render request:

Pass/fail rules:

Return PASS only if:
- Images load across Designs, Review, Delivery, and Share.
- Current version is consistent across product pages.
- Share link works.
- Review and Delivery show truthful professional deliverables state.
- New jobs do not run Sprint 4 stages or create Sprint 4 product outputs.
- Worker has usd-core==26.5.
- Web lint/build pass.
- API focused tests and Sprint 3 golden parity pass.
- Local product E2E produces or truthfully reports Phase 2 artifacts.

Return NEEDS_REVIEW if:
- A product decision is unexpectedly required despite the locked decisions above.
- A non-critical UI cleanup remains but core E2E is correct.
- Structured LLM extraction appears necessary to meet a product claim beyond this remediation scope.

Return BLOCKED if:
- Docker E2E cannot run.
- Professional worker cannot build.
- Required artifacts cannot be produced due to missing local toolchain.
- Database migration cannot be applied.

Do not mark the remediation complete if the UI merely hides errors without fixing backend state, asset access, version selection, and job truthfulness.
```
