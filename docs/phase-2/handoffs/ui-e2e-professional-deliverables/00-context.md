---
title: UI E2E Professional Deliverables Handoff - Context
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Context

AI Architect Phase 2 Sprint 1-3 deliverables are accepted through local verification:

- Sprint 1: 2D DXF/DWG/PDF foundation.
- Sprint 2: GLB, FBX, and KTX2 texture outputs.
- Sprint 3: USDZ and 4K master video.

The accepted implementation currently proves the pipeline through CLI and local Linux parity commands, especially:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
make sprint3-ci-linux
```

This is not yet a product-level end-to-end flow. The UI currently lets users generate and review design versions, but there is no product-facing bridge from a real `DesignVersion.geometry_json` to the accepted Phase 2 professional deliverables pipeline.

## User Goal

The PM wants to test the real product locally:

```text
UI click -> async job -> Phase 2 professional deliverables bundle
```

This is Option B: true product E2E from the existing UI and project/version data, not a golden-fixture-only demo button.

## Confirmed PM Decisions

- The first slice supports only `DesignVersion.geometry_json` produced by the current system. No import/upload model support.
- Review page must include the user-facing trigger and progress bar.
- A dedicated heavy `professional-worker` Docker service is allowed and preferred. Do not put Blender/KTX/FFmpeg into the main API container.
- Local E2E must generate the real `master_4k.mp4`, even if slow.
- DWG may be skipped locally when ODA is not configured, but PDF, DXF, GLB, FBX, USDZ, and MP4 must run.
- No paid GitHub dependency. Local git and local Docker verification are the source of truth for this phase.

## Repos

- API repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Web repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`
- Docs/compose repo: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`

## Existing Local Stack

Current local stack is defined in:

```text
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docker-compose.local.yml
```

It currently contains:

- `web`
- `api`
- `gpu`
- `worker`
- `postgres`
- `redis`
- `minio`

The new flow must extend this local stack with a professional deliverables worker rather than depending on GitHub Actions.

