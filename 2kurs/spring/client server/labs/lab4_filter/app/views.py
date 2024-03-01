from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'lab4': {'tom': 'HELLO world',
                        'date': '2023-01-22 04:10:00.678349'}}

    return render(request, 'index.html', context)
