
from django.shortcuts import render, redirect
from .models import *
from .forms import JoinQueueForm


def index(request):
    return render(request, 'index.html')


def queue(request):
    users = Customer.objects.all()
    userCount = len(users)
    return render(request, 'queue.html', {'users': users, 'count': userCount})


# def join_queue(request):
#     if request.method == 'POST':
#         form = JoinQueueForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('queue')
#     else:
#         form = JoinQueueForm()
#     return render(request, 'add.html', {'form': form})


# def serve_user(request):
#     if request.method == 'POST':
#         if Customer.objects.exists():
#             user = Customer.objects.first()
#             user.delete()
#     return redirect('queue')


def read_doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})
