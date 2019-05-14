from rest_framework import routers
from .api import TurnoViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/turno", TurnoViewSet, "turno")

urlpatterns = router.urls
