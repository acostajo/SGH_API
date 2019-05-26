from rest_framework import routers
from .api import AgendaViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/agenda", AgendaViewSet, "agenda")

urlpatterns = router.urls
