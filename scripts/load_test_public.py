from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0.0.0 Safari/537.36"
)


@dataclass
class RequestResult:
    ok: bool
    status_code: int
    duration_ms: float
    path: str


def curl_request(base_url: str, path: str) -> RequestResult:
    started = time.perf_counter()
    command = [
        "curl",
        "-sS",
        "-o",
        "/dev/null",
        "-w",
        "%{http_code}",
        "-H",
        f"User-Agent: {USER_AGENT}",
        "-H",
        "Connection: close",
        f"{base_url}{path}",
    ]
    response = subprocess.run(command, capture_output=True, check=False)
    duration_ms = round((time.perf_counter() - started) * 1000, 2)
    status_code = int(response.stdout.decode("utf-8") or "0")
    return RequestResult(
        ok=response.returncode == 0 and 200 <= status_code < 400,
        status_code=status_code,
        duration_ms=duration_ms,
        path=path,
    )


def percentile(values: list[float], ratio: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, int(round((len(ordered) - 1) * ratio))))
    return ordered[index]


def main() -> int:
    parser = argparse.ArgumentParser(description="Simple public load baseline for kts.blackbirdzzzz.art")
    parser.add_argument("--base-url", default="https://kts.blackbirdzzzz.art")
    parser.add_argument("--requests", type=int, default=50)
    parser.add_argument("--concurrency", type=int, default=10)
    parser.add_argument(
        "--paths",
        nargs="*",
        default=["/", "/backend-health"],
        help="Paths to rotate during the load test",
    )
    parser.add_argument(
        "--report-path",
        default="/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/load-tests/public-baseline.json",
    )
    args = parser.parse_args()

    jobs = [args.paths[index % len(args.paths)] for index in range(args.requests)]
    results: list[RequestResult] = []

    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
      futures = [executor.submit(curl_request, args.base_url, path) for path in jobs]
      for future in as_completed(futures):
          results.append(future.result())

    durations = [item.duration_ms for item in results]
    passed = [item for item in results if item.ok]
    failed = [item for item in results if not item.ok]

    report = {
        "summary": {
            "base_url": args.base_url,
            "requests": args.requests,
            "concurrency": args.concurrency,
            "passed": len(passed),
            "failed": len(failed),
            "avg_ms": round(statistics.mean(durations), 2) if durations else 0.0,
            "p95_ms": round(percentile(durations, 0.95), 2),
            "max_ms": max(durations) if durations else 0.0,
        },
        "results": [asdict(item) for item in results],
    }

    report_path = Path(args.report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
