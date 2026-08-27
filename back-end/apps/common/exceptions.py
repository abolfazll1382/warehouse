import logging

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

logger = logging.getLogger(__name__)


class ServiceError(APIException):
    """
    Raise this from a services.py function for a business-rule violation
    (e.g. "cannot issue more stock than is on hand"). It's a 400 by default —
    pass status_code= to override.

        raise ServiceError("Cannot issue more than current stock.")
    """

    status_code = 400
    default_code = "service_error"

    def __init__(self, detail, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        super().__init__(detail)


def erp_exception_handler(exc, context):
    """
    Wraps DRF's default handler so every error response — validation,
    permission, not-found, or a raised ServiceError — has the same shape:

        {"detail": "...", "code": "..."}

    instead of DRF's default shape varying by exception type. Makes the
    frontend's error handling one code path instead of five.
    """
    response = drf_exception_handler(exc, context)

    if response is None:
        # Unhandled exception — don't leak internals, but do log them.
        logger.exception("Unhandled exception in %s", context.get("view"))
        return Response(
            {"detail": "Internal server error.", "code": "internal_error"},
            status=500,
        )

    detail = response.data.get("detail", response.data) if isinstance(response.data, dict) else response.data
    response.data = {
        "detail": detail,
        "code": getattr(exc, "default_code", "error"),
    }
    return response
