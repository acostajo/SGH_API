from django.urls import path
from orinasimple import views

urlpatterns = [
    path('orinas/', views.orina_list),
    path('orinas/<int:pk>/', views.orina_detail),
]