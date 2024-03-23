from django.urls import path
from branch_app.views import read_branch

urlpatterns = [
    path('', read_branch, name='readBranch'),
]
