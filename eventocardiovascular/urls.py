from rest_framework import routers
from .api import EventoCardiovascularViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/eventocardio", EventoCardiovascularViewSet, "eventocardio")

urlpatterns = router.urls
