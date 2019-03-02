from django.urls import path
from eventocardiovascular import views

urlpatterns = [
    path('eventocardio/', views.eventocardiovascular_list),
    path('eventocardio/<int:pk>/', views.eventocardiovascular_detail),
]