# Phase 5 Implementation Slice: Option Strategy Profiles and Decision Metadata

## 1. Purpose

This document defines the implementation slice for the most important quality gap in the Phase 5 generation lane:

- generated options are still too close to placeholder variants,
- the system does not clearly express the design strategy behind each option,
- and the `Designs` page does not yet receive enough metadata to help the user make a confident decision.

This slice is intentionally narrow.

It does not attempt to redesign the whole generation engine.

It defines the minimum contract needed so Phase 5 can turn:

- `3 generated options`

into:

- `3 intentionally differentiated options with professional decision support`.

## 2. Scope of This Slice

This slice covers only two layers from `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`:

1. `Option Strategy Profiles`
2. `Decision Metadata`

It explicitly excludes:

- full brief clarification logic,
- full program-synthesis implementation,
- full quality scoring engine,
- hero-render generation,
- and export/package logic from Phase 3.

## 3. Why This Slice Exists

The current architecture already has a reasonable baseline for:

- brief capture,
- generation orchestration,
- geometry fallback,
- and version persistence.

But the user still experiences the result as generic because the output lacks two things:

1. a clearly defined strategy identity per option,
2. and clear decision-ready explanation per option.

Without those two layers, the frontend can only display:

- image,
- label,
- and a weak description.

That is not enough for a premium architectural decision flow.

## 4. Safety Invariants

This slice must preserve the following invariants:

1. No option may be presented as strategically different unless the backend can explain the difference through explicit machine-readable fields.
2. `option_label` and `option_description` may remain for backward compatibility, but they must become derived presentation fields, not the primary truth.
3. Strategy metadata must be generated before the version is serialized to the `Designs` page.
4. Decision metadata must only summarize known signals from the brief, geometry, and rules; it must not invent confirmed facts.
5. If the brief is incomplete, the backend may degrade strategy richness, but it must expose the degraded state explicitly.
6. Phase 5 must stay rule-based. No hidden LLM-only reasoning may become the sole source of architectural claims.

## 5. As-Is

### 5.1 Current behavior

Current option generation is effectively:

1. brief enters generation,
2. generator produces option variants,
3. geometry is normalized,
4. versions are stored,
5. frontend renders labels and previews.

The current lane does not yet guarantee:

- a named strategy profile per option,
- a machine-readable explanation of why options differ,
- or decision-grade metadata that can survive API serialization.

### 5.2 Current product symptom

Because of that gap, the user sees:

- generic option naming,
- weak explanation,
- and cards that feel like a gallery rather than a professional decision pack.

### 5.3 Current likely truth sources

This slice assumes current runtime ownership remains roughly as already documented:

- orchestration: `../ai-architect-api/app/api/v1/generation.py`
- serialization: `../ai-architect-api/app/api/v1/projects.py`
- geometry rules: `../ai-architect-api/app/services/geometry.py`
- state transitions: `../ai-architect-api/app/services/state_machine.py`
- persistence: `../ai-architect-api/app/models.py`
- frontend rendering: `../ai-architect-web/src/components/designs-client.tsx`

## 6. Target Execution Model

Phase 5 should implement the following minimal order of operations:

1. validate that the brief is allowed to generate,
2. derive a reduced `program_synthesis` object from the brief,
3. resolve a distinct `option_strategy_profile` for each option,
4. generate geometry with that strategy profile as an explicit input,
5. compute `decision_metadata` from brief + geometry + strategy profile,
6. persist both strategy and decision metadata on the version,
7. serialize decision-ready fields to the frontend.

The key change is this:

- strategy and decision explanation become explicit intermediate artifacts,
- not UI-only copy written after the fact.

## 7. Core Domain Contracts

### 7.1 `program_synthesis` minimal contract

This slice depends on a lightweight synthesis object.

Phase 5 does not need a complete programming engine, but it does need a stable intermediate contract:

```json
{
  "typology": "townhouse",
  "project_mode": "new_build",
  "household_profile": "family_3_generations",
  "priority_tags": ["daylight", "garage", "elder_room"],
  "required_spaces": ["garage", "living_room", "kitchen", "ancestor_room"],
  "special_constraints": ["ground_floor_elder_room"],
  "lot_snapshot": {
    "width_m": 5,
    "depth_m": 20,
    "orientation": "south"
  }
}
```

This object may remain transient in Phase 5, but it must exist in code as a named contract.

### 7.2 `option_strategy_profile` contract

Each generated option must receive one explicit strategy profile.

