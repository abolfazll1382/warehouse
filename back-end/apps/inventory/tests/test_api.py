import pytest

from apps.inventory.tests.factories import InventoryItemFactory

pytestmark = pytest.mark.django_db


class TestInventoryItemPermissions:
    def test_anonymous_cannot_list_items(self, api_client):
        response = api_client.get("/api/v1/inventory/items/")
        assert response.status_code == 401

    def test_any_authenticated_user_can_read(self, authed_client):
        client, _ = authed_client(department="sales")  # not inventory — read should still work
        InventoryItemFactory()

        response = client.get("/api/v1/inventory/items/")

        assert response.status_code == 200
        assert response.data["count"] == 1

    def test_non_warehouse_staff_cannot_write(self, authed_client):
        client, _ = authed_client(department="sales")

        response = client.post(
            "/api/v1/inventory/categories/", {"name": "Should be rejected"}, format="json"
        )

        assert response.status_code == 403

    def test_warehouse_staff_can_write(self, authed_client):
        client, _ = authed_client(department="inventory")

        response = client.post("/api/v1/inventory/categories/", {"name": "Fittings"}, format="json")

        assert response.status_code == 201

    def test_management_bypasses_department_check(self, authed_client):
        client, _ = authed_client(department="management")

        response = client.post("/api/v1/inventory/categories/", {"name": "Fittings"}, format="json")

        assert response.status_code == 201


class TestInventoryItemIssueEndpoint:
    def test_issue_reduces_quantity_via_api(self, authed_client):
        client, _ = authed_client(department="inventory")
        item = InventoryItemFactory(quantity=40)

        response = client.post(
            f"/api/v1/inventory/items/{item.id}/issue/",
            {"quantity": 15, "reason": "sale"},
            format="json",
        )

        assert response.status_code == 200
        assert response.data["quantity"] == 25

    def test_issue_more_than_available_returns_400(self, authed_client):
        client, _ = authed_client(department="inventory")
        item = InventoryItemFactory(quantity=5)

        response = client.post(
            f"/api/v1/inventory/items/{item.id}/issue/",
            {"quantity": 999, "reason": "sale"},
            format="json",
        )

        assert response.status_code == 400
        assert response.data["code"] == "service_error"
