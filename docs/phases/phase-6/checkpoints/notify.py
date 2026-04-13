#!/usr/bin/env python3
"""
Checkpoint notification script.
Sends status to ntfy.sh after each CP implementation or validation.

Usage (Implementation Agent):
    python checkpoints/notify.py \\
        --cp cp0-phase6-scope-lock-and-baseline-audit \\
        --role implementer \\
        --status READY \\
        --summary "Checkpoint implementation is ready for validation." \\
        --result-file artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/result.json

Usage (Validator Agent):
    python checkpoints/notify.py \\
        --cp cp0-phase6-scope-lock-and-baseline-audit \\
        --role validator \\
        --status PASS \\
        --summary "All checks passed." \\
        --result-file artifacts/phase6/cp0-phase6-scope-lock-and-baseline-audit/validation.json

Status values:
    implementer: READY | BLOCKED
    validator:   PASS | FAIL | PARTIAL
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / "config.json"


def load_config() -> dict:
    config = {
        "ntfy_topic": "",
        "ntfy_base": "https://ntfy.sh",
        "dashboard_url": "http://localhost:3000",
        "project_slug": "",
    }

    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config.update(json.load(f))

    if os.environ.get("NTFY_TOPIC"):
        config["ntfy_topic"] = os.environ["NTFY_TOPIC"]
    if os.environ.get("NTFY_BASE"):
        config["ntfy_base"] = os.environ["NTFY_BASE"]
    if os.environ.get("DASHBOARD_URL"):
        config["dashboard_url"] = os.environ["DASHBOARD_URL"]
    if os.environ.get("PROJECT_SLUG"):
        config["project_slug"] = os.environ["PROJECT_SLUG"]

    return config


STATUS_EMOJI = {
    "READY": "✅",
    "BLOCKED": "🚫",
    "PASS": "✅",
    "FAIL": "❌",
    "PARTIAL": "⚠️",
}

STATUS_PRIORITY = {
    "READY": "default",
    "BLOCKED": "high",
    "PASS": "default",
    "FAIL": "high",
    "PARTIAL": "default",
}


def send_ntfy(topic: str, base_url: str, title: str, message: str, priority: str = "default", tags: str = "") -> bool:
    url = f"{base_url.rstrip('/')}/{topic}"
    headers = {
        "Title": title.encode("utf-8"),
        "Priority": priority,
        "Content-Type": "text/plain; charset=utf-8",
    }
    if tags:
        headers["Tags"] = tags

    try:
        data = message.encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except urllib.error.URLError as exc:
        print(f"  ✗ Failed to send to ntfy.sh: {exc}", file=sys.stderr)
        return False


def post_dashboard_status(result_file: str, config: dict) -> bool:
    dashboard_url = config.get("dashboard_url", "").strip()
    project_slug = config.get("project_slug", "").strip()

    if not dashboard_url or not project_slug:
        print("  - Skip dashboard sync: dashboard_url/project_slug not configured")
        return False

    script_path = SCRIPT_DIR / "post-status.py"
    cmd = [
        sys.executable,
        str(script_path),
        "--result-file",
        result_file,
        "--dashboard-url",
        dashboard_url,
        "--project-slug",
        project_slug,
    ]

    print("\nPosting status to dashboard...")
    print(f"  URL:  {dashboard_url}")
    print(f"  Slug: {project_slug}")
    completed = subprocess.run(cmd, check=False)
    return completed.returncode == 0


def notify(cp: str, role: str, status: str, summary: str, result_file: str, config: dict):
    if not config.get("ntfy_topic"):
        print(
            "\nERROR: ntfy_topic not configured.\n"
            "  Option 1: Set NTFY_TOPIC env var\n"
            "  Option 2: Edit checkpoints/config.json\n",
            file=sys.stderr,
        )
        sys.exit(1)

    emoji = STATUS_EMOJI.get(status, "ℹ️")
    role_label = "impl" if role == "implementer" else "validator"
    title = f"[Phase6] {cp} | {role_label} | {status} {emoji}"

    tags_map = {
        ("implementer", "READY"): "white_check_mark,computer",
        ("implementer", "BLOCKED"): "no_entry,computer",
        ("validator", "PASS"): "white_check_mark,test_tube",
        ("validator", "FAIL"): "x,test_tube",
        ("validator", "PARTIAL"): "warning,test_tube",
    }
    tags = tags_map.get((role, status), "information_source")

    message_lines = [
        summary,
        "",
        f"CP:          {cp}",
        f"Role:        {role_label}",
        f"Status:      {status} {emoji}",
        f"Result file: {result_file}",
        f"Time:        {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Dashboard: https://ntfy.sh/{config['ntfy_topic']}",
    ]

    print("\nSending notification...")
    print(f"  Title:   {title}")
    print(f"  Topic:   {config['ntfy_topic']}")

    ok = send_ntfy(
        topic=config["ntfy_topic"],
        base_url=config["ntfy_base"],
        title=title,
        message="\n".join(message_lines),
        priority=STATUS_PRIORITY.get(status, "default"),
        tags=tags,
    )

    if ok:
        print("  ✓ Sent successfully")
        print(f"\nView at: https://ntfy.sh/{config['ntfy_topic']}")
    else:
        print("  ✗ Failed — check network or topic name", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Send checkpoint notification")
    parser.add_argument("--cp", required=True)
    parser.add_argument("--role", required=True, choices=["implementer", "validator"])
    parser.add_argument("--status", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--result-file", required=True)
    parser.add_argument("--post-dashboard", action="store_true")
    args = parser.parse_args()

    config = load_config()
    notify(args.cp, args.role, args.status, args.summary, args.result_file, config)

    if args.post_dashboard:
        ok = post_dashboard_status(args.result_file, config)
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
