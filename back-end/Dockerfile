# syntax=docker/dockerfile:1

# ---------------------------------------------------------------------------
# base — OS deps + Python deps shared by every environment. Kept as its own
# stage so `local` and `production` don't duplicate the apt-get layer.
# ---------------------------------------------------------------------------
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY requirements/ requirements/

# ---------------------------------------------------------------------------
# local — used by docker-compose.yml. Code is bind-mounted over this at
# runtime (see the volumes: in docker-compose.yml), so COPY . . here mostly
# just means `docker build` also works standalone without compose.
# ---------------------------------------------------------------------------
FROM base AS local

RUN pip install -r requirements/local.txt
COPY . .

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ---------------------------------------------------------------------------
# production — used by docker-compose.prod.yml. No bind mount: the image is
# the deployable artifact. Runs as a non-root user and serves via gunicorn.
# ---------------------------------------------------------------------------
FROM base AS production

RUN pip install -r requirements/production.txt
COPY . .

RUN addgroup --system django && adduser --system --ingroup django django \
    && chown -R django:django /app
USER django

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
