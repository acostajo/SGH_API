from django.conf.urls import url
from .views import ArchivoUploadView
urlpatterns = [
  url(r'^upload/$', ArchivoUploadView.as_view(), name='file-upload'),
]