
from app import views
from django.urls import path
from .views import StudentGetCreate, StudentUpdateDelete
urlpatterns = [
    path('', StudentGetCreate.as_view()),
    path('<int:pk>', StudentUpdateDelete.as_view()),
]