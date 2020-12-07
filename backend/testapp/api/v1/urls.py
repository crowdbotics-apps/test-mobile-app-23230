from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import VehicleViewSet

router = DefaultRouter()
router.register("vehicle", VehicleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
