# MY_DJANGO PROJECTS TRAINING/warehouse_erp/users/views/user_group.py

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from django.contrib.auth import get_user_model

from users.serializers.user_group import UserGroupSerializer



User = get_user_model()


class UserGroupAssignView(GenericAPIView):
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return User.objects.get(pk=self.kwargs["pk"])

    def get(self, request, pk):
        user = self.get_object()
        return Response({
            "user": user.id,
            "groups": [
                {"id": g.id, "name": g.name}
                for g in user.groups.all()
            ]
        })

    def patch(self, request, pk):
        user = self.get_object()

        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.validated_data)

        return Response({
            "message": "User groups updated successfully"
        }, status=status.HTTP_200_OK)