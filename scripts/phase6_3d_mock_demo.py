from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


ROOT = Path("/Users/nguyenquocthong/project/ai-architect-mvp")
MOCK_DIR = ROOT / "implementation" / "phase-6" / "mock-inputs"
ARTIFACT_DIR = ROOT / "artifacts" / "phase6-demo"
DEFAULT_BASE_URL = os.environ.get("PHASE6_DEMO_BASE_URL", "https://kts.blackbirdzzzz.art")
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0.0.0 Safari/537.36"
)

MOCK_REQUIREMENTS: dict[str, list[str]] = {
    "01-intake-clarification-input.json": ["project_context", "client_profile", "site_input", "space_program", "design_direction", "presentation_goal"],
    "02-brief-lock-input.json": ["project_type", "lot", "floors", "rooms", "style", "budget_vnd", "timeline_months"],
    "03-canonical-2d-design-input.json": ["project_id", "version_id", "status", "issued_package", "site", "levels", "rooms", "facade_logic"],
    "04-style-material-mapper-input.json": ["style_profile_id", "style_family", "material_palette", "lighting_direction", "room_scene_rules"],
    "05-presentation-scene-spec.json": ["scene_spec_version", "project_ref", "building_scene", "geometry_refs", "still_shots", "walkthrough_video"],
    "06-render-video-request.json": ["renderer", "scene_spec_ref", "model_output", "still_render_outputs", "video_output"],
    "07-qa-validator-input.json": ["source_refs", "mandatory_checks", "delivery_gate"],
    "08-client-delivery-package.json": ["package_type", "project_ref", "deliverables", "viewer", "approval"],
}


def curl_request(
    base_url: str,
    path: str,
    *,
    method: str,
    body: dict[str, Any] | None = None,
    token: str | None = None,
) -> bytes:
    command = [
        "curl",
        "-fsS",
        "--http1.1",
        "--connect-timeout",
        "10",
        "--max-time",
        "60",
        "-X",
        method,
        f"{base_url}{path}",
        "-H",
        f"User-Agent: {DEFAULT_USER_AGENT}",
        "-H",
        "Connection: close",
    ]
    if body is not None:
        command.extend(["-H", "Content-Type: application/json", "--data", json.dumps(body)])
    if token:
        command.extend(["-H", f"Authorization: Bearer {token}"])

    response = subprocess.run(command, capture_output=True, check=False)
    if response.returncode != 0:
        detail = response.stderr.decode("utf-8", errors="ignore").strip() or response.stdout.decode("utf-8", errors="ignore").strip()
        raise RuntimeError(f"{method} {path} failed: {detail}")
    return response.stdout


def json_request(
    base_url: str,
    path: str,
    *,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    token: str | None = None,
) -> Any:
    content = curl_request(base_url, path, method=method, body=body, token=token).decode("utf-8")
    return json.loads(content) if content else None


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_mock_inputs() -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for filename, required_keys in MOCK_REQUIREMENTS.items():
        path = MOCK_DIR / filename
        payload = load_json(path)
        missing = [key for key in required_keys if key not in payload]
        results.append(
            {
                "file": str(path),
                "present": path.exists(),
                "required_keys": required_keys,
                "missing_required_keys": missing,
                "valid": not missing,
            }
        )
    return results


