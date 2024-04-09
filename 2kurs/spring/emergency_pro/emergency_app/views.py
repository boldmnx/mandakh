
from django.shortcuts import render, redirect
from .models import User
from .forms import JoinQueueForm


def queue(request):
    users = User.objects.all()
    userCount = len(users)
    return render(request, 'queue.html', {'users': users,'count': userCount})


def join_queue(request):
    if request.method == 'POST':
        form = JoinQueueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('queue')
    else:
        form = JoinQueueForm()
    return render(request, 'add.html', {'form': form})


def serve_user(request):
    if request.method == 'POST':
        if User.objects.exists():
            user = User.objects.first()
            user.delete()
    return redirect('queue')
