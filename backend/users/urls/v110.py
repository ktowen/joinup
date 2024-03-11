from rest_framework import routers

from users.viewsets import v110

router = routers.DefaultRouter()
router.register(r"user", v110.UserViewSet, basename="user-v110")

urlpatterns = router.urls
