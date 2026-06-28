# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/group.py

from django.contrib.auth.models import Group

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from users.serializers.group import (
    GroupSerializer,
)

from users.permissions import StrictModelPermissions


class GroupViewSet(
    ModelViewSet
):

    queryset = Group.objects.all()

    serializer_class = (
        GroupSerializer
    )

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]