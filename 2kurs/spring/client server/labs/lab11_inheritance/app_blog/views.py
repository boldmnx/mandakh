from django.shortcuts import render
from app_blog.models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def read_blog(request, id):
    if request.method == 'GET':
        blog = Blog.objects.filter(btorol=id)
        torol = Torol.objects.get(id=id)
        return render(request, 'blog/read.html', {"blog": blog, 'torol': torol})


def detail_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/detail.html', {'blog': blog})
