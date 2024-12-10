
from app import views
from django.urls import path
from .views import StudentGetCreate, StudentUpdateDelete
urlpatterns = [
    path('students/', StudentGetCreate.as_view()),
    path('students/<int:pk>/', StudentUpdateDelete.as_view()),
]