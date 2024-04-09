from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        uform = UserForm()
        udform = UserDetailForm()
        return render(request, 'signup.html', {'form1': uform, 'form2': udform})

    elif request.method == 'POST':
        sbForm1 = UserForm(request.POST)
        sbForm2 = UserDetailForm(request.POST)
        if sbForm1.is_valid() and sbForm2.is_valid():
            sbForm2.save()
            sbForm1.save()
        return redirect('/')
