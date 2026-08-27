import logging

logger = logging.getLogger(__name__)


def safe_delay(task, **kwargs):
    """
    Dispatch a Celery task without letting a broker outage break the caller.

    Any `.delay()` called from inside a request (a notification, a
    low-stock check, ...) is a side effect, not the thing the user actually
    asked for — issuing stock must succeed even if Valkey is briefly down.
    Combined with CELERY_TASK_PUBLISH_RETRY_POLICY (settings/base.py), a
    broker outage fails in ~0.4s and lands here instead of hanging or
    surfacing as a 500 on an otherwise-successful operation.
    """
    try:
        task.delay(**kwargs)
    except Exception:
        logger.warning("Could not dispatch task %s(%s) — broker unreachable?", task.name, kwargs, exc_info=True)
