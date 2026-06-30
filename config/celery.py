"""Celery application bootstrap.

Wires Celery to Django settings and auto-discovers task modules in every
installed app (e.g. users.tasks).
"""

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("warehouse_erp")

# Read all CELERY_* settings from Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Look for tasks.py inside every installed app.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
