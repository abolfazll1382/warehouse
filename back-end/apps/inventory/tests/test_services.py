import pytest

from apps.common.exceptions import ServiceError
from apps.inventory import services
from apps.inventory.models import StockMovement
from apps.inventory.tests.factories import InventoryItemFactory

pytestmark = pytest.mark.django_db


class TestInventoryItemReceive:
    def test_increases_quantity(self, django_user_model):
        item = InventoryItemFactory(quantity=10)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        services.inventory_item_receive(item=item, quantity=25, reason="purchase", actor=actor)

        item.refresh_from_db()
        assert item.quantity == 35

    def test_creates_positive_stock_movement(self, django_user_model):
        item = InventoryItemFactory(quantity=10)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        services.inventory_item_receive(item=item, quantity=25, reason="purchase", actor=actor)

        movement = StockMovement.objects.get(item=item)
        assert movement.quantity == 25
        assert movement.reason == "purchase"

    def test_rejects_non_positive_quantity(self, django_user_model):
        item = InventoryItemFactory(quantity=10)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        with pytest.raises(ServiceError):
            services.inventory_item_receive(item=item, quantity=0, reason="purchase", actor=actor)


class TestInventoryItemIssue:
    def test_decreases_quantity(self, django_user_model):
        item = InventoryItemFactory(quantity=50)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        services.inventory_item_issue(item=item, quantity=20, reason="sale", actor=actor)

        item.refresh_from_db()
        assert item.quantity == 30

    def test_records_negative_stock_movement(self, django_user_model):
        item = InventoryItemFactory(quantity=50)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        services.inventory_item_issue(item=item, quantity=20, reason="sale", actor=actor)

        movement = StockMovement.objects.get(item=item)
        assert movement.quantity == -20

    def test_rejects_issuing_more_than_available(self, django_user_model):
        item = InventoryItemFactory(quantity=5)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        with pytest.raises(ServiceError, match="only 5"):
            services.inventory_item_issue(item=item, quantity=10, reason="sale", actor=actor)

        # Nothing should have changed — the whole point of the check.
        item.refresh_from_db()
        assert item.quantity == 5
        assert not StockMovement.objects.filter(item=item).exists()

    def test_low_stock_notification_does_not_break_the_request(self, django_user_model, settings):
        """Regression test: dispatching notify_low_stock must never raise
        or hang the caller, even if the broker is unreachable — see
        apps/common/tasks.safe_delay and CELERY_TASK_IGNORE_RESULT."""
        settings.CELERY_TASK_ALWAYS_EAGER = False
        item = InventoryItemFactory(quantity=12, reorder_threshold=10)
        actor = django_user_model.objects.create_user(email="a@test.local", password="x")

        # Should complete normally and NOT raise, regardless of broker state.
        result = services.inventory_item_issue(item=item, quantity=5, reason="sale", actor=actor)

        assert result.quantity == 7
        assert result.status == "low_stock"
