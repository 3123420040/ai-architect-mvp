---
title: Sprint 4 Final Bundle Handoff - Context
phase: 2
status: ready-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
related:
  - docs/phase-2/03-adr-001-standards-combo.md
  - docs/phase-2/04-deferred-roadmap.md
  - docs/phase-2/05-prd-deliverables.md
  - docs/phase-2/07-local-git-verification-protocol.md
  - docs/phase-2/08-current-state-and-next-actions.md
---

# Context

Sprint 1, Sprint 2, Sprint 3, and the first product E2E slice are accepted.

The current local product flow can generate a Phase 2 professional deliverables bundle from a selected system-generated `DesignVersion.geometry_json` and show artifact links on the Delivery page.

Accepted product E2E output currently includes:

- `/2d/bundle.pdf`
- `/2d/*.dxf`
- `/3d/model.glb`
- `/3d/model.fbx`
- `/3d/model.usdz`
- `/video/master_4k.mp4`
- gate summary JSON/Markdown

Local DWG may be skipped when ODA is not configured. That skip is accepted only when explicit and when the bundle is marked degraded/partial.

## Sprint 4 Purpose

Sprint 4 closes the remaining PRD canonical bundle gaps:

- marketing reel
- hero still
- GIF preview
- final `manifest.json`
- final self-contained bundle/archive validation

Sprint 4 is a completion and packaging slice. It must build on the accepted product E2E pipeline and must not reopen the 2D, 3D, USDZ, or master-video architecture unless required to register final artifacts.

## Local-First Constraint

The Product Owner does not want paid GitHub CI. Verification must run locally using the active local protocol.

Required evidence should be produced through:

- local unit/integration tests
- local Docker Compose E2E
- local Linux parity where needed
- local git commits only when Product Owner later asks for commit

No remote push or PR unless Product Owner explicitly requests it.

## Repos

- API: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Web: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`
- Docs/compose: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`

## Baseline Commits

- API: `4dcbbe2 feat(deliverables): connect professional bundle product flow`
- Web: `853c97c feat(delivery): trigger professional deliverables from review`
- Docs/compose: `2fbc752 docs(phase-2): sign off local professional deliverables e2e`

## Known Dirty Files

Do not touch these unless explicitly assigned:

- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/components/designs-client.tsx`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/src/components/status-badge.tsx`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/phases/**`
- `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/implementation/**`

