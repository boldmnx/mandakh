
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('queue', views.queue, name='queue'),
    # path('join/', views.join_queue, name='join_queue'),
    # path('serve/', views.serve_user, name='serve_user'),
    path('doctor/', views.read_doctor, name='doctor'),
]
