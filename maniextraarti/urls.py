from django.urls import path
from maniextraarti import views

urlpatterns = [
    path('maniextraarti/', views.maniextraarti_list),
    path('maniextraarti/<int:pk>/', views.maniextraarti_detail),
]