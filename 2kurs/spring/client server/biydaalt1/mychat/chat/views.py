from django.shortcuts import render, redirect
from .models import Message


def index(request):
    messages = Message.objects.all()
    return render(request, 'chat/index.html', {'messages': messages})


def send_message(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        content = request.POST['content']
        Message.objects.create(sender=sender, content=content)
        return redirect('index')
