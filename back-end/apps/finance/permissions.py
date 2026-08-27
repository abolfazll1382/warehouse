from apps.common.permissions import IsDepartmentStaff


class IsFinanceStaff(IsDepartmentStaff):
    """Financial data — same strict, no-read-only-carve-out rule as HR."""

    department = "finance"
