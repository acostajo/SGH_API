from rest_framework import routers
from .api import ConsultaViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/consulta", ConsultaViewSet, "consulta")

urlpatterns = router.urls
