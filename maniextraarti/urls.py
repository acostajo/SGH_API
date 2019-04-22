from rest_framework import routers
from .api import ManiExtraArtiViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/manif_extra_art", ManiExtraArtiViewSet, "manif_extra_art")

urlpatterns = router.urls
