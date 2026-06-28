# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/department.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import Department
from users.serializers.department import (
    DepartmentSerializer,
)

from users.permissions import StrictModelPermissions


class DepartmentViewSet(ModelViewSet):

    queryset = Department.objects.all().order_by(
        "name"
    )

    serializer_class = DepartmentSerializer

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]