from rest_framework import routers
from .api import FichaViewSet, PacienteViewSet
from django.urls import path
from ficha import views

router = routers.DefaultRouter()
router.register("api/ficha", FichaViewSet, "ficha")
router.register("api/paciente", PacienteViewSet, "paciente")

urlpatterns = router.urls

