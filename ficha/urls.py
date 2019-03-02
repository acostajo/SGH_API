from django.urls import path
from ficha import views

urlpatterns = [
    path('fichas/', views.ficha_list),
    path('fichas/<int:pk>/', views.ficha_detail),
    path('pacientes/', views.paciente_list),
    path('pacientes/<int:pk>/', views.paciente_detail),
]
