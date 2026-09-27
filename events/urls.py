from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ReservationViewSet

router = DefaultRouter()

router.register(r'events', EventViewSet, basename='event')
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = router.urls

# router.register() → tells router what ViewSet to handle
# router.urls       → gives Django the generated URL patterns
# urlpatterns     → Django uses this variable to know what URLs to handle