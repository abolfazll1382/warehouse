from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.serializers import ERPTokenObtainPairSerializer, UserSerializer


class ERPTokenObtainPairView(TokenObtainPairView):
    serializer_class = ERPTokenObtainPairSerializer


class MeView(RetrieveUpdateAPIView):
    """GET /api/v1/auth/me/ — current user's profile. PATCH to self-update
    name/phone (department is admin-managed, not self-service)."""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
