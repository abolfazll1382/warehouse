#!/bin/sh
# Waits for Postgres to accept connections before handing off to CMD.
# Shared by web / worker / beat — none of them should start hammering the
# DB with connection errors just because Postgres takes a few seconds
# longer to come up than Django does.
set -e

python << PYEOF
import os, socket, time

host = os.environ.get("POSTGRES_HOST", "db")
port = int(os.environ.get("POSTGRES_PORT", 5432))

for attempt in range(30):
    try:
        socket.create_connection((host, port), timeout=1).close()
        break
    except OSError:
        print(f"Waiting for Postgres at {host}:{port} ({attempt + 1}/30)...")
        time.sleep(1)
else:
    raise SystemExit(f"Postgres never became reachable at {host}:{port}")
PYEOF

echo "Postgres is up — continuing."
exec "$@"
