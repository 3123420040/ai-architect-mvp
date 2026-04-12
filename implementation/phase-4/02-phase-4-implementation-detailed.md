# Phase 4 Implementation Detailed

## 1. Capability Contract

Phase 4 introduces four new working objects:

1. structured brief,
2. clarification state,
3. design-direction board,
4. confirmation-ready brief.

## 2. Backend Changes

### 2.1 Brief parsing

The backend must parse and persist at least:

- project type,
- project mode,
- site size and orientation,
- floors,
- room counts,
- household profile,
- lifestyle priorities,
- style direction,
- material direction,
- color direction,
- budget,
- timeline,
- special requests,
- must-haves,
- must-not-haves.

### 2.2 Clarification state

The backend must return a reusable `clarification_state` object from:

- project detail,
- brief get/update,
- chat turn response.

Required fields:

- readiness label,
- completion ratio,
- completed section count,
- blocking missing list,
- advisory missing list,
- next questions,
- per-section detail,
- summary.

### 2.3 Chat reliability

The intake chat path must:

- not depend on multiple slow LLM round trips,
- fall back safely when LLM is slow,
- keep the user flow responsive in production.

## 3. Frontend Changes

### 3.1 Intake workspace

Replace the current intake emphasis:

- from raw JSON-first
- to guided clarification-first.

### 3.2 UI blocks

Required Phase 4 UI blocks:

- AI clarification workspace,
- progress / readiness indicator,
- section-by-section requirement board,
- design-direction board,
- advanced technical editor for KTS.

### 3.3 Language

The Phase 4 intake experience must use Vietnamese with diacritics for:

- section names,
- button labels,
- helper text,
- readiness guidance.

## 4. Cross-Phase Integration

Phase 4 must hand off a better brief into the existing Phase 3 path.

The following must remain compatible:

- `/generate`,
- review / lock,
- package preview,
- package issue,
- handoff.

## 5. Quality Bar

Phase 4 is acceptable only if:

- local tests pass,
- web production build passes,
- deploy succeeds,
- production loops still pass after the intake changes,
- no regression is introduced into the Phase 3 package flow.
