from django.urls import path
from .views import *

urlpatterns = [
    path('', read_branch, name='readBranch'),
    path('create', create_branch, name='create'),
    path('delete/<id>', delete_branch, name='delete'),
    path('update/<id>', update_branch, name='update'),
    path('detail/<id>', detail_branch, name='detail')
]
