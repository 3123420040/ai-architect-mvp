---
title: Sprint 4 Final Bundle Handoff - Decision Log
phase: 2
status: active
date: 2026-04-27
owner: Codex Coordinator
---

# Decision Log

## 2026-04-27 — Local-First Verification

Decision: Sprint 4 continues the local-first git and verification protocol.

Implication:

- No paid GitHub CI required.
- No remote push or PR unless Product Owner asks.
- Local Docker/Linux parity evidence is acceptable.

## 2026-04-27 — Build on Product E2E Baseline

Decision: Sprint 4 builds on the accepted Review page -> professional-worker -> Delivery page flow.

Implication:

- Do not create a separate demo-only path for final bundle.
- Demo commands are allowed, but product E2E must remain the proof path.

## 2026-04-27 — Derive Marketing Assets from Master Video

Decision: Reel, hero still, and GIF must derive from existing `master_4k.mp4`.

Implication:

- No new Blender/Twinmotion/Lumion render for derivatives.
- Use FFmpeg/ffprobe tooling in professional-worker.

## 2026-04-27 — DWG Local Skip Remains Accepted

Decision: Local DWG skip remains allowed when ODA File Converter is not configured.

Implication:

- Missing DWG must be explicit in degraded reasons.
- Do not include fake DWG entries in manifest file inventory.

## 2026-04-27 — Archive Is Conditional

Decision: Final zip archive is desirable because PRD DoD says bundle zips to <500 MB, but it must not force broad storage/product redesign.

Implication:

- Implement archive if it fits the existing asset model.
- Stop and report if archive requires larger architecture change.

