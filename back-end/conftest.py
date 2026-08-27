import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authed_client(api_client, django_user_model):
    """An APIClient already carrying a valid JWT for a plain (no-department)
    user — use `authed_client(department=...)` patterns per-app for
    permission tests instead of re-deriving auth in every test module."""

    def _make(*, department: str = "", is_superuser: bool = False):
        user = django_user_model.objects.create_user(
            email=f"user{django_user_model.objects.count()}@test.local",
            password="test-pass-123",
            department=department,
            is_superuser=is_superuser,
            is_staff=is_superuser,
        )
        client = APIClient()
        client.force_authenticate(user=user)
        return client, user

    return _make