Suggested contract:

```json
{
  "strategy_key": "daylight_first",
  "strategy_family": "layout_priority",
  "title_vi": "Ưu tiên lấy sáng",
  "summary_vi": "Tập trung mở mặt thoáng, tăng thông gió và ưu tiên các không gian sinh hoạt gần nguồn sáng.",
  "differentiators": [
    "front_and_rear_openings",
    "void_or_lightwell_priority",
    "public_space_near_daylight"
  ],
  "rule_overrides": {
    "stair_position": "side_or_center_whichever_preserves_void",
    "service_core": "compact",
    "facade_openness": "high"
  },
  "fit_conditions": [
    "lot_depth_gte_16m",
    "daylight_priority_present"
  ],
  "confidence": "high",
  "generation_source": "rule_based_phase5"
}
```

Required fields:

- `strategy_key`
- `title_vi`
- `summary_vi`
- `differentiators`
- `rule_overrides`
- `confidence`
- `generation_source`

Optional fields:

- `fit_conditions`
- `strategy_family`
- `fallback_reason`

### 7.3 `decision_metadata` contract

Each persisted option must also expose a decision-oriented metadata object.

Suggested contract:

```json
{
  "option_title_vi": "Phương án ưu tiên lấy sáng",
  "option_summary_vi": "Phù hợp khi gia chủ ưu tiên nhà sáng, thoáng và muốn khu sinh hoạt chung có cảm giác rộng hơn.",
  "fit_reasons": [
    "Phù hợp lô đất hướng Nam và chiều sâu đủ để mở trước sau.",
    "Ưu tiên ánh sáng tự nhiên đúng với brief đã chốt.",
    "Giảm cảm giác tối ở khu giữa nhà so với phương án còn lại."
  ],
  "strengths": [
    "Không gian sinh hoạt chung sáng và thông thoáng hơn.",
    "Luồng giao thông chính rõ ràng.",
    "Mặt bằng phù hợp cho nhà phố nhiều tầng."
  ],
  "caveats": [
    "Diện tích kín cho kho hoặc phòng phụ có thể giảm.",
    "Cần kiểm soát nắng mặt đứng nếu mặt tiền quá mở."
  ],
  "metrics": {
    "floor_count": 4,
    "bedroom_count": 4,
    "wc_count": 3,
    "parking_count": 1,
    "estimated_gfa_m2": 280
  },
  "quality_flags": {
    "brief_fit": "good",
    "assumption_risk": "medium",
    "presentation_confidence": "high"
  },
  "compare_axes": [
    "daylight",
    "privacy",
    "circulation",
    "garage_layout"
  ]
}
```

Required fields:

- `option_title_vi`
- `option_summary_vi`
- `fit_reasons`
- `strengths`
- `caveats`
- `metrics`

Optional Phase 5 fields:

- `quality_flags`
- `compare_axes`
- `degraded`
- `degraded_reasons`

### 7.4 Compatibility fields

For Phase 5, the existing fields may stay in place:

- `design_versions.option_label`
- `design_versions.option_description`
- `design_versions.generation_metadata`

But the source of truth must shift to:

- `generation_metadata.option_strategy_profile`
- `generation_metadata.decision_metadata`

Compatibility rule:

- `option_label = decision_metadata.option_title_vi`
- `option_description = decision_metadata.option_summary_vi`

That preserves older consumers while moving the real contract into structured metadata.

## 8. Persistence Strategy

### 8.1 Phase 5 persistence decision

Do not introduce a new top-level database table for strategy profiles in Phase 5.

Use `design_versions.generation_metadata` as the durable container.

Recommended shape:

```json
{
  "model_id": "rule-based-v2",
  "workflow_version": "phase5-option-strategy-v1",
  "seed": 42,
  "generation_source": "rule_based_phase5",
  "program_synthesis": { "...": "..." },
  "option_strategy_profile": { "...": "..." },
  "decision_metadata": { "...": "..." },
  "quality_scores": {
    "brief_fit_score": 0.82,
    "daylight_score": 0.78,
    "privacy_score": 0.64
  }
}
```

This is the right Phase 5 tradeoff because:

- it avoids a migration-heavy change,
- it stays compatible with current JSONB design,
- and it gives CP4 and CP5 enough structured data to work with.

### 8.2 When a migration is justified later

Move strategy or decision metadata into normalized tables only when at least one of these becomes necessary:

