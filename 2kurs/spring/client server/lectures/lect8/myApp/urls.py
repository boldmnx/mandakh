from django.urls import path
from .views import *

urlpatterns = [
    path('', read_branch, name='readBranch')
]
