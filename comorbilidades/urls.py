from rest_framework import routers
from .api import ComorbilidadViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/comorbilidad", ComorbilidadViewSet, "comorbilidad")

urlpatterns = router.urls
