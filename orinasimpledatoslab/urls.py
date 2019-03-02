from django.urls import path
from orinasimpledatoslab import views

urlpatterns = [
    path('orinasDL/', views.orinaDL_list),
    path('orinasDL/<int:pk>/', views.orinaDL_detail),
]