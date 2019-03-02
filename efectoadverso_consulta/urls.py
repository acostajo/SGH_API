from django.urls import path
from efectoadverso_consulta import views

urlpatterns = [
    path('efectoadversos_consulta/', views.efectoadversoconsulta_list),
    path('efectoadversos_consulta/<int:pk>/', views.efectoadversoconsulta_detail),
]