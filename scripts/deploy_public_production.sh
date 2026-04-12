#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_FILE="${ROOT_DIR}/.env.production.runtime"
APP_ENV_FILE="${ROOT_DIR}/.env.production.app"

if [[ ! -f "${RUNTIME_FILE}" ]]; then
  "${ROOT_DIR}/scripts/configure_public_tunnel.sh"
fi

set -a
# shellcheck disable=SC1091
source "${RUNTIME_FILE}"

if [[ -f "${APP_ENV_FILE}" ]]; then
  # shellcheck disable=SC1091
  source "${APP_ENV_FILE}"
fi
set +a

export NEXT_PUBLIC_API_URL="${NEXT_PUBLIC_API_URL:-/api/v1}"
export NEXT_PUBLIC_WS_URL="${NEXT_PUBLIC_WS_URL:-/}"
export NEXT_PUBLIC_APP_URL="${NEXT_PUBLIC_APP_URL:-https://kts.blackbirdzzzz.art}"
export APP_CORS_ORIGINS="${APP_CORS_ORIGINS:-https://kts.blackbirdzzzz.art,http://localhost}"
export PUBLIC_BASE_URL="${PUBLIC_BASE_URL:-https://kts.blackbirdzzzz.art}"
export PUBLIC_HTTP_PORT="${PUBLIC_HTTP_PORT:-80}"

docker compose -f "${ROOT_DIR}/docker-compose.production.yml" --profile public-edge up -d --build