- cross-project analytics on strategy usage,
- version-to-version comparison queries directly in SQL,
- filtering projects by strategy family,
- or formal review/reporting over option rationale.

That is not required for Phase 5 acceptance.

## 9. Service Boundaries

### 9.1 New backend services

Phase 5 should add two explicit services:

#### A. `option_strategy_profiles.py`

Responsibility:

- map brief + synthesis + option index into a deliberate strategy profile,
- ensure sibling options are meaningfully different,
- apply typology-aware fallback rules,
- expose `strategy_key`, `title_vi`, and `rule_overrides`.

Suggested function:

```python
def resolve_option_strategy_profiles(
    brief: dict,
    program_synthesis: dict,
    num_options: int = 3,
) -> list[dict]:
    ...
```

#### B. `decision_metadata.py`

Responsibility:

- transform brief + geometry + strategy into decision-grade output,
- compute human-readable strengths and caveats,
- derive compare axes and metrics,
- and produce frontend-safe Vietnamese copy.

Suggested function:

```python
def build_decision_metadata(
    brief: dict,
    geometry: dict,
    strategy_profile: dict,
) -> dict:
    ...
```

### 9.2 Existing files to update

Primary runtime files:

- `../ai-architect-api/app/api/v1/generation.py`
- `../ai-architect-api/app/api/v1/projects.py`
- `../ai-architect-api/app/services/geometry.py`
- `../ai-architect-api/app/models.py`
- `../ai-architect-web/src/components/designs-client.tsx`

Likely new files:

- `../ai-architect-api/app/services/option_strategy_profiles.py`
- `../ai-architect-api/app/services/decision_metadata.py`
- `../ai-architect-api/tests/test_option_strategy_profiles.py`
- `../ai-architect-api/tests/test_decision_metadata.py`

### 9.3 Ownership split

`generation.py` should remain the orchestration boundary.

It should not directly own strategy-selection logic or UI copy composition.

Required split:

- `generation.py`: orchestration and persistence
- `option_strategy_profiles.py`: option differentiation logic
- `geometry.py`: geometry generation from rules + strategy input
- `decision_metadata.py`: explanation and metrics synthesis
- `projects.py`: serialization contract to frontend
- `designs-client.tsx`: display only, not content invention

## 10. API and Serialization Contract

### 10.1 Internal generation result contract

Before persistence, each generated option should expose:

```json
{
  "option_key": "opt_daylight_first",
  "strategy_profile": { "...": "..." },
  "geometry": { "...": "..." },
  "decision_metadata": { "...": "..." },
  "preview": {
    "technical_preview_url": "https://...",
    "hero_preview_url": null
  }
}
```

### 10.2 External project/version payload contract

`GET /projects/{project_id}` and any `Designs` page source endpoint should serialize at minimum:

```json
{
  "id": "uuid",
  "status": "generated",
  "option_title_vi": "Phương án ưu tiên lấy sáng",
  "option_summary_vi": "Tập trung lấy sáng và thông gió cho khu sinh hoạt chung.",
  "option_strategy_key": "daylight_first",
  "option_strategy_label_vi": "Ưu tiên lấy sáng",
  "fit_reasons": ["...", "..."],
  "strengths": ["...", "..."],
  "caveats": ["...", "..."],
  "metrics": {
    "bedroom_count": 4,
    "wc_count": 3,
    "estimated_gfa_m2": 280
  },
  "compare_axes": ["daylight", "privacy", "circulation"],
  "generation_source": "rule_based_phase5",
  "thumbnail_url": "https://..."
}
```

These fields should be top-level serialized fields for frontend convenience.

Do not force the frontend to unpack nested JSON blobs just to render the main decision card.

### 10.3 Degraded-mode contract

If the strategy or explanation is incomplete, the API must expose that explicitly:

```json
{
  "decision_metadata_degraded": true,
  "decision_metadata_degraded_reasons": [
    "missing_household_profile",
    "missing_site_orientation"
  ]
}
```

This avoids fake confidence in the decision workspace.

## 11. Frontend Contract for the Designs Page

The `Designs` page must consume this slice in a read-only way.

Frontend must not:

- invent option strategies,
- infer strengths or caveats from raw labels,
- or silently collapse missing metadata into placeholder copy.

Required rendering contract:

1. card heading uses `option_title_vi`,
2. strategy pill uses `option_strategy_label_vi`,
3. summary block uses `option_summary_vi`,
4. compare area uses `fit_reasons`, `strengths`, `caveats`, and `metrics`,
5. degraded metadata shows a compact warning instead of fake polish.

