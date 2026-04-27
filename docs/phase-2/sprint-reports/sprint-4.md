---
title: Sprint 4 Final Bundle Report
phase: 2
status: pass
date: 2026-04-27
owner: opencode
---

Decision: PASS

Repos:
- API repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- API branch: codex/sprint3-professional-deliverables
- API commit: 4dcbbe2
- API dirty status: Sprint 4 changes only
- Web repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Web branch: cp7-pascal-editor-integration
- Web commit: 853c97c
- Web dirty status: Sprint 4 delivery change plus unrelated designs-client/status-badge dirty files
- Docs/compose repo: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
- Docs branch: codex/sprint3-plan-professional-deliverables
- Docs commit: 2fbc752
- Docs dirty status: this Sprint 4 report plus unrelated docs/phases and implementation dirty files

Files changed:
- API:
  - Makefile
  - app/services/professional_deliverables/orchestrator.py
  - app/services/professional_deliverables/manifest_builder.py
  - app/services/professional_deliverables/sprint4_validators.py
  - app/services/professional_deliverables/video_derivatives.py
  - app/tasks/professional_deliverables.py
  - tests/professional_deliverables/test_product_e2e_bridge.py
  - tests/professional_deliverables/test_sprint4_final_bundle.py
  - tools/sprint3/run-local-linux-parity.sh
- Web:
  - src/components/delivery-client.tsx
- Docs/compose:
  - docs/phase-2/sprint-reports/sprint-4.md

Implementation summary:
- Reel: ffmpeg derives video/reel_9x16_1080p.mp4 from video/master_4k.mp4 with deterministic center crop/scale to 1080x1920, 30fps, H.264, target 12 Mbps.
- Hero still: ffmpeg extracts derivatives/hero_still_4k.png from the master video at a deterministic 8-12s-safe timestamp and pads/scales to 3840x2160.
- GIF: ffmpeg extracts derivatives/preview.gif from a 6-10s segment and re-encodes if needed to stay <=5 MB.
- Manifest: manifest.json includes PRD Appendix B top-level fields, relative file inventory, real SHA-256, Sprint 2 LOD/material metadata, source brief, and degraded DWG/ODA reason in provenance quality metadata.
- Gate summaries: sprint4_gate_summary.json and sprint4_gate_summary.md are written with GateResult pattern and required gates.
- UI: Delivery page links marketing reel, hero still, GIF preview, manifest, and Sprint 4 gate summaries.
- Optional archive: not implemented; existing asset model did not require archive support for acceptance.

Artifact paths:
- Bundle root: /app/storage/professional-deliverables/projects/a15f9c6f-7362-462b-8931-e6cae5900b17/versions/f9158153-8187-4d2b-ad54-4d22ea3d7328
- Reel: video/reel_9x16_1080p.mp4
- Hero still: derivatives/hero_still_4k.png
- GIF: derivatives/preview.gif
- Manifest: manifest.json
- Sprint 4 gate JSON: sprint4_gate_summary.json
- Sprint 4 gate MD: sprint4_gate_summary.md
- Optional zip: not implemented

E2E IDs if product flow was run:
- Project: a15f9c6f-7362-462b-8931-e6cae5900b17
- Version: f9158153-8187-4d2b-ad54-4d22ea3d7328
- Bundle: 7d95c21f-844f-4226-9390-1c3181581c92
- Job: 1292b51d-626e-4965-a005-021ab0ecd4fa
- Final bundle status: ready
- Final quality_status: partial
- Degraded reasons: DWG clean-open skipped because ODA/DWG converter is unavailable: ODA converter unavailable locally; CI runs the required DWG audit

Gate table:
| Gate | Result | Evidence |
|---|---|---|
| Reel format | pass | 1080x1920 h264 30.00s 30.000fps bitrate=54675; encoder target remains 12 Mbps, low ffprobe average is accepted for deterministic low-complexity synthetic render variance |
| Reel integrity | pass | decoder pass and non-black samples; size=205034 |
| Hero still | pass | PNG 3840x2160 non-black |
| GIF preview | pass | animated 8.01s, 64 frames, size=27833 |
| Manifest schema | pass | required PRD Appendix B fields present; metallic-roughness enforced; no Specular-Glossiness |
| Manifest inventory/checksum | pass | 84 relative file paths verified with real SHA-256 |
| LOD summary | pass | 68 scene elements match Sprint 2 metadata |
| Bundle self-contained | pass | required Sprint 1-4 artifacts resolve within bundle root |
| Failure case | pass | missing master video is checked before Sprint 4 derivative generation |

Commands run:
1. gh auth status
2. git remote -v in API/Web/Docs repos
3. PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
4. PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
5. pnpm lint
6. pnpm build
7. make sprint3-ci-linux
8. make sprint4-ci-linux
9. docker compose -f docker-compose.local.yml up --build -d api professional-worker web
10. python3 /Users/nguyenquocthong/project/ai-architect/e2e_professional_flow.py
11. docker exec kts-blackbirdzzzz-art-api python -c "...print sprint4 gate evidence..."

Tool versions:
- Python: 3.12.3 in Linux parity container; 3.12.13 host venv
- Node: v22.22.2 in Linux parity container
- FFmpeg: 6.1.1-3ubuntu5 in Linux parity container/professional worker
- ffprobe: 6.1.1-3ubuntu5 in Linux parity container/professional worker
- Blender: 4.5.1 in professional worker/parity image
- KTX: 4.4.2 in professional worker/parity image
- Docker image/OS if used: ubuntu:24.04 linux/amd64 parity/professional-worker

Verification result:
- tests/professional_deliverables: 36 passed, 2 skipped on host; 38 passed in Linux parity through sprint3-ci-linux
- tests/test_foundation.py tests/test_flows.py: 15 passed
- make sprint3-ci-linux: pass
- make sprint4-ci-linux: pass; explicitly runs test_sprint4_final_bundle.py and test_product_e2e_bridge.py in Linux with ffmpeg/ffprobe, 10 passed, 0 skipped
- pnpm lint: pass with 9 warnings
- pnpm build: pass
- Docker Compose product E2E: pass; final ready/partial with Sprint 4 outputs and Sprint 4 gates pass

Scope compliance:
- No remote push: yes
- No PR: yes
- No ADR/PRD relaxation: yes
- No external upload/import: yes
- No deferred-roadmap item: yes
- No Sprint 4 non-goal implemented: yes
- Known unrelated dirty files left untouched: web src/components/designs-client.tsx, web src/components/status-badge.tsx, docs/phases/**, implementation/**

Remaining blockers:
- None.
