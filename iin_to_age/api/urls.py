from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet

app_name = "api"

router = DefaultRouter()
router.register(r"", PersonViewSet, basename="iin")

urlpatterns = [
    path(r"", include(router.urls)),
]
