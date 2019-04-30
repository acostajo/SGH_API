from rest_framework import routers
from .api import EstudioViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/estudio", EstudioViewSet, "estudio")

urlpatterns = router.urls
