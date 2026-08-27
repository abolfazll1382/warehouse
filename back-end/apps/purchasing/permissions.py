from apps.common.permissions import IsDepartmentStaffOrReadOnly


class IsPurchasingStaffOrReadOnly(IsDepartmentStaffOrReadOnly):
    department = "purchasing"
