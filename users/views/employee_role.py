# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/employee_role.py

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from users.models import EmployeeRole
from users.serializers.employee_role import (
    EmployeeRoleSerializer,
)

from users.permissions import StrictModelPermissions


class EmployeeRoleViewSet(ModelViewSet):

    queryset = EmployeeRole.objects.all()

    serializer_class = (
        EmployeeRoleSerializer
    )

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]