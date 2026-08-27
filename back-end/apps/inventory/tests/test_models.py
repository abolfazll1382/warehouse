import pytest

from apps.inventory.tests.factories import InventoryItemFactory

pytestmark = pytest.mark.django_db


class TestInventoryItemStatus:
    def test_in_stock_when_above_threshold(self):
        item = InventoryItemFactory(quantity=50, reorder_threshold=10)
        assert item.status == "in_stock"

    def test_low_stock_at_threshold(self):
        item = InventoryItemFactory(quantity=10, reorder_threshold=10)
        assert item.status == "low_stock"

    def test_low_stock_below_threshold(self):
        item = InventoryItemFactory(quantity=3, reorder_threshold=10)
        assert item.status == "low_stock"

    def test_out_of_stock_at_zero(self):
        item = InventoryItemFactory(quantity=0)
        assert item.status == "out_of_stock"
