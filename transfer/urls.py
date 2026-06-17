from rest_framework.routers import DefaultRouter

from transfer.views.transfer import TransferViewSet


router = DefaultRouter()

router.register(
    "transfers",
    TransferViewSet,
    basename="transfers",
)

urlpatterns = router.urls