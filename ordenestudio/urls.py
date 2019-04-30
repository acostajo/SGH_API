from rest_framework import routers
from .api import OrdenEstudioViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/ordenestudio", OrdenEstudioViewSet, "ordenestudio")

urlpatterns = router.urls
