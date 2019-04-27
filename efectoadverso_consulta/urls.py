from rest_framework import routers
from .api import EfectoAdversoConsultaViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/efecto_adverso_consulta", EfectoAdversoConsultaViewSet, "efecto_adverso_consulta")

urlpatterns = router.urls
