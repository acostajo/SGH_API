from django.urls import path
from manifestacion import views

urlpatterns = [
    path('manifestacion/', views.manifestacion_list),
    path('manifestacion/<int:pk>/', views.manifestacion_detail),
]