from django.urls import path
from eventocardio_ficha import views

urlpatterns = [
    path('eventocardio_ficha/', views.eventocardiovascularficha_list),
    path('eventocardio_ficha/<int:pk>/', views.eventocardiovascularficha_detail),
]