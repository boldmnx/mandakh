from django.urls import path
from .views import read_worker

urlpatterns = [
    path('worker', read_worker, name='readWorker')
]
