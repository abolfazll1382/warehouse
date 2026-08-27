from django.urls import path

from apps.dashboard.views import OverviewView

app_name = "dashboard"

urlpatterns = [
    path("overview/", OverviewView.as_view(), name="overview"),
]
