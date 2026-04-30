# H2 Prompt - Harness Core Wrapper

Copy everything below into a new Codex chat session only after H1 is accepted and merged into API `main`.

```text
You are the Harness Core Wrapper Agent for AI Architect.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-core

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
2. Confirm H1 trace support is present.
3. If H1 is not present, stop and report BLOCKED_BY_PENDING_H1_TRACE.

Primary objective:
Introduce `app/services/design_harness/` with `DesignIntakeHarnessLoop`, while preserving existing `/projects/{project_id}/chat` response shape and current product behavior.

Owned files:
- app/services/design_harness/**
- app/services/llm.py
- app/api/v1/chat.py
- app/schemas.py only for optional harness fields
- tests/test_design_harness_loop.py
- tests/test_llm_intake.py
- tests/test_flows.py

Read-only unless required:
- app/services/briefing.py
- app/api/v1/generation.py
- app/services/design_intelligence/**
- app/services/professional_deliverables/**

Hard constraints:
- Do not implement readiness/assumption engine yet beyond pass-through stubs.
- Do not add concept input snapshots yet.
- Do not break existing deterministic fallback.
- Do not change Web.
- Do not push or create PRs.

Tasks:
1. Create `app/services/design_harness/` with:
   - `schemas.py`
   - `loop.py`
   - `context_builder.py`
   - `model_client.py` or adapter around existing `llm.py`
   - `validators.py`
   - `trace_store.py`
2. Move or wrap the current `generate_intake_turn(...)` behavior behind `DesignIntakeHarnessLoop.run(...)`.
3. Keep the old `generate_intake_turn(...)` as a compatibility wrapper if needed.
4. Add `DesignHarnessTurnResult` containing:
   - conversation output;
   - machine output;
   - trace metadata;
   - backward-compatible fields.
5. Update `chat.py` to call the harness loop.
6. Preserve existing `ChatResponse` fields.
7. Add optional `harness` field only if it does not break current tests/UI.
8. Add fake-model/fake-tool tests for:
   - deterministic unconfigured path;
   - configured LLM path through harness;
   - fallback path through harness;
   - old ChatResponse compatibility.

Acceptance criteria:
- `/chat` behavior remains backward-compatible.
- Existing intake tests pass.
- New harness loop is testable without live provider.
- Trace metadata from H1 still exists.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_design_harness_loop.py tests/test_llm_intake.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_flows.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py -q`
- `git diff --check`

Commit locally:
- Suggested message: `feat(ai-harness): wrap intake in harness loop`

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: H2 Harness Core Wrapper
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Compatibility:
- ChatResponse shape:
- Deterministic fallback:
- LLM trace:
- Web impact:

Verification:
- Commands run:
- Focused tests:
- Regression tests:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No Web changes:
- No generation changes:
- No push/PR:

Known issues:
-
```
