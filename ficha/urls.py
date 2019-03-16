from rest_framework import routers
from .api import FichaViewSet
from django.urls import path
from ficha import views

router = routers.DefaultRouter()
router.register("api/ficha", FichaViewSet, "ficha")

urlpatterns = router.urls
