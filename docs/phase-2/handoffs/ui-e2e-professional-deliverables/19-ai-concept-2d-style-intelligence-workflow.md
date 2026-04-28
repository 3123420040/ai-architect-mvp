---
title: AI Concept 2D Style Intelligence Workflow
phase: phase-2
status: draft-for-implementation
related_files:
  - 13-output-quality-remediation-plan.md
  - 14-artifact-input-process-quality-contract.md
  - 18-output-quality-uplift-implementation-guide-and-agent-prompt.md
---

# AI Concept 2D Style Intelligence Workflow

This document defines the next improvement workflow for producing market-readable 2D concept drawing packages from natural customer conversation, reference images, style knowledge, and deterministic drawing rules.

The goal is not construction documentation. The goal is a professional concept/schematic 2D package that lets a non-technical homeowner understand the site, room layout, spatial intent, and architectural style well enough to review and request revisions.

## 1. Product Principle

The homeowner should not be forced to answer technical architectural questions.

The AI must:

- talk naturally and efficiently;
- infer lifestyle, constraints, and style intent from sparse conversation;
- analyze reference images when provided;
- propose design direction proactively;
- fill technical concept parameters from approved style knowledge and project patterns;
- ask for confirmation only when a decision is materially important or blocking;
- render a structured 2D package from a normalized concept model;
- support review and revision through chat and annotations.

The core product behavior is:

```text
customer chat + optional reference images
  -> customer understanding
  -> style inference
  -> style/profile retrieval
  -> concept program and layout strategy
  -> architectural concept model
  -> drawing package model
  -> PDF/DXF render
  -> semantic + visual QA
  -> customer review loop
```

## 2. Target Output

The target 2D package is `Professional Concept 2D Package, not for construction`.

Minimum sheets:

- cover/index and assumptions;
- site plan with true or explicitly assumed lot geometry;
- floor plan per floor with rooms, walls, doors, windows, stairs, fixtures, furniture, room areas, and dimensions;
- roof/terrace plan when relevant;
- front elevation and at least one concept side/rear elevation when relevant;
- one section through stair/lightwell or major spatial idea;
- room/area schedule;
- door/window schedule at concept level;
- style/material concept notes;
- revision notes.

Every sheet must be customer-readable and architecturally coherent. It does not need structural, MEP, geotechnical, legal compliance, or construction-grade details unless verified by a later professional workflow.

## 3. Required System Layers

### 3.1 CustomerUnderstanding

Captured from conversation and optional image uploads:

- site facts: width/depth, front edge, orientation, access, existing context if known;
- family/lifestyle: people, ages, elders, children, work-from-home, pets;
- program: floors, bedrooms, toilets, garage, prayer, garden, laundry, storage;
- priorities: light, ventilation, privacy, budget, low maintenance, premium feel;
- likes/dislikes;
- reference images and extracted style tokens;
- blocking unknowns.

### 3.2 StyleKnowledgeBase

Versioned structured data, not free-form prompts:

- style aliases and natural language signals;
- visual signals from reference images;
- spatial rules;
- typology rules;
- layout tendencies;
- room size ranges;
- opening rules;
- facade rules;
- material palettes;
- drawing rules;
- avoid rules;
- validation rules;
- explanation templates.

Initial styles:

- `modern_tropical`;
- `minimal_warm`;
- `indochine_soft`.

### 3.3 PatternMemory

Reusable project patterns:

- site range;
- typology;
- style fit;
- family/program fit;
- stair/lightwell position;
- room sequence;
- facade strategy;
- known tradeoffs;
- previous customer feedback tags.

Patterns seed generation. They must not blindly copy old projects.

### 3.4 ArchitecturalConceptModel

The normalized model used by all renderers:

- site polygon and assumptions;
- buildable area;
- levels;
- rooms with polygons, areas, labels, priorities, adjacency;
- walls with thickness/type/height;
- doors/windows with wall references and dimensions;
- stairs and circulation;
- fixtures/furniture;
- lightwell/courtyard/green zones;
- facade concept;
- section lines;
- material/style concept;
- decisions with source, confidence, and assumptions.

