# users/views/permission.py

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from users.permissions import IsCEO
from users.serializers.permission import PermissionSerializer, UserPermissionAssignSerializer

User = get_user_model()

class PermissionListView(ListAPIView):
    """
    Returns a list of ALL available permissions (tick boxes) in the system.
    Only the CEO needs to see this list.
    """
    queryset = Permission.objects.all().order_by('content_type__model', 'name')
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsCEO]


class UserPermissionAssignView(GenericAPIView):
    """
    GET: View which permissions a specific user currently has.
    PATCH: Update/Assign permissions to a specific user.
    """
    serializer_class = UserPermissionAssignSerializer
    permission_classes = [IsAuthenticated, IsCEO]

    def get_object(self):
        return User.objects.get(pk=self.kwargs["pk"])

    def get(self, request, pk):
        user = self.get_object()
        return Response({
            "user": user.username,
            "user_permissions": [
                {"id": p.id, "name": p.name}
                for p in user.user_permissions.all()
            ]
        })

    def patch(self, request, pk):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.validated_data)

        return Response({
            "message": f"Permissions updated successfully for {user.username}"
        }, status=status.HTTP_200_OK)