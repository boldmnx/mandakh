from django.urls import path
from .views import *
urlpatterns = [
    path('', read, name='read'),
    path('create', create, name='createWorker'),
    path('update/<int:id>', update, name='updateWorker'),
    path('delete/<int:wid>', delete, name='deleteWorker'),
    path('detail/<int:wid>', detail, name='detailWorker')
]
