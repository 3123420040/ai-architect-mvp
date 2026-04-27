---
title: Sprint 4 Final Bundle Handoff - System Analysis
phase: 2
status: ready-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# System Analysis

## Current Behavior

The accepted product E2E flow creates an async professional deliverables job from the Review page.

The job:

1. Reads the selected `DesignVersion.geometry_json`.
2. Converts it through the professional deliverables geometry adapter.
3. Generates 2D outputs.
4. Generates GLB/FBX/KTX2 outputs.
5. Generates USDZ and master 4K video.
6. Validates Sprint 1-3 gates.
7. Registers assets and shows links on Delivery page.

Current final state can be `ready/partial` when DWG is skipped because ODA is unavailable locally.

## Remaining Data Flow

Sprint 4 should extend the accepted flow after `master_4k.mp4` exists:

```text
master_4k.mp4
  -> reel_9x16_1080p.mp4
  -> hero_still_4k.png
  -> preview.gif

existing scene metadata + artifacts
  -> manifest.json
  -> optional zip archive
  -> artifact registration
  -> Delivery page links
```

## Likely API Modules

Expected API files or file areas:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/services/professional_deliverables/orchestrator.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/tasks/professional_deliverables.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/api/v1/professional_deliverables.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/schemas.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/app/models.py`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/tests/professional_deliverables/`

Expected new API modules:

- `app/services/professional_deliverables/video_derivatives.py`
- `app/services/professional_deliverables/manifest_builder.py`
- `app/services/professional_deliverables/sprint4_validators.py`
- Optional: `app/services/professional_deliverables/bundle_archive.py`

## Likely Web Modules

Expected Web files:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/components/review-client.tsx`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/components/delivery-client.tsx`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/lib/professional-deliverables.ts`

Web changes should be minimal: show new artifact roles and keep existing Review progress behavior.

## Tooling

Use existing professional-worker tooling:

- FFmpeg/ffprobe for video derivatives and validation.
- Python for manifest, checksum, schema validation, and tests.
- Existing Docker Compose professional worker for local E2E.

Do not add another heavy worker unless the existing worker cannot support ffmpeg-based derivative extraction.

## Architecture Pattern

Follow existing Sprint 1-3 gate pattern:

- `GateResult` dataclass.
- Machine-readable JSON summary.
- Human-readable Markdown summary.
- Fail required gates.
- Allow only explicitly accepted local DWG/ODA skip.

Follow existing product E2E persistence:

- professional deliverables bundle/job/assets tables
- project/version scoped storage path
- asset roles for Delivery page links

## Risks

### Manifest Accuracy

Risk: manifest can pass shape validation but contain stale or missing file paths.

Mitigation: tests must recompute file inventory and checksums from disk. Fake entries are not allowed.

### Reel Cropping

Risk: simple center crop may cut important building content in vertical format.

Mitigation: implement deterministic crop policy and record crop metadata. For this slice, pass/fail should verify format and non-black content; visual safe-area perfection can be improved later if needed.

### GIF Size

Risk: 4K-derived GIF can exceed 5 MB.

Mitigation: downscale GIF preview and tune fps/palette deterministically while preserving 6-10s duration.

### Archive Scope

Risk: implementing archive download may require product/storage redesign.

Mitigation: keep archive local and asset-registered only if it fits existing asset model. Otherwise report before redesign.

## Assumptions

- Sprint 4 can derive reel/derivatives from `master_4k.mp4` without re-rendering.
- Existing professional-worker has FFmpeg/ffprobe available.
- Existing scene metadata from Sprint 2/3 is sufficient to derive `lod_summary` and `material_list`.
- PRD Appendix B schema is the contract; additional provenance fields are allowed when they do not break validation.

