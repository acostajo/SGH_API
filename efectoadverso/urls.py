from django.urls import path
from efectoadverso import views

urlpatterns = [
    path('efectoadversos/', views.efectoadverso_list),
    path('efectoadversos/<int:pk>/', views.efectoadverso_detail),
]