from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsDepartmentStaff(BasePermission):
    """
    Base class for "only people in department X (or management/superusers)
    may use this endpoint" rules. Subclass per-app instead of instantiating
    directly:

        class IsHRStaff(IsDepartmentStaff):
            department = "hr"

    Management and superusers always pass, everyone else must belong to the
    exact department the view requires.
    """

    department: str | None = None
    message = "You do not have access to this module."

    def has_permission(self, request, view):
        user = request.user
        if not (user and user.is_authenticated):
            return False
        if user.is_superuser or user.department == "management":
            return True
        return user.department == self.department


class IsDepartmentStaffOrReadOnly(IsDepartmentStaff):
    """Same rule, but any authenticated user may read (GET/HEAD/OPTIONS)."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return super().has_permission(request, view)
