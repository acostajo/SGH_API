from rest_framework import routers
from .api import TurnoDistViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/turno_dist", TurnoDistViewSet, "turno_dist")

urlpatterns = router.urls
