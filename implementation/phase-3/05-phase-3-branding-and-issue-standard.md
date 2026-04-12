# Phase 3 Branding and Issue Standard

*Status: Locked for Phase 3*
*Studio identity: KTC KTS*
*Related scope authority: `04-phase-3-scope-lock.md`*

---

## 1. Purpose

This document defines the mandatory branding, title block, disclaimer, and issue-state presentation rules for Phase 3 packages.

The goal is not decorative branding. The goal is to make every issued package feel:

- credible,
- premium,
- internally consistent,
- architect-owned,
- and clearly differentiated from permit or construction documentation.

---

## 2. Studio Identity

### 2.1 Official studio name

`KTC KTS`

### 2.2 Wordmark usage

- Primary wordmark: `KTC KTS`
- Use uppercase only on cover and title blocks.
- Do not add extra slogans or alternate company names in Phase 3.
- Use the supplied wordmark asset: `assets/ktc-kts-wordmark.svg`

### 2.3 Brand tone

The visual tone should feel architectural, restrained, and premium:

- not playful,
- not startup-generic,
- not luxury-overstyled,
- not engineering-cold.

The visual system should communicate precision first and personality second.

---

## 3. Color System

These color tokens apply to package rendering, title blocks, and UI surfaces for Phase 3.

| Token | Hex | Use |
|------|-----|-----|
| `ink_charcoal` | `#1F1E1A` | Primary text, drawing linework, key dividers |
| `warm_stone` | `#DCCFBE` | Secondary lines, sheet framing, subtle separators |
| `bone` | `#F7F3EC` | Sheet background, presentation cards |
| `terracotta_accent` | `#A65A3A` | Approved accent for `client_presentation` preset |
| `sage_grey` | `#6A6F63` | Secondary metadata, quiet labels, legends |
| `degraded_red` | `#B4412F` | DEGRADED label, blocked issue state |

### 3.1 Preset application

- `technical_neutral`
  - primary palette: `ink_charcoal`, `warm_stone`, `bone`
  - no prominent accent blocks
  - highest legibility and lowest visual noise

- `client_presentation`
  - same base palette
  - may use `terracotta_accent` for cover highlights, key dividers, and selected emphasis
  - must not reduce technical readability

---

## 4. Typography Direction

Phase 3 package typography should follow a restrained editorial hierarchy:

- Serif or serif-like wordmark treatment for the KTC KTS header
- Clean sans-serif for metadata, sheet labels, notes, and schedules

Minimum hierarchy:

- package title
- sheet title
- room tags
- dimensions
- notes / secondary metadata

Typography must never feel like a marketing brochure. It is still a working design package.

---

## 5. Title Block Standard

### 5.1 Mandatory fields

Every issued sheet must include:

- KTC KTS wordmark
- project name
- package label: `DESIGN DEVELOPMENT PACKAGE`
- sheet title
- sheet number
- scale
- preset
- issue date
- revision
- status

### 5.2 Standard wording

Use the following wording exactly:

```text
KTC KTS
DESIGN DEVELOPMENT PACKAGE
SHEET: {sheet_title}
NO: {sheet_number}
SCALE: {scale}
PRESET: {deliverable_preset}
DATE: {issue_date}
REV: {revision_label}
STATUS: {package_status}
```

### 5.3 Allowed status labels

- `DRAFT`
- `REVIEW`
- `ISSUED`
- `DEGRADED PREVIEW`

No other status copy should appear on title blocks in Phase 3.

---

## 6. Disclaimer Standard

### 6.1 Cover-sheet disclaimer

Use this full disclaimer on the cover sheet:

```text
DESIGN DEVELOPMENT PACKAGE FOR CLIENT ALIGNMENT, DESIGN COORDINATION, AND CAD/BIM HANDOFF.
NOT FOR PERMIT SUBMISSION, CONSTRUCTION, FABRICATION, OR SITE EXECUTION WITHOUT PROFESSIONAL VERIFICATION.
```

### 6.2 Per-sheet short disclaimer

Use this short disclaimer on non-cover sheets where needed:

```text
NOT FOR PERMIT, CONSTRUCTION, OR SITE EXECUTION.
```

### 6.3 Forbidden wording

Phase 3 packages must not use any wording that implies:

- permit readiness,
- construction readiness,
- code approval,
- site-issued execution,
- or sealed professional sign-off.

---

## 7. DEGRADED Preview Treatment

### 7.1 Mandatory DEGRADED wording

Use this exact message wherever a degraded preview is shown:

```text
DEGRADED PREVIEW. QUALITY GATES NOT PASSED. PREVIEW ONLY. ISSUE BLOCKED.
```

### 7.2 Visual treatment

- background/label color: `degraded_red`
- text: white or `bone`
- must be visible on:
  - preview banner
  - package metadata panel
  - exported preview cover

### 7.3 Rules

- DEGRADED may appear on previews and internal review exports
- DEGRADED must never appear on an `ISSUED` package
- DEGRADED must disable issue actions in the product

---

## 8. Sheet Visual Direction

### 8.1 What makes it feel premium

- consistent framing and margins
- restrained but deliberate spacing
- clear lineweight hierarchy
- no cluttered badge soup
- no default UI-style chips pasted onto sheets
- room labels and schedule tags that feel coordinated, not ad hoc

### 8.2 What to avoid

- random accent use
- oversized logos
- multiple font families without purpose
- decorative gradients or marketing layout tropes
- title block language that changes by sheet

---

## 9. File Naming and Package Naming

### 9.1 Package naming

Use:

```text
{project_slug}_dd_package_rev_{revision_label}
```

Example:

```text
tran_residence_dd_package_rev_A
```

### 9.2 Sheet naming

Use:

```text
{sheet_number}_{sheet_slug}.{ext}
```

Example:

```text
A6_south_elevation.svg
```

### 9.3 Preset labeling in UI

Use the following user-facing labels:

- `Technical Neutral`
- `Client Presentation`

Do not expose `branded_studio` as a selectable Phase 3 release preset.

---

## 10. Asset Reference

Primary wordmark asset:

- `assets/ktc-kts-wordmark.svg`

This asset is the visual reference for package and title block implementation. Engineering may adapt it into SVG/component form, but the wording and palette must remain consistent with this document.
