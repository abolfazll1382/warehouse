from apps.common.permissions import IsDepartmentStaff


class IsHRStaff(IsDepartmentStaff):
    """HR data (payroll especially) is sensitive — unlike inventory, there's
    no read-only carve-out for other departments here."""

    department = "hr"
