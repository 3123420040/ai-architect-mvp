# AI Needs Clarification Product Requirements

## 1. Goal of the Capability

Build a professional AI-assisted clarification system that turns vague client input into:

- a structured requirement brief,
- a visible clarification state,
- a design-direction board,
- and a confirmation-ready package for downstream 2D / 3D generation.

## 2. Target User and Use Case

Primary user:

- architect,
- residential designer,
- design-build operator,
- BA / PM supporting early-stage requirement locking.

Secondary user:

- end client reviewing and confirming scope.

Core use case:

1. Collect rough project intent
2. Clarify requirements section by section
3. Show missing information and assumptions
4. Build a design-direction board
5. Confirm the locked brief
6. Hand off to design generation

## 3. Recommended End-to-End Workflow

### Stage 1: intake

Input sources:

- AI chat,
- structured form,
- optional notes or references in later extensions.

Output:

- initial brief draft,
- first clarification score,
- list of missing sections.

### Stage 2: clarification loop

System behavior:

- ask focused follow-up questions,
- group information by section,
- expose contradictions and missing items,
- summarize after each update.

Output:

- enriched brief,
- clarification board,
- recommended next questions.

### Stage 3: design-direction board

System behavior:

- summarize goals,
- map style and material direction,
- surface do / do-not guidance,
- package a client-facing requirement board.

Output:

- design board / requirement board draft.

### Stage 4: confirmation

System behavior:

- mark brief as ready only when core sections are complete,
- preserve missing-but-advisory items separately,
- require explicit confirmation.

Output:

- confirmed brief,
- locked clarification state,
- downstream handoff-safe payload.

## 4. Required Input Data

The system must support:

- project type,
- project mode: new build or renovation,
- site width/depth/area,
- site orientation,
- floor count target,
- room program basics,
- household / usage profile,
- lifestyle priorities,
- style direction,
- material direction,
- color direction,
- budget band,
- timeline target,
- special requests,
- must-haves,
- must-not-haves,
- freeform notes.

## 5. Required AI Behaviors

AI must:

- ask progressively rather than dumping a long questionnaire,
- classify information into requirement sections,
- detect missing critical sections,
- summarize in Vietnamese clearly,
- expose what still needs confirmation,
- fall back safely if the LLM path is slow or unavailable.

AI may:

- normalize terminology,
- infer question order,
- suggest candidate tags for style and lifestyle.

AI must not:

- invent site facts,
- infer compliance,
- imply permit readiness,
- turn style references into technical certainty without confirmation.

## 6. Required User Confirmation Steps

The user must be able to:

- review clarification completeness,
- inspect blocking missing items,
- inspect advisory missing items,
- edit the brief manually,
- confirm the brief before generation.

## 7. Required Output Artifacts

The system must generate:

1. Structured brief JSON
2. Clarification state
3. Design-direction board
4. Confirmation-ready summary

## 8. Required Design Board Elements

The design board must include:

- project overview,
- user goals,
- household / usage summary,
- program priorities,
- style direction,
- material direction,
- color direction,
- precedent / reference zone,
- must-have and must-avoid notes,
- assumption note,
- approval state.

## 9. Required Scope-Lock Elements

Before a brief is considered lock-ready, the system must expose:

- which sections are complete,
- which sections are blocking,
- which sections are advisory only,
- what assumptions still exist,
- who confirmed the brief and when.

## 10. What Is Explicitly Out of Scope

Phase 4 does not include:

- automatic code-compliance sign-off,
- final permit documentation,
- automatic professional liability transfer to AI,
- replacing architect review,
- high-fidelity image-board generation from user uploads as a release blocker.

## 11. Acceptance Criteria

### Product

- user can complete the flow in Vietnamese,
- the system shows structured completeness instead of a vague “ready/not ready” state,
- design-direction summary is visible before generation.

### Engineering

- API returns clarification state consistently,
- chat path falls back safely under LLM latency,
- form path and chat path converge to the same brief structure,
- production build and tests pass.

### UX

- intake is no longer raw-JSON-first,
- missing information is visible and understandable,
- labels and helper text are Vietnamese with diacritics,
- brief confirmation feels intentional and trustworthy.

## 12. Implementation Notes for Product and Engineering

Recommended implementation split:

1. Brief model and clarification-state contract
2. Chat orchestration and fallback behavior
3. Vietnamese-first intake UI revamp
4. Design-direction board block
5. Confirmation and downstream handoff integration

Technical rule:

- Phase 4 must build on the shipped Phase 3 package/export baseline instead of replacing it.

## 13. Suggested Next-Phase Extensions

- attachment ingestion,
- reference image clustering,
- architect/client dual sign-off,
- contradiction timeline view,
- richer requirement matrix,
- reusable board templates by typology.
