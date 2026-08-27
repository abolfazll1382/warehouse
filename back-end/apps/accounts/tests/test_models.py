import pytest

from apps.accounts.models import User

pytestmark = pytest.mark.django_db


class TestUserManager:
    def test_create_user_normalizes_email_and_hashes_password(self):
        user = User.objects.create_user(email="Test@Example.com", password="s3cret-pass")

        assert user.email == "test@example.com" or user.email == "Test@example.com"
        assert user.password != "s3cret-pass"
        assert user.check_password("s3cret-pass")
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_user_requires_email(self):
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="s3cret-pass")

    def test_create_superuser_sets_staff_and_superuser_flags(self):
        admin = User.objects.create_superuser(email="admin@example.com", password="s3cret-pass")

        assert admin.is_staff is True
        assert admin.is_superuser is True

    def test_create_superuser_rejects_is_staff_false(self):
        with pytest.raises(ValueError):
            User.objects.create_superuser(email="admin@example.com", password="x", is_staff=False)
