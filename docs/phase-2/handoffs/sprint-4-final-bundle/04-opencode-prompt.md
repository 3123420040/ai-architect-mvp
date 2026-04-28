---
title: Sprint 4 Final Bundle Handoff - opencode Prompt
phase: 2
status: ready-to-copy
date: 2026-04-27
owner: Codex Coordinator
---

# Start opencode

Run opencode from the shared project root:

```bash
cd /Users/nguyenquocthong/project/ai-architect
opencode
```

Paste this prompt:

```text
You are opencode acting as the Implementation Agent for AI Architect Phase 2 Sprint 4 Final Bundle.

Do not redefine product strategy. Do not broaden scope. Do not push remote. Do not open PRs. Do not commit unless explicitly asked in a later follow-up.

Read these docs first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/03-adr-001-standards-combo.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/04-deferred-roadmap.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/05-prd-deliverables.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/07-local-git-verification-protocol.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/08-current-state-and-next-actions.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-4-final-bundle/00-context.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-4-final-bundle/01-requirements.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-4-final-bundle/02-system-analysis.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-4-final-bundle/03-implementation-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-4-final-bundle/05-opencode-report-template.md

Repos:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Docs/compose repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Baseline commits:
- API: 4dcbbe2
- Web: 853c97c
- Docs/compose: 2fbc752

Task objective:
Complete Sprint 4 final bundle outputs for the accepted product E2E professional deliverables flow. Build on the existing Review page -> async professional-worker -> Delivery page flow. Add derived marketing reel, hero still, GIF preview, final manifest, validation gates, and Delivery page artifact links.

Required outputs:
- video/reel_9x16_1080p.mp4
- derivatives/hero_still_4k.png
- derivatives/preview.gif
- manifest.json
- sprint4_gate_summary.json
- sprint4_gate_summary.md
- optional bundle zip only if it fits the existing storage/asset model without broad redesign

Scope:
- Derive reel/hero/GIF from existing video/master_4k.mp4.
- Generate final manifest.json from existing bundle files and scene metadata.
- Register Sprint 4 artifacts in the existing professional deliverables asset model.
- Show Sprint 4 artifact links on Delivery page.
- Preserve accepted Sprint 1-3 and product E2E behavior.
- Keep local-first verification. No remote push, no PR.

Non-goals:
- No new master render architecture.
- No re-rendering reel/derivatives from Blender.
- No audio/soundtrack.
- No custom branding/watermark.
- No external model upload/import.
- No IFC.
- No Pascal Editor integration.
- No ISO 19650 full process compliance.
- No TCVN/QCVN compliance.
- No Specular-Glossiness.
- No procedural materials.
- No 50-material curated starter pack.
- No mid-length 30-45s video cut.
- No ADR/PRD acceptance relaxation.

Allowed files/areas:
API:
- app/services/professional_deliverables/orchestrator.py
- app/services/professional_deliverables/demo.py
- app/services/professional_deliverables/sprint3_demo.py
- new app/services/professional_deliverables/video_derivatives.py
- new app/services/professional_deliverables/manifest_builder.py
- new app/services/professional_deliverables/sprint4_validators.py
- optional new app/services/professional_deliverables/bundle_archive.py
- app/tasks/professional_deliverables.py
- app/api/v1/professional_deliverables.py
- app/schemas.py
- app/models.py only if new asset roles/status fields require it
- alembic/versions/ only if model changes require it
- tests/professional_deliverables/
- Makefile only for verification commands
- Dockerfile.professional-worker only if required Sprint 4 tooling is missing

Web:
- src/components/delivery-client.tsx
- src/components/review-client.tsx only if progress-stage display needs it
- src/lib/professional-deliverables.ts

Docs/compose:
- docker-compose.local.yml only if professional-worker cannot run Sprint 4 commands
- docs/phase-2/sprint-reports/sprint-4.md
- docs/phase-2/handoffs/sprint-4-final-bundle/ only for implementation notes/report updates

Forbidden changes:
- Do not touch unrelated dirty files:
  - ai-architect-web/src/components/designs-client.tsx
  - ai-architect-web/src/components/status-badge.tsx
  - ai-architect-mvp/docs/phases/**
  - ai-architect-mvp/implementation/**
- Do not weaken existing Sprint 1-3 gates.
- Do not overwrite storage/professional-deliverables/project-golden-townhouse.
- Do not make heavy generation synchronous inside FastAPI.
- Do not mark bundle ready if any required Sprint 4 gate fails.

Implementation requirements:
1. Add ffmpeg-based derivative generation:
   - Derive reel_9x16_1080p.mp4 from master_4k.mp4.
   - Use deterministic crop/scale policy.
   - Target 20-30s, 1080x1920, 30fps, H.264, 10-15 Mbps.
   - Extract hero_still_4k.png from 8-12s, 3840x2160.
   - Extract preview.gif from 6-10s segment, animated, <=5 MB.

2. Add manifest builder:
   - Validate against PRD Appendix B schema.
   - Include project_id, generated_at, version, naming_convention, lod_summary, material_list, file_inventory, source_brief, agent_provenance.
   - Use relative paths.
   - Compute real SHA-256 for every file_inventory item.
   - Include DWG only if it exists. If DWG is skipped locally, record the degraded reason in provenance/quality metadata, not as a fake file.
   - Material workflow must be metallic-roughness only.

3. Add Sprint 4 validators:
   - Reel ffprobe format.
   - Reel integrity/non-black frames.
   - Hero still resolution/non-black.
   - GIF duration/animation/size/non-black.
   - Manifest schema.
   - Manifest file existence/checksum.
   - LOD summary count.
   - Bundle self-contained check.
   - Failure case for missing/corrupt master video.
   - Write sprint4_gate_summary.json and sprint4_gate_summary.md using the same GateResult pattern.

4. Extend orchestrator/task:
   - Add Sprint 4 stages after master video is available.
   - Suggested progress: derive_reel 90, derive_derivatives 94, build_manifest 97, archive_bundle 99, ready 100.
   - Existing UI should display backend stage labels.
   - Required Sprint 4 failure must prevent ready status.
   - Existing DWG/ODA local skip remains accepted as ready/partial only when explicit.

5. Extend asset registration and Delivery UI:
   - Register marketing_reel, hero_still, gif_preview, manifest, sprint4 gate summaries, optional bundle archive.
   - Delivery page must show links for these final outputs.

Acceptance criteria:
- Product E2E job reaches ready or accepted ready/partial only after Sprint 4 gates pass.
- reel_9x16_1080p.mp4 exists and passes format/integrity gates.
- hero_still_4k.png exists and passes resolution/non-black gates.
- preview.gif exists, animated, 6-10s, <=5 MB, non-black.
- manifest.json validates, all relative paths exist, all SHA-256 checksums match.
- Delivery page shows final Sprint 4 artifact links.
- Existing Sprint 1-3 golden/parity commands still pass.
- Existing product E2E still works from Review page.
- No forbidden scope touched.

Required verification commands:
API:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux

Add and run if implemented:
make sprint4-ci-linux

Web:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build

Local product E2E:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build

Then manually verify through the UI:
- create/open project
- lock/select generated version
- click professional deliverables on Review page
- observe progress through Sprint 4 stages
- open Delivery page
- verify PDF/DXF/GLB/FBX/USDZ/master MP4/reel/hero/GIF/manifest/gate links

If any contract is ambiguous, stop and report NEEDS_CLARIFICATION. Do not guess. If any required local tool is missing, stop and report BLOCKED with exact command, error, elapsed time, and smallest proposed fix.

Report back using:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phase-2/handoffs/sprint-4-final-bundle/05-opencode-report-template.md
```

