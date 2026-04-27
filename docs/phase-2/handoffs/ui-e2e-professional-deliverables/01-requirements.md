---
title: UI E2E Professional Deliverables Handoff - Requirements
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Requirements

## Objective

Enable a local product E2E flow where a user can create a project in the web UI, generate a design version, approve/lock it, then trigger Phase 2 professional deliverables from the Review page and retrieve the generated bundle.

## In Scope

- Convert current `DesignVersion.geometry_json` into the existing professional deliverables `DrawingProject` contract.
- Generalize the accepted Sprint 1-3 generators so they can run against a real project/version, while preserving all golden-fixture commands and tests.
- Add async API/job orchestration for professional deliverables.
- Add a dedicated Docker Compose worker service with Blender/KTX/FFmpeg/USD tooling.
- Add Review page UI trigger with progress bar.
- Add Delivery page bundle status and artifact links.
- Store outputs in canonical project/version scoped storage.
- Add tests and local verification commands.

## Out of Scope

- No upload/import of external CAD/BIM/3D models.
- No Sprint 4 deliverables: final `manifest.json`, 9:16 reel, hero still, GIF.
- No IFC export.
- No Pascal Editor integration.
- No ISO 19650 process compliance.
- No TCVN/QCVN compliance implementation.
- No Specular-Glossiness PBR workflow.
- No AI procedural materials.
- No GitHub Actions, remote push, or PR requirement.

## Required Product Flow

1. Start local stack with Docker Compose.
2. Open the web UI at `http://localhost:3000`.
3. Create or use a project.
4. Lock brief.
5. Generate design version.
6. Select version for review.
7. Approve/lock version.
8. In Review page, click `Tạo Phase 2 Professional Deliverables`.
9. UI shows progress bar and current stage.
10. Backend runs the professional deliverables job asynchronously.
11. UI reaches `ready` state and links to:
    - PDF bundle.
    - DXF sheets.
    - DWG sheets when ODA is configured, otherwise skipped with clear reason.
    - GLB.
    - FBX.
    - USDZ.
    - 4K MP4.
    - Sprint 3 gate summary JSON/MD.
12. Delivery page shows the same bundle as the canonical handoff/download surface.

## Acceptance Criteria

- A real version from the current generation flow can trigger the professional deliverables pipeline.
- The generated bundle is not hardcoded to `project-golden-townhouse`.
- Outputs are written under a project/version scoped path.
- Job status includes progress percent and stage.
- The Review page has a visible progress bar while the job is running.
- The Delivery page exposes generated artifact links after completion.
- Heavy processing is run through Celery and the dedicated `professional-worker` service.
- API requests do not synchronously block on 3D/video generation.
- Local Docker Compose can run the full UI/API/worker flow without GitHub.
- Golden fixture commands from Sprint 1-3 still pass.
- DWG is allowed to be skipped locally only when ODA is missing; all other required formats must be produced.
- No forbidden roadmap item is implemented.

## Expected Local Commands

Docker Compose should remain the default local product run path:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build
```

Professional pipeline parity should remain available:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make sprint3-ci-linux
```

