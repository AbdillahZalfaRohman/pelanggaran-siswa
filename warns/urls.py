from rest_framework import routers
from .views import WarnsViewSet

router = routers.DefaultRouter()
router.register(r'api/warns', WarmsViewSet, 'warns')

urlpatterns = router.urls