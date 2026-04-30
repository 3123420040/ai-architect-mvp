# H3 Prompt - Readiness And Assumptions

Copy everything below into a new Codex chat session only after H2 is accepted and merged into API `main`.

```text
You are the Readiness And Assumptions Agent for AI Architect.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-readiness

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
2. Confirm `app/services/design_harness/` exists.
3. If H2 is absent, stop and report BLOCKED_BY_PENDING_H2_HARNESS_CORE.

Primary objective:
Add field-level readiness and homeowner-visible design assumptions to the harness machine output, without changing generation behavior.

Owned files:
- app/services/design_harness/readiness.py
- app/services/design_harness/schemas.py
- app/services/design_harness/loop.py
- app/services/design_harness/validators.py
- tests/test_design_harness_readiness.py
- tests/test_design_harness_loop.py
- tests/test_flows.py

Read-only unless required:
- app/services/briefing.py
- app/services/design_intelligence/**
- app/api/v1/generation.py

Hard constraints:
- Do not add concept input snapshot persistence yet.
- Do not change Web.
- Do not trigger generation automatically.
- Do not label inferred/defaulted data as confirmed facts.
- Do not claim construction/permit/legal/MEP/geotech/code readiness.

Tasks:
1. Add `DesignHarnessReadiness` with field statuses:
   - confirmed
   - inferred
   - defaulted
   - missing_critical
   - missing_optional
   - conflicting
2. Add `DesignAssumption` schema with:
   - id
   - field_path
   - value
   - source: user | llm | deterministic | style_profile | pattern_memory | default
   - confidence
   - needs_confirmation
   - explanation
   - status: proposed | confirmed | rejected | superseded
3. Compute readiness for:
   - landed house/townhouse/villa/shophouse/home-office;
   - apartment renovation.
4. Map current `build_clarification_state(...)` into the richer harness readiness without removing old fields.
5. For low-communication briefs, propose assumptions instead of asking too many technical questions.
6. Keep critical missing site/program fields blocking concept input.
7. Include readiness/assumptions in optional `harness` response metadata and AI message metadata.
8. Add tests for:
   - low-communication 5x20 townhouse;
   - apartment area-only brief;
   - missing site geometry blocker;
   - inferred style needing confirmation;
   - confirmed facts not downgraded;
   - unsafe scope remains blocked.

Acceptance criteria:
- Existing `clarification_state` still works.
- Harness readiness has field-level evidence.
- Assumptions are visible and provenance-tagged.
- No downstream generation behavior changed.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_design_harness_readiness.py tests/test_design_harness_loop.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_llm_intake.py tests/test_flows.py -q`
- `git diff --check`

Commit locally:
- Suggested message: `feat(ai-harness): add intake readiness assumptions`

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: H3 Readiness And Assumptions
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Readiness coverage:
- Landed house:
- Apartment:
- Low-communication defaults:
- Critical blockers:
- Assumption provenance:

Verification:
- Commands run:
- Focused tests:
- Regression tests:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No generation trigger:
- No Web changes:
- No unsafe readiness claims:
- No push/PR:

Known issues:
-
```
