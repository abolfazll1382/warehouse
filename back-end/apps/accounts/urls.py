from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.accounts.views import ERPTokenObtainPairView, MeView

app_name = "accounts"

urlpatterns = [
    path("token/", ERPTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="me"),
]
