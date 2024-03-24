from django.urls import path
from branch_app.views import *

urlpatterns = [
    path('', read_branch, name='rBranch'),
    path('updateBranch/<int:bid>', update_branch, name='uBranch'),
    path('deleteBranch/<int:bid>', delete_branch, name='dBranch'),
]
