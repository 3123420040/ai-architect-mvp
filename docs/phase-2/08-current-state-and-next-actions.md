---
title: Phase 2 Current State and Next Actions
phase: 2
status: active-source-of-truth
date: 2026-04-27
owner: Codex Coordinator
related:
  - docs/phase-2/03-adr-001-standards-combo.md
  - docs/phase-2/04-deferred-roadmap.md
  - docs/phase-2/05-prd-deliverables.md
  - docs/phase-2/07-local-git-verification-protocol.md
  - docs/phase-2/09-github-account-migration.md
  - docs/phase-2/handoffs/ui-e2e-professional-deliverables/08-local-e2e-signoff.md
  - docs/phase-2/handoffs/sprint-4-final-bundle/
---

# Phase 2 Current State and Next Actions

This file is the quick handoff entrypoint for any agent joining the AI Architect Phase 2 Professional Deliverables workstream.

## Operating Model

The project is running in a local-first coordination model:

- Codex acts as Principal Coordinator, Requirement Architect, and Handoff Owner.
- opencode acts as implementation and verification agent.
- Product Owner copies Codex prompts into opencode and returns opencode reports.
- GitHub Actions, remote PRs, and remote push are optional only. They are not required for acceptance.
- Local L2 Linux parity is the preferred replacement for `ubuntu-latest` verification.

Source-of-truth priority:

1. `docs/phase-2/03-adr-001-standards-combo.md`
2. `docs/phase-2/05-prd-deliverables.md`
3. `docs/phase-2/07-local-git-verification-protocol.md`
4. Sprint reports and handoff docs
5. Chat history

## Accepted Baseline

### Sprint 1 — 2D Foundation

Accepted.

Delivered:

- DXF/DWG exporter path with AIA layer dictionary.
- PDF bundled sheet set with Vietnamese labels and embedded font.
- Sheet strategy with per-floor `A-101-F<N>` output.
- Local gate result pattern using JSON/Markdown summaries.

Local DWG can be skipped when ODA File Converter is not configured, but the skip must be explicit and quality must be marked degraded/partial.

### Sprint 2 — 3D Core Formats

Accepted.

Delivered:

- `model.glb` glTF 2.0, Metal-Roughness only, Draco/KTX2 pipeline.
- `model.fbx` Twinmotion preset path.
- `/textures/` KTX2 texture layout.
- Dynamic validation infrastructure for GLB/FBX/material policy.

Forbidden remains: Specular-Glossiness, procedural materials, external model upload/import.

### Sprint 3 — AR + Master Video

Accepted.

Delivered:

- `model.usdz` derived from Sprint 2 `model.glb`.
- `master_4k.mp4`, 3840x2160, 30fps, 60s.
- Local Linux parity runner with Blender/KTX/FFmpeg/USD tooling.
- Gate summaries for USDZ and master video.

Sprint 3 does not include reel, hero still, GIF, or final `manifest.json`.

### Product E2E Slice — UI to Professional Bundle

Accepted.

Scope:

```text
Review page click -> async professional-worker -> bundle from selected DesignVersion.geometry_json -> Delivery page artifact links
```

Accepted E2E evidence:

- Project: `4cec7b39-d892-4386-a3b0-1a4ac896b8b0`
- Version: `2564d91c-cac5-4e82-b30e-9e2ba3537ba3`
- Bundle: `478293e2-6b7b-4d6d-9c77-3947c81ccf03`
- Job: `08b5e666-3a91-4810-8993-924a5986fe9d`
- Final bundle status: `ready`
- Final quality status: `partial`
- Partial reason: DWG/ODA unavailable locally.

Verified artifacts:

- PDF
- DXF
- GLB
- FBX
- USDZ
- MP4 master
- Gate JSON
- Gate MD
- DWG skipped with explicit ODA reason

## Local Git Baseline

Repos:

- API: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Web: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`
- Docs/compose: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`

Canonical GitHub account after migration:

- `3123420040`

Canonical public remotes:

- `https://github.com/3123420040/ai-architect-api`
- `https://github.com/3123420040/ai-architect-web`
- `https://github.com/3123420040/ai-architect-gpu`
- `https://github.com/3123420040/ai-architect-mvp`

See `docs/phase-2/09-github-account-migration.md` for remote policy.

Accepted local commits:

- API: `4dcbbe2 feat(deliverables): connect professional bundle product flow`
- Web: `853c97c feat(delivery): trigger professional deliverables from review`
- Docs/compose: `2fbc752 docs(phase-2): sign off local professional deliverables e2e`

Known unrelated dirty files to leave untouched unless Product Owner explicitly assigns them:

- Web: `src/components/designs-client.tsx`
- Web: `src/components/status-badge.tsx`
- Docs/compose: `docs/phases/**`
- Docs/compose: `implementation/**`

## Current Product Capability

The product can now run a real local E2E flow:

1. User creates or opens a project.
2. User generates a design version from the current system.
3. User locks/approves the generated version.
4. User clicks professional deliverables on the Review page.
5. API creates an async professional deliverables job.
6. Dedicated `professional-worker` processes the bundle.
7. UI progress bar updates through the job stages.
8. Delivery page shows artifact links after completion.

Current output is useful for:

- Client concept review.
- Architect/engineer handoff at concept/schematic level.
- 3D model handoff to web/AR/Twinmotion-style tools.
- Local proof that Phase 2 generation can run from UI instead of demo-only CLI.

Current output is not yet complete for the final PRD bundle because Sprint 4 outputs are still missing.

## Remaining Phase 2 Gap

Sprint 4 must close the canonical bundle:

```text
/video/reel_9x16_1080p.mp4
/derivatives/hero_still_4k.png
/derivatives/preview.gif
/manifest.json
optional or required final bundle archive, depending on implementation contract
```

Sprint 4 must derive video artifacts from the existing `master_4k.mp4`. It must not re-render the scene unless Product Owner approves a separate scope.

## Next Action

Use this handoff folder for the next opencode task:

```text
docs/phase-2/handoffs/sprint-4-final-bundle/
```

Start with:

- `00-context.md`
- `01-requirements.md`
- `02-system-analysis.md`
- `03-implementation-contract.md`
- `04-opencode-prompt.md`

Do not start implementation without following the contract in that folder.
