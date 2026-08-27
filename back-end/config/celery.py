import os

from celery import Celery

# Default to local settings so `celery -A config worker` works out of the box
# during development; docker-compose / production override this via env.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("erp_backend")

# Read CELERY_* keys from Django settings (see config/settings/base.py).
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py in every INSTALLED_APPS app.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
