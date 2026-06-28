# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/role.py

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import Role
from users.serializers.role import RoleSerializer

from users.permissions import StrictModelPermissions


class RoleViewSet(ModelViewSet):

    queryset = Role.objects.all().order_by("name")

    serializer_class = RoleSerializer

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]