def run_current_system_demo(base_url: str) -> dict[str, Any]:
    unique = uuid4().hex[:10]
    email = f"phase6-demo-{unique}@kts.blackbirdzzzz.art"
    password = f"Phase6-{unique}-Secure"
    locked_brief = load_json(MOCK_DIR / "02-brief-lock-input.json")

    register = json_request(
        base_url,
        "/api/v1/auth/register",
        method="POST",
        body={
            "email": email,
            "password": password,
            "full_name": "Phase 6 Demo User",
            "role": "architect",
            "organization_name": "KTC KTS Phase 6 Demo",
        },
    )
    token = register["access_token"]

    project = json_request(
        base_url,
        "/api/v1/projects",
        method="POST",
        token=token,
        body={
            "name": "Phase 6 3D Demo - Villa Vuon Thu Duc",
            "client_name": "Le Minh Anh",
            "client_phone": "0901234567",
        },
    )
    project_id = project["id"]

    brief_response = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/brief",
        method="PUT",
        token=token,
        body={"brief_json": locked_brief, "status": "confirmed"},
    )

    generation = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/generate",
        method="POST",
        token=token,
        body={"num_options": 3},
    )
    versions = generation["versions"]
    selected_version_id = versions[0]["id"]

    select = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/select",
        method="POST",
        token=token,
        body={"comment": "Select first option for 3D demo"},
    )

    approve = json_request(
        base_url,
        f"/api/v1/reviews/{selected_version_id}/approve",
        method="POST",
        token=token,
        body={"comment": "Approve for 3D derivation demo"},
    )

    derivation = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/derive-3d",
        method="POST",
        token=token,
    )

    project_after = json_request(
        base_url,
        f"/api/v1/projects/{project_id}",
        token=token,
    )

    model_payload = curl_request(base_url, derivation["model_url"], method="GET").decode("utf-8")
    render_payload_size = len(curl_request(base_url, derivation["render_urls"][0], method="GET"))

    active_version = next(item for item in project_after["versions"] if item["id"] == selected_version_id)
    return {
        "base_url": base_url,
        "project_id": project_id,
        "brief_contract_state": brief_response["brief_contract_state"],
        "generated_versions": len(versions),
        "selected_version_id": selected_version_id,
        "selection_status": select["status"],
        "approval_status": approve["status"],
        "project_status_after_approve": project_after["status"],
        "model_url": derivation["model_url"],
        "render_urls": derivation["render_urls"],
        "model_payload_prefix": model_payload[:240],
        "first_render_payload_size": render_payload_size,
        "current_viewer_supported": bool(active_version.get("model_url")),
        "video_available": False,
        "presentation_manifest_available": False,
        "notes": [
            "Current production can derive model_url + render_urls from a locked version.",
            "Current production does not yet produce walkthrough.mp4.",
            "Current production does not yet expose a client presentation manifest for 3D.",
        ],
    }


def build_summary(report: dict[str, Any]) -> str:
    validation = report["mock_validation"]
    demo = report["current_system_demo"]
    valid_count = sum(1 for item in validation if item["valid"])
    lines = [
        "# Phase 6 3D Mock Demo Summary",
        "",
        f"- Generated at: {report['generated_at']}",
        f"- Mock files valid: {valid_count}/{len(validation)}",
        f"- Demo base URL: {demo['base_url']}",
        f"- Demo project id: {demo['project_id']}",
        f"- Brief contract state after lock: {demo['brief_contract_state']}",
        f"- Generated versions: {demo['generated_versions']}",
        f"- Selected version id: {demo['selected_version_id']}",
        f"- Approval status: {demo['approval_status']}",
        f"- Current project status after approve: {demo['project_status_after_approve']}",
        f"- Current model URL exists: {demo['current_viewer_supported']}",
        f"- Current render count: {len(demo['render_urls'])}",
        f"- Current walkthrough video available: {demo['video_available']}",
        f"- Current 3D presentation manifest available: {demo['presentation_manifest_available']}",
        "",
        "## Current capability verdict",
        "",
        "- The mock input chain for the target architecture is structurally complete.",
        "- The current production system can lock a brief, generate options, approve a version, and derive 3D assets.",
        "- The current production system still stops at `model_url + render_urls` and does not yet output a walkthrough video or client-ready 3D presentation bundle.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mock_validation": validate_mock_inputs(),
        "current_system_demo": run_current_system_demo(DEFAULT_BASE_URL),
    }

    report_path = ARTIFACT_DIR / "phase6-3d-mock-demo-report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    summary_path = ARTIFACT_DIR / "phase6-3d-mock-demo-summary.md"
    summary_path.write_text(build_summary(report), encoding="utf-8")

    print(json.dumps(report, indent=2))
    print(f"\nSaved report to {report_path}")
    print(f"Saved summary to {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
