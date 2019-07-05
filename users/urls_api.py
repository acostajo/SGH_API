from rest_framework import routers
from .api import UserViewSet
from django.urls import path


router = routers.DefaultRouter()
router.register("api/usuario", UserViewSet, "user")

urlpatterns = router.urls
