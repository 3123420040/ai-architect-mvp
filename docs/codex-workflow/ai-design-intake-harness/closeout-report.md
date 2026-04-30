# AI Design Intake Harness Closeout Report

Decision: PASS

## Scope

- Session: H7 Evidence And Closeout
- Docs branch/worktree: `codex/ai-harness-closeout` at `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/.worktrees/ai-harness-closeout`
- API branch/commit: `main` / `9c121cd` (`merge: accept ai harness concept input contract`)
- Web branch/commit: `main` / `59b3246` (`merge: accept ai harness ui assumption preview`)
- Docs branch/commit: `codex/ai-harness-closeout` / this local H7 closeout commit; integrated docs `main` was fast-forwarded to `8ae7f65` before closeout docs edits.
- Owned files changed:
  - `docs/codex-workflow/ai-design-intake-harness/closeout-report.md`
  - `docs/codex-workflow/ai-design-intake-harness/ledger.md`
- Shared files changed: none

## Integrated State

- H1 merge present: yes, API `6bcbc35 merge: accept ai harness trace observability`
- H2 merge present: yes, API `97b7043 merge: accept ai harness core wrapper`
- H3 merge present: yes, API `f9c0828 merge: accept ai harness readiness assumptions`
- H4 merge present: yes, API `9c121cd merge: accept ai harness concept input contract`
- H5 merge present: yes, API `07a2c67 merge: accept ai harness style pattern tools`
- H6 merge present: yes, Web `59b3246 merge: accept ai harness ui assumption preview`

## Summary

- Implemented: server-controlled intake harness, sanitized trace metadata, field readiness, homeowner-visible assumptions, style/pattern tools, validated `concept_design_input_v1`, AI harness state/emit routes, and Web harness preview/CTA.
- Not implemented: no product fixes were implemented during H7.
- Deferred: durable concept-input snapshot tables and live vision/image analysis remain deferred by phase scope; concept input snapshots are stored in latest AI message harness metadata.

## Dirty Status

- API: clean, `main...origin/main [ahead 11]`
- Web: clean after removing the generated Playwright CLI scratch folder created during browser verification, `main...origin/main [ahead 3]`
- Docs main: clean, `main...origin/main [ahead 6]`
- Closeout worktree before docs edit: clean on `codex/ai-harness-closeout`, fast-forwarded to `8ae7f65`
- Closeout worktree after docs edit: dirty only in owned docs files until the local H7 closeout commit

## Verification

- API tests:
  - `PYTHONPATH=. .venv/bin/python -m pytest tests/test_llm_intake.py tests/test_flows.py -q` -> 19 passed, dependency deprecation warnings only.
  - `PYTHONPATH=. .venv/bin/python -m pytest tests/test_design_harness_loop.py tests/test_design_harness_readiness.py tests/test_design_harness_style_tools.py tests/test_design_harness_compiler.py -q` -> 24 passed, dependency deprecation warnings only.
  - `PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_model_contract.py tests/test_concept_layout_generator.py tests/test_product_concept_adapter.py -q` -> 22 passed, dependency deprecation warnings only.
  - `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_ai_concept_2d_e2e.py tests/professional_deliverables/test_concept_2d_live_integration.py -q` -> 16 passed, dependency deprecation warnings only.
- Web lint/build:
  - `pnpm lint` -> pass with 5 existing warnings in files outside the H6 changed file.
  - `pnpm build` -> pass.
- Browser/manual:
  - Temporary API on `127.0.0.1:18080` with temp SQLite/storage and Web on `127.0.0.1:3100`.
  - Registered via Web, created project, opened intake, sent low-communication townhouse message, then fuller details, then remaining confirmation details.
  - Browser showed assumptions, critical missing guidance, valid concept data, `Chốt brief và xem Phương án` CTA, and navigation to `/designs` with locked brief and generation button.
- Evidence files:
  - This closeout report and merged ledger are the evidence summary.
  - No worker evidence was used as final truth; all commands above were rerun on integrated local `main` or the H7 closeout worktree.

