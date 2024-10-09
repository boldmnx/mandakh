from django.urls import path
from appbackend import views

urlpatterns = [
    path('user/', views.checkService),
]
