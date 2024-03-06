from django.urls import path
from branch_app import views
urlpatterns = [
    path('salbar', views.branch, name='branch')
]
