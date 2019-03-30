from rest_framework import routers
from .api import FamesViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/fames", FamesViewSet, "fames")

urlpatterns = router.urls
