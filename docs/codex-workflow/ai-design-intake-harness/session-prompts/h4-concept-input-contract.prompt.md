# H4 Prompt - Concept Input Contract

Copy everything below into a new Codex chat session only after H3 and H5 are accepted and merged into API `main`.

```text
You are the Concept Input Contract Agent for AI Architect.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-concept-input

Main API repo, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs repo, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/02-solution-design-current-code-agentic-os.md

Precondition:
1. Merge current local main: `git merge --no-edit main`.
2. Confirm H3 readiness/assumption contract is present.
3. Confirm H5 style/pattern tool contract is present, or stop with BLOCKED_BY_PENDING_H5_STYLE_TOOLS.

Primary objective:
Add `concept_design_input_v1` compiler, validator, and optional snapshot/handoff API without breaking existing `Project.brief_json` generation.

Owned files:
- app/services/design_harness/compiler.py
- app/services/design_harness/validators.py
- app/services/design_harness/schemas.py
- app/services/design_harness/loop.py
- app/api/v1/ai_harness.py if endpoints are added
- app/api/v1/router.py if endpoints are added
- app/models.py and alembic/versions/** only if durable snapshots are needed
- tests/test_design_harness_compiler.py
- tests/test_design_harness_loop.py
- tests/test_flows.py

Read-only unless required:
- app/api/v1/generation.py
- app/services/gpu_client.py
- app/services/design_intelligence/**
- app/services/professional_deliverables/**

Hard constraints:
- Do not replace generation pipeline.
- Do not require Web changes in this slice.
- Do not emit concept input if critical readiness is missing.
- Do not persist unsafe construction-ready claims.
- Keep `Project.brief_json` as compatibility mirror.
- No push/PR.

Tasks:
1. Define `concept_design_input_v1` schema in code.
2. Implement compiler from:
   - merged brief;
   - harness readiness;
   - assumptions;
   - style intent;
   - reference descriptors;
   - provenance.
3. Validate required fields for:
   - landed house;
   - apartment renovation.
4. Include:
   - `concept_only=true`
   - `construction_ready=false`
   - field provenance for critical fields
   - assumptions requiring confirmation
5. Decide minimal persistence:
   - Prefer storing latest snapshot in harness metadata if enough for this phase.
   - Add tables only if necessary for clean API state.
6. Add endpoint(s) if useful:
   - `GET /projects/{project_id}/ai-harness/state`
   - `POST /projects/{project_id}/ai-harness/emit-concept-input`
7. Add tests for:
   - valid low-communication townhouse with assumptions;
   - blocked missing site dimensions;
   - apartment input;
   - unsafe claims removed/blocked;
   - backward compatibility with `/chat`;
   - snapshot/current state if persisted.

Acceptance criteria:
- Valid concept input JSON can be emitted only when readiness allows.
- Invalid/missing critical data blocks with machine-readable reasons.
- Existing generation tests still pass.
- No unsafe scope claims survive validation.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_design_harness_compiler.py tests/test_design_harness_loop.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_llm_intake.py tests/test_flows.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_model_contract.py tests/test_concept_layout_generator.py tests/test_product_concept_adapter.py -q`
- `git diff --check`

Commit locally:
- Suggested message: `feat(ai-harness): add concept input contract`

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: H4 Concept Input Contract
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Contract coverage:
- Schema:
- Compiler:
- Validator:
- Snapshot/API:
- Backward compatibility:

Verification:
- Commands run:
- Focused tests:
- Regression tests:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No generation replacement:
- No unsafe readiness claims:
- No Web changes:
- No push/PR:

Known issues:
-
```
