from django.shortcuts import render

# Create your views here.


def help(request):
    return render(request, 'helpApp/help.html', {'help': 'this is help page'})
