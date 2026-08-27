from apps.common.permissions import IsDepartmentStaffOrReadOnly


class IsProductionStaffOrReadOnly(IsDepartmentStaffOrReadOnly):
    department = "production"
