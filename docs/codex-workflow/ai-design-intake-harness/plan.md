# AI Design Intake Harness Product Update Plan

Status: tailored

## Decision

Build a server-controlled AI intake harness instead of continuing to expand `app/services/llm.py` as a one-shot LLM helper.

The current code already has:

- deterministic briefing in `app/services/briefing.py`;
- LLM extraction in `app/services/llm.py`;
- style and concept modules under `app/services/design_intelligence/`;
- Concept 2D package output under `app/services/professional_deliverables/`;
- intake/review/generation UI in Web.

The missing product layer is a harness that coordinates these pieces into a safe, auditable, homeowner-friendly flow.

## Goal

At the end of this phase, the repo should be able to run homeowner intake through a harness that can preserve natural chat UX, propose assumptions, compute design readiness, produce validated concept input JSON when ready, and expose that state to UI without breaking existing generation/review/deliverable paths.

## Non-Goals

- No broad backend rewrite.
- No replacement of existing generation, professional deliverables, or Concept 2D modules.
- No construction-ready, permit-ready, legal, structural, MEP, geotech, or code-compliance claims.
- No direct LLM write to DB without server validation.
- No real image analysis claims; reference images remain structured descriptors unless a separate vision phase is approved.
- No production deploy or remote push.

## Workstreams

### H0 - Bootstrap/Worktrees

Create isolated API/Web/docs worktrees from clean local `main`.

### H1 - LLM Trace Observability

Add sanitized trace evidence to the current LLM intake path. This must not change chat behavior.

Key output:

```text
ChatMessage.metadata.harness_trace
```

### H2 - Harness Core Wrapper

Add `app/services/design_harness/` and route `/chat` through `DesignIntakeHarnessLoop` while preserving old response fields.

### H3 - Readiness And Assumptions

Add field-level readiness:

```text
confirmed | inferred | defaulted | missing_critical | missing_optional | conflicting
```

Add homeowner-visible design assumptions with confirmation lifecycle.

### H4 - Concept Input Contract

Add `concept_design_input_v1` compiler/validator and optional snapshot persistence.

### H5 - Style Pattern Tools

Turn existing style KB, pattern memory, dislikes, and reference descriptors into explicit harness tools.

### H6 - UI Assumption Preview Flow

Expose harness state in Web:

- assumptions;
- readiness;
- confirmation CTA;
- preview/generation CTA;
- dev/debug trace visibility only where safe.

### H7 - Evidence And Closeout

Rerun integrated tests and manual browser flows. Write closeout report.

## Merge Order

```text
H1 -> H2 -> H3 -> H5 -> H4 -> H6 -> H7
```

H3 and H5 may run in parallel after H2, but merge H3 first because H5 should adapt to the readiness/assumption contract if conflicts occur.

## Exit Gate

PASS requires:

- API tests:
  - `tests/test_llm_intake.py`
  - `tests/test_flows.py`
  - new design harness tests
  - concept model/layout/product adapter regressions
  - focused professional deliverables concept tests
- Web:
  - `pnpm lint`
  - `pnpm build`
- Browser/manual evidence:
  - natural AI conversation uses provider/fallback trace;
  - low-communication homeowner gets useful assumptions, not a technical interrogation;
  - concept input JSON emits only when ready;
  - UI CTA moves to the next screen when ready;
  - unsafe scope request is blocked safely;
  - existing generation/review/Concept 2D package still works.

Return NEEDS_REVIEW if:

- core harness behavior works but UI copy or non-critical evidence polish remains.

Return BLOCKED if:

- baseline is dirty before worktrees;
- LLM/provider trace cannot be safely persisted without leaking secrets;
- concept input cannot be validated without a broader schema decision;
- integrated main fails existing product flows.
