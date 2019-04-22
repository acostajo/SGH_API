from rest_framework import routers
from .api import EnfermedadViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/enfermedad", EnfermedadViewSet, "enfermedad")

urlpatterns = router.urls
