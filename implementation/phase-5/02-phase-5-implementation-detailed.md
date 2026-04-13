# Phase 5 Implementation Detailed

## 1. Product Contract

Phase 5 introduces four implementation contracts:

1. chat-only clarification workspace,
2. explicit brief-lock contract,
3. corrected generation-to-review state sequence,
4. decision-grade designs workspace.

## 2. Intake Workspace Contract

### 2.1 Primary interaction model

The intake page must treat the AI conversation as the main workspace.

That means:

- no large suggestion rail competing with the chat,
- no repeated brief examples outside the chat body,
- no duplicate summary surfaces fighting for attention.

Allowed supporting UI outside the chat:

- a compact header,
- a compact brief status chip,
- a minimal drawer or collapsible panel for technical summary,
- and the final brief lock action.

### 2.2 Assistant response structure

The AI response must be structured around:

- what was understood,
- what was updated,
- what still needs confirmation,
- and suggested short replies.

The assistant payload should remain renderable as UI blocks, but the visible interaction should feel like a conversation rather than a dashboard.

## 3. Brief Lock Contract

### 3.1 Separate `readiness` from `brief state`

The current `clarification_state.readiness_label` is not enough.

Phase 5 must separate:

- `clarification readiness`
- from
- `brief contract state`

Required brief contract states:

- `draft`
- `ready_to_lock`
- `locked`
- `reopened`

### 3.2 Lock semantics

`brief locked` means:

- all required sections are complete,
- there are no active conflicts,
- and the user or architect has explicitly confirmed the brief.

This state must be visible in:

- project detail,
- brief get/update,
- chat response,
- intake header,
- dashboard badge,
- and downstream generation gating.

## 4. Sequence and State Machine Changes

### 4.1 Correct project sequence

The system must stop marking a project as effectively under review immediately after generation.

Required sequence:

1. `brief_locked`
2. `options_generating`
3. `options_generated`
4. `option_selected`
5. `under_review`
6. `approved` / `rejected` / `revise`

### 4.2 Version selection

Selecting a generated option should:

- mark the chosen version `under_review`,
- move sibling generated versions to `superseded`,
- and only then move project-level state into review.

### 4.3 Generation client behavior

The `Designs` page must not open an eager generation stream on page load unless generation is actively being started.

## 5. Designs Decision Workspace

### 5.1 Change the page role

The current page is a gallery.

Phase 5 must turn it into a decision workspace with:

- clearer stage framing,
- stronger option metadata,
- option comparison affordances,
- clearer primary CTA,
- and better Vietnamese copy.

### 5.2 Minimum option card content

Each option card should present:

- preview,
- option title in Vietnamese,
- one-line strategy summary,
- key metrics,
- strengths,
- caveats,
- compare action,
- and a primary select-for-review action.

### 5.3 Compare mode

At minimum, the page should support comparing two options side by side.

The comparison does not need to become a full review workspace, but it must help the user choose.

## 6. Option Generation Architecture

### 6.1 Current limitation

The current generation lane is operational, but it does not yet transform the full brief richness into differentiated architectural options.

Phase 5 must explicitly address the gap between:

- a clarified brief upstream,
- and a still-template-heavy option output downstream.

### 6.2 Required target

The generation lane must move toward a layered architecture:

1. brief gate,
2. program synthesis,
3. option strategy profiles,
4. geometry generation,
5. preview packaging,
6. quality scoring,
7. decision-ready metadata for the `Designs` page.

### 6.3 Minimum Phase 5 outcome

Phase 5 does not need to become a full generative planning engine, but it must materially improve:

- the semantic correctness of generation states,
- the quality and usefulness of option metadata,
- the explainability of why one option differs from another,
- and the presentation quality of option previews and copy.

### 6.4 Reference

All option-generation work in this phase must follow:

- `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`
- `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md`

## 7. Production Truth Validation

Phase 5 is not accepted based on local implementation alone.

The final gate must include:

- production deployment,
- at least one real intake audit after simplification,
- one real generated-options project checked against system sequence,
- and screenshot evidence for intake and designs states.

## 8. Quality Bar

Phase 5 is acceptable only if:

- backend tests for state and sequence pass,
- frontend build passes,
- intake no longer exposes the removed suggestion surfaces,
- `brief locked` is explicit and consistent,
- the designs page no longer reads as a technical gallery,
- option generation metadata and presentation are materially stronger than the current placeholder-style output,
- and production truth confirms the expected sequence and UX.
