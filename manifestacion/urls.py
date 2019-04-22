from rest_framework import routers
from .api import ManifestacionViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/manif", ManifestacionViewSet, "manif")

urlpatterns = router.urls
