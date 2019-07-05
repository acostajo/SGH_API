from django.conf.urls import url

from .views import UserObtainAuthToken

urlpatterns = [
    url('authenticate/', UserObtainAuthToken.as_view()),
]