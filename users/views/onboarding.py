# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/onboarding.py

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response

from users.permissions import IsCEO

from users.serializers.onboarding import (
    EmployeeOnboardingSerializer,
)

from users.services.onboarding import (
    onboard_employee,
)


class EmployeeOnboardingAPIView(GenericAPIView):

    serializer_class = (
        EmployeeOnboardingSerializer
    )

    permission_classes = [
        IsAuthenticated,
        IsCEO,
    ]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        employee = onboard_employee(
            **serializer.validated_data
        )

        return Response(
            {
                "employee_id": employee.id,
                "employee_code": (
                    employee.employee_code
                ),
            },
            status=status.HTTP_201_CREATED,
        )