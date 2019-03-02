from django.urls import path
from enfermedad import views

urlpatterns = [
    path('enfermedades/', views.enfermedad_list),
    path('enfermedades/<int:pk>/', views.enfermedad_detail),
]