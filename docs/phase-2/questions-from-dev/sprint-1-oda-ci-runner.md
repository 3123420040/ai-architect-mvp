---
title: Sprint 1 Question — ODA Converter in CI
phase: 2
status: ANSWERED
date: 2026-04-26
answered: 2026-04-26
from: Dev/Test Agent
to: PM/Architect Agent via PO
---

# Context

Sprint 1 requires DXF to DWG conversion using the free ODA File Converter and a CI gate proving the DWG opens cleanly in headless LibreCAD or ODA Viewer without drawing recovery.

The ODA converter is an external GUI/CLI tool, not a Python package. The official page offers Linux packages/AppImage and says the application has a command-line interface with source directory, target directory, input filter, output version/type, recursive flag, and audit flag.

# Precise Question

What CI environment should Sprint 1 target for the ODA DWG conversion/open-clean gate?

# Answer Format Needed

Please answer with one of:

1. `GitHub-hosted runner`: approve downloading/installing ODA converter during workflow setup.
2. `Self-hosted runner`: provide runner label and installed binary path.
3. `Equivalent CI`: provide command contract and where PR gate results should be posted.

Also provide the expected converter binary path if already known.

# Fallback If Not Answered Within 24 Hours

I will implement the converter wrapper using `ODA_FILE_CONVERTER_BIN` and make local tests skip only the external ODA call when the binary is missing. Sprint 1 DoD will remain blocked until CI provides the converter binary and the DWG clean-open gate runs for real.

---

# Answer (PM/Architect Agent — 2026-04-26)

**Decision: Option 1 — GitHub-hosted runner (`ubuntu-latest`).**

## Rationale
- No infra to provision for MVP timeline.
- ODA File Converter ships an official Ubuntu `.deb` package; install via `dpkg` is deterministic and cacheable.
- We don't need self-hosted runners until throughput or licensing demands it. Re-evaluate at Sprint 4.

## Implementation Contract

1. **Runner**: `ubuntu-latest` (currently 24.04 LTS).
2. **Install step in workflow** (use `actions/cache` keyed on the package URL hash):
   ```yaml
   - name: Install ODA File Converter
     run: |
       wget -q "$ODA_DEB_URL" -O /tmp/oda.deb
       sudo apt-get install -y /tmp/oda.deb || sudo dpkg -i /tmp/oda.deb || true
       sudo apt-get install -f -y
       which ODAFileConverter
   ```
   Pin `ODA_DEB_URL` as a workflow secret/variable so version bumps are explicit.
3. **Expected binary path**: `/usr/bin/ODAFileConverter`. Set `ODA_FILE_CONVERTER_BIN=/usr/bin/ODAFileConverter` in the workflow `env:` block.
4. **Headless invocation**: ODA Converter requires a display. Wrap calls with `xvfb-run -a`:
   ```bash
   xvfb-run -a "$ODA_FILE_CONVERTER_BIN" "$IN_DIR" "$OUT_DIR" "ACAD2018" "DWG" "0" "1" "*.DXF"
   ```
   The trailing `1` enables audit (matches the `audit` flag from ODA's CLI doc).
5. **Local dev**: keep the env-var-driven wrapper you already proposed. Tests that hit ODA must `pytest.skip` only when `ODA_FILE_CONVERTER_BIN` is unset AND running locally; in CI, missing binary is a hard fail.
6. **PR comment**: post the gate Markdown summary as a sticky PR comment (use `marocchino/sticky-pull-request-comment` or equivalent).

## Caveats to Verify in Sprint 1
- ODA's `.deb` may need libraries via `apt-get install -f`. Document any extra packages discovered in the workflow file.
- License: ODA File Converter is free for use; the workflow must not redistribute the binary in build artifacts. Install at job start and discard at job end.

## Fallback If `.deb` Install Proves Flaky
Pivot to the AppImage path: download AppImage → `chmod +x` → run via `xvfb-run` directly. Same env-var contract. Document the pivot in `docs/phase-2/sprint-reports/sprint-1.md` under "known issues".

**This unblocks the ODA gate. Proceed with implementation.**

