# Phase 4 Analysis Brief

## Problem Statement

The current intake flow is still too close to an MVP:

- too little structure,
- weak requirement coverage,
- raw JSON is too prominent,
- design-direction locking is not credible enough,
- AI clarification quality is not strong enough for premium client-facing workflows.

## Decision

Phase 4 will solve this by building:

1. a richer clarification contract,
2. a Vietnamese-first guided intake experience,
3. a visible clarification board,
4. a design-direction board,
5. and a confirmation step that produces a stronger handoff into the existing Phase 3 pipeline.

## In Scope

- requirement categories and completeness model,
- AI clarification state,
- intake chat + structured form convergence,
- design-direction summary board,
- Vietnamese UX rewrite for the intake workspace,
- safer production fallback behavior for chat.

## Out of Scope

- full image-reference ingestion pipeline,
- permit/compliance automation,
- replacing architect approval,
- rebuilding the Phase 3 export workflow.

## Success Criteria

- user can understand what is still missing without reading JSON,
- AI asks sharper follow-up questions,
- brief quality is stronger before generation,
- design direction is visible and reviewable,
- the Phase 3 downstream flow still works unchanged.
