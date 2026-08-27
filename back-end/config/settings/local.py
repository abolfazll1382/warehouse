"""
Local development settings.

Used automatically by manage.py and by the `web` service in
docker-compose.yml (DJANGO_SETTINGS_MODULE=config.settings.local).
"""

from .base import *  # noqa: F401,F403
from .base import env

DEBUG = True

# Wide open locally — you're the only one hitting this server.
ALLOWED_HOSTS = ["*"]

# Don't fight CORS while you're building the frontend integration; lock this
# down to CORS_ALLOWED_ORIGINS in production.
CORS_ALLOW_ALL_ORIGINS = True

# Background-job emails print to the runserver console instead of needing
# real SMTP creds while you develop.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Surface real DB errors instead of Django's pretty (and slow) debug pages
# when iterating on the API directly.
REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
}

# Celery: run tasks synchronously if you haven't got the worker container up
# yet — flip via .env, defaults to real async behaviour like production.
CELERY_TASK_ALWAYS_EAGER = env.bool("CELERY_TASK_ALWAYS_EAGER", default=False)
