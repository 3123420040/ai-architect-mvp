from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0.0.0 Safari/537.36"
)
VERBOSE = os.environ.get("PRODUCTION_LOOP_VERBOSE") == "1"
TRANSIENT_CURL_ERRORS = (
    "ssl connection timeout",
    "connection timed out",
    "operation timed out",
    "failed to connect",
    "connection reset",
    "empty reply from server",
    "recv failure",
    "http/2 stream",
)


def trace(label: str) -> None:
    if VERBOSE:
        print(f"[trace] {label}", flush=True)


def is_transient_curl_failure(detail: str) -> bool:
    normalized = detail.lower()
    return any(marker in normalized for marker in TRANSIENT_CURL_ERRORS)


def curl_request(
    base_url: str,
    path: str,
    *,
    method: str,
    body: dict[str, Any] | None = None,
    token: str | None = None,
    host_header: str | None = None,
) -> bytes:
    max_attempts = 3
    last_detail = ""

    for attempt in range(1, max_attempts + 1):
        command = [
            "curl",
            "-fsS",
            "--http1.1",
            "--connect-timeout",
            "10",
            "--max-time",
            "45",
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
        if host_header:
            command.extend(["-H", f"Host: {host_header}"])

        response = subprocess.run(command, capture_output=True, check=False)
        if response.returncode == 0:
            return response.stdout

        last_detail = response.stderr.decode("utf-8", errors="ignore").strip() or response.stdout.decode("utf-8", errors="ignore").strip()
        if attempt < max_attempts and is_transient_curl_failure(last_detail):
            trace(f"retry {method} {path} after transient curl failure: {last_detail}")
            time.sleep(attempt)
            continue
        break

    raise RuntimeError(f"{method} {path} failed: {last_detail}")


@dataclass
class LoopResult:
    loop_number: int
    passed: bool
    duration_seconds: float
    project_id: str
    selected_version_id: str
    package_id: str
    package_status: str
    package_issue_date: str
    share_token: str
    exported_pdf_url: str
    exported_svg_url: str
    exported_dxf_url: str
    exported_ifc_url: str
    exported_manifest_url: str
    schedule_csv_urls: dict[str, str]
    model_url: str
    render_count: int
    notifications: int
    checked_at: str


def json_request(
    base_url: str,
    path: str,
    *,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    token: str | None = None,
    host_header: str | None = None,
) -> Any:
    content = curl_request(
        base_url,
        path,
        method=method,
        body=body,
        token=token,
        host_header=host_header,
    ).decode("utf-8")
    return json.loads(content) if content else None


def raw_request(
    base_url: str,
    path: str,
    *,
    method: str = "GET",
    host_header: str | None = None,
) -> bytes:
    return curl_request(
        base_url,
        path,
        method=method,
        host_header=host_header,
    )


def run_single_loop(loop_number: int, base_url: str, host_header: str | None) -> LoopResult:
    started_at = time.perf_counter()
    unique = uuid4().hex[:10]
    email = f"prod-loop-{loop_number}-{unique}@kts.blackbirdzzzz.art"
    password = f"ProdLoop-{unique}-Secure"

    trace("homepage")
    homepage = raw_request(base_url, "/", host_header=host_header).decode("utf-8")
    assert "KTC KTS" in homepage

    trace("backend health")
    health = json_request(base_url, "/backend-health", host_header=host_header)
    assert health["status"] == "ok"

    trace("register")
    register = json_request(
        base_url,
        "/api/v1/auth/register",
        method="POST",
        host_header=host_header,
        body={
            "email": email,
            "password": password,
            "full_name": "Production Loop",
            "role": "architect",
            "organization_name": f"KTS Loop {loop_number}",
        },
    )
    token = register["access_token"]

    trace("login")
    login = json_request(
        base_url,
        "/api/v1/auth/login",
        method="POST",
        host_header=host_header,
        body={"email": email, "password": password},
    )
    assert login["access_token"]

    trace("refresh")
    refresh = json_request(
        base_url,
        "/api/v1/auth/refresh",
        method="POST",
        host_header=host_header,
        body={"refresh_token": login["refresh_token"]},
    )
    assert refresh["access_token"]

    trace("create project")
    project = json_request(
        base_url,
        "/api/v1/projects",
        method="POST",
        token=token,
        host_header=host_header,
        body={
            "name": f"Nha Pho Production Loop {loop_number}",
            "client_name": "Anh Production",
            "client_phone": "0901234567",
        },
    )
    project_id = project["id"]

    trace("update brief")
    json_request(
        base_url,
        f"/api/v1/projects/{project_id}/brief",
        method="PUT",
        token=token,
        host_header=host_header,
        body={
            "brief_json": {
                "project_type": "townhouse",
                "project_mode": "new_build",
                "lot": {"width_m": 5, "depth_m": 20, "orientation": "south"},
                "floors": 4,
                "style": "modern_minimalist",
                "rooms": {"bedrooms": 4, "bathrooms": 4},
                "household_profile": "Gia dinh 3 the he",
                "occupant_count": 6,
                "budget_vnd": 4_500_000_000,
                "timeline_months": 8,
                "design_goals": ["Hien dai am, nhieu anh sang tu nhien"],
                "special_requests": ["garage", "balcony"],
                "must_haves": ["gara o to", "phong tho", "lay sang tu nhien"],
            },
            "status": "confirmed",
        },
    )

    trace("chat")
    chat = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/chat",
        method="POST",
        token=token,
        host_header=host_header,
        body={
            "message": "Toi muon nha 5x20m, 4 tang, co gara, phong cach toi gian, can ban cong mat tien va phong tho."
        },
    )
    assert chat["brief_json"]["lot"]["width_m"] == 5
    assert chat["clarification_state"]["total_sections"] >= 6
    assert isinstance(chat["clarification_state"]["blocking_missing"], list)
    assert isinstance(chat["clarification_state"]["sections"], list)
    assert chat["brief_contract_state"] == "reopened"

    trace("chat history")
    history = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/chat/history",
        token=token,
        host_header=host_header,
    )
    assert len(history["messages"]) >= 2

    trace("re-lock brief")
    relocked = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/brief",
        method="PUT",
        token=token,
        host_header=host_header,
        body={
            "brief_json": {},
            "status": "confirmed",
        },
    )
    assert relocked["brief_contract_state"] == "locked"

    trace("generate")
    generation = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/generate",
        method="POST",
        token=token,
        host_header=host_header,
        body={"num_options": 3},
    )
    versions = generation["versions"]
    assert len(versions) == 3
    assert versions[0]["option_title_vi"]
    assert isinstance(versions[0]["fit_reasons"], list)
    assert versions[0]["option_strategy_key"]
    selected_version_id = versions[0]["id"]

    trace("project after generation")
    generated_project = json_request(
        base_url,
        f"/api/v1/projects/{project_id}",
        token=token,
        host_header=host_header,
    )
    assert generated_project["status"] == "options_generated"
    assert generated_project["brief_contract_state"] == "locked"

    trace("select version")
    select = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/select",
        method="POST",
        token=token,
        host_header=host_header,
        body={"comment": "Best option for production loop"},
    )
    assert select["status"] == "under_review"
    assert select["project_status"] == "under_review"

    trace("annotation")
    annotation = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/annotations",
        method="POST",
        token=token,
        host_header=host_header,
        body={"x": 0.44, "y": 0.31, "comment": "Mo rong cua so phong khach"},
    )
    assert annotation["comment"]

    trace("approve")
    approve = json_request(
        base_url,
        f"/api/v1/reviews/{selected_version_id}/approve",
        method="POST",
        token=token,
        host_header=host_header,
        body={"comment": "Ready to lock in production loop"},
    )
    assert approve["status"] == "locked"

    trace("share link")
    share = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/share-links",
        method="POST",
        token=token,
        host_header=host_header,
    )
    share_token = share["token"]

    trace("public share")
    public_share = json_request(
        base_url,
        f"/api/v1/share/{share_token}",
        host_header=host_header,
    )
    assert public_share["project"]["id"] == project_id

    trace("feedback")
    feedback = json_request(
        base_url,
        f"/api/v1/share/{share_token}/feedback",
        method="POST",
        host_header=host_header,
        body={"content": "Nong them khu bep va bo sung gieng troi nho."},
    )
    assert feedback["status"] == "submitted"

    trace("revise")
    revision = json_request(
        base_url,
        f"/api/v1/reviews/{selected_version_id}/revise",
        method="POST",
        token=token,
        host_header=host_header,
        body={"comment": "Nong them khu bep va bo sung gieng troi nho."},
    )
    assert revision["parent_version_id"] == selected_version_id

    trace("export preview")
    exports = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/exports",
        method="POST",
        token=token,
        host_header=host_header,
    )
    package_id = exports["package"]["id"]
    assert exports["package"]["status"] == "review"
    assert exports["package"]["quality_status"] == "pass"

    trace("list packages")
    packages = json_request(
        base_url,
        f"/api/v1/projects/{project_id}/packages",
        token=token,
        host_header=host_header,
    )
    assert packages["data"][0]["id"] == package_id

    trace("issue package")
    issued = json_request(
        base_url,
        f"/api/v1/packages/{package_id}/issue",
        method="POST",
        token=token,
        host_header=host_header,
        body={"note": "Production loop issue approval"},
    )
    assert issued["package"]["status"] == "issued"
    assert issued["version_status"] == "handoff_ready"

    exported_pdf_url = issued["package"]["export_urls"]["pdf"]
    exported_svg_url = issued["package"]["export_urls"]["svg"]
    exported_dxf_url = issued["package"]["export_urls"]["dxf"]
    exported_ifc_url = issued["package"]["export_urls"]["ifc"]
    exported_manifest_url = issued["package"]["export_urls"]["manifest"]
    schedule_csv_urls = {
        "door": issued["package"]["export_urls"]["door_csv"],
        "window": issued["package"]["export_urls"]["window_csv"],
        "room": issued["package"]["export_urls"]["room_csv"],
    }
    package_status = issued["package"]["status"]
    package_issue_date = issued["package"]["issue_date"]

    trace("download pdf")
    assert raw_request(base_url, exported_pdf_url, host_header=host_header).startswith(b"%PDF")
    trace("download svg")
    assert b"<svg" in raw_request(base_url, exported_svg_url, host_header=host_header)
    trace("download dxf")
    assert raw_request(base_url, exported_dxf_url, host_header=host_header)
    trace("download ifc")
    assert raw_request(base_url, exported_ifc_url, host_header=host_header).startswith(b"ISO-10303-21;")
    trace("download manifest")
    manifest = json.loads(raw_request(base_url, exported_manifest_url, host_header=host_header).decode("utf-8"))
    assert manifest["status"] == "issued"
    assert manifest["issue_date"] == package_issue_date
    assert len(manifest["sheets"]) >= 12
    trace("download csv")
    for csv_url in schedule_csv_urls.values():
        csv_payload = raw_request(base_url, csv_url, host_header=host_header).decode("utf-8")
        assert "\n" in csv_payload and "," in csv_payload

    trace("derive 3d")
    derivation = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/derive-3d",
        method="POST",
        token=token,
        host_header=host_header,
    )
    model_url = derivation["model_url"]
    render_urls = derivation["render_urls"]
    assert len(render_urls) >= 1
    trace("download model")
    model_payload = raw_request(base_url, model_url, host_header=host_header).decode("utf-8")
    assert "meshes" in model_payload
    trace("download renders")
    for render_url in render_urls:
        assert b"<svg" in raw_request(base_url, render_url, host_header=host_header)

    trace("handoff")
    handoff = json_request(
        base_url,
        f"/api/v1/versions/{selected_version_id}/handoff",
        method="POST",
        token=token,
        host_header=host_header,
    )
    assert handoff["status"] == "handoff_ready"

    trace("notifications")
    notifications = json_request(
        base_url,
        "/api/v1/notifications",
        token=token,
        host_header=host_header,
    )
    notification_count = len(notifications["data"])
    assert notification_count >= 2

    duration = round(time.perf_counter() - started_at, 2)
    return LoopResult(
        loop_number=loop_number,
        passed=True,
        duration_seconds=duration,
        project_id=project_id,
        selected_version_id=selected_version_id,
        package_id=package_id,
        package_status=package_status,
        package_issue_date=package_issue_date,
        share_token=share_token,
        exported_pdf_url=exported_pdf_url,
        exported_svg_url=exported_svg_url,
        exported_dxf_url=exported_dxf_url,
        exported_ifc_url=exported_ifc_url,
        exported_manifest_url=exported_manifest_url,
        schedule_csv_urls=schedule_csv_urls,
        model_url=model_url,
        render_count=len(render_urls),
        notifications=notification_count,
        checked_at=datetime.now(timezone.utc).isoformat(),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run repeatable production-like checks for the KTC KTS package-centric flow")
    parser.add_argument("--loops", type=int, default=3)
    parser.add_argument("--base-url", default="http://127.0.0.1")
    parser.add_argument("--host-header", default="kts.blackbirdzzzz.art")
    parser.add_argument(
        "--report-path",
        default="/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/production-checks/latest-report.json",
    )
    args = parser.parse_args()

    results: list[dict[str, Any]] = []
    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    for loop_number in range(1, args.loops + 1):
        print(f"[loop {loop_number}] running", flush=True)
        try:
            result = run_single_loop(loop_number, args.base_url, args.host_header)
            results.append(asdict(result))
            print(f"[loop {loop_number}] passed in {result.duration_seconds}s", flush=True)
        except Exception as exc:  # noqa: BLE001
            failure = {
                "loop_number": loop_number,
                "passed": False,
                "error": str(exc),
                "checked_at": datetime.now(timezone.utc).isoformat(),
            }
            results.append(failure)
            report_path.write_text(json.dumps({"results": results}, indent=2), encoding="utf-8")
            print(json.dumps(failure, indent=2), file=sys.stderr)
            return 1

    report_path.write_text(json.dumps({"results": results}, indent=2), encoding="utf-8")
    print(json.dumps({"results": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
