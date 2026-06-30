# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/urls.py

from django.urls import path

from rest_framework.routers import DefaultRouter

from users.views.department import (
    DepartmentViewSet,
)

from users.views.employee_profile import (
    EmployeeProfileViewSet,
)

from users.views.role import RoleViewSet

from users.views.employee_role import (
    EmployeeRoleViewSet,
)

from users.views.user import UserViewSet

from users.views.onboarding import (
    EmployeeOnboardingAPIView,
)

from users.views.group import GroupViewSet
from users.views.user_group import UserGroupAssignView
from users.views.permission import PermissionListView, UserPermissionAssignView
from users.views.customer_auth import (
    CustomerRegistrationView,
    VerifyEmailView,
    ResendVerificationView,
)


router = DefaultRouter()

router.register(
    "users",
    UserViewSet,
    basename="users",
)

router.register(
    "departments",
    DepartmentViewSet,
    basename="departments",
)

router.register(
    "employees",
    EmployeeProfileViewSet,
    basename="employees",
)

router.register(
    "roles",
    RoleViewSet,
    basename="roles",
)

router.register(
    "employee-roles",
    EmployeeRoleViewSet,
    basename="employee-roles",
)

router.register(
    "groups",
    GroupViewSet,
    basename="groups",
)
urlpatterns = [
    *router.urls,
    
    path(
        "onboarding/",
        EmployeeOnboardingAPIView.as_view(),
    ),

    path(
        "user/<int:pk>/groups/",
        UserGroupAssignView.as_view(),
        name="user-groups",
    ),

    path(
        "permissions/", 
        PermissionListView.as_view(), 
        name="permissions-list"
    ),

    # 2. Endpoint to assign permissions to a user
    path(
        "user/<int:pk>/permissions/", 
        UserPermissionAssignView.as_view(), 
        name="user-permissions-assign"
    ),

    path(
        "register/",
        CustomerRegistrationView.as_view(),
        name="customer-register",
    ),

    path(
        "verify/",
        VerifyEmailView.as_view(),
        name="customer-verify",
    ),

    path(
        "resend/",
        ResendVerificationView.as_view(),
        name="customer-resend",
    ),
]