from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profileForm = UserProfileInfoForm(request.POST)
        if form.is_valid() and profileForm.is_valid():
            form.save()
            profileForm.save()
        return redirect('/')
    elif request.method == 'GET':
        form = UserForm()
        profile = UserProfileInfoForm()
        return render(request, 'register.html', {
            'user_form': form, 'profile_form': profile})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        return redirect('/')
