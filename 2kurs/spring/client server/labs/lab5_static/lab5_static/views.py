from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def our_works(request):
    return render(request, 'our_works.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
