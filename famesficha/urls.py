from django.urls import path
from famesficha import views

urlpatterns = [
    path('famesficha/', views.famesficha_list),
    path('famesficha/<int:pk>/', views.famesficha_detail),
]