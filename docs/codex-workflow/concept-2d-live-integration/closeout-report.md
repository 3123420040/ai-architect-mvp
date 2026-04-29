# C2DL5 Closeout Acceptance Report

Decision: PASS

Scope:
- Session: C2DL5 Closeout Acceptance
- API branch/commit: `main` / `083bdb7`
- Web branch/commit: `main` / `a0d060c`
- Docs branch/commit: `main` / `51d9049` before this report
- Owned files changed: `docs/codex-workflow/concept-2d-live-integration/closeout-report.md`
- Shared files changed: none

Integrated state:
- C2DL1 merge present: yes, API `codex/concept-2d-live-contract` is an ancestor of `main`
- C2DL2 merge present: yes, API `codex/concept-2d-live-deliverables` is an ancestor of `main`
- C2DL3 merge present: yes, Web `codex/concept-2d-live-ui` is an ancestor of `main`
- C2DL4 merge present: yes, API `codex/concept-2d-live-evidence` is an ancestor of `main`

Summary:
- Implemented: integrated local `main` now generates the live Concept 2D package from the locked product version, with 11 PDF pages, 11 physical DXF sheets, ready concept package metadata, quality report links, and Review/Delivery UI exposure.
- Not implemented: no new code changes were made during closeout.
- Deferred: DWG clean-open remains a local ODA-converter skip with explicit warning; CI remains responsible for the DWG audit.

Verification:
- API professional_deliverables: `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q` -> 74 passed, 2 skipped
- API foundation/flows: `PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q` -> 15 passed
- sprint3-ci-linux: `make sprint3-ci-linux` -> passed; parity container reported 76 passed in both Sprint 2 and Sprint 3 suites
- Web lint/build: `pnpm lint` -> 0 errors, 5 existing warnings; `pnpm build` -> passed
- Docker rebuild: `docker compose -f docker-compose.local.yml up -d --build` -> built and restarted API/Web/worker/professional-worker/GPU

Manual review evidence:
- Project id: `56e4c77f-5f46-4506-af8c-df88362aad34`
- Version id: `5e6b84dd-5e4c-419d-a00a-b4f9b54918ee`
- Bundle/job id: bundle `51884d82-7ca8-4166-93b7-e8a63f66a495`, job `06138f8b-ba35-4bf3-b4ec-34d1ca6fd16d`
- Review URL: `http://localhost:3000/projects/56e4c77f-5f46-4506-af8c-df88362aad34/review`
- PDF URL/path: `http://localhost:18000/media/professional-deliverables/projects/56e4c77f-5f46-4506-af8c-df88362aad34/versions/5e6b84dd-5e4c-419d-a00a-b4f9b54918ee/2d/bundle.pdf`; container path `/app/storage/professional-deliverables/projects/56e4c77f-5f46-4506-af8c-df88362aad34/versions/5e6b84dd-5e4c-419d-a00a-b4f9b54918ee/2d/bundle.pdf`
- DXF directory/path: `/app/storage/professional-deliverables/projects/56e4c77f-5f46-4506-af8c-df88362aad34/versions/5e6b84dd-5e4c-419d-a00a-b4f9b54918ee/2d`
- Quality report paths: `/app/storage/professional-deliverables/projects/56e4c77f-5f46-4506-af8c-df88362aad34/versions/5e6b84dd-5e4c-419d-a00a-b4f9b54918ee/2d/artifact_quality_report.json` and `.md`
- PDF page count: 11 pages, all pages A3 landscape `1190.55 x 841.89` pt
- Expected concept sheet tokens: present in PDF and UI/API metadata: `A-000`, `A-100`, `A-101-F1`, `A-101-F2`, `A-101-F3`, `A-101-F4`, `A-201`, `A-301`, `A-601`, `A-602`, `A-901`, `Professional Concept 2D Package`, room/area schedule, door/window schedule, assumptions/style notes
- Stale dimension result: stale `Ranh dat 5 m x 15 m` / `Ranh đất 5 m x 15 m` absent; selected geometry present as `5 m x 20 m`, `5.00 m`, `20.00 m`, and quality report `qa_bounds.lot_width_m=5.0`, `lot_depth_m=20.0`
- UI link/status evidence: Review and Delivery snapshots both show `Professional Deliverables`, `Concept 2D package`, PDF bundle link, all 11 DXF sheet links, quality report JSON/MD links, `Ready 100%`, and partial bundle warning for local DWG skip

Residual risk:
- Flakes: none observed in reruns.
- Known gaps: local DWG clean-open remains skipped because ODA/DWG converter is unavailable; Web Playwright console showed a non-blocking missing Presentation 3D `404` and minified React hydration warning while the Review/Delivery content still rendered the required links/status.

Contract compliance:
- No push: yes
- No PR: yes
- No unsafe construction/permit/MEP/legal claims: yes; generated PDF is marked concept review only / not for construction
- Selected-version geometry preserved: yes, locked version geometry remains `5 m x 20 m` in generated PDF text and quality metadata
- Worker evidence not used as final truth: yes, closeout reran tests, Docker rebuild, live API job, physical artifact inspection, and browser UI snapshots from integrated local `main`

Known issues:
- Bundle `quality_status` is `partial` because local DWG clean-open is skipped, not because Concept 2D package generation failed. Concept package metadata is `enabled=true`, `readiness=ready`, `sheet_count=11`, and `fallback_reason=null`.
