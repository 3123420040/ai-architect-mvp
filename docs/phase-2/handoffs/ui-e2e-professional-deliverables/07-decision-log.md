---
title: UI E2E Professional Deliverables Handoff - Decision Log
phase: 2
status: approved-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Decision Log

## 2026-04-27 - Option B Selected

Decision: implement true product E2E from UI click to Phase 2 professional deliverables bundle.

Rationale: The accepted Sprint 1-3 pipeline proves deliverable generation, but the product cannot yet exercise it from a real user/version flow.

## 2026-04-27 - Geometry Source Limited to Current System Output

Decision: first slice supports only `DesignVersion.geometry_json` produced by the current generation system.

Rationale: Import/upload workflows are a different product surface and would expand validation, security, and geometry normalization scope.

## 2026-04-27 - Review Page Required

Decision: Review page must include the trigger and progress bar.

Rationale: The user's mental model is to approve a version and then request professional outputs from the review workflow. Delivery remains the artifact/download workspace.

## 2026-04-27 - Dedicated Professional Worker

Decision: add a dedicated heavy `professional-worker` Docker service.

Rationale: Blender, KTX, FFmpeg, Node, and USD tooling should not bloat the main API container. The pipeline is async and compute-heavy.

## 2026-04-27 - Real 4K MP4 Required

Decision: local E2E must generate actual `master_4k.mp4`, not a preview-only substitute.

Rationale: The PM wants to test the real product deliverable, accepting slower local runtime.

## 2026-04-27 - DWG May Skip Locally

Decision: DWG can be skipped locally when ODA is not configured. PDF, DXF, GLB, FBX, USDZ, and MP4 remain required.

Rationale: ODA setup is external and already treated as special in Sprint 1. Local E2E should remain testable without paid/fragile remote infrastructure.

## 2026-04-27 - Local Git and Docker Verification

Decision: no GitHub paid dependency, no remote push, no PR requirement for this task.

Rationale: The PM selected local-first workflow. Docs and local verification are the source of truth for this phase.

## 2026-04-27 - UI E2E Professional Deliverables Accepted

Decision: ACCEPTED.

Rationale: Local Docker product E2E successfully generated Phase 2 bundle from a real generated/locked DesignVersion.geometry_json. All required non-DWG outputs were produced and registered. DWG skip is accepted because ODA is unavailable locally.

## 2026-04-27 - Remediation Defaults Approved

Decision: use the remediation recommendations from `11-remediation-execution-playbook.md` as approved implementation defaults.

Approved defaults:

- Asset access: use API proxy or presigned URL helper. Do not rely on raw private MinIO URLs. Do not use public MinIO bucket as the product default.
- Partial artifacts: allow download of generated artifacts from failed/partial bundles when the individual artifact is valid. Label them clearly as `Partial / not final`.
- Viewer: allow the Viewer to display a professional deliverables GLB from a failed/partial bundle when the GLB itself is valid. Show a warning that the bundle is not final.
- Current version: latest `locked` version is the source of truth for the current approved version. All Designs, Review, Delivery, and Viewer pages must use the same rule.
- Intake: fix the deterministic parser first for known Vietnamese natural-language failures. Do not require real LLM extraction in this remediation unless a later PM decision explicitly changes scope.

Rationale: These defaults keep the remediation local-first, avoid broadening scope, preserve observability for partially generated evidence, and prioritize a correct product state model before deeper AI/NLU expansion.
