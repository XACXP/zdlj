#!/bin/bash
# Upload a local image to Alibaba CDN via the local Accio gateway.
#
# Prerequisites: Accio desktop app must be running and user must be logged in.
#
# Usage:
#   bash scripts/upload-image-to-cdn.sh <image_path>
#   bash scripts/upload-image-to-cdn.sh ~/Downloads/photo.jpg
#
# Output (stdout): the CDN URL on success, or an error message on failure.
# Exit code: 0 on success, 1 on failure.

set -euo pipefail

IMAGE_PATH="${1:?Usage: upload-image-to-cdn.sh <image_path>}"

# Expand ~ if present
IMAGE_PATH="${IMAGE_PATH/#\~/$HOME}"

if [ ! -f "$IMAGE_PATH" ]; then
  echo "Error: file not found: $IMAGE_PATH" >&2
  exit 1
fi

# Auto-detect gateway port: try 4097 (default) then 4098 (fallback), or use env override
if [ -n "${GATEWAY_PORT:-}" ]; then
  PORTS=("$GATEWAY_PORT")
else
  PORTS=(4097 4098)
fi

GATEWAY_PORT=""
for p in "${PORTS[@]}"; do
  if curl -s -o /dev/null -w '' --connect-timeout 1 "http://127.0.0.1:${p}/" 2>/dev/null; then
    GATEWAY_PORT="$p"
    break
  fi
done

if [ -z "$GATEWAY_PORT" ]; then
  echo "Error: Accio gateway not reachable on ports ${PORTS[*]}. Is the app running?" >&2
  exit 1
fi

# Use python to encode + POST (avoids shell ARG_MAX limit for large images)
python3 -c "
import base64, json, urllib.request, sys, os

path = sys.argv[1]
port = sys.argv[2]

with open(path, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

ext = path.rsplit('.', 1)[-1].lower()
mime_map = {
    'jpg': 'image/jpeg', 'jpeg': 'image/jpeg',
    'png': 'image/png', 'webp': 'image/webp',
    'gif': 'image/gif', 'bmp': 'image/bmp',
}
mime = mime_map.get(ext, 'image/jpeg')
data_uri = f'data:{mime};base64,{b64}'

payload = json.dumps({'data_uri': data_uri}).encode()
req = urllib.request.Request(
    f'http://127.0.0.1:{port}/api/image/cdn/upload',
    data=payload,
    headers={'Content-Type': 'application/json'},
    method='POST',
)

try:
    resp = urllib.request.urlopen(req, timeout=120)
    result = json.loads(resp.read())
    url = result.get('url')
    if url:
        print(url)
    else:
        print(f'Error: unexpected response: {json.dumps(result)}', file=sys.stderr)
        sys.exit(1)
except Exception as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)
" "$IMAGE_PATH" "$GATEWAY_PORT"
