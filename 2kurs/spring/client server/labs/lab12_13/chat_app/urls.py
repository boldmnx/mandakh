from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', register, name='register'),
    path('login', sign, name='login'),
    path('logeduser', loged_user, name='logeduser'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', remove, name='delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