### 3.5 DrawingPackageModel

Renderer-ready data:

- sheet list;
- sheet size, scale, and title block;
- viewports;
- line weights/layers;
- labels;
- dimensions derived from geometry;
- schedules;
- annotations;
- assumption notes;
- QA bounds.

Exporters must consume this model and must not invent technical content independently.

## 4. Decision Model

Every meaningful AI-filled value must record provenance:

```json
{
  "value": 4.0,
  "source": "derived_from_parking_requirement",
  "confidence": 0.8,
  "assumption": true,
  "customer_visible_explanation": "Chừa sân trước 4m để có chỗ đậu xe concept.",
  "needs_confirmation": true
}
```

Allowed sources:

- `user_fact`;
- `reference_image`;
- `style_profile`;
- `pattern_memory`;
- `rule_default`;
- `ai_proposal`;
- `reviewer_override`.

## 5. Conversation Strategy

The AI should use assumption-first design.

Ask directly only for:

- lot size or known site shape;
- floor count;
- bedroom/WC count;
- garage/parking;
- family/lifestyle constraints;
- preferred feel/style or reference images;
- major dislikes or must-haves.

The AI should not ask the homeowner for wall thickness, sill height, door width, CAD layers, text height, sheet scale, or dimension style. These are resolved by style/rule defaults and exposed only as assumptions when useful.

## 6. Style Inference

The style classifier receives text, images, and project facts. It returns ranked candidates:

```json
{
  "style_candidates": [
    {
      "style_id": "modern_tropical",
      "confidence": 0.84,
      "evidence": ["thoang", "nhieu cay", "hien dai", "wood louvers"]
    }
  ],
  "selected_style_id": "modern_tropical",
  "needs_confirmation": false
}
```

If confidence is low, ask one friendly contrast question:

```text
Em đang thấy hai hướng hợp: hiện đại xanh mát hoặc tối giản ấm. Anh/chị thích hướng nào hơn?
```

## 7. Revision Loop

After rendering, customer feedback becomes structured operations:

```json
{
  "change_request": "Phong khach rong hon",
  "operations": [
    {"type": "resize_room", "room_id": "living", "intent": "increase_area"},
    {"type": "rebalance_adjacent_rooms", "affected_rooms": ["kitchen_dining", "garage"]}
  ]
}
```

Each new render creates a new design version with:

- parent version;
- changed decisions;
- changed geometry;
- QA results;
- customer-facing changelog.

## 8. Checkpoint Workflow

This improvement is split into implementation checkpoints:

| Order | Code | Goal |
|---|---|---|
| 8 | `cp8-style-knowledge-base` | Structured style KB and pattern memory seed |
| 9 | `cp9-conversation-style-inference` | Natural conversation/image signals to style and brief facts |
| 10 | `cp10-concept-model-contract` | ArchitecturalConceptModel and provenance contract |
| 11 | `cp11-layout-technical-defaults` | Program/layout/default resolver and validation |
| 12 | `cp12-concept-2d-render-qa` | DrawingPackageModel, PDF/DXF renderer, QA gates |
| 13 | `cp13-client-review-revision-loop` | Chat/annotation revision operations and versioning |
| 14 | `cp14-integrated-concept-package` | End-to-end acceptance on realistic homeowner scenarios |

## 9. Acceptance Bar

The workflow is successful when a sparse homeowner brief plus optional reference images can produce a customer-readable 2D concept package where:

- site geometry is true or explicitly assumed;
- style intent is visible in plan/elevation/material notes;
- room program matches customer intent;
- rooms, walls, doors, windows, stairs, fixtures, and furniture are coherent;
- dimensions are derived from geometry;
- labels do not overlap;
- sheets are legible;
- assumptions are visible;
- customer revisions update the model and regenerate a new package.
