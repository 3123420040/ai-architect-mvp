---
title: Sprint 4 Final Bundle Handoff - Review Checklist
phase: 2
status: ready-for-opencode-handoff
date: 2026-04-27
owner: Codex Coordinator
---

# Review Checklist

Use this checklist when opencode reports back.

## Scope

- Only Sprint 4 final bundle outputs were added.
- Reel/hero/GIF derive from `master_4k.mp4`.
- No scene re-render was added for derivatives.
- No remote push or PR.
- No ADR/PRD relaxation.
- No deferred-roadmap item was implemented.
- Known unrelated dirty files were left untouched.

## Outputs

- `video/reel_9x16_1080p.mp4` exists.
- `derivatives/hero_still_4k.png` exists.
- `derivatives/preview.gif` exists.
- `manifest.json` exists.
- `sprint4_gate_summary.json` exists.
- `sprint4_gate_summary.md` exists.
- Optional bundle archive exists only if implemented inside existing storage model.

## Gates

- Reel format passes ffprobe checks.
- Reel integrity passes non-black and decoder checks.
- Hero still is 3840x2160 PNG and non-black.
- GIF is animated, 6-10s, <= 5 MB, and non-black.
- Manifest validates against PRD Appendix B.
- Manifest file inventory has relative paths only.
- Manifest SHA-256 checksums match actual files.
- LOD summary count matches scene metadata.
- Missing/corrupt master video failure case is covered.

## Product E2E

- Review page still triggers professional deliverables job.
- Progress shows Sprint 4 stages or generic backend stage labels.
- Heavy work remains async in professional-worker.
- Delivery page shows Sprint 4 artifact links.
- Bundle is not marked ready if required Sprint 4 output fails.
- DWG skip remains explicit and partial/degraded when ODA is unavailable.

## Regression

- Sprint 1-3 golden/parity commands still pass.
- Existing product E2E accepted flow still works.
- Web lint/build pass.
- API foundation/flows pass.

## Review Decision

Return `ACCEPTED` only if all acceptance criteria pass.

Return `NEEDS_FIX` if implementation violates scope, misses an output, weakens gates, or registers invalid artifacts.

Return `NEEDS_MORE_TESTS` if implementation appears correct but verification is insufficient.

Return `NEEDS_CLARIFICATION` if a product decision is needed.

