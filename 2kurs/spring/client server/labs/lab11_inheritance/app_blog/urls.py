
from django.urls import path, include
from app_blog.views import *


app_name = 'blog'
urlpatterns = [
    path('<int:id>', read_blog, name='readBlog'),
    path('detail/<int:id>', detail_blog, name='detailBlog'),
]
