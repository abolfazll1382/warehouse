from apps.common.permissions import IsDepartmentStaffOrReadOnly


class IsWarehouseStaffOrReadOnly(IsDepartmentStaffOrReadOnly):
    """Anyone signed in can check stock levels; only inventory (or
    management) can receive/issue stock. Sales/Purchasing need read access
    to this module in day-to-day use, which is why this isn't a strict
    department-only permission like HR/Finance use."""

    department = "inventory"
