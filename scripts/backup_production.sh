#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP="$(date '+%Y%m%d-%H%M%S')"
BACKUP_DIR="${ROOT_DIR}/artifacts/backups/${STAMP}"
POSTGRES_CONTAINER="${POSTGRES_CONTAINER:-kts-blackbirdzzzz-art-postgres-prod}"
POSTGRES_DB="${POSTGRES_DB:-ai_architect}"
POSTGRES_USER="${POSTGRES_USER:-dev}"

resolve_volume() {
  local suffix="$1"
  docker volume ls --format '{{.Name}}' | awk -v needle="${suffix}" '$0 ~ needle "$" { print; exit }'
}

archive_volume() {
  local volume_name="$1"
  local output_name="$2"
  docker run --rm \
    -v "${volume_name}:/source:ro" \
    -v "${BACKUP_DIR}:/backup" \
    alpine:3.20 \
    sh -lc "cd /source && tar -czf /backup/${output_name} ."
}

main() {
  mkdir -p "${BACKUP_DIR}"

  docker exec "${POSTGRES_CONTAINER}" pg_dump -U "${POSTGRES_USER}" "${POSTGRES_DB}" > "${BACKUP_DIR}/database.sql"

  local pg_volume
  local storage_volume
  pg_volume="$(resolve_volume 'pgdata_prod')"
  storage_volume="$(resolve_volume 'api_storage_prod')"

  if [[ -n "${pg_volume}" ]]; then
    archive_volume "${pg_volume}" "postgres-volume.tar.gz"
  fi

  if [[ -n "${storage_volume}" ]]; then
    archive_volume "${storage_volume}" "api-storage.tar.gz"
  fi

  cat > "${BACKUP_DIR}/manifest.json" <<EOF
{
  "created_at": "${STAMP}",
  "postgres_container": "${POSTGRES_CONTAINER}",
  "postgres_db": "${POSTGRES_DB}",
  "postgres_user": "${POSTGRES_USER}",
  "postgres_volume": "${pg_volume:-}",
  "api_storage_volume": "${storage_volume:-}"
}
EOF

  echo "Backup completed at ${BACKUP_DIR}"
}

main "$@"
