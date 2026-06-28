# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/employee_profile.py

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from users.models import EmployeeProfile
from users.serializers.employee_profile import (
    EmployeeProfileSerializer,
)

from users.permissions import StrictModelPermissions

class EmployeeProfileViewSet(ModelViewSet):

    queryset = EmployeeProfile.objects.all()

    serializer_class = EmployeeProfileSerializer

    permission_classes = [
        IsAuthenticated,
        StrictModelPermissions
    ]