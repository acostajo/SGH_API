from django.urls import path
from consulta import views

urlpatterns = [
    path('consultas/', views.consulta_list),
    path('consultas/<int:pk>/', views.consulta_detail),
]