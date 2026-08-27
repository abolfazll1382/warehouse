from rest_framework.routers import DefaultRouter

from apps.hr.views import EmployeeViewSet, PayrollViewSet

app_name = "hr"

router = DefaultRouter()
router.register("employees", EmployeeViewSet, basename="employee")
router.register("payroll", PayrollViewSet, basename="payroll")

urlpatterns = router.urls
