from rest_framework import routers
from .viewsets import ArchivoViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/archivo", ArchivoViewSet, "archivo")

urlpatterns = router.urls
