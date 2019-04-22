from rest_framework import routers
from .api import EventoCardiovascularFichaViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/eventocardio_ficha", EventoCardiovascularFichaViewSet, "eventocardio_ficha")

urlpatterns = router.urls
