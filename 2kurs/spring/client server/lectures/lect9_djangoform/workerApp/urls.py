from django.urls import path, include
from .views import workerCreate

urlpatterns = [
    path('', workerCreate, name='createWorker')
]
