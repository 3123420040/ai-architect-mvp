---
title: Sprint 4 Final Bundle Handoff - Requirements
phase: 2
status: ready-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Requirements

## Goal

Complete the Phase 2 canonical professional deliverables bundle for the local product E2E flow.

The user should be able to trigger professional deliverables from the Review page and receive a final bundle containing:

- 2D outputs from Sprint 1/product E2E
- 3D outputs from Sprint 2/product E2E
- USDZ and master video from Sprint 3/product E2E
- Sprint 4 reel, hero still, GIF preview, and final `manifest.json`

## Functional Requirements

### Reel

Generate:

```text
/video/reel_9x16_1080p.mp4
```

Requirements:

- Derived from `/video/master_4k.mp4`.
- No new render.
- 20-30 seconds.
- 1080x1920.
- 9:16 vertical.
- 30fps.
- H.264 MP4.
- Target bitrate 10-15 Mbps.
- Important content should stay inside safe area, avoiding top 13% and bottom 17% overlay zones as much as possible.

### Derivatives

Generate:

```text
/derivatives/hero_still_4k.png
/derivatives/preview.gif
```

Requirements:

- Hero still extracted from master video between 8s and 12s.
- Hero still resolution 3840x2160.
- GIF extracted from a 6-10 second segment.
- GIF must be animated, loopable, and <= 5 MB.
- Both must be non-black and readable.

### Manifest

Generate:

```text
/manifest.json
```

Requirements from PRD Appendix B:

- `project_id`
- `generated_at`
- `version`
- `naming_convention`
- `lod_summary`
- `material_list`
- `file_inventory`
- `source_brief`
- `agent_provenance`

File inventory requirements:

- Relative paths only.
- Existing files only.
- Size in bytes.
- SHA-256 checksum.
- Include all delivered artifacts.
- Include DWG only when produced. If DWG is skipped locally, record the degraded reason in provenance/quality metadata, not as a fake file inventory item.

Material requirements:

- Metal-Roughness only.
- No Specular-Glossiness fields or extensions.
- Texture paths must be relative and point to KTX2 files where texture assets are listed.

LOD requirements:

- `lod_100`, `lod_200`, and `lod_300` counts must be derived from scene metadata.
- The element count must match the accepted scene graph metadata used by Sprint 2/3 validators.

### Bundle Archive

Create a self-contained archive if the current architecture has a natural asset/archive registration path.

Recommended output:

```text
/project-<id>-professional-deliverables.zip
```

Requirements:

- Includes the canonical bundle folder.
- All manifest paths resolve after extraction.
- Archive size < 500 MB.

If archive support requires broader storage/product architecture changes, stop and report with the smallest proposed contract adjustment before implementing a large redesign.

### UI

Delivery page must show links for new Sprint 4 outputs:

- reel
- hero still
- GIF preview
- manifest JSON
- bundle archive, if implemented

Review page progress may add post-processing stages if needed.

## Non-Goals

- No new 3D scene generation.
- No external model upload/import.
- No re-render for reel or derivatives.
- No audio/soundtrack.
- No custom branding/watermark.
- No long-form walkthrough.
- No mid-length 30-45s cut.
- No final IFC, Pascal Editor integration, ISO 19650 full process, TCVN/QCVN compliance, procedural materials, or 50-material curated pack.
- No ADR-001 or PRD-05 relaxation.
- No remote push or PR.

## Acceptance Criteria

- Product E2E job reaches `ready` or accepted `ready/partial` only when all required Sprint 4 outputs pass validation.
- `/video/reel_9x16_1080p.mp4` exists and passes ffprobe checks.
- `/derivatives/hero_still_4k.png` exists and passes resolution/non-black checks.
- `/derivatives/preview.gif` exists, is animated, is 6-10 seconds, and is <= 5 MB.
- `/manifest.json` validates against the PRD schema and all SHA-256 checksums match.
- Delivery page shows links for all final outputs.
- Existing Sprint 1-3 golden commands still pass.
- Existing product E2E does not regress.
- DWG local skip remains allowed only with explicit ODA reason.

