# H1 Prompt - LLM Trace Observability

Copy everything below into a new Codex chat session only after H0 reports `AI_DESIGN_INTAKE_HARNESS_WORKTREES_READY`.

```text
You are the LLM Trace Observability Agent for AI Architect.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/ai-harness-trace

Main API repo, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Docs repo, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/ai-design-intake-harness/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/output/ai-harness-design/02-solution-design-current-code-agentic-os.md

Source files to inspect:
- app/services/llm.py
- app/api/v1/chat.py
- app/services/briefing.py
- app/schemas.py
- app/models.py
- tests/test_llm_intake.py
- tests/test_flows.py

Primary objective:
Add sanitized LLM/harness trace observability to the current intake path without changing user-visible chat behavior.

Owned files:
- app/services/llm.py
- app/api/v1/chat.py
- app/schemas.py if optional response fields are needed
- tests/test_llm_intake.py
- tests/test_flows.py

Read-only unless absolutely required:
- app/services/briefing.py
- app/services/design_intelligence/**
- app/services/professional_deliverables/**
- app/api/v1/generation.py

Hard constraints:
- Do not add new harness behavior yet.
- Do not change the existing ChatResponse required fields.
- Do not change generation/review/professional deliverables.
- Do not persist raw API keys, Authorization headers, or secret-like values.
- Do not print the OpenAI-compatible key.
- Do not weaken deterministic fallback.
- Do not push or create PRs.

Tasks:
1. Merge current local API main: `git merge --no-edit main`.
2. Inspect current intake tests and source.
3. Add a sanitized trace structure for every AI turn, preferably under assistant `ChatMessage.message_metadata["harness_trace"]`.
4. Trace should include:
   - source: llm_openai_compat | deterministic | deterministic_fallback
   - provider family, never key
   - model
   - prompt_id
   - sanitized request summary
   - recent history count, not full unbounded transcript
   - deterministic draft summary
   - LLM response byte count if provider was called
   - parsed payload summary
   - validation gates
   - fallback reason if any
   - merged brief changed keys
5. If useful, expose the same sanitized trace in `assistant_payload.source_metadata.trace_summary`.
6. Add tests proving:
   - configured LLM turn records trace summary;
   - invalid JSON fallback records fallback reason;
   - deterministic unconfigured path records deterministic trace;
   - secret-like strings are redacted;
   - existing chat flow response shape remains compatible.
7. Do not add new DB tables in H1 unless there is no safe metadata path.

Acceptance criteria:
- Existing chat behavior and response shape remain compatible.
- Latest chat history has sanitized trace metadata for AI messages.
- Tests prove no raw key/Authorization value is persisted.
- `tests/test_llm_intake.py` and `tests/test_flows.py` pass.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_llm_intake.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_flows.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py -q`
- `git diff --check`

Commit locally:
- Suggested message: `feat(ai-harness): add sanitized intake llm traces`

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: H1 LLM Trace Observability
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Trace coverage:
- Provider call:
- Prompt id:
- Parsed payload:
- Validation gates:
- Fallback:
- Redaction:

Verification:
- Commands run:
- Focused tests:
- Regression tests:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- Existing ChatResponse preserved:
- No raw secrets persisted:
- No generation/review changes:
- No push/PR:

Known issues:
-
```
