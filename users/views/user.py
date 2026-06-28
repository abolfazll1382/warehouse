# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/user.py

from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from users.serializers.user import UserSerializer

from users.permissions import IsCEO

from users.permissions import StrictModelPermissions

User = get_user_model()


class UserViewSet(ModelViewSet):

    queryset = User.objects.all().order_by("id")

    serializer_class = UserSerializer

    permission_classes = [
        IsAuthenticated,
        IsCEO,
        StrictModelPermissions
    ]