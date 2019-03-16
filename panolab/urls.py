from rest_framework import routers
from .api import PanolabViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/panolab", PanolabViewSet, "panolab")

urlpatterns = router.urls