## Product Evidence

- LLM trace:
  - API trace persistence check confirmed public chat response omits raw `harness_trace`.
  - Chat history metadata persisted `harness_trace_summary_v1` with source `deterministic`, provider family `none`, gates `deterministic_analysis`, `llm_configured`, `deterministic_merge`, and `style_pattern_tools`.
  - Trace summary in `assistant_payload.source_metadata.trace_summary` matched persisted metadata.
  - No `sk-` secret markers appeared in persisted trace summary.
- Harness loop:
  - Direct harness runs used deterministic path with LLM disabled and returned `design_intake_harness` legacy-compatible output.
- Readiness:
  - Low-communication townhouse: `missing_critical`; confirmed `project_type`, `site.width_m`, `site.depth_m`; critical gaps `floors`, `program.bedrooms`, `program.bathrooms`; concept input blocked.
  - Full townhouse: `partial_with_assumptions`; confirmed floors, bedrooms, bathrooms, width/depth; `concept_design_input_v1` available and validation `valid`.
  - Apartment renovation area/style only: `missing_critical`; confirmed `project_type=apartment_reno`, `site.area_m2`, `style`; critical gaps `renovation_scope`, `program.bedrooms`, `program.bathrooms`; concept input blocked.
- Assumptions:
  - Low-communication townhouse proposed assumptions from `pattern_memory` for floors/bedrooms/bathrooms and defaults for project mode/style.
  - Apartment renovation proposed apartment-specific defaults for renovation scope and program assumptions.
  - Full townhouse kept project mode/style assumptions visible for confirmation.
- Style/pattern tools:
  - Trace gates included `style_pattern_tools`; full townhouse produced style assumptions, and the later browser flow inferred tropical-modern direction from green/natural/light/ventilation wording.
- Concept input JSON:
  - Full townhouse emitted `concept_design_input_v1`, `project.concept_only=true`, `project.construction_ready=false`, `site.kind=land_lot`, validation `valid`.
  - Missing-critical and unsafe cases did not emit concept input.
- UI CTA:
  - Web intake preview showed `Kiểm tra: blocked` for missing data, `Kiểm tra: valid` after fuller details, then `Chốt brief và xem Phương án`.
  - Clicking the CTA emitted concept input, locked the brief, and navigated to `/projects/{id}/designs`.
- Existing generation/review:
  - API manual flow locked brief, generated 2 options, selected a version, approved review, exported package artifacts with quality `pass`, and created a professional-deliverables bundle/job.
- Unsafe-scope handling:
  - Unsafe construction/permit/legal/MEP readiness request returned `blocked_by_safety_scope`, conflicting field `safety_scope.unsafe_request`, `safe_to_emit_concept_input=false`, concept input blocked, and no `construction_ready` or `permit_ready` field entered `brief_json`.

## Residual Risk

- Flakes: none observed in H7 reruns.
- Known gaps:
  - No live provider call was made during H7; deterministic provider-disabled path was used to avoid key exposure and keep evidence reproducible.
  - Browser verification used temporary local API/Web ports because `18000` and `3000` were already occupied by an existing Docker listener.
  - Web lint still reports 5 existing warnings unrelated to the H6 changed file.
  - Manual professional-deliverables route evidence stopped at queued bundle/job; required integrated tests separately verified Concept 2D/professional deliverables package behavior.

## Contract Compliance

- No push/PR: complied.
- No worker evidence as final truth: complied; integrated commands and manual checks were rerun in H7.
- No unsafe readiness claims: complied; concept inputs and unsafe case keep `construction_ready=false` or block emission.
- Existing product flow preserved: complied; tests and manual API flow passed.

## Known Issues

- Existing Web lint warnings remain:
  - `src/components/asset-image.tsx`: `<img>` warning.
  - `src/components/dashboard-client.tsx`: `<img>` warning.
  - `src/components/delivery-client.tsx`: `<img>` warning.
  - `src/components/viewer-client.tsx`: missing `useEffect` dependency and `<img>` warning.
