from django.urls import path
from ficha import views

urlpatterns = [
    path('fichas/', views.ficha_list),
    path('fichas/<int:pk>/', views.ficha_detail),
]