## 12. Detailed Implementation Order

### 12.1 Slice A: backend contract introduction

Goal:

- create strategy and decision services,
- wire them into generation flow,
- and persist structured metadata.

Files:

- `../ai-architect-api/app/services/option_strategy_profiles.py`
- `../ai-architect-api/app/services/decision_metadata.py`
- `../ai-architect-api/app/api/v1/generation.py`
- `../ai-architect-api/app/models.py`

Acceptance:

- newly generated versions persist structured `generation_metadata.option_strategy_profile`,
- newly generated versions persist structured `generation_metadata.decision_metadata`,
- compatibility fields are still populated.

### 12.2 Slice B: serialization and page consumption

Goal:

- expose the new contract cleanly to the frontend,
- remove placeholder-only assumptions from the page.

Files:

- `../ai-architect-api/app/api/v1/projects.py`
- `../ai-architect-web/src/components/designs-client.tsx`

Acceptance:

- top-level response fields exist,
- option card copy is strategy-aware,
- compare mode uses real metadata differences.

### 12.3 Slice C: degraded and fallback handling

Goal:

- make partial-metadata behavior explicit instead of silently low-quality.

Files:

- `../ai-architect-api/app/services/decision_metadata.py`
- `../ai-architect-api/app/api/v1/projects.py`
- `../ai-architect-web/src/components/designs-client.tsx`

Acceptance:

- missing brief inputs create degraded metadata flags,
- UI reflects degraded state compactly,
- issue flow remains blocked if deeper phase rules require full quality.

## 13. Checkpoint Mapping

### 13.1 CP4

CP4 must deliver the backend readiness for this slice:

- project/version sequence remains correct,
- generation payload can carry structured strategy and decision metadata,
- no eager frontend assumptions lock the system into `Option A/B/C`.

### 13.2 CP5

CP5 must consume this slice visibly:

- option cards show strategy-aware naming,
- compare mode uses meaningful differences,
- and the page reads like a decision workspace instead of a raw gallery.

### 13.3 CP6

CP6 must validate this slice against production truth:

- do real options feel intentionally different,
- do rationale and caveats feel credible,
- do any cards still look placeholder-like,
- and does degraded behavior stay honest.

## 14. Test Plan

### 14.1 Backend unit tests

- strategy resolver returns three distinct strategies when the brief allows it
- strategy resolver falls back deterministically when the brief is sparse
- decision metadata builder never returns empty `fit_reasons` for a non-degraded option
- decision metadata builder marks degraded state when required inputs are missing
- compatibility fields mirror structured metadata correctly

### 14.2 Backend flow tests

- generation creates versions with structured metadata populated
- selected option moves to review without losing strategy metadata
- serialized project payload exposes flattened decision fields

### 14.3 Frontend tests

- option card renders structured metadata
- compare mode shows differences in strengths/caveats/metrics
- degraded option state renders warning treatment instead of placeholder prose

### 14.4 Production validation

At least one real project must be checked for:

- meaningful option differentiation,
- clean Vietnamese copy,
- credible fit reasons,
- non-generic card presentation,
- and absence of raw placeholder titles.

## 15. Non-Goals for Phase 5

Do not expand this slice into:

- full ML ranking,
- architect-grade compliance checking,
- automatic cost estimation,
- automatic detail-sheet generation,
- or architectural sign-off automation.

This slice is about making options explainable and decision-ready, not pretending the system is already a full design reviewer.

## 16. Open Questions

1. Should `program_synthesis` remain transient in Phase 5 or be persisted inside `generation_metadata` for debugging and audits
2. Should strategy titles be fully curated per typology or assembled from reusable rule fragments
3. Should `compare_axes` be backend-authored only, or may the frontend reorder them for presentation
4. Should degraded strategy metadata block only presentation polish, or also block selection for review in some edge cases

## 17. Immediate Decision

Phase 5 should implement this slice using:

- rule-based strategy resolution,
- JSONB persistence inside `generation_metadata`,
- flattened decision-ready API fields,
- and frontend rendering that treats metadata as first-class product content.

That is the smallest implementation slice that can materially improve perceived option quality without destabilizing the rest of the generation pipeline.

## 18. Execution Reference

For assignable engineering work across backend, frontend, and validation lanes, use:

- `implementation/phase-5/06-phase-5-option-strategy-technical-task-breakdown.md`
