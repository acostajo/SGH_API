from rest_framework import routers
from .api import EfectoAdversoViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/efecto_adverso", EfectoAdversoViewSet, "efecto_adverso")

urlpatterns = router.urls
