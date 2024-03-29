from django.shortcuts import render, redirect
from .models import *
from .forms import *
import datetime


def read_news(request):
    if request.method == 'GET':
        newsModels = News.objects.all()
        newsForm = NewsForm()
        return render(request, 'read_news.html', {'nForm': newsForm, 'news': newsModels})
    elif request.method == 'POST':
        subNews = NewsForm(request.POST)
        if subNews.is_valid():
            subNews.save()
        return redirect('/')


def update_news(request, nid):
    if request.method == 'GET':
        newsModel = News.objects.get(id=nid)
        newsForm = NewsForm(instance=newsModel)
        return render(request, 'update.html', {'nform': newsForm})
    elif request.method == 'POST':
        model = News.objects.get(id=nid)
        sub_news = NewsForm(request.POST, instance=model)
        if sub_news.is_valid():
            sub_news.save()
        return redirect('/')


def delete_news(request, nid):
    newsForm = News.objects.get(id=nid)
    newsForm.delete()
    return redirect('/')


def get_news(request, nid):
    newsId = News.objects.get(id=nid)
    return render(request, 'detail.html', {'newsId': newsId})
