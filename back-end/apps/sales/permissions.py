from apps.common.permissions import IsDepartmentStaffOrReadOnly


class IsSalesStaffOrReadOnly(IsDepartmentStaffOrReadOnly):
    department = "sales"
