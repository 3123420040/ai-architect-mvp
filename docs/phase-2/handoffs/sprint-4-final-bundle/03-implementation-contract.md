---
title: Sprint 4 Final Bundle Handoff - Implementation Contract
phase: 2
status: ready-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Implementation Contract

## Scope

Complete final bundle outputs for the accepted product E2E flow:

```text
existing professional bundle + master_4k.mp4
  -> reel_9x16_1080p.mp4
  -> hero_still_4k.png
  -> preview.gif
  -> manifest.json
  -> optional zip archive
  -> Delivery page links
```

## Allowed Changes

API repo:

- `app/services/professional_deliverables/orchestrator.py`
- `app/services/professional_deliverables/demo.py`
- `app/services/professional_deliverables/sprint3_demo.py`
- new `app/services/professional_deliverables/video_derivatives.py`
- new `app/services/professional_deliverables/manifest_builder.py`
- new `app/services/professional_deliverables/sprint4_validators.py`
- optional new `app/services/professional_deliverables/bundle_archive.py`
- `app/tasks/professional_deliverables.py`
- `app/api/v1/professional_deliverables.py`
- `app/schemas.py`
- `app/models.py` only if new asset roles/status fields require it
- Alembic migration only if model changes require it
- `tests/professional_deliverables/`
- `Makefile` only for Sprint 4 verification commands
- professional-worker Dockerfile only if a missing ffmpeg/image dependency blocks Sprint 4

Web repo:

- `src/components/delivery-client.tsx`
- `src/components/review-client.tsx` only if progress stages need display updates
- `src/lib/professional-deliverables.ts`

Docs/compose repo:

- `docker-compose.local.yml` only if existing professional-worker cannot run Sprint 4 commands
- `docs/phase-2/handoffs/sprint-4-final-bundle/` for implementation notes/report updates
- `docs/phase-2/sprint-reports/sprint-4.md`

## Forbidden Changes

- No remote push.
- No PR.
- No ADR-001 changes.
- No PRD-05 acceptance relaxation.
- No new master render architecture.
- No re-rendering reel/derivatives from Blender.
- No external model upload/import.
- No IFC.
- No Pascal Editor integration.
- No ISO 19650 full process compliance.
- No TCVN/QCVN compliance implementation.
- No Specular-Glossiness.
- No procedural materials.
- No 50-material curated starter pack.
- No audio/soundtrack.
- No custom branding/watermark.
- No mid-length 30-45s video cut.
- Do not weaken existing Sprint 1-3 gates.
- Do not overwrite the golden fixture output folder.
- Do not touch known unrelated dirty files.

## Required Outputs

Write outputs into the existing project/version scoped bundle root:

```text
storage/professional-deliverables/projects/{project_id}/versions/{version_id}/
```

Required Sprint 4 paths:

```text
video/reel_9x16_1080p.mp4
derivatives/hero_still_4k.png
derivatives/preview.gif
manifest.json
sprint4_gate_summary.json
sprint4_gate_summary.md
```

Optional if implementation fits existing storage model:

```text
project-{project_id}-professional-deliverables.zip
```

## Progress Contract

Preserve existing stages and add post-processing stages only if needed.

Recommended final stage map:

```text
queued: 0
adapter: 10
export_2d: 25
export_3d: 50
export_usdz: 65
render_video: 85
derive_reel: 90
derive_derivatives: 94
build_manifest: 97
archive_bundle: 99
ready: 100
failed: preserve last progress
```

If adding stages requires too much UI change, keep UI generic by displaying backend stage labels.

## Validation Gates

Sprint 4 gates must include:

1. Reel format
   - `ffprobe` width 1080
   - height 1920
   - fps 30.000 +/- 0.001
   - codec `h264`
   - duration 20-30 seconds
   - bitrate target 10-15 Mbps, or documented tolerance if ffmpeg encoder variance is small and justified

2. Reel integrity
   - no all-black frames at start/middle/end
   - plays start-to-finish without decoder errors
   - file size <= 30 MB when feasible under PRD non-functional target

3. Hero still
   - PNG
   - 3840x2160
   - extracted from 8-12s
   - non-black

4. GIF preview
   - animated
   - 6-10 seconds
   - <= 5 MB
   - non-black sample frames

5. Manifest schema
   - validates against PRD Appendix B schema
   - all required top-level fields present
   - `material_list.workflow` is `metallic-roughness`
   - no Specular-Glossiness fields

6. Manifest file inventory
   - every listed path exists
   - every SHA-256 matches
   - paths are relative
   - no fake DWG entry when DWG is skipped

7. LOD summary
   - `lod_100`, `lod_200`, `lod_300` exist
   - total matches scene metadata count used by Sprint 2/3

8. Bundle self-contained
   - GLB/FBX/USDZ and textures referenced relatively or embedded as already accepted
   - optional zip archive extracts with manifest paths resolving
   - archive size < 500 MB if archive implemented

9. Failure case
   - missing or corrupt `master_4k.mp4` fails Sprint 4 gates
   - bundle is not marked ready when required Sprint 4 artifacts are missing or invalid

## Asset Registration

Add asset roles for:

- `marketing_reel`
- `hero_still`
- `gif_preview`
- `manifest`
- optional `bundle_archive`
- `sprint4_gate_summary_json`
- `sprint4_gate_summary_md`

Delivery page must show these links when present.

## Verification Commands

API:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux
```

Add a new Sprint 4 command if useful:

```bash
make sprint4-ci-linux
```

Web:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Product E2E:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build
```

Then verify manually through the UI:

- create/open project
- lock/select generated version
- trigger professional deliverables on Review page
- observe progress through Sprint 4 stages
- open Delivery page
- verify all final artifact links

