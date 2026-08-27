# Arvin ERP — Backend

Django + Django REST Framework backend for the [Arvin ERP dashboard](../erp-dashboard) —
HR, Production, Purchasing, Sales, Inventory and Finance, built to the same
module structure as the frontend so the two plug together directly.

## Stack

| | |
|---|---|
| Language | Python 3.12 |
| Framework | Django 5.2 LTS + Django REST Framework 3.18 |
| Database | PostgreSQL 17 |
| Cache / Celery broker | [Valkey](https://valkey.io) 8 (Redis-protocol compatible — see *Why Valkey, not Redis* below) |
| Async tasks | Celery 5.6 + Celery Beat |
| Auth | JWT (`djangorestframework-simplejwt`) |
| API docs | `drf-spectacular` → OpenAPI schema + Swagger UI + Redoc |
| Containerization | Docker (multi-stage) + docker-compose |

## Quick start

```bash
git clone <this repo> erp-backend && cd erp-backend
# .env is already included with working dev defaults — see "About .env" below
docker compose up --build
```

Then:
- API root: **http://localhost:8000/api/v1/**
- Swagger UI: **http://localhost:8000/api/v1/docs/**
- Redoc: **http://localhost:8000/api/v1/redoc/**
- Admin: **http://localhost:8000/admin/**

Create yourself an admin user in a second terminal:

```bash
docker compose exec web python manage.py createsuperuser
```

### About the Postgres port

**Host port 5432 is remapped to `5435`** because 5432–5434 were already in
use by other projects on this machine (`POSTGRES_HOST_PORT` in `.env`).
Postgres still listens on 5432 *inside* the Docker network — Django's
`POSTGRES_PORT` stays 5432 regardless. If 5435 is also taken, change
`POSTGRES_HOST_PORT` (and `DJANGO_HOST_PORT` / `VALKEY_HOST_PORT` if those
collide too) in `.env` — nothing else needs to change.

### About `.env`

Both `.env` and `.env.example` are included. `.env` has working dev-only
credentials so `docker compose up` works immediately after cloning — it is
still git-ignored (check `.gitignore`), because the habit of never
committing `.env` matters more than whether *this particular* file has real
secrets in it. `.env.example` is the template that actually gets committed.
For anything beyond your own machine, treat every value in `.env` as
compromised and regenerate it.

## Project structure

```
config/
  settings/
    base.py         # shared by every environment
    local.py         # DEBUG=True, used by docker-compose.yml
    production.py     # gunicorn/whitenoise/security headers, used by docker-compose.prod.yml
  celery.py           # Celery app, autodiscovers tasks.py in every app
  urls.py             # wires up each app's urls.py + /schema/, /docs/, /redoc/

apps/
  common/         # TimeStampedModel, permission bases, exception handler, safe_delay()
  accounts/        # custom User (email-based auth, `department` field)
  inventory/       # the reference app — see "The pattern" below
  hr/  production/  purchasing/  sales/  finance/
  dashboard/       # no models — aggregates the other 6 apps for the Overview page

docker/entrypoint.sh   # waits for Postgres before migrate/runserver/celery start
requirements/{base,local,production}.txt
docker-compose.yml       # local dev
docker-compose.prod.yml   # production reference (see its header comment for caveats)
```

Every domain app follows the same shape:

```
apps/<name>/
  models.py        # shape of the data, invariants that must always hold
  selectors.py       # read queries (so every "give me the list" builds it the same way)
  services.py          # writes with real business logic (omitted where there isn't any)
  permissions.py          # who's allowed to touch this module
  serializers.py            # shape over the wire + validation
  views.py                    # thin — parse request, call service/selector, return response
  urls.py
  admin.py
  tests/
```

## The pattern, in one app

`apps/inventory` is the fullest example — receiving and issuing stock both
go through `services.py`, which is the only code path allowed to change
`InventoryItem.quantity`, and every change is logged to `StockMovement` for
a real audit trail instead of a bare mutable counter. `apps/sales/services.py`
composes on top of it: creating an invoice atomically creates its line items
*and* issues the matching stock out of inventory in the same transaction —
read those two files together to see how the pieces fit.

Not every app needs a `services.py`. HR/Production/Purchasing are close to
plain CRUD, so they don't have one — adding one anyway would be ceremony,
not architecture.

## Permissions

`apps/common/permissions.IsDepartmentStaff` is the base: management and
superusers always pass, everyone else must belong to the exact department a
view requires. Each app subclasses it once:

```python
class IsHRStaff(IsDepartmentStaff):
    department = "hr"
```

HR and Finance use the strict version (no read access outside the
department — this is salary and account-balance data). Inventory,
Production, Purchasing and Sales use `IsDepartmentStaffOrReadOnly` instead,
since e.g. Sales staff legitimately need to *see* stock levels even though
only Inventory can change them.

## Background jobs (Celery)

`apps/inventory/tasks.py` has the two real examples: `notify_low_stock`
(fired from `services.inventory_item_issue` when a movement drops an item
to/below its reorder threshold) and `check_all_low_stock` (a daily sweep —
register it in **Admin → Periodic Tasks** to schedule it via Celery Beat).

Every task is dispatched through `apps/common/tasks.safe_delay()`, not
`.delay()` directly — a notification is a side effect, not the thing the
caller actually asked for, so a broker hiccup must never turn "issue this
stock" into a failed or hanging request. This isn't hypothetical: it's a
real bug that was caught and fixed during this build (see the git log and
`apps/inventory/tests/test_services.py::test_low_stock_notification_does_not_break_the_request`)
— dispatching a task with `CELERY_RESULT_BACKEND` pointed at an unreachable
broker hung for ~19 seconds per request. Fixed via `CELERY_TASK_IGNORE_RESULT`
(these tasks are fire-and-forget, so there's no result to store) plus the
`safe_delay` wrapper as a second line of defense.

## Why Valkey, not Redis

Redis relicensed away from an OSI-approved license in 2024; the community
(Linux Foundation, AWS, Google, and the original Redis maintainers among
them) forked it as **Valkey**, which is what current Ubuntu/Debian/Fedora
ship by default and what AWS/GCP default new managed cache instances to.
Same wire protocol, same `redis-py` client — `docker-compose.yml` just pulls
`valkey/valkey:8-alpine` instead of `redis:alpine`, nothing else changes.

## Running tests

```bash
docker compose exec web pytest
# or on the host, against the same Postgres via the exposed 5435 port:
pytest
```

22 tests currently — `apps/accounts` (custom user manager) and
`apps/inventory` (models, services, and permission-enforcement API tests)
are built out as the reference; the other apps follow the same
`factories.py` + `test_models.py` + `test_services.py` + `test_api.py`
shape when you extend them.

## Frontend integration

`DJANGO_CORS_ALLOWED_ORIGINS` in `.env` already includes
`http://localhost:3000` (the Next.js dev server from the `erp-dashboard`
project). Point the frontend's `NEXT_PUBLIC_API_BASE_URL` at
`http://localhost:8000/api/v1` and:

- `POST /api/v1/auth/token/` returns `{access, refresh, user}` in one call
- `GET /api/v1/dashboard/overview/` returns exactly the shape
  `RevenueChart` / `KpiCard` / `RecentTransactions` / `TopProducts` expect —
  it returns raw numbers and semantic `id`s, not Persian labels; the
  frontend already owns that mapping in `lib/nav-config.ts` / `lib/data/*`,
  so that's where labels stay

## Known limitations / next steps

- **Enum naming in the OpenAPI schema**: several models have a `status`
  field with different choices; `drf-spectacular` resolves the resulting
  name collision automatically (e.g. `StatusA8fEnum`) but it's not pretty.
  Cosmetic only — fix via `ENUM_NAME_OVERRIDES` in `SPECTACULAR_SETTINGS`
  if it bothers you enough.
- **`docker-compose.prod.yml`** is a real starting point, not a hardened
  deployment — it deliberately has no reverse proxy / TLS termination in
  front of it (see the comment at the top of that file for why).
- Only inventory + accounts have a full test suite; extend the others
  following the same shape.
- No object storage wired up for `MEDIA_ROOT` in production — fine for now
  since nothing in the current models uses file uploads.
