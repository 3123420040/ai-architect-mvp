#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNTIME_FILE="${ROOT_DIR}/.env.production.runtime"
PUBLIC_HOSTNAME="${KTS_PUBLIC_HOSTNAME:-kts.blackbirdzzzz.art}"
TUNNEL_NAME="${KTS_PUBLIC_TUNNEL_NAME:-kts-blackbirdzzzz-art}"

if [[ ! -f "${HOME}/.config/blackbird-deploy/load_runtime.sh" ]]; then
  echo "Missing Cloudflare runtime helper at ~/.config/blackbird-deploy/load_runtime.sh" >&2
  exit 1
fi

# shellcheck disable=SC1091
source "${HOME}/.config/blackbird-deploy/load_runtime.sh" >/dev/null 2>&1

if [[ -z "${CF_ACCOUNT_ID:-}" || -z "${CF_ZONE_ID:-}" || -z "${CF_API_TOKEN:-}" ]]; then
  echo "Cloudflare runtime is incomplete. Need CF_ACCOUNT_ID, CF_ZONE_ID, and CF_API_TOKEN." >&2
  exit 1
fi

cf_api() {
  local method="$1"
  local path="$2"
  local body="${3:-}"
  if [[ -n "${body}" ]]; then
    curl -fsS -X "${method}" "https://api.cloudflare.com/client/v4${path}" \
      -H "Authorization: Bearer ${CF_API_TOKEN}" \
      -H "Content-Type: application/json" \
      --data "${body}"
  else
    curl -fsS -X "${method}" "https://api.cloudflare.com/client/v4${path}" \
      -H "Authorization: Bearer ${CF_API_TOKEN}"
  fi
}

ensure_tunnel() {
  local existing_id
  existing_id="$(
    cf_api GET "/accounts/${CF_ACCOUNT_ID}/cfd_tunnel" |
      jq -r --arg name "${TUNNEL_NAME}" '.result[] | select(.name == $name) | .id' |
      head -n 1
  )"

  if [[ -n "${existing_id}" ]]; then
    printf '%s' "${existing_id}"
    return
  fi

  cf_api POST "/accounts/${CF_ACCOUNT_ID}/cfd_tunnel" \
    "$(jq -nc --arg name "${TUNNEL_NAME}" '{name: $name, config_src: "cloudflare"}')" |
    jq -r '.result.id'
}

write_tunnel_config() {
  local tunnel_id="$1"
  local config_payload
  config_payload="$(
    jq -nc --arg hostname "${PUBLIC_HOSTNAME}" '{
      config: {
        ingress: [
          {
            hostname: $hostname,
            service: "http://caddy:80"
          },
          {
            service: "http_status:404"
          }
        ],
        "warp-routing": {
          enabled: false
        }
      }
    }'
  )"
  cf_api PUT "/accounts/${CF_ACCOUNT_ID}/cfd_tunnel/${tunnel_id}/configurations" "${config_payload}" >/dev/null
}

ensure_dns_record() {
  local tunnel_id="$1"
  local tunnel_target="${tunnel_id}.cfargotunnel.com"
  local existing_id

  existing_id="$(
    cf_api GET "/zones/${CF_ZONE_ID}/dns_records?type=CNAME&name=${PUBLIC_HOSTNAME}" |
      jq -r '.result[0].id // empty'
  )"

  local dns_payload
  dns_payload="$(
    jq -nc --arg name "${PUBLIC_HOSTNAME}" --arg content "${tunnel_target}" '{
      type: "CNAME",
      name: $name,
      content: $content,
      proxied: true
    }'
  )"

  if [[ -n "${existing_id}" ]]; then
    cf_api PUT "/zones/${CF_ZONE_ID}/dns_records/${existing_id}" "${dns_payload}" >/dev/null
  else
    cf_api POST "/zones/${CF_ZONE_ID}/dns_records" "${dns_payload}" >/dev/null
  fi
}

detach_hostname_from_shared_tunnel() {
  if [[ -z "${CF_TUNNEL_ID:-}" || "${CF_TUNNEL_ID}" == "${1}" ]]; then
    return
  fi

  local current_config
  current_config="$(cf_api GET "/accounts/${CF_ACCOUNT_ID}/cfd_tunnel/${CF_TUNNEL_ID}/configurations")"

  local updated_config
  updated_config="$(
    printf '%s' "${current_config}" |
      jq --arg hostname "${PUBLIC_HOSTNAME}" '{
        config: (
          .result.config
          | .ingress = [(.ingress // [])[] | select(.hostname? != $hostname)]
        )
      }'
  )"

  cf_api PUT "/accounts/${CF_ACCOUNT_ID}/cfd_tunnel/${CF_TUNNEL_ID}/configurations" "${updated_config}" >/dev/null
}

write_runtime_file() {
  local tunnel_id="$1"
  local tunnel_token
  tunnel_token="$(
    cf_api GET "/accounts/${CF_ACCOUNT_ID}/cfd_tunnel/${tunnel_id}/token" |
      jq -r '.result'
  )"

  umask 077
  cat > "${RUNTIME_FILE}" <<EOF
CF_TUNNEL_TOKEN=${tunnel_token}
KTS_CLOUDFLARE_TUNNEL_ID=${tunnel_id}
KTS_PUBLIC_HOSTNAME=${PUBLIC_HOSTNAME}
EOF
}

main() {
  local tunnel_id
  tunnel_id="$(ensure_tunnel)"
  write_tunnel_config "${tunnel_id}"
  ensure_dns_record "${tunnel_id}"
  detach_hostname_from_shared_tunnel "${tunnel_id}"
  write_runtime_file "${tunnel_id}"

  echo "Configured dedicated Cloudflare tunnel ${tunnel_id} for ${PUBLIC_HOSTNAME}."
  echo "Runtime file written to ${RUNTIME_FILE}."
}

main "$@"
