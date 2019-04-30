from rest_framework import routers
from .api import FameFichaViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/famesficha", FameFichaViewSet, "famesficha")

urlpatterns = router.urls