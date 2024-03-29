from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def read(request):
    products = Product.objects.all()
    return render(request, 'read.html', {'products': products})


def create(request, pid):
    pass


def update(request, pid):
    if request.method == 'GET':
        product = Product.objects.get(id=pid)
        pForm = ProductForm(instance=product)

        return render(request, 'update.html', {'pForm': pForm})
    elif request.method == 'POST':
        sub_product = ProductForm(request.POST)
        if sub_product.is_valid():
            sub_product.save()
        return redirect('')


def delete(request):
    pass
