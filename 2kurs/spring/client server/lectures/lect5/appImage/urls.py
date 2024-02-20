
from django.urls import path
from appImage.views import image


urlpatterns = [
    path('zurag', image, name='zurag'),
]
