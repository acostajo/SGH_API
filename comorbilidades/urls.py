from django.urls import path
from comorbilidades import views

urlpatterns = [
    path('comorbilidades/', views.comorbilidad_list),
    path('comorbilidades/<int:pk>/', views.comorbilidad_detail),
]