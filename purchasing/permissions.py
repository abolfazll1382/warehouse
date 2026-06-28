# MY_DJANGO PROJECTS TRAINING/warehouse_erp/purchasing/permissions.py

from users.permissions import (
    HasGroupPermission,
)


class CanApprovePurchaseOrder(
    HasGroupPermission
):

    required_groups = [
        "CEO",
        "Purchasing",
    ]