from rest_framework import routers

from users.viewsets import v100

router = routers.DefaultRouter()
router.register(r"user", v100.UserViewSet, basename="user-v100")

urlpatterns = router.urls
