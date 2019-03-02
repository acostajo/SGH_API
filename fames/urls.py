from django.urls import path
from fames import views

urlpatterns = [
    path('fames/', views.fames_list),
    path('fames/<int:pk>/', views.fames_detail),